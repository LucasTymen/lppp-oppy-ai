"""
Scrape les pages clés de maisons-alfort.fr pour le Concierge IA (RAG Flowise).
Usage :
  python manage.py scrape_maisons_alfort
  python manage.py scrape_maisons_alfort --output /tmp/maisons-alfort-pages.json
  python manage.py scrape_maisons_alfort --urls "https://www.maisons-alfort.fr/autre-page"
Sortie : JSON sur stdout ou dans le fichier --output.
"""
import json
from pathlib import Path

from django.core.management.base import BaseCommand

from apps.scraping.concierge import scrape_urls, DEFAULT_MAISONS_ALFORT_URLS


class Command(BaseCommand):
    help = "Scrape les pages Maisons-Alfort (ou URLs fournies) pour le RAG Concierge IA."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output", "-o",
            type=str,
            default=None,
            help="Fichier de sortie JSON (sinon stdout).",
        )
        parser.add_argument(
            "--urls",
            type=str,
            nargs="*",
            default=None,
            help="URLs à scraper (sinon URLs par défaut Maisons-Alfort).",
        )

    def handle(self, *args, **options):
        urls = options.get("urls") or DEFAULT_MAISONS_ALFORT_URLS
        pages = scrape_urls(urls)
        data = {"status": "ok", "pages": pages}
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        output = options.get("output")
        if output:
            Path(output).parent.mkdir(parents=True, exist_ok=True)
            Path(output).write_text(json_str, encoding="utf-8")
            self.stdout.write(self.style.SUCCESS(f"Écrit {len(pages)} pages dans {output}"))
        else:
            self.stdout.write(json_str)
