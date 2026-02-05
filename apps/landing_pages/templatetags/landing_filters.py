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


@register.filter
def youtube_embed_background(value):
    """Transforme une URL YouTube (watch ou embed) en embed URL pour fond hero : autoplay, mute, loop, sans contrôles."""
    if not value or not isinstance(value, str):
        return ""
    value = value.strip()
    # Extraire l'id (watch?v=ID ou embed/ID)
    import re
    m = re.search(r"(?:v=|embed/)([a-zA-Z0-9_-]{11})", value)
    if not m:
        return value
    vid = m.group(1)
    return f"https://www.youtube.com/embed/{vid}?autoplay=1&mute=1&loop=1&playlist={vid}&controls=0&rel=0&showinfo=0"
