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

# Charte FitClem — Soft Wellness / girly (fitness & bien-être, candidature RMD)
# Source : brief graphiste (palette hex, typo Montserrat/Inter, bordures organiques, ombres légères)
THEME_FITCLEM = {
    "fonts": {"body": "Inter", "heading": "Montserrat"},
    "colors": {
        "background": "#FFFFFF",
        "text": "#1A1A1A",
        "primary": "#FF6633",
        "secondary": "#FFA385",
        "gray_light": "#F9F9F9",
    },
    "logo_url": None,
    "background_image_url": None,
}

THEME_CSS_FITCLEM = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@600;700&family=Pacifico&family=Delius&family=Sniglet:wght@400;800&display=swap');

:root {
  /* Charte FitClem — Soft Wellness / girly (d'après fitclem.fr) */
  --fitclem-orange: #FF6633;
  --fitclem-peach: #FFA385;
  --fitclem-white: #FFFFFF;
  --fitclem-black: #1A1A1A;
  --fitclem-gray-light: #F9F9F9;
  --fitclem-magenta: #D81B60;
  --fitclem-lavender: #B9A9D0;
  --fitclem-pastel-pink: #FFE4E1;
  --fitclem-green: #57B894;
  --fitclem-blue: #7EB8DA;
  /* Mapping LP */
  --lp-font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --lp-font-heading: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
  --lp-bg: #FFFFFF;
  --lp-text: #1A1A1A;
  --lp-primary: #FF6633;
  --lp-secondary: #FFA385;
  --lp-border: rgba(255, 102, 51, 0.35);
  --lp-block-bg: #F9F9F9;
  --lp-muted: #5c5c5c;
  --lp-heading: #1A1A1A;
  --lp-cta-text: #ffffff;
  --lp-font-delius: "Delius", cursive;
  --lp-font-sniglet: "Sniglet", system-ui, sans-serif;
  --lp-border-radius-soft: 50px;
  --lp-shadow-soft: 0 4px 15px rgba(0,0,0,0.05);
}

/* Empêcher scroll horizontal (hero 100vw) */
html, body { overflow-x: hidden !important; }

/* Bandeau promo top — style fitclem.fr (magenta, texte blanc, centré) */
.alert-banner {
  background: var(--fitclem-magenta) !important;
  color: var(--fitclem-white) !important;
  text-align: center !important;
  font-weight: 600 !important;
  letter-spacing: 0.5px !important;
}

/* Hero sans vidéo — fond lavande dégradé vers blanc (option Soft Wellness) */
.hero:not(.has-bg-image):not(.has-bg-video) {
  background: linear-gradient(180deg, var(--fitclem-lavender) 0%, var(--fitclem-pastel-pink) 40%, var(--fitclem-white) 100%) !important;
}

/* Hero vidéo 100% largeur viewport (supprime les barres noires) + parallaxe (vidéo fixe au scroll) */
.hero.has-bg-video {
  width: 100vw !important;
  max-width: 100vw !important;
  margin-left: calc(50% - 50vw) !important;
  overflow: hidden !important;
}
.hero.has-bg-video .hero-bg-video {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  min-width: 100vw !important;
  min-height: 100vh !important;
  z-index: 0 !important;
  pointer-events: none !important;
}
.hero.has-bg-video .hero-bg-video iframe,
.hero.has-bg-video .hero-bg-video video {
  width: 100vw !important;
  min-width: 100vw !important;
  min-height: 100vh !important;
  height: 56.25vw !important;
  max-height: none !important;
  object-fit: cover !important;
  left: 50% !important;
  top: 50% !important;
  transform: translate(-50%, -50%) !important;
}

