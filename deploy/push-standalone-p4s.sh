#!/usr/bin/env bash
# Push la landing P4S standalone vers LPPP_P4S-Architecture (GitHub + GitLab).
# Usage : depuis la racine du repo LPPP : bash deploy/push-standalone-p4s.sh
# Prérequis : git, accès SSH aux remotes (WSL ou Git Bash).

set -e
REPO_DIR="deploy/repo-p4s"
GITHUB_URL="git@github.com:LucasTymen/LPPP_P4S-Architecture.git"
GITLAB_URL="git@gitlab.com:LucasTymen/lppp_p4s-architecture.git"

cd "$(dirname "$0")/.."
echo "=== Copie du contenu standalone-p4s vers le repo ==="
rm -rf "$REPO_DIR"
git clone "$GITHUB_URL" "$REPO_DIR"
cp -r deploy/standalone-p4s/. "$REPO_DIR/"
cd "$REPO_DIR"
git add .
git status
git commit -m "Landing P4S standalone — contenu depuis JSON (version locale)"
git push -u origin main
if git remote get-url gitlab 2>/dev/null; then
  git push gitlab main
else
  git remote add gitlab "$GITLAB_URL" 2>/dev/null || true
  git push -u gitlab main
fi
echo "=== Push OK. Vercel (lppp-p4-s-architecture) va builder. ==="
