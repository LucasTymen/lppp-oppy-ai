# Stratégie opérationnelle Make — LPPP

**Objectif** : Unifier tout l'opérationnel du projet (maintien, mise à jour, lancement, migrations, contrôle des modules) autour de `make`, avec une répartition claire des responsabilités entre l'équipe technique et les pilotes.

**Pilotes** : Chef de Projet, DevOps, Dev Django, Orchestrateur  
**Référence** : `Makefile` (racine), `docs/base-de-connaissances/infra-devops.md`, `docs/base-de-connaissances/pret-a-demarrer.md`  
**Inspiration** : SquidResearch Makefile (go, relance, démarrage séquentiel, backup, couleurs, .env)

---

## 1. Vision : un seul point d'entrée opérationnel

`make` devient le **point d'entrée unique** pour :
- **Lancer** le projet (Docker, services, modules)
- **Maintenir** (migrations, dépendances, images)
- **Mettre à jour** (rebuild, restart, pull)
- **Contrôler** (état des services, logs, santé)
- **Valider** avant prod (tests, lint, checklist sécurité)

Toute commande opérationnelle passe par `make` — les agents et l'utilisateur n'ont pas besoin de connaître les détails Docker/Django.

---

## 2. Principes de répartition des responsabilités

| Pilote | Responsabilité opérationnelle | Commandes Make associées |
|--------|------------------------------|---------------------------|
| **DevOps** | Infra, conteneurs, déploiement, santé des services | `up`, `down`, `build`, `full`, `restart`, `pull`, `ps`, `logs`, `health`, `prod-check` |
| **Dev Django** | Code, migrations, tests, qualité applicative | `migrate`, `makemigrations`, `shell`, `test`, `lint`, `createsuperuser`, `check` |
| **Chef de Projet** | Validation avant prod, ordonnancement des releases | `validate`, `release-checklist` |
| **Orchestrateur** | Alignement registre ↔ Make, cohérence docs | Vérifier que `make help` reflète la stratégie |

---

## 3. Catalogue des commandes Make (stratégie complète)

### 3.0 Commandes principales (stratégie SquidResearch)

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make start` | **Lancer tout en une commande** | Démarrage séquentiel, attente Django, migrate, health-check, URLs. Usage quotidien recommandé. Pas de venv requis. | DevOps |
| `make go` | **Démarrage à froid complet** | down -v, build, démarrage séquentiel (db→redis→web→celery→n8n,flowise), attente Django, migrate, collectstatic, health-check, affichage URLs | DevOps |
| `make relance` | Redémarrer sans rebuild | Redémarrage séquentiel des services (containers déjà construits) | DevOps |
| `make full-setup` | Configuration complète initiale | build + up + migrate + static + health-check | DevOps |
| `make services-urls` | Afficher les URLs | Liste Django, admin, essais, n8n, Flowise, PostgreSQL, Redis | Tous |
| `make info` | Informations projet | Versions Python, Docker, liste des services | Tous |
| `make backup` | Sauvegarder la base | pg_dump vers `backups/backup_YYYYMMDD_HHMMSS.sql` | DevOps |
| `make restore` | Restaurer la base | Liste les sauvegardes ; restauration manuelle | DevOps |
| `make backup-clean` | Nettoyer sauvegardes | Supprime les backups > 7 jours | DevOps |
| `make security-check` | Vérifier CVE | safety check (dépendances) | Dev Django |

**Stratégies SquidResearch intégrées** :
- Chargement automatique du `.env` (variables d'environnement)
- Couleurs dans les messages (GREEN, YELLOW, CYAN, etc.)
- Démarrage séquentiel (éviter race conditions db → web → celery)
- Attente que Django soit prêt avant migrate (`migrate-wait`)
- Commande `go` = tout depuis zéro en une seule commande

### 3.1 Lancement et arrêt

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make up` | Lancer le stack standard | `docker compose up -d` (db, redis, web, celery, celery-beat, n8n, flowise) | DevOps |
| `make down` | Arrêter le stack | `docker compose down` | DevOps |
| `make full` | Lancer le stack complet | Profil `full` : enriched + kalilinux (OSINT, stratégie enrichissement) | DevOps / Growth |
| `make restart` | Redémarrer tous les services | `docker compose restart` | DevOps |
| `make stop` | Arrêter sans supprimer | `docker compose stop` | DevOps |

### 3.2 Build et mise à jour

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make build` | Construire les images | `docker compose build` | DevOps |
| `make build-no-cache` | Reconstruire sans cache | `docker compose build --no-cache` | DevOps |
| `make pull` | Mettre à jour les images de base | `docker compose pull` | DevOps |
| `make update` | Pull + build + restart | Mise à jour complète du stack | DevOps |

### 3.3 Migrations et base de données

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make migrate` | Appliquer les migrations | `docker compose exec web python manage.py migrate --noinput` | Dev Django |
| `make makemigrations` | Créer les migrations | `docker compose exec web python manage.py makemigrations` | Dev Django |
| `make dbshell` | Shell PostgreSQL | `docker compose exec db psql -U ${DB_USER} -d ${DB_NAME}` | DevOps / Dev Django |
| `make reset-db` | Réinitialiser la DB (⚠️ destructif) | Drop + create + migrate | Dev Django (dev uniquement) |

