# Sprint général — Générer la page complète FitClem (landing multipage + infographie)

**Nom du livrable** : **LPPP-FitClem**.

**Date** : 2026-01-30  
**Statut** : 🟡 En cours  
**Pilote** : **Chef de Projet**. **Orchestrateur** : s’assurer que chaque rôle livre sa part.  
**Sprint de référence** : `2026-02-09-sprint-general-fitclem-landing-multipage.md` (structure cible, rôles de base).

**Règle Git** : En clôture, **commit + push sur les deux remotes** (origin + gitlab). Réf. `git-remotes-github-gitlab.md`.

---

## 1. Objectif

**Générer la landing multipage FitClem complète** : toutes les pages remplies avec le contenu réel (plus de placeholder sur l’étude SEO), CTA sur chaque page, et **une infographie autonome** (chiffres clés manque à gagner) produite par InfographicCraft pour renforcer la page Étude SEO et le dossier candidature.

**Périmètre « page complète »** :
- **Accueil** : hero, intro candidature, liens vers les 4 études + CTA.
- **Étude marketing** : contenu depuis `strategie-marketing-fitclem.md` (PESTEL, SWOT, Porter, concurrentiel, growth).
- **Étude SEO** : **contenu réel** depuis `rapport-seo-fitclem-manque-a-gagner.md` (pertes directes, chiffrage, actions prioritaires, argument candidature) + **lien ou intégration** vers l’infographie (fichier HTML autonome).
- **Étude iconographique et graphique** : palette, typo, codes visuels, quick wins (recherche FitClem).
- **Proposition KPI** : 6 KPI, plan 30/60 j, CTA contact.
- **Infographie** : un fichier `infographie-manque-a-gagner.html` (ou équivalent) dans `docs/contacts/fitclem/`, prêt à être ouvert en standalone ou lié depuis la page Étude SEO.

---

## 2. Rôles et tâches (ordre d’exécution)

### 2.1 Orchestrateur

- [ ] Rappeler à chaque rôle sa part et les **livrables attendus** (voir ci‑dessous).
- [ ] Vérifier que les **sources de contenu** sont bien utilisées (pas d’invention) : `strategie-marketing-fitclem.md`, `rapport-seo-fitclem-manque-a-gagner.md`, `audit-seo/`, `diapo-audit-seo-fitclem-structure.md`.
- [ ] Ne pas faire le travail à la place des autres : coordonner Rédacteur, Infographiste, Dev Django, Designer, Expert SEO.

### 2.2 Dev Django (structure en premier)

- [ ] **Créer les routes et vues** FitClem (sur le modèle Yuwell) :
  - `fitclem_presentation`, `fitclem_etude_marketing`, `fitclem_etude_seo`, `fitclem_etude_iconographique_graphique`, `fitclem_proposition_kpi`, (optionnel) `fitclem_contact`.
- [ ] **Templates** : base `fitclem_base.html` + une page par section, avec **blocs CTA** (lien section suivante + CTA contact).
- [ ] **URLs** : `fitclem/`, `fitclem/presentation/`, `fitclem/etude-marketing/`, `fitclem/etude-seo/`, `fitclem/etude-iconographique-graphique/`, `fitclem/proposition-kpi/`, (optionnel) `fitclem/contact/`.
- [ ] **Contexte** : préparer les variables de contexte pour que le Rédacteur puisse fournir le contenu (titres, blocs texte) ; pour l’étude SEO, prévoir un emplacement pour **lien vers infographie** (ou iframe selon choix Chef de Projet).
- **Référence** : `apps/landing_pages/views.py` (`_yuwell_common_context`, `yuwell_*`), `urls.py`, `templates/landing_pages/yuwell_*.html`.

### 2.3 Rédacteur (contenu pour toutes les pages)

- [ ] **Lire** : `strategie-marketing-fitclem.md`, **`rapport-seo-fitclem-manque-a-gagner.md`** (pour la page Étude SEO).
- [ ] **Rédiger** le contenu de **chaque page** :
  - **Accueil** : hero, intro candidature, liens vers les 4 études + CTA.
  - **Étude marketing** : synthèses PESTEL, SWOT, Porter, concurrentiel, growth & positionnement ; CTA.
  - **Étude SEO** : **contenu réel** — entonnoir percé, pertes directes (429, performance), opportunités SEO (H1, alt), tableau synthèse erreur → impact → action, **chiffrage** (11–27 k€/mois, 132–324 k€/an), argument candidature (« stabiliser le site », 150 k€/an). CTA + mention « Voir l’infographie » (lien vers `infographie-manque-a-gagner.html` ou équivalent).
  - **Étude iconographique et graphique** : palette (rose/orange), typo, codes visuels, quick wins ; CTA.
  - **Proposition KPI** : 6 KPI, plan 30/60 j, phrase de synthèse ; CTA contact.
- [ ] **Livrable** : `docs/contacts/fitclem/content-landing-fitclem.md` (ou structure équivalente) avec textes prêts pour intégration dans les templates. **Pas de placeholder** sur l’étude SEO : tout doit venir du rapport.

### 2.4 Infographiste (InfographicCraft) — infographie manque à gagner

