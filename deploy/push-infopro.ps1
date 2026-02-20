# Push Infopro — copie le contenu dans le repo lppp-infopro et push
# Usage : depuis la racine LPPP, .\deploy\push-infopro.ps1
# Prérequis : export déjà fait (python manage.py export_landing_static infopro ...)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

Write-Host "Export Infopro (si pas deja fait)..." -ForegroundColor Cyan
python manage.py export_landing_static infopro --json docs/contacts/infopro/landing-proposition-infopro.json --output deploy/static-infopro-vercel/index.html --rapport-md docs/contacts/infopro/rapport-complet-infopro.md

Write-Host "Clone + copie vers deploy/repo-infopro..." -ForegroundColor Cyan
Remove-Item -Recurse -Force deploy/repo-infopro -ErrorAction SilentlyContinue
git clone https://github.com/LucasTymen/lppp-infopro.git deploy/repo-infopro
Copy-Item deploy/static-infopro-vercel/* deploy/repo-infopro/ -Recurse -Force

Set-Location deploy/repo-infopro
git add .
git status
git commit -m "Landing Infopro Digital — page statique (export Django)"
git push -u origin main
git remote add gitlab https://gitlab.com/LucasTymen/lppp_infopro.git -ErrorAction SilentlyContinue
git push -u gitlab main
Set-Location $root
Write-Host "Push termine. Vercel deploie automatiquement." -ForegroundColor Green
