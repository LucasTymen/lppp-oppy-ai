#!/usr/bin/env bash
# Push la landing ACKURACY standalone vers LPPP_Ackuracy (GitHub + GitLab).
# Usage : depuis la racine du repo LPPP : bash deploy/push-standalone-ackuracy.sh
# Prérequis : git, accès SSH aux remotes (WSL ou Git Bash).
# La version déployée = celle dans deploy/standalone-ackuracy/ (celle qu'on travaille en local / localhost).

set -e
REPO_DIR="deploy/repo-ackuracy"
GITHUB_URL="git@github.com:LucasTymen/LPPP_Ackuracy.git"
GITLAB_URL="git@gitlab.com:LucasTymen/lppp_ackuracy.git"

cd "$(dirname "$0")/.."
echo "=== Copie du contenu standalone-ackuracy (version locale) vers le repo ==="
rm -rf "$REPO_DIR"
git clone "$GITHUB_URL" "$REPO_DIR"
cp -r deploy/standalone-ackuracy/. "$REPO_DIR/"
cd "$REPO_DIR"
git add .
git status
git commit -m "Landing ACKURACY standalone — contenu JSON, hero image/parallax/scanlines"
git push -u origin main
if git remote get-url gitlab 2>/dev/null; then
  git push gitlab main
else
  git remote add gitlab "$GITLAB_URL" 2>/dev/null || true
  git push -u gitlab main
fi
echo "=== Push OK. Vercel va builder la version locale. ==="
