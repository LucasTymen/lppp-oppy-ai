"""
Pipeline d’enrichissement OSINT pour liste de prospects.
Alimente enriched_data, quality et score (intelligence métier).
Pilotable par Flowise / N8N via API ou tâches Celery.
Référence algorithmes : SquidResearch data_nodes + apps.intelligence.
"""
import logging
from typing import Any, Dict, List, Optional

from apps.intelligence.quality import prospect_completeness
from apps.intelligence.scoring import score_prospect

from .osint_sources import (
    get_default_sources,
    merge_enriched_results,
    MAX_SOURCES_PER_RUN,
)

logger = logging.getLogger(__name__)


def extract_domain_from_email(email: Optional[str]) -> Optional[str]:
    """Extrait un domaine plausible depuis un email (ex. user@acme.com -> acme.com)."""
    if not email or "@" not in email:
        return None
    return email.strip().split("@")[-1].lower()


def run_enrichment_pipeline(
    company_name: str = "",
    contact_name: Optional[str] = None,
    email: Optional[str] = None,
    domain: Optional[str] = None,
    sources: Optional[List[Any]] = None,
    max_sources: int = MAX_SOURCES_PER_RUN,
) -> Dict[str, Any]:
    """
    Exécute le pipeline d’enrichissement OSINT sur un prospect (une ligne).
    - Valide et normalise les entrées (guide-rails dans osint_sources).
    - Appelle chaque source (rate limit respecté), fusionne les résultats.
    - Calcule complétude et score via apps.intelligence.
    Retourne un payload compatible ENRICHEDEnrichmentNode et sauvegarde Prospect.
    """
    company_name = (company_name or "").strip()
    contact_name = (contact_name or "").strip() if contact_name else None
    email = (email or "").strip() if email else None
    if not domain and email:
        domain = extract_domain_from_email(email)

    sources = sources or get_default_sources()
    sources = sources[:max_sources]

    results: List[Dict[str, Any]] = []
    for src in sources:
        try:
            out = src.enrich(
                company_name=company_name,
                contact_name=contact_name,
                email=email,
                domain=domain,
            )
            results.append(out)
        except Exception as e:
            logger.warning("Source %s failed in pipeline: %s", getattr(src, "name", "?"), e)

    merged = merge_enriched_results(results)
    enriched_data: Dict[str, Any] = {
        "company": merged.get("company") or {},
        "contact": merged.get("contact") or {},
    }
    # Alimenter company/contact depuis entrées si vides
    if not enriched_data["company"].get("name") and company_name:
        enriched_data["company"]["name"] = company_name
    if not enriched_data["contact"].get("name") and contact_name:
        enriched_data["contact"]["name"] = contact_name
    if not enriched_data["contact"].get("email") and email:
        enriched_data["contact"]["email"] = email

    comp = prospect_completeness(
        company_name=company_name,
        contact_name=contact_name or "",
        email=email or "",
        enriched_data=enriched_data,
    )
    score = score_prospect(
        has_email=comp["has_email"],
        has_company=comp["has_company"],
        has_contact_name=comp["has_contact"],
        enriched_completeness=comp["enriched_completeness"],
    )

    payload: Dict[str, Any] = {
        "company_name": company_name,
        "contact_name": contact_name or "",
        "email": email or "",
        "enriched_data": enriched_data,
        "quality": comp,
        "score": score,
    }
    logger.info(
        "Pipeline run company=%s score=%.0f",
        company_name or "(empty)",
        score,
    )
    return payload


def run_batch_enrichment(
    rows: List[Dict[str, Any]],
    company_key: str = "company_name",
    contact_key: str = "contact_name",
    email_key: str = "email",
    domain_key: Optional[str] = "domain",
) -> List[Dict[str, Any]]:
    """
    Enrichit une liste de prospects (ex. CSV importé, webhook N8N).
    Chaque ligne est un dict avec company_key, contact_key, email_key (et optionnellement domain_key).
    Retourne la liste des payloads enrichis (enriched_data, quality, score).
    """
    out: List[Dict[str, Any]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        company = row.get(company_key) or row.get("company") or ""
        contact = row.get(contact_key) or row.get("contact")
        email = row.get(email_key) or row.get("email")
        domain = row.get(domain_key) if domain_key else None
        payload = run_enrichment_pipeline(
            company_name=company,
            contact_name=contact,
            email=email,
            domain=domain,
        )
        out.append(payload)
    return out
