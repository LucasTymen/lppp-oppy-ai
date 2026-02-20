# Push portfolio Yuwell vers GitHub et GitLab

**Repos cibles :**
- **GitHub** : [LucasTymen/LPPP_yuwell_portfolio](https://github.com/LucasTymen/LPPP_yuwell_portfolio)
- **GitLab** : [LucasTymen/lppp_yuwell_portfolio](https://gitlab.com/LucasTymen/lppp_yuwell_portfolio)

---

## 1. Générer le site statique

À la **racine du repo LPPP** :

```bash
python manage.py export_yuwell_static --output deploy/yuwell-portfolio
```

- Génère : `index.html`, `study-case.html`, `study-case-2.html`, `charte-graphique.html`, `a-propos.html` + dossier `static/` (fonts Oswald, images).
- Windows : `python` au lieu de `python3` si besoin.

---

## 2. Premier push (repos vides) — GitHub puis GitLab

Les deux repos sont vides. On initialise le dépôt **dans le dossier export**, on pousse d’abord sur **GitHub**, puis on ajoute GitLab et on pousse.

### 2.1 Identité Git (optionnel, pour ce repo uniquement)

```bash
cd deploy/yuwell-portfolio
git config --local user.name "Lucas Tymen"
git config --local user.email "lucas.tymen@gmail.com"
```

### 2.2 Init, premier commit, push GitHub

```bash
cd deploy/yuwell-portfolio
git init --initial-branch=main
git add .
git commit -m "Portfolio Yuwell — 5 pages statiques (charte, Oswald, hero video)"
git remote add origin https://github.com/LucasTymen/LPPP_yuwell_portfolio.git
git push -u origin main
```

**PowerShell :**
```powershell
cd deploy/yuwell-portfolio
git init -b main
git add .
git commit -m "Portfolio Yuwell - 5 pages statiques (charte, Oswald, hero video)"
git remote add origin https://github.com/LucasTymen/LPPP_yuwell_portfolio.git
git push -u origin main
```

### 2.3 Ajouter GitLab et pousser

```bash
cd deploy/yuwell-portfolio
git remote add gitlab git@gitlab.com:LucasTymen/lppp_yuwell_portfolio.git
git push -u gitlab main
```

**Si tu préfères HTTPS pour GitLab :**
```bash
git remote add gitlab https://gitlab.com/LucasTymen/lppp_yuwell_portfolio.git
git push -u gitlab main
```

---

## 3. Mises à jour suivantes (déjà cloné ou déjà poussé)

Après avoir régénéré l’export :

```bash
# À la racine LPPP
python manage.py export_yuwell_static --output deploy/yuwell-portfolio

cd deploy/yuwell-portfolio
git add .
git commit -m "Mise à jour portfolio Yuwell"
git push origin main
git push gitlab main
```

**Si tu travailles depuis un clone du repo (et non depuis deploy/yuwell-portfolio) :**

1. Cloner une fois : `git clone https://github.com/LucasTymen/LPPP_yuwell_portfolio.git` (ex. dans `deploy/repo-yuwell`).
2. Ajouter le remote GitLab : `git remote add gitlab git@gitlab.com:LucasTymen/lppp_yuwell_portfolio.git`.
3. À chaque mise à jour : régénérer l’export, copier les fichiers dans le clone, commit, push origin, push gitlab.

```bash
# Exemple : copie des fichiers export vers le clone
cp deploy/yuwell-portfolio/index.html deploy/yuwell-portfolio/*.html deploy/repo-yuwell/
cp -r deploy/yuwell-portfolio/static deploy/repo-yuwell/
# ou sous PowerShell :
# Copy-Item deploy/yuwell-portfolio/*.html deploy/repo-yuwell/
# Copy-Item -Recurse deploy/yuwell-portfolio/static deploy/repo-yuwell/
cd deploy/repo-yuwell
git add .
git commit -m "Mise à jour portfolio Yuwell"
git push origin main
git push gitlab main
```

---

## 4. Déploiement Vercel

- **Vercel** : [vercel.com/new](https://vercel.com/new) → Import Git Repository → choisir **LucasTymen/LPPP_yuwell_portfolio** (GitHub).
- **Framework** : **Other** (pas Next.js ni autre framework).
- **Build Command** : laisser vide.
- **Output Directory** : `.` (racine du repo).
- **Root Directory** : laisser vide (contenu à la racine).
- Le fichier `vercel.json` dans le repo est déjà configuré (`framework: null`, `outputDirectory: "."`). Aucun build : Vercel sert les fichiers statiques tels quels.
- Après déploiement : URL type `https://lppp-yuwell-portfolio.vercel.app` (ou domaine personnalisé). Enregistrer l’URL dans la doc (ex. `docs/ressources-utilisateur/etudes/yuwell-portfolio-etude-graphique.md` ou `decisions.md`).

---

## 5. Hébergement (GitHub Pages / GitLab Pages)

- **GitHub Pages** : Settings → Pages → Source = **Deploy from a branch** → branch `main`, folder `/ (root)`.
- **GitLab Pages** : le site sera servi depuis la racine du repo ; URL type `https://lucastymen.gitlab.io/lppp_yuwell_portfolio/`.

Aucun build nécessaire : site 100 % statique (HTML + CSS inlined + `static/`).
