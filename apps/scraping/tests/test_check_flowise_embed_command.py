"""
Tests de la commande check_flowise_embed (stratégie écran vide).
Vérifie que le diagnostic automatisé s’exécute et affiche les bonnes infos.
"""
import os
from unittest.mock import patch

import pytest
from django.core.management import call_command
from io import StringIO


class TestCheckFlowiseEmbedCommand:
    """Commande check_flowise_embed — diagnostic URL d’embed."""

    def test_command_outputs_diagnostic_with_embed_url(self):
        """Quand FLOWISE_URL et FLOWISE_CHATFLOW_ID sont définis, la commande affiche l’URL d’embed."""
        out = StringIO()
        with patch.dict(
            os.environ,
            {"FLOWISE_URL": "http://localhost:3010", "FLOWISE_CHATFLOW_ID": "test-id-123"},
            clear=False,
        ):
            call_command("check_flowise_embed", stdout=out)
        text = out.getvalue()
        assert "Diagnostic" in text or "embed" in text.lower()
        assert "3010" in text
        assert "test-id-123" in text or "/embed/" in text

    def test_command_outputs_warning_when_chatflow_id_empty(self):
        """Quand FLOWISE_CHATFLOW_ID est vide, la commande signale l’URL d’embed vide."""
        out = StringIO()
        with patch.dict(
            os.environ,
            {"FLOWISE_URL": "http://localhost:3010", "FLOWISE_CHATFLOW_ID": ""},
            clear=False,
        ):
            call_command("check_flowise_embed", stdout=out)
        text = out.getvalue()
        assert "vide" in text.lower() or "configuration" in text.lower() or "FLOWISE_CHATFLOW_ID" in text

    def test_command_ping_does_not_crash(self):
        """Avec --ping, la commande tente la connexion (sans mock : peut échouer si Flowise down)."""
        out = StringIO()
        with patch.dict(os.environ, {"FLOWISE_URL": "http://localhost:3010", "FLOWISE_CHATFLOW_ID": "x"}, clear=False):
            call_command("check_flowise_embed", "--ping", stdout=out)
        text = out.getvalue()
        assert "connexion" in text.lower() or "3010" in text
        # Soit succès (Réponse 200), soit erreur (Erreur) selon que Flowise tourne ou non
        assert "Réponse" in text or "Erreur" in text or "3010" in text
