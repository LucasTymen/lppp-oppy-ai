# Sprint LPPP-OppyAI — SEO technique, SEO sémantique & propositions de valeur

**Date** : 2026-03-30  
**Pilote** : Orchestrateur  
**Statut** : 🟡 En cours

**Règle Git** : En clôture, **commit + push** sur origin et gitlab (`make push-both` ou `make commit-push MSG="..."`). Réf. `git-remotes-github-gitlab.md`.

---

## Contexte

Le dossier **`docs/contacts/lppp-oppy-ai/`** est **complet** avec :

- **`SEO Semantique.md`** — audit sémantique oppy.ai (cohérence marque Oppycx/Opportunity/OPPYAI, H1, métadonnées, entité de marque, E-E-A-T, clusters, recommandations).
- **`SEO Technique.md`** — écosystème officiel (oppy.ai, oppycx.com, allmysms.com), URLs stratégiques, API, RCS, références business (Omnes, Ecovadis).
- **`rapport seo complet.md`** — audit consolidé (technique + sémantique), données mesurées (TTFB, cache, fragmentation canonical/og:url), pertes chiffrées, plan d’action P0/P1/P2.
- **`seo-technique-semantique-oppy-ai.md`** — trame existante (grilles, piliers, prochaines étapes).
- **Propositions de valeur** — contenu ajouté par l’utilisateur (à intégrer dans la landing).

**Objectif** : intégrer ces éléments dans la **landing LPPP-OppyAI** (JSON, infographie, positionnement, sections) pour livrer une proposition crédible et chiffrée.

---

## Équipes mobilisées

| Rôle | Responsabilité |
|------|----------------|
| **Orchestrateur** | Pilote le sprint, répartit les tâches, met à jour le registre, rend des comptes. |
| **Rédacteur** | Textes, meta, propositions de valeur ; mise à jour JSON ; alignement bonnes pratiques (`docs/bonnes-pratiques.md`). |
| **Designer** | Infographie, positionnement-marketing, hiérarchie visuelle, responsive, accessibilité. |
| **Expert SEO** | Consultation C sur les choix sémantiques et techniques ; validation des recommandations. |
| **Chef de Projet** | Validation finale, mise à jour logs et docs. |

---

## Segmentation des tâches

### 1. Rédacteur — SEO technique & sémantique

**Sources** : `SEO Semantique.md`, `SEO Technique.md`, `rapport seo complet.md`, `seo-technique-semantique-oppy-ai.md`

- [ ] **Enrichir** `landing-proposition-lppp-oppy-ai.json` :
  - `seo_technique_semantique` : injecter les **diagnostics réels** (fragmentation canonical, dilution marque, P0/P1/P2 du rapport) ; mettre à jour `technique_sections` et `semantique_sections` avec les constats des rapports.
  - `seo_resume` ou section dédiée : intégrer les **chiffres du rapport** (perte 20–40 %, gap 1,5 M€, TTFB 0,43 s, poids 297 Ko, plan d’action).
  - `key_figures_carousel` : ajouter les métriques mesurées (TTFB, poids page, perte estimée) si pertinent.
- [ ] **Mettre à jour** `seo-technique-semantique-oppy-ai.md` : cocher les cases remplies, référencer les rapports consolidés, ajouter les URLs stratégiques (oppy.ai, oppycx, allmysms, API, RCS) depuis `SEO Technique.md`.
- [ ] Appliquer les **bonnes pratiques éditoriales** (`docs/bonnes-pratiques.md` § 1–2) : ton direct, pas de formules IA, ancrage concret.

**Livrables** : JSON à jour, markdown SEO complété, textes validés.

---

### 2. Rédacteur — Propositions de valeur

**Source** : contenu ajouté par l’utilisateur dans le dossier.

- [ ] Extraire et structurer les **propositions de valeur** (benefits, différenciation, USPs).
- [ ] Les intégrer dans `landing-proposition-lppp-oppy-ai.json` :
  - `mission_flash`, `why_growth_engineer`, `solution_piliers`, `pain_points`, ou blocs dédiés si besoin.
- [ ] S’assurer de la **cohérence** avec l’étude stratégique (`etude-oppy-ai-source.md`) et le rapport SEO.

