#!/usr/bin/env bash
# Commit et push sur origin + gitlab (à lancer depuis WSL ou Git Bash)
# Usage : depuis la racine du projet : bash scripts/commit-push-avancement.sh

set -e
cd "$(dirname "$0")/.."

echo "=== Ajout des fichiers ==="
git add -A
git reset -- deploy/yuwell-portfolio 2>/dev/null || true
git reset -- deploy/static-orsys-vercel 2>/dev/null || true

echo "=== Statut ==="
git status -s | head -20
echo "..."

echo "=== Commit ==="
if [ -f .git_commit_msg.txt ]; then
  git commit -F .git_commit_msg.txt
else
  git commit -m "Avancement projet: FitClem, InfographicCraft, sprint page complete, registre et segmentations"
fi

echo "=== Push origin main ==="
git push origin main
echo "=== Push gitlab main ==="
git push gitlab main
echo "=== Terminé ==="
