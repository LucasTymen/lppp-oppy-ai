"""
Pousse les documents de data/flowise/ vers le Document Store Flowise (API).
Usage :
  python manage.py flowise_push_documents
  python manage.py flowise_push_documents --file data/flowise/maisons-alfort-contenu.txt
Variables d'environnement : FLOWISE_URL, FLOWISE_DOCUMENT_STORE_ID, FLOWISE_API_KEY (optionnel).
Voir docs/base-de-connaissances/flowise-push-documents-informatique.md
"""
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from apps.scraping.flowise_client import get_flowise_config, push_file_to_flowise

BASE_DIR = Path(settings.BASE_DIR)
DEFAULT_FLOWISE_DIR = BASE_DIR / "data" / "flowise"


class Command(BaseCommand):
    help = "Pousse les fichiers de data/flowise/ vers le Document Store Flowise (API)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--file", "-f",
            type=str,
            default=None,
            help="Fichier unique à pousser (ex. data/flowise/maisons-alfort-contenu.txt). Sinon tous les .txt de data/flowise/.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Afficher les fichiers qui seraient envoyés sans appeler l'API.",
        )

    def handle(self, *args, **options):
        base_url, store_id, api_key = get_flowise_config()
        if not store_id:
            self.stdout.write(
                self.style.ERROR(
                    "FLOWISE_DOCUMENT_STORE_ID manquant. "
                    "Renseigne-le dans .env (UUID du Document Store Flowise)."
                )
            )
            return

        flowise_dir = DEFAULT_FLOWISE_DIR
        if not flowise_dir.exists():
            self.stdout.write(self.style.WARNING(f"Répertoire absent : {flowise_dir}"))
            return

        if options["file"]:
            path = Path(options["file"])
            if not path.is_absolute():
                path = BASE_DIR / path
            files_to_send = [path] if path.exists() else []
        else:
            files_to_send = sorted(flowise_dir.glob("*.txt"))

        if not files_to_send:
            self.stdout.write(self.style.WARNING("Aucun fichier .txt à envoyer."))
            return

        if options["dry_run"]:
            for p in files_to_send:
                self.stdout.write(f"  [dry-run] {p}")
            self.stdout.write(self.style.SUCCESS(f"{len(files_to_send)} fichier(s) seraient envoyés vers {base_url}"))
            return

        self.stdout.write(f"Envoi vers {base_url} (store {store_id[:8]}…)")
        for file_path in files_to_send:
            result = push_file_to_flowise(file_path, base_url, store_id, api_key)
            if result and "error" in result:
                self.stdout.write(self.style.ERROR(f"  {file_path.name}: {result['error']}"))
            else:
                added = result.get("numAdded", result.get("addedDocs", []))
                if isinstance(added, list):
                    added = len(added)
                self.stdout.write(self.style.SUCCESS(f"  {file_path.name}: ok (numAdded={added})"))