**Avant migrations / relance** : sauvegarder l’état (commit + push) puis migrations puis relance. Voir **`procedure-avant-migrations-relance.md`** (Architecte, DevOps, Dev Django).

### 3.4 Django : administration et maintenance

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make shell` | Shell Django | `python manage.py shell` | Dev Django |
| `make createsuperuser` | Créer un superutilisateur | Interactif | DevOps / Dev Django |
| `make static` | Collecter les fichiers statiques | `collectstatic --noinput` | Dev Django |
| `make check` | Vérifier la config Django | `python manage.py check` | Dev Django |
| `make showmigrations` | Lister l'état des migrations | `python manage.py showmigrations` | Dev Django |

### 3.5 Tests et qualité

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make test` | Lancer les tests | `pytest` (SQLite, hors Docker) | Dev Django |
| `make test-docker` | Tests dans le conteneur web | `docker compose exec web pytest` | Dev Django |
| `make lint` | Linter le code | flake8, black --check, isort --check | Dev Django |
| `make lint-fix` | Corriger automatiquement | black, isort | Dev Django |
| `make validate` | Validation complète avant prod | check + test + lint + prod-check | Chef de Projet |

### 3.6 Contrôle et observation

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make ps` | État des services | `docker compose ps` | DevOps |
| `make logs` | Logs en temps réel | `docker compose logs -f` | DevOps |
| `make logs-web` | Logs du service web uniquement | `docker compose logs -f web` | DevOps |
| `make logs-celery` | Logs Celery | `docker compose logs -f celery` | DevOps |
| `make health` | Vérifier la santé des services | Ping db, redis, web (healthcheck) | DevOps |

### 3.7 Dev local (WSL / Linux sans Docker web)

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make venv-install` | **Créer venv + installer deps** | Crée .venv + `pip install -r requirements.txt` (dont django-environ). Corrige ModuleNotFoundError en WSL. | DevOps |
| `make runserver` | Lancer Django en local | Utilise `.venv/bin/python` si présent, sinon `python3` (db+redis en Docker ou .env local) | Dev Django |
| `make venv` | Créer le venv uniquement | `python3 -m venv .venv` + instructions (sans installer deps) | DevOps |
| `make dev` | Démarrer db+redis pour dev local | `docker compose up -d db redis` ; puis `make venv-install && make runserver` | DevOps |

### 3.8 Sécurité et production

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make prod-check` | Checklist avant prod | Vérifie DEBUG=False, ALLOWED_HOSTS, secrets | Chef de Projet / DevOps |
| `make secret-key` | Générer une SECRET_KEY | `python -c "from django.core.management.utils import get_random_secret_key; print(...)"` | DevOps |

### 3.9 Modules spécifiques (n8n, Flowise, Celery)

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make celery-restart` | Redémarrer le worker Celery | `docker compose restart celery` | DevOps |
| `make celery-beat-restart` | Redémarrer Celery Beat | `docker compose restart celery-beat` | DevOps |
| `make n8n-logs` | Logs n8n | `docker compose logs -f n8n` | Growth / DevOps |
| `make flowise-logs` | Logs Flowise | `docker compose logs -f flowise` | Growth / DevOps |

### 3.10 Autres

| Commande | Rôle | Description | Pilote |
|----------|------|-------------|--------|
| `make help` | Aide | Liste toutes les commandes disponibles | Tous |
| `make clean` | Nettoyer (cache, __pycache__, .pyc) | Supprimer les artefacts locaux | Dev Django |

---

## 4. Workflows opérationnels (qui fait quoi, quand)

### 4.1 Premier lancement (nouvelle machine / nouveau dev)

```
1. DevOps   : cp .env.example .env ; éditer .env (SECRET_KEY, DB_PASSWORD)
2. DevOps   : make build
3. DevOps   : make up
4. DevOps   : make createsuperuser
5. Dev Django : (optionnel) make migrate si entrypoint n'a pas migré
6. Tous    : Ouvrir http://localhost:8000/admin/
```

**Référence** : `docs/base-de-connaissances/pret-a-demarrer.md`

### 4.2 Après modification du code (feature, bugfix)

```
1. Dev Django : make makemigrations  (si modèles modifiés)
2. Dev Django : make test            (valider avant commit)
3. Dev Django : make lint            (qualité)
4. DevOps   : make build             (si Dockerfile/requirements modifiés)
5. DevOps   : make restart           (ou make up si down)
6. Dev Django : make migrate         (si nouvelles migrations)
```

### 4.3 Mise à jour du stack (dépendances, images)

```
1. DevOps   : make pull              (images de base)
2. DevOps   : make build             (rebuild avec nouveaux requirements)
3. Chef Projet : make validate       (check + test + lint + prod-check)
4. DevOps   : make restart           (appliquer les changements)
5. Dev Django : make migrate         (si migrations Django liées)
```

### 4.4 Avant déploiement en production

