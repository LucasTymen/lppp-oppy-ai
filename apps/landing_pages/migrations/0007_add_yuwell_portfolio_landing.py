# Migration données : entrée Landing Page pour le portfolio Yuwell (suivi admin/console)

from django.db import migrations


def create_yuwell_portfolio_landing(apps, schema_editor):
    LandingPage = apps.get_model("landing_pages", "LandingPage")
    if LandingPage.objects.filter(slug="yuwell-portfolio").exists():
        return
    LandingPage.objects.create(
        title="Portfolio Yuwell — étude graphique",
        slug="yuwell-portfolio",
        prospect_name="",
        prospect_company="Yuwell (Jiangsu Yuyue Medical Equipment)",
        sector="autre",
        category="proposition",
        template_key="proposition",
        content_json={},
        is_published=True,
        deploy_url="",
    )


def remove_yuwell_portfolio_landing(apps, schema_editor):
    LandingPage = apps.get_model("landing_pages", "LandingPage")
    LandingPage.objects.filter(slug="yuwell-portfolio").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("landing_pages", "0006_maisons_alfort_hero_video_url"),
    ]

    operations = [
        migrations.RunPython(create_yuwell_portfolio_landing, remove_yuwell_portfolio_landing),
    ]
