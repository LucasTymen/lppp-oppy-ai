"""
Crée la landing 0Flow (Samson Fedida) à partir du JSON existant.
Usage : python3 manage.py create_landing_0flow
Idempotent : n'écrase pas si la landing existe déjà (met à jour le content_json si --update).

Thème 0Flaw manuel : palette réelle du site (navy, teal/cyan, dégradé hero) car CSS Vampire
extrait mal les couleurs d'accent. Source visuelle : https://0flaw.fr/solution/formation
"""
import json
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.landing_pages.models import LandingPage

# Palette 0Flaw (page Formation) : bleu navy, teal/cyan accent, dégradés
THEME_0FLAW = {
    "fonts": {"body": "system-ui", "heading": "system-ui"},
    "colors": {
        "background": "#0A192F",
        "text": "#ffffff",
        "primary": "#00C2CB",   # teal/cyan (boutons CTA, Connexion, bannière)
        "secondary": "#00E6FF", # teal clair (dégradés, hover)
    },
    "logo_url": "https://0flaw.fr/logo-0flaw-blue-fade.png",
    "background_image_url": None,
}

THEME_CSS_0FLAW = """:root {
  --lp-font-body: system-ui, -apple-system, sans-serif;
  --lp-font-heading: system-ui, -apple-system, sans-serif;
  --lp-bg: #0A192F;
  --lp-text: #ffffff;
  --lp-primary: #00C2CB;
  --lp-secondary: #00E6FF;
  --lp-border: #1e3a5f;
  --lp-block-bg: #0d2137;
  --lp-muted: rgba(255,255,255,0.7);
  --lp-heading: #ffffff;
  --lp-cta-text: #ffffff;
}
/* Hero dégradé 0Flaw (navy → léger teal) */
.hero:not(.has-bg-image)::before {
  background: linear-gradient(135deg, #0A192F 0%, #0D113C 40%, rgba(0,194,203,0.12) 100%);
}
"""


class Command(BaseCommand):
    help = "Crée la landing 0Flow (Samson Fedida) depuis docs/contacts/0flow/landing-proposition-samson.json"

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
            / "0flow"
            / "landing-proposition-samson.json"
        )
        if not json_path.exists():
            self.stderr.write(self.style.ERROR(f"Fichier introuvable : {json_path}"))
            return

        with open(json_path, encoding="utf-8") as f:
            content = json.load(f)

        title = content.get("page_title") or content.get("hero_title") or "Lucas Tymen x 0Flow — Automatisation"
        slug = "0flow"
        prospect_company = "0Flow"
        prospect_name = "Samson Fedida"
        sector = "cybersecurite"
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
