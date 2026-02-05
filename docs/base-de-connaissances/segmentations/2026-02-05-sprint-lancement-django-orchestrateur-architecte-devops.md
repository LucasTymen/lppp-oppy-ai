# Sprint — Lancement Django (Orchestrateur, Architecte, DevOps)

**Date** : 2026-02-05  
**Statut** : 🟢 Terminé (2026-02-05 — stack lancé avec succès)  
**Objectif** : Lancer **proprement** le projet LPPP pour que **Django fonctionne correctement** (stack accessible, admin, essais, landings). Coordination **Orchestrateur** (alignement registre / procédures), **Architecte** (chaîne routes / vues / cohérence), **DevOps** (conteneurs, .env, santé des services).

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both` ou `make commit-push MSG="..."`). Réf. `git-remotes-github-gitlab.md`.

**Log commun** : Consulter `docs/base-de-connaissances/log-commun-lppp-squidresearch.md` avant toute action sur Docker/ports/.env. **SquidResearch a la priorité** ; ne modifier que les conteneurs **lppp_***.

---

## Contexte

- **Django n'est pas lancé** : le projet doit être démarré de façon reproductible et validée.
- **Environnement** : WSL (bash) par défaut — voir `pilotage-agents.mdc`, `environnement-wsl-linux.md`. Chemin projet WSL : `/home/lucas/tools/homelucastoolsLandingsPagesPourProspections`.

---

## Tâches par agent

### Orchestrateur
- [ ] Vérifier que le **registre** (`registre-agents-ressources.md`) et les **guides** (GUIDE-CHEF-PROJET, GUIDE-AGENTS) pointent vers les procédures de lancement (`strategie-operationnelle-make.md`, `pret-a-demarrer.md`).
- [ ] S'assurer que la segmentation **lancement Docker** (`2025-01-30-lancement-docker-projet.md`) et ce sprint sont cohérents (commandes, rôles).
- [ ] Après lancement réussi : mettre à jour le **log projet** et ce sprint (statut 🟢) en coordination avec le Chef de Projet.

### Architecte (structure, routes, cohérence)
- [ ] Vérifier la **chaîne d'intégration** : `lppp/urls.py` → apps (landing_pages, landingsgenerator, scraping, campaigns) ; pas de route orpheline ni de conflit.
- [ ] Confirmer que les **URLs critiques** sont documentées : `/admin/`, `/essais/`, `/`, `/p/<slug>/`, `/maisons-alfort/` — réf. `routes-back-lppp.md`.
- [ ] S'assurer que les **migrations** sont appliquées (landing_pages, campaigns, etc.) ; en cas de conflit ou d'état incohérent, documenter dans `erreurs-et-solutions.md` et coordonner avec Dev Django (procedure-avant-migrations-relance.md).

### DevOps (Responsable — R du lancement)
- [x] **Consulter le log commun** (`log-commun-lppp-squidresearch.md`) : pas de conflit de ports avec SquidResearch ; n'utiliser que les conteneurs **lppp_***.
- [x] **.env** : `make ensure-env` (copie depuis `.env.example` si absent). Ne jamais committer `.env`.
- [x] **Lancer le stack** : `make start` (exécuté depuis WSL : `/mnt/c/home/lucas/tools/homelucastoolsLandingsPagesPourProspections`) (démarrage séquentiel db → redis → web → celery → n8n → flowise, puis migrate, health-check, services-urls). Alternative : `make up` puis `make migrate` et `make health-check`.
- [ ] **En cas de conflit de conteneurs** (« container name already in use ») : `make clean-containers` (supprime uniquement les lppp_*) puis `make start`.
- [x] **Vérifier la santé** : `make health-check` — tous les services ✅ — tous les services (db, redis, web, celery, celery-beat, n8n, flowise) en état Up.
- [x] **Vérifier l'accès** : Django répond sur http://127.0.0.1:8000/ (services-urls affichés) (ou localhost:8000) ; `make services-urls` pour lister les URLs.
- [ ] **Option B (runserver sur l'hôte)** : si Docker web inaccessible (ex. ERR_EMPTY_RESPONSE sous Windows) : `docker compose up -d db redis` (et optionnellement flowise pour le chatbot), `.env` avec `DB_HOST=localhost`, `make venv-install` puis `make runserver` (port 8080 ou 8082). Documenter dans `pret-a-demarrer.md` § 5 si appliqué.
- [ ] Documenter toute **erreur rencontrée** et sa solution dans `erreurs-et-solutions.md`.

### Chef de Projet (validation)
- [ ] Valider que **Django est lancé** et que l'application est accessible (au moins une URL : /, /admin/, /essais/).
- [ ] Mettre à jour ce sprint (statut 🟢 Terminé) et `docs/logs/log-projet.md` une fois la validation OK.

---

## Commandes à exécuter (DevOps — WSL)

À la **racine du projet** (WSL : `/home/lucas/tools/homelucastoolsLandingsPagesPourProspections`).

```bash
# 1. S'assurer que .env existe
make ensure-env

# 2. Lancer tout le stack (séquentiel + migrate + health-check + URLs)
make start

# Si erreur "container name already in use" :
# make clean-containers
# make start

# 3. Vérifier les services
make health-check
make services-urls

# 4. (Première fois) Créer un superutilisateur pour l'admin
make createsuperuser
```

**URLs attendues** (après `make services-urls`) : Django (8000), admin (8000/admin/), essais (8000/essais/), n8n (5678), Flowise (3000).

---

## Critères de succès

- [x] **Stack lancé** : `make health-check` affiche ✅ pour db, redis, web, celery, celery-beat, n8n, flowise.
- [x] **Django répond** : http://127.0.0.1:8000/ (ou localhost:8000) retourne une page (200).
- [x] **Admin accessible** : http://127.0.0.1:8000/admin/ (connexion possible après createsuperuser).
- [x] **Essais accessible** : http://127.0.0.1:8000/essais/ charge sans erreur 500.
- [ ] Aucune régression documentée sans entrée dans `erreurs-et-solutions.md`.

---

## Références

- **Stratégie Make** : `strategie-operationnelle-make.md` (catalogue commandes, pilotes)
- **Prêt à démarrer** : `pret-a-demarrer.md` (Option A Docker, Option B runserver)
- **Infra** : `infra-devops.md` (§ 1.1 Comment faire tourner LPPP, § 3.4 Ports)
- **Log commun** : `log-commun-lppp-squidresearch.md`
- **Sprint lancement historique** : `2025-01-30-lancement-docker-projet.md`
- **Routes back** : `routes-back-lppp.md`
- **Registre** : `registre-agents-ressources.md`
