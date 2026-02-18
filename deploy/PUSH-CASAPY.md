# Push LPPP-Casapy vers GitHub et GitLab

** Prérequis** : créer les repos **LPPP-Casapy** sur GitHub et GitLab (sans README).

---

## Commandes (WSL / Git Bash)

```bash
cd deploy/LPPP-Casapy

# Config identité locale (optionnel)
git config --local user.name "Lucas Tymen"
git config --local user.email "lucas.tymen@gmail.com"

# Init + commit initial
git init --initial-branch=main
git add .
git commit -m "Initial commit — landing Casapy audit SEO et proposition de valeur"

# GitHub (origin)
git remote add origin https://github.com/LucasTymen/LPPP-Casapy.git
git push -u origin main

# GitLab (second remote)
git remote add gitlab https://gitlab.com/LucasTymen/LPPP-Casapy.git
git push -u gitlab main
```

---

## Vercel

Après le push : lier le repo LPPP-Casapy à Vercel. Root Directory = `.` (racine du repo). Framework = Other (page statique).
