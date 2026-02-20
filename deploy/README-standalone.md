# Landings standalone — rapide et précis

**Objectif** : une landing = un repo au nom de la société + un projet Vercel dédié. Pas de hub. Réutilisable pour ~15 autres landings.

**Stratégie fluide (Git + Vercel, sans erreur)** : voir **`docs/base-de-connaissances/strategie-deploiement-git-vercel.md`** — checklist unique à suivre pour chaque projet (1, 2, … 10+). En cas de galère (404, push oublié, conflit repo), consulter **`docs/base-de-connaissances/erreurs-et-solutions.md`**.

---

## Important : la version locale = le modèle à publier sur Vercel

**La version travaillée en local est celle qui doit servir sur Vercel.**

| Landing | Contenu déployé | Repos cibles |
|---------|-----------------|--------------|
| **P4S** | **Page statique** (un seul `index.html` généré par Django) — voir `deploy/static-p4s-vercel/` et `PUSH-POUR-VERSION-COMPLETE.md` | GitHub LPPP_P4S-Architecture + GitLab lppp_p4s_architecture |
| **ACKURACY** | App Next.js (`deploy/standalone-ackuracy/`) — `bash deploy/push-standalone-ackuracy.sh` | GitHub LPPP_Ackuracy + GitLab lppp_ackuracy |
| **Yuwell (portfolio)** | **Site statique** (5 pages HTML + `static/`) — `deploy/yuwell-portfolio/`, génération : `python manage.py export_yuwell_static --output deploy/yuwell-portfolio`. Vercel : Framework = **Other**, Build = vide. Voir `PUSH-YUWELL.md`. | GitHub LPPP_yuwell_portfolio + GitLab lppp_yuwell_portfolio |

**Sans WSL/Git Bash (PowerShell)** — deux options :

**Option A — Script (clone + copie + commit, puis push à la main)**  
Depuis la racine du projet : `.\deploy\push-standalone-p4s.ps1`  
Le script affiche les commandes à exécuter pour le **push** (authentification GitHub/GitLab requise).

**Option B — P4S (page statique, pas Next.js)** : voir **`deploy/PUSH-POUR-VERSION-COMPLETE.md`**. En bref : `python manage.py export_landing_static p4s-archi --output deploy/static-p4s-vercel/index.html`, copier `deploy/static-p4s-vercel/*` dans `deploy/repo-p4s/`, puis commit + push. Sur Vercel : Framework = **Other**, Build Command = vide.

**ACKURACY** :
```powershell
Remove-Item -Recurse -Force deploy/repo-ackuracy -ErrorAction SilentlyContinue
git clone https://github.com/LucasTymen/LPPP_Ackuracy.git deploy/repo-ackuracy
Copy-Item deploy/standalone-ackuracy/* deploy/repo-ackuracy/ -Recurse -Force
Copy-Item deploy/standalone-ackuracy/.gitignore deploy/repo-ackuracy/ -Force
cd deploy/repo-ackuracy
git add .
git commit -m "Landing ACKURACY standalone — contenu JSON, hero image/parallax/scanlines"
git push -u origin main
git remote add gitlab git@gitlab.com:LucasTymen/lppp_ackuracy.git
git push -u gitlab main
```

Après le push, Vercel rebuild automatiquement. Vérifier l’URL du projet (ex. lppp-p4-s-architecture.vercel.app, lppp-ackuracy.vercel.app).

---

## P4S : page statique (la landing, pas une app)

