"""
CSS Vampire — extrait le style (polices, couleurs, logo, fonds) d'un site cible
pour reproduire une ambiance proche sur la landing et mettre le prospect à l'aise.

Usage : voir la commande manage.py css_vampire.
"""
import re
from collections import Counter
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# Timeout et User-Agent pour les requêtes
REQUEST_TIMEOUT = 15
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
SESSION_HEADERS = {"User-Agent": USER_AGENT}


def _get(url):
    """GET une URL et retourne le texte ou None."""
    try:
        r = requests.get(url, headers=SESSION_HEADERS, timeout=REQUEST_TIMEOUT)
        r.raise_for_status()
        r.encoding = r.apparent_encoding or "utf-8"
        return r.text
    except Exception:
        return None


def _resolve_url(base_url, href):
    """Rend href absolu par rapport à base_url."""
    if not href or href.startswith(("data:", "javascript:")):
        return None
    return urljoin(base_url, href)


def _collect_css(soup, page_url):
    """Récupère tout le CSS (inline + liens) et retourne une chaîne."""
    parts = []
    for tag in soup.find_all("style"):
        if tag.string:
            parts.append(tag.string)
    for link in soup.find_all("link", rel="stylesheet"):
        href = link.get("href")
        if not href:
            continue
        full_url = _resolve_url(page_url, href)
        if not full_url:
            continue
        css_text = _get(full_url)
        if css_text:
            parts.append(css_text)
    return "\n".join(parts)


def _extract_fonts(css_text):
    """Extrait les font-family du CSS. Retourne body et heading (première trouvée)."""
    # font-family: ... ; (gérer guillemets et virgules)
    pattern = re.compile(
        r"font-family\s*:\s*([^;]+?)\s*;",
        re.IGNORECASE | re.DOTALL,
    )
    fonts = []
    for m in pattern.finditer(css_text):
        raw = m.group(1).strip()
        # Ignorer les var(...) et valeurs non utilisables comme police
        if raw.startswith("var(") or not raw:
            continue
        parts = [p.strip().strip("'\"").strip() for p in re.split(r",\s*", raw)]
        if parts and parts[0].lower() not in ("inherit", "initial", "unset"):
            fonts.append(parts[0])
    if not fonts:
        return {}
    # La plus fréquente = probablement body
    counter = Counter(fonts)
    body_font = counter.most_common(1)[0][0]
    heading_font = body_font
    for f in fonts:
        if f != body_font and "sans" not in f.lower():
            heading_font = f
            break
    return {"body": body_font, "heading": heading_font}


def _normalize_color(raw):
    """Tente de normaliser une couleur en hex (#rrggbb)."""
    raw = (raw or "").strip().lower()
    if not raw:
        return None
    hex_match = re.match(r"#([a-f0-9]{3}|[a-f0-9]{6})\b", raw)
    if hex_match:
        h = hex_match.group(1)
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return f"#{h}"
    # rgb(r,g,b) -> hex approximatif
    rgb = re.match(r"rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", raw)
    if rgb:
        r, g, b = int(rgb.group(1)), int(rgb.group(2)), int(rgb.group(3))
        return f"#{r:02x}{g:02x}{b:02x}"
    # Noms courants
    names = {
        "white": "#ffffff", "black": "#000000", "transparent": None,
        "red": "#dc3545", "blue": "#0d6efd", "green": "#198754",
    }
    return names.get(raw)


def _extract_colors(css_text):
    """Extrait couleurs (background, color, border) et déduit primary/background/text."""
    colors = []
    for prop in ("background-color", "background", "color", "border-color", "border-top-color"):
        pattern = re.compile(
            rf"{re.escape(prop)}\s*:\s*([^;]+?)\s*;",
            re.IGNORECASE,
        )
        for m in pattern.finditer(css_text):
            raw = m.group(1).strip()
            if "url(" in raw or "gradient" in raw:
                continue
            c = _normalize_color(raw.split()[0] if raw else None) or _normalize_color(raw)
            if c:
                colors.append((prop, c))
    if not colors:
        return {}
    # Couleurs les plus présentes
    color_counts = Counter(c for _, c in colors)
    most_common = [c for c, _ in color_counts.most_common(12)]
    background = "#ffffff"
    text = "#111111"
    primary = "#0d6efd"
    for c in most_common:
        lum = _luminance(c)
        if lum < 0.25 and background == "#ffffff":
            background = c
        elif lum > 0.85 and text == "#111111":
            text = c
        elif 0.25 <= lum <= 0.75 and primary == "#0d6efd":
            primary = c
    # Site sombre : texte clair
    if _luminance(background) < 0.3:
        text = "#e6e6e6"
    return {
        "background": background,
        "text": text,
        "primary": primary,
        "secondary": _adjust_brightness(primary, 0.15),
    }


def _luminance(hex_color):
    """Luminance relative approximative (0 noir, 1 blanc)."""
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    if len(hex_color) != 6:
        return 0.5
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255
    return 0.299 * r + 0.587 * g + 0.114 * b


