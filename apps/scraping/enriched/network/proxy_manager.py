"""
Proxy Manager — Gestion dynamique des profils réseau (récupéré SquidResearch).
Centralise la stratégie d’anonymisation des scrapers ENRICHED.
- Sélection de proxy par domaine (Tor strict, Tor relax, direct)
- Rotation automatique (NEWNYM) lorsque Tor est bloqué
- Interface unique pour tous les scrapers
"""
from __future__ import annotations

import logging
import os
import time
from collections import defaultdict
from dataclasses import dataclass
from threading import Lock
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse

try:
    from scrapper.idfinder.tor_manager import TorManager
except ImportError:
    TorManager = None

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ProxyStrategy:
    """Stratégie de connexion pour un domaine."""

    name: str
    use_tor: bool
    tor_required: bool = False
    rotate_on_fail: bool = True
    failure_threshold: int = 2
    jitter: Tuple[float, float] = (1.8, 1.2)
    fallback: Optional[str] = None
    headers: Optional[Dict[str, str]] = None


class ProxyManager:
    """Gestionnaire centralisé des stratégies proxy (SquidResearch)."""

    DEFAULT_STRATEGY = ProxyStrategy("tor_relaxed", use_tor=True, tor_required=False)

    STRATEGIES: Dict[str, ProxyStrategy] = {
        "tor_relaxed": ProxyStrategy(
            name="tor_relaxed",
            use_tor=True,
            tor_required=False,
            jitter=(2.0, 1.4),
            failure_threshold=3,
        ),
        "tor_strict": ProxyStrategy(
            name="tor_strict",
            use_tor=True,
            tor_required=True,
            jitter=(2.4, 1.6),
            failure_threshold=1,
        ),
        "tor_fallback_direct": ProxyStrategy(
            name="tor_fallback_direct",
            use_tor=True,
            tor_required=False,
            jitter=(2.2, 1.5),
            failure_threshold=2,
            fallback="direct",
        ),
        "direct": ProxyStrategy(
            name="direct",
            use_tor=False,
            tor_required=False,
            jitter=(1.4, 0.9),
            rotate_on_fail=False,
            failure_threshold=3,
        ),
    }

    DOMAIN_POLICY: Dict[str, str] = {
        "linkedin.com": "tor_strict",
        "www.linkedin.com": "tor_strict",
        "indeed.com": "tor_strict",
        "indeed.fr": "tor_strict",
        "apec.fr": "tor_relaxed",
        "welcometothejungle.com": "tor_relaxed",
        "jobteaser.com": "tor_relaxed",
        "pole-emploi.fr": "tor_relaxed",
        "monster.fr": "tor_fallback_direct",
        "glassdoor.com": "tor_fallback_direct",
        "kompass.com": "tor_strict",
        "fr.kompass.com": "tor_strict",
        "google.com": "tor_relaxed",
        "*": "tor_relaxed",
    }

    def __init__(self) -> None:
        self._failures: Dict[str, int] = defaultdict(int)
        self._last_rotation: float = 0.0
        self._lock = Lock()
        self.rotation_cooldown = int(os.getenv("TOR_ROTATION_COOLDOWN", "12"))

    def get_residential_proxy(self) -> Optional[Dict[str, str]]:
        """Proxy résidentiel (optionnel, si EnrichedProxyConfig disponible)."""
        try:
            from apps.scrapper.enriched.network.enriched_proxy_config import EnrichedProxyConfig
            config = EnrichedProxyConfig()
            return config.get_proxy_dict()
        except Exception:
            return None

    def get_strategy(self, domain: str) -> ProxyStrategy:
        domain = (domain or "").lower()
        base_domain = domain.lstrip("www.")
        strategy_name = (
            self.DOMAIN_POLICY.get(domain)
            or self.DOMAIN_POLICY.get(base_domain)
            or self.DOMAIN_POLICY.get("*")
        )
        strategy = self.STRATEGIES.get(strategy_name)
        return strategy or self.DEFAULT_STRATEGY

    def get_strategy_by_name(self, name: str) -> ProxyStrategy:
        return self.STRATEGIES.get(name, self.DEFAULT_STRATEGY)

    def record_success(self, domain: str) -> None:
        if domain in self._failures:
            self._failures.pop(domain, None)

    def record_failure(self, domain: str, status_code: Optional[int] = None) -> bool:
        strategy = self.get_strategy(domain)
        if not strategy.rotate_on_fail:
            return False
        with self._lock:
            self._failures[domain] += 1
            failure_count = self._failures[domain]
            logger.warning(
                "Proxy failure %s domain=%s status=%s count=%s",
                strategy.name, domain, status_code, failure_count,
            )
            if failure_count >= strategy.failure_threshold and strategy.use_tor:
                rotated = self._rotate_tor_identity(domain)
                if rotated:
                    self._failures[domain] = 0
                    return True
        return False

    def should_retry_with_fallback(self, strategy: ProxyStrategy) -> bool:
        return bool(strategy.fallback)

    def _rotate_tor_identity(self, domain: str) -> bool:
        now = time.time()
        if now - self._last_rotation < self.rotation_cooldown:
            logger.info("Rotation Tor ignorée (cooldown %ss)", self.rotation_cooldown)
            return False
        if TorManager is None:
            logger.debug("TorManager non disponible")
            return False
        if not TorManager.is_tor_running():
            logger.debug("Tor inactif")
            return False
        logger.info("Rotation identité Tor domain=%s", domain)
        success = TorManager.request_new_identity()
        if success:
            self._last_rotation = now
        return success

    @staticmethod
    def extract_domain(url: str) -> str:
        return urlparse(url).netloc.lower()


proxy_manager = ProxyManager()
