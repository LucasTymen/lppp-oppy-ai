#!/bin/bash
# Push Infopro — copie le contenu dans lppp-infopro et push (WSL/bash)
# Usage : ./deploy/push-infopro.sh  (depuis la racine LPPP)
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== 1. Export Infopro ==="
python3 manage.py export_landing_static infopro \
  --json docs/contacts/infopro/landing-proposition-infopro.json \
  --output deploy/static-infopro-vercel/index.html \
  --rapport-md docs/contacts/infopro/rapport-complet-infopro.md

echo "=== 2. Clone + copie vers deploy/repo-infopro ==="
rm -rf deploy/repo-infopro
git clone git@github.com:LucasTymen/lppp-infopro.git deploy/repo-infopro
cp -r deploy/static-infopro-vercel/* deploy/repo-infopro/

echo "=== 3. Commit + push ==="
cd deploy/repo-infopro
git add .
git status
git commit -m "Landing Infopro Digital — page statique (export Django)"
git push -u origin main
git remote add gitlab git@gitlab.com:LucasTymen/lppp_infopro.git 2>/dev/null || true
git push -u gitlab main

cd "$ROOT"
echo "=== OK. Vercel deploie automatiquement. ==="