**Livrables** : Propositions de valeur intégrées dans le JSON.

---

### 3. Designer — Infographie & positionnement

**Sources** : `rapport seo complet.md`, `SEO Semantique.md`, `SEO Technique.md`, `infographie-lppp-oppy-ai-7-formats.html`, `positionnement-marketing.html`

- [ ] **Infographie** (`infographie-lppp-oppy-ai-7-formats.html`) :
  - Ajouter une section ou bloc **SEO** : fragmentation canonique, perte estimée, plan P0/P1/P2 (schéma visuel).
  - Intégrer les **URLs stratégiques** (vitrine, technique, API) dans un encart si pertinent.
  - Conserver la palette navy/vert et le ton LPPP.
- [ ] **Positionnement marketing** (`positionnement-marketing.html`) :
  - Enrichir avec les **propositions de valeur** validées par le Rédacteur.
  - Ajouter un encart **écosystème** (oppy.ai, oppycx, allmysms) si utile au discours.
- [ ] **Responsive & accessibilité** : vérifier mobile-first, contrastes, structure sémantique (`docs/bonnes-pratiques.md` § 5).

**Livrables** : `infographie-lppp-oppy-ai-7-formats.html` et `positionnement-marketing.html` mis à jour.

---

### 4. Orchestrateur — Coordination

- [ ] S’assurer que **Rédacteur** et **Designer** ont accès aux mêmes sources.
- [ ] Vérifier que les **dépendances** sont respectées : Rédacteur termine les textes / structure avant que Designer finalise les visuels dépendants.
- [ ] Mettre à jour **`registre-agents-ressources.md`** si de nouvelles ressources sont créées.
- [ ] Mettre à jour **`log-projet.md`** à la clôture du sprint.
- [ ] Rappeler **commit + push** en fin de sprint.

---

### 5. Chef de Projet — Validation

- [ ] Valider la cohérence **stratégie ↔ SEO ↔ propositions de valeur**.
- [ ] Vérifier qu’**aucun chiffre n’est inventé** (anti-hallucination) ; tout provient des rapports fournis.
- [ ] Valider la **checklist pré-prod** si déploiement prévu (`checklist-pre-prod-integrite.md`).
- [ ] Mettre à jour **`decisions.md`** et **`sources.md`** si décisions prises.

---

## Références sources

| Fichier | Contenu |
|---------|---------|
| `docs/contacts/lppp-oppy-ai/SEO Semantique.md` | Audit sémantique homepage, métadonnées, entité marque, E-E-A-T, clusters, recommandations P0. |
| `docs/contacts/lppp-oppy-ai/SEO Technique.md` | Écosystème URLs, API, RCS, références Omnes/Ecovadis, vigilance noms similaires. |
| `docs/contacts/lppp-oppy-ai/rapport seo complet.md` | Audit consolidé, TTFB, cache, fragmentation, pertes chiffrées, plan P0/P1/P2. |
| `docs/contacts/lppp-oppy-ai/seo-technique-semantique-oppy-ai.md` | Trame technique + sémantique (à compléter). |
| `docs/contacts/lppp-oppy-ai/etude-oppy-ai-source.md` | Contexte business GAM (à croiser avec SEO). |

---

## Critères de succès

- [ ] La landing `/p/lppp-oppy-ai/` affiche les **données SEO réelles** (pas de placeholders inventés).
- [ ] Les **propositions de valeur** sont visibles et cohérentes avec l’étude et le rapport.
- [ ] L’**infographie** et le **positionnement** reflètent le rapport consolidé.
- [ ] **Commit + push** effectués ; logs et registre à jour.

---

## Suivi

| Agent | Statut | Avancement | Bloqueurs |
|-------|--------|------------|-----------|
| Orchestrateur | 🟡 En cours | — | — |
| Rédacteur | ⚪ Pas démarré | 0% | — |
| Designer | ⚪ Pas démarré | 0% | Attend structuration Rédacteur |
| Chef de Projet | ⚪ Pas démarré | 0% | Attend livrables |

---

*Document créé par l’Orchestrateur. Dernière mise à jour : 2026-03-30.*
