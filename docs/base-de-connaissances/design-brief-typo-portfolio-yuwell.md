# Brief design — Typographie portfolio Yuwell (rapprochement yuwell-eu.com)

**Pour** : Designer UI/UX (rôle Designer, registre `registre-agents-ressources.md`).  
**Contexte** : Le portfolio Yuwell doit **se rapprocher du style yuwell-eu.com** (clean, pur, beaucoup de gris) tout en gardant notre **alternative couleur par gamme**. La typographie actuelle en était loin ; la demande est d’utiliser des **polices libres / Google Fonts** avec des **ultra fines (thin) et extra-light** pour coller à leur hiérarchie (corps très léger, titres marqués).

---

## 1. Référence : yuwell-eu.com

- **Style** : très clean, pur, fond sombre, palette gris / blanc.
- **Typo** : sans-serif neutre, moderne (esprit Helvetica / corporate EU). Hiérarchie nette :
  - Titres principaux : blanc, gros, bold.
  - Sous-titres : gris clair, medium.
  - **Corps de texte : très fin (thin / extra-light)** — aspect aéré et premium.
  - Titres de section parfois en très grand **outline** (contour fin) ; numéros de section (01, 02, 03) très grands.
- **Observation terrain** : les changements de rubrique sur yuwell-eu.com reposent sur **plusieurs familles** (ex. MiSans-Thin pour certains bandeaux, Oswald pour le body, etc. — **jusqu’à ~7 typo** selon les sections). Cohérence visuelle fragmentée.
- **Contrainte** : on ne vise pas la même fonderie exacte (souvent propriétaire) mais **un équivalent libre qui s’en rapproche**, avec **poids 100 (Thin) et 200 (ExtraLight)** disponibles. **Notre parti pris** : **une seule famille (Work Sans)** et hiérarchie par **poids**, pas par changement de fonderie.

---

## 2. Polices libres / Google Fonts recommandées (ultra fines)

Candidates avec **Thin (100)** et **ExtraLight (200)** sur Google Fonts :

| Police       | Poids dispo        | Style                    | Usage suggéré                    |
|-------------|--------------------|---------------------------|----------------------------------|
| **Work Sans** | 100–900            | Neutre, géométrique, proche Helvetica | **Retenu** : corps en 200/300, titres 600/700. |
| **Fira Sans**  | 100–900            | Humaniste, professionnel | Alternative si préféré par le Designer. |
| **Source Sans 3** | 200–900 (pas 100) | Adobe, corporate         | Alternative si 200 suffit pour « thin ». |
| **Encode Sans** | 100–900           | Plus technique           | Option secondaire.               |

**Validation Designer (appliqué)** : **Work Sans** (100, 200, 300, 400, 500, 600, 700) — chargement Google Fonts, variables `--lp-font-body` / `--lp-font-heading`. Hiérarchie : body 300, hero-sub 200, titres 600/700 ; classes `.yuwell-thin` (100) et `.yuwell-extralight` (200) pour usage ponctuel.

---

## 3. Rôle du Designer

- **Valider ou ajuster** le choix de fonderie (Work Sans vs Fira Sans vs Source Sans 3) selon le rendu sur les pages Yuwell.
- **Définir la hiérarchie** : quels blocs en 100, 200, 300 (body, hero-sub, légendes) et 600/700 (titres).
- **Accessibilité** : s’assurer que le texte en thin/extra-light reste lisible (contraste, taille min, fallback).
- **Documenter** dans ce fichier ou dans `yuwell-portfolio-etude-graphique.md` le choix final et les cas d’usage (ex. « Body : 300, hero-sub : 200, h2 : 600 »).

---

## 4. Fichiers impactés

- `apps/landing_pages/themes.py` : `THEME_YUWELL`, `THEME_CSS_YUWELL` (nom de police + stack).
- `templates/landing_pages/yuwell_base.html` : lien Google Fonts (poids 100, 200, 300, 400, 500, 600, 700), variables CSS, `font-weight` sur `.hero .hero-sub`, `.section p`, `body`, etc.
- `docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md` : paragraphe typo (référence à ce brief et choix Designer).

---

## 5. Livrables

- [x] Validation police : **Work Sans** appliquée (corps 300, hero-sub 200, titres 600/700).
- [x] Règles de poids documentées ci-dessus.
- [ ] Vérification lisibilité et accessibilité (contraste, taille min) — à confirmer par le Designer.

*Référence : registre `registre-agents-ressources.md` § Designer ; segmentations `2026-02-08-remplissage-contenu-portfolio-yuwell.md`.*
