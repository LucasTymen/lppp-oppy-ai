# Push landing Oppy-AI vers Vercel

**Deux stratégies possibles :**

| Stratégie | Repo | Config Vercel |
|-----------|------|---------------|
| **A — Repo dédié** | `LPPP_OppyAI` (GitHub) — à créer si absent | Root Directory = `./` |
| **B — Monorepo** | `lppp-oppy-ai` (existant) | Root Directory = `deploy/static-oppy-ai-vercel` |

**Note :** Si `LPPP_OppyAI` n’existe pas, utiliser la **stratégie B** (repo lppp-oppy-ai + Root Directory).

---

## 1. Générer la page statique

À la **racine du repo LPPP** :

```bash
python3 manage.py export_landing_static lppp-oppy-ai --json docs/contacts/lppp-oppy-ai/landing-proposition-lppp-oppy-ai.json --output deploy/static-oppy-ai-vercel/index.html
```

- **Rapport :** sans `--rapport-md`, si un Markdown de rapport est présent dans `docs/contacts/lppp-oppy-ai/` (même règles que Django : `rapport-teaser*`, `rapport-complet*`, `rapport-*`, ou tout `rapport*.md` ex. `rapport seo complet.md`), la commande génère **`rapport.html`** et le lien « Consulter le rapport complet » — aligné avec `http://localhost:8010/p/lppp-oppy-ai/rapport/`.
- **Optionnel :** `--rapport-md "chemin/vers/fichier.md"` force un fichier précis (prioritaire sur la détection auto).
- **Vercel :** le `vercel.json` à la racine du monorepo inclut des **rewrites** `/rapport` et `/rapport/` → `rapport.html` ; pour un déploiement depuis **seul** `deploy/static-oppy-ai-vercel`, copier aussi ce `vercel.json` dans ce dossier (ou équivalent) avant push.
- Windows : `python` au lieu de `python3` si besoin.

---

## 2. Créer les repos (si pas déjà faits)

- **GitHub** : New repository → nom = `LPPP_OppyAI` → **ne pas** initialiser avec README.
- **GitLab** : New project → Create blank project → nom = `lppp_oppy_ai` → **ne pas** initialiser avec README.

---

## 3. Pousser vers GitHub

### Option A — Repo déjà créé sur GitHub (avec ou sans README)

```bash
# À la racine du repo LPPP
rm -rf deploy/repo-oppy-ai
git clone https://github.com/LucasTymen/LPPP_OppyAI.git deploy/repo-oppy-ai
cp deploy/static-oppy-ai-vercel/index.html deploy/static-oppy-ai-vercel/rapport.html deploy/repo-oppy-ai/
cp deploy/static-oppy-ai-vercel/vercel.json deploy/repo-oppy-ai/
cp deploy/static-oppy-ai-vercel/README.md deploy/repo-oppy-ai/
cd deploy/repo-oppy-ai
git add .
git commit -m "Landing Oppy-AI — page statique (thème Oppy cyan, hero CodePen Waves Pins, rapport SEO)"
git push -u origin main
```

**PowerShell :**
```powershell
Remove-Item -Recurse -Force deploy/repo-oppy-ai -ErrorAction SilentlyContinue
git clone https://github.com/LucasTymen/LPPP_OppyAI.git deploy/repo-oppy-ai
Copy-Item deploy/static-oppy-ai-vercel/index.html, deploy/static-oppy-ai-vercel/rapport.html deploy/repo-oppy-ai/
Copy-Item deploy/static-oppy-ai-vercel/vercel.json, deploy/static-oppy-ai-vercel/README.md deploy/repo-oppy-ai/
cd deploy/repo-oppy-ai
git add .
git commit -m "Landing Oppy-AI — page statique (thème Oppy cyan, hero CodePen Waves Pins)"
git push -u origin main
```

### Option B — Premier push (repo vide)

Si tu viens de créer le repo **sans** cocher « Add a README » :

```bash
cd deploy/static-oppy-ai-vercel
git init
git add .
git commit -m "Landing Oppy-AI — page statique (thème Oppy cyan, hero CodePen Waves Pins)"
git branch -M main
git remote add origin https://github.com/LucasTymen/LPPP_OppyAI.git
git push -u origin main
```

---

## 4. Pousser vers GitLab

```bash
cd deploy/repo-oppy-ai   # ou deploy/static-oppy-ai-vercel si Option B
git remote add gitlab git@gitlab.com:LucasTymen/lppp_oppy_ai.git
git push -u gitlab main
```

(Si le remote `gitlab` existe déjà : `git push gitlab main`.)

---

## 5. Vercel

### Cas repo lppp-oppy-ai (monorepo) — build échoue avec Next.js

Configurer **Root Directory** dans Vercel :
1. Projet lppp-oppy-ai → **Settings** → **General**
2. **Root Directory** : `deploy/static-oppy-ai-vercel`
3. **Framework Preset** : **Other**
4. **Build Command** : vide
5. **Redeploy**

Voir `deploy/static-oppy-ai-vercel/VERCEL-CONFIG.md`.

### Cas repo LPPP_OppyAI (static only)

1. Aller sur [vercel.com/new](https://vercel.com/new)
2. **Import Git Repository** → choisir le repo **LPPP_OppyAI** (GitHub)
3. **Root Directory** : laisser vide ou `./`
4. **Framework Preset** : **Other**
5. **Build Command** : vide (Override)
6. **Output Directory** : `.`
7. **Deploy**

Après le déploiement : ouvrir l’URL (ex. `https://lppp-oppy-ai.vercel.app` ou nom du projet) — la landing doit s’afficher avec le hero CodePen Waves Pins, le thème Oppy cyan, et le lien « Consulter le rapport » vers rapport.html.

---

## Récap

| Étape | Action |
|-------|--------|
| 1 | Exporter : `python manage.py export_landing_static lppp-oppy-ai --json ... --output ... --rapport-md ...` |
| 2 | Créer repos GitHub `LPPP_OppyAI` + GitLab `lppp_oppy_ai` (sans README) |
| 3 | Clone + copie index.html, rapport.html, vercel.json, README → commit + push origin |
| 4 | Push gitlab main |
| 5 | Vercel : importer LPPP_OppyAI, Framework=Other, Build=vide, Output=. |

Réf. : `strategie-deploiement-git-vercel.md`, `procedure-fin-landing-repo-deploiement.md`.
