# Push landing Promovacances — LPPP_promovacances

**Repos** : GitHub `LucasTymen/LPPP_promovacances`, GitLab `LucasTymen/lppp_promovacances`.  
**Vercel** : projet **lppp-promovacances** (tiret), lié au repo GitHub. Supprimer tout doublon (ex. lppp_promovacances). 1 repo = 1 projet Vercel.  
**Contenu** : page statique (proposition) + infographie + assets. Framework Vercel = **Other**, Build = vide.

## 1. Régénérer la page (après modification)

À la racine du repo LPPP :

```bash
python manage.py export_landing_static promovacances --json docs/contacts/promovacances/landing-proposition-promovacances.json --output deploy/static-promovacances-vercel/index.html
```

Optionnel (lien « Consulter le rapport ») :

```bash
python manage.py export_landing_static promovacances --json docs/contacts/promovacances/landing-proposition-promovacances.json --output deploy/static-promovacances-vercel/index.html --rapport-md docs/contacts/promovacances/README.md
```

## 2. Clone + copie + push (PowerShell)

Depuis la racine LPPP :

```powershell
Remove-Item -Recurse -Force deploy/repo-promovacances -ErrorAction SilentlyContinue
git clone https://github.com/LucasTymen/LPPP_promovacances.git deploy/repo-promovacances
Copy-Item deploy/static-promovacances-vercel/* deploy/repo-promovacances/ -Recurse -Force
cd deploy/repo-promovacances
git add .
git status
git commit -m "Landing Promovacances — page statique (export Django)"
git push -u origin main
git remote add gitlab git@gitlab.com:LucasTymen/lppp_promovacances.git
git push -u gitlab main
```

## 3. Vercel

Projet **lppp-promovacances** lié au repo **LPPP_promovacances** (GitHub). Framework **Other**, Build Command = vide, Root Directory = `./`.  
En cas de doublon (lppp_promovacances, etc.) : Settings → Delete Project pour ne garder qu’un seul projet.
