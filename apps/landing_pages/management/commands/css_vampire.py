"""
Commande CSS Vampire : visite le site de la société cible et extrait
polices, couleurs, logo (et optionnellement fond) pour reproduire leur style
sur la landing et mettre le prospect à l'aise.

Usage :
  python manage.py css_vampire https://p4s-archi.com
  python manage.py css_vampire https://p4s-archi.com --slug p4s-archi
  python manage.py css_vampire https://p4s-archi.com --slug p4s-archi --apply
"""
import json

from django.core.management.base import BaseCommand

from apps.landing_pages.css_vampire import theme_to_css_vars, vampire
from apps.landing_pages.models import LandingPage


class Command(BaseCommand):
    help = (
        "Visite l'URL du site cible, extrait polices/couleurs/logo "
        "et optionnellement applique le thème à une landing (content_json.theme)."
    )

    def add_arguments(self, parser):
        parser.add_argument("url", help="URL du site de la société (ex. https://p4s-archi.com)")
        parser.add_argument(
            "--slug",
            default="",
            help="Slug de la landing à mettre à jour (content_json.theme).",
        )
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Enregistre le thème dans content_json.theme de la landing (--slug requis).",
        )
        parser.add_argument(
            "--no-logo",
            action="store_true",
            help="Ne pas inclure logo_url dans le thème (éviter images externes si besoin).",
        )

    def handle(self, *args, **options):
        url = options["url"].strip()
        slug = options["slug"].strip()
        apply_ = options["apply"]
        no_logo = options["no_logo"]

        if apply_ and not slug:
            self.stderr.write(self.style.ERROR("--apply nécessite --slug."))
            return

        self.stdout.write(f"Visite de {url}…")
        theme = vampire(url)

        if theme.get("error"):
            self.stderr.write(self.style.ERROR(theme["error"]))
            return

        if no_logo:
            theme.pop("logo_url", None)
            theme.pop("background_image_url", None)

        self.stdout.write(self.style.SUCCESS("Thème extrait :"))
        self.stdout.write(json.dumps({k: v for k, v in theme.items() if k != "source_url"}, indent=2))
        self.stdout.write(f"  source_url: {theme.get('source_url', '')}")

        css_vars = theme_to_css_vars(theme)
        if css_vars:
            self.stdout.write("\nVariables CSS générées :")
            self.stdout.write(css_vars)

        if apply_ and slug:
            try:
                lp = LandingPage.objects.get(slug=slug)
            except LandingPage.DoesNotExist:
                self.stderr.write(self.style.ERROR(f"Landing slug={slug} introuvable."))
                return
            content = dict(lp.content_json or {})
            content["theme"] = {
                "fonts": theme.get("fonts"),
                "colors": theme.get("colors"),
                "logo_url": theme.get("logo_url"),
                "background_image_url": theme.get("background_image_url"),
            }
            content["theme_css"] = theme_to_css_vars(theme)
            lp.content_json = content
            lp.save()
            self.stdout.write(self.style.SUCCESS(f"Thème enregistré dans la landing « {lp.title } » (slug={slug})."))