/* Titres — blanc sur fonds colorés ; rose/magenta sur fond blanc (éviter texte sombre) */
h1 {
  font-family: var(--lp-font-delius) !important;
  font-weight: 400 !important;
  text-transform: none !important;
  letter-spacing: 0.5px !important;
  color: var(--fitclem-magenta) !important;
}
/* H2, H3, H4 : Delius (cursive) et Sniglet (rounded, playful) */
h2 {
  font-family: var(--lp-font-delius) !important;
  font-weight: 400 !important;
  text-transform: none !important;
  letter-spacing: 0.5px !important;
  color: var(--fitclem-magenta) !important;
}
h3, h4 {
  font-family: var(--lp-font-sniglet) !important;
  font-weight: 800 !important;
  text-transform: uppercase !important;
  letter-spacing: 1px !important;
  color: var(--fitclem-magenta) !important;
}
h4 { font-weight: 400 !important; text-transform: none !important; }
/* Hero : H1 et sous-titre en BLANC (priorité) */
.hero.has-bg-video h1,
.hero.has-bg-video .hero-sub,
.hero.has-bg-image h1,
.hero.has-bg-image .hero-sub {
  color: #fff !important;
  text-shadow: 0 1px 4px rgba(0,0,0,0.5), 0 2px 8px rgba(0,0,0,0.3) !important;
}
/* Sections fond rose : titres et texte en BLANC */
.section h2, .section .section-head .section-num { color: #fff !important; }

/* Boutons CTA — pill (border-radius 50px), uppercase, style FitClem */
.cta, .nav-cta, .hero .cta, .cta-wrap .cta {
  background-color: var(--fitclem-orange) !important;
  color: white !important;
  border-radius: 50px !important;
  text-transform: uppercase !important;
  font-weight: 700 !important;
  font-family: var(--lp-font-heading) !important;
  box-shadow: var(--lp-shadow-soft) !important;
  transition: transform 0.2s ease, background-color 0.2s ease !important;
}
.cta:hover, .nav-cta:hover, .hero .cta:hover, .cta-wrap .cta:hover {
  transform: scale(1.05) !important;
  background-color: #e55a2d !important;
}

/* Badge circulaire type "1er Prix Top Santé" — pour manque à gagner SEO */
.fitclem-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 120px;
  padding: 0.75rem 1.25rem;
  background: var(--fitclem-magenta) !important;
  color: white !important;
  border-radius: 50px !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
}

/* Manque à gagner — accent magenta */
.seo-manque {
  font-weight: 700 !important;
  color: var(--fitclem-magenta) !important;
}

