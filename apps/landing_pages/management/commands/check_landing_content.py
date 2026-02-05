"""
Vérifie les clés présentes dans content_json d'une landing (diagnostic vidéo hero / thème).
Usage : python3 manage.py check_landing_content orsys
"""
from django.core.management.base import BaseCommand

from apps.landing_pages.models import LandingPage


class Command(BaseCommand):
    help = "Affiche les clés content_json d'une landing (slug) pour diagnostic."

    def add_arguments(self, parser):
        parser.add_argument("slug", type=str, help="Slug de la landing (ex. orsys)")

    def handle(self, *args, **options):
        slug = options["slug"]
        lp = LandingPage.objects.filter(slug=slug).first()
        if not lp:
            self.stdout.write(self.style.ERROR(f"Landing slug={slug} introuvable."))
            return
        content = lp.content_json or {}
        self.stdout.write(f"Landing : {lp.title} (slug={slug})")
        self.stdout.write(f"  theme présent : {'theme' in content}")
        self.stdout.write(f"  theme_css présent : {'theme_css' in content}")
        self.stdout.write(f"  hero_video_url présent : {'hero_video_url' in content}")
        if content.get("hero_video_url"):
            self.stdout.write(f"  hero_video_url = {content['hero_video_url'][:50]}...")
        if content.get("theme"):
            self.stdout.write(f"  theme.logo_url : {bool(content['theme'].get('logo_url'))}")
            self.stdout.write(f"  theme.colors.primary : {bool(content['theme'].get('colors', {}).get('primary'))}")
        self.stdout.write(self.style.SUCCESS("Pour injecter thème + vidéo : python3 manage.py create_landing_orsys --update --publish"))
