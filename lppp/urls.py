from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", RedirectView.as_view(url="/admin/login/", permanent=False)),
    path("", include("apps.landing_pages.urls")),
    path("essais/", include("apps.landingsgenerator.urls")),
    path("campaigns/", include("apps.campaigns.urls")),
    path("api/", include("apps.scraping.urls")),
]
