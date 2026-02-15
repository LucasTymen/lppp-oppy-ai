#!/usr/bin/env bash
# Orchestration du déploiement LPPP sur Contabo
# À lancer depuis WSL, à la racine du projet : bash scripts/deploy-contabo.sh
# Prérequis : clé SSH ~/.ssh/contabo_key présente. Aucun secret dans ce script.
# Réf. : segmentations/2026-02-07-sprint-deploiement-contabo-lppp.md

set -e

SSH_KEY="${HOME}/.ssh/contabo_key"
SSH_HOST="root@173.249.4.106"
LP_PATH="/var/www/lppp"
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "=== Orchestration déploiement LPPP sur Contabo ==="
echo ""

# 1. Vérifier la clé SSH
if [ ! -f "$SSH_KEY" ]; then
  echo "ERREUR: Clé SSH non trouvée: $SSH_KEY"
  echo "Récupérer la clé depuis ton coffre/backup ou la recréer, puis réessayer."
  exit 1
fi
echo "✓ Clé SSH trouvée"

# 2. Rsync du projet vers le serveur (exclut .env, venv, cache, etc.)
echo ""
echo "→ Envoi du projet vers $SSH_HOST:$LP_PATH ..."
rsync -avz --delete \
  --exclude='.env' \
  --exclude='.env.local' \
  --exclude='.env.production' \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.venv' \
  --exclude='.venv.wsl' \
  --exclude='venv' \
  --exclude='staticfiles' \
  --exclude='media' \
  --exclude='celerybeat-schedule' \
  --exclude='node_modules' \
  --exclude='.cursor' \
  --exclude='htmlcov' \
  --exclude='.pytest_cache' \
  -e "ssh -i $SSH_KEY -o StrictHostKeyChecking=accept-new" \
  "$PROJECT_ROOT/" "$SSH_HOST:$LP_PATH/"
echo "✓ Projet envoyé"

# 3. Sur le serveur : .env, build, up, migrate
echo ""
echo "→ Sur le serveur : préparation .env, build, up, migrate ..."
ssh -i "$SSH_KEY" "$SSH_HOST" bash -s << 'REMOTE'
set -e
cd /var/www/lppp

# .env : copier depuis .env.example si absent
if [ ! -f .env ]; then
  cp .env.example .env
  echo "ATTENTION: .env créé depuis .env.example. TU DOIS L'ÉDITER sur le serveur avant de relancer."
  echo "  - SECRET_KEY (générer une clé forte)"
  echo "  - DB_PASSWORD"
  echo "  - DEBUG=False"
  echo "  - ALLOWED_HOSTS=173.249.4.106,ton-domaine.com,..."
  echo "  - FLOWISE_URL, FLOWISE_CHATFLOW_ID si chatbot"
  echo ""
  echo "  ssh -i ~/.ssh/contabo_key root@173.249.4.106"
  echo "  cd /var/www/lppp && nano .env"
  echo ""
  echo "Puis relancer: bash scripts/deploy-contabo.sh"
  exit 1
fi

docker compose build
docker compose up -d

echo "Attente démarrage services (20s)..."
sleep 20

docker compose exec -T web python manage.py migrate --no-input

echo ""
echo "✓ Build, up, migrate OK"
echo ""
echo "Première fois ? Créer un superuser:"
echo "  ssh -i ~/.ssh/contabo_key root@173.249.4.106"
echo "  cd /var/www/lppp && docker compose exec web python manage.py createsuperuser"
echo ""
echo "Vérifier: curl -s -o /dev/null -w '%{http_code}' http://173.249.4.106:8010/"
REMOTE

echo ""
echo "=== Déploiement terminé ==="
echo ""
echo "Vérifier: curl -s -o /dev/null -w '%{http_code}' http://173.249.4.106:8010/"
echo "Admin: http://173.249.4.106:8010/admin/"
echo "Essais: http://173.249.4.106:8010/essais/"
echo ""
