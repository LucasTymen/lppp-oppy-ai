"""
Crée la landing ORSYS (Aboubakar Timite) à partir du JSON existant.
Usage : python manage.py create_landing_orsys
Idempotent : n'écrase pas si la landing existe déjà (met à jour le content_json si --update).

Thème ORSYS : charte orsys.fr extraite par CSS Vampire (fond sombre, Lato, bleu).
Stratégie : Volume — signaux faibles, restructuration, conformité IA Act.
Contact : Aboubakar Timite (profil opérationnel).
"""
import json
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.landing_pages.models import LandingPage
from apps.landing_pages.themes import THEME_CSS_ORSYS, THEME_ORSYS


class Command(BaseCommand):
    help = "Crée la landing ORSYS (Aboubakar Timite) depuis docs/contacts/orsys/landing-proposition-aboubakar.json"

    def add_arguments(self, parser):
        parser.add_argument(
            "--update",
            action="store_true",
            help="Met à jour content_json si la landing existe déjà.",
        )
        parser.add_argument(
            "--publish",
            action="store_true",
            help="Crée ou met à jour en publiée (is_published=True).",
        )

    def handle(self, *args, **options):
        json_path = (
            Path(settings.BASE_DIR)
            / "docs"
            / "contacts"
            / "orsys"
            / "landing-proposition-aboubakar.json"
        )
        if not json_path.exists():
            self.stderr.write(self.style.ERROR(f"Fichier introuvable : {json_path}"))
            return

        with open(json_path, encoding="utf-8") as f:
            content = json.load(f)

        # Injecter le thème ORSYS (couleurs orsys.fr)
        content["theme"] = THEME_ORSYS
        content["theme_css"] = THEME_CSS_ORSYS

        title = content.get("page_title") or "Optimisation Growth pour ORSYS"
        slug = "orsys"
        prospect_company = "ORSYS"
        prospect_name = "Aboubakar Timite"
        sector = "formation"
        category = "proposition"
        template_key = "proposition"

        User = get_user_model()
        created_by = User.objects.filter(is_superuser=True).first()

        lp, created = LandingPage.objects.get_or_create(
            slug=slug,
            defaults={
                "title": title,
                "prospect_company": prospect_company,
                "prospect_name": prospect_name,
                "sector": sector,
                "category": category,
                "template_key": template_key,
                "content_json": content,
                "is_published": options["publish"],
                "created_by": created_by,
            },
        )
        if created:
            lp.content_json = content
            lp.save()
            self.stdout.write(self.style.SUCCESS(f"Landing créée : {lp.title} (slug={slug})"))
        else:
            if options["update"]:
                lp.content_json = content
                lp.title = title
                lp.prospect_company = prospect_company
                lp.prospect_name = prospect_name
                lp.sector = sector
                lp.category = category
                lp.template_key = template_key
                if options["publish"]:
                    lp.is_published = True
                lp.save()
                self.stdout.write(self.style.SUCCESS(f"Landing mise à jour : {lp.title}"))
            else:
                self.stdout.write(
                    self.style.WARNING(f"Landing déjà existante : {lp.title}. Utilisez --update pour mettre à jour.")
                )
                return

        self.stdout.write(f"  URL : /p/{slug}/")
        self.stdout.write(f"  Rapport : /p/{slug}/rapport/")
