# Contraste textes / fond — règle graphiste (landings)

**Public** : Designer UI/UX & Front-End (graphiste), tout agent qui modifie le CSS des landings.  
**Objectif** : Appliquer partout et tout le temps une règle de contraste lisible et accessible.

---

## Règle unique

- **Fond clair** (blanc, pastel très clair, #F9F9F9, etc.) → **couleur de paragraphe sombre** (`--lp-text-on-light`, ex. `#1a1a1a`).
- **Fond foncé** (noir, magenta, bleu nuit, sections colorées sombres, etc.) → **couleur de paragraphe claire** (`--lp-text-on-dark`, ex. `#f5f5f5` ou `#fff`).

À appliquer à tous les blocs (sections, cards, icebreaker, CTA wrap, services, modales, etc.) et à tout le contenu texte des paragraphes (`p`, `.section-lead`, listes, cellules de tableau quand c’est du texte courant).

---

## Variables CSS à définir dans chaque thème

Dans le bloc `:root` du thème (ou dans la base si pas de thème) :

```css
--lp-text-on-light: #1a1a1a;   /* paragraphes sur fond clair */
--lp-text-on-dark: #f5f5f5;    /* paragraphes sur fond foncé */
```

Chaque thème peut surcharger ces valeurs (ex. noir pur `#000`, blanc pur `#fff`) selon la charte.

---

## Où l’appliquer

| Contexte | Fond | Couleur texte paragraphe |
|----------|------|---------------------------|
| `body` (landing fond blanc) | clair | `var(--lp-text-on-light)` |
| `body` (landing fond noir) | foncé | `var(--lp-text-on-dark)` |
| `.section` (sections colorées type magenta/bleu) | foncé | `var(--lp-text-on-dark)` |
| `.section#services .services-panel`, `.services-segment-box` | clair | `var(--lp-text-on-light)` |
| `.mission-flash`, `.why-quote`, `.stack-tag` (boxes fond blanc) | clair | `var(--lp-text-on-light)` |
| `.icebreaker`, `.cta-wrap` (fond pastel clair) | clair | `var(--lp-text-on-light)` |
| `.section .card` (overlay sur section colorée) | foncé | `var(--lp-text-on-dark)` |
| Infographies dans section (fond semi-transparent sombre) | foncé | `var(--lp-text-on-dark)` |
| Modales, nav (selon fond) | selon cas | `--lp-text-on-light` ou `--lp-text-on-dark` |
| **Sticky navbar** | fond = `--lp-bg` (clair pour FitClem, foncé pour Maisons-Alfort) | `.nav-links a`, `.nav a`, `.nav-waffle` : fond clair → `--lp-text-on-light`, fond foncé → `--lp-text-on-dark` |

Les **titres** (H1–H4) et **labels** (badges, tag-line, CTA) peuvent garder la couleur d’accent du thème ; seuls les **paragraphes et textes de lecture** suivent obligatoirement cette règle de contraste.

---

## Fichiers concernés

- `apps/landing_pages/themes.py` : chaque `THEME_CSS_*` doit définir `--lp-text-on-light` et `--lp-text-on-dark` et les utiliser pour tous les blocs à fond clair ou foncé.
- `templates/landing_pages/proposition.html` : le `:root` de base (hors thème) peut définir des valeurs par défaut.
- Exports statiques (ex. `deploy/LPPP-FitClem/index.html`) : garder les mêmes variables et règles si le CSS est dupliqué.

---

## Référence

- Décision projet : contraste systématique fond clair ↔ texte sombre, fond foncé ↔ texte clair (partout et tout le temps).
- Registre : `docs/base-de-connaissances/registre-agents-ressources.md` → Designer UI/UX & Front-End.
