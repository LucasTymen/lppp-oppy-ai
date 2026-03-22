# Sprint LPPP-OppyAI — Orchestrateur, DevOps, Architecte, Designer, Rédacteur

**Date** : 2026-01-30  
**Pilote** : Orchestrateur  
**Statut** : 🟡 En cours

**Règle Git** : En clôture, **commit + push** sur origin et gitlab (`make push-both` ou `make commit-push MSG="..."`). Réf. `git-remotes-github-gitlab.md`.

---

## Contexte

Le projet **LPPP-OppyAI** est en phase de finalisation : landing Django avec animation Waves Pins, contenu JSON, charte graphique Oppy.ai. Ce sprint mobilise **cinq agents** pour livrer une landing propre, déployée et prête pour la prospection.

**Objectif** : coordonner Orchestrateur, DevOps, Architecte, Designer et Rédacteur pour livrer une landing Oppy-AI de qualité, avec repo dédié et déploiement vérifié.

---

## Équipes mobilisées

| Rôle | Responsabilité |
|------|----------------|
| **Orchestrateur** | Pilote le sprint, répartit les tâches, met à jour le registre, coordonne les dépendances. |
| **DevOps** | Git init/remotes, repo au nom de la société, déploiement (Vercel), vérification page OK. |
| **Architecte** | Structure technique, intégration (routes, vues, templates), points de défaillance, cohérence stack. |
| **Designer** | Charte graphique, infographie, positionnement-marketing, responsive, accessibilité, contraste. |
| **Rédacteur** | Textes, propositions de valeur, JSON, bonnes pratiques éditoriales, SEO. |

---

## Segmentation des tâches

### 1. Orchestrateur — Coordination

**Sources** : `registre-agents-ressources.md`, `agents-roles-responsabilites.md`, `procedure-fin-landing-repo-deploiement.md`

- [ ] **Piloter le sprint** : s'assurer que chaque agent connaît ses tâches et les dépendances.
- [ ] **Ordre des livrables** : Rédacteur → Designer (textes avant visuels) ; Architecte + DevOps en parallèle sur structure et déploiement.
- [ ] **Mettre à jour** `registre-agents-ressources.md` si nouvelles ressources ou rôles impliqués.
- [ ] **Mettre à jour** `log-projet.md` et `log-ia.md` à la clôture.
- [ ] Rappeler **commit + push** en fin de sprint (`make push-both`).

**Livrables** : Sprint coordonné, registre et logs à jour.

---

### 2. DevOps — Repo et déploiement

**Sources** : `procedure-fin-landing-repo-deploiement.md`, `strategie-deploiement-git-vercel.md`, `git-remotes-github-gitlab.md`

- [ ] **Créer le repo** au nom de la société (ex. `lppp-oppy-ai` ou `landing-opportunity-oppy-ai`) sur GitHub et GitLab.
- [ ] **Git init** (si besoin) et **premier commit** avec les fichiers landing.
- [ ] **Push** vers origin (GitHub) et gitlab (GitLab).
- [ ] **Configurer Vercel** (ou stack cible) : Root Directory si monorepo, variables d'env si besoin.
- [ ] **Vérifier le déploiement** : build OK, page accessible, pas d'erreur 404.
- [ ] **Documenter** : URL prod, nom du repo dans `docs/contacts/lppp-oppy-ai/README.md` ou `decisions.md`.

**Livrables** : Repo dédié, déploiement actif, page vérifiée.

**Réf** : RACI — DevOps R sur étapes 1–7 de la checklist fin de landing.

---

### 3. Architecte — Structure et intégration

**Sources** : `routes-back-lppp.md`, `infra-devops.md`, templates Django, `apps/landing_pages/`

- [ ] **Vérifier la cohérence des routes** : `/p/lppp-oppy-ai/`, `/p/lppp-oppy-ai/proposition/`, assets.
- [ ] **Vérifier la chaîne d'intégration** : vue → template → content JSON → thème Oppy.
- [ ] **Identifier les points de défaillance** : chargement Waves Pins (Three.js jsDelivr, static `waves-pins-hero.js`), fallback si erreur.
- [ ] **Tester l'animation Waves Pins** : lancer `make run` ou `python manage.py runserver 8010`, ouvrir http://localhost:8010/p/lppp-oppy-ai/ et /proposition/, vérifier que l'animation s'affiche et qu'il n'y a pas d'erreur 404 sur le script ou Three.js.
- [ ] **Structure des fichiers** : `landing-proposition-lppp-oppy-ai.json`, thème `THEME_OPPY_AI`, script `waves-pins-hero.js`.
- [ ] **Coordonner avec DevOps** : fichiers à inclure dans le premier commit, structure pour déploiement.

**Livrables** : Structure validée, documentation des flux et dépendances.

---

### 4. Designer — Charte, infographie, visuel

**Sources** : `charte-graphique-oppy-ai.md`, `theming-landing-prospect.md`, `contraste-textes-landing.md`, `infographie-lppp-oppy-ai-7-formats.html`, `positionnement-marketing.html`

