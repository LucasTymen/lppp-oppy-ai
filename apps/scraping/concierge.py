"""
Scraping pour le Concierge IA (Quick Win Maisons-Alfort).
Extrait le texte des pages web pour alimenter un RAG (Flowise).
"""
import logging
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

# User-Agent raisonnable pour éviter blocage basique
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; LPPP-Concierge/1.0; +https://github.com/LucasTymen/landingPageCreatorForProspection)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
}

# URLs par défaut pour Maisons-Alfort (pages clés : accueil, état civil, déchets, horaires, contact)
DEFAULT_MAISONS_ALFORT_URLS = [
    "https://maisons-alfort.fr/",
    "https://maisons-alfort.fr/votre-ville-votre-mairie/les-demarches-en-ligne/etat-civil/",
    "https://maisons-alfort.fr/votre-cadre-de-vie/le-tri-facile-pour-vos-dechets/",
    "https://maisons-alfort.fr/votre-cadre-de-vie/voirie/",
    "https://maisons-alfort.fr/votre-cadre-de-vie/travaux/",
    "https://maisons-alfort.fr/accueil/infos-pratiques/vos-contacts-en-mairie/",
]


def scrape_page(url: str, timeout: int = 15) -> dict:
    """
    Récupère une page et en extrait le texte principal (body, sans scripts/styles).
    Retourne {"url": str, "text": str, "error": str | None}.
    """
    try:
        resp = requests.get(url, headers=DEFAULT_HEADERS, timeout=timeout)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, "lxml")
        # Retirer scripts et styles
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        body = soup.find("body") or soup
        text = body.get_text(separator="\n", strip=True) if body else ""
        # Nettoyer lignes vides multiples
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        text = "\n".join(lines)
        return {"url": url, "text": text[:50000], "error": None}  # cap 50k chars par page
    except Exception as e:
        logger.warning("Scrape failed for %s: %s", url, e)
        return {"url": url, "text": "", "error": str(e)}


def scrape_urls(urls: list[str]) -> list[dict]:
    """
    Scrape une liste d'URLs et retourne une liste de {"url", "text", "error"}.
    """
    result = []
    for url in urls:
        if not url or not url.startswith(("http://", "https://")):
            result.append({"url": url or "", "text": "", "error": "URL invalide"})
            continue
        result.append(scrape_page(url))
    return result
