#!/bin/bash
# Push landing Oppy-AI vers LPPP_OppyAI (Vercel)
# Usage : bash deploy/push-oppy-ai.sh
# Prérequis : export déjà fait (index.html, rapport.html dans deploy/static-oppy-ai-vercel)
# Si LPPP_OppyAI n'existe pas : créer le repo sur GitHub (sans README) puis relancer.

set -e
REPO_DIR="deploy/repo-oppy-ai"
GITHUB_URL="https://github.com/LucasTymen/LPPP_OppyAI.git"
GITLAB_URL="git@gitlab.com:LucasTymen/lppp_oppy_ai.git"

cd "$(dirname "$0")/.."

echo "=== 1. Export landing (si pas déjà fait) ==="
# Détection auto du Markdown rapport (docs/contacts/lppp-oppy-ai/rapport*.md) — même logique que Django /p/.../rapport/
python3 manage.py export_landing_static lppp-oppy-ai \
  --json docs/contacts/lppp-oppy-ai/landing-proposition-lppp-oppy-ai.json \
  --output deploy/static-oppy-ai-vercel/index.html

echo "=== 2. Clone ou mise à jour repo LPPP_OppyAI ==="
rm -rf "$REPO_DIR"
if git ls-remote "$GITHUB_URL" &>/dev/null; then
  git clone "$GITHUB_URL" "$REPO_DIR"
else
  echo "ERREUR: Repo LPPP_OppyAI introuvable. Créer sur GitHub : https://github.com/new?name=LPPP_OppyAI (sans README)"
  exit 1
fi

echo "=== 3. Copie des fichiers ==="
cp deploy/static-oppy-ai-vercel/index.html "$REPO_DIR/"
if [ -f deploy/static-oppy-ai-vercel/rapport.html ]; then
  cp deploy/static-oppy-ai-vercel/rapport.html "$REPO_DIR/"
fi
cp vercel.json "$REPO_DIR/" 2>/dev/null || cp deploy/static-oppy-ai-vercel/vercel.json "$REPO_DIR/" 2>/dev/null || true
cp deploy/static-oppy-ai-vercel/README.md "$REPO_DIR/" 2>/dev/null || true
cp deploy/static-oppy-ai-vercel/package.json "$REPO_DIR/" 2>/dev/null || true

echo "=== 4. Commit et push ==="
cd "$REPO_DIR"
git add .
git status
echo "---"
echo "Exécution du commit (contourner erreur 'trailer requires a value' : utiliser terminal externe si échec)"
if git commit -m "Landing Oppy-AI — page statique (thème Oppy, hero Waves Pins, rapport SEO)" 2>/dev/null; then
  git push -u origin main
  if git remote get-url gitlab 2>/dev/null; then
    git push gitlab main
  else
    git remote add gitlab "$GITLAB_URL" 2>/dev/null || true
    git push -u gitlab main 2>/dev/null || echo "Push GitLab : à faire manuellement (git push gitlab main)"
  fi
  echo "=== DÉPLOIEMENT TERMINÉ ==="
  echo "Vercel va redéployer automatiquement. Vérifier : https://vercel.com/dashboard"
else
  echo "COMMIT ÉCHOUÉ (erreur trailer ?). À faire manuellement depuis un terminal externe (Git Bash, PowerShell) :"
  echo "  cd $REPO_DIR"
  echo "  git add . && git commit -m 'Landing Oppy-AI' && git push origin main"
fi
