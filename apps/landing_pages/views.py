from itertools import groupby

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import LandingPage


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


def landing_public(request, slug):
    """Affiche une landing page publique (pour la cible). Staff peut prévisualiser les brouillons."""
    lp = get_object_or_404(LandingPage, slug=slug)
    if not lp.is_published and not (request.user.is_authenticated and request.user.is_staff):
        raise Http404("Landing non publiée")
    content = lp.content_json or {}
    use_perso_style = _use_perso_style(lp)
    perso_ref_path = getattr(settings, "LANDING_PERSO_REF_PATH", "")
    response = render(
        request,
        f"landing_pages/{lp.template_key}.html",
        {
            "landing_page": lp,
            "content": content,
            "use_perso_style": use_perso_style,
            "perso_ref_path": perso_ref_path,
        },
    )
    # Éviter le cache navigateur pour que les modifications (content_json, templates) soient visibles immédiatement
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response


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
