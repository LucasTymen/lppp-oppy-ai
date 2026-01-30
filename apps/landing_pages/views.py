from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import LandingPage


def landing_public(request, slug):
    """Affiche une landing page publique (pour la cible)."""
    lp = get_object_or_404(LandingPage, slug=slug, is_published=True)
    return render(
        request,
        f"landing_pages/{lp.template_key}.html",
        {"landing_page": lp, "content": lp.content_json},
    )


def landing_list(request):
    """Liste des landing pages (admin / dashboard)."""
    if not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.get_full_path())
    pages = LandingPage.objects.filter(created_by=request.user).order_by("-created_at")
    return render(request, "landing_pages/list.html", {"landing_pages": pages})
