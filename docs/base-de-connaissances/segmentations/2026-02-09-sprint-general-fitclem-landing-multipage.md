# Sprint général — Landing commerciale multipage FitClem (candidature)

**Date** : 2026-02-09  
**Statut** : 🟡 En cours  
**Pilote** : **Chef de Projet** (validation, livraison). **Orchestrateur** : s’assurer que **chacun fait sa part** (rédaction, design, dev, SEO) et que les tâches sont clairement réparties.

**Règle Git** : En clôture de livraison, **commit + push sur les deux remotes** (origin + gitlab). Réf. `git-remotes-github-gitlab.md`.

---

## 1. Objectif

Créer une **landing page commerciale multipage** pour la **candidature FitClem** (poste Responsable Marketing Digital), sur le modèle des landings multipages existantes (ex. portfolio Yuwell). La landing doit inclure :

- **Une partie étude marketing** (growth, positionnement, PESTEL, SWOT, Porter, concurrentiel)
- **Une partie étude SEO** (structure prête, **point d’attente** : données à fournir plus tard par l’utilisateur)
- **Une étude iconographique et graphique**
- **Une proposition d’amélioration des KPI**
- **Des CTA sur chaque page** (ne pas oublier les CTA)

**Source de contenu** : Toute la recherche est fournie dans `docs/contacts/fitclem/strategie-marketing-fitclem.md` (et fichier utilisateur initial en Downloads).

---

## 2. Structure des pages (cible)

| Page | URL (cible) | Contenu principal |
|------|-------------|-------------------|
| **Accueil / Présentation** | `/fitclem/` ou `/fitclem/presentation/` | Hero, contexte candidature, liens vers les 4 sections + CTA |
| **Étude marketing** | `/fitclem/etude-marketing/` | Growth, positionnement, PESTEL, SWOT, Porter, concurrentiel — CTA vers étude SEO / graphique / KPI |
| **Étude SEO** | `/fitclem/etude-seo/` | **Placeholder** : bloc "Étude SEO sémantique & axes d’amélioration — données et analyse à fournir". Structure et titres prêts. CTA |
| **Étude iconographique et graphique** | `/fitclem/etude-iconographique-graphique/` | Palette, typo, codes visuels, Ads Library, quick wins UI — CTA |
| **Proposition KPI** | `/fitclem/proposition-kpi/` | 6 KPI, plan 30/60 j, phrase de synthèse — CTA final (contact) |
| **Contact / CTA final** | Section sur dernière page ou page dédiée `/fitclem/contact/` | Coordonnées, prise de contact, CTA |

---

## 3. Rôles et tâches (Orchestrateur : répartir et suivre)

### 3.1 Orchestrateur

- [ ] **Diffuser** cette segmentation à tous les agents concernés (Chef de Projet, Rédacteur, Designer, Dev Django, Expert SEO).
- [ ] **Mettre à jour le registre** `registre-agents-ressources.md` : ajouter la ressource FitClem (dossier contact, sprint, stratégie marketing).
- [ ] **Rappeler** à chaque rôle sa part (voir ci‑dessous) et vérifier que les livrables sont déposés ou branchés (templates, textes, routes).
- [ ] **Ne pas faire** le travail à la place des autres : coordonner et s’assurer que Rédacteur rédige, Designer conçoit, Dev Django code, Expert SEO structure les meta/titres.

### 3.2 Chef de Projet

- [ ] Valider le **brief** et la structure des 5–6 pages avec l’utilisateur si besoin.
- [ ] S’assurer que **les CTA** sont présents sur chaque page (libellés, liens internes + CTA final contact).
- [ ] Valider les livrables (textes, maquette, templates, SEO) avant clôture.
- [ ] Mettre à jour `docs/logs/log-projet.md` et `docs/TODO.md` en fin de sprint.

### 3.3 Rédacteur

- [ ] **Lire** `docs/contacts/fitclem/strategie-marketing-fitclem.md` (source unique).
- [ ] **Rédiger** les textes pour chaque page :
  - **Accueil** : hero, intro candidature, liens vers les 4 études + CTA.
  - **Étude marketing** : synthèses PESTEL, SWOT, Porter, concurrentiel, growth & positionnement (en s’appuyant sur la stratégie marketing) ; CTA vers les autres sections.
  - **Étude SEO** : texte **placeholder** ("Données et analyse SEO à venir — structure prête pour intégration") + titres/sous-titres ; CTA.
  - **Étude iconographique et graphique** : palette (rose/orange), typo, codes visuels, quick wins UI (d’après la recherche) ; CTA.
  - **Proposition KPI** : 6 KPI, plan 30/60 j, phrase de synthèse ; CTA contact.
