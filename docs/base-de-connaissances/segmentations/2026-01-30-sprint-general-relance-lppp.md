# Sprint général — Relance LPPP (équipe + coordinateurs)

**Date** : 2026-01-30  
**Statut** : 🟡 En cours  
**Priorité** : URGENT  
**Objectif** : Relancer LPPP de bout en bout : séparation SquidResearch/LPPP opérationnelle, conteneurs rebuildés, migrations appliquées, Django accessible ; commit + push une fois l’état satisfaisant.

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both` ou `make commit-push MSG="..."`).

---

## 1. Contexte et objectifs

- **Problème** : Pas d’accès à Django ; incertitude sur la séparation réelle LPPP/SquidResearch (instance Django propre, conteneurs dédiés).
- **Référence** : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md` — stack LPPP autonome (lppp_web, lppp_db, lppp_redis, lppp_n8n, lppp_flowise) ; ports dédiés 8010 (Django), 5433 (PostgreSQL), 6380 (Redis), 5681 (n8n), 3010 (Flowise).
- **Objectifs du sprint** :
  1. Vérifier / finaliser la séparation LPPP/SquidResearch (docker-compose, .env, pas de dépendance à SquidResearch).
  2. Rendre les conteneurs LPPP opérationnels (build, up, migrate).
  3. Appliquer toutes les migrations Django.
  4. Atteindre un état fonctionnel : accès à Django (http://localhost:8010/), admin/essais OK.
  5. Commit + push après validation.

---

## 2. Ports et URLs LPPP (référence)

| Service   | Port hôte | URL / remarque                    |
|----------|-----------|-----------------------------------|
| Django   | 8010      | http://localhost:8010/           |
| PostgreSQL | 5433    | localhost:5433                    |
| Redis    | 6380      | localhost:6380                    |
| n8n      | 5681      | http://localhost:5681             |
| Flowise  | 3010      | http://localhost:3010             |

**Important** : Ne pas utiliser les ports SquidResearch (8000, 5432, 6379, 5679, 3000/3001) dans la config ou la doc LPPP.

---

## 3. Tâches par rôle

### Orchestrateur
- [ ] S’assurer que ce sprint et le log commun sont le fil conducteur de la relance.
- [ ] Après succès : mettre à jour log-projet.md, log-ia.md, ce document (statut 🟢).

### Chef de Projet
- [ ] Valider les critères de succès (Django 8010 OK, health-check OK, migrations appliquées).
- [ ] Mettre à jour TODO.md, boite-a-idees.md si besoin ; valider le commit/push.

### Architecte / DevOps (Responsables — build, réseau, déploiement)
- [ ] Vérifier que `docker-compose.yml` utilise bien les ports LPPP (8010, 5433, 6380, 5681, 3010) et les noms de conteneurs `lppp_*`.
- [ ] Séquences à exécuter (WSL ou environnement où `make` est disponible) — **en préservant les données** :
  - `make relance-safe` (recommandé) — ou à la main : `make ensure-env`, `make clean-containers`, `make build`, `make start`.
  - Ne pas utiliser `make go` si vous voulez garder landing pages, workflow Flowise, agent chatbot, études (voir § 4).
- [ ] En cas d’échec : documenter dans `erreurs-et-solutions.md` ; tenter `make build` puis `make start` et `make migrate` à la main.
- [ ] Vérifier `make health-check` et `make services-urls` ; confirmer accès http://localhost:8010/.

### Dev Django
- [ ] Vérifier que `lppp/settings.py` et `.env` pointent vers la stack LPPP (DB_HOST=db, REDIS_URL=redis://redis:6379/0, etc.) et pas vers SquidResearch.
- [ ] Après démarrage : vérifier admin Django, essais, landings si besoin ; créer superutilisateur si nécessaire (`make createsuperuser`).

### Pentester (si disponible)
- [ ] Vérifier ALLOWED_HOSTS et absence de régression sécurité après relance.

### Automatizer (n8n / Flowise)
- [ ] Après relance : vérifier que N8N_WEBHOOK_URL, FLOWISE_URL dans .env correspondent aux ports 5681 et 3010.

---

## 4. Préservation des données (important)

- **`make go`** exécute `docker compose down -v` : les **volumes sont supprimés** (postgres_data, redis_data, static_volume, media_volume, n8n_data, flowise_data, etc.) → **perte des données** (base, Redis, Flowise, n8n, fichiers).
- **Pour ne pas perdre vos données** : ne pas utiliser `make go`. Utiliser à la place :
  - **`make relance-safe`** (recommandé) : ensure-env + clean-containers + build + up séquentiel + migrate + collectstatic + health-check. Les volumes ne sont jamais supprimés.
  - Ou à la main : `make ensure-env && make clean-containers && make build && make start`.

### Où sont stockées vos données (toutes préservées avec `relance-safe`)

| Ce que vous avez | Où c’est stocké | Préservé avec relance-safe |
|------------------|-----------------|----------------------------|
| **Landing pages** (contenus, campagnes) | Base Django → volume **postgres_data** | Oui |
| **Templates / thèmes** des landings | Dépôt (apps/landing_pages, templates/) | Oui (fichiers versionnés) |
| **Études en cours** | Dépôt **docs/** ou base Django | Oui (repo + postgres_data) |
| **Workflow Flowise** (chatflows, pipelines) | Volume **flowise_data** + sauvegardes dans **docs/flowise-workflows/** | Oui (volume + backups versionnés) |
| **Agent chatbot** (conciergerie, etc.) | Volume **flowise_data** (config Flowise) + **docs/flowise-workflows/** (backups, sources) | Oui |
| **Fichiers déposés pour Flowise** (FAISS, sources) | **data/flowise/** (monté dans le conteneur) + volume flowise_data | Oui (dossier repo + volume) |
| **Workflows n8n** | Volume **n8n_data** | Oui |

Avec **`make relance-safe`** : aucun de ces volumes n’est supprimé ; le dépôt (docs/, data/, templates/) n’est pas modifié par Docker. Vos landing pages, études, workflow Flowise et agent chatbot restent intacts.

## 5. Séquence opérationnelle recommandée

1. **Environnement** : WSL (ou Git Bash) depuis la racine du dépôt LPPP.
2. **Prérequis** : Docker et Docker Compose installés.
3. **Commandes (données préservées)** :
   ```bash
   make relance-safe
   ```
   Ou en détail :
   ```bash
   make ensure-env
   make clean-containers
   make build
   make start
   ```
4. **Vérifications** :
   - Ouvrir http://localhost:8010/ (page d’accueil ou admin).
   - `make health-check` : tous les services en vert.
   - Si pas de superutilisateur : `make createsuperuser`.

---

## 5. Critères de succès

- [ ] Fichier `.env` présent (créé depuis .env.example si besoin).
- [ ] Conteneurs `lppp_*` démarrés sans conflit avec SquidResearch.
- [ ] Migrations Django appliquées sans erreur.
- [ ] Django accessible sur http://localhost:8010/.
- [ ] `make health-check` OK.
- [ ] État jugé satisfaisant par le Chef de Projet → **commit + push** (`make push-both` ou `make commit-push MSG="chore: relance LPPP stack, migrations, health-check OK"`).

---

## 7. Références

- **Log commun LPPP/SquidResearch** : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md`
- **Log canonique (SquidResearch)** : `docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md` (dépôt SquidResearch)
- **Makefile / stratégie** : `docs/base-de-connaissances/strategie-operationnelle-make.md`
- **Sprint routage conteneurs** : `docs/base-de-connaissances/segmentations/2026-02-05-sprint-urgent-routage-conteneurs.md`

---

*Document créé pour le sprint général de relance LPPP. Dernière mise à jour : 2026-01-30.*