def _adjust_brightness(hex_color, factor):
    """Éclaircit (factor > 0) ou assombrit (factor < 0) une couleur hex."""
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    if len(hex_color) != 6:
        return hex_color
    delta = int(255 * max(-1, min(1, factor)))
    r = max(0, min(255, int(hex_color[0:2], 16) + delta))
    g = max(0, min(255, int(hex_color[2:4], 16) + delta))
    b = max(0, min(255, int(hex_color[4:6], 16) + delta))
    return f"#{r:02x}{g:02x}{b:02x}"


def _extract_logo(soup, page_url):
    """Cherche une image logo (classe/id logo, ou première img dans header)."""
    for sel in ("img.logo", ".logo img", "header img", "[class*='logo'] img", "a.logo img"):
        try:
            el = soup.select_one(sel)
            if el and el.get("src"):
                src = _resolve_url(page_url, el["src"])
                if src and not src.startswith("data:"):
                    return src
        except Exception:
            continue
    # Première image qui ressemble à un logo (pas trop grande)
    for img in soup.find_all("img", src=True)[:5]:
        src = _resolve_url(page_url, img["src"])
        if src and not src.startswith("data:") and "logo" in (img.get("alt") or "").lower():
            return src
    return None


def _extract_background_image(css_text, page_url):
    """Extrait la première URL de background-image (pour ambiance)."""
    pattern = re.compile(
        r"background(?:-image)?\s*:\s*url\s*\(\s*['\"]?([^)'\"]+)['\"]?\s*\)",
        re.IGNORECASE,
    )
    for m in pattern.finditer(css_text):
        url = m.group(1).strip().strip("'\"").strip()
        if url and not url.startswith("data:"):
            return url
    return None


def vampire(url):
    """
    Visite l'URL, extrait polices, couleurs, logo et retourne un thème réutilisable.

    Returns:
        dict: {
            "fonts": {"body": "...", "heading": "..."},
            "colors": {"background": "#...", "text": "#...", "primary": "#...", "secondary": "#..."},
            "logo_url": "https://..." ou None,
            "background_image_url": "https://..." ou None,
            "source_url": url
        }
    """
    parsed = urlparse(url)
    if not parsed.scheme:
        url = "https://" + url
    html = _get(url)
    if not html:
        return {"error": "Impossible de récupérer la page", "source_url": url}

    soup = BeautifulSoup(html, "lxml")
    css_text = _collect_css(soup, url)
    fonts = _extract_fonts(css_text)
    colors = _extract_colors(css_text)
    logo_url = _extract_logo(soup, url)
    bg_image = _extract_background_image(css_text, url)
    if bg_image:
        bg_image = _resolve_url(url, bg_image)

    return {
        "fonts": fonts,
        "colors": colors,
        "logo_url": logo_url,
        "background_image_url": bg_image,
        "source_url": url,
    }


def theme_to_css_vars(theme):
    """
    Convertit un thème vampire en variables CSS pour injection dans la landing.

    theme: dict retourné par vampire() (sans clé "error").
    Returns: str (contenu pour <style> :root { ... }).
    """
    if not theme or theme.get("error"):
        return ""
    lines = []
    fonts = theme.get("fonts") or {}
    if fonts.get("body"):
        lines.append(f"--lp-font-body: {fonts['body']}, system-ui, sans-serif;")
    if fonts.get("heading"):
        lines.append(f"--lp-font-heading: {fonts['heading']}, system-ui, sans-serif;")
    colors = theme.get("colors") or {}
    if colors.get("background"):
        lines.append(f"--lp-bg: {colors['background']};")
    if colors.get("text"):
        lines.append(f"--lp-text: {colors['text']};")
    if colors.get("primary"):
        lines.append(f"--lp-primary: {colors['primary']};")
    if colors.get("secondary"):
        lines.append(f"--lp-secondary: {colors['secondary']};")
    # Variables dérivées pour cohérence
    bg = colors.get("background") or "#0d0d0d"
    primary = colors.get("primary") or "#4a9eff"
    lum_bg = _luminance(bg)
    lum_primary = _luminance(primary)
    if lum_bg < 0.4:
        lines.append(f"--lp-border: {_adjust_brightness(bg, 0.15)};")
        lines.append(f"--lp-block-bg: {_adjust_brightness(bg, 0.08)};")
        lines.append("--lp-muted: #999;")
    else:
        lines.append(f"--lp-border: {_adjust_brightness(bg, -0.1)};")
        lines.append(f"--lp-block-bg: {_adjust_brightness(bg, -0.05)};")
        lines.append("--lp-muted: #666;")
    lines.append(f"--lp-heading: {colors.get('text') or '#fff'};")
    lines.append("--lp-cta-text: #fff;" if lum_primary < 0.5 else "--lp-cta-text: #0d0d0d;")
    if not lines:
        return ""
    return ":root {\n  " + "\n  ".join(lines) + "\n}"
