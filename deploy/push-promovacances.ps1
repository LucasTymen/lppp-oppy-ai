# Push landing Promovacances vers GitHub + GitLab
# Usage : depuis la racine LPPP, .\deploy\push-promovacances.ps1
# Prérequis : export déjà fait (python manage.py export_landing_static promovacances ...)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $root

Write-Host "Export Promovacances (si pas déjà fait)..." -ForegroundColor Cyan
python manage.py export_landing_static promovacances --json docs/contacts/promovacances/landing-proposition-promovacances.json --output deploy/static-promovacances-vercel/index.html

Write-Host "Clone + copie vers deploy/repo-promovacances..." -ForegroundColor Cyan
Remove-Item -Recurse -Force deploy/repo-promovacances -ErrorAction SilentlyContinue
git clone https://github.com/LucasTymen/LPPP_promovacances.git deploy/repo-promovacances
Copy-Item deploy/static-promovacances-vercel/* deploy/repo-promovacances/ -Recurse -Force

Set-Location deploy/repo-promovacances
git add .
git status
git commit -m "Landing Promovacances — page statique (export Django)"
git push -u origin main
git remote add gitlab git@gitlab.com:LucasTymen/lppp_promovacances.git -ErrorAction SilentlyContinue
git push -u gitlab main
Set-Location $root
Write-Host "Push termine." -ForegroundColor Green
