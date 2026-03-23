#!/bin/bash
# Upload des fichiers Oppy-AI vers LPPP_OppyAI via GitHub API (contourne git commit)
# Usage : à la racine LPPP : bash deploy/upload-oppy-api.sh
set -e
cd "$(dirname "$0")/.."
python3 manage.py export_landing_static lppp-oppy-ai \
  --json docs/contacts/lppp-oppy-ai/landing-proposition-lppp-oppy-ai.json \
  --output deploy/static-oppy-ai-vercel/index.html \
  --rapport-md "docs/contacts/lppp-oppy-ai/rapport seo complet.md"
cd deploy/static-oppy-ai-vercel
REPO="LucasTymen/LPPP_OppyAI"
for f in README.md vercel.json index.html rapport.html; do
  echo "Upload $f..."
  gh api -X PUT "repos/$REPO/contents/$f" -f message="Update $f" -f content="$(base64 -w0 $f)" >/dev/null
done
echo "OK. https://github.com/$REPO"
