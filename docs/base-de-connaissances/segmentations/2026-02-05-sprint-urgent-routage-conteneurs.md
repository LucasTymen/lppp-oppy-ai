# Sprint URGENT — Revoir les routages des conteneurs (toute l'équipe)

**Date** : 2026-02-05  
**Statut** : 🔴 URGENT — En cours  
**Objectif** : **Revoir absolument les routages de nos conteneurs** en s'appuyant sur le **log commun** et la **recommandation de l'équipe SquidResearch**. Mobilisation **globale** de toute l'équipe ; étude d'impact et de risques réalisée en amont.

**Contrainte prioritaire** : **SquidResearch a la priorité.** Aucune modification de la stack SquidResearch. LPPP s'adapte (ports, noms, .env). Réf. `decisions.md`, `infra-devops.md` § 1, `log-commun-lppp-squidresearch.md`.

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both` ou `make commit-push MSG="..."`).

---

## 1. Document de référence (recommandation SquidResearch)

La **recommandation de l'équipe SquidResearch** et l'état détaillé des ports/routages sont dans le **log commun**, maintenu dans le dépôt SquidResearch :

| Contexte | Chemin du document canonique |
|----------|------------------------------|
| **Linux / WSL** | `/home/lucas/tools/squidResearch/docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md` |
| **Windows (accès WSL)** | `\\wsl.localhost\Ubuntu-22.04\home\lucas\tools\squidResearch\docs\infrastructure\LOG_COMMUN_LPPP_SQUIDRESEARCH.md` |
| **Depuis la racine SquidResearch** | `docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md` |

**Pointeur dans LPPP** : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md`.

**Contenu attendu du log commun** (résumé) : § 1 Adresses et conflits de ports (LPPP : 8000, 5678, 3000, 5432, 6379 ; SquidResearch : 8000, 3000, 5679, 3001, 5432, 5555, etc.) ; § 2 Variables d'env ; § 3 Chemins ; § 4 Fichiers à tenir à jour ; **§ 5 Avis et recommandations (coexistence, hermeticité)** ; § 6 Résumé ; § 7 État des projets Docker.

**Action obligatoire** : L'**Architecte réseau** et le **DevOps** doivent **lire le document canonique** (chemin ci-dessus) pour extraire la **recommandation précise** sur les routages et l'appliquer côté LPPP.

---

## 2. Étude d'impact et de risques

Une **étude d'impact et de risques** a été rédigée : `docs/base-de-connaissances/etude-impact-risques-routage-conteneurs-lppp.md`. Elle synthétise :

- État actuel des routages LPPP (ports, conteneurs, .env).
- Impact pour LPPP d'un changement de routage (docker-compose, Makefile, .env, doc, Option B).
- Matrice de risques (conflits, régression, doc obsolète, sécurité).
- **Points d'attention** (conflits 8000/3000/5432/5678, Flowise/n8n, ALLOWED_HOSTS, etc.).

Toute l'équipe est invitée à la lire avant ou pendant le sprint.

---

## 3. Tâches par rôle (mobilisation globale)

### Orchestrateur
- [ ] S'assurer que le registre et les guides pointent vers le log commun et ce sprint.
- [ ] Après application de la recommandation : mettre à jour le log projet et ce sprint ; aligner la doc (infra-devops, erreurs-et-solutions, strategie-operationnelle-make).

### Architecte (réseau / structure)
- [ ] **Lire le log commun** (document canonique SquidResearch, chemin § 1) et en extraire la **recommandation routage / coexistence**.
- [ ] Synthétiser pour LPPP : quels ports, quels noms de conteneurs, quelles règles de coexistence (LPPP seul vs LPPP + SquidResearch).
- [ ] Proposer le plan de changement (ports exposés, override docker-compose si besoin, documentation).
- [ ] Vérifier la cohérence routes Django / URLs documentées après changement (routes-back-lppp.md).

### DevOps (Responsable — R de l'application)
- [ ] **Lire le log commun** et la recommandation SquidResearch.
- [ ] Appliquer les changements de routage côté LPPP uniquement : `docker-compose.yml` (mapping de ports), éventuel fichier d'override (ex. `docker-compose.override.yml` pour port Django 8001 si recommandé), `.env.example` et doc.
- [ ] Mettre à jour le **Makefile** et **strategie-operationnelle-make.md** si les ports ou commandes changent (ex. services-urls, health-check).
- [ ] Tester : `make clean-containers` puis `make start` (ou procédure validée) ; vérifier accès Django, n8n, Flowise sur les nouveaux ports.
- [ ] Documenter dans **erreurs-et-solutions.md** toute entrée « Routage conteneurs » (nouveaux ports, procédure, pièges).
- [ ] **Ne jamais** modifier ni supprimer les conteneurs ou la config SquidResearch.

### Dev Django
- [ ] Adapter si besoin **ALLOWED_HOSTS** (lppp/settings.py ou .env) si nouveau(s) port(s) ou host(s) (en coordination avec Pentester).
- [ ] Vérifier que les URLs d'API et les appels internes (ex. flowise_client.py, FLOWISE_URL) restent cohérents avec le nouveau routage (ex. localhost vs nom de service Docker).
- [ ] Tester l'application après changement (admin, essais, landing chatbot).

