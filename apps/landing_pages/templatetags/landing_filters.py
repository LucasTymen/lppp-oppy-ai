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


def _youtube_video_id(value):
    """Extrait l'id vidéo d'une URL YouTube (watch ou embed). Retourne None si pas trouvé."""
    if not value or not isinstance(value, str):
        return None
    import re
    m = re.search(r"(?:v=|embed/)([a-zA-Z0-9_-]{11})", value.strip())
    return m.group(1) if m else None


@register.filter
def youtube_embed_background(value):
    """Transforme une URL YouTube (watch ou embed) en embed URL pour fond hero : autoplay, mute, loop, sans contrôles.
    Utilise youtube-nocookie.com (privacy-enhanced)."""
    vid = _youtube_video_id(value)
    if not vid:
        return value if value else ""
    return f"https://www.youtube-nocookie.com/embed/{vid}?autoplay=1&mute=1&loop=1&playlist={vid}&controls=0&rel=0&showinfo=0"


@register.filter
def youtube_embed_no_autoplay(value):
    """Embed YouTube (youtube-nocookie) SANS autoplay ni mute : évite souvent l'Erreur 153.
    Contrôles visibles, l'utilisateur clique sur lecture. À utiliser quand l'embed avec autoplay échoue."""
    vid = _youtube_video_id(value)
    if not vid:
        return value if value else ""
    return f"https://www.youtube-nocookie.com/embed/{vid}?autoplay=0&controls=1&rel=0&modestbranding=1"


@register.filter
def youtube_watch_url(value):
    """Retourne l'URL de visionnage YouTube (watch?v=ID) à partir d'une URL watch ou embed. Vide si pas YouTube."""
    vid = _youtube_video_id(value)
    if not vid:
        return ""
    return f"https://www.youtube.com/watch?v={vid}"


@register.filter
def youtube_thumbnail_url(value):
    """URL de la miniature YouTube (hqdefault, fiable). Afficher une image sans embed — contourne erreurs 151/153."""
    vid = _youtube_video_id(value)
    if not vid:
        return ""
    return f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"