- **Repo** : [LPPP_P4S-Architecture](https://github.com/LucasTymen/LPPP_P4S-Architecture).
- **Contenu déployé** : **un seul fichier HTML** (`index.html`) = la page rendue par Django sur `/p/p4s-archi/`. Génération : `python manage.py export_landing_static p4s-archi --output deploy/static-p4s-vercel/index.html`. Puis copier `deploy/static-p4s-vercel/*` dans le repo et push. Vercel : Framework = **Other**, Build Command = vide.
- **Procédure détaillée** : `deploy/PUSH-POUR-VERSION-COMPLETE.md`.

---

## Yuwell : portfolio (site statique 5 pages)

- **Repo** : [LPPP_yuwell_portfolio](https://github.com/LucasTymen/LPPP_yuwell_portfolio) (GitHub) · [lppp_yuwell_portfolio](https://gitlab.com/LucasTymen/lppp_yuwell_portfolio) (GitLab).
- **Contenu déployé** : **5 pages HTML** (index.html = Présentation, study-case.html, study-case-2.html, charte-graphique.html, a-propos.html) + dossier `static/` (fonts Oswald, images). Génération : `python manage.py export_yuwell_static --output deploy/yuwell-portfolio`. Le dossier `deploy/yuwell-portfolio/` est poussé tel quel sur les deux remotes (ou copié dans un clone du repo). **Vercel** : importer le repo GitHub LPPP_yuwell_portfolio → Framework = **Other**, Build Command = vide, Output Directory = `.`. Voir `deploy/PUSH-YUWELL.md` et `deploy/yuwell-portfolio/vercel.json`.

---

## Pour les prochaines landings (réutilisable)

### 1. Préparer le contenu et la page

- **Template recommandé** (landings « proposition » avec contenu riche + hero image/parallax/scanlines) : **`deploy/standalone-ackuracy/`** — contenu depuis JSON, hero avec image de fond + parallax + scanlines **actifs par défaut**. Voir **`docs/base-de-connaissances/generation-landing-nextjs-contenu-hero.md`**.
- **Copier** `deploy/standalone-ackuracy/` (ou `standalone-p4s/` si page simple sans hero image) vers un dossier dédié (ex. `deploy/standalone-<slug>/`).
- **Contenu** : copier le JSON du contact `docs/contacts/<slug>/landing-proposition-*.json` vers `src/content/landing.json` dans le standalone. La page doit afficher toutes les sections (hero, pain points, services, about_me, mission_flash, etc.).
- **Hero** : image de fond (champ `hero_background_url` du JSON ou image par défaut), parallax et scanlines déjà en place dans le template ACKURACY — ne pas les désactiver.
- **Adapter** `src/app/layout.tsx` (title, description) et `package.json` (name: `lppp-<slug>`) pour la société.

### 2. Créer le repo (GitHub + GitLab)

- **Nom** : au nom de la société (ex. `LPPP_NomSociete`), **sans README**.
- GitHub : `LucasTymen/LPPP_NomSociete`
- GitLab : `LucasTymen/lppp_nomsociete`

### 3. Push (WSL ou Git Bash)

```bash
cd /chemin/vers/LPPP   # racine du repo LPPP
rm -rf deploy/repo-<slug>
git clone git@github.com:LucasTymen/LPPP_NomSociete.git deploy/repo-<slug>
cp -r deploy/standalone-<slug>/. deploy/repo-<slug>/
cd deploy/repo-<slug>
git add .
git commit -m "Landing <NomSociete> standalone — page unique, pas de hub"
git push -u origin main
git remote add gitlab git@gitlab.com:LucasTymen/lppp_nomsociete.git
git push -u gitlab main
```

### 4. Vercel

- Créer ou lier le projet Vercel au repo **LPPP_NomSociete** (Root Directory = `./` car l’app est à la racine du repo standalone).

---

## Submodules : landings = projets à part entière

**Décision** : chaque landing déployée en standalone est un **projet à part entière** (repo dédié). Dans LPPP, on la référence via un **submodule Git** (ex. `deploy/static-0flow-vercel`, `deploy/static-orsys-vercel`) pour figer une version sans dupliquer l’historique. Réf. `docs/base-de-connaissances/decisions.md` (2026-02-05).

**Après avoir créé le repo et poussé la landing** : ajouter le submodule dans LPPP (une seule fois) :

```bash
# Depuis la racine LPPP
git submodule add git@github.com:LucasTymen/LPPP_NomSociete.git deploy/static-<slug>-vercel
git add .gitmodules deploy/static-<slug>-vercel
git commit -m "chore: ajout submodule landing <slug>"
git push origin main && git push gitlab main
```

**Clone frais de LPPP** (récupérer aussi le contenu des submodules) :

```bash
git clone --recurse-submodules <url_lppp>   # ou après clone :
git submodule update --init --recursive
```

**Mettre à jour la référence** (après modif dans le repo de la landing) : aller dans le dossier du submodule, pull, puis dans LPPP commit la nouvelle référence (hash).

---

## Récap

| Étape | Action | Qui |
|-------|--------|-----|
| 1 | Copier `standalone-ackuracy` (ou p4s), copier JSON contact → `src/content/landing.json`, hero image/parallax/scanlines par défaut | Dev Django / Rédacteur / Designer |
| 2 | Créer repo GitHub + GitLab (sans README) | Chef de Projet ou DevOps |
| 3 | Clone + copier + commit + push (commandes ci-dessus) | DevOps / Architecte réseau |
| 4 | Lier Vercel au repo, vérifier déploiement | DevOps |

Réf. : **`strategie-deploiement-git-vercel.md`** (checklist fluide), **`generation-landing-nextjs-contenu-hero.md`** (contenu + hero par défaut), `procedure-fin-landing-repo-deploiement.md`, `docs/contacts/p4s-archi/README.md`, `erreurs-et-solutions.md` (pièges Git/Vercel).