### Pentester (sécurité)
- [ ] Vérifier que les changements de routage n'ouvrent pas de surface d'attaque (ALLOWED_HOSTS explicite, pas de wildcard).
- [ ] Valider la conformité avec `regles-securite.md` et `politique-credentials-securite-flux.md`.

### Automatizer (n8n, Flowise)
- [ ] Vérifier que **N8N_WEBHOOK_URL**, **FLOWISE_URL** et les URLs d'embed restent valides après changement de ports (doc et .env.example).
- [ ] S'assurer que les workflows n8n et Flowise (concierge, etc.) fonctionnent avec la nouvelle configuration.

### Chef de Projet
- [ ] Valider le plan (recommandation SquidResearch + étude d'impact) avant application.
- [ ] Valider que les critères de succès sont atteints après application.
- [ ] Mettre à jour **log-projet.md**, **decisions.md** (décision « Routage conteneurs LPPP ») et ce sprint (statut 🟢).
- [ ] S'assurer que **erreurs-et-solutions.md** et **infra-devops.md** sont à jour.

---

## 3.1 Builds et migrations — Responsables : Architecte + DevOps

**Directive** : Les **builds** (Docker) et les **migrations** (Django) pour appliquer la nouvelle stack (ports dédiés, routage) sont **sous la responsabilité de l'Architecte (réseau) et du DevOps**. Ils s'en chargent ; les autres agents apportent leur aide **quand ils en ont besoin** (infos, validation, correctifs).

**Périmètre** :
- **Builds** : `make build` ou `make build-no-cache` si besoin ; `make full-setup` ou `make go` pour un démarrage à froid complet.
- **Migrations** : `make makemigrations` (si modèles modifiés), `make migrate` ou `make migrate-wait` ; vérification avec `make showmigrations`.
- **Séquence type** : `make clean-containers` → `make start` (qui inclut migrate) ; ou `make go` pour tout recréer (ensure-env, build, up, migrate).
- **Vérifications** : stack accessible (Django 8010, Flowise 3010, n8n 5681), admin Django, health-check.

**Soutien des autres agents (sur demande)** :
- **Dev Django** : modèles, ALLOWED_HOSTS, cohérence URLs/code si les migrations ou le routage l'exigent.
- **Automatizer** : URLs Flowise/n8n, webhooks, embed après changement de ports.
- **Pentester** : validation sécurité (ALLOWED_HOSTS, pas de régression) avant ou après déploiement.
- **Chef de Projet** : validation des critères de succès et mise à jour des logs/décisions en fin de séquence.

Références : `Makefile` (build, migrate, start, go), `strategie-operationnelle-make.md`, `infra-devops.md`, `pret-a-demarrer.md`.

---

## 4. Ordre d'exécution recommandé

1. **Architecte** : lecture du log commun (SquidResearch) → synthèse recommandation + plan LPPP.
2. **Chef de Projet** : validation du plan + étude d'impact.
3. **DevOps** : application des changements (docker-compose, override, .env.example, Makefile, doc).
4. **Dev Django** : ALLOWED_HOSTS et cohérence code ; **Pentester** : validation sécurité ; **Automatizer** : validation URLs n8n/Flowise.
5. **DevOps** : tests de bout en bout (`make start`, accès Django/n8n/Flowise).
6. **Chef de Projet** : validation finale, mise à jour logs et décisions.

---

## 5. Critères de succès

- [x] Recommandation SquidResearch lue et intégrée (log commun § 5.3, § 5.4, AVIS_SOLUTIONS).
- [x] Routages LPPP revus et appliqués : ports dédiés 8010 (Django), 5433 (DB), 6380 (Redis), 3010 (Flowise), 5681 (n8n) — **sans modification de la stack SquidResearch**.
- [ ] Stack LPPP démarrable et accessible (Django http://localhost:8010, admin, essais, n8n, Flowise) — à valider après `make start`.
- [x] Doc à jour : infra-devops.md § 3.4, log-commun (pointeur § 5.3, § 5.4, AVIS_SOLUTIONS), erreurs-et-solutions, pret-a-demarrer, flowise-concierge, flowise_client.py, Makefile, .env.example.
- [x] Étude d'impact et de risques documentée ; doc référence `avis-et-solutions-routage-lppp-reference.md` créée.

---

## 6. Références

- **Log commun (pointeur)** : `log-commun-lppp-squidresearch.md`
- **Étude impact/risques** : `etude-impact-risques-routage-conteneurs-lppp.md`
- **Infra** : `infra-devops.md` (§ 1, § 3.4), `strategie-operationnelle-make.md`
- **Sprint réseau existant** : `2026-01-30-sprint-resolution-reseau-django.md`
- **Erreurs** : `erreurs-et-solutions.md` (conflits conteneurs, localhost:8000, Flowise 3000)
- **Priorité SquidResearch** : `decisions.md`, `infra-devops.md` § 1
