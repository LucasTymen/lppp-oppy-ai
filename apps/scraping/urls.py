"""
URLs API scraping / enrichissement (N8N, Flowise).
"""
from django.urls import path

from . import views

app_name = "scraping"

urlpatterns = [
    path("enriched/enrich", views.EnrichWebhookView.as_view(), name="enrich_webhook"),
    path("enriched/enrich-one", views.enrich_single_sync_view, name="enrich_one"),
]
