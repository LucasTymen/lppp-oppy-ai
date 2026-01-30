from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseNode(ABC):
    """Noeud de traitement (pipeline données / enrichment)."""

    @abstractmethod
    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Exécute le noeud et retourne le payload enrichi."""
        pass
