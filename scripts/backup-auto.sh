#!/usr/bin/env bash
# Sauvegarde automatique PostgreSQL LPPP — à appeler par cron ou Planificateur de tâches.
# Usage : depuis la racine du projet : ./scripts/backup-auto.sh
#         ou via cron : cd /chemin/vers/projet && make backup && make backup-clean

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

# Charger .env si présent (pour make)
if [ -f .env ]; then
  set -a
  source .env 2>/dev/null || true
  set +a
fi

make backup
make backup-clean