```
1. Dev Django : make check
2. Dev Django : make test
3. Dev Django : make lint
4. Chef Projet : make prod-check     (checklist regles-securite.md)
5. Chef Projet : make release-checklist  (validation finale)
6. DevOps   : (déploiement selon processus CI/CD ou manuel)
```

**Référence** : `docs/base-de-connaissances/regles-securite.md` § 9

### 4.5 Dépannage (admin ne répond pas, erreur 500)

```
1. DevOps   : make ps                (services up ?)
2. DevOps   : make logs-web          (erreurs applicatives ?)
3. DevOps   : make health            (db, redis OK ?)
4. Dev Django : make shell           (débugger en Python)
5. Si Windows ERR_EMPTY_RESPONSE : Option B (pret-a-demarrer.md § 5)
   - make dev
   - make runserver
```

### 4.6 Lancer les modules enrichissement (enriched, Kali)

```
1. DevOps / Growth : make full       (profil full)
2. Growth   : Contrôler enriched, kalilinux via make ps
3. Growth   : make logs (ou cible enrich) pour suivi
```

---

## 5. Règles de coordination entre pilotes

### 5.1 DevOps

- **Possède** : `Makefile` (commandes infra), `docker-compose.yml`, `.env.example`
- **Consulte** : Dev Django pour migrations, requirements ; Chef de Projet pour validation prod
- **Informe** : Chef de Projet quand le stack est prêt pour validation ; tous quand une nouvelle commande Make est ajoutée

### 5.2 Dev Django

- **Possède** : Migrations, tests, lint, `requirements.txt`
- **Consulte** : DevOps pour build, ports, env ; Chef de Projet pour ordonnancement des releases
- **Informe** : DevOps quand `requirements.txt` ou Dockerfile doit changer ; Chef de Projet quand les tests passent

### 5.3 Chef de Projet

- **Possède** : Validation finale, checklist prod, ordonnancement des releases
- **Consulte** : DevOps pour l'état du stack ; Dev Django pour l'état des tests
- **Informe** : Tous quand une release est validée ou bloquée

### 5.4 Orchestrateur

- **Vérifie** : Le registre `registre-agents-ressources.md` référence ce document ; `make help` est à jour ; les guides (GUIDE-CHEF-PROJET, GUIDE-AGENTS) pointent vers la stratégie opérationnelle

---

## 6. Intégration avec les segmentations

Les segmentations existantes (ex. `2025-01-30-lancement-docker-projet.md`) **référencent** les commandes Make :

- **DevOps** exécute `make build`, `make up`, `make createsuperuser` dans le cadre de la mobilisation système
- **Dev Django** exécute `make migrate`, `make test` dans le cadre du développement

Toute nouvelle segmentation impliquant des opérations système doit :
1. Lister les commandes Make à exécuter
2. Indiquer le pilote responsable
3. Référencer ce document (`strategie-operationnelle-make.md`)

---

## 7. Inspiration SquidResearch (intégrée)

Stratégies reprises du Makefile SquidResearch (chemin WSL : `\\wsl.localhost\Ubuntu-22.04\home\lucas\tools\squidResearch`) :

- **`go`** : démarrage à froid complet (down -v, build, up séquentiel, migrate, collectstatic, health)
- **`relance`** : redémarrage sans rebuild (plus rapide)
- **Démarrage séquentiel** : db redis → web → celery → n8n flowise (éviter race conditions)
- **Attente Django** : boucle `until docker compose exec web python manage.py check` avant migrate
- **Chargement .env** : `include .env` + export des variables
- **Couleurs** : messages colorés (GREEN, YELLOW, CYAN, RED)
- **backup / restore / backup-clean** : maintenance base de données
- **services-urls / info** : affichage des URLs et infos projet

---

## 8. Évolutions futures (boîte à idées)

- **CI/CD** : GitHub Actions / GitLab CI appelant `make validate` avant merge, `make build` + déploiement sur push main
- **Makefile targets** : `make deploy-staging`, `make deploy-prod` (SquidResearch a ces cibles)
- **Monitoring** : `make health` étendu (Prometheus, healthcheck HTTP)
- **Backup** : `make backup-db`, `make restore-db` (PostgreSQL dump/restore)
- **Environnements multiples** : `make up-env=staging`, `make up-env=prod` (fichiers docker-compose par env)

---

## 8. Références

- **Makefile** : racine du projet
- **Infra** : `docs/base-de-connaissances/infra-devops.md`
- **Prêt à démarrer** : `docs/base-de-connaissances/pret-a-demarrer.md`
- **Sécurité** : `docs/base-de-connaissances/regles-securite.md`
- **Registre** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Rôles** : `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Règle DevOps** : `.cursor/rules/devops.mdc`

---

## 10. Validation par l'équipe technique

| Pilote | Validation | Date |
|--------|------------|------|
| DevOps | [ ] Stratégie cohérente avec infra existante | |
| Dev Django | [ ] Commandes migrations/tests/lint adaptées | |
| Chef de Projet | [ ] Workflows de validation et release OK | |
| Orchestrateur | [ ] Alignement registre et docs | |

---

*Document créé pour discussion avec l'équipe technique et les responsables. Dernière mise à jour : 2025-01-30.*