/* Sections — fonds roses alternés avec écritures BLANCHES (plus de relief) */
.section {
  border-left: 5px solid rgba(255,255,255,0.5) !important;
  box-shadow: var(--lp-shadow-soft) !important;
  border-radius: 20px !important;
  color: #fff !important;
}
.section h2, .section .section-head, .section-num, .section-lead, .section p, .section .card,
.pain-list, .pain-list li, .coordonnees-intro, .coordonnees-list, .mission-flash-content,
.why-quote, .stack-label, .stack-tag, .seo-resume-card p, .seo-manque, .rapport-cta-link {
  color: #fff !important;
}
.section h2 { text-shadow: 0 1px 2px rgba(0,0,0,0.2); }
.section a:not(.cta):not(.nav-cta):not(.seo-cta) { color: rgba(255,255,255,0.95); text-decoration: underline; }
.section a:not(.cta):not(.nav-cta):not(.seo-cta):hover { color: #fff; }
/* Alternance nuances de rose */
.section:nth-of-type(4n+1) { background: var(--fitclem-magenta) !important; }
.section:nth-of-type(4n+2) { background: #CC3399 !important; }
.section:nth-of-type(4n+3) { background: var(--fitclem-lavender) !important; }
.section:nth-of-type(4n) { background: #E85A8A !important; }
/* Cards dans sections — léger overlay pour lisibilité */
.section .card {
  background: rgba(0,0,0,0.15) !important;
  border-color: rgba(255,255,255,0.3) !important;
}
/* Icebreaker et CTA wrap — fond clair : texte en ROSE (éviter contraste sombre) */
.icebreaker {
  background: var(--fitclem-peach) !important;
  color: var(--fitclem-magenta) !important;
  border-left: 5px solid var(--fitclem-magenta) !important;
}
.cta-wrap {
  background: linear-gradient(180deg, var(--fitclem-lavender) 0%, var(--fitclem-pastel-pink) 100%) !important;
  color: var(--fitclem-magenta) !important;
}
.cta-wrap .cta { color: #fff !important; }

/* Cards et blocs — formes organiques */
.section .card, .workflow-figure, .services-panel, .seo-resume-card {
  border-radius: 24px !important;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
}

/* Key figures carousel — texte lisible sur fond rose */
.section .key-figures-carousel { background: rgba(0,0,0,0.15) !important; border-color: rgba(255,255,255,0.4) !important; }
.section .kpi-value { color: #fff !important; }
.section .kpi-unit { color: var(--fitclem-peach) !important; }
.section .kpi-label { color: rgba(255,255,255,0.9) !important; }
.section .key-figures-nav button { border-color: rgba(255,255,255,0.8) !important; color: #fff !important; }
.section .key-figures-nav button:hover { background: rgba(255,255,255,0.3) !important; color: #fff !important; }
.section .key-figures-dots span { background: rgba(255,255,255,0.5) !important; }
.section .key-figures-dots span.active { background: #fff !important; }
.section .key-figures-timeline-item { background: rgba(0,0,0,0.15) !important; border-left-color: rgba(255,255,255,0.6) !important; }
.section .key-figures-timeline-item .t-period { color: #fff !important; }
.section .key-figures-timeline-item .t-desc { color: rgba(255,255,255,0.9) !important; }
.section .bar-val { color: #fff !important; }
/* Services tabs — onglet actif sur fond rose */
.section .services-tabs label { color: rgba(255,255,255,0.9) !important; }
.section .services-tabs input:checked + label { background: rgba(255,255,255,0.25) !important; color: #fff !important; border-color: rgba(255,255,255,0.5) !important; }

/* Lien étude SEO — style CTA */
.seo-cta {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: var(--fitclem-orange) !important;
  color: white !important;
  border-radius: 50px !important;
  text-transform: uppercase !important;
  font-weight: 600 !important;
  text-decoration: none !important;
  transition: transform 0.2s ease !important;
}
.seo-cta:hover {
  transform: scale(1.05) !important;
  color: white !important;
}

/* Contraste : zones fond blanc/clair → texte en ROSE (pas de texte sombre) */
body { color: var(--fitclem-black); }
.report-unavailable { color: var(--fitclem-magenta) !important; font-weight: 600; }

/* ===== Desktop : occuper l'espace, content players deux colonnes (brief § 4–5) ===== */
@media (min-width: 1024px) {
  /* Sections plus larges (1200px au lieu de 720px) */
  .section, .key-figures-section, .icebreaker {
    max-width: 1200px !important;
    width: 100% !important;
    padding: clamp(3rem, 6vw, 5rem) clamp(1.5rem, 4vw, 4rem) !important;
  }
  .icebreaker { max-width: 1200px !important; margin-left: auto !important; margin-right: auto !important; }

  /* Content player : layout deux colonnes (texte + visuel) */
  .section.content-player .section-head { grid-column: 1 / -1; }
  .section.content-player {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 2.5rem 3rem !important;
    align-items: start !important;
  }
  .section.content-player .content-player-text { grid-column: 1; }
  .section.content-player .content-player-visual { grid-column: 2; }
  .section.content-player.alt .content-player-text { grid-column: 2; order: 2; }
  .section.content-player.alt .content-player-visual { grid-column: 1; order: 1; }

  /* Card avec workflow-figure ou content-player-diagram : deux colonnes */
  .section .card:has(.workflow-figure),
  .section .card:has(.content-player-diagram) {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 2rem !important;
  }
  .section .card:has(.workflow-figure) > p,
  .section .card:has(.content-player-diagram) > p { margin: 0 !important; }
  .section .card:has(.workflow-figure) .workflow-figure,
  .section .card:has(.content-player-diagram) .content-player-diagram { margin: 0 !important; }

  /* Pain-list en grille 2 colonnes (enjeux) */
  .section#enjeux .pain-list {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 0 2rem !important;
  }

  /* Services : section élargie (content player déjà en place via tabs) */
  .section#services .services-tabs { gap: 1rem; }
  .section#services .services-panels { min-width: 0; }

  /* SEO : card + mini dashboard côte à côte (FitClem uniquement) */
  .section#resume-seo:has(.content-player-dashboard) {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 2rem !important;
  }
  .section#resume-seo:has(.content-player-dashboard) .section-head { grid-column: 1 / -1; }
  .section#resume-seo:has(.content-player-dashboard) .seo-resume-card { margin: 0; }
}

/* Section Solution segmentée (FitClem) — boxes + infographie pour rythmer */
.section.solution-segmented .solution-lead {
  margin-bottom: 1.5rem;
  font-size: 1.05rem;
  color: rgba(255,255,255,0.95) !important;
}
.solution-boxes {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.25rem;
  margin-bottom: 2rem;
}
.solution-box {
  padding: 1.25rem 1.5rem;
  background: rgba(0,0,0,0.2);
  border-radius: 16px;
  border-left: 4px solid rgba(255,255,255,0.5);
}
.solution-box-title {
  margin: 0 0 0.5rem 0 !important;
  font-size: 1rem !important;
  color: #fff !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
}
.solution-box-desc {
  margin: 0 !important;
  font-size: 0.95rem;
  line-height: 1.5;
  color: rgba(255,255,255,0.9) !important;
}
.solution-infographic {
  margin: 2rem 0;
  padding: 1.5rem;
  background: rgba(0,0,0,0.15);
  border-radius: 20px;
}
.solution-boxes-after { margin-bottom: 0; }
.solution-infographic-label {
  margin: 0 0 1rem 0 !important;
  font-size: 0.9rem !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  color: rgba(255,255,255,0.9) !important;
}
@media (min-width: 640px) {
  .solution-boxes { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 900px) {
  .solution-boxes { grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
}

/* Content player visuels — flowchart, dashboard (CSS pur) */
.content-player-flowchart {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 1rem;
  padding: 1.5rem;
  background: rgba(0,0,0,0.15);
  border-radius: 20px;
}
.content-player-flowchart .flow-step {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1rem;
  background: rgba(255,255,255,0.2);
  border-radius: 12px;
  font-size: 0.9rem;
  font-weight: 600;
  color: #fff;
}
.content-player-flowchart .flow-arrow { color: rgba(255,255,255,0.7); font-size: 1.2rem; }
.content-player-dashboard {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1.5rem;
  background: rgba(0,0,0,0.15);
  border-radius: 20px;
}
.content-player-dashboard .kpi-row {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.content-player-dashboard .kpi-label { flex: 0 0 120px; font-size: 0.9rem; }
.content-player-dashboard .kpi-bar {
  flex: 1;
  height: 12px;
  background: rgba(255,255,255,0.3);
  border-radius: 6px;
  overflow: hidden;
}
.content-player-dashboard .kpi-bar-fill {
  height: 100%;
  background: var(--fitclem-orange);
  border-radius: 6px;
}
.content-player-diagram {
  padding: 1.5rem;
  background: rgba(0,0,0,0.15);
  border-radius: 20px;
}
.content-player-diagram .process-steps {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.content-player-diagram .process-step {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.75rem 1rem;
  background: rgba(255,255,255,0.15);
  border-radius: 12px;
  font-size: 0.95rem;
  color: #fff;
}
.content-player-diagram .process-num {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--fitclem-orange);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.85rem;
}
"""

# Slug → (theme dict, theme_css string) pour injection côté vue
LANDING_THEMES = {
    "orsys": (THEME_ORSYS, THEME_CSS_ORSYS),
    "maisons-alfort": (THEME_MAISONS_ALFORT, THEME_CSS_MAISONS_ALFORT),
    "fitclem": (THEME_FITCLEM, THEME_CSS_FITCLEM),
}
