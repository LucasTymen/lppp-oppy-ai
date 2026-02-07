# Mise à jour hero_video_url Maisons-Alfort (embed fourni par l'utilisateur)

from django.db import migrations


HERO_VIDEO_URL = "https://www.youtube.com/embed/0btaHttkokc?si=N-DNOkmaos-TY-zW"


def update_hero_video_url(apps, schema_editor):
    LandingPage = apps.get_model("landing_pages", "LandingPage")
    lp = LandingPage.objects.filter(slug="maisons-alfort").first()
    if not lp or not lp.content_json:
        return
    content = dict(lp.content_json)
    content["hero_video_url"] = HERO_VIDEO_URL
    lp.content_json = content
    lp.save()


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("landing_pages", "0005_maisons_alfort_landing_proposition_enrichie"),
    ]

    operations = [
        migrations.RunPython(update_hero_video_url, noop_reverse),
    ]
