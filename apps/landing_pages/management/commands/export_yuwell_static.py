"""
Exporte le portfolio Yuwell (5 pages) en site statique pour déploiement GitHub / GitLab.
Usage : python manage.py export_yuwell_static [--output deploy/yuwell-portfolio]
Génère : index.html (présentation), study-case.html, study-case-2.html, charte-graphique.html, a-propos.html
         + copie static/landing_pages/yuwell/ et images utilisées.
Liens et chemins /static/ sont convertis en relatifs pour fonctionnement sans serveur Django.
"""
import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.test import RequestFactory

from apps.landing_pages.views import (
    _yuwell_common_context,
    yuwell_presentation,
    yuwell_study_case,
    yuwell_study_case_2,
    yuwell_charte_graphique,
    yuwell_a_propos,
)


PAGES = [
    ("presentation", "yuwell_presentation", "yuwell_presentation.html", "index.html"),
    ("study-case", "yuwell_study_case", "yuwell_study_case.html", "study-case.html"),
    ("study-case-2", "yuwell_study_case_2", "yuwell_study_case_2.html", "study-case-2.html"),
    ("charte-graphique", "yuwell_charte_graphique", "yuwell_charte_graphique.html", "charte-graphique.html"),
    ("a-propos", "yuwell_a_propos", "yuwell_a_propos.html", "a-propos.html"),
]


def _replace_static_links(html: str) -> str:
    """Rend les liens et assets relatifs pour site statique."""
    # Liens internes Yuwell
    html = html.replace('href="/yuwell/presentation/"', 'href="index.html"')
    html = html.replace('href="/yuwell/study-case/"', 'href="study-case.html"')
    html = html.replace('href="/yuwell/study-case-2/"', 'href="study-case-2.html"')
    html = html.replace('href="/yuwell/charte-graphique/"', 'href="charte-graphique.html"')
    html = html.replace('href="/yuwell/a-propos/"', 'href="a-propos.html"')
    # Assets : /static/ -> static/ (relatif)
    html = html.replace('href="/static/', 'href="static/')
    html = html.replace('src="/static/', 'src="static/')
    html = html.replace("url('/static/", "url('static/")
    html = html.replace('url("/static/', 'url("static/')
    return html


class Command(BaseCommand):
    help = "Exporte le portfolio Yuwell en HTML statique (5 pages + assets) pour GH/GL."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            default="deploy/yuwell-portfolio",
            help="Dossier de sortie (ex. deploy/yuwell-portfolio)",
        )

    def handle(self, *args, **options):
        out_dir = Path(options["output"])
        out_dir.mkdir(parents=True, exist_ok=True)
        factory = RequestFactory()
        request = factory.get("/yuwell/presentation/")

        for active_nav, view_name, template_name, out_name in PAGES:
            if view_name == "yuwell_presentation":
                response = yuwell_presentation(request)
            elif view_name == "yuwell_study_case":
                response = yuwell_study_case(request)
            elif view_name == "yuwell_study_case_2":
                response = yuwell_study_case_2(request)
            elif view_name == "yuwell_charte_graphique":
                response = yuwell_charte_graphique(request)
            else:
                response = yuwell_a_propos(request)
            html = response.content.decode("utf-8")
            html = _replace_static_links(html)
            (out_dir / out_name).write_text(html, encoding="utf-8")
            self.stdout.write(f"  {out_name}")

        # Copie des statiques Yuwell
        static_root = Path(settings.BASE_DIR) / "apps" / "landing_pages" / "static" / "landing_pages"
        yuwell_static = static_root / "yuwell"
        out_static = out_dir / "static" / "landing_pages"
        out_static.mkdir(parents=True, exist_ok=True)
        if yuwell_static.exists():
            shutil.copytree(yuwell_static, out_static / "yuwell", dirs_exist_ok=True)
            self.stdout.write("  static/landing_pages/yuwell/ (fonts, images)")
        # Images utilisées par les templates (ex. portrait)
        images_src = static_root / "images"
        if images_src.exists():
            shutil.copytree(images_src, out_static / "images", dirs_exist_ok=True)
            self.stdout.write("  static/landing_pages/images/")

        self.stdout.write(self.style.SUCCESS("Export termine -> %s" % out_dir.absolute()))
