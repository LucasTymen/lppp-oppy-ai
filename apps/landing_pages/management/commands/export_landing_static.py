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
        use_json_file = json_path and Path(json_path).exists()
        # Si --json fourni : privilégier le fichier (même logique que la vue pour fitclem) — services_segments, infographies, contrastes
        if use_json_file:
            with open(json_path, encoding="utf-8") as f:
                content = _content_with_defaults(json.load(f), "proposition")
            _slug, _content = slug, content
            class MockLanding:
                title = _content.get("page_title", "Landing")
                slug = _slug
                prospect_company = _content.get("prospect_company", "P4S Architecture")
                prospect_name = _content.get("prospect_name", "Joël Courtois")
                template_key = "proposition"
                content_json = _content

            lp = MockLanding()
            if slug == "orsys":
                lp.prospect_company = "ORSYS"
                lp.prospect_name = "Aboubakar"
            elif slug == "fitclem":
                lp.prospect_company = "FitClem"
                lp.prospect_name = "Clémentine Sarlat"
            elif slug == "casapy":
                lp.prospect_company = "Casapy"
                lp.prospect_name = ""
            elif slug == "promovacances":
                lp.prospect_company = "Promovacances"
                lp.prospect_name = ""
            elif slug == "infopro":
                lp.prospect_company = "Infopro Digital"
                lp.prospect_name = ""
            elif slug == "lppp-oppy-ai":
                lp.prospect_company = "OPPORTUNITY (Oppy.ai)"
                lp.prospect_name = ""
            use_perso_style = _use_perso_style(lp)
            self.stdout.write(f"Contenu chargé depuis {json_path} (use_perso_style={use_perso_style})")
        else:
            try:
                lp = LandingPage.objects.get(slug=slug)
                content = _content_with_defaults(dict(lp.content_json or {}), lp.template_key)
                use_perso_style = _use_perso_style(lp)
                self.stdout.write(f"Landing trouvée en base : {lp.title} (use_perso_style={use_perso_style})")
            except (LandingPage.DoesNotExist, Exception) as e:
                if isinstance(e, LandingPage.DoesNotExist):
                    pass
                else:
                    self.stdout.write(self.style.WARNING(f"Base non accessible ({e!r}), fallback JSON si fourni."))
                self.stdout.write(
                    self.style.ERROR(
                        f"Landing {slug} introuvable et pas de --json. Utilisez --json pour fournir le fichier JSON."
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
                # Contexte pour rapport avec nav (comme sur le reste du site)
                theme_dict, theme_css = (None, None)
                if slug in LANDING_THEMES:
                    theme_dict, theme_css = LANDING_THEMES[slug]
                hero_video_embed = ""
                hero_video_mp4 = ""
                if slug in ("promovacances", "infopro"):
                    mp4_url = content.get("hero_video_mp4_url") or ""
                    if mp4_url:
                        hero_video_mp4 = mp4_url
                    else:
                        import re
                        url = content.get("hero_video_url") or ""
                        m = re.search(r"(?:v=|embed/)([a-zA-Z0-9_-]{11})", str(url).strip()) if url else None
                        vid = m.group(1) if m else ("ArifpieowSw" if slug == "promovacances" else "IG9WGfuTOIQ")
                        hero_video_embed = f"https://www.youtube-nocookie.com/embed/{vid}?autoplay=1&mute=1&loop=1&playlist={vid}&controls=0&rel=0&showinfo=0"
                rapport_ctx = {
                    "company_name": getattr(lp, "prospect_company", content.get("prospect_company", "")),
                    "logo_url": (theme_dict or {}).get("logo_url") if theme_dict else None,
                    "theme_css": theme_css or "",
                    "index_url": "index.html",
                    "rapport_url": "rapport.html",
                    "infographie_url": content.get("infographie_url") or ("infographie-promovacances-7-formats.html" if slug == "promovacances" else "infographie-infopro-7-formats.html" if slug == "infopro" else None),
                    "positionnement_marketing_url": "positionnement-marketing.html" if slug in ("promovacances", "infopro") else None,
                    "audit_dashboard_url": content.get("audit_dashboard_url") or "",
                    "report_body": body_html,
                    "hero_video_embed_url": hero_video_embed,
                    "hero_video_mp4_url": hero_video_mp4,
                }
                rapport_html = render_to_string("landing_pages/rapport_static_export.html", rapport_ctx)
                rapport_out.write_text(rapport_html, encoding="utf-8")
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

        # Promovacances / Infopro (export statique) : URLs relatives pour assets
        if slug == "promovacances":
            content["promovacances_assets_url"] = ""
            content["infographie_url"] = "infographie-promovacances-7-formats.html"
            content["positionnement_marketing_url"] = "positionnement-marketing.html"
            # rapport_url : conservé si --rapport-md ; sinon le lien rapport est masqué par le template
            # audit_dashboard_url : laissé vide en statique (pas de dashboard embarqué)
        elif slug == "infopro":
            content["infographie_url"] = "infographie-infopro-7-formats.html"
            content["positionnement_marketing_url"] = "positionnement-marketing.html"
        elif slug == "lppp-oppy-ai":
            content["infographie_url"] = "infographie-lppp-oppy-ai-7-formats.html"
            content["positionnement_marketing_url"] = "positionnement-marketing.html"
            content["audit_dashboard_url"] = "infographies-oppy-ai.html"
            content["oppy_assets_prefix"] = ""
            if content.get("infographies_oppy"):
                for info in content["infographies_oppy"]:
                    info["url"] = info.get("file", "")

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
        if slug == "lppp-oppy-ai":
            # Remplacer le script waves-pins (chemin Django /static/...) par chemin relatif
            import re
            html = re.sub(
                r'src="[^"]*waves-pins-hero\.js"',
                'src="waves-pins-hero.js"',
                html,
            )
        output_path.write_text(html, encoding="utf-8")
        self.stdout.write(self.style.SUCCESS(f"Écrit : {output_path}"))

        # Casapy : copier les infographies PNG et HTML dans le dossier de déploiement
        if slug == "casapy":
            import shutil
            casapy_assets = Path(settings.BASE_DIR) / "docs" / "contacts" / "casapy"
            out_dir = output_path.parent
            patterns = ["slide*.svg", "one-pager*.svg", "casapy-wave*.svg", "slide*.png", "one-pager*.png", "casapy-wave*.png", "infographie*.html"]
            for pat in patterns:
                for f in casapy_assets.glob(pat):
                    dest = out_dir / f.name
                    shutil.copy2(f, dest)
                    self.stdout.write(self.style.SUCCESS(f"  Copié : {f.name}"))

        # Promovacances / Infopro : copier infographie HTML et style tokens
        if slug == "promovacances":
            import shutil
            promo_assets = Path(settings.BASE_DIR) / "docs" / "contacts" / "promovacances"
            out_dir = output_path.parent
            patterns = ["infographie*.html", "positionnement-marketing.html", "promovacances_style_tokens.css", "audit-dashboard.json", "hero-promovacances.mp4"]
            for pat in patterns:
                for f in promo_assets.glob(pat):
                    dest = out_dir / f.name
                    shutil.copy2(f, dest)
                    self.stdout.write(self.style.SUCCESS(f"  Copié : {f.name}"))
        elif slug == "infopro":
            import shutil
            infopro_assets = Path(settings.BASE_DIR) / "docs" / "contacts" / "infopro"
            out_dir = output_path.parent
            patterns = ["infographie*.html", "positionnement-marketing.html", "infopro_style_tokens.css", "audit-dashboard.json", "hero-infopro.mp4"]
            for pat in patterns:
                for f in infopro_assets.glob(pat):
                    dest = out_dir / f.name
                    shutil.copy2(f, dest)
                    self.stdout.write(self.style.SUCCESS(f"  Copié : {f.name}"))
        elif slug == "lppp-oppy-ai":
            import shutil
            oppy_assets = Path(settings.BASE_DIR) / "docs" / "contacts" / "lppp-oppy-ai"
            out_dir = output_path.parent
            patterns = [
                "competitive_mapping_2d.html", "seo_action_plan_timeline.svg",
                "revenue_gap_calculator.html", "link_juice_flow_diagram.svg",
                "reverse_waterfall_funnel.html", "radar_chart_positioning.html",
                "infographie-lppp-oppy-ai-7-formats.html", "positionnement-marketing.html",
                "waves-pins-hero.js",
            ]
            for fname in patterns:
                f = oppy_assets / fname
                if f.is_file():
                    shutil.copy2(f, out_dir / fname)
                    self.stdout.write(self.style.SUCCESS(f"  Copié : {fname}"))
            if content.get("infographies_oppy"):
                infos_ctx = {"infographies": content["infographies_oppy"]}
                infos_html = render_to_string("landing_pages/infographies_oppy_static.html", infos_ctx)
                (out_dir / "infographies-oppy-ai.html").write_text(infos_html, encoding="utf-8")
                self.stdout.write(self.style.SUCCESS("  Copié : infographies-oppy-ai.html (généré)"))

        self.stdout.write(
            "Déploiement Vercel : pousser le dossier contenant ce index.html (repo = uniquement la page, pas Next.js)."
        )
