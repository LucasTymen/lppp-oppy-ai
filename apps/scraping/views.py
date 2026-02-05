"""
API d’enrichissement pour N8N / Flowise.
Webhooks POST : enrichir un prospect par ID, une liste d’IDs, ou une liste de lignes (company, contact, email).
"""
import json
import logging
from pathlib import Path

from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator

from apps.campaigns.models import Prospect
from apps.scraping.enriched.pipelines import run_enrichment_pipeline, run_batch_enrichment
from apps.scraping.enriched.tasks import enrich_prospect, enrich_batch
from apps.scraping.enriched.security import enrichment_rate_limiter

from apps.scraping.concierge import scrape_urls, DEFAULT_MAISONS_ALFORT_URLS
from apps.scraping.flowise_client import get_flowise_config, push_file_to_flowise

logger = logging.getLogger(__name__)

BASE_DIR = Path(settings.BASE_DIR)
DEFAULT_FLOWISE_DIR = BASE_DIR / "data" / "flowise"
DEFAULT_CONCIERGE_FILENAME = "maisons-alfort-contenu.txt"


def _parse_json_body(request):
    """Parse JSON body ; retourne None si vide ou invalide."""
    if not request.body:
        return None
    try:
        return json.loads(request.body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return None


@method_decorator(csrf_exempt, name="dispatch")
class EnrichWebhookView(View):
    """
    POST /api/enriched/enrich
    Body JSON :
    - { "prospect_id": 1 } → enrichit le prospect 1 (async Celery), retourne { "status": "queued", "prospect_id": 1 }
    - { "prospect_ids": [1, 2, 3] } → enrichit les prospects (async Celery), retourne { "status": "queued", "count": 3 }
    - { "sync": true, "prospect_id": 1 } → enrichit en synchrone et retourne le payload enrichi
    - { "rows": [ { "company_name": "Acme", "contact_name": "John", "email": "j@acme.com" } ] } → enrichit les lignes en sync, retourne liste de payloads
    Guide-rail : max 50 lignes ou IDs par requête.
    """

    def post(self, request):
        data = _parse_json_body(request)
        if not data or not isinstance(data, dict):
            return JsonResponse(
                {"error": "Body JSON attendu (prospect_id, prospect_ids, ou rows)"},
                status=400,
            )
        # Rate limiting (inspiré SquidResearch enrichment/security)
        identifier = request.META.get("REMOTE_ADDR", "anonymous")
        allowed, info = enrichment_rate_limiter.is_allowed(identifier, "enrich_api")
        if not allowed:
            return JsonResponse(
                {"error": "rate_limit_exceeded", "detail": info},
                status=429,
            )

        # Un seul prospect en async
        if "prospect_id" in data and "rows" not in data and "prospect_ids" not in data:
            pid = data.get("prospect_id")
            try:
                pid = int(pid)
            except (TypeError, ValueError):
                return JsonResponse({"error": "prospect_id doit être un entier"}, status=400)
            if data.get("sync"):
                try:
                    prospect = Prospect.objects.get(pk=pid)
                except Prospect.DoesNotExist:
                    return JsonResponse({"error": "Prospect non trouvé", "prospect_id": pid}, status=404)
                payload = run_enrichment_pipeline(
                    company_name=prospect.company_name or "",
                    contact_name=prospect.contact_name or None,
                    email=prospect.email or None,
                )
                prospect.enriched_data = payload.get("enriched_data") or {}
                prospect.save(update_fields=["enriched_data"])
                return JsonResponse({"status": "ok", "payload": payload})
            enrich_prospect.delay(pid, sources=data.get("sources") or [])
            return JsonResponse({"status": "queued", "prospect_id": pid})

        # Liste d’IDs en async
        if "prospect_ids" in data and "rows" not in data:
            pids = data.get("prospect_ids", [])
            if not isinstance(pids, list):
                return JsonResponse({"error": "prospect_ids doit être une liste"}, status=400)
            pids = [int(x) for x in pids[:50] if x is not None]
            enrich_batch.delay(pids, sources=data.get("sources") or [])
            return JsonResponse({"status": "queued", "count": len(pids)})

        # Lignes (rows) en synchrone : idéal pour N8N qui envoie une liste de prospects
        if "rows" in data:
            rows = data.get("rows", [])
            if not isinstance(rows, list):
                return JsonResponse({"error": "rows doit être une liste"}, status=400)
            rows = rows[:50]
            payloads = run_batch_enrichment(
                rows,
                company_key=data.get("company_key", "company_name"),
                contact_key=data.get("contact_key", "contact_name"),
                email_key=data.get("email_key", "email"),
                domain_key=data.get("domain_key"),
            )
            return JsonResponse({"status": "ok", "count": len(payloads), "payloads": payloads})

        return JsonResponse(
            {"error": "Indiquer prospect_id, prospect_ids, ou rows dans le body"},
            status=400,
        )


@csrf_exempt
@require_http_methods(["POST"])
def enrich_single_sync_view(request):
    """
    POST /api/enriched/enrich-one
    Body : { "company_name": "", "contact_name": "", "email": "" }
    Enrichit une ligne en synchrone et retourne le payload (sans sauvegarder en base).
    Pratique pour tester ou pour un robot Flowise/N8N qui envoie une ligne.
    """
    data = _parse_json_body(request)
    if not data or not isinstance(data, dict):
        return JsonResponse({"error": "Body JSON attendu"}, status=400)
    payload = run_enrichment_pipeline(
        company_name=data.get("company_name") or data.get("company") or "",
        contact_name=data.get("contact_name") or data.get("contact"),
        email=data.get("email"),
        domain=data.get("domain"),
    )
    return JsonResponse({"status": "ok", "payload": payload})


@method_decorator(csrf_exempt, name="dispatch")
class ConciergeScrapeView(View):
    """
    GET ou POST /api/concierge/scrape
    - GET : scrape les URLs par défaut (Maisons-Alfort).
    - POST body JSON : { "urls": ["https://...", ...] } (max 20 URLs).
    Retourne : { "status": "ok", "pages": [ { "url": "...", "text": "...", "error": null } ] }.
    Pour alimenter le RAG Flowise (Quick Win Concierge IA).
    """

    def get(self, request):
        pages = scrape_urls(DEFAULT_MAISONS_ALFORT_URLS)
        return JsonResponse({"status": "ok", "pages": pages})

    def post(self, request):
        data = _parse_json_body(request)
        urls = None
        if data and isinstance(data, dict) and "urls" in data:
            urls = data.get("urls", [])
        if not urls or not isinstance(urls, list):
            return JsonResponse(
                {"error": "Body JSON attendu : { \"urls\": [ \"https://...\", ... ] }"},
                status=400,
            )
        urls = urls[:20]  # max 20 URLs
        pages = scrape_urls(urls)
        return JsonResponse({"status": "ok", "pages": pages})


@method_decorator(csrf_exempt, name="dispatch")
class ConciergeSaveContentView(View):
    """
    POST /api/concierge/save-content
    Body JSON : { "pages": [ { "url": "...", "text": "..." } ] } ou { "content": "texte brut" }.
    Écrit le contenu dans data/flowise/<filename> (défaut : maisons-alfort-contenu.txt).
    Query : ?filename=autre.txt pour un autre fichier (nom simple, pas de path).
    Pour n8n après le scrape : appeler scrape puis save-content puis push-to-flowise.
    """

    def post(self, request):
        data = _parse_json_body(request)
        if not data or not isinstance(data, dict):
            return JsonResponse(
                {"error": "Body JSON attendu : { \"pages\": [...] } ou { \"content\": \"...\" }"},
                status=400,
            )
        filename = request.GET.get("filename", DEFAULT_CONCIERGE_FILENAME)
        if "/" in filename or "\\" in filename or not filename.endswith(".txt"):
            filename = DEFAULT_CONCIERGE_FILENAME
        if not DEFAULT_FLOWISE_DIR or not DEFAULT_FLOWISE_DIR.exists():
            return JsonResponse(
                {"error": "Répertoire data/flowise non configuré ou absent"},
                status=500,
            )
        file_path = DEFAULT_FLOWISE_DIR / filename
        if "content" in data and isinstance(data["content"], str):
            content = data["content"]
        elif "pages" in data and isinstance(data["pages"], list):
            parts = []
            for p in data["pages"]:
                if isinstance(p, dict) and p.get("text"):
                    parts.append(p.get("text", ""))
            content = "\n\n".join(parts)
        else:
            return JsonResponse(
                {"error": "Indiquer \"content\" (string) ou \"pages\" (liste avec .text)"},
                status=400,
            )
        try:
            file_path.write_text(content, encoding="utf-8")
        except OSError as e:
            logger.exception("Concierge save-content write failed: %s", e)
            return JsonResponse({"error": f"Écriture impossible : {e}"}, status=500)
        return JsonResponse({"status": "ok", "file": filename, "size": len(content)})


@method_decorator(csrf_exempt, name="dispatch")
class ConciergePushToFlowiseView(View):
    """
    POST /api/concierge/push-to-flowise
    Pousse le fichier data/flowise/<filename> vers le Document Store Flowise.
    Query : ?filename=maisons-alfort-contenu.txt (défaut).
    Prérequis : FLOWISE_URL, FLOWISE_DOCUMENT_STORE_ID dans .env.
    """

    def post(self, request):
        filename = request.GET.get("filename", DEFAULT_CONCIERGE_FILENAME)
        if "/" in filename or "\\" in filename or not filename.endswith(".txt"):
            filename = DEFAULT_CONCIERGE_FILENAME
        if not DEFAULT_FLOWISE_DIR or not DEFAULT_FLOWISE_DIR.exists():
            return JsonResponse(
                {"error": "Répertoire data/flowise non configuré ou absent"},
                status=500,
            )
        file_path = DEFAULT_FLOWISE_DIR / filename
        if not file_path.exists():
            return JsonResponse(
                {"error": f"Fichier absent : {filename}. Appeler save-content avant."},
                status=400,
            )
        base_url, store_id, api_key = get_flowise_config()
        if not store_id:
            return JsonResponse(
                {"error": "FLOWISE_DOCUMENT_STORE_ID manquant dans .env"},
                status=500,
            )
        result = push_file_to_flowise(file_path, base_url, store_id, api_key)
        if result.get("error"):
            return JsonResponse(
                {"error": result["error"], "status_code": result.get("status_code")},
                status=502,
            )
        added = result.get("numAdded", result.get("addedDocs", []))
        if isinstance(added, list):
            added = len(added)
        return JsonResponse({"status": "ok", "file": filename, "numAdded": added})
