from itertools import groupby
from pathlib import Path

import markdown
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import LandingPage
from .themes import LANDING_THEMES, THEME_YUWELL, THEME_CSS_YUWELL
from apps.scraping.flowise_client import get_flowise_chat_embed_url, get_flowise_chat_embed_config


def _use_perso_style(lp):
    """
    Algorithme fallback : utiliser le style perso (landing CV) quand on ne peut pas
    récupérer l'identité visuelle ou que le thème extrait est jugé trop moche.
    """
    if lp.template_key != "proposition":
        return False
    content = lp.content_json or {}
    theme = content.get("theme") or {}
    # Explicite : use_perso_style ou use_fallback sur le thème
    if content.get("use_perso_style") is True or theme.get("use_fallback") is True:
        return True
    # Pas de thème du tout (CSS Vampire jamais lancé ou erreur)
    if not theme:
        return True
    # Thème "moche" : pas de logo ni image de fond, couleurs très minimales
    has_identity = bool(theme.get("logo_url") or theme.get("background_image_url"))
    colors = theme.get("colors") or {}
    has_primary = bool(colors.get("primary"))
    if not has_identity and not has_primary:
        return True
    return False


def concierge_maisons_alfort_public(request):
    """Landing publique Concierge IA Maisons-Alfort pour les équipes municipales (chatbot intégré)."""
    flowise_embed_url = get_flowise_chat_embed_url() or ""
    base_url, chatflow_id = get_flowise_chat_embed_config()
    return render(
        request,
        "landing_pages/concierge_maisons_alfort.html",
        {
            "flowise_embed_url": flowise_embed_url,
            "flowise_api_host": base_url,
            "flowise_chatflow_id": chatflow_id,
        },
    )


# Données palettes Yuwell (étude graphique portfolio) — source: docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md
YUWELL_PALETTE_CORPORATE = [
    {"usage": "Marque principale", "name": "Yuwell Red", "hex": "#E60012", "rgb": "230, 0, 18", "pantone": "PANTONE 186 C"},
    {"usage": "Neutre principal", "name": "Pure White", "hex": "#FFFFFF", "rgb": "255, 255, 255", "pantone": "PANTONE White"},
    {"usage": "Neutre secondaire", "name": "Cool Gray", "hex": "#F5F5F5", "rgb": "245, 245, 245", "pantone": "PANTONE Cool Gray 1 C"},
    {"usage": "Texte principal", "name": "Dark Charcoal", "hex": "#333333", "rgb": "51, 51, 51", "pantone": "PANTONE 426 C"},
]
YUWELL_PALETTE_GAMMES = [
    {
        "gamme": "Solutions respiratoires",
        "description": "Concentrateurs d’oxygène, nébuliseurs, aspiration — Bleu clair / cyan médical.",
        "colors": [
            {"name": "Cyan médical", "hex": "#00C2D1", "rgb": "0, 194, 209", "pantone": "3125 C"},
            {"name": "Bleu moyen", "hex": "#0078A8", "rgb": "0, 120, 168", "pantone": "7699 C"},
            {"name": "Bleu grisé", "hex": "#90C2D3", "rgb": "144, 194, 211", "pantone": "544 C"},
        ],
    },
    {
        "gamme": "Diagnostic & monitoring",
        "description": "Tensiomètres, oxymètres, thermomètres — Vert médical doux.",
        "colors": [
            {"name": "Vert stable", "hex": "#57B894", "rgb": "87, 184, 148", "pantone": "7496 C"},
            {"name": "Vert moyen", "hex": "#3F8D68", "rgb": "63, 141, 104", "pantone": "3292 C"},
            {"name": "Vert désaturé", "hex": "#AACFBF", "rgb": "170, 207, 191", "pantone": "565 C"},
        ],
    },
    {
        "gamme": "Soins à domicile & chronic care",
        "description": "Suivi long terme, patients chroniques — Teal doux.",
        "colors": [
            {"name": "Teal doux", "hex": "#4DA6A1", "rgb": "77, 166, 161", "pantone": "7718 C"},
            {"name": "Teal clair", "hex": "#8FC7C4", "rgb": "143, 199, 196", "pantone": "3245 C"},
            {"name": "Gris bleuté", "hex": "#BECFD1", "rgb": "190, 207, 209", "pantone": "656 C"},
        ],
    },
    {
        "gamme": "Mobilité & rééducation",
        "description": "Fauteuils roulants, aides à la mobilité — Gris structurant + accent.",
        "colors": [
            {"name": "Cool Slate", "hex": "#7A7A7A", "rgb": "122, 122, 122", "pantone": "Cool Gray 9 C"},
            {"name": "Orange attention", "hex": "#E08E3C", "rgb": "224, 142, 60", "pantone": "7584 C"},
        ],
    },
    {
        "gamme": "Équipements cliniques & urgence",
        "description": "DAE, équipements hospitaliers — Rouge désaturé (alerte uniquement).",
        "colors": [
            {"name": "Rouge sécurisé", "hex": "#C5281C", "rgb": "197, 40, 28", "pantone": "186 C (désaturé)"},
        ],
    },
]


