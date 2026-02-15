# Sprint — Contenu cas d’usage 1 & 2 (Yuwell) : visuels, intégrations produits, campagnes paid media

**Date** : 2026-02-09  
**Statut** : 🟡 En cours  
**Pilote** : Chef de Projet  
**Rôles mobilisés** : **Designer**, **Rédacteur** (coordination Chef de Projet).  
**Objectif** : Mettre en place le contenu des **cas d’usage 1 et 2** du portfolio Yuwell en commençant par la structure et les livrables : visuels, rendus et concepts d’intégration produits ; propositions pour campagnes **paid media** (Meta, Pinterest, Google, Reddit). **L’idéal est de mettre en application la charte graphique proposée** (celle du portfolio) sur tous les livrables.

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both`). Réf. `git-remotes-github-gitlab.md`.

---

## Charte graphique à appliquer

**Tous les livrables (visuels, rendus, concepts d’intégration produits, propositions paid media) doivent appliquer la charte graphique que tu leur proposes** — celle documentée dans le portfolio Yuwell :

- **Corporate** : Yuwell Red #E60012, Pure White #FFFFFF, Cool Gray #F5F5F5, Dark Charcoal #333333 ; cyan #00C2D1 (secondaire), bordure #90C2D3.
- **Par gamme** : Respiratoire (cyan, bleu), Diagnostic (vert), Soins à domicile (teal), Mobilité (gris + orange), Clinique/urgence (rouge alerte #C5281C — usage strict).
- **Typo** : Work Sans (poids 100–700), hiérarchie nette ; règles d’usage (une gamme = une couleur dominante, max 2 couleurs de gamme par support, contraste et accessibilité).
- **Icônes** : décliner en style **fil de fer / ultra thin** (outline, trait fin). Ressources gratuites médical / produit : Health Icons (CC0), Lineicons (MIT), Unicons thin line, Lucide ; voir `yuwell-portfolio-etude-graphique.md` § 6 et `docs/base-de-connaissances/icones-fil-de-fer-medical-product.md`.

**Références** : page **Charte graphique** du portfolio (`/yuwell/charte-graphique/`), `yuwell-portfolio-etude-graphique.md` § 3 et § 6, `apps/landing_pages/themes.py` (THEME_CSS_YUWELL, variables `--yuwell-*`).

---

## Contexte

- Le portfolio Yuwell a sa structure technique et sa charte en place. Les pages **Study case** (cas d’usage 1) et **Study case 2** (cas d’usage 2) doivent être alimentées en **contenu éditorial et visuel**.
- L’utilisateur souhaite y développer : **visuels**, **rendus et concepts d’intégration produits**, et **propositions pour campagnes paid media** (Meta, Pinterest, Google, Reddit), **en appliquant systématiquement la charte graphique proposée**.
- Ce sprint pose les bases : structure du contenu, brief commun Design + Rédaction, et premières livrables pour les deux cas d’usage.

**Référence** : `docs/base-de-connaissances/segmentations/2026-02-08-remplissage-contenu-portfolio-yuwell.md` (remplissage global) ; `docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md`.

---

## Périmètre du sprint

### Cas d’usage 1 (Study case)
- Contenu déjà partiellement en place (système couleur par gamme). À **enrichir** avec :
  - Visuels et rendus (mock-ups, intégrations produits)
  - Éventuelles propositions paid media en lien avec la gamme / l’identité

### Cas d’usage 2 (Study case 2)
- Contenu à **définir et remplir** (fiche produit, design system, notice patient ou autre — voir PDF et étude) avec :
  - Visuels, rendus et **concepts d’intégration produits**
  - **Propositions campagnes paid media** : Meta, Pinterest, Google, Reddit (formats, messages, visuels type bannières / carrés / stories selon plateforme)

---

## Segmentation des tâches

### Rédacteur (Responsible : textes, structure éditoriale)

- [ ] **Cas d’usage 1** : Vérifier / enrichir les textes existants pour intégrer les blocs « visuels & rendus » et « paid media » (intro, légendes, objectifs des campagnes) ; ton professionnel, aligné avec le PDF et `yuwell-portfolio-etude-graphique.md` ; **mentionner l’application de la charte graphique proposée** (système couleur par gamme, cohérence visuelle).
- [ ] **Cas d’usage 2** : Rédiger la structure et les textes (Contexte → Contraintes → Réponse graphique → Résultat) en incluant des **sections dédiées** : visuels / intégration produits ; propositions paid media (Meta, Pinterest, Google, Reddit) avec court brief par plateforme (objectif, cible, message, format), **en cohérence avec la charte** (identité, gammes).
- [ ] Rédiger les **descriptions et légendes** pour les visuels et rendus (intégration produits, concepts) que le Designer produira ou intégrera — en rappelant le lien avec la charte (gamme concernée, usage couleur).
- [ ] Appliquer les bonnes pratiques éditoriales (`docs/bonnes-pratiques.md`).

**Livrables** : Fichier de copy ou textes prêts pour les templates (Study case, Study case 2) ; brief paid media par plateforme (Meta, Pinterest, Google, Reddit) pour le Designer ; **texte qui porte la charte graphique proposée** (clarté, système, règles d’usage).

---

### Designer UI/UX (Responsible : visuels, rendus, concepts, maquettes paid media)

- [ ] **Appliquer la charte graphique proposée** à tous les livrables : couleurs corporate et par gamme, typo Work Sans, règles d’usage (voir section « Charte graphique à appliquer » ci-dessus).
- [ ] **Cas d’usage 1** : Proposer et intégrer **visuels, rendus et concepts d’intégration produits** (mock-ups, mises en situation) **en respect strict de la charte** (couleurs par gamme, hiérarchisation corporate → gamme → usage).
- [ ] **Cas d’usage 2** : Proposer et intégrer **visuels, rendus et concepts d’intégration produits** ; proposer des **maquettes ou specs visuelles** pour les campagnes paid media (Meta, Pinterest, Google, Reddit) : formats (carré, story, bannière, etc.), **charte appliquée** (couleurs, typo, lisibilité).
- [ ] S’assurer que la **mise en page** des deux pages (sections visuels, blocs paid media) est claire, responsive et accessible.
- [ ] Documenter ou livrer les **propositions paid media** (dimensions, recommandations visuelles par plateforme) dans le dossier contact ou la base de connaissances.

**Livrables** : Visuels et rendus intégrés ou livrés (assets), **tous conformes à la charte graphique proposée** ; propositions visuelles / maquettes paid media (Meta, Pinterest, Google, Reddit) appliquant la charte ; validation hiérarchie et responsive.

---

### Chef de Projet (Accountable : validation, coordination, dépendances)

- [ ] Valider le périmètre (cas 1, cas 2, visuels, paid media) et s’assurer que Designer et Rédacteur ont accès aux ressources (étude Yuwell, PDF, charte).
- [ ] **Contrôler les dépendances** : ordre des livrables (ex. brief Rédacteur → visuels Designer ; ou parallèle avec points de synchro).
- [ ] Valider les contenus et visuels avant intégration définitive.
- [ ] Mettre à jour ce document (statut, suivi) et `docs/logs/log-projet.md` en fin de phase.
- [ ] Enregistrer les décisions (choix Study case 2, formats paid media retenus) dans `docs/base-de-connaissances/decisions.md` si nécessaire.

---

## Dépendances et ordre suggéré

1. **Rédacteur** : rédiger la structure et les textes des deux cas (dont brief paid media par plateforme) → **Livrable 1**.
2. **Designer** : en parallèle ou après Livrable 1 — visuels, rendus, concepts d’intégration produits ; puis propositions visuelles paid media (Meta, Pinterest, Google, Reddit).
3. **Chef de Projet** : point de synchro après brief Rédacteur pour aligner Designer ; validation finale des livrables.

(Le Chef de Projet peut affiner l’ordre selon les disponibilités ; voir `agents-roles-responsabilites.md` § Contrôler les dépendances de tâches.)

---

## Fichiers et ressources concernés

| Élément | Fichier / ressource |
|--------|----------------------|
| Cas d’usage 1 | `templates/landing_pages/yuwell_study_case.html` |
| Cas d’usage 2 | `templates/landing_pages/yuwell_study_case_2.html` |
| Charte, palettes | `apps/landing_pages/themes.py` (THEME_CSS_YUWELL), `yuwell-portfolio-etude-graphique.md` |
| Éditorial | `docs/bonnes-pratiques.md` |
| Registre / RACI | `registre-agents-ressources.md`, `agents-roles-responsabilites.md` |

---

## Critères de succès

- [ ] **Charte graphique proposée appliquée** sur tous les livrables (visuels, rendus, concepts, paid media) : couleurs corporate et par gamme, typo Work Sans, règles d’usage.
- [ ] Cas d’usage 1 : contenu enrichi avec visuels / rendus / concepts d’intégration produits (et optionnellement amorce paid media), **conformes à la charte**.
- [ ] Cas d’usage 2 : contenu rédigé + visuels / rendus / concepts d’intégration produits + **propositions campagnes paid media** (Meta, Pinterest, Google, Reddit) documentées ou intégrées, **en application de la charte**.
- [ ] Designer et Rédacteur ont livré selon le brief ; Chef de Projet a validé.
- [ ] Décisions et livrables documentés (decisions.md, logs, ou dossier contact Yuwell).

---

## Références

- **Étude Yuwell** : `docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md`
- **Remplissage global** : `segmentations/2026-02-08-remplissage-contenu-portfolio-yuwell.md`
- **Règles éditoriales** : `docs/bonnes-pratiques.md` ; règle `editorial.mdc`
- **Design** : `design-brief-typo-portfolio-yuwell.md`, charte responsive (§ 5 bonnes-pratiques.md)

---

*Sprint créé pour coordonner Design et Rédaction sur les cas d’usage 1 et 2 (visuels, intégrations produits, paid media). Dernière mise à jour : 2026-02-09.*
