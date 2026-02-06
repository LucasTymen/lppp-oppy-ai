"""
Client API Flowise pour push de documents (partagé entre commande et vues).
Variables : FLOWISE_URL, FLOWISE_DOCUMENT_STORE_ID, FLOWISE_API_KEY.
Voir docs/base-de-connaissances/flowise-push-documents-informatique.md
"""
import os
from pathlib import Path


def get_flowise_config():
    """URL, store ID et optionnellement API key depuis l'environnement."""
    url = os.environ.get("FLOWISE_URL", "http://flowise:3000").rstrip("/")  # en interne Docker : flowise:3000 ; depuis l'hôte : FLOWISE_URL=http://localhost:3010
    store_id = os.environ.get("FLOWISE_DOCUMENT_STORE_ID", "")
    api_key = os.environ.get("FLOWISE_API_KEY", "")
    return url, store_id, api_key


# Chatflow Concierge IA Maisons-Alfort (ID Flowise Embed). Overridable par FLOWISE_CHATFLOW_ID.
# ID du chatflow qui fonctionne (Flowise UI → Embed) ; mettre à jour si tu recrées le flow.
DEFAULT_CHATFLOW_ID = "67206a96-470e-4607-ba8b-5955e97aa116"


def get_flowise_chat_embed_url():
    """
    URL d'embed du chatflow Flowise (landing /essais/concierge/ et /p/maisons-alfort/).
    L'URL est consommée par le navigateur (iframe) : elle doit être joignable depuis la machine
    où s'ouvre la page (souvent l'hôte). Si FLOWISE_URL n'est pas défini : on utilise
    http://localhost:3010 (port LPPP). Définir explicitement FLOWISE_URL=http://localhost:3010
    dans .env et redémarrer le service web après modification.
    Override : FLOWISE_URL, FLOWISE_CHATFLOW_ID.
    """
    base_url = os.environ.get("FLOWISE_URL", "").strip()
    if not base_url:
        db_host = (os.environ.get("DB_HOST") or "db").strip().lower()
        if db_host in ("localhost", "127.0.0.1"):
            base_url = "http://localhost:3010"  # port LPPP dédié (stack autonome)
        else:
            # DB_HOST=db (Docker) : l'embed est affiché dans le navigateur sur l'hôte → localhost:3010
            base_url = "http://localhost:3010"
    base_url = base_url.rstrip("/")
    chatflow_id = (os.environ.get("FLOWISE_CHATFLOW_ID") or DEFAULT_CHATFLOW_ID).strip()
    if not chatflow_id:
        return ""
    return f"{base_url}/embed/{chatflow_id}"


def get_flowise_chat_embed_config():
    """
    Retourne (base_url, chatflow_id) pour l'embed par script (flowise-embed).
    Si pas configuré : ("", ""). Utilisé par le template pour Chatbot.initFull({ apiHost, chatflowid }) (embed in-place).
    """
    embed_url = get_flowise_chat_embed_url()
    if not embed_url:
        return "", ""
    # embed_url = "http://localhost:3010/embed/UUID"
    parts = embed_url.rstrip("/").split("/embed/")
    if len(parts) != 2:
        return "", ""
    return parts[0], (parts[1].split("?")[0].strip() or "")


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
