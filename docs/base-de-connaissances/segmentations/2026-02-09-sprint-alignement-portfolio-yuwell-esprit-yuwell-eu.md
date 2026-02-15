# Sprint — Alignement portfolio Yuwell sur l’esprit yuwell-eu.com

**Date** : 2026-02-09  
**Statut** : 🟡 En cours  
**Pilote** : **Chef de Projet** (dirige Webdesigner, Rédacteur, Dev)  
**Rôles mobilisés** : **Designer UI/UX (Webdesigner)**, **Rédacteur**, **Développeur Django**.

**Objectif** : Coller au plus près de l’esprit du site [yuwell-eu.com](https://www.yuwell-eu.com/) (composition, style, templates) en s’appuyant sur l’analyse de la page produit et du style global, tout en conservant la charte graphique proposée (couleurs par gamme, typo unique Work Sans + Oswald ExtraLight).

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both`). Réf. `git-remotes-github-gitlab.md`.

---

## Référence analysée

- **Document d’analyse** : `docs/ressources-utilisateur/etudes/yuwell-eu-com-analyse-composition-style.md`  
  - Composition, style, typo (MiSans-Thin, Oswald, titres outline, numéros 01/02/03), fond sombre, grille.
- **Page produit** : [yuwell-eu.com — Product categoryId=51](https://www.yuwell-eu.com/#/product?categoryId=51&switchover=1) — à analyser manuellement (captures, grille, cartes produit, footer).
- **Brief typo** : `docs/base-de-connaissances/design-brief-typo-portfolio-yuwell.md`.  
- **Charte à conserver** : `yuwell-portfolio-etude-graphique.md`, `themes.py` (THEME_CSS_YUWELL).

---

## Segmentation des tâches

### Chef de Projet (Pilote — Responsible : direction, validation, priorisation)

- [ ] **Brief** : Valider et diffuser l’analyse yuwell-eu.com (`yuwell-eu-com-analyse-composition-style.md`) et la checklist (layout, hero, cartes, nav, footer, typo, couleurs, responsive).
- [ ] **Priorisation** : Définir avec l’équipe les **3 à 5 principes** à transposer en priorité (ex. numéros de section grands, respiration, fond/transparence, hiérarchie titres).
- [ ] **Coordination** : S’assurer que Webdesigner et Rédacteur s’alignent sur les mêmes références ; que le Dev intègre les maquettes/CSS sans casser la charte.
- [ ] **Recette** : Valider les livrables (templates, textes, comportement) et clôturer le sprint (doc, logs, push Git).
- [ ] **Documentation** : Mettre à jour `decisions.md` et logs si décisions de design prises.

**Livrables** : Brief validé ; liste de principes priorisés ; validation finale ; mise à jour doc.

---

### Webdesigner / Designer UI/UX (Responsible : visuel, templates, cohérence)

- [ ] **Analyse** : Consulter la page produit yuwell-eu.com (et l’analyse) ; remplir la **checklist** (§ 3 de `yuwell-eu-com-analyse-composition-style.md`) — captures d’écran si utile, déposées dans `docs/ressources-utilisateur/` ou dossier dédié.
- [ ] **Principes** : Transposer dans le portfolio LPPP (templates Yuwell) :
  - **Respiration** : espacements, corps extra-light, hiérarchie nette.
  - **Numéros de section** : grands, bold, couleur accent (ex. 01, 02, 03) — adapter `.section-num` si besoin.
  - **Titres** : option outline ou contraste fort (blanc sur sombre / dark sur clair) en restant lisible.
  - **Fond** : garder transparence / glass déjà en place ; cohérence avec fond sombre/clair selon zones.
- [ ] **Templates** : Adapter `yuwell_base.html` et pages (présentation, study case, study case 2, charte, à propos) pour coller à l’esprit (grille, cartes, blocs) **sans** multiplier les typo — garder Work Sans + Oswald ExtraLight.
- [ ] **Cartes / blocs** : Si study case ou contenu type « produit », s’inspirer de la **grille et des cartes** de la page produit yuwell-eu.com (ratio image, typo, bordures).
- [ ] **Responsive** : Vérifier que les changements restent responsives (`bonnes-pratiques.md` § 5).
- [ ] **Charte** : Tous les visuels restent conformes à la charte graphique proposée (couleurs corporate + gammes, icônes fil de fer).

**Livrables** : Checklist d’analyse complétée ; modifications templates/CSS ; principes appliqués documentés (dans l’analyse ou le brief).

---

### Rédacteur (Responsible : textes, ton, structure éditoriale)

- [ ] **Référence** : Lire l’analyse yuwell-eu.com et le ton du site (corporate, médical, sobre) pour aligner le **ton** des textes du portfolio.
- [ ] **Structure** : Adapter si besoin les **titres et sous-titres** des sections (présentation, study case, study case 2, à propos) pour refléter une hiérarchie type yuwell-eu (accroches courtes, sous-titres gris/light).
- [ ] **Numéros** : Rédiger ou valider les libellés des sections numérotées (01, 02, 03…) en cohérence avec le design.
- [ ] **Cohérence** : Textes conformes à `docs/bonnes-pratiques.md` et à la charte (système couleur par gamme mentionné où pertinent).

**Livrables** : Textes mis à jour ou validés ; libellés sections/numéros ; ton aligné avec l’esprit yuwell-eu.

---

### Développeur Django (Responsible : intégration, données, technique)

- [ ] **Intégration** : Appliquer les changements de templates/CSS fournis par le Webdesigner (structure HTML, classes, variables CSS) sans régressions.
- [ ] **Données** : Si besoin, exposer en contexte vue les données pour numéros de section, titres, ou blocs « type produit » (ex. liste de gammes, cartes).
- [ ] **Statics** : S’assurer que les polices (Oswald dans `static/landing_pages/yuwell/fonts/`) et images Yuwell sont bien servies ; pas de 404.
- [ ] **Tests** : Vérifier les vues Yuwell (présentation, study case, study case 2, charte, à propos) et la nav ; pas d’erreur console ou template.
- [ ] **Git** : En clôture, commit + push sur les deux remotes (`make push-both`).

**Livrables** : Code intégré et testé ; statics OK ; push effectué.

---

## Ordre et dépendances

1. **Chef de Projet** : Valide et diffuse l’analyse + priorités (bloquant pour la suite).
2. **Webdesigner** : Analyse terrain + checklist → adaptations templates/CSS (en parallèle le Rédacteur peut lire l’analyse et ajuster le ton).
3. **Rédacteur** : Ajuste textes et libellés en cohérence avec la structure visuelle.
4. **Dev** : Intègre les maquettes et données après livrables Designer ; vérifie statics et vues.
5. **Chef de Projet** : Recette et clôture (doc, logs, validation Git).

---

## Critères de succès

- [ ] L’analyse yuwell-eu.com est documentée et la checklist remplie (ou complétée par le Designer).
- [ ] Au moins **3 principes** de l’esprit yuwell-eu (respiration, numéros de section, hiérarchie titres, fond/glass, grille/cartes) sont transposés dans le portfolio.
- [ ] La charte graphique proposée (couleurs, typo unique, icônes fil de fer) est respectée.
- [ ] Les 5 pages Yuwell s’affichent correctement, sont responsives et sans régression.
- [ ] Chef de Projet a validé ; commit + push effectués.

---

## Références

- **Analyse** : `docs/ressources-utilisateur/etudes/yuwell-eu-com-analyse-composition-style.md`
- **Étude graphique** : `docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md`
- **Brief typo** : `docs/base-de-connaissances/design-brief-typo-portfolio-yuwell.md`
- **RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Registre** : `docs/base-de-connaissances/registre-agents-ressources.md`

*Sprint créé pour aligner le portfolio Yuwell sur l’esprit yuwell-eu.com. Pilote : Chef de Projet. Dernière mise à jour : 2026-02-09.*
