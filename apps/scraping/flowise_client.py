"""
Client API Flowise pour push de documents (partagé entre commande et vues).
Variables : FLOWISE_URL, FLOWISE_DOCUMENT_STORE_ID, FLOWISE_API_KEY.
Voir docs/base-de-connaissances/flowise-push-documents-informatique.md
"""
import os
from pathlib import Path
from typing import Any, Dict


def get_flowise_config():
    """URL, store ID et optionnellement API key depuis l'environnement."""
    url = os.environ.get("FLOWISE_URL", "http://flowise:3000").rstrip("/")  # en interne Docker : flowise:3000 ; depuis l'hôte : FLOWISE_URL=http://localhost:3010
    store_id = os.environ.get("FLOWISE_DOCUMENT_STORE_ID", "")
    api_key = os.environ.get("FLOWISE_API_KEY", "")
    return url, store_id, api_key


def get_flowise_chat_api_config():
    """
    Configuration API chat Flowise (prediction chatflow).
    - FLOWISE_URL : base URL (ex: http://localhost:3010, http://127.0.0.1:43001).
    - FLOWISE_CHATFLOW_ID : ID du chatflow RAG.
    - FLOWISE_API_KEY : optionnel.
    """
    base_url = (os.environ.get("FLOWISE_URL", "http://flowise:3000") or "").strip().rstrip("/")
    raw_chatflow_id = (os.environ.get("FLOWISE_CHATFLOW_ID") or "").strip()
    if not raw_chatflow_id:
        raw_chatflow_id = DEFAULT_CHATFLOW_ID
    chatflow_id = (raw_chatflow_id or "").split("?")[0].strip()
    api_key = (os.environ.get("FLOWISE_API_KEY", "") or "").strip()
    return base_url, chatflow_id, api_key


# Chatflow Concierge IA Maisons-Alfort (ID Flowise Embed). Overridable par FLOWISE_CHATFLOW_ID.
# ID du chatflow qui fonctionne (Flowise UI → Embed) ; mettre à jour si tu recrées le flow.
DEFAULT_CHATFLOW_ID = "67206a96-470e-4607-ba8b-5955e97aa116"


def _flowise_embed_base_url():
    """
    URL de base joignable par le navigateur (iframe). L'embed est affiché dans le navigateur
    (souvent sur l'hôte), donc l'URL ne doit jamais être flowise:3000 (résolu uniquement dans Docker).
    """
    base_url = os.environ.get("FLOWISE_URL", "").strip().rstrip("/")
    # Si l'URL pointe vers le conteneur (flowise:3000), le navigateur ne peut pas la joindre → utiliser localhost:3010
    if base_url and ("flowise:" in base_url or base_url.startswith("http://flowise/") or base_url.startswith("https://flowise/")):
        base_url = "http://localhost:3010"
    if not base_url:
        base_url = "http://localhost:3010"
    return base_url.rstrip("/")


def _flowise_chatflow_id_stripped():
    """ID du chatflow (env ou défaut), sans query string."""
    raw = (os.environ.get("FLOWISE_CHATFLOW_ID") or DEFAULT_CHATFLOW_ID).strip()
    return (raw.split("?")[0].strip() or raw) if raw else ""


def get_flowise_chat_embed_url():
    """
    URL d'embed du chatflow Flowise (landing /essais/concierge/ et /p/maisons-alfort/).
    L'URL est consommée par le navigateur (iframe) : toujours une URL joignable depuis le navigateur
    (localhost:3010). Override : FLOWISE_URL, FLOWISE_CHATFLOW_ID.
    """
    base_url = _flowise_embed_base_url()
    chatflow_id = _flowise_chatflow_id_stripped()
    if not chatflow_id:
        return ""
    return f"{base_url}/embed/{chatflow_id}"


def get_flowise_chat_embed_config():
    """
    Retourne (base_url, chatflow_id) pour l'embed (iframe ou script). base_url est toujours
    une URL joignable par le navigateur (localhost:3010). Les query strings sont retirées du chatflow_id.
    """
    base_url = _flowise_embed_base_url()
    chatflow_id = _flowise_chatflow_id_stripped()
    if not chatflow_id:
        return "", ""
    return base_url, chatflow_id


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


def ask_flowise_chatflow(question: str, base_url: str, chatflow_id: str, api_key: str = "", timeout: int = 45) -> Dict[str, Any]:
    """
    Appel standard Flowise prediction:
    POST {FLOWISE_BASE}/api/v1/prediction/{CHATFLOW_ID}
    body: {"question": "..."}
    """
    try:
        import requests
    except ImportError:
        return {"error": "requests non installé (pip install requests)"}

    if not base_url:
        return {"error": "FLOWISE_URL manquant"}
    if not chatflow_id:
        return {"error": "FLOWISE_CHATFLOW_ID manquant"}
    if not question or not question.strip():
        return {"error": "question vide"}

    endpoint = f"{base_url.rstrip('/')}/api/v1/prediction/{chatflow_id}"
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    payload = {"question": question.strip()}
    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as exc:
        return {
            "error": str(exc),
            "status_code": getattr(getattr(exc, "response", None), "status_code", None),
            "endpoint": endpoint,
        }

    try:
        return {"ok": True, "data": response.json(), "endpoint": endpoint}
    except ValueError:
        return {"ok": True, "data": {"text": response.text}, "endpoint": endpoint}
