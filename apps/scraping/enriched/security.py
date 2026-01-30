"""
Sécurité enrichissement ENRICHED (inspiré SquidResearch apps/enrichment/security.py).
Rate limiting pour les opérations d’enrichissement (API, pipeline).
"""
import logging
import time
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

# Fallback in-memory (si Django cache non configuré)
_memory_counts: Dict[str, int] = {}
_memory_ts: Dict[str, float] = {}
_WINDOW = 60  # 1 minute


def _memory_get(key: str) -> int:
    now = time.time()
    if key in _memory_ts and now - _memory_ts[key] > _WINDOW:
        _memory_counts.pop(key, None)
        _memory_ts.pop(key, None)
    return _memory_counts.get(key, 0)


def _memory_incr(key: str) -> int:
    now = time.time()
    if key in _memory_ts and now - _memory_ts[key] > _WINDOW:
        _memory_counts[key] = 0
    _memory_counts[key] = _memory_counts.get(key, 0) + 1
    _memory_ts[key] = time.time()
    return _memory_counts[key]


class EnrichmentRateLimiter:
    """
    Rate limiting pour les opérations ENRICHED (SquidResearch).
    Utilise Django cache si disponible, sinon fallback mémoire.
    """

    def __init__(
        self,
        requests_per_minute: int = 10,
        burst_limit: int = 5,
        window_seconds: int = 60,
    ):
        self.requests_per_minute = requests_per_minute
        self.burst_limit = burst_limit
        self.window_size = window_seconds

    def is_allowed(
        self,
        identifier: str,
        operation_type: str = "default",
    ) -> tuple[bool, Dict[str, Any]]:
        """
        Vérifie si une requête est autorisée.
        Returns:
            (allowed, info_dict)
        """
        try:
            from django.core.cache import cache
            minute_key = f"rate_limit:{operation_type}:{identifier}:minute"
            burst_key = f"rate_limit:{operation_type}:{identifier}:burst"
            minute_count = cache.get(minute_key, 0)
            burst_count = cache.get(burst_key, 0)
            if minute_count >= self.requests_per_minute:
                return False, {
                    "reason": "minute_limit_exceeded",
                    "limit": self.requests_per_minute,
                    "current": minute_count,
                    "reset_in_seconds": cache.ttl(minute_key) or 60,
                }
            if burst_count >= self.burst_limit:
                return False, {
                    "reason": "burst_limit_exceeded",
                    "limit": self.burst_limit,
                    "current": burst_count,
                    "reset_in_seconds": 10,
                }
            cache.set(minute_key, minute_count + 1, timeout=60)
            cache.set(burst_key, burst_count + 1, timeout=10)
            return True, {
                "allowed": True,
                "remaining_minute": self.requests_per_minute - minute_count - 1,
                "remaining_burst": self.burst_limit - burst_count - 1,
            }
        except Exception:
            # Fallback : limite par mémoire
            key = f"{operation_type}:{identifier}"
            n = _memory_get(key)
            if n >= self.requests_per_minute:
                return False, {
                    "reason": "minute_limit_exceeded",
                    "limit": self.requests_per_minute,
                    "current": n,
                    "reset_in_seconds": _WINDOW,
                }
            _memory_incr(key)
            return True, {"allowed": True, "remaining_minute": self.requests_per_minute - n - 1}


# Instance par défaut (configurable via env si besoin)
enrichment_rate_limiter = EnrichmentRateLimiter(
    requests_per_minute=int(__import__("os").environ.get("ENRICHMENT_RPM", "30")),
    burst_limit=10,
)
