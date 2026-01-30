"""
Tâches Celery pour enrichment (scraping, mise à jour données).
Pilotables par Flowise / N8N via webhook qui déclenche ces tâches.

Stratégie anti-blocage (Google/LinkedIn) : une tâche = un outil.
- enrich_prospect_single_source : une source OSINT par tâche, résultat partiel en Redis.
- enrich_prospect_merge_and_save : fusion des partiels + intelligence métier (qualité, score).
- enrich_prospect_decomposed : enchaîne N sources puis merge (recommandé en prod).
Voir docs/base-de-connaissances/strategie-enrichissement.md.
"""
import json
import logging
from typing import Any, Dict, List

from celery import shared_task
from django.conf import settings

from .osint_sources import get_source, merge_enriched_results, SOURCE_REGISTRY
from .pipelines import run_enrichment_pipeline

logger = logging.getLogger(__name__)

REDIS_PARTIAL_PREFIX = "lppp:enriched:partial:"
REDIS_PARTIAL_TTL = 86400  # 24h


def _get_redis():
    """Connexion Redis pour résultats partiels (DB 0 ou REDIS_URL)."""
    import redis
    url = getattr(settings, "REDIS_URL", None) or "redis://redis:6379/0"
    return redis.Redis.from_url(url, decode_responses=True)


@shared_task(name="apps.scraping.enriched.enrich_prospect_single_source")
def enrich_prospect_single_source(prospect_id: int, source_name: str):
    """
    Lance une seule source OSINT pour un prospect (une tâche = un outil).
    Stocke le résultat partiel en Redis pour fusion ultérieure.
    Anti-blocage : évite les patterns bot Google/LinkedIn.
    """
    from apps.campaigns.models import Prospect

    logger.info("Enrich prospect id=%s single source=%s", prospect_id, source_name)
    try:
        prospect = Prospect.objects.get(pk=prospect_id)
    except Prospect.DoesNotExist:
        logger.warning("Prospect id=%s not found", prospect_id)
        return {"prospect_id": prospect_id, "source": source_name, "status": "not_found"}

    source = get_source(source_name)
    if not source:
        logger.warning("Source %s unknown", source_name)
        return {"prospect_id": prospect_id, "source": source_name, "status": "unknown_source"}

    try:
        result = source.enrich(
            company_name=prospect.company_name or "",
            contact_name=prospect.contact_name or None,
            email=prospect.email or None,
            domain=None,
        )
    except Exception as e:
        logger.warning("Source %s failed for prospect %s: %s", source_name, prospect_id, e)
        return {"prospect_id": prospect_id, "source": source_name, "status": "error", "error": str(e)}

    r = _get_redis()
    key = f"{REDIS_PARTIAL_PREFIX}{prospect_id}"
    r.hset(key, source_name, json.dumps(result, default=str))
    r.expire(key, REDIS_PARTIAL_TTL)
    logger.info("Prospect id=%s partial stored for source=%s", prospect_id, source_name)
    return {"prospect_id": prospect_id, "source": source_name, "status": "ok"}


