# Brief graphique FitClem — Soft Wellness / Girly

**Contexte** : Landing candidature Responsable Marketing Digital. Style **"Soft Wellness"** — douceur (soin/santé) + dynamisme (fitness). Référence visuelle : fitclem.fr (captures dans assets/).

**Appliqué** : Thème dans `apps/landing_pages/themes.py` (THEME_FITCLEM, slug `fitclem`). La vue injecte automatiquement la charte sur `/p/fitclem/`.

**Sprint graphique et éditorial** : `docs/base-de-connaissances/segmentations/2026-01-30-sprint-fitclem-graphique-editorial.md` — tâches détaillées pour alignement visuel et ton.

---

## 1. Palette de couleurs (Hex)

### Actuelle

| Usage | Variable | Hex |
|-------|----------|-----|
| Primaire (Action/CTA) | `--fitclem-orange` | `#FF6633` |
| Secondaire (Douceur) | `--fitclem-peach` | `#FFA385` |
| Fond & Pureté | `--fitclem-white` | `#FFFFFF` |
| Texte / Accent | `--fitclem-black` | `#1A1A1A` |
| Fond bloc | `--fitclem-gray-light` | `#F9F9F9` |

### Extensions (d’après fitclem.fr)

| Usage | Variable | Hex |
|-------|----------|-----|
| Bandeau promo / badges | `--fitclem-magenta` | `#CC3399` / `#D81B60` |
| Hero lavande | `--fitclem-lavender` | `#B9A9D0` |
| Fond pastel rose | `--fitclem-pastel-pink` | `#FFE4E1` / `#FFB6C1` |
| Badge vert | `--fitclem-green` | `#57B894` |
| Onglet Diagnostic | `--fitclem-blue` | `#7EB8DA` |

---

## 2. Typographie

- **Titres** : Montserrat (Bold 600–700), uppercase, letter-spacing 1px
- **Corps** : Inter (400–700)

---

## 3. Éléments iconographiques et formes

- **Bordures** : `border-radius` élevés (20px à 50px) — formes organiques, accueillantes
- **Boutons CTA** : `border-radius: 50px`, uppercase, effet hover `scale(1.05)`
- **Ombres** : légères `0 4px 15px rgba(0,0,0,0.05)`
- **Sections** : fond gris clair, bordure gauche 5px pêche

---

## 4. Joueur de contenu (content player)

**Objectif** : éviter des sections « plat et fade » avec uniquement du texte dans des boxes. Chaque section doit intégrer un **joueur de contenu** visuel, au-delà de la hero (qui reste top).

### 4.1 Principes

- **Pas que du texte** : chaque section associe texte + élément visuel (diagramme, schéma, graphique, mockup).
- **Mise en page deux colonnes** : texte à gauche (ou droite) + visuel à droite (ou gauche), pour exploiter la largeur desktop.
- **Référence** : maquettes Flowline/Framer (flowcharts, dashboards, comparaison avant/après, mockup mobile).

### 4.2 Exemples de content players par section

| Section | Content player proposé |
|---------|------------------------|
| Chiffres clés | Carrousel + graphiques en barres (132–324 k€) + timeline 30/60 j — déjà en place, à enrichir visuellement |
| Enjeux | Schéma type flowchart : Pain point → Impact → Solution (flèches, blocs) |
| Solution | Diagramme processus : Audit → Matrice créa → LP → A/B tests (ou équivalent) |
| Étude marketing | Comparaison « Sans vs Avec » (colonnes avec ✓ et ✗), ou matrice PESTEL/SWOT visuelle |
| Étude SEO | Mini dashboard : KPIs (LCP, 429, H1) + graphique évolution manque à gagner |
| Proposition KPI | Timeline horizontale 0–30 j / 30–60 j avec icônes et livrables par phase |
| Stack / Offre | Blocs visuels par compétence (icônes, tags) + CTA pill |

### 4.3 Livrables Designer

- [ ] Maquettes ou wireframes pour chaque content player (desktop + tablette + mobile).
- [ ] Spécifier les assets (icônes, illustrations) ou références (InfographicCraft, etc.).
- [ ] Coordonner avec Dev Django pour intégration dans `proposition.html` ou templates FitClem dédiés.

---

## 5. Occuper l’espace desktop (éviter le vide)

**Problème** : Sur desktop, beaucoup de marge vide à gauche et droite ; le contenu est centré en colonne étroite (ex. max-width 720px).

### 5.1 Recommandations

- **Sections pleine largeur** : `max-width: 100%` ou `max-width: 1200–1400px` selon le contenu ; padding latéral généreux.
- **Layout deux colonnes** : texte (40–50 %) + visuel (50–60 %) en `display: grid` ou `flex` sur desktop (min-width 1024px).
- **Alternance gauche/droite** : section 1 = texte gauche / visuel droite ; section 2 = visuel gauche / texte droite.
- **Espacement interne** : `clamp(3rem, 8vw, 6rem)` pour padding vertical ; `clamp(1.5rem, 4vw, 4rem)` pour padding horizontal.
- **Composant Flexpace** : zones d’espacement dédiées entre sections pour aérer sans créer du vide inutile — le contenu doit occuper la largeur utile.

### 5.2 Breakpoints cibles

| Breakpoint | Largeur contenu | Layout |
|------------|-----------------|--------|
| Mobile | 100 % − padding | Une colonne, empilé |
| Tablette (768px) | 100 % − padding | Une colonne ou début 2 col. |
| Desktop (1024px+) | 1100–1400px max | Deux colonnes, content players visuels |
| Large (1440px+) | 1200–1400px | Idem, marges latérales proportionnelles |

### 5.3 Fichiers à modifier

- `templates/landing_pages/proposition.html` : structure `.section` (grid/flex), max-width, breakpoints.
- `apps/landing_pages/themes.py` : THEME_CSS_FITCLEM — overrides pour sections FitClem (layout deux colonnes, largeur).

---

## 6. Fichiers concernés

- `apps/landing_pages/themes.py` : THEME_FITCLEM, THEME_CSS_FITCLEM
- Vue `landing_public` : injection automatique si `slug == "fitclem"`
- Template `proposition.html` : utilise `content.theme_css` si thème présent
