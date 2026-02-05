from itertools import groupby
from pathlib import Path

import markdown
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import LandingPage
from .themes import LANDING_THEMES
from apps.scraping.flowise_client import get_flowise_chat_embed_url


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
    flowise_embed_url = get_flowise_chat_embed_url()
    return render(
        request,
        "landing_pages/concierge_maisons_alfort.html",
        {"flowise_embed_url": flowise_embed_url},
    )


def _content_with_defaults(content, template_key):
    """Renseigne les clés optionnelles manquantes pour éviter VariableDoesNotExist dans les templates."""
    if template_key != "proposition":
        return content
    defaults = {
        "positionnement": "",
        "activite_pain_points": "",
        "mission_flash": "",
        "produit_commercial": "",
    }
    return {**defaults, **content}


def landing_public(request, slug):
    """Affiche une landing page publique (pour la cible). Staff peut prévisualiser les brouillons."""
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
    if lp.template_key == "concierge_maisons_alfort":
        try:
            context["flowise_embed_url"] = get_flowise_chat_embed_url() or ""
        except Exception:
            context["flowise_embed_url"] = ""
    response = render(
        request,
        f"landing_pages/{lp.template_key}.html",
        context,
    )
    # Éviter le cache navigateur pour que les modifications (content_json, templates) soient visibles immédiatement
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
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