- [ ] **Charte Oppy.ai** : appliquer palette (cyan #00C9D4, fond sombre), polices Inter/Montserrat.
- [ ] **Contraste** : fond sombre → texte clair (`--lp-text-on-dark`), vérifier lisibilité.
- [ ] **Infographie** (`infographie-lppp-oppy-ai-7-formats.html`) : cohérence visuelle, responsive, accessibilité.
- [ ] **Positionnement marketing** (`positionnement-marketing.html`) : hiérarchie visuelle, encarts, lisibilité.
- [ ] **Animation Waves Pins** (héritée CodePen Sabo Sugi) : vérifier z-index, overlay, contenu au-dessus (main, nav).
- [ ] **Tester l'animation** : ouvrir `/p/lppp-oppy-ai/` et `/p/lppp-oppy-ai/proposition/` — l'animation doit s'afficher (points + lignes animés, fond dégradé cyan/violet), rester fixe au scroll, sans erreur console.
- [ ] **Mobile-first** : breakpoints, touch, contrastes.

**Livrables** : Infographie et positionnement à jour, charte appliquée, responsive validé.

**Réf** : `docs/base-de-connaissances/contraste-textes-landing.md`, `docs/contacts/lppp-oppy-ai/charte-graphique-oppy-ai.md`.

---

### 5. Rédacteur — Contenus et JSON

**Sources** : `landing-proposition-lppp-oppy-ai.json`, `etude-oppy-ai-source.md`, `SEO Semantique.md`, `rapport seo complet.md`, `docs/bonnes-pratiques.md` (éditorial)

- [ ] **Enrichir** `landing-proposition-lppp-oppy-ai.json` : propositions de valeur, mission_flash, why_growth_engineer, pain_points, solution_piliers.
- [ ] **Section SEO** : intégrer diagnostics réels (fragmentation canonical, pertes chiffrées) si pertinent.
- [ ] **Bonnes pratiques** : ton direct, pas de formules IA, ancrage concret, humanisation.
- [ ] **Cohérence** avec l'étude stratégique et le rapport SEO.
- [ ] **Validation** : orthographe, grammaire, cohérence des messages.

**Livrables** : JSON à jour, textes validés, propositions de valeur intégrées.

---

## Dépendances et ordre

| Phase | Agents | Ordre |
|-------|--------|-------|
| 1 | Rédacteur | En premier : textes et structure JSON |
| 2 | Designer | Après Rédacteur : visuels dépendent des textes |
| 2 | Architecte | En parallèle : vérification structure |
| 2 | DevOps | En parallèle : préparation repo et déploiement |
| 3 | Orchestrateur | Continu : coordination, logs, registre |
| 4 | DevOps + Architecte | Fin : push, déploiement, vérification page |

---

## Critères de succès

- [ ] La landing `/p/lppp-oppy-ai/` et `/p/lppp-oppy-ai/proposition/` s'affichent correctement.
- [ ] L'animation **Waves Pins** est visible (position fixe, z-index OK).
- [ ] Le **contenu** est cohérent, sans placeholders inventés.
- [ ] **Repo dédié** créé et poussé (GitHub + GitLab).
- [ ] **Déploiement** configuré et **page vérifiée**.
- [ ] **Commit + push** effectués ; logs et registre à jour.

---

## Références sources

| Fichier | Contenu |
|---------|---------|
| `docs/contacts/lppp-oppy-ai/landing-proposition-lppp-oppy-ai.json` | Contenu dynamique landing |
| `docs/contacts/lppp-oppy-ai/charte-graphique-oppy-ai.md` | Charte Oppy.ai |
| `docs/contacts/lppp-oppy-ai/etude-oppy-ai-source.md` | Contexte business GAM |
| `apps/landing_pages/themes.py` | THEME_OPPY_AI |
| `procedure-fin-landing-repo-deploiement.md` | Checklist DevOps + Architecte |
| `registre-agents-ressources.md` | Agents et ressources |
| `docs/contacts/lppp-oppy-ai/waves-pins-source.md` | Source CodePen, paramètres, licence MIT |

---

## Vérification animation Waves Pins (ex-CodePen)

**Obligatoire** : l'animation (originellement CodePen Sabo Sugi) doit être **placée et testée** avant clôture.

| Étape | Action | Qui |
|-------|--------|-----|
| 1 | Lancer le serveur : `make run` ou `python manage.py runserver 8010` | Architecte / DevOps |
| 2 | Ouvrir http://localhost:8010/p/lppp-oppy-ai/ | Tous |
| 3 | Ouvrir http://localhost:8010/p/lppp-oppy-ai/proposition/ | Tous |
| 4 | Vérifier : animation visible (points + lignes animés, dégradé cyan/violet) | Designer |
| 5 | Vérifier : position fixe au scroll (fond ne bouge pas) | Designer |
| 6 | Ouvrir la console (F12) : aucune erreur JS, pas de 404 sur Three.js ni waves-pins-hero.js | Architecte |

**Prérequis test** : Docker (PostgreSQL) ou `make run` — si erreur DB, lancer `docker-compose up -d db` puis `make run`.

---

## Suivi

| Agent | Statut | Avancement | Bloqueurs |
|-------|--------|------------|-----------|
| Orchestrateur | 🟡 En cours | — | — |
| DevOps | ⚪ Pas démarré | 0% | — |
| Architecte | ⚪ Pas démarré | 0% | — |
| Designer | ⚪ Pas démarré | 0% | Attend livrables Rédacteur |
| Rédacteur | ⚪ Pas démarré | 0% | — |

**Légende** : ⚪ Pas démarré | 🟡 En cours | 🟢 Terminé | 🔴 Bloqué

---

*Document créé par l'Orchestrateur. Dernière mise à jour : 2026-01-30.*