- [ ] **Ton** : professionnel, candidature Responsable Marketing Digital ; pas de promesses vagues.
- [ ] **Livrable** : textes dans un fichier (ex. `docs/contacts/fitclem/content-landing-fitclem.md`) ou directement proposés pour intégration dans les templates (coordination avec Dev Django / Designer).

### 3.4 Designer

- [ ] **Charte visuelle** : s’inspirer des codes FitClem (rose poudré, orange CTA, moderne DTC) pour la landing candidature — cohérence sans copier à l’identique.
- [ ] **Maquette / structure** : navigation commune (comme Yuwell), hiérarchie claire, **emplacements CTA** visibles (boutons, liens).
- [ ] **Responsive** : mobile-first, lisibilité (bonnes pratiques § 5).
- [ ] **Livrable** : instructions ou modifications des templates (base FitClem, sections, CTA) pour que Dev Django intègre.

### 3.5 Dev Django

- [ ] **Créer les routes et vues** pour FitClem (sur le modèle Yuwell) :
  - `fitclem_presentation` (accueil), `fitclem_etude_marketing`, `fitclem_etude_seo`, `fitclem_etude_iconographique_graphique`, `fitclem_proposition_kpi`, optionnel `fitclem_contact`.
- [ ] **Templates** : base commune `fitclem_base.html` + une page par section (`fitclem_presentation.html`, etc.), avec **blocs CTA** (lien vers section suivante + CTA final contact).
- [ ] **URLs** : `fitclem/`, `fitclem/presentation/`, `fitclem/etude-marketing/`, `fitclem/etude-seo/`, `fitclem/etude-iconographique-graphique/`, `fitclem/proposition-kpi/`, (optionnel) `fitclem/contact/`.
- [ ] **Contexte** : passer le contenu (texte, titres) aux templates ; pour l’étude SEO, contenu placeholder par défaut.
- [ ] **Référence** : `apps/landing_pages/views.py` (yuwell_*), `urls.py`, `templates/landing_pages/yuwell_*.html`.

### 3.6 Expert SEO

- [ ] **Structure des pages** : titres (H1, H2), meta (title, description) pour chaque URL FitClem.
- [ ] **Page étude SEO (placeholder)** : proposer la structure (titres, emplacements pour données à venir) pour que l’utilisateur puisse fournir l’étude SEO plus tard sans refonte.
- [ ] **Recommandations** : accessibilité, lisibilité, bonnes pratiques SEO sur les CTA (ancres, libellés).

---

## 4. Critères de succès

- [ ] **5 à 6 pages** accessibles (accueil, étude marketing, étude SEO placeholder, étude iconographique/graphique, proposition KPI, éventuellement contact).
- [ ] **CTA présents** sur chaque page (au moins un CTA par page vers une autre section ou vers contact).
- [ ] **Contenu** : étude marketing, étude iconographique/graphique et proposition KPI alimentées à partir de `strategie-marketing-fitclem.md` ; étude SEO = placeholder clair.
- [ ] **Design** : cohérent, responsive, charte FitClem (rose/orange) respectée.
- [ ] **Orchestrateur** : chaque rôle a bien réalisé sa part (rédaction, design, code, SEO).

---

## 5. Fichiers et références

| Ressource | Emplacement |
|-----------|-------------|
| Recherche / stratégie | `docs/contacts/fitclem/strategie-marketing-fitclem.md` |
| README contact | `docs/contacts/fitclem/README.md` |
| Modèle technique (multipage) | `views.py` (yuwell_*), `templates/landing_pages/yuwell_*.html`, `urls.py` |
| Règles éditorial / design | `docs/bonnes-pratiques.md`, `schema-landing-proposition.md` (CTA, structure) |

---

## 6. Ordre de travail suggéré

1. **Chef de Projet** : valider structure des pages et liste des CTA avec l’utilisateur.
2. **Dev Django** : créer routes, vues, templates de base (structure vide + nav) pour que Rédacteur et Designer aient des supports.
3. **Rédacteur** : rédiger les textes (source = strategie-marketing-fitclem.md) ; **Designer** : charte et emplacements CTA.
4. **Dev Django** : intégrer textes et mise en forme ; **Expert SEO** : meta, titres, structure page SEO placeholder.
5. **Chef de Projet** : validation finale ; **Orchestrateur** : vérifier que tout le monde a livré sa part.

---

*Sprint créé pour la landing candidature FitClem. L’Orchestrateur doit s’assurer que chacun fait sa part (rédaction, design, dev, SEO). Dernière mise à jour : 2026-02-09.*