# Vidéo hero portfolio Yuwell — YouTube embed (autoplay, mute, loop)
YUWELL_HERO_VIDEO_URL = "https://www.youtube.com/watch?v=6pNskp5ZMqA"


def _yuwell_common_context(active_nav):
    """Contexte commun pour toutes les pages Yuwell (thème, palettes, vidéo hero)."""
    content = {
        "theme": THEME_YUWELL,
        "theme_css": THEME_CSS_YUWELL,
        "page_title": "Yuwell — Portfolio étude graphique",
        "hero_headline": "Study case — Yuwell",
        "hero_sub_headline": "Structuration chromatique par gamme de dispositifs médicaux",
    }
    return {
        "content": content,
        "palette_corporate": YUWELL_PALETTE_CORPORATE,
        "palette_gammes": YUWELL_PALETTE_GAMMES,
        "hero_video_url": YUWELL_HERO_VIDEO_URL,
        "active_nav": active_nav,
    }


def yuwell_presentation(request):
    """Page Présentation — accueil portfolio Yuwell (hero vidéo + liens vers les autres pages)."""
    ctx = _yuwell_common_context("presentation")
    ctx["content"]["page_title"] = "Yuwell — Présentation"
    ctx["content"]["hero_headline"] = "Portfolio Yuwell"
    ctx["content"]["hero_sub_headline"] = "Étude graphique : système couleur & charte par gamme produit"
    return render(request, "landing_pages/yuwell_presentation.html", ctx)


def yuwell_study_case(request):
    """Page Study case 1 — contexte, principes, gammes, palettes, règles, bénéfices."""
    ctx = _yuwell_common_context("study-case")
    ctx["content"]["page_title"] = "Yuwell — Study case : système couleur"
    return render(request, "landing_pages/yuwell_study_case.html", ctx)


def yuwell_study_case_2(request):
    """Page Study case 2 — second cas d'étude (à compléter)."""
    ctx = _yuwell_common_context("study-case-2")
    ctx["content"]["page_title"] = "Yuwell — Study case 2"
    return render(request, "landing_pages/yuwell_study_case_2.html", ctx)


def yuwell_charte_graphique(request):
    """Page Charte graphique — palettes corporate + par gamme, règles d'usage."""
    ctx = _yuwell_common_context("charte-graphique")
    ctx["content"]["page_title"] = "Yuwell — Charte graphique"
    return render(request, "landing_pages/yuwell_charte_graphique.html", ctx)


def yuwell_a_propos(request):
    """Page À propos de moi."""
    ctx = _yuwell_common_context("a-propos")
    ctx["content"]["page_title"] = "Yuwell — À propos"
    return render(request, "landing_pages/yuwell_a_propos.html", ctx)


def yuwell_portfolio(request):
    """Redirection vers la page Présentation (accueil Yuwell)."""
    from django.shortcuts import redirect
    return redirect("yuwell_presentation", permanent=False)


def _content_with_defaults(content, template_key):
    """Renseigne les clés optionnelles manquantes pour éviter VariableDoesNotExist dans les templates.
    Normalise hero sub : une seule valeur (hero_sub_headline puis hero_subtitle) renseignée dans les DEUX clés
    pour que tout template (proposition, proposition_value, relance-evenement) puisse utiliser l'une ou l'autre sans erreur."""
    templates_using_content = ("proposition", "proposition_value", "relance-evenement")
    if template_key not in templates_using_content:
        return content
    defaults = {
        "positionnement": "",
        "activite_pain_points": "",
        "mission_flash": "",
        "produit_commercial": "",
        "hero_subtitle": "",
        "hero_sub_headline": "",
        "icebreaker": "",
        "intro": "",
        "hero_title": "",
    }
    out = {**defaults, **content}
    # Toujours renseigner les deux clés avec la même valeur (évite VariableDoesNotExist si un template référence l'une ou l'autre)
    hero_sub = out.get("hero_sub_headline") or out.get("hero_subtitle") or ""
    out["hero_sub_headline"] = out["hero_subtitle"] = hero_sub
    return out


