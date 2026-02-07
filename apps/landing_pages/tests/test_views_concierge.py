"""
Tests des vues landing Conciergerie IA Maisons-Alfort (chatbot embed).
Couverture pour la feature chatbot landing agents municipaux.
"""
from unittest.mock import patch

import pytest
from django.urls import reverse
from django.test import Client, RequestFactory

from apps.landing_pages.models import LandingPage
from apps.landing_pages import views as landing_views


@pytest.mark.django_db
class TestConciergeMaisonsAlfortPublic:
    """Vue concierge_maisons_alfort_public (couverture directe car URL actuelle = redirect)."""

    def test_view_returns_200_and_uses_concierge_template(self):
        """Vue concierge renvoie 200 et le contenu typique du template (RequestFactory ne fournit pas .templates)."""
        with patch("apps.landing_pages.views.get_flowise_chat_embed_url") as m:
            m.return_value = "http://localhost:3010/embed/abc"
            req = RequestFactory().get("/maisons-alfort/")
            response = landing_views.concierge_maisons_alfort_public(req)
            assert response.status_code == 200
            html = response.content.decode()
            assert "Conciergerie" in html or "maisons-alfort" in html.lower()
            assert "3010" in html

    def test_context_has_flowise_embed_url_when_configured(self):
        """URL embed renseignée → page contient 3010 et (script Chatbot.initFull ou iframe)."""
        with patch("apps.landing_pages.views.get_flowise_chat_embed_url") as m:
            m.return_value = "http://localhost:3010/embed/abc"
            req = RequestFactory().get("/maisons-alfort/")
            response = landing_views.concierge_maisons_alfort_public(req)
            html = response.content.decode()
            assert "http://localhost:3010/embed/abc" in html
            assert "3010" in html
            assert "Chatbot.initFull" in html or "Chatbot.init" in html or "iframe" in html

    def test_context_has_api_host_and_chatflow_id_when_embed_configured(self):
        """Vue concierge injecte flowise_api_host et flowise_chatflow_id dans le HTML (script embed)."""
        with patch("apps.landing_pages.views.get_flowise_chat_embed_url") as m_url:
            with patch("apps.landing_pages.views.get_flowise_chat_embed_config") as m_cfg:
                m_url.return_value = "http://localhost:3010/embed/xyz-123"
                m_cfg.return_value = ("http://localhost:3010", "xyz-123")
                req = RequestFactory().get("/maisons-alfort/")
                response = landing_views.concierge_maisons_alfort_public(req)
                html = response.content.decode()
                assert "http://localhost:3010" in html
                assert "xyz-123" in html

    def test_template_renders_script_embed_when_api_host_and_chatflow_id_set(self):
        """Quand api_host et chatflow_id sont fournis, le template injecte Chatbot.initFull (embed in-place)."""
        with patch("apps.landing_pages.views.get_flowise_chat_embed_url") as m_url:
            with patch("apps.landing_pages.views.get_flowise_chat_embed_config") as m_cfg:
                m_url.return_value = "http://localhost:3010/embed/cf-123"
                m_cfg.return_value = ("http://localhost:3010", "cf-123")
                req = RequestFactory().get("/maisons-alfort/")
                response = landing_views.concierge_maisons_alfort_public(req)
                html = response.content.decode()
                assert "Chatbot.initFull" in html
                assert "flowise-fullchatbot" in html
                assert "apiHost" in html and "chatflowid" in html.lower()
                assert "cf-123" in html

    def test_context_placeholder_when_no_embed_url(self):
        """Stratégie écran vide : pas d’URL embed → placeholder « Chat en cours de configuration »."""
        with patch("apps.landing_pages.views.get_flowise_chat_embed_url") as m:
            m.return_value = ""
            req = RequestFactory().get("/maisons-alfort/")
            response = landing_views.concierge_maisons_alfort_public(req)
            assert b"configuration" in response.content.lower() or b"Chat" in response.content
            # Pas d’iframe avec src (évite écran vide sans message)
            html = response.content.decode()
            assert 'iframe src="http' not in html or html.count("iframe") == 0

    def test_redirect_maisons_alfort_to_landing_public(self):
        client = Client()
        response = client.get(reverse("concierge_maisons_alfort_public"))
        assert response.status_code == 302
        assert "p/maisons-alfort" in response.url


@pytest.mark.django_db
class TestLandingPublicConciergeTemplate:
    """Vue /p/maisons-alfort/ (landing_public avec template_key concierge_maisons_alfort)."""

    def test_landing_maisons_alfort_injects_flowise_embed_url(self):
        lp, _ = LandingPage.objects.get_or_create(
            slug="maisons-alfort",
            defaults={
                "title": "Conciergerie IA Maisons-Alfort",
                "template_key": "concierge_maisons_alfort",
                "is_published": True,
            },
        )
        lp.template_key = "concierge_maisons_alfort"
        lp.is_published = True
        lp.save()

        # Mock des deux fonctions utilisées par la vue (landing_public appelle les deux)
        with patch("apps.landing_pages.views.get_flowise_chat_embed_url") as m_url:
            with patch("apps.landing_pages.views.get_flowise_chat_embed_config") as m_cfg:
                m_url.return_value = "http://localhost:3010/embed/flow-id"
                m_cfg.return_value = ("http://localhost:3010", "flow-id")
                client = Client()
                response = client.get(reverse("landing_public", kwargs={"slug": "maisons-alfort"}))
                assert response.status_code == 200
                assert "flowise_embed_url" in response.context
                assert response.context["flowise_embed_url"] == "http://localhost:3010/embed/flow-id"
                assert response.context.get("flowise_api_host") == "http://localhost:3010"
                assert response.context.get("flowise_chatflow_id") == "flow-id"

    def test_landing_maisons_alfort_handles_flowise_exception(self):
        lp = LandingPage.objects.filter(slug="maisons-alfort").first()
        if not lp:
            lp = LandingPage.objects.create(
                slug="maisons-alfort",
                title="Conciergerie",
                template_key="concierge_maisons_alfort",
                is_published=True,
            )
        with patch("apps.landing_pages.views.get_flowise_chat_embed_url") as m:
            m.side_effect = Exception("Flowise down")
            client = Client()
            response = client.get(reverse("landing_public", kwargs={"slug": "maisons-alfort"}))
            assert response.status_code == 200
            assert response.context.get("flowise_embed_url") == ""

    def test_concierge_template_does_not_expose_secrets_in_html(self):
        """Pentester / sécurité : aucun secret (clé API, sk-) ne doit apparaître dans le HTML rendu."""
        with patch("apps.landing_pages.views.get_flowise_chat_embed_url") as m_url:
            with patch("apps.landing_pages.views.get_flowise_chat_embed_config") as m_cfg:
                m_url.return_value = "http://localhost:3010/embed/safe-uuid"
                m_cfg.return_value = ("http://localhost:3010", "safe-uuid")
                req = RequestFactory().get("/maisons-alfort/")
                response = landing_views.concierge_maisons_alfort_public(req)
                html = response.content.decode()
                assert "sk-" not in html
                assert "FLOWISE_API_KEY" not in html
