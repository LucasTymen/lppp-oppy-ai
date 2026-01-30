# Réparer et lancer le stack — conteneur, backend, front, admin

**Sprint** : voir `2025-01-30-sprint-equipe-technique.md` (toute l'équipe technique mobilisée).  
**Date** : 2025-01-30  
**Statut** : 🟢 **Mobilisation agents système et connexions**  
**Objectif** : Tous les agents en relation avec le **système et les connexions** sont mobilisés pour **réparer et lancer** le conteneur Docker, le backend Django, le front (templates, /essais/) et l’admin Django, afin que le projet soit accessible (localhost ou 127.0.0.1:8000).

---

## Mobilisation : agents système et connexions

| Agent | Rôle | Tâche prioritaire | Livrable / critère de fin |
|-------|------|-------------------|---------------------------|
| **DevOps** | Conteneur, ports, env, accès | Lancer le stack Docker (build, up) ; si accès localhost/admin en ERR_EMPTY_RESPONSE sous Windows, mettre en place l’**Option B** (runserver local) et documenter dans `pret-a-demarrer.md` | Conteneurs up ; admin et /essais/ accessibles (Docker ou runserver) |
| **Dev Django** | Backend, URLs, admin, front | Vérifier que le backend Django répond (vues, URLs, static) ; que l’admin et /essais/ sont configurés ; corriger les erreurs applicatives qui empêchent le chargement | Backend et front répondent ; admin et /essais/ fonctionnels |
| **Pentester** (sécurité connexions) | Flux et connexions | Une fois le stack lancé : vérifier isolation des flux (API enrich, Flowise, n8n), pas de fuite de données ; collaborer avec **Automatizer** pour la sécurité des workflows (voir `info-automatizer-pour-equipe.md`) ; appliquer `regles-securite.md` | Pas de régression sécurité sur les connexions |
| **Automatizer** (workflows N8N, Flowise) | Workflows et automatisation | Développer/maintenir workflows N8N/Flowise ; monitoring, optimisation tokens, traces de performances ; collaborer avec DevOps (conteneurs), Dev Django (API, Celery), Growth (pipelines), Pentester (sécurité flux). Voir `info-automatizer-pour-equipe.md`. | Workflows opérationnels, pas de régression |

**Parallélisation** : DevOps et Dev Django peuvent avancer en parallèle (DevOps sur conteneur/ports/env, Dev Django sur code et URLs). Pentester intervient une fois l’accès rétabli.

---

## Tâches détaillées

### DevOps (Responsable — R)

- [ ] Vérifier que `docker-compose.yml`, `docker/Dockerfile.web`, `docker/entrypoint.sh` sont en place.
- [ ] S’assurer qu’un `.env` existe (copie de `.env.example` si besoin) — ne jamais committer `.env`.
- [ ] **Build** : `make build` (ou `docker compose build`).
- [ ] **Lancer le stack** : `make up` (ou `docker compose up -d`).
- [ ] Vérifier les services : `make ps` — db, redis, web, celery, celery-beat (et optionnellement n8n, flowise).
- [ ] **Si localhost/admin ne répond pas (ERR_EMPTY_RESPONSE sous Windows)** : mettre en place l’**Option B** (dev local) — voir `pret-a-demarrer.md` § 5 Dépannage : `docker compose up -d db redis`, `.env` avec `DB_HOST=localhost`, `runserver` en local. Documenter la procédure si besoin.
- [ ] Indiquer à l’utilisateur : **`make createsuperuser`** (ou `python manage.py createsuperuser` en Option B) pour accéder à l’admin.
- [ ] En cas d’erreur : documenter (logs : `make logs`, `docker compose logs web`).

**Référence** : `docs/base-de-connaissances/infra-devops.md`, `docs/base-de-connaissances/pret-a-demarrer.md` (§ 2 Option A/B, § 5 Dépannage).

### Dev Django (Responsable — R)

- [ ] Vérifier que le **backend** Django démarre sans erreur (migrations, `gunicorn` ou `runserver`).
- [ ] Vérifier les **URLs** : `/admin/`, `/essais/`, `/`, `/p/<slug>/` (voir `lppp/urls.py`, apps).
- [ ] Vérifier que l’**admin** est enregistré (modèles campagnes, prospects, landing pages) et que les static files sont servis (`collectstatic` dans l’entrypoint).
- [ ] Vérifier le **front** : templates `/essais/` (landingsgenerator), landing pages ; corriger toute erreur de template ou de vue qui empêche le chargement.
- [ ] Corriger les erreurs applicatives (500, imports, settings) qui bloquent l’affichage de l’admin ou du front.

**Référence** : `lppp/urls.py`, `apps/landing_pages/`, `apps/landingsgenerator/`, `docker/entrypoint.sh`.

### Pentester (sécurité — une fois le stack up)

- [ ] Vérifier isolation des flux (API enrich, Flowise, n8n) ; pas de fuite de données ; appliquer `regles-securite.md`, `politique-credentials-securite-flux.md`.

---

## Commandes à exécuter (résumé)

À la **racine du projet** (référence : `docs/base-de-connaissances/strategie-operationnelle-make.md`, `make help`). **Environnement** : WSL/Linux recommandé — voir `environnement-wsl-linux.md`.

```bash
# 1. .env (si pas déjà fait) — Linux : cp ; Windows : copy
cp .env.example .env
# Éditer .env si besoin (SECRET_KEY, DB_PASSWORD, etc.)

# 2. Build des images
make build

# 3. Lancer le stack
make up

# 4. Créer un superutilisateur (interactif)
make createsuperuser

# 5. Vérifier l'état des services
make ps
make health
```

Puis ouvrir : **http://localhost:8000/admin/** et **http://localhost:8000/essais/** (ou **http://127.0.0.1:8000/...** si Option B runserver local).

**Si ERR_EMPTY_RESPONSE** : suivre `pret-a-demarrer.md` § 5 Dépannage (Option B — runserver local avec db + redis en Docker).

---

## Références

- **Infra** : `docs/base-de-connaissances/infra-devops.md`
- **Prêt à démarrer** : `docs/base-de-connaissances/pret-a-demarrer.md` (§ 2 Option A/B, § 5 Dépannage)
- **Sécurité** : `docs/base-de-connaissances/regles-securite.md`, `politique-credentials-securite-flux.md`
- **README** : `README.md`

---

*Segmentation mise à jour pour mobilisation des agents système et connexions (DevOps, Dev Django, Pentester). Dernière mise à jour : 2025-01-30.*
