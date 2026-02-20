# Sprint : URLs incohérentes + duplication projet Vercel (Promovacances)

**Date** : 2026-01-30  
**Statut** : 🟡 À traiter  
**Pilotes** : **DevOps**, **Architecte réseau**  
**Référence** : `procedure-fin-landing-repo-deploiement.md`, `strategie-deploiement-git-vercel.md`

---

## 1. Problèmes signalés

| # | Problème | Impact |
|---|----------|--------|
| 1 | **URLs incohérentes** | Mélange Django (`/p/promovacances/...`) et statique (`rapport.html`) ; liens cassés ou redondants |
| 2 | **Duplication projet Vercel** | Plusieurs projets Vercel pointent vers le même repo GitHub `LPPP_promovacances` |

---

## 2. Audit URLs (Promovacances statique Vercel)

### 2.1 Contexte

- **Django (local)** : URLs `/p/promovacances/`, `/p/promovacances/rapport/`, `/p/promovacances/audit-dashboard/`
- **Vercel (statique)** : racine = `/` ; fichiers = `index.html`, `rapport.html`, `infographie-promovacances-7-formats.html`, `positionnement-marketing.html`
- **vercel.json** : rewrites `/p/promovacances/rapport` et `/p/promovacances/rapport/` → `/rapport.html`

### 2.2 Liens internes actuels (deploy/static-promovacances-vercel)

| Page | Liens utilisés |
|------|----------------|
| index.html | `rapport.html`, `positionnement-marketing.html`, `rapport.html#analyse-seo-complete` |
| rapport.html | `index.html`, `rapport.html`, `infographie-promovacances-7-formats.html`, `positionnement-marketing.html` |
| infographie | `index.html`, `rapport.html`, `infographie-promovacances-7-formats.html`, `positionnement-marketing.html` |
| positionnement-marketing | `index.html`, `rapport.html`, `infographie-promovacances-7-formats.html`, `positionnement-marketing.html` |

**Problème identifié** : le texte de index.html mentionne `/p/promovacances/audit-dashboard/` — URL Django qui **n’existe pas** sur Vercel (pas de dashboard embarqué en statique). Les liens cliquables pointent correctement vers `rapport.html`.

### 2.3 Règle de cohérence (statique Vercel)

- **Utiliser uniquement** des chemins relatifs : `index.html`, `rapport.html`, `infographie-promovacances-7-formats.html`, `positionnement-marketing.html`
- **Ne pas utiliser** `/p/promovacances/...` dans les liens (sauf si rewrites vercel.json)
- Les rewrites `/p/promovacances/rapport/` → `/rapport.html` servent aux liens **externes** (ex. lien partagé) ; les liens internes restent en `rapport.html`

---

## 3. Duplication projet Vercel

### 3.1 Diagnostic

Sur [vercel.com](https://vercel.com) → Projects, vérifier :

- Combien de projets ont **LPPP_promovacances** (ou variante) dans le nom
- Quel projet a le repo `LucasTymen/LPPP_promovacances` lié
- Quelles URLs chacun expose (ex. `xxx.vercel.app`)

### 3.2 Solution

| Étape | Action |
|-------|--------|
| 1 | Lister tous les projets Vercel liés au repo `LPPP_promovacances` |
| 2 | Choisir **un seul** projet à conserver (le plus récent ou celui avec la bonne config) |
| 3 | Noter l’URL du projet conservé |
| 4 | **Supprimer** les projets dupliqués : Settings → General → Delete Project |
| 5 | Documenter l’URL finale dans `docs/contacts/promovacances/README.md` |

### 3.3 Config attendue (1 projet = 1 repo)

- **1 repo GitHub** : `LucasTymen/LPPP_promovacances`
- **1 projet Vercel** : lié à ce repo
- **Root Directory** : `./` (contenu à la racine du repo)
- **Framework** : Other
- **Build Command** : vide
- **Output Directory** : `.` ou vide

---

## 4. Actions à réaliser

- [ ] **DevOps** : audit Vercel — lister les projets liés à LPPP_promovacances, identifier les doublons
- [ ] **DevOps** : supprimer les projets dupliqués, garder un seul
- [ ] **DevOps / Dev Django** : corriger la mention `/p/promovacances/audit-dashboard/` dans index.html (texte descriptif) — remplacer par `rapport.html#analyse-seo-complete` ou formulation neutre
- [ ] **DevOps** : documenter l’URL Vercel finale et la config dans la fiche contact
- [ ] Mettre à jour `erreurs-et-solutions.md` avec une entrée « Duplication projet Vercel »

---

## 5. Références

- `deploy/PUSH-PROMOVACANCES.md`
- `docs/contacts/promovacances/README.md`
- `docs/base-de-connaissances/erreurs-et-solutions.md`
- `docs/base-de-connaissances/strategie-deploiement-git-vercel.md`
