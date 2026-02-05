# Migration données : landing Conciergerie IA Maisons-Alfort (élus)

from django.db import migrations


def create_conciergerie_landing(apps, schema_editor):
    LandingPage = apps.get_model("landing_pages", "LandingPage")
    if LandingPage.objects.filter(slug="maisons-alfort").exists():
        return
    LandingPage.objects.create(
        title="Conciergerie IA Maisons-Alfort (élus)",
        slug="maisons-alfort",
        prospect_name="",
        prospect_company="",
        sector="autre",
        category="autre",
        template_key="concierge_maisons_alfort",
        content_json={
            "hero": {
                "headline": "Conciergerie IA Maisons-Alfort",
                "subheadline": "Découvrez les démarches Passeport et CNI en mairie.",
            },
        },
        is_published=True,
        deploy_url="",
    )


def remove_conciergerie_landing(apps, schema_editor):
    LandingPage = apps.get_model("landing_pages", "LandingPage")
    LandingPage.objects.filter(slug="maisons-alfort").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("landing_pages", "0003_alter_landingpage_category_choices"),
    ]

    operations = [
        migrations.RunPython(create_conciergerie_landing, remove_conciergerie_landing),
    ]