- [ ] **Brief** (voir `brief-infographiccraft.md`) :
  - **THEME** : Audit SEO FitClem — manque à gagner et leviers prioritaires.
  - **AUDIENCE** : Recruteur (candidature Responsable Marketing Digital).
  - **TON** : Professionnel, factuel, percutant.
  - **SECTIONS** : Contexte entonnoir percé ; 3 pertes (4xx/429, lenteur, SEO) ; tableau synthèse k€/mois et k€/an ; 3 actions prioritaires ; argument candidature.
  - **DATA** : `docs/contacts/fitclem/rapport-seo-fitclem-manque-a-gagner.md` (84 URL 4xx, Speed Index 10,6 s, LCP 4,1 s, 11–27 k€/mois, 132–324 k€/an, argument « 150 k€/an »).
  - **CONSTRAINTS** : 1 couleur primaire + 1 accent, print-friendly, pas d’invention de chiffres.
- [ ] **Sortie** : (1) Plan court (6–10 lignes), (2) **fichier complet** `infographie-manque-a-gagner.html` déposé dans **`docs/contacts/fitclem/`** (HTML + CSS + JS inline, vanilla, autonome).

### 2.5 Designer

- [ ] **Charte visuelle** FitClem : rose poudré, orange CTA, moderne DTC — cohérence avec les codes marque sans copier à l’identique.
- [ ] **Navigation et CTA** : même logique que Yuwell (nav commune, emplacements CTA visibles sur chaque page).
- [ ] **Responsive** : mobile-first, lisibilité (bonnes pratiques § 5).
- [ ] **Livrable** : instructions ou modifications des templates FitClem (sections, CTA, couleurs) pour que Dev Django intègre.

### 2.6 Dev Django (intégration contenu + infographie)

- [ ] **Intégrer** les textes fournis par le Rédacteur dans les templates FitClem (contexte des vues, blocs template).
- [ ] **Page Étude SEO** : afficher le contenu réel (pertes, chiffrage, argument) et **lien clair** vers l’infographie (ex. « Télécharger / voir l’infographie » pointant vers le fichier statique ou une route qui sert `infographie-manque-a-gagner.html`). Décision Chef de Projet : lien de téléchargement, ouverture dans nouvel onglet, ou iframe.
- [ ] S’assurer que l’infographie est **accessible** depuis la landing (chemin static ou vue dédiée selon architecture retenue).

### 2.7 Expert SEO

- [ ] **Meta et titres** : title, description, H1/H2 pour chaque URL FitClem.
- [ ] **Page Étude SEO** : structure sémantique adaptée au contenu réel (titres, sous-titres, tableaux si présents).
- [ ] **Accessibilité et CTA** : ancres, libellés, bonnes pratiques.

### 2.8 Chef de Projet

- [ ] Valider la **structure** et l’ordre des livrables (structure → contenu → infographie → intégration).
- [ ] Décider comment **exposer l’infographie** depuis la page Étude SEO (lien fichier, iframe, ouverture nouvelle fenêtre).
- [ ] **Validation finale** : toutes les pages complètes, CTA présents, infographie livrée et liée.
- [ ] Mettre à jour `docs/logs/log-projet.md`, `docs/TODO.md` en fin de sprint. **Commit + push** sur les deux remotes en clôture.

---

## 3. Ordre de travail recommandé

1. **Dev Django** : créer routes, vues, templates de base FitClem (structure + nav + blocs CTA vides).
2. **Rédacteur** : rédiger tout le contenu (y compris page Étude SEO à partir de `rapport-seo-fitclem-manque-a-gagner.md`) → `content-landing-fitclem.md` (ou équivalent).
3. **InfographicCraft** : produire **plan** puis **`infographie-manque-a-gagner.html`** dans `docs/contacts/fitclem/` (brief ci‑dessus).
4. **Designer** : charte et emplacements CTA ; **Dev Django** : intégrer textes + lien/affichage infographie sur page Étude SEO.
5. **Expert SEO** : meta, titres, structure.
6. **Chef de Projet** : validation finale ; **Orchestrateur** : vérifier que chaque rôle a livré sa part.

---

## 4. Critères de succès (page complète)

- [ ] **5 à 6 pages** FitClem accessibles et **remplies** (plus de placeholder sur l’étude SEO).
- [ ] **Page Étude SEO** : contenu réel (entonnoir percé, chiffres, tableau, argument) + **lien ou accès** à l’infographie manque à gagner.
- [ ] **Infographie** : `docs/contacts/fitclem/infographie-manque-a-gagner.html` existant, autonome, print-friendly, données issues du rapport (pas d’invention).
- [ ] **CTA** sur chaque page (vers section suivante ou contact).
- [ ] **Design** cohérent, responsive, charte FitClem (rose/orange).
- [ ] **Commit + push** sur les deux remotes en clôture.

---

## 5. Fichiers et références

| Ressource | Emplacement |
|-----------|-------------|
| Stratégie marketing | `docs/contacts/fitclem/strategie-marketing-fitclem.md`, `strategie-marketing-fitclem-complet.md` |
| Rapport SEO / manque à gagner | `docs/contacts/fitclem/rapport-seo-fitclem-manque-a-gagner.md` |
| Structure diapo | `docs/contacts/fitclem/diapo-audit-seo-fitclem-structure.md` |
| Audit SEO (données brutes) | `docs/contacts/fitclem/audit-seo/` |
| Brief InfographicCraft | `docs/base-de-connaissances/brief-infographiccraft.md` |
| Modèle technique multipage | `views.py`, `urls.py`, `templates/landing_pages/yuwell_*` |
| Règle InfographicCraft | `.cursor/rules/infographiste-dataviz.mdc` |

---

*Sprint « générer la page complète » FitClem : landing multipage avec contenu réel (dont étude SEO) + infographie manque à gagner. Orchestrateur assure la coordination ; Chef de Projet valide en fin de sprint.*
