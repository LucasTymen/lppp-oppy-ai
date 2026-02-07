"""
Tests du client Flowise : config, URL embed, push documents.
Couverture pour la feature chatbot landing agents municipaux.
"""
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from apps.scraping.flowise_client import (
    get_flowise_config,
    get_flowise_chat_embed_url,
    get_flowise_chat_embed_config,
    push_file_to_flowise,
    DEFAULT_CHATFLOW_ID,
)


class TestGetFlowiseConfig:
    """get_flowise_config() — URL, store ID, API key depuis l'environnement."""

    def test_defaults_when_env_empty(self):
        with patch.dict(os.environ, {}, clear=False):
            for key in ("FLOWISE_URL", "FLOWISE_DOCUMENT_STORE_ID", "FLOWISE_API_KEY"):
                os.environ.pop(key, None)
            url, store_id, api_key = get_flowise_config()
            assert "flowise" in url or "3000" in url
            assert store_id == ""
            assert api_key == ""

    def test_reads_env(self):
        with patch.dict(
            os.environ,
            {
                "FLOWISE_URL": "http://localhost:3010",
                "FLOWISE_DOCUMENT_STORE_ID": "store-123",
                "FLOWISE_API_KEY": "secret",
            },
        ):
            url, store_id, api_key = get_flowise_config()
            assert url == "http://localhost:3010"
            assert store_id == "store-123"
            assert api_key == "secret"

    def test_strips_trailing_slash(self):
        with patch.dict(os.environ, {"FLOWISE_URL": "http://localhost:3010/"}):
            url, _, _ = get_flowise_config()
            assert url.rstrip("/") == "http://localhost:3010"


class TestGetFlowiseChatEmbedUrl:
    """get_flowise_chat_embed_url() — URL iframe pour landing /p/maisons-alfort/ (stratégie écran vide)."""

    def test_returns_empty_when_chatflow_id_strips_to_empty(self):
        # Quand FLOWISE_CHATFLOW_ID est uniquement des espaces, .strip() donne "" → retour ""
        with patch.dict(
            os.environ,
            {"FLOWISE_URL": "http://localhost:3010", "FLOWISE_CHATFLOW_ID": "   "},
        ):
            assert get_flowise_chat_embed_url() == ""

    def test_uses_env_url_and_chatflow_id(self):
        with patch.dict(
            os.environ,
            {
                "FLOWISE_URL": "http://localhost:3010",
                "FLOWISE_CHATFLOW_ID": "abc-123",
            },
        ):
            url = get_flowise_chat_embed_url()
            assert url == "http://localhost:3010/embed/abc-123"

    def test_uses_default_chatflow_id_when_not_set(self):
        with patch.dict(
            os.environ,
            {"FLOWISE_URL": "http://localhost:3010"},
            clear=False,
        ):
            os.environ.pop("FLOWISE_CHATFLOW_ID", None)
            url = get_flowise_chat_embed_url()
            assert DEFAULT_CHATFLOW_ID in url
            assert url == f"http://localhost:3010/embed/{DEFAULT_CHATFLOW_ID}"

    def test_fallback_base_url_when_flowise_url_empty_docker(self):
        with patch.dict(
            os.environ,
            {"FLOWISE_URL": "", "DB_HOST": "db", "FLOWISE_CHATFLOW_ID": "xyz"},
            clear=False,
        ):
            url = get_flowise_chat_embed_url()
            assert "localhost:3010" in url
            assert "/embed/xyz" in url

    def test_fallback_base_url_when_flowise_url_empty_localhost(self):
        with patch.dict(
            os.environ,
            {"FLOWISE_URL": "", "DB_HOST": "127.0.0.1", "FLOWISE_CHATFLOW_ID": "xyz"},
            clear=False,
        ):
            url = get_flowise_chat_embed_url()
            assert "3010" in url
            assert "/embed/xyz" in url


class TestGetFlowiseChatEmbedConfig:
    """get_flowise_chat_embed_config() — (base_url, chatflow_id) pour embed par script."""

    def test_returns_empty_tuple_when_embed_url_empty(self):
        with patch.dict(
            os.environ,
            {"FLOWISE_URL": "http://localhost:3010", "FLOWISE_CHATFLOW_ID": "   "},
        ):
            base, cid = get_flowise_chat_embed_config()
            assert base == ""
            assert cid == ""

    def test_parses_embed_url_into_base_and_id(self):
        with patch.dict(
            os.environ,
            {
                "FLOWISE_URL": "http://localhost:3010",
                "FLOWISE_CHATFLOW_ID": "my-flow-uuid",
            },
        ):
            base, cid = get_flowise_chat_embed_config()
            assert base == "http://localhost:3010"
            assert cid == "my-flow-uuid"

    def test_strips_query_string_from_chatflow_id(self):
        with patch.dict(
            os.environ,
            {"FLOWISE_URL": "http://localhost:3010", "FLOWISE_CHATFLOW_ID": "uuid?foo=bar"},
        ):
            base, cid = get_flowise_chat_embed_config()
            assert base == "http://localhost:3010"
            assert cid == "uuid"


class TestPushFileToFlowise:
    """push_file_to_flowise() — envoi fichier au Document Store (mock HTTP)."""

    def test_returns_error_when_store_id_empty(self):
        result = push_file_to_flowise(
            Path("/tmp/foo.txt"), "http://flowise:3000", "", ""
        )
        assert "error" in result
        assert "FLOWISE_DOCUMENT_STORE_ID" in result["error"]

    def test_returns_json_on_success(self):
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
            f.write(b"content")
            f.flush()
            path = Path(f.name)
        try:
            with patch("requests.post") as mpost:
                mresp = mpost.return_value
                mresp.raise_for_status = lambda: None
                mresp.json.return_value = {"inserted": 1}
                result = push_file_to_flowise(
                    path, "http://flowise:3000", "store-id", ""
                )
                assert result.get("inserted") == 1
                mpost.assert_called_once()
        finally:
            path.unlink(missing_ok=True)

    def test_returns_error_on_request_exception(self):
        import requests as requests_module
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
            f.write(b"x")
            f.flush()
            path = Path(f.name)
        try:
            with patch("requests.post") as mpost:
                # Le code attrape requests.RequestException (ex. ConnectionError)
                mpost.side_effect = requests_module.exceptions.ConnectionError("Connection refused")
                result = push_file_to_flowise(
                    path, "http://flowise:3000", "store-id", ""
                )
                assert "error" in result
                assert "Connection refused" in result["error"]
        finally:
            path.unlink(missing_ok=True)
