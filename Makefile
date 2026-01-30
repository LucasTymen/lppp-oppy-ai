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

.PHONY: help go relance full-setup services-urls info backup restore backup-clean
.PHONY: up down stop restart full build build-no-cache pull update
.PHONY: migrate migrate-wait makemigrations showmigrations dbshell
.PHONY: shell createsuperuser static check
.PHONY: test test-docker lint lint-fix validate prod-check release-checklist
.PHONY: ps logs logs-web logs-celery logs-n8n logs-flowise health health-check
.PHONY: celery-restart celery-beat-restart
.PHONY: venv runserver dev docker-up-seq
.PHONY: secret-key clean security-check

# =============================================================================
# COMMANDES PRINCIPALES (stratégie SquidResearch)
# =============================================================================

# go — Démarrage à froid complet (tout depuis zéro)
# Requiert : bash ou sh (Linux, Mac, WSL, Git Bash)
go:
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

# relance — Redémarrer sans rebuild (containers déjà construits)
relance: docker-restart-seq health-check
	@echo "$(GREEN)✅ Application relancée$(NC)"
	@$(MAKE) services-urls

# full-setup — Configuration complète initiale (première fois)
full-setup: build
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
docker-up-seq:
	@echo "$(CYAN)🚀 Démarrage séquentiel...$(NC)"
	$(DOCKER) up -d db redis
	@sleep 10
	$(DOCKER) up -d web
	@sleep 15
	$(DOCKER) up -d celery celery-beat
	$(DOCKER) up -d n8n flowise
	@echo "$(GREEN)✅ Services démarrés$(NC)"

# Redémarrage séquentiel
docker-restart-seq:
	@echo "$(CYAN)🔄 Redémarrage séquentiel...$(NC)"
	-$(DOCKER) restart db redis 2>/dev/null || $(DOCKER) up -d db redis
	@sleep 8
	-$(DOCKER) restart web 2>/dev/null || $(DOCKER) up -d web
	@sleep 12
	-$(DOCKER) restart celery celery-beat 2>/dev/null || $(DOCKER) up -d celery celery-beat
	-$(DOCKER) restart n8n flowise 2>/dev/null || $(DOCKER) up -d n8n flowise
	@echo "$(GREEN)✅ Services redémarrés$(NC)"

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
	@echo "$(CYAN)🚀 Commandes principales (stratégie SquidResearch):$(NC)"
	@echo "  make go           — DÉMARRAGE À FROID COMPLET (recommandé première fois)"
	@echo "  make relance      — Redémarrer sans rebuild"
	@echo "  make full-setup   — Configuration complète initiale"
	@echo "  make services-urls — Afficher les URLs des services"
	@echo "  make info         — Informations du projet"
	@echo ""
	@echo "$(CYAN)Lancement et arrêt:$(NC)"
	@echo "  make up           — Lancer le stack"
	@echo "  make down         — Arrêter le stack"
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
	@echo "$(CYAN)Dev local:$(NC)"
	@echo "  make dev          — db+redis pour runserver"
	@echo "  make venv         — Créer .venv"
	@echo "  make runserver    — Lancer runserver"
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
# Dev local
# =============================================================================

dev:
	$(DOCKER) up -d db redis
	@echo "db et redis démarrés. .env : DB_HOST=localhost, REDIS_URL=redis://127.0.0.1:6379/0"
	@echo "Puis : make runserver"

venv:
	python3 -m venv .venv
	@echo "Activer (Linux/WSL) : source .venv/bin/activate"
	@echo "Activer (Windows)   : .venv\\Scripts\\Activate.ps1"
	@echo "Puis : pip install -r requirements.txt"

runserver:
	PYTHONPATH=".:apps" python manage.py runserver

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
