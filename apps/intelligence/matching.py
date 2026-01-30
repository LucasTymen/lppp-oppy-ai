"""
Matching : prospect ↔ landing page, normalisation, proposition de contenu.
Réutilisé par campaigns, landing_pages et pipelines d’enrichissement.
"""
import logging
from typing import Optional, TYPE_CHECKING

from apps.intelligence.quality import (
    normalize_company_name,
    normalize_contact_name,
    prospect_completeness,
)
from apps.intelligence.scoring import score_prospect

if TYPE_CHECKING:
    from apps.campaigns.models import Prospect
    from apps.landing_pages.models import LandingPage

logger = logging.getLogger(__name__)


def get_prospect_score(prospect: "Prospect") -> float:
    """Calcule le score de qualité d’un prospect (0–100)."""
    comp = prospect_completeness(
        company_name=prospect.company_name or "",
        contact_name=prospect.contact_name or "",
        email=prospect.email or "",
        enriched_data=prospect.enriched_data if hasattr(prospect, "enriched_data") else None,
    )
    return score_prospect(
        has_email=comp["has_email"],
        has_company=comp["has_company"],
        has_contact_name=comp["has_contact"],
        enriched_completeness=comp["enriched_completeness"],
    )


def best_landing_for_prospect(
    prospect: "Prospect",
    candidates: Optional[list] = None,
) -> Optional["LandingPage"]:
    """
    Retourne la landing page la plus adaptée pour ce prospect.
    - Si le prospect a déjà une landing liée (OneToOne), on la retourne.
    - Sinon, parmi les candidates fournies (ou campagnes), on peut choisir par template_key,
      score, ou première disponible (logique extensible).
    """
    from apps.landing_pages.models import LandingPage

    if hasattr(prospect, "landing_page") and prospect.landing_page_id:
        return prospect.landing_page

    if not candidates:
        return None

    # Pour l’instant : première candidate publiée, sinon première tout court
    for lp in candidates:
        if isinstance(lp, LandingPage) and getattr(lp, "is_published", False):
            return lp
    return candidates[0] if candidates else None


def prospect_matches_landing(
    prospect_company: str,
    prospect_contact: str,
    landing_prospect_company: str = "",
    landing_prospect_name: str = "",
) -> bool:
    """
    Indique si les champs prospect correspondent à ceux de la landing (après normalisation).
    Utile pour vérifier la cohérence ou proposer une mise à jour du contenu.
    """
    nc = normalize_company_name(prospect_company)
    ncontact = normalize_contact_name(prospect_contact)
    lc = normalize_company_name(landing_prospect_company)
    ln = normalize_contact_name(landing_prospect_name)
    company_ok = nc == lc if (nc and lc) else True
    contact_ok = ncontact == ln if (ncontact and ln) else True
    return company_ok and contact_ok
