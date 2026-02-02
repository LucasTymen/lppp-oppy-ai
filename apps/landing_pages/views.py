from itertools import groupby

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import LandingPage


def landing_public(request, slug):
    """Affiche une landing page publique (pour la cible). Staff peut prévisualiser les brouillons."""
    lp = get_object_or_404(LandingPage, slug=slug)
    if not lp.is_published and not (request.user.is_authenticated and request.user.is_staff):
        from django.http import Http404
        raise Http404("Landing non publiée")
    return render(
        request,
        f"landing_pages/{lp.template_key}.html",
        {"landing_page": lp, "content": lp.content_json},
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
