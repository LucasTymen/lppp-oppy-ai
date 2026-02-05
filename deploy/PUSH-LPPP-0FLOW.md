# Pousser la landing 0Flow vers LPPP_0flow (GitHub, GitLab, Vercel)

Tu as créé **GitHub** (LPPP_0flow), **GitLab** et **Vercel** pour ce repo. Procédure pour le premier push et les suivants.

**Prérequis** : export à jour dans `deploy/static-0flow-vercel/` (index.html, rapport.html, hero-0flow.png, vercel.json). Voir ci-dessous § 1.

---

## 1. Régénérer l’export (depuis la racine du repo LPPP, en WSL)

```bash
cd /mnt/c/home/lucas/tools/homelucastoolsLandingsPagesPourProspections

# Export landing + rapport
python3 manage.py export_landing_static 0flow --output deploy/static-0flow-vercel/index.html --rapport-md docs/contacts/0flow/rapport-complet-0flow.md

# Copier l’image hero (pour que le HTML la trouve en relatif)
cp apps/landing_pages/static/landing_pages/images/hero-0flow.png deploy/static-0flow-vercel/

# Remplacer le chemin absolu par un chemin relatif dans index.html
sed -i "s|/static/landing_pages/images/hero-0flow.png|hero-0flow.png|g" deploy/static-0flow-vercel/index.html
```

---

## 2. Premier push vers LPPP_0flow (dossier existant → GitHub + GitLab)

Les deux repos sont vides. Depuis la **racine du repo LPPP** (WSL) :

```bash
cd /mnt/c/home/lucas/tools/homelucastoolsLandingsPagesPourProspections/deploy/static-0flow-vercel

# Identité locale (optionnel, pour ce repo uniquement)
git config --local user.name "Lucas Tymen"
git config --local user.email "lucas.tymen@gmail.com"

# Init + deux remotes
git init --initial-branch=main
git remote add origin git@github.com:LucasTymen/LPPP_0flow.git
git remote add gitlab git@gitlab.com:LucasTymen/LPPP_0flow.git

git add .
git status   # index.html, rapport.html, hero-0flow.png, vercel.json, README.md
git commit -m "Landing 0Flow — page statique (export Django) + rapport SEO"
git push -u origin main
git push -u gitlab main
```

**Alternative (clone GitHub puis copie)** : si tu préfères garder le repo LPPP séparé du dossier exporté, clone d’abord GitHub dans `deploy/repo-0flow`, copie les 4 fichiers + vercel.json dedans, puis commit et push origin + gitlab (voir § 4 pour les pushes suivants).

---

## 3. Vercel

- **Import** : [vercel.com/new](https://vercel.com/new) → Import Git Repository → **LPPP_0flow** (GitHub).
- **Root Directory** : laisser vide ou `./`.
- **Framework Preset** : Other. **Build Command** : vide (Override). Pas de build.
- **Deploy** → une fois le build « Ready », ouvrir l’URL (ex. `https://lppp-0flow.vercel.app`).

---

## 4. Pushes suivants

Régénérer l’export (§ 1) depuis la racine LPPP, puis depuis le dossier du repo 0flow :

```bash
# 1. Racine LPPP : régénérer l’export (écrit dans deploy/static-0flow-vercel/)
cd /mnt/c/home/lucas/tools/homelucastoolsLandingsPagesPourProspections
# ... commandes § 1 ...

# 2. Aller dans le repo 0flow (si tu as fait git init dans static-0flow-vercel)
cd deploy/static-0flow-vercel
git add .
git commit -m "Landing 0Flow — mise à jour export"
git push origin main
git push gitlab main
```

(Si tu as utilisé un clone dans `deploy/repo-0flow`, remplace par `cd deploy/repo-0flow`, copie les fichiers depuis `../static-0flow-vercel/`, puis commit et push.)

---

## 5. Où noter les infos

- **URL de prod** : dans `docs/contacts/0flow/README.md` (section Repo / Déploiement).
- **Décisions** : `docs/base-de-connaissances/decisions.md` (ex. « Landing 0Flow : repo LPPP_0flow, Vercel lppp-0flow »).
