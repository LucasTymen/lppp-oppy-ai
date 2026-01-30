from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.landing_pages.urls")),
    path("essais/", include("apps.landingsgenerator.urls")),
    path("campaigns/", include("apps.campaigns.urls")),
    path("api/", include("apps.scraping.urls")),
]
