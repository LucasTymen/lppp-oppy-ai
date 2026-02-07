"""
Diagnostic « écran vide » : vérifie que l’URL d’embed est construite et (optionnel) que Flowise répond.
Stratégie : écran vide = souvent URL d’embed (.env + restart web) ou Flowise pas sur 3010.
Usage :
  python manage.py check_flowise_embed
  python manage.py check_flowise_embed --ping
Voir docs/base-de-connaissances/segmentations/2026-01-30-strategie-chatbot-ecran-vide-et-flux.md
"""
import os
import urllib.error
import urllib.request

from django.core.management.base import BaseCommand

from apps.scraping.flowise_client import get_flowise_chat_embed_url


class Command(BaseCommand):
    help = "Vérifie FLOWISE_URL, FLOWISE_CHATFLOW_ID et l’URL d’embed du chatbot (stratégie écran vide)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--ping",
            action="store_true",
            help="Tester la connexion à Flowise (GET sur la base URL).",
        )

    def handle(self, *args, **options):
        flowise_url = (os.environ.get("FLOWISE_URL") or "").strip()
        chatflow_id = (os.environ.get("FLOWISE_CHATFLOW_ID") or "").strip()

        self.stdout.write("--- Diagnostic embed chatbot (port LPPP 3010) ---")
        self.stdout.write(f"  FLOWISE_URL       = {repr(flowise_url) or '(vide → fallback localhost:3010)'}")
        self.stdout.write(f"  FLOWISE_CHATFLOW_ID = {repr(chatflow_id) or '(vide → pas d’URL embed)'}")

        embed_url = get_flowise_chat_embed_url()
        if embed_url:
            self.stdout.write(self.style.SUCCESS(f"  URL d’embed       = {embed_url}"))
        else:
            self.stdout.write(
                self.style.WARNING(
                    "  URL d’embed       = (vide) → la landing affichera « Chat en cours de configuration »."
                )
            )
            self.stdout.write(
                "  → Renseigner FLOWISE_CHATFLOW_ID dans .env (ID depuis Flowise → chatflow → Embed), puis : docker compose restart web"
            )

        if not flowise_url:
            self.stdout.write(
                "  → Pour forcer l’URL navigateur : FLOWISE_URL=http://localhost:3010 dans .env, puis : docker compose restart web"
            )

        if options.get("ping"):
            base = (flowise_url or "http://localhost:3010").rstrip("/")
            self.stdout.write(f"\n--- Test connexion GET {base} ---")
            try:
                req = urllib.request.Request(base, method="GET")
                with urllib.request.urlopen(req, timeout=5) as resp:
                    self.stdout.write(self.style.SUCCESS(f"  Réponse {resp.status}"))
            except urllib.error.URLError as e:
                self.stdout.write(self.style.ERROR(f"  Erreur : {e.reason}"))
                self.stdout.write("  → Vérifier que Flowise tourne : docker compose ps (lppp_flowise), http://localhost:3010/")
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  Erreur : {e}"))

        self.stdout.write("")
