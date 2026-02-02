# LandingsPagesPourProspections — Makefile (stratégie SquidResearch + opérationnelle LPPP)
# Référence : docs/base-de-connaissances/strategie-operationnelle-make.md
# Inspiration : SquidResearch Makefile (go, relance, démarrage séquentiel, backup, etc.)
# Usage : make help

# Chargement automatique du .env (stratégie SquidResearch)
ifneq (,$(wildcard .env))
include .env
export $(shell sed -n 's/^\([A-Za-z_][A-Za-z0-9_]*\)=.*/\1/p' .env 2>/dev/null)
endif

PYTHONPATH := .:apps
export PYTHONPATH

# Variables (stratégie SquidResearch)
PROJECT_NAME = LPPP
DOCKER = docker compose
SERVICES = db redis web celery celery-beat n8n flowise

# Couleurs pour les messages (stratégie SquidResearch)
GREEN  = \033[0;32m
YELLOW = \033[1;33m
RED    = \033[0;31m
CYAN   = \033[0;36m
NC     = \033[0m

.PHONY: help start go relance full-setup services-urls info backup restore backup-clean
.PHONY: up down stop restart full build build-no-cache pull update clean-containers
.PHONY: migrate migrate-wait makemigrations showmigrations dbshell
.PHONY: shell createsuperuser landing-p4s static check
.PHONY: test test-docker lint lint-fix validate prod-check release-checklist
.PHONY: ps logs logs-web logs-celery logs-n8n logs-flowise health health-check
.PHONY: celery-restart celery-beat-restart
.PHONY: venv venv-install runserver dev docker-up-seq ensure-env
.PHONY: secret-key clean security-check

# =============================================================================
# Prérequis Docker (.env requis par docker-compose env_file)
# =============================================================================
# Si .env n'existe pas, docker compose up échoue. Créer .env depuis .env.example.
ensure-env:
	@if [ ! -f .env ]; then \
		echo "$(YELLOW)⚠️  Fichier .env absent — copie depuis .env.example$(NC)"; \
		cp .env.example .env; \
		echo "$(GREEN)✅ .env créé. Vérifier SECRET_KEY et mots de passe si besoin.$(NC)"; \
	else \
		echo "$(GREEN)✅ .env présent$(NC)"; \
	fi

# =============================================================================
# COMMANDES PRINCIPALES (stratégie SquidResearch)
# =============================================================================

# go — Démarrage à froid complet (tout depuis zéro)
# Requiert : bash ou sh (Linux, Mac, WSL, Git Bash)
go: ensure-env
	@echo "$(CYAN)🚀 $(PROJECT_NAME) — DÉMARRAGE À FROID COMPLET$(NC)"
	@echo "$(YELLOW)⚠️  Arrêt et nettoyage des services existants...$(NC)"
	$(DOCKER) down -v --remove-orphans 2>/dev/null || $(DOCKER) down
	@echo "$(GREEN)✅ Services arrêtés$(NC)"
	@echo ""
	@echo "$(CYAN)🔨 Construction des images...$(NC)"
	$(DOCKER) build
	@echo "$(GREEN)✅ Images construites$(NC)"
	@echo ""
	@echo "$(CYAN)🚀 Démarrage séquentiel (db → redis → web → celery → n8n, flowise)...$(NC)"
	$(DOCKER) up -d db redis
	@sleep 10
	$(DOCKER) up -d web
	@sleep 15
	$(DOCKER) up -d celery celery-beat
	$(DOCKER) up -d n8n flowise
	@echo "$(GREEN)✅ Services démarrés$(NC)"
	@echo ""
	@echo "$(CYAN)⏳ Attente que Django soit prêt...$(NC)"
	@until $(DOCKER) exec web python manage.py check >/dev/null 2>&1; do \
		echo "  Django pas encore prêt, attente 5s..."; sleep 5; \
	done
	@echo "$(GREEN)✅ Django prêt$(NC)"
	@echo ""
	@echo "$(CYAN)📝 Migrations...$(NC)"
	$(DOCKER) exec web python manage.py migrate --noinput
	@echo "$(CYAN)📦 Fichiers statiques...$(NC)"
	$(DOCKER) exec web python manage.py collectstatic --noinput --clear 2>/dev/null || true
	@echo "$(GREEN)✅ Config Django terminée$(NC)"
	@echo ""
	@echo "$(YELLOW)👤 Créer un superutilisateur : make createsuperuser$(NC)"
	@echo ""
	@$(MAKE) health-check
	@echo ""
	@echo "$(GREEN)🎉 DÉMARRAGE TERMINÉ !$(NC)"
	@$(MAKE) services-urls

# start — Lancer tout le stack en une commande (démarrer ou redémarrer)
# Usage quotidien recommandé. Pas de venv requis : tout tourne dans Docker.
start: docker-up-seq
	@echo "$(CYAN)⏳ Attente que Django soit prêt...$(NC)"
	@until $(DOCKER) exec web python manage.py check >/dev/null 2>&1; do \
		echo "  Django pas encore prêt, attente 5s..."; sleep 5; \
	done
	@echo "$(GREEN)✅ Django prêt$(NC)"
	@$(MAKE) migrate
	@$(MAKE) health-check
	@echo ""
	@$(MAKE) services-urls

# relance — Redémarrer sans rebuild (containers déjà construits)
relance: docker-restart-seq health-check
	@echo "$(GREEN)✅ Application relancée$(NC)"
	@$(MAKE) services-urls

# full-setup — Configuration complète initiale (première fois)
full-setup: ensure-env build
	@echo "$(CYAN)🚀 Configuration complète $(PROJECT_NAME)...$(NC)"
	$(DOCKER) up -d
	@sleep 15
	@$(MAKE) migrate
	@$(MAKE) static
	@echo "$(YELLOW)👤 Créer un superutilisateur : make createsuperuser$(NC)"
	@$(MAKE) health-check
	@echo "$(GREEN)🎯 Configuration terminée !$(NC)"
	@$(MAKE) services-urls

# Démarrage séquentiel (éviter race conditions)
docker-up-seq: ensure-env
	@echo "$(CYAN)🚀 Démarrage séquentiel...$(NC)"
	$(DOCKER) up -d db redis
	@sleep 10
	$(DOCKER) up -d web
	@sleep 15
	$(DOCKER) up -d celery celery-beat
	$(DOCKER) up -d n8n flowise
	@echo "$(GREEN)✅ Services démarrés$(NC)"

# Redémarrage séquentiel (up -d redémarre aussi les conteneurs Exited)
docker-restart-seq:
	@echo "$(CYAN)🔄 Démarrage/redémarrage séquentiel...$(NC)"
	$(DOCKER) up -d db redis
	@sleep 8
	$(DOCKER) up -d web
	@sleep 12
	$(DOCKER) up -d celery celery-beat n8n flowise
	@echo "$(GREEN)✅ Services démarrés$(NC)"

# =============================================================================
# Aide et informations (stratégie SquidResearch)
# =============================================================================

services-urls:
	@echo "$(CYAN)📊 URLs des services$(NC)"
	@echo "  🌐 Django:       http://localhost:8000"
	@echo "  📊 Admin:        http://localhost:8000/admin/"
	@echo "  📋 Essais:       http://localhost:8000/essais/"
	@echo "  🔄 n8n:          http://localhost:5678"
	@echo "  🤖 Flowise:      http://localhost:3000"
	@echo "  🗄️  PostgreSQL:   localhost:5432"
	@echo "  🔴 Redis:        localhost:6379"

info:
	@echo "$(CYAN)📊 $(PROJECT_NAME) — Informations$(NC)"
	@echo "  Python:  $$(python --version 2>/dev/null || echo 'N/A')"
	@echo "  Docker:  $$(docker --version 2>/dev/null || echo 'N/A')"
	@echo "  Services: $(SERVICES)"
	@echo "  Doc: docs/base-de-connaissances/strategie-operationnelle-make.md"

# =============================================================================
# Aide (make help)
# =============================================================================

help:
	@echo "$(GREEN)$(PROJECT_NAME) — Landings Pages Pour Prospections$(NC)"
	@echo ""
	@echo "$(CYAN)🚀 Commandes principales:$(NC)"
	@echo "  make start        — LANCER TOUT en une commande (usage quotidien, pas de venv)"
	@echo "  make go           — DÉMARRAGE À FROID COMPLET (première fois ou reset)"
	@echo "  make relance      — Redémarrer sans rebuild"
	@echo "  make full-setup   — Configuration complète initiale"
	@echo "  make services-urls — Afficher les URLs des services"
	@echo "  make info         — Informations du projet"
	@echo ""
	@echo "$(CYAN)Lancement et arrêt:$(NC)"
	@echo "  make start        — Lancer tout (séquentiel, attente Django, migrate)"
	@echo "  make up           — Lancer le stack (sans attente)"
	@echo "  make down         — Arrêter le stack"
	@echo "  make clean-containers — Supprimer conteneurs lppp_* (si « name already in use »)"
	@echo "  make stop         — Arrêter sans supprimer"
	@echo "  make restart      — Redémarrer"
	@echo "  make full         — Stack complet (enriched + kalilinux)"
	@echo ""
	@echo "$(CYAN)Build et mise à jour:$(NC)"
	@echo "  make build        — Construire les images"
	@echo "  make build-no-cache — Reconstruire sans cache"
	@echo "  make pull         — Mettre à jour les images"
	@echo "  make update       — Pull + build + restart"
	@echo ""
	@echo "$(CYAN)Migrations et base:$(NC)"
	@echo "  make migrate      — Appliquer les migrations"
	@echo "  make migrate-wait — Migrer après attente Django"
	@echo "  make makemigrations — Créer les migrations"
	@echo "  make showmigrations — État des migrations"
	@echo "  make dbshell      — Shell PostgreSQL"
	@echo ""
	@echo "$(CYAN)Django:$(NC)"
	@echo "  make shell        — Shell Django"
	@echo "  make createsuperuser — Créer un superutilisateur"
	@echo "  make landing-p4s  — Créer/mettre à jour la landing P4S en base (évite 404 /p/p4s-archi/)"
	@echo "  make push-both    — Push sur origin main + gitlab main (WSL/Git Bash)"
	@echo "  make commit-push MSG=\"...\" — add ., commit, push sur les deux remotes"
	@echo "  make static       — Collecter les fichiers statiques"
	@echo "  make check        — Vérifier la config Django"
	@echo ""
	@echo "$(CYAN)Tests et qualité:$(NC)"
	@echo "  make test         — pytest (local, SQLite)"
	@echo "  make test-docker  — pytest dans le conteneur"
	@echo "  make lint         — flake8, black, isort (check)"
	@echo "  make lint-fix     — Formatage auto"
	@echo "  make validate     — check + test + lint + prod-check"
	@echo "  make prod-check   — Checklist avant prod"
	@echo "  make release-checklist — Validation finale"
	@echo "  make security-check — safety check (CVE)"
	@echo ""
	@echo "$(CYAN)Contrôle:$(NC)"
	@echo "  make ps           — État des services"
	@echo "  make logs         — Logs temps réel"
	@echo "  make logs-web     — Logs web"
	@echo "  make logs-celery  — Logs Celery"
	@echo "  make health       — Santé des services"
	@echo "  make health-check — Vérification détaillée"
	@echo ""
	@echo "$(CYAN)Maintenance (stratégie SquidResearch):$(NC)"
	@echo "  make backup       — Sauvegarder la base"
	@echo "  make restore      — Restaurer la base"
	@echo "  make backup-clean — Nettoyer anciennes sauvegardes"
	@echo ""
	@echo "$(CYAN)Dev local (WSL / Linux sans Docker):$(NC)"
	@echo "  make venv-install — Créer .venv + installer deps (dont django-environ) — corriger ModuleNotFoundError en WSL"
	@echo "  make runserver     — Lancer Django en local (utilise .venv si présent)"
	@echo "  make dev          — db+redis pour runserver (Docker) ; puis make venv-install && make runserver"
	@echo "  make venv         — Créer .venv uniquement (sans installer deps)"
	@echo ""
	@echo "$(CYAN)Prérequis Docker:$(NC)"
	@echo "  make ensure-env   — Créer .env depuis .env.example si absent (évite plantage compose)"
	@echo ""
	@echo "$(CYAN)Utilitaires:$(NC)"
	@echo "  make secret-key   — Générer SECRET_KEY"
	@echo "  make clean        — Nettoyer cache"

# =============================================================================
# Lancement et arrêt
# =============================================================================

up:
	$(DOCKER) up -d

down:
	$(DOCKER) down

# Supprimer les conteneurs LPPP par nom (quand "container name already in use" après make down)
# Utile si les conteneurs ont été créés sous un autre répertoire / projet Compose
clean-containers:
	@echo "$(YELLOW)Suppression des conteneurs lppp_* (conflit de noms)...$(NC)"
	@docker rm -f lppp_web lppp_celery lppp_celery_beat lppp_db lppp_redis lppp_n8n lppp_flowise lppp_enriched lppp_kali 2>/dev/null || true
	@echo "$(GREEN)✅ Conteneurs supprimés. Relancer : make start$(NC)"

stop:
	$(DOCKER) stop

restart:
	$(DOCKER) restart

full:
	$(DOCKER) --profile full up -d

# =============================================================================
# Build et mise à jour
# =============================================================================

build:
	$(DOCKER) build

build-no-cache:
	$(DOCKER) build --no-cache

pull:
	$(DOCKER) pull

update: pull build restart
	@echo "Mise à jour terminée. Penser à : make migrate"

# =============================================================================
# Migrations et base de données
# =============================================================================

migrate:
	$(DOCKER) exec web python manage.py migrate --noinput

# Migration avec attente que Django soit prêt (stratégie SquidResearch)
migrate-wait:
	@echo "$(YELLOW)⏳ Attente que Django soit prêt...$(NC)"
	@until $(DOCKER) exec web python manage.py check >/dev/null 2>&1; do sleep 5; done
	@echo "$(GREEN)✅ Application des migrations...$(NC)"
	$(DOCKER) exec web python manage.py migrate --noinput

makemigrations:
	$(DOCKER) exec web python manage.py makemigrations

showmigrations:
	$(DOCKER) exec web python manage.py showmigrations

dbshell:
	$(DOCKER) exec db psql -U lpppuser -d lppp

# =============================================================================
# Django : administration et maintenance
# =============================================================================

shell:
	$(DOCKER) exec web python manage.py shell

createsuperuser:
	$(DOCKER) exec web python manage.py createsuperuser

# Recréer / mettre à jour la landing P4S en base (évite 404 sur /p/p4s-archi/)
landing-p4s:
	$(DOCKER) exec web python manage.py create_landing_p4s --update --publish
	@echo "$(GREEN)✅ Landing P4S à jour. URL : http://localhost:8000/p/p4s-archi/$(NC)"

static:
	$(DOCKER) exec web python manage.py collectstatic --noinput

check:
	$(DOCKER) exec web python manage.py check

# =============================================================================
# Tests et qualité
# =============================================================================

test:
	PYTEST_USE_SQLITE=1 PYTHONPATH=".:apps" python -m pytest apps/ -v --tb=short 2>/dev/null || true

test-docker:
	$(DOCKER) exec web python -m pytest apps/ -v --tb=short 2>/dev/null || true

lint:
	@echo "=== flake8 ===" && (flake8 apps/ lppp/ --max-line-length=120 --exclude=migrations 2>/dev/null || echo "flake8: pip install flake8")
	@echo "=== black ===" && (black apps/ lppp/ --check --exclude=migrations 2>/dev/null || echo "black: pip install black")
	@echo "=== isort ===" && (isort apps/ lppp/ --check-only --skip=migrations 2>/dev/null || echo "isort: pip install isort")

lint-fix:
	black apps/ lppp/ --exclude=migrations 2>/dev/null || true
	isort apps/ lppp/ --skip=migrations 2>/dev/null || true

security-check:
	@echo "$(CYAN)🔒 Vérification CVE (safety)...$(NC)"
	@which safety >/dev/null 2>&1 && safety check || echo "safety non installé : pip install safety"

prod-check:
	@echo "Checklist avant prod (regles-securite.md) :"
	@echo "  Vérifier : DEBUG=False, SECRET_KEY forte, ALLOWED_HOSTS explicite"
	@PYTHONPATH=".:apps" python manage.py check --deploy 2>/dev/null || echo "  (Django check --deploy : exécuter manuellement si erreur)"

validate:
	@echo "=== Django check ===" && PYTHONPATH=".:apps" python manage.py check
	@echo "=== Tests ===" && $(MAKE) test
	@echo "=== Lint ===" && $(MAKE) lint
	@echo "=== Prod check ===" && $(MAKE) prod-check
	@echo "$(GREEN)Validation terminée.$(NC)"

release-checklist: validate
	@echo "Release checklist :"
	@echo "  [ ] DEBUG=False | [ ] SECRET_KEY forte | [ ] ALLOWED_HOSTS | [ ] HTTPS"
	@echo "Voir docs/base-de-connaissances/regles-securite.md § 9"

# =============================================================================
# Contrôle et observation
# =============================================================================

ps:
	$(DOCKER) ps

logs:
	$(DOCKER) logs -f

logs-web:
	$(DOCKER) logs -f web

logs-celery:
	$(DOCKER) logs -f celery

logs-n8n:
	$(DOCKER) logs -f n8n

logs-flowise:
	$(DOCKER) logs -f flowise

health:
	@echo "Vérification db..." && $(DOCKER) exec db pg_isready -U lpppuser -d lppp 2>/dev/null || echo "db: N/A"
	@echo "Vérification redis..." && $(DOCKER) exec redis redis-cli ping 2>/dev/null || echo "redis: N/A"
	@curl -s -o /dev/null -w "Web: %{http_code}\n" http://localhost:8000/ 2>/dev/null || echo "web: non accessible"

# Vérification santé détaillée (stratégie SquidResearch)
health-check:
	@echo "$(CYAN)🏥 Santé des services$(NC)"
	@for s in $(SERVICES); do \
		if $(DOCKER) ps $$s 2>/dev/null | grep -q Up; then \
			echo "  $(GREEN)✅ $$s$(NC)"; \
		else \
			echo "  $(RED)❌ $$s$(NC)"; \
		fi; \
	done

# =============================================================================
# Maintenance — Sauvegarde et restauration (stratégie SquidResearch)
# =============================================================================

backup:
	@mkdir -p backups
	@echo "$(CYAN)💾 Sauvegarde de la base...$(NC)"
	$(DOCKER) exec db pg_dump -U lpppuser lppp > backups/backup_$$(date +%Y%m%d_%H%M%S).sql
	@echo "$(GREEN)✅ Sauvegarde créée dans backups/$(NC)"

restore:
	@echo "$(YELLOW)📥 Restauration — Lister les sauvegardes :$(NC)"
	@ls -la backups/ 2>/dev/null || echo "Aucune sauvegarde. Usage : $(DOCKER) exec -i db psql -U lpppuser lppp < backups/backup_XXX.sql"

backup-clean:
	@echo "$(CYAN)🧹 Nettoyage sauvegardes > 7 jours$(NC)"
	@find backups -name "backup_*.sql" -mtime +7 -delete 2>/dev/null || true
	@echo "$(GREEN)✅ Nettoyage terminé$(NC)"

# =============================================================================
# Modules
# =============================================================================

celery-restart:
	$(DOCKER) restart celery

celery-beat-restart:
	$(DOCKER) restart celery-beat

# =============================================================================
# Dev local (WSL / Linux / option B sans Docker)
# =============================================================================
# Référence : docs/base-de-connaissances/pret-a-demarrer.md § 5.1 (ModuleNotFoundError environ)
# DevOps : venv-install, runserver. Dev Django : deps, check. Orchestrateur : cohérence Make ↔ doc.

dev:
	$(DOCKER) up -d db redis
	@echo "db et redis démarrés. .env : DB_HOST=localhost, REDIS_URL=redis://127.0.0.1:6379/0"
	@echo "Puis : make venv-install && make runserver"

# venv — Créer le venv uniquement (sans installer les deps)
venv:
	python3 -m venv .venv 2>/dev/null || python -m venv .venv
	@echo "Activer (Linux/WSL) : source .venv/bin/activate"
	@echo "Activer (Windows)   : .venv\\Scripts\\Activate.ps1"
	@echo "Puis : make venv-install ou pip install -r requirements.txt"

# venv-install — Créer le venv + installer toutes les dépendances (dont django-environ)
# À utiliser en WSL/Linux quand ModuleNotFoundError: No module named 'environ'
venv-install:
	@if [ ! -d .venv ]; then echo "$(CYAN)Création du venv...$(NC)"; python3 -m venv .venv 2>/dev/null || python -m venv .venv; fi
	@echo "$(CYAN)Installation des dépendances (requirements.txt)...$(NC)"
	@if [ -f .venv/bin/pip ]; then .venv/bin/pip install -r requirements.txt; elif [ -f .venv/Scripts/pip.exe ]; then .venv/Scripts/pip install -r requirements.txt; else pip3 install -r requirements.txt || pip install -r requirements.txt; fi
	@echo "$(GREEN)✅ Venv prêt. Lancer : make runserver$(NC)"

# runserver — Lance Django en local (utilise .venv si présent, sinon python3)
# WSL/Linux : après make venv-install, make runserver fonctionne sans activer le venv à la main
runserver:
	@if [ -f .venv/bin/python ]; then PYTHONPATH=".:apps" .venv/bin/python manage.py runserver; elif [ -f .venv/Scripts/python.exe ]; then PYTHONPATH=".:apps" .venv/Scripts/python.exe manage.py runserver; else PYTHONPATH=".:apps" python3 manage.py runserver 2>/dev/null || PYTHONPATH=".:apps" python manage.py runserver; fi

# =============================================================================
# Utilitaires
# =============================================================================

secret-key:
	@python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

clean:
	@python -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if p.is_dir()]" 2>/dev/null || true
	@python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc') if p.is_file()]" 2>/dev/null || true
	@python -Bc "import pathlib, shutil; p=pathlib.Path('.pytest_cache'); shutil.rmtree(p) if p.exists() else None" 2>/dev/null || true
	@echo "Nettoyage terminé."

# =============================================================================
# Git — commit et push sur les deux remotes (origin + gitlab)
# =============================================================================
# À lancer depuis WSL ou Git Bash (git dans le PATH).
# Exemple : make commit-push MSG="docs: DevOps + Architecte réseau, procédure fin de landing"
# Ou : git add . && git commit -m "ton message" && make push-both

.PHONY: push-both commit-push

push-both:
	git push origin main
	git push gitlab main
	@echo "$(GREEN)✅ Push origin main et gitlab main OK$(NC)"

# commit-push — add ., commit avec MSG=..., push origin + gitlab
# Usage : make commit-push MSG="docs: description du commit"
commit-push:
	@if [ -z "$(MSG)" ]; then echo "$(RED)Usage : make commit-push MSG=\"ton message\"$(NC)"; exit 1; fi
	git add .
	git status
	git commit -m "$(MSG)"
	$(MAKE) push-both
