# Push la landing P4S standalone vers LPPP_P4S-Architecture (GitHub + GitLab).
# Usage : depuis la racine du repo LPPP : .\deploy\push-standalone-p4s.ps1
# Prérequis : Git installé (chemin utilisé : C:\Program Files\Git\bin\git.exe ou git dans le PATH).

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
if (-not (Test-Path (Join-Path $ProjectRoot "deploy\standalone-p4s"))) {
    $ProjectRoot = (Get-Location).Path
}
if (-not (Test-Path (Join-Path $ProjectRoot "deploy\standalone-p4s"))) {
    throw "Impossible de trouver deploy\standalone-p4s. Exécutez le script depuis la racine du repo LPPP."
}
$RepoDir = Join-Path $ProjectRoot "deploy\repo-p4s"
$GitExe = "C:\Program Files\Git\bin\git.exe"
if (-not (Test-Path $GitExe)) { $GitExe = "git" }

Set-Location $ProjectRoot
Write-Host "=== Copie du contenu standalone-p4s vers le repo ===" -ForegroundColor Cyan
if (Test-Path $RepoDir) { Remove-Item -Recurse -Force $RepoDir }
& $GitExe clone "https://github.com/LucasTymen/LPPP_P4S-Architecture.git" $RepoDir
Copy-Item -Path (Join-Path $ProjectRoot "deploy\standalone-p4s\*") -Destination $RepoDir -Recurse -Force
Copy-Item (Join-Path $ProjectRoot "deploy\standalone-p4s\.gitignore") $RepoDir -Force
Set-Location $RepoDir
& $GitExe add .
& $GitExe status
& $GitExe commit -m "Landing P4S standalone — version complète clone Django (proposition.html)"
Write-Host ""
Write-Host "=== Étape manuelle : push (authentification requise) ===" -ForegroundColor Yellow
Write-Host "Depuis ce dossier : $RepoDir" -ForegroundColor White
Write-Host "1. git push -u origin main   (GitHub : PAT ou SSH selon votre config)" -ForegroundColor White
Write-Host "2. git remote add gitlab git@gitlab.com:LucasTymen/lppp_p4s-architecture.git   (si pas déjà fait)" -ForegroundColor White
Write-Host "3. git push -u gitlab main   (GitLab)" -ForegroundColor White
Write-Host ""
Write-Host "Vercel (lppp-p4-s-architecture) rebuildera après le push." -ForegroundColor Green
