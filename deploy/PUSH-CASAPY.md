# Push LPPP-Casapy vers GitHub et GitLab

**Prérequis** : créer les repos **LPPP-Casapy** sur GitHub et GitLab (sans README).

---

## 1. Régénérer l’export statique (après modif JSON/template)

```bash
# À la racine du repo LPPP
python manage.py export_landing_static casapy --json docs/contacts/casapy/landing-proposition-casapy.json --output deploy/LPPP-Casapy/index.html --rapport-md docs/contacts/casapy/rapport-complet-casapy.md
```

---

## 2. Commandes Git — LPPP (projet principal)

```bash
cd c:\home\lucas\tools\homelucastoolsLandingsPagesPourProspections
git add templates/landing_pages/proposition.html docs/contacts/casapy/landing-proposition-casapy.json deploy/LPPP-Casapy/
git commit -m "Casapy: mise à jour landing"
git push origin main
git push gitlab main
```

---

## 3. Commandes Git — LPPP-Casapy (repo standalone pour Vercel)

**Remotes configurés** : origin = `LPPP_casapy` (GitHub), gitlab = `LPPP-Casapy` (GitLab).

### Premier push (init) — si le repo est vide

```bash
cd deploy/LPPP-Casapy

git config --local user.name "Lucas Tymen"
git config --local user.email "lucas.tymen@gmail.com"

git init --initial-branch=main
git add .
git commit -m "Landing Casapy — audit SEO et proposition de valeur"

git remote add origin https://github.com/LucasTymen/LPPP_casapy.git
git push -u origin main

git remote add gitlab https://gitlab.com/LucasTymen/LPPP-Casapy.git
git push -u gitlab main
```

### Mise à jour (après export) — cas normal

```bash
cd deploy/LPPP-Casapy
git add .
git status   # vérifier : index.html, PNG, rapport.html
git commit -m "feat: 7 slides + wave + spec consultant-grade"
git pull origin main --rebase   # intégrer les commits distants si présents
git push origin main
git push gitlab main
```

### Push refusé : « Updates were rejected (remote contains work) »

Si le remote a des commits que tu n'as pas en local (ex. README créé sur GitHub) :

```bash
cd deploy/LPPP-Casapy
git add .
git commit -m "feat: mise à jour landing Casapy"
git pull origin main --rebase
# En cas de conflits : résoudre, puis git rebase --continue
git push origin main
git push gitlab main
```

(Utilise HTTPS si SSH échoue avec « Host key verification failed ». Voir `ssh-host-key-verification-github-gitlab.md`.)

---

## 4. Vercel

Après le push : lier le repo LPPP-Casapy à Vercel. Root Directory = `.`, Framework = **Other** (page statique), Build Command = vide.

**Si « No Production Deployment »** : vérifier que le push sur `main` a bien été effectué ; que le repo GitHub est bien `LucasTymen/LPPP-Casapy` (tiret, pas underscore) ; que la config Vercel pointe vers la bonne branche. À traiter par Architecte / DevOps.
