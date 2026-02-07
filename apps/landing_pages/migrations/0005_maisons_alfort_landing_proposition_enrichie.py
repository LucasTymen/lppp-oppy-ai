# Migration : Maisons-Alfort = landing prospection (missions, CDI, CDD), pas page municipale.
# Structure enrichie, même niveau de qualité que les autres landings ; iframe Conciergerie = démo.

from django.db import migrations


CONTENT_JSON = {
    "page_title": "Missions & CDI/CDD — Ville de Maisons-Alfort",
    "hero_headline": "Automatisation, IA et modernisation au service de la ville",
    "hero_sub_headline": "Missions, CDD, CDI — Growth Engineer ancré sur Maisons-Alfort",
    "hero_video_url": "https://www.youtube.com/embed/0btaHttkokc?si=N-DNOkmaos-TY-zW",
    "intro": "Je vous contacte pour des missions courtes, des CDD ou un CDI : mettre l’IA et l’automatisation au service de l’accueil citoyen, de la DSI et des services. La démo Conciergerie en bas de page montre ce que je peux déjà implanter chez vous.",
    "enjeux_lead": "Pour la ville et les équipes, j’ai identifié quelques enjeux où un profil technique peut débloquer la situation :",
    "pain_points": [
        "Désengorgement de l’accueil : les questions répétitives (démarches, horaires, pièces) peuvent être traitées par un assistant IA basé sur vos documents officiels.",
        "Interopérabilité : faire communiquer vos logiciels métiers (Python, APIs) sans tout casser.",
        "Jeunesse et emploi : automatiser le sourcing et la diffusion d’offres pour les jeunes alfortais.",
        "Visibilité et SEO : le site municipal peut mieux capter les requêtes des habitants et réduire la charge sur les guichets.",
    ],
    "solution_workflow": "Je m’appuie sur du code (Python, Flowise, RAG), des APIs et des bases documentaires : l’assistant ne répond qu’à partir de vos textes validés, sans inventer. On peut partir d’une démo (comme la Conciergerie ci-dessous), l’élargir à d’autres démarches, puis la déployer en prod et la connecter à vos outils.",
    "services": [
        {
            "title": "Missions courtes & CDD/CDI",
            "description": "Missions ciblées (audit, mise en place d’un assistant IA, connecteurs) ou CDD/CDI pour ancrer l’automatisation et l’IA dans vos services. Je m’adapte au rythme de la collectivité.",
        },
        {
            "title": "Conciergerie IA & RAG",
            "description": "Assistant qui répond aux citoyens à partir de vos documents (démarches, FAQ). Réponses factuelles, pas d’hallucination. Démo en bas de page ; on peut étendre les thèmes et déployer sur votre environnement.",
        },
        {
            "title": "Audit SEO & modernisation",
            "description": "Rapport de synthèse sur la visibilité du site (démarches, requêtes locales) et pistes pour réduire la charge sur l’accueil. Données terrain, pas du marketing.",
        },
    ],
    "mission_flash": "Diagnostic flash (48h) : j’identifie 3 leviers concrets (Conciergerie, interopérabilité ou SEO) et je vous propose un plan d’action. Sans engagement.",
    "why_growth_engineer": "Vous gardez la maîtrise : le code et les flux que je mets en place sont livrés et documentés. Pas d’agence qui repart avec la clé sous la porte — on construit ensemble.",
    "cta_text": "Échanger ou planifier un diagnostic",
    "contact_email": "lucas.tymen@gmail.com",
    "coordonnees_intro": "Pour une mission, un CDD, un CDI ou voir la démo Conciergerie en détail :",
    "theme": {
        "fonts": {"body": "Roboto", "heading": "Roboto"},
        "colors": {
            "background": "#000000",
            "text": "#e6e6e6",
            "primary": "#ac7fe8",
            "secondary": "#d2a5ff",
        },
        "logo_url": "https://maisons-alfort.fr/wp-content/uploads/2018/12/logo-maisons-alfort.png",
        "background_image_url": "https://maisons-alfort.fr/wp-content/uploads/2022/02/bg-agenda.jpg?id=22720",
    },
    "alert_banner": "Missions, CDD, CDI — Démo Conciergerie IA en bas de page",
}


def upgrade_maisons_alfort_to_proposition(apps, schema_editor):
    LandingPage = apps.get_model("landing_pages", "LandingPage")
    lp = LandingPage.objects.filter(slug="maisons-alfort").first()
    if not lp:
        return
    lp.title = "Missions & CDI/CDD — Ville de Maisons-Alfort"
    lp.template_key = "proposition"
    lp.sector = "mairie"
    lp.category = "proposition"
    lp.prospect_company = "Ville de Maisons-Alfort"
    lp.content_json = CONTENT_JSON
    lp.save()


def reverse_maisons_alfort_to_concierge(apps, schema_editor):
    LandingPage = apps.get_model("landing_pages", "LandingPage")
    lp = LandingPage.objects.filter(slug="maisons-alfort").first()
    if not lp:
        return
    lp.title = "Conciergerie IA Maisons-Alfort (élus)"
    lp.template_key = "concierge_maisons_alfort"
    lp.sector = "autre"
    lp.category = "autre"
    lp.prospect_company = ""
    lp.content_json = {
        "hero": {"headline": "Conciergerie IA Maisons-Alfort", "subheadline": "Découvrez les démarches Passeport et CNI en mairie."},
    }
    lp.save()


class Migration(migrations.Migration):

    dependencies = [
        ("landing_pages", "0004_add_conciergerie_maisons_alfort_landing"),
    ]

    operations = [
        migrations.RunPython(upgrade_maisons_alfort_to_proposition, reverse_maisons_alfort_to_concierge),
    ]
