"""
Noeuds de données et enrichment (inspiré SquidResearch ENRICHED).
Branche apps.intelligence pour qualité et scoring.
"""
import logging
from typing import Dict, Any

from apps.intelligence.quality import prospect_completeness
from apps.intelligence.scoring import score_prospect

from .base import BaseNode

logger = logging.getLogger(__name__)


class ENRICHEDEnrichmentNode(BaseNode):
    """Noeud d'enrichissement (données entreprise / contact) + qualité et score."""

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        company = payload.get("company_name") or payload.get("company")
        contact = payload.get("contact_name") or payload.get("contact")
        email = payload.get("email", "")
        enriched_data = payload.get("enriched_data") or {}
        out = dict(payload)
        out.setdefault("enriched_data", {})
        out["enriched_data"]["company"] = company
        out["enriched_data"]["contact"] = contact
        # Qualité et scoring (intelligence métier)
        comp = prospect_completeness(
            company_name=company or "",
            contact_name=contact or "",
            email=email,
            enriched_data=out["enriched_data"],
        )
        out["quality"] = comp
        out["score"] = score_prospect(
            has_email=comp["has_email"],
            has_company=comp["has_company"],
            has_contact_name=comp["has_contact"],
            enriched_completeness=comp["enriched_completeness"],
        )
        logger.info("ENRICHED node run for company=%s score=%.0f", company, out["score"])
        return out