def landing_public(request, slug):
    """Affiche une landing page publique (pour la cible). Staff peut prévisualiser les brouillons."""
    # Portfolio Yuwell : suivi en base pour admin/console, mais pages réelles sous /yuwell/
    if slug == "yuwell-portfolio":
        from django.shortcuts import redirect
        return redirect("yuwell_presentation", permanent=False)
    lp = get_object_or_404(LandingPage, slug=slug)
    if not lp.is_published and not (request.user.is_authenticated and request.user.is_staff):
        raise Http404("Landing non publiée")
    content = _content_with_defaults(lp.content_json or {}, lp.template_key)
    # Pour les slugs enregistrés (ex. orsys), le thème vient de themes.py → les modifs sont visibles sans --update
    if lp.slug in LANDING_THEMES:
        theme_dict, theme_css = LANDING_THEMES[lp.slug]
        content = {**content, "theme": theme_dict, "theme_css": theme_css}
    # ORSYS : vidéo hero en HTML5 (CDN ORSYS) — plus fiable que YouTube embed
    if lp.slug == "orsys":
        content["hero_video_mp4_url"] = "https://cdn.prod.website-files.com/68ad6297550fb653e920efc5/68ffa0854b21bf93944847b7_ORSYS_VideoHomepage-transcode.mp4"
        content["hero_video_webm_url"] = "https://cdn.prod.website-files.com/68ad6297550fb653e920efc5/68ffa0854b21bf93944847b7_ORSYS_VideoHomepage-transcode.webm"
        content["hero_video_url"] = ""
    use_perso_style = _use_perso_style(lp) if lp.slug not in LANDING_THEMES else False
    perso_ref_path = getattr(settings, "LANDING_PERSO_REF_PATH", "")
    context = {
        "landing_page": lp,
        "content": content,
        "use_perso_style": use_perso_style,
        "perso_ref_path": perso_ref_path,
    }
    # Démo Conciergerie IA (iframe) : pour slug maisons-alfort, même avec template proposition
    if lp.slug == "maisons-alfort":
        try:
            context["flowise_embed_url"] = get_flowise_chat_embed_url() or ""
            base_url, chatflow_id = get_flowise_chat_embed_config()
            context["flowise_api_host"] = base_url
            context["flowise_chatflow_id"] = chatflow_id
        except Exception:
            context["flowise_embed_url"] = ""
            context["flowise_api_host"] = ""
            context["flowise_chatflow_id"] = ""
    response = render(
        request,
        f"landing_pages/{lp.template_key}.html",
        context,
    )
    # Éviter le cache navigateur pour que les modifications (content_json, templates) soient visibles immédiatement
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    # YouTube embed Erreur 153 : la page doit être servie avec Referrer-Policy pour que l'iframe envoie le Referer à YouTube
    response["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response


def console_landings(request):
    """
    Console : toutes les landing pages avec URLs Django et URL déployée (Vercel).
    Permet de consulter et traquer les landings générées (Django + standalone).
    Réservé aux utilisateurs connectés (staff pour voir toutes, sinon seulement les siennes).
    """
    if not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.get_full_path())
    pages = LandingPage.objects.all().order_by("-created_at")
    if not request.user.is_staff:
        pages = pages.filter(created_by=request.user)
    sector = request.GET.get("sector", "").strip()
    category = request.GET.get("category", "").strip()
    if sector:
        pages = pages.filter(sector=sector)
    if category:
        pages = pages.filter(category=category)
    # URL Django (base du site) pour chaque landing
    base_url = request.build_absolute_uri("/").rstrip("/")
    rows = []
    for lp in pages:
        rows.append({
            "landing": lp,
            "url_django": f"{base_url}/p/{lp.slug}/",
            "url_deploy": lp.deploy_url or "",
        })
    return render(
        request,
        "landing_pages/console.html",
        {
            "rows": rows,
            "sector_filter": sector,
            "category_filter": category,
            "sector_choices": LandingPage.SECTOR_CHOICES,
            "category_choices": LandingPage.CATEGORY_CHOICES,
        },
    )


