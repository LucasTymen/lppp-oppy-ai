# Push landing ORSYS vers LPPP_orsys

**Repos cibles :** GitHub `LucasTymen/LPPP_orsys` · GitLab `LucasTymen/lppp_orsys`

---

## 1. Générer la page statique

À la **racine du repo LPPP** :

```bash
python manage.py export_landing_static orsys --json docs/contacts/orsys/landing-proposition-aboubakar.json --output deploy/static-orsys-vercel/index.html --rapport-md docs/contacts/orsys/rapport-complet-orsys.md
```

- `--rapport-md` : génère `rapport.html` et définit le lien « Consulter le rapport » vers cette page. Sans ça, `/p/orsys/rapport/` renvoie 404 sur Vercel.
- Windows : `python` au lieu de `python3` si besoin.

---

## 2. Pousser vers GitHub

### Option A — Repo déjà créé sur GitHub (avec ou sans README)

Si tu as déjà fait « Create repository » sur GitHub (éventuellement avec le README proposé) :

```bash
# À la racine du repo LPPP
rm -rf deploy/repo-orsys
git clone https://github.com/LucasTymen/LPPP_orsys.git deploy/repo-orsys
cp deploy/static-orsys-vercel/index.html deploy/static-orsys-vercel/rapport.html deploy/repo-orsys/
cp deploy/static-orsys-vercel/vercel.json deploy/repo-orsys/
cp deploy/static-orsys-vercel/README.md deploy/repo-orsys/
cd deploy/repo-orsys
git add .
git commit -m "Landing ORSYS — page statique (hero vidéo CDN, thème #FDFEFE, overlay, scanlines)"
git push -u origin main
```

**PowerShell :**
```powershell
Remove-Item -Recurse -Force deploy/repo-orsys -ErrorAction SilentlyContinue
git clone https://github.com/LucasTymen/LPPP_orsys.git deploy/repo-orsys
Copy-Item deploy/static-orsys-vercel/index.html, deploy/static-orsys-vercel/rapport.html deploy/repo-orsys/
Copy-Item deploy/static-orsys-vercel/vercel.json deploy/repo-orsys/
Copy-Item deploy/static-orsys-vercel/README.md deploy/repo-orsys/
cd deploy/repo-orsys
git add .
git commit -m "Landing ORSYS — page statique (hero vidéo CDN, thème #FDFEFE, overlay, scanlines)"
git push -u origin main
```

### Option B — Premier push (repo vide, comme sur la page GitHub « Quick setup »)

Si tu viens de créer le repo **sans** cocher « Add a README » :

```bash
cd deploy/static-orsys-vercel
git init
git add .
git commit -m "Landing ORSYS — page statique (hero vidéo CDN, thème #FDFEFE)"
git branch -M main
git remote add origin https://github.com/LucasTymen/LPPP_orsys.git
git push -u origin main
```

Si le repo a été créé **avec** le README par GitHub, utilise l’**Option A** (clone puis copie des fichiers) pour ne pas écraser l’historique.

---

## 2b. Pousser vers GitLab (repo vide)

Si le repo **GitLab** est vide (`gitlab.com/LucasTymen/lppp_orsys`) :

```bash
cd deploy/static-orsys-vercel
git init --initial-branch=main
git remote add origin git@gitlab.com:LucasTymen/lppp_orsys.git
git add .
git commit -m "Landing ORSYS — page statique (hero vidéo CDN, thème #FDFEFE, overlay, scanlines)"
git push --set-upstream origin main
```

**PowerShell** (même dossier) :
```powershell
git init -b main
git remote add origin git@gitlab.com:LucasTymen/lppp_orsys.git
git add .
git commit -m "Landing ORSYS — page statique (hero vidéo CDN, thème #FDFEFE, overlay, scanlines)"
git push -u origin main
```

---

## 3. Vercel

Lier le projet Vercel au repo **LPPP_orsys**.  
Framework = **Other**, Build Command = vide, Output Directory = `.`.
