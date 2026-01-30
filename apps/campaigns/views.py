"""Vues campagnes — liste et détail (montage projet)."""
from django.shortcuts import render, get_object_or_404
from .models import Campaign


def campaign_list(request):
    """Liste des campagnes (accès authentifié)."""
    if not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.get_full_path())
    campaigns = Campaign.objects.filter(created_by=request.user).order_by("-created_at")
    return render(request, "campaigns/list.html", {"campaigns": campaigns})


def campaign_detail(request, slug):
    """Détail d'une campagne (prospects)."""
    if not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.get_full_path())
    campaign = get_object_or_404(Campaign, slug=slug, created_by=request.user)
    prospects = campaign.prospects.select_related("landing_page").order_by("company_name")
    return render(request, "campaigns/detail.html", {"campaign": campaign, "prospects": prospects})
