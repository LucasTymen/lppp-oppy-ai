"""
Qualité des données : complétude, cohérence, normalisation.
Alimente le scoring et les stratégies d’affichage (contenus rédigés).
"""
import re
import unicodedata
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

# Regex email basique (éviter les faux positifs courants)
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def is_valid_email(value: str) -> bool:
    """Retourne True si la chaîne ressemble à un email valide."""
    if not value or not isinstance(value, str):
        return False
    return bool(EMAIL_REGEX.match(value.strip()))


def normalize_company_name(name: Optional[str]) -> str:
    """Normalise un nom d’entreprise : strip, lowercase, suppression accents optionnelle."""
    if not name or not isinstance(name, str):
        return ""
    s = name.strip()
    if not s:
        return ""
    # Option : enlever accents pour comparaison (conservative)
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s


def normalize_contact_name(name: Optional[str]) -> str:
    """Normalise un nom de contact : strip, espaces multiples collapsés."""
    if not name or not isinstance(name, str):
        return ""
    return " ".join(name.strip().split())


def prospect_completeness(
    *,
    company_name: str = "",
    contact_name: str = "",
    email: str = "",
    enriched_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Retourne des indicateurs de complétude pour un prospect.
    Utilisé pour le scoring et les rapports qualité.
    """
    enriched = enriched_data or {}
    has_company = bool(normalize_company_name(company_name))
    has_contact = bool(normalize_contact_name(contact_name))
    has_email = is_valid_email(email)
    # Complétude enriched : présence de clés utiles (ex. company, contact)
    enriched_keys = set(enriched.keys()) if isinstance(enriched, dict) else set()
    enriched_score = 0.0
    if "company" in enriched_keys:
        enriched_score += 0.5
    if "contact" in enriched_keys:
        enriched_score += 0.5

    return {
        "has_company": has_company,
        "has_contact": has_contact,
        "has_email": has_email,
        "enriched_completeness": enriched_score,
        "company_normalized": normalize_company_name(company_name),
        "contact_normalized": normalize_contact_name(contact_name),
    }
