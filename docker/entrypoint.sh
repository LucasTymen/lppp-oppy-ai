#!/bin/bash
set -e

# Attendre PostgreSQL si DB_HOST présent
if [ -n "${DB_HOST}" ]; then
  echo "Waiting for PostgreSQL at ${DB_HOST}..."
  while ! python -c "import socket; s=socket.socket(); s.settimeout(2); s.connect(('${DB_HOST}', ${DB_PORT:-5432})); s.close()" 2>/dev/null; do
    sleep 1
  done
  echo "PostgreSQL is up."
fi

# Migrations (pour le service web)
if [ "$1" = "gunicorn" ]; then
  python manage.py migrate --noinput
  python manage.py collectstatic --noinput --clear 2>/dev/null || true
fi

exec "$@"