def landing_list(request):
    """Liste de toutes les landing pages, classées par secteur puis nom de société."""
    if not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.get_full_path())
    pages = (
        LandingPage.objects.all()
        .order_by("sector", "prospect_company", "title")
    )
    if not request.user.is_staff:
        pages = pages.filter(created_by=request.user)
    sector = request.GET.get("sector", "").strip()
    category = request.GET.get("category", "").strip()
    if sector:
        pages = pages.filter(sector=sector)
    if category:
        pages = pages.filter(category=category)
    sector_labels = dict(LandingPage.SECTOR_CHOICES)
    sectors_with_pages = []
    for sector_key, group in groupby(pages, key=lambda lp: lp.sector or "autre"):
        pages_list = list(group)
        sectors_with_pages.append({
            "sector_key": sector_key,
            "sector_label": sector_labels.get(sector_key, sector_key),
            "pages": pages_list,
        })
    return render(
        request,
        "landing_pages/list.html",
        {
            "sectors_with_pages": sectors_with_pages,
            "sector_filter": sector,
            "category_filter": category,
            "sector_choices": LandingPage.SECTOR_CHOICES,
            "category_choices": LandingPage.CATEGORY_CHOICES,
        },
    )


def _contact_dir(slug):
    """Dossier contact docs/contacts/<slug>/ (convention : slug = nom dossier contact)."""
    base = Path(settings.BASE_DIR)
    return base / "docs" / "contacts" / slug


def _rapport_html(slug):
    """
    Lit le rapport Markdown du dossier contact, retourne HTML ou None.
    Priorité : rapport-teaser*.md (extrait public pour montrer le sérieux) si présent,
    sinon rapport-complet*.md (source unique, généré une seule fois, trace pour réutilisation).
    """
    contact = _contact_dir(slug)
    if not contact.is_dir():
        return None
    # Teaser en priorité (1–2 éléments pour prouver qu'on a des données, sans tout dévoiler)
    teasers = list(contact.glob("rapport-teaser*.md"))
    rapports = list(contact.glob("rapport-complet*.md"))
    path = None
    if teasers:
        path = teasers[0]
    elif rapports:
        path = rapports[0]
    if not path:
        return None
    try:
        text = path.read_text(encoding="utf-8")
        return markdown.markdown(text, extensions=["extra"])
    except Exception:
        return None


def _common_landing_context(lp):
    """Contexte commun pour les pages annexes (rapport, prospects, proposition)."""
    content = lp.content_json or {}
    use_perso_style = _use_perso_style(lp)
    return {
        "landing_page": lp,
        "content": content,
        "use_perso_style": use_perso_style,
    }


def landing_rapport(request, slug):
    """Page « Consulter le rapport » : rendu du rapport complet Markdown (fiche + stratégie + SEO)."""
    lp = get_object_or_404(LandingPage, slug=slug)
    if not lp.is_published and not (request.user.is_authenticated and request.user.is_staff):
        raise Http404("Landing non publiée")
    report_html = _rapport_html(slug)
    ctx = _common_landing_context(lp)
    ctx["report_html"] = report_html
    ctx["report_available"] = bool(report_html)
    response = render(request, "landing_pages/rapport.html", ctx)
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response


def landing_prospects(request, slug):
    """Page « Prospects » : échantillon de prospects (content_json.prospects ou à renseigner)."""
    lp = get_object_or_404(LandingPage, slug=slug)
    if not lp.is_published and not (request.user.is_authenticated and request.user.is_staff):
        raise Http404("Landing non publiée")
    content = lp.content_json or {}
    prospects = content.get("prospects") or []
    ctx = _common_landing_context(lp)
    ctx["prospects"] = prospects
    response = render(request, "landing_pages/prospects.html", ctx)
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response


def landing_proposition_value(request, slug):
    """Page « Proposition de valeur » : vue structurée (enjeux, solution, services, offre)."""
    lp = get_object_or_404(LandingPage, slug=slug)
    if not lp.is_published and not (request.user.is_authenticated and request.user.is_staff):
        raise Http404("Landing non publiée")
    ctx = _common_landing_context(lp)
    response = render(request, "landing_pages/proposition_value.html", ctx)
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response
