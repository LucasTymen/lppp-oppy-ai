"""
Sources OSINT pour enrichissement prospects (stratégie SquidResearch).
Guide-rails : validation entrées, rate limiting, pas d’exécution de code arbitraire.
ProxyManager (network.proxy_manager) optionnel pour stratégie Tor/domaine.
"""
import logging
import time
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


def get_proxy_strategy_for_domain(domain: Optional[str]) -> Optional[Any]:
    """
    Retourne la stratégie proxy SquidResearch pour un domaine (optionnel).
    Les sources qui font des requêtes HTTP peuvent l’utiliser (jitter, Tor, fallback).
    """
    try:
        from apps.scraping.enriched.network.proxy_manager import proxy_manager
        return proxy_manager.get_strategy(domain or "google.com")
    except Exception:
        return None

# Guide-rails : limites
MAX_COMPANY_NAME_LEN = 500
MAX_CONTACT_NAME_LEN = 200
MAX_EMAIL_LEN = 254
MAX_SOURCES_PER_RUN = 10
RATE_LIMIT_DELAY_SEC = 0.5  # délai minimum entre appels source


def _validate_company(company: Optional[str]) -> str:
    """Normalise et valide le nom d’entreprise (guide-rail)."""
    if company is None:
        return ""
    s = (company or "").strip()
    if len(s) > MAX_COMPANY_NAME_LEN:
        s = s[:MAX_COMPANY_NAME_LEN]
    return s


def _validate_contact(contact: Optional[str]) -> str:
    """Normalise et valide le nom de contact (guide-rail)."""
    if contact is None:
        return ""
    s = (contact or "").strip()
    if len(s) > MAX_CONTACT_NAME_LEN:
        s = s[:MAX_CONTACT_NAME_LEN]
    return s


def _validate_email(email: Optional[str]) -> str:
    """Valide longueur email (guide-rail)."""
    if email is None:
        return ""
    s = (email or "").strip()
    if len(s) > MAX_EMAIL_LEN:
        return ""
    return s


class BaseOSINTSource(ABC):
    """Source OSINT abstraite : entreprise et/ou contact."""

    name: str = "base"
    last_call_time: float = 0.0

    def _rate_limit(self) -> None:
        """Guide-rail : respect d’un délai minimal entre appels."""
        elapsed = time.monotonic() - self.last_call_time
        if elapsed < RATE_LIMIT_DELAY_SEC:
            time.sleep(RATE_LIMIT_DELAY_SEC - elapsed)
        self.last_call_time = time.monotonic()

    @abstractmethod
    def fetch_company(self, company_name: str, domain: Optional[str] = None) -> Dict[str, Any]:
        """Enrichit les données entreprise. Retourne un dict (company, site, sector, etc.)."""
        pass

    @abstractmethod
    def fetch_contact(
        self,
        company_name: str,
        contact_name: Optional[str] = None,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enrichit les données contact. Retourne un dict (name, title, email, linkedin, etc.)."""
        pass

    def enrich(
        self,
        company_name: str = "",
        contact_name: Optional[str] = None,
        email: Optional[str] = None,
        domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Point d’entrée unique : valide les entrées (guide-rails), applique rate limit,
        appelle fetch_company et fetch_contact, fusionne les résultats.
        """
        company_name = _validate_company(company_name)
        contact_name = _validate_contact(contact_name) if contact_name else None
        email = _validate_email(email) if email else None

        self._rate_limit()
        out: Dict[str, Any] = {"company": {}, "contact": {}, "source": self.name}
        try:
            if company_name:
                out["company"] = self.fetch_company(company_name, domain=domain)
            if company_name or contact_name or email:
                out["contact"] = self.fetch_contact(
                    company_name, contact_name=contact_name, email=email
                )
        except Exception as e:
            logger.warning("OSINT source %s failed: %s", self.name, e)
        return out


class PlaceholderOSINTSource(BaseOSINTSource):
    """
    Source factice pour tests et développement.
    Remplacer par des implémentations réelles (SquidResearch, APIs tierces).
    """

    name = "placeholder"

    def fetch_company(self, company_name: str, domain: Optional[str] = None) -> Dict[str, Any]:
        self._rate_limit()
        return {
            "name": company_name,
            "domain": domain or "",
            "sector": "",
            "size": "",
            "source": self.name,
        }

    def fetch_contact(
        self,
        company_name: str,
        contact_name: Optional[str] = None,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        self._rate_limit()
        return {
            "name": contact_name or "",
            "email": email or "",
            "title": "",
            "source": self.name,
        }


# Registre des sources par nom (pour flux décomposé : une tâche = une source)
SOURCE_REGISTRY: Dict[str, BaseOSINTSource] = {
    "placeholder": PlaceholderOSINTSource(),
}


def get_source(name: str) -> Optional[BaseOSINTSource]:
    """
    Retourne une source OSINT par son nom (pour tâche décomposée).
    Utilisé par enrich_prospect_single_source.
    """
    return SOURCE_REGISTRY.get(name)


def get_default_sources() -> List[BaseOSINTSource]:
    """
    Retourne la liste des sources OSINT utilisées par le pipeline.
    À étendre : instancier des sources réelles (APIs, scrapers SquidResearch).
    """
    return list(SOURCE_REGISTRY.values())


def merge_enriched_results(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Fusionne les résultats de plusieurs sources (company + contact).
    Les clés des sources suivantes écrasent les précédentes si non vides.
    """
    company: Dict[str, Any] = {}
    contact: Dict[str, Any] = {}
    for r in results:
        if isinstance(r.get("company"), dict):
            for k, v in r["company"].items():
                if v not in (None, ""):
                    company[k] = v
        if isinstance(r.get("contact"), dict):
            for k, v in r["contact"].items():
                if v not in (None, ""):
                    contact[k] = v
    return {"company": company, "contact": contact}
