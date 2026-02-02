"""Filtres template pour les landing pages."""
from django import template

register = template.Library()


@register.filter
def as_list(value):
    """Si value est une chaîne, retourne [value] pour permettre une boucle unique ; sinon retourne value (liste)."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return value
