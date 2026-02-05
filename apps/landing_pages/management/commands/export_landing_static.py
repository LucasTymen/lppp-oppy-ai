"""
Exporte une landing (template proposition) en un fichier HTML statique.
Usage : python manage.py export_landing_static p4s-archi --output deploy/static-p4s-vercel/index.html
Avec version intermédiaire du rapport (société, stratégie, SEO) :
  python manage.py export_landing_static p4s-archi --rapport-md docs/contacts/p4s-archi/etude-concurrentielle-pestel-swot-porter.md
La page générée est exactement ce que Django sert sur /p/<slug>/ (contenu inlined, pas d'app).
Préserve tous les degrés de personnalisation : thème (CSS Vampire), style perso (fallback), hero background, etc.
Pour Vercel : déployer le dossier contenant ce index.html (page statique, pas Next.js).
"""
import json
from pathlib import Path

import markdown
from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from apps.landing_pages.models import LandingPage
from apps.landing_pages.themes import LANDING_THEMES
from apps.landing_pages.views import _content_with_defaults, _use_perso_style

RAPPORT_HTML_HEAD = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport — société, stratégie, SEO</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root { --lp-bg: #0a0a0f; --lp-text: #e8e8ed; --lp-heading: #fff; --lp-muted: #9898a8; --lp-primary: #6366f1; }
        * { box-sizing: border-box; }
        body { font-family: 'Inter', system-ui, sans-serif; margin: 0; min-height: 100vh; background: var(--lp-bg); color: var(--lp-text); line-height: 1.65; padding: clamp(2rem, 5vw, 4rem); max-width: 900px; margin: 0 auto; }
        a { color: var(--lp-primary); }
        h1, h2, h3 { color: var(--lp-heading); }
        table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
        th, td { border: 1px solid rgba(255,255,255,0.15); padding: 0.5rem 0.75rem; text-align: left; }
        th { background: rgba(99, 102, 241, 0.2); }
        blockquote { border-left: 4px solid var(--lp-primary); margin: 1rem 0; padding-left: 1rem; color: var(--lp-muted); }
        .back-link { display: inline-block; margin-bottom: 2rem; color: var(--lp-primary); text-decoration: none; }
        .back-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <a href="index.html" class="back-link">← Retour à la proposition</a>
    <div class="rapport-body">
"""

RAPPORT_HTML_FOOT = """
    </div>
</body>
</html>
"""


class Command(BaseCommand):
    help = "Exporte une landing (proposition) en HTML statique pour déploiement Vercel (la page, pas une app). Préserve thème et style perso. Option --rapport-md : exporte une version intermédiaire du rapport (société, stratégie, SEO) en rapport.html et affiche le lien « Consulter le rapport »."

    def add_arguments(self, parser):
        parser.add_argument("slug", help="Slug de la landing (ex. p4s-archi)")
        parser.add_argument(
            "--output",
            default="deploy/static-p4s-vercel/index.html",
            help="Chemin du fichier HTML de sortie",
        )
        parser.add_argument(
            "--json",
            help="Si la landing n'existe pas en base, charger ce JSON (ex. docs/contacts/p4s-archi/landing-proposition-joel.json)",
        )
        parser.add_argument(
            "--rapport-md",
            help="Chemin vers un fichier Markdown (ex. docs/contacts/p4s-archi/etude-concurrentielle-pestel-swot-porter.md). Génère rapport.html et définit rapport_url pour le lien « Consulter le rapport complet ».",
        )

    def handle(self, *args, **options):
        slug = options["slug"]
        output_path = Path(options["output"])
        json_path = options.get("json")
        rapport_md_path = options.get("rapport_md")

        lp = None
        content = {}
        try:
            lp = LandingPage.objects.get(slug=slug)
            content = _content_with_defaults(dict(lp.content_json or {}), lp.template_key)
            use_perso_style = _use_perso_style(lp)
            self.stdout.write(f"Landing trouvée en base : {lp.title} (use_perso_style={use_perso_style})")
        except LandingPage.DoesNotExist:
            if json_path and Path(json_path).exists():
                with open(json_path, encoding="utf-8") as f:
                    content = _content_with_defaults(json.load(f), "proposition")
                # Objet minimal pour le template + _use_perso_style (content_json, template_key)
                class MockLanding:
                    title = content.get("page_title", "Landing")
                    slug = slug
                    prospect_company = content.get("prospect_company", "P4S Architecture")
                    prospect_name = content.get("prospect_name", "Joël Courtois")
                    template_key = "proposition"
                    content_json = content

                lp = MockLanding()
                if slug == "orsys":
                    lp.prospect_company = "ORSYS"
                    lp.prospect_name = "Aboubakar"
                use_perso_style = _use_perso_style(lp)
                self.stdout.write(f"Contenu chargé depuis {json_path} (use_perso_style={use_perso_style})")
            else:
                self.stdout.write(
                    self.style.ERROR(
                        f"Landing {slug} introuvable en base. Utilisez --json pour fournir le fichier JSON."
                    )
                )
                return

        # Export optionnel de la version intermédiaire du rapport (société, stratégie, SEO)
        if rapport_md_path:
            rapport_path = Path(rapport_md_path)
            if rapport_path.exists():
                md_text = rapport_path.read_text(encoding="utf-8")
                body_html = markdown.markdown(
                    md_text,
                    extensions=["tables", "fenced_code", "nl2br"],
                )
                rapport_out = output_path.parent / "rapport.html"
                output_path.parent.mkdir(parents=True, exist_ok=True)
                rapport_out.write_text(
                    RAPPORT_HTML_HEAD + body_html + RAPPORT_HTML_FOOT,
                    encoding="utf-8",
                )
                self.stdout.write(self.style.SUCCESS(f"Rapport intermédiaire écrit : {rapport_out}"))
                content = dict(content)
                content["rapport_url"] = "rapport.html"
            else:
                self.stdout.write(self.style.WARNING(f"Fichier rapport non trouvé : {rapport_path}"))

        # Thème + vidéo hero pour les slugs enregistrés (ex. orsys) — même logique que la vue
        content = dict(content)
        if slug in LANDING_THEMES:
            theme_dict, theme_css = LANDING_THEMES[slug]
            content["theme"] = theme_dict
            content["theme_css"] = theme_css
            use_perso_style = False
        if slug == "orsys":
            content["hero_video_mp4_url"] = "https://cdn.prod.website-files.com/68ad6297550fb653e920efc5/68ffa0854b21bf93944847b7_ORSYS_VideoHomepage-transcode.mp4"
            content["hero_video_webm_url"] = "https://cdn.prod.website-files.com/68ad6297550fb653e920efc5/68ffa0854b21bf93944847b7_ORSYS_VideoHomepage-transcode.webm"
            content["hero_video_url"] = ""

        perso_ref_path = getattr(settings, "LANDING_PERSO_REF_PATH", "")
        html = render_to_string(
            "landing_pages/proposition.html",
            {
                "landing_page": lp,
                "content": content,
                "use_perso_style": use_perso_style,
                "perso_ref_path": perso_ref_path,
            },
        )

        # Ne pas remplacer les URLs Django par des ancres inexistantes (pas de liens prospects/rapport/proposition sur la page statique)
        # Les liens « Consulter le rapport » sont gérés par rapport_url dans le template.

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html, encoding="utf-8")
        self.stdout.write(self.style.SUCCESS(f"Écrit : {output_path}"))
        self.stdout.write(
            "Déploiement Vercel : pousser le dossier contenant ce index.html (repo = uniquement la page, pas Next.js)."
        )
