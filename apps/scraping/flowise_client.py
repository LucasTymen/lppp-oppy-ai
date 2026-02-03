"""
Client API Flowise pour push de documents (partagé entre commande et vues).
Variables : FLOWISE_URL, FLOWISE_DOCUMENT_STORE_ID, FLOWISE_API_KEY.
Voir docs/base-de-connaissances/flowise-push-documents-informatique.md
"""
import os
from pathlib import Path


def get_flowise_config():
    """URL, store ID et optionnellement API key depuis l'environnement."""
    url = os.environ.get("FLOWISE_URL", "http://flowise:3000").rstrip("/")
    store_id = os.environ.get("FLOWISE_DOCUMENT_STORE_ID", "")
    api_key = os.environ.get("FLOWISE_API_KEY", "")
    return url, store_id, api_key


def push_file_to_flowise(file_path: Path, base_url: str, store_id: str, api_key: str):
    """Envoie un fichier au Document Store Flowise via POST multipart."""
    try:
        import requests
    except ImportError:
        return {"error": "requests non installé (pip install requests)"}
    if not store_id:
        return {"error": "FLOWISE_DOCUMENT_STORE_ID manquant"}
    url = f"{base_url}/api/v1/document-store/upsert/{store_id}"
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    with open(file_path, "rb") as f:
        files = {"files": (file_path.name, f, "text/plain")}
        try:
            resp = requests.post(url, files=files, headers=headers, timeout=120)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {
                "error": str(e),
                "status_code": getattr(getattr(e, "response", None), "status_code", None),
            }
