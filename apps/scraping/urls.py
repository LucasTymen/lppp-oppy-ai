"""
URLs API scraping / enrichissement (N8N, Flowise).
"""
from django.urls import path

from . import views

app_name = "scraping"

urlpatterns = [
    path("chat/flowise", views.flowise_chat_proxy_view, name="flowise_chat_proxy"),
    path("enriched/enrich", views.EnrichWebhookView.as_view(), name="enrich_webhook"),
    path("enriched/enrich-one", views.enrich_single_sync_view, name="enrich_one"),
    path("concierge/scrape", views.ConciergeScrapeView.as_view(), name="concierge_scrape"),
    path("concierge/save-content", views.ConciergeSaveContentView.as_view(), name="concierge_save_content"),
    path("concierge/push-to-flowise", views.ConciergePushToFlowiseView.as_view(), name="concierge_push_to_flowise"),
]
