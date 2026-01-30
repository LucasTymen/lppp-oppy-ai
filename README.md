# Landings Pages Pour Prospections (LPPP)

Programme de **prospection et démarchage** via des **landing pages personnalisées**, avec **scraping** pour la recherche et l’ajustement des données. Architecture reprise de **SquidResearch** (conteneurs, monorepo `apps/`, Django, Celery, n8n, Flowise, Enriched, Kali Linux).

**Environnement préféré** : WSL ou Linux — voir `docs/base-de-connaissances/environnement-wsl-linux.md`.

## Stack (conteneurs)

| Service      | Rôle                          | Port |
|-------------|--------------------------------|------|
| **db**      | PostgreSQL 16                 | 5432 (exposé pour dev local) |
| **redis**   | Broker Celery + cache         | 6379 (exposé pour dev local) |
| **web**     | Django (Gunicorn)             | 8000 |
| **celery**  | Worker Celery                 | —    |
| **celery-beat** | Planificateur Celery      | —    |
| **n8n**     | Automatisation workflows      | 5678 |
| **flowise** | LLM / chatbots                | 3000 |
| **enriched**| Scraping / enrichment (queue) | —    |
| **kalilinux** | **Conteneur quali** : outils OSINT / sécurité (central à la stratégie d'enrichissement) | — |

- **Enriched** et **Kali (conteneur quali)** : démarrés avec le profil `full` (stratégie d'enrichissement, anti-blocage Google/LinkedIn) :  
  `docker compose --profile full up -d`  
  Voir `docs/base-de-connaissances/strategie-enrichissement.md`.

## Démarrage rapide

**Guide détaillé** (venv, Docker, dev local avec PostgreSQL, tester l’admin) : **`docs/base-de-connaissances/pret-a-demarrer.md`**

### Option Docker (recommandé)

```bash
cp .env.example .env
# Ajuster SECRET_KEY, DB_PASSWORD, etc.

make build
make up
make createsuperuser   # pour accéder à l’admin
```

- **Django** : http://localhost:8000  
- **Admin** : http://localhost:8000/admin/  
- **Interface essais** : http://localhost:8000/essais/  
- **n8n** : http://localhost:5678  
- **Flowise** : http://localhost:3000  

### Option dev local (PostgreSQL + Redis dans Docker, Django en local)

```bash
docker compose up -d db redis
cp .env.example .env
# Dans .env : DB_HOST=localhost, REDIS_URL=redis://127.0.0.1:6379/0, CELERY_BROKER_URL=redis://127.0.0.1:6379/1, CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/2
make venv
# Activer le venv puis :
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py createsuperuser
make runserver
```

- **Admin** : http://127.0.0.1:8000/admin/  
- **Interface essais** : http://127.0.0.1:8000/essais/  

On reste sur **PostgreSQL** partout (pas de SQLite en dev).  

## Structure (stratégie SquidResearch)

- **`apps/`** : applications Django métier  
  - `landing_pages` : création et affichage des landing pages personnalisées  
  - `campaigns` : campagnes et prospects (noeuds ENRICHED dans `nodes/`)  
  - `scraping` : module ENRICHED (enrichment, réseau, tâches Celery)  
- **`lppp/`** : projet Django (settings, urls, wsgi, asgi, celery)  
- **`templates/`** : templates des landing pages  
- **`docker/`** : Dockerfile web, enriched, entrypoint  
- **`docker-compose.yml`** : tous les services  

Le **PYTHONPATH** inclut `apps/` (manage.py, wsgi, asgi, celery) pour les imports métier.

## Landing pages

- **Création** : via l’admin Django ou une API à venir (champs : titre, slug, prospect, template, `content_json`).  
- **Affichage public** : `/p/<slug>/` (uniquement si `is_published=True`).  
- **Scraping / données** : module **Enriched** et noeuds dans `apps.campaigns.nodes` pour alimenter et ajuster les données (entreprises, contacts) utilisées pour personnaliser les pages.

## Tests (hors Docker)

```bash
PYTEST_USE_SQLITE=1 PYTHONPATH=".:apps" python -m pytest apps/ -v
```

## Référence

- **SquidResearch** : monorepo `apps/`, PostgreSQL, Celery, n8n, Flowise, ENRICHED, Makefile, docker-compose.
