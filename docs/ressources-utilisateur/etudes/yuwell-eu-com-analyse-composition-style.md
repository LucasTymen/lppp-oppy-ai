# Yuwell EU — Analyse composition, style et templates (référence portfolio)

**Objectif** : s’inspirer du site officiel [yuwell-eu.com](https://www.yuwell-eu.com/) pour aligner le portfolio LPPP sur leur esprit visuel et éditorial.  
**Page produit de référence** : [yuwell-eu.com — Product (categoryId=51)](https://www.yuwell-eu.com/#/product?categoryId=51&switchover=1) (Yuwell Medical Official Website).

---

## 1. Ce que l’on sait déjà (terrain et brief)

D’après les observations et le brief typo (`design-brief-typo-portfolio-yuwell.md`, `yuwell-portfolio-etude-graphique.md`) :

### 1.1 Style global

- **Ambiance** : très clean, pur, **fond sombre**, palette **gris / blanc**.
- **Positionnement** : corporate médical EU, sobre, premium.

### 1.2 Typographie

- **Plusieurs familles** selon les rubriques (jusqu’à ~7 typo) : MiSans-Thin, Oswald, etc.
- **Hiérarchie** :
  - Titres principaux : **blanc**, gros, bold.
  - Sous-titres : **gris clair**, medium.
  - **Corps** : très fin (thin / extra-light) — aspect aéré et premium.
  - Titres de section parfois en **très grand outline** (contour fin).
  - **Numéros de section** (01, 02, 03) **très grands**.
- **Exemples repérés** : bandeau « TECHNOLOGY AS THE FOUNDATION FOR PROGRESS » (MiSans-Thin), « NEWS CENTER », body en Oswald.

### 1.3 Composition

- **Sections** : rubriques marquées par des changements de typo et de mise en page.
- **Nav / structure** : site SPA (hash routing `#/product`, `#/`), navigation par catégories produits.

### 1.4 Technique (observé)

- **Polices** : MiSans-Thin, Oswald (body `font-family: Oswald, sans-serif`), autres selon blocs.
- **Couleurs** : `#686868` (gris texte bandeaux), `#555` (body), fond sombre.
- **CSS** : variables possibles (`--scrollHeight`, `--fontMargin`, `--header-height`), classes type `health-fotter-title`, `hidden-xs-only`.

---

## 2. Page produit / catégorie (categoryId=51)

**URL** : https://www.yuwell-eu.com/#/product?categoryId=51&switchover=1

- Page **catalogue / listing produit** par catégorie (51 = à identifier : ex. respiratoire, diagnostic, etc.).
- **À analyser manuellement** (site SPA, contenu chargé en JS) :
  - Structure de la page : hero / bannière, filtre catégories, grille ou liste produits.
  - Cartes produit : image, titre, sous-titre, CTA, badge.
  - Hiérarchie visuelle : titres vs corps, numéros, outline.
  - Couleurs : fond, cartes, texte, bordures, accents.
  - Espacements, grille, max-width, responsive.
  - Composants réutilisables : cards, boutons, liens, footer.

---

## 3. Checklist d’analyse (Designer + Chef de Projet)

À remplir avec **captures d’écran** et **notes** (à déposer dans `docs/ressources-utilisateur/etudes/` ou `docs/ressources-utilisateur/images/yuwell-eu/` si créé) :

| Élément | À noter |
|--------|---------|
| **Layout** | Grille (colonnes), max-width contenu, centrage, sections full-width vs boxed. |
| **Hero / bannière** | Hauteur, fond (image/vidéo/dégradé), titre + sous-titre, CTA. |
| **Cartes produit** | Ratio image, typo titre/prix/description, bordure, ombre, hover. |
| **Navigation** | Sticky, transparente ou fond, liens, dropdown catégories. |
| **Footer** | Blocs (texte type « TECHNOLOGY AS… »), liens, copyright. |
| **Typo** | Familles par zone, tailles, poids, outline/numéros. |
| **Couleurs** | Fond global, cartes, texte principal, texte secondaire, accent (rouge Yuwell ?). |
| **Responsive** | Comportement mobile (menu, grille 1 col, espacements). |

---

## 4. Principes à transposer dans le portfolio LPPP

- **Respiration** : beaucoup d’espace, corps très fin (extra-light), hiérarchie nette.
- **Fond** : possibilité de fond sombre ou très clair avec transparence (déjà en place : hero vidéo + sections en glass).
- **Numéros de section** : grands, bold, couleur accent (ex. 01, 02, 03).
- **Titres** : option outline ou très contrastés (blanc sur sombre / dark sur clair).
- **Cohérence** : on garde **une seule famille (Work Sans) + Oswald ExtraLight** en local pour le corps, pour un design system plus lisible que leurs 7 typo — tout en reprenant **l’esprit** (léger, aéré, sections marquées).
- **Produit** : si le portfolio inclut des « fiches produit » ou study case produit, s’inspirer de la **grille / cartes** et de la **hiérarchie** de la page produit yuwell-eu.com.

---

## 5. Références projet

- **Étude graphique** : `docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md`
- **Brief typo** : `docs/base-de-connaissances/design-brief-typo-portfolio-yuwell.md`
- **Sprint alignement** : `docs/base-de-connaissances/segmentations/2026-02-09-sprint-alignement-portfolio-yuwell-esprit-yuwell-eu.md`

*Document créé pour l’analyse de la page yuwell-eu.com et l’alignement du portfolio. Dernière mise à jour : 2026-02-09.*
