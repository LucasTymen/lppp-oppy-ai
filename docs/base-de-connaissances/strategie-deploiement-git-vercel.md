# Stratégie fluide : Git (GitHub + GitLab) + Vercel — 1 projet = 1 repo + 1 déploiement

**Objectif** : Une seule procédure claire, sans erreur, réutilisable pour **chaque landing** (1, 2, … 10+ projets).  
**Pilote** : DevOps / Architecte réseau (voir `procedure-fin-landing-repo-deploiement.md`).  
**Références** : `git-remotes-github-gitlab.md`, `deploiement-vercel-frontend.md`, `erreurs-et-solutions.md`.

---

## Principe

| Élément | Règle |
|--------|--------|
| **1 landing** | 1 repo au nom de la société (ex. `LPPP_P4S-Architecture`) |
| **Git** | 2 remotes : **GitHub** (`origin`) + **GitLab** (`gitlab`) — **push sur les deux à chaque fois** |
| **Vercel** | 1 projet Vercel par repo ; Root Directory = `./` si app à la racine du repo (standalone) |
| **Ordre** | Créer repos → préparer code → clone → copier → commit → **push origin** → **push gitlab** → lier Vercel → vérifier page |

---

## Checklist par projet (à suivre dans l’ordre)

Cocher au fur et à mesure. Même ordre pour le projet 1, 2, … 10+.

### Avant de commencer

- [ ] **Slug** du projet (ex. `p4s-archi`, `nom-societe`) et **nom de société** pour le repo (ex. `LPPP_P4S-Architecture`).
- [ ] **Terminal** : WSL ou Git Bash (Git + SSH configurés, clés SquidResearch si utilisées). Voir `git-remotes-github-gitlab.md`.

### 1. Créer les repos (GitHub + GitLab)

- [ ] **GitHub** : New repository → nom = `LPPP_<NomSociete>` (ex. `LPPP_P4S-Architecture`) → **ne pas** initialiser avec README.
- [ ] **GitLab** : New project → Create blank project → nom = `lppp_<nomsociete>` (ex. `lppp_p4s_architecture`) → **ne pas** initialiser avec README.
- [ ] Noter les URLs SSH :
  - GitHub : `git@github.com:LucasTymen/LPPP_<NomSociete>.git`
  - GitLab : `git@gitlab.com:LucasTymen/lppp_<nomsociete>.git`

### 2. Préparer le code (dans LPPP)

- [ ] Code de la landing dans un dossier dédié (ex. `deploy/standalone-<slug>/` ou `deploy/standalone-p4s/` à copier puis adapter).
- [ ] App Next.js **à la racine** du dossier (pas de sous-dossier `frontend/`) pour que le repo standalone ait Root Directory = `./` sur Vercel.

### 3. Clone + copie + commit (depuis la racine du repo LPPP)

Depuis la **racine du repo LPPP** (où se trouve `deploy/`), en remplaçant `<slug>`, `<NomSociete>`, `<nomsociete>` et les URLs :

```bash
REPO_DIR="deploy/repo-<slug>"
GITHUB_URL="git@github.com:LucasTymen/LPPP_<NomSociete>.git"
GITLAB_URL="git@gitlab.com:LucasTymen/lppp_<nomsociete>.git"

rm -rf "$REPO_DIR"
git clone "$GITHUB_URL" "$REPO_DIR"
cp -r deploy/standalone-<slug>/. "$REPO_DIR/"
cd "$REPO_DIR"
git add .
git status   # vérifier : pas de .env ni fichier sensible
git commit -m "Landing <NomSociete> standalone — page unique, pas de hub"
git push -u origin main
git remote add gitlab "$GITLAB_URL"
git push -u gitlab main
cd ../..
```

- [ ] **Push origin** exécuté sans erreur.
- [ ] **Push gitlab** exécuté sans erreur (miroir à jour).

### 4. Vercel

- [ ] **Vercel** → [vercel.com/new](https://vercel.com/new) → Import Git Repository → choisir le repo **LPPP_<NomSociete>** (GitHub).
- [ ] **Root Directory** : laisser vide ou `./` (app à la racine du repo). **Ne pas** mettre `frontend` sauf si le repo contient un sous-dossier `frontend/`.
- [ ] **Deploy** → attendre build **Ready**.
- [ ] **Vérifier la page** : ouvrir l’URL (ex. `https://lppp-<slug>.vercel.app`) — pas de 404, contenu correct.

### 5. Après déploiement

- [ ] **URL** enregistrée dans la fiche contact (ex. `docs/contacts/<slug>/README.md`).
- [ ] **Nom du repo** et **projet Vercel** documentés (fiche contact ou `decisions.md`).

---

## Pièges à éviter (voir aussi `erreurs-et-solutions.md`)

| Piège | Conséquence | Prévention |
|-------|-------------|------------|
| **Push seulement sur GitHub** | GitLab désynchronisé, backup incomplet. | Toujours exécuter `git push gitlab main` après `git push origin main`. |
| **Root Directory Vercel incorrect** | Build depuis la mauvaise racine → 404 ou "NOT_FOUND". | Repo standalone = Root Directory `./` (ou vide). Monorepo avec `frontend/` = Root Directory `frontend`. |
| **Repo créé avec README** | Conflit au premier push (histoires différentes). | Créer les repos **sans** README, **sans** .gitignore initial. |
| **Oublier de vérifier la page** | Déploiement "Ready" mais page cassée ou 404. | Toujours ouvrir l’URL dans le navigateur après le déploiement. |

---

## Réutilisation pour les 10+ projets

1. **Dupliquer le script** : copier `deploy/push-standalone-p4s.sh` vers `deploy/push-standalone-<slug>.sh`, adapter `REPO_DIR`, `GITHUB_URL`, `GITLAB_URL` et le message de commit.
2. **Ou** : garder une seule checklist (ce document) et remplacer à la main les variables `<slug>`, `<NomSociete>`, `<nomsociete>` à chaque nouveau projet.
3. **Fiche contact** : pour chaque prospect, noter dans `docs/contacts/<slug>/README.md` les noms de repo (GitHub + GitLab), l’URL Vercel et le nom du projet Vercel.

---

## Récap des références

- **Git (remotes, SSH)** : `git-remotes-github-gitlab.md`
- **Vercel (config, Root Directory, 404)** : `deploiement-vercel-frontend.md`
- **Fin de landing (qui fait quoi)** : `procedure-fin-landing-repo-deploiement.md`
- **Erreurs connues et solutions** : `erreurs-et-solutions.md`
- **Exemple P4S** : `deploy/README-standalone.md`, `deploy/push-standalone-p4s.sh`, `docs/contacts/p4s-archi/README.md`

---

*Document créé pour une stratégie fluide Git + Vercel réutilisable sans erreur sur 10+ projets. Dernière mise à jour : 2025-02-02.*
