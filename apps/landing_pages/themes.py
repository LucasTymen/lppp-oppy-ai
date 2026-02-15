"""
Thèmes par partenaire (charte graphique) — ref. orsys.fr, 0flaw.fr, etc.
Utilisé par les commandes create_landing_* et par la vue pour forcer la charte quand slug connu.

Charte ORSYS : fond #FDFEFE, pas de vidéo hero embed, accent magenta, polices Lato.
"""

# Charte ORSYS (orsys.fr) — fond clair #FDFEFE, pas de vidéo de fond, accent magenta
THEME_ORSYS = {
    "fonts": {"body": "Lato", "heading": "Lato"},
    "colors": {
        "background": "#FDFEFE",
        "text": "#1a2d6b",
        "primary": "#d81b60",
        "secondary": "#26a69a",
    },
    "logo_url": "https://upload.wikimedia.org/wikipedia/fr/e/e3/LOGO_ORSYS_FRA_2025.png",
    "background_image_url": None,
}

THEME_CSS_ORSYS = """:root {
  --lp-font-body: Lato, system-ui, sans-serif;
  --lp-font-heading: Lato, system-ui, sans-serif;
  --lp-bg: #FDFEFE;
  --lp-text: #1a2d6b;
  --lp-primary: #d81b60;
  --lp-secondary: #26a69a;
  --lp-border: #2d4a8f;
  --lp-block-bg: #f0f4f8;
  --lp-muted: #5c6b7a;
  --lp-heading: #1a2d6b;
  --lp-cta-text: #ffffff;
}
"""

# Charte Maisons-Alfort (CSS Vampire) — fond sombre, primary #ac7fe8
THEME_MAISONS_ALFORT = {
    "fonts": {"body": "Roboto", "heading": "Roboto"},
    "colors": {
        "background": "#000000",
        "text": "#e6e6e6",
        "primary": "#ac7fe8",
        "secondary": "#d2a5ff",
    },
    "logo_url": "https://maisons-alfort.fr/wp-content/uploads/2018/12/logo-maisons-alfort.png",
    "background_image_url": "https://maisons-alfort.fr/wp-content/uploads/2022/02/bg-agenda.jpg?id=22720",
}

THEME_CSS_MAISONS_ALFORT = """:root {
  --lp-font-body: Roboto, system-ui, sans-serif;
  --lp-font-heading: Roboto, system-ui, sans-serif;
  --lp-bg: #000000;
  --lp-text: #e6e6e6;
  --lp-primary: #ac7fe8;
  --lp-secondary: #d2a5ff;
  --lp-border: #262626;
  --lp-block-bg: #141414;
  --lp-muted: #999;
  --lp-heading: #e6e6e6;
  --lp-cta-text: #0d0d0d;
}
"""

# Charte Yuwell (portfolio étude graphique) — palette officielle / étude PDF
# Typo : rapprochement yuwell-eu.com (clean, pur, thin/extra-light) — Work Sans 100–700, voir design-brief-typo-portfolio-yuwell.md.
# Couleurs : notre alternative structurante (rouge, cyan, gammes) ; yuwell-eu = beaucoup de gris.
THEME_YUWELL = {
    "fonts": {"body": "Work Sans", "heading": "Work Sans"},
    "colors": {
        "background": "#FFFFFF",
        "text": "#333333",
        "primary": "#E60012",
        "secondary": "#00C2D1",
        "neutral_light": "#F5F5F5",
        "border": "#90C2D3",
    },
    "logo_url": None,
    "background_image_url": None,
}

THEME_CSS_YUWELL = """:root {
  /* Typo — validation Designer : Work Sans */
  --lp-font-body: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  --lp-font-heading: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  /* Charte proposée — corporate */
  --lp-bg: #FFFFFF;
  --lp-text: #333333;
  --lp-primary: #E60012;
  --lp-secondary: #00C2D1;
  --lp-border: #90C2D3;
  --lp-block-bg: #F5F5F5;
  --lp-muted: #5c6b7a;
  --lp-heading: #333333;
  --lp-cta-text: #ffffff;
  /* Charte proposée — couleurs par gamme (étude yuwell-portfolio-etude-graphique.md) */
  --yuwell-respiratoire: #00C2D1;
  --yuwell-respiratoire-bleu: #0078A8;
  --yuwell-respiratoire-gris: #90C2D3;
  --yuwell-diagnostic: #57B894;
  --yuwell-diagnostic-vert: #3F8D68;
  --yuwell-diagnostic-desature: #AACFBF;
  --yuwell-soins-domicile: #4DA6A1;
  --yuwell-soins-domicile-clair: #8FC7C4;
  --yuwell-soins-domicile-gris: #BECFD1;
  --yuwell-mobilite: #7A7A7A;
  --yuwell-mobilite-orange: #E08E3C;
  --yuwell-urgence-alerte: #C5281C;
}
"""

# Slug → (theme dict, theme_css string) pour injection côté vue
LANDING_THEMES = {
    "orsys": (THEME_ORSYS, THEME_CSS_ORSYS),
    "maisons-alfort": (THEME_MAISONS_ALFORT, THEME_CSS_MAISONS_ALFORT),
}
