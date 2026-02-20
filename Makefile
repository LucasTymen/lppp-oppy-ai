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
# Windows : port 8080 au lieu de 8000 pour éviter ERR_CONNECTION_RESET (voir docker-compose.windows.yml)
DOCKER_WIN = docker compose -f docker-compose.yml -f docker-compose.windows.yml
SERVICES = db redis web celery celery-beat n8n flowise

# Couleurs pour les messages (stratégie SquidResearch)
GREEN  = \033[0;32m
YELLOW = \033[1;33m
RED    = \033[0;31m
CYAN   = \033[0;36m
NC     = \033[0m

.PHONY: help start go relance relance-safe full-setup services-urls info backup restore backup-clean
.PHONY: test-cov test-cov-docker test-cov-docker-build
.PHONY: up down stop restart full build build-no-cache pull update clean-containers
.PHONY: migrate migrate-wait makemigrations showmigrations dbshell
.PHONY: shell createsuperuser landing-p4s landing-promovacances landing-promovacances-full landing-infopro landing-infopro-full landings-restore static check
.PHONY: test test-docker lint lint-fix validate prod-check release-checklist
.PHONY: start-win services-urls-win ps logs logs-web logs-celery logs-n8n logs-flowise health health-check
.PHONY: celery-restart celery-beat-restart
.PHONY: venv venv-install runserver dev docker-up-seq ensure-env
.PHONY: deploy-contabo secret-key clean security-check

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
# ATTENTION : utilise "down -v" → SUPPRIME les volumes (postgres_data, redis_data, static, media) = PERTE DE DONNÉES.
# Pour préserver les données : utiliser "make relance-safe" (build + start sans supprimer les volumes).
# Requiert : bash ou sh (Linux, Mac, WSL, Git Bash)
go: ensure-env
	@echo "$(CYAN)🚀 $(PROJECT_NAME) — DÉMARRAGE À FROID COMPLET$(NC)"
	@echo "$(RED)⚠️  ATTENTION : down -v supprime les volumes (données BDD, Redis, static, media).$(NC)"
	@echo "$(YELLOW)   Pour garder vos données, utilisez : make relance-safe$(NC)"
	@echo "$(YELLOW)  Arrêt et nettoyage des services existants...$(NC)"
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
# On applique migrate tôt pour que "check" puisse passer (souvent bloqué sinon après clean-containers).
# Après 12 tentatives (1 min), affiche la sortie de "check" pour diagnostiquer.
start: docker-up-seq
	@echo "$(CYAN)⏳ Attente 15s que le conteneur web démarre...$(NC)"
	@sleep 15
	@echo "$(CYAN)📝 Application des migrations...$(NC)"
	@$(DOCKER) exec web python manage.py migrate --noinput 2>/dev/null || true
	@echo "$(CYAN)⏳ Vérification Django (check)...$(NC)"
	@i=0; while [ $$i -lt 12 ]; do \
		if $(DOCKER) exec web python manage.py check >/dev/null 2>&1; then \
			echo "$(GREEN)✅ Django prêt$(NC)"; break; \
		fi; \
		echo "  Django pas encore prêt, attente 5s..."; sleep 5; \
		i=$$(($$i+1)); \
		if [ $$i -eq 12 ]; then \
			echo "$(RED)❌ Django toujours pas prêt après 1 min. Sortie de 'python manage.py check':$(NC)"; \
			$(DOCKER) exec web python manage.py check || true; \
			echo ""; echo "Voir aussi: make logs-web"; exit 1; \
		fi; \
	done
	@$(MAKE) health-check
	@echo ""
	@$(MAKE) services-urls

# relance — Redémarrer sans rebuild (containers déjà construits)
relance: docker-restart-seq health-check
	@echo "$(GREEN)✅ Application relancée$(NC)"
	@$(MAKE) services-urls

# relance-safe — Rebuild + démarrage SANS supprimer les volumes (préserve postgres_data, redis_data, static, media)
# À utiliser quand on ne veut pas perdre ses données. N'utilise pas "down -v".
relance-safe: ensure-env clean-containers
	@echo "$(CYAN)🔨 Construction des images (volumes préservés)...$(NC)"
	$(DOCKER) build
	@echo "$(GREEN)✅ Images construites$(NC)"
	@echo "$(CYAN)🚀 Démarrage séquentiel...$(NC)"
	$(DOCKER) up -d db redis
	@sleep 10
	$(DOCKER) up -d web
	@sleep 15
	$(DOCKER) up -d celery celery-beat
	$(DOCKER) up -d n8n flowise
	@echo "$(CYAN)⏳ Attente que Django soit prêt...$(NC)"
	@until $(DOCKER) exec web python manage.py check >/dev/null 2>&1; do \
		echo "  Django pas encore prêt, attente 5s..."; sleep 5; \
	done
	@echo "$(CYAN)📝 Migrations...$(NC)"
	$(DOCKER) exec web python manage.py migrate --noinput
	@echo "$(CYAN)📦 Fichiers statiques...$(NC)"
	$(DOCKER) exec web python manage.py collectstatic --noinput --clear 2>/dev/null || true
	@$(MAKE) health-check
	@echo "$(GREEN)🎉 Relance terminée (données préservées)$(NC)"
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
	@echo "  🌐 Django:       http://localhost:8010"
	@echo "  📊 Admin:        http://localhost:8010/admin/"
	@echo "  📋 Essais:       http://localhost:8010/essais/"
	@echo "  🔄 n8n:          http://localhost:5681"
	@echo "  🤖 Flowise:      http://localhost:3010"
	@echo "  🗄️  PostgreSQL:   localhost:5433"
	@echo "  🔴 Redis:        localhost:6380"

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
	@echo "  make go           — DÉMARRAGE À FROID COMPLET (⚠️ supprime les volumes = perte de données)"
	@echo "  make relance-safe — Rebuild + start SANS supprimer les volumes (préserve les données)"
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
	@echo "  make landing-p4s     — Créer/mettre à jour la landing P4S en base (évite 404 /p/p4s-archi/)"
	@echo "  make landing-promovacances — Créer la landing Promovacances en base (prérequis : make start)"
	@echo "  make landing-promovacances-full — Start le stack puis créer la landing Promovacances (tout en un)"
	@echo "  make landing-infopro — Créer la landing Infopro Digital en base (prérequis : make start)"
	@echo "  make landing-infopro-full — Start le stack puis créer la landing Infopro (tout en un)"
	@echo "  make landings-restore — Recréer Casapy, FitClem, Promovacances en base (après base vide)"
	@echo "  make sync-landing-p4s — Copier landing-proposition-joel.json vers standalone + frontend"
	@echo "  make push-both    — Push sur origin main + gitlab main (WSL/Git Bash)"
	@echo "  make commit-push MSG=\"...\" — add ., commit, push sur les deux remotes"
	@echo "  make deploy-contabo — Déployer LPPP sur Contabo (rsync + SSH + docker)"
	@echo "  make push-standalone-p4s — push landing P4S vers LPPP_P4S-Architecture (GitHub + GitLab)"
	@echo "  make static       — Collecter les fichiers statiques"
	@echo "  make check        — Vérifier la config Django"
	@echo "  make check-flowise-embed — Diagnostic chatbot (URL embed, .env, port 3010)"
	@echo ""
	@echo "$(CYAN)Tests et qualité:$(NC)"
	@echo "  make test             — pytest (local ; tests DB échouent sans PostgreSQL)"
	@echo "  make test-docker      — pytest dans le conteneur"
	@echo "  make test-cov-docker  — pytest + coverage dans le conteneur (PostgreSQL)"
	@echo "  make test-cov-docker-build — rebuild image web puis test-cov-docker (si No module named pytest)"
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
	@echo "$(GREEN)✅ Landing P4S à jour. URL : http://localhost:8010/p/p4s-archi/$(NC)"

# Créer la landing Promovacances en base (PPP — rapport audit SEO). Prérequis : make start ou Docker up.
landing-promovacances:
	$(DOCKER) exec web python manage.py create_landing_promovacances --publish
	@echo "$(GREEN)✅ Landing Promovacances créée. URL : http://localhost:8010/p/promovacances/$(NC)"

# Enchaîner start puis création Promovacances (à la racine LPPP). Usage : tout lancer quand le stack n'est pas démarré.
# Voir docs/base-de-connaissances/segmentations/2026-02-19-landing-promovacances-creation-coordonnee.md
landing-promovacances-full: start
	@$(MAKE) landing-promovacances

# Créer la landing Infopro Digital (lppp-infopro). Prérequis : make start.
landing-infopro:
	$(DOCKER) exec web python manage.py create_landing_infopro --publish
	@echo "$(GREEN)✅ Landing Infopro Digital créée. URL : http://localhost:8010/p/infopro/$(NC)"

landing-infopro-full: start
	@$(MAKE) landing-infopro

# Recréer en base toutes les landings « générateur » (même système). À lancer après base vide (ex. volume recréé, prod).
# Maisons-Alfort et Yuwell viennent des migrations (migrate). Les autres sont créées ici.
landings-restore:
	$(DOCKER) exec web python manage.py create_landing_casapy --update --publish
	$(DOCKER) exec web python manage.py create_landing_fitclem --update --publish
	$(DOCKER) exec web python manage.py create_landing_promovacances --publish
	$(DOCKER) exec web python manage.py create_landing_infopro --update --publish
	$(DOCKER) exec web python manage.py create_landing_p4s --update --publish
	@echo "$(GREEN)✅ Landings générateur recréées : Casapy, FitClem, Promovacances, Infopro, P4S. + Maisons-Alfort / Yuwell via migrations.$(NC)"

# Synchroniser le contenu P4S (source unique JSON) vers standalone et frontend Next.js
# Après édition de docs/contacts/p4s-archi/landing-proposition-joel.json
sync-landing-p4s:
	@cp docs/contacts/p4s-archi/landing-proposition-joel.json deploy/standalone-p4s/src/content/landing.json && \
	cp docs/contacts/p4s-archi/landing-proposition-joel.json frontend/src/app/p4s-archi/landing.json && \
	echo "$(GREEN)✅ Contenu P4S synchronisé vers standalone + frontend$(NC)"

static:
	$(DOCKER) exec web python manage.py collectstatic --noinput

check:
	$(DOCKER) exec web python manage.py check

# Diagnostic chatbot (écran vide) : URL d'embed, .env, optionnel --ping Flowise. Voir docs/base-de-connaissances/segmentations/2026-01-30-strategie-chatbot-ecran-vide-et-flux.md
check-flowise-embed:
	$(DOCKER) exec web python manage.py check_flowise_embed

# =============================================================================
# Tests et qualité
# =============================================================================

test:
	PYTHONPATH=".:apps" python3 -m pytest apps/ -v --tb=short 2>/dev/null || PYTHONPATH=".:apps" python -m pytest apps/ -v --tb=short 2>/dev/null || true

test-docker:
	$(DOCKER) exec web python -m pytest apps/ -v --tb=short 2>/dev/null || true

# Coverage (feature chatbot, intégration, flux). Local : tests sans DB. Docker : tous les tests + coverage.
test-cov:
	@echo "$(CYAN)📊 Tests avec couverture (apps/)$(NC)"
	PYTHONPATH=".:apps" python3 -m pytest apps/ -v --tb=short --cov=apps --cov-report=term-missing --cov-report=html:htmlcov \
		--cov-config=.coveragerc 2>/dev/null || PYTHONPATH=".:apps" python -m pytest apps/ -v --tb=short --cov=apps --cov-report=term-missing --cov-report=html:htmlcov \
		--cov-config=.coveragerc 2>/dev/null || (echo "$(YELLOW)Installer : pip install -r requirements-test.txt$(NC)" && exit 1)

# Coverage dans le conteneur web (PostgreSQL dispo → tous les tests). Requiert image à jour (pytest dans requirements.txt).
# Si "No module named pytest" : rebuild d'abord avec make build puis make test-cov-docker.
test-cov-docker:
	@echo "$(CYAN)📊 Tests + coverage dans Docker (apps/)$(NC)"
	$(DOCKER) exec web python -m pytest apps/ -v --tb=short --cov=apps --cov-report=term-missing --cov-report=html:htmlcov --cov-config=.coveragerc

# Rebuild de l'image web (installe pytest, pytest-django, pytest-cov) puis tests + coverage
test-cov-docker-build:
	@echo "$(YELLOW)🔨 Rebuild image web (pytest inclus)...$(NC)"
	$(DOCKER) build web
	@echo "$(CYAN)📊 Tests + coverage...$(NC)"
	$(MAKE) test-cov-docker

# Rapport HTML coverage (après make test-cov ou make test-cov-docker) : ouvrir htmlcov/index.html
coverage-report: test-cov
	@echo "$(GREEN)Rapport HTML : htmlcov/index.html$(NC)"

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
	@PYTHONPATH=".:apps" python3 manage.py check --deploy 2>/dev/null || PYTHONPATH=".:apps" python manage.py check --deploy 2>/dev/null || echo "  (Django check --deploy : exécuter manuellement si erreur)"

validate:
	@echo "=== Django check ===" && (PYTHONPATH=".:apps" python3 manage.py check || PYTHONPATH=".:apps" python manage.py check)
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
	@curl -s -o /dev/null -w "Web: %{http_code}\n" http://localhost:8010/ 2>/dev/null || echo "web: non accessible"

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
	$(DOCKER) exec db pg_dump -U $(DB_USER) $(DB_NAME) > backups/backup_$$(date +%Y%m%d_%H%M%S).sql
	@echo "$(GREEN)✅ Sauvegarde créée dans backups/$(NC)"

restore:
	@echo "$(YELLOW)📥 Restauration — Lister les sauvegardes :$(NC)"
	@ls -la backups/ 2>/dev/null || echo "Aucune sauvegarde. Usage : $(DOCKER) exec -i db psql -U $(DB_USER) $(DB_NAME) < backups/backup_XXX.sql"

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
	@echo "db et redis démarrés. .env : DB_HOST=localhost, DB_PORT=5433, REDIS_URL=redis://127.0.0.1:6380/0"
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

# runserver — Lance Django en local sur le port 8010 (SquidResearch garde le 8000)
# WSL/Linux : après make venv-install, make runserver fonctionne sans activer le venv à la main
runserver:
	@if [ -f .venv/bin/python ]; then PYTHONPATH=".:apps" .venv/bin/python manage.py runserver 8010; elif [ -f .venv/Scripts/python.exe ]; then PYTHONPATH=".:apps" .venv/Scripts/python.exe manage.py runserver 8010; else PYTHONPATH=".:apps" python3 manage.py runserver 8010 2>/dev/null || PYTHONPATH=".:apps" python manage.py runserver 8010; fi

# =============================================================================
# Utilitaires
# =============================================================================

secret-key:
	@python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())" 2>/dev/null || python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

clean:
	@python3 -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if p.is_dir()]" 2>/dev/null || python -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if p.is_dir()]" 2>/dev/null || true
	@python3 -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc') if p.is_file()]" 2>/dev/null || python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc') if p.is_file()]" 2>/dev/null || true
	@python3 -Bc "import pathlib, shutil; p=pathlib.Path('.pytest_cache'); shutil.rmtree(p) if p.exists() else None" 2>/dev/null || python -Bc "import pathlib, shutil; p=pathlib.Path('.pytest_cache'); shutil.rmtree(p) if p.exists() else None" 2>/dev/null || true
	@echo "Nettoyage terminé."

# =============================================================================
# Git — commit et push sur les deux remotes (origin + gitlab)
# =============================================================================
# À lancer depuis WSL ou Git Bash (git dans le PATH).
# Exemple : make commit-push MSG="docs: DevOps + Architecte réseau, procédure fin de landing"
# Ou : git add . && git commit -m "ton message" && make push-both

.PHONY: push-both commit-push push-standalone-p4s

# deploy-contabo — orchestration du déploiement LPPP sur Contabo (rsync + SSH + docker)
# Prérequis : clé ~/.ssh/contabo_key. Réf. segmentations/2026-02-07-sprint-deploiement-contabo-lppp.md
deploy-contabo:
	@echo "$(CYAN)Orchestration déploiement LPPP sur Contabo...$(NC)"
	@bash scripts/deploy-contabo.sh
	@echo "$(GREEN)✅ Déploiement terminé. Vérifier http://173.249.4.106:8010/$(NC)"

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

# push-standalone-p4s — clone LPPP_P4S-Architecture, copie deploy/standalone-p4s, commit, push GitHub + GitLab.
# WSL/Git Bash. Vercel (lppp-p4-s-architecture) build au push. Autres landings : deploy/README-standalone.md.
push-standalone-p4s:
	@echo "$(CYAN)Push landing P4S standalone...$(NC)"
	@rm -rf deploy/repo-p4s
	@git clone git@github.com:LucasTymen/LPPP_P4S-Architecture.git deploy/repo-p4s
	@cp -r deploy/standalone-p4s/. deploy/repo-p4s/
	@cp deploy/standalone-p4s/.gitignore deploy/repo-p4s/ 2>/dev/null || true
	@(cd deploy/repo-p4s && git add . && git status && git commit -m "Landing P4S standalone — page unique, pas de hub" && git push -u origin main)
	@(cd deploy/repo-p4s && (git remote get-url gitlab 2>/dev/null && git push gitlab main || (git remote add gitlab git@gitlab.com:LucasTymen/lppp_p4s-architecture.git && git push -u gitlab main)))
	@echo "$(GREEN)Push OK. Vercel (lppp-p4-s-architecture) va builder.$(NC)"
