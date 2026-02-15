# Remplissage contenu — Portfolio Yuwell (rédaction, design, SEO)

**Date** : 2026-02-08  
**Statut** : 🟡 En cours  
**Pilote** : Chef de Projet  
**Objectif** : Remplir le contenu des 5 pages du portfolio Yuwell en mobilisant **Rédacteur**, **Designer** et **Expert SEO**. Source éditoriale et structure : `portfolio Yuwell_1.pdf` (Downloads) et `docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md`.

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both`). Réf. `git-remotes-github-gitlab.md`.

---

## Contexte

- Le portfolio Yuwell (étude graphique pour candidature graphiste) a sa **structure technique** en place : 5 pages (Présentation, Study case, Study case 2, Charte graphique, À propos), charte couleur Yuwell, nav commune.
- Les pages **Study case 2** et **À propos** sont des **placeholders** ; les textes des autres pages peuvent être **enrichis** à partir du PDF (formulations, structure des 3 cas, pitch « à propos »).
- Référence éditoriale : `docs/bonnes-pratiques.md` (éditorial anti-détection IA, humanisation). Pas de ton créatif ou artistique : **fonction, lisibilité, système**.

---

## Brief commun (PDF — points à intégrer)

- **Positionnement** : « Mon approche du design est orientée clarté, usage et cohérence. Je travaille des systèmes graphiques capables de s’adapter à des contextes techniques et internationaux, tout en restant humains et accessibles. »
- **3 cas suggérés dans le PDF** : (1) Refonte fiche produit médicale — (2) Mini design system Yuwell-like — (3) Notice ou support patient (schémas, pictogrammes, accessibilité). Le **Study case 1** actuel = système couleur par gamme ; **Study case 2** = à choisir parmi (1), (2) ou (3) ou combinaison.
- **Ton** : professionnel, structurant, pas de signature artistique ; contraintes médicales et internationales.

---

## Tâches par rôle

### Rédacteur (Responsible : textes, cohérence éditoriale)

- [ ] **Présentation** : Rédiger ou ajuster le paragraphe « Bienvenue » et les courts descriptifs des 4 cartes (Study case, Study case 2, Charte graphique, À propos) pour qu’ils soient clairs et alignés avec le PDF.
- [ ] **Study case 1** : Vérifier / enrichir les textes (Contexte & objectifs, Principes de design, Déclinaison par gamme, Règles d’usage, Bénéfices) à partir des formulations du PDF ; garder un ton sobre et professionnel.
- [ ] **Study case 2** : Rédiger le contenu de la page en s’appuyant sur le PDF (un des 3 cas : fiche produit, design system, notice patient). Structure proposée : Contexte → Contraintes → Réponse graphique → Résultat. Pas de texte « à compléter » en production.
- [ ] **Charte graphique** : Rédiger une courte intro au-dessus des tableaux (palette corporate + gammes) et une phrase de conclusion pour les règles d’usage si besoin.
- [ ] **À propos** : Rédiger la page « À propos de moi » (parcours, approche design, positionnement) en utilisant le pitch du PDF et les éléments fournis par l’utilisateur (bio, compétences, contact). Si des infos manquent, les demander à l’utilisateur ou poser des placeholders explicites.
- [ ] Appliquer les bonnes pratiques éditoriales (`docs/bonnes-pratiques.md`) : humanisation, pas de détection IA, orthographe/grammaire.

**Livrables** : Textes prêts à intégrer dans les templates (fichier de copy ou PR avec modifications des templates). Réf. `docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md`.

---

### Designer UI/UX (Responsible : visuel, hiérarchie, accessibilité)

- [ ] Vérifier la **hiérarchie visuelle** sur les 5 pages (titres, sous-titres, corps, légendes tableaux) ; cohérence avec la charte Yuwell (couleurs, Lato, espacements).
- [ ] **Study case 2** : Proposer la mise en page des blocs (Contexte, Contraintes, Réponse graphique, Résultat) en réutilisant les composants existants (section, section-head, card) ; pas de surcharge décorative.
- [ ] **À propos** : S’assurer que la page (bio, compétences, contact) est lisible et alignée avec le reste du portfolio (sections, cartes).
- [ ] Vérifier le **responsive** (mobile, tablette) et l’**accessibilité** (contrastes, titres, liens) sur toutes les pages Yuwell.

**Livrables** : Ajustements CSS/HTML si besoin ; validation visuelle des 5 pages. Réf. `templates/landing_pages/yuwell_*.html`, `apps/landing_pages/themes.py` (THEME_CSS_YUWELL).

---

### Expert SEO / AI-GEO (Responsible : métadonnées, titres, SEO)

- [ ] Définir les **titres de page** (balise `<title>`) et **meta description** pour les 5 pages (Présentation, Study case, Study case 2, Charte graphique, À propos) : mots-clés pertinents (ex. Yuwell, étude graphique, charte couleur, design system médical) sans sur-optimisation.
- [ ] Proposer des **titres H1 / H2** cohérents avec la structure et le SEO (un H1 par page, hiérarchie claire).
- [ ] Si pertinent : recommandations pour **balises meta** (og:title, description) en vue d’un partage ou d’un référencement ; documenter dans la base de connaissances ou dans ce sprint.

**Livrables** : Liste des titres et meta par page (ou modifications des templates / contexte vue). Réf. `expert-seo-ai-geo.mdc`, bonnes pratiques SEO du projet.

---

### Chef de Projet (Accountable : validation, coordination)

- [ ] Valider le brief et s’assurer que Rédacteur, Designer et Expert SEO ont accès au PDF et à `yuwell-portfolio-etude-graphique.md`.
- [ ] Valider les contenus rédigés et la mise en page avant intégration définitive.
- [ ] Mettre à jour ce document (statut, suivi) et `docs/logs/log-projet.md` en fin de phase.
- [ ] Enregistrer toute décision (choix du Study case 2, ton, SEO) dans `docs/base-de-connaissances/decisions.md` si nécessaire.

---

## Dépendances et ordre suggéré

1. **Rédacteur** et **Expert SEO** peuvent travailler en parallèle (SEO sur titres/meta, Rédacteur sur les textes).
2. **Designer** peut vérifier la hiérarchie et le responsive dès que les textes sont stabilisés (ou en parallèle sur la structure existante).
3. **Chef de Projet** valide les livrables et clôture le sprint.

---

## Fichiers à modifier (intégration contenu)

| Page | Template | Contexte (vue) |
|------|----------|----------------|
| Présentation | `yuwell_presentation.html` | `views.yuwell_presentation` — `content` (hero_headline, hero_sub_headline) ; textes en dur dans le template |
| Study case | `yuwell_study_case.html` | idem — textes en dur |
| Study case 2 | `yuwell_study_case_2.html` | idem — à remplir |
| Charte graphique | `yuwell_charte_graphique.html` | idem — intro/conclusion à ajouter |
| À propos | `yuwell_a_propos.html` | idem — à remplir |

Les titres de page (`content.page_title`) sont définis dans les vues (`views.py`) ; l’Expert SEO peut proposer des valeurs et le Dev Django ou le Rédacteur les intègrent dans la vue ou via un fichier de config si créé.

---

## Critères de succès

- [ ] Aucune page avec texte « à compléter » ou « Contenu à venir » en production (sauf décision explicite).
- [ ] Study case 2 : contenu rédigé (un cas parmi fiche produit / design system / notice patient) avec structure Contexte → Contraintes → Réponse → Résultat.
- [ ] À propos : bio / approche / contact rédigés (ou placeholders validés par le Chef de Projet).
- [ ] Titres et meta cohérents SEO sur les 5 pages.
- [ ] Hiérarchie visuelle et accessibilité validées par le Designer.
- [ ] Bonnes pratiques éditoriales respectées (`docs/bonnes-pratiques.md`).

---

## Références

- **Sprint dédié cas d’usage 1 & 2 (visuels, paid media)** : `segmentations/2026-02-09-sprint-contenu-cas-usage-1-2-yuwell-design-redaction.md` — visuels, rendus, concepts d’intégration produits ; propositions campagnes Meta, Pinterest, Google, Reddit.
- **Étude Yuwell** : `docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md`
- **Source PDF** : `portfolio Yuwell_1.pdf` (Downloads utilisateur — contenu résumé dans l’étude ci-dessus)
- **Templates** : `templates/landing_pages/yuwell_base.html`, `yuwell_presentation.html`, `yuwell_study_case.html`, `yuwell_study_case_2.html`, `yuwell_charte_graphique.html`, `yuwell_a_propos.html`
- **Vues** : `apps/landing_pages/views.py` (yuwell_*)
- **Registre / RACI** : `docs/base-de-connaissances/registre-agents-ressources.md`, `agents-roles-responsabilites.md`
- **Éditorial** : `docs/bonnes-pratiques.md` ; règle `editorial.mdc`

---

*Document créé pour coordonner le remplissage du contenu du portfolio Yuwell. Dernière mise à jour : 2026-02-08.*
