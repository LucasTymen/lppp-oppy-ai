"""
Tests de la vue /essais/concierge/ (ConciergeChatView).
Couverture pour la feature chatbot landing agents municipaux.
"""
from unittest.mock import patch

import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestConciergeChatView:
    """Interface de test chatbot Concierge IA (authentifiée)."""

    def test_redirects_anonymous_to_login(self):
        client = Client()
        response = client.get(reverse("landingsgenerator:concierge_chat"))
        assert response.status_code == 302
        assert "login" in response.url.lower()

    def test_returns_200_for_staff_with_embed_url(self):
        user = User.objects.create_user(
            username="staff", password="test", is_staff=True, is_superuser=True
        )
        client = Client()
        client.force_login(user)
        with patch("apps.landingsgenerator.views.get_flowise_chat_embed_url") as m:
            m.return_value = "http://localhost:3010/embed/xyz"
            response = client.get(reverse("landingsgenerator:concierge_chat"))
        assert response.status_code == 200
        assert response.context["flowise_embed_url"] == "http://localhost:3010/embed/xyz"
