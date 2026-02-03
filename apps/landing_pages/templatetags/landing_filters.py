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


@register.filter
def mailto_to_email(value):
    """Extrait l'adresse email d'un lien mailto: (ex. mailto:xxx@yyy.com?subject=... → xxx@yyy.com). Pour afficher l'email en dur au lieu d'un lien."""
    if not value or not isinstance(value, str):
        return ""
    value = value.strip()
    if value.lower().startswith("mailto:"):
        value = value[7:].split("?")[0].strip()
    return value or ""
