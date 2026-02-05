#!/usr/bin/env bash
# Option B : runserver (contournement port Docker sous Windows/WSL)
# À lancer depuis WSL, à la racine du projet : bash scripts/runserver-wsl.sh [port]
# Port par défaut : 8080. Si occupé : bash scripts/runserver-wsl.sh 8082
set -e
cd "$(dirname "$0")/.."
PORT="${1:-8080}"
export DB_HOST=localhost
export REDIS_URL=redis://127.0.0.1:6379/0
export CELERY_BROKER_URL=redis://127.0.0.1:6379/1
export CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/2
export PYTHONPATH=.:apps

if [ ! -d .venv.wsl ]; then
  echo "Création .venv.wsl et installation des deps (2–3 min)..."
  python3 -m venv .venv.wsl
  .venv.wsl/bin/pip install -q -r requirements.txt
fi

echo "Démarrage runserver http://127.0.0.1:${PORT}/"
echo "Admin : http://127.0.0.1:${PORT}/admin/"
.venv.wsl/bin/python manage.py runserver 127.0.0.1:${PORT}