@shared_task(name="apps.scraping.enriched.enrich_prospect_merge_and_save")
def enrich_prospect_merge_and_save(partial_task_results: List[Dict[str, Any]] = None):
    """
    Fusionne les résultats partiels (Redis) pour un prospect, applique
    l'intelligence métier (qualité, score), sauvegarde enriched_data sur Prospect.
    Collaboration avec apps.intelligence.
    Appelée en callback chord : reçoit la liste des retours des tâches single_source.
    """
    from apps.campaigns.models import Prospect
    from apps.intelligence.quality import prospect_completeness
    from apps.intelligence.scoring import score_prospect

    partial_task_results = partial_task_results or []
    prospect_id = None
    if partial_task_results and isinstance(partial_task_results[0], dict):
        prospect_id = partial_task_results[0].get("prospect_id")
    logger.info("Merge and save prospect id=%s (from %s partial tasks)", prospect_id, len(partial_task_results))

    if not prospect_id:
        return {"prospect_id": prospect_id, "status": "no_prospect_id"}

    try:
        prospect = Prospect.objects.get(pk=prospect_id)
    except Prospect.DoesNotExist:
        logger.warning("Prospect id=%s not found", prospect_id)
        return {"prospect_id": prospect_id, "status": "not_found"}

    r = _get_redis()
    key = f"{REDIS_PARTIAL_PREFIX}{prospect_id}"
    raw = r.hgetall(key)
    if not raw:
        logger.warning("No partial data for prospect id=%s", prospect_id)
        return {"prospect_id": prospect_id, "status": "no_partial_data"}

    results = []
    for _k, v in raw.items():
        try:
            results.append(json.loads(v))
        except (json.JSONDecodeError, TypeError):
            continue
    r.delete(key)

    merged = merge_enriched_results(results)
    enriched_data = {
        "company": merged.get("company") or {},
        "contact": merged.get("contact") or {},
    }
    company_name = prospect.company_name or ""
    contact_name = prospect.contact_name or ""
    email = prospect.email or ""
    if not enriched_data["company"].get("name") and company_name:
        enriched_data["company"]["name"] = company_name
    if not enriched_data["contact"].get("name") and contact_name:
        enriched_data["contact"]["name"] = contact_name
    if not enriched_data["contact"].get("email") and email:
        enriched_data["contact"]["email"] = email

    comp = prospect_completeness(
        company_name=company_name,
        contact_name=contact_name or "",
        email=email or "",
        enriched_data=enriched_data,
    )
    score = score_prospect(
        has_email=comp["has_email"],
        has_company=comp["has_company"],
        has_contact_name=comp["has_contact"],
        enriched_completeness=comp["enriched_completeness"],
    )

    prospect.enriched_data = enriched_data
    prospect.save(update_fields=["enriched_data"])
    logger.info("Prospect id=%s merged and saved score=%.0f", prospect_id, score)
    return {"prospect_id": prospect_id, "status": "ok", "score": score}


@shared_task(name="apps.scraping.enriched.enrich_prospect_decomposed")
def enrich_prospect_decomposed(prospect_id: int, source_names: List[str] = None):
    """
    Flux décomposé : lance une tâche par source, puis merge + intelligence.
    Recommandé en prod pour éviter blocages Google/LinkedIn.
    source_names : liste des noms (ex. ["placeholder"]). Si None, utilise SOURCE_REGISTRY.
    """
    from celery import chord

    source_names = source_names or list(SOURCE_REGISTRY.keys())
    if not source_names:
        logger.warning("No sources for prospect id=%s", prospect_id)
        return {"prospect_id": prospect_id, "status": "no_sources"}

    header = [enrich_prospect_single_source.s(prospect_id, name) for name in source_names]
    chord(header)(enrich_prospect_merge_and_save.s())
    logger.info("Prospect id=%s decomposed enrichment started (%s sources)", prospect_id, len(source_names))
    return {"prospect_id": prospect_id, "status": "started", "sources": source_names}


@shared_task(name="apps.scraping.enriched.enrich_prospect")
def enrich_prospect(prospect_id: int, sources: list = None):
    """
    Enrichit un prospect (données entreprise / contact) via le pipeline OSINT,
    puis sauvegarde enriched_data sur le modèle Prospect.
    """
    sources = sources or []
    logger.info("Enrich prospect id=%s sources=%s", prospect_id, sources)
    from apps.campaigns.models import Prospect

    try:
        prospect = Prospect.objects.get(pk=prospect_id)
    except Prospect.DoesNotExist:
        logger.warning("Prospect id=%s not found", prospect_id)
        return {"prospect_id": prospect_id, "status": "not_found", "sources": sources}

    payload = run_enrichment_pipeline(
        company_name=prospect.company_name or "",
        contact_name=prospect.contact_name or None,
        email=prospect.email or None,
        domain=None,
        sources=None,
    )
    prospect.enriched_data = payload.get("enriched_data") or {}
    prospect.save(update_fields=["enriched_data"])
    logger.info("Prospect id=%s enriched score=%.0f", prospect_id, payload.get("score", 0))
    return {
        "prospect_id": prospect_id,
        "status": "ok",
        "score": payload.get("score"),
        "sources": sources,
    }


@shared_task(name="apps.scraping.enriched.enrich_batch")
def enrich_batch(prospect_ids: list, sources: list = None):
    """
    Enrichit une liste de prospects (idéal pour webhook N8N avec liste d’IDs).
    Chaque ID déclenche enrich_prospect (séquentiel pour respecter rate limit).
    """
    results = []
    for pid in prospect_ids[:50]:  # guide-rail : max 50 par batch
        if not isinstance(pid, int):
            try:
                pid = int(pid)
            except (TypeError, ValueError):
                continue
        result = enrich_prospect(pid, sources=sources or [])
        results.append(result)
    return {"processed": len(results), "results": results}
