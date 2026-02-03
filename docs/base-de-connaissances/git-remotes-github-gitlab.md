# Git — Initialisation et remotes (GitHub + GitLab)

**Pilote** : **DevOps** (règle `.cursor/rules/devops.mdc`).  
**Rôle** : Configuration Git LPPP avec deux remotes ; **GitHub pilote** (principal), **GitLab** en miroir.  
**Référence** : `docs/base-de-connaissances/infra-devops.md` (secrets, flux).

**Règle (important, tout le temps)** : **Penser à installer/vérifier Git** (WSL ou Git Bash) en clôture de feature ou livraison, puis **commit + push sur les deux remotes** (origin + gitlab). Voir Makefile `push-both` / `commit-push`, template de segmentation § Règle Git.

> **À exécuter sur ta machine** : les commandes ci-dessous doivent être lancées dans un terminal où **Git est installé** (WSL, Git Bash, ou PowerShell avec Git dans le PATH).  
> **Premier commit et push** : réalisés le 2025-01-30 (commit 67a2055, 125 fichiers ; push origin main et push gitlab main OK).

---

## Clés et stratégie SSH : réutiliser SquidResearch

**Stratégie** : réutiliser les **clés SSH et la stratégie déjà en place pour SquidResearch** (même machine, même `~/.ssh`, même agent SSH). On gagne du temps : pas de nouvelle config, pas de nouveaux tokens HTTPS.

- **Même environnement** : lancer Git depuis WSL/Linux (ou le même terminal où SquidResearch push/pull fonctionne).
- **Mêmes clés** : les clés déjà utilisées pour GitHub et GitLab (SquidResearch) servent pour LPPP — ajouter les URLs des dépôts LPPP aux remotes en **SSH**.
- **Aucune clé dans le dépôt** : les clés restent dans `~/.ssh` et ne sont jamais committées (cf. `infra-devops.md`).

---

## URLs LPPP (configurées) — en SSH (recommandé, aligné SquidResearch)

- **GitHub (origin)** : `git@github.com:LucasTymen/landingPageCreatorForProspection.git`
- **GitLab (gitlab)** : `git@gitlab.com:LucasTymen/landingpagecreatorforprospection.git`

**HTTPS** (fallback si SSH non utilisé) :  
- GitHub : `https://github.com/LucasTymen/landingPageCreatorForProspection.git`  
- GitLab : `https://gitlab.com/LucasTymen/landingpagecreatorforprospection.git`

**Note** : GitLab a été créé **vide** (sans README par défaut) pour éviter tout conflit au premier push.

---

## Checklist rapide (à faire maintenant) — SSH (clés SquidResearch)

**À la racine du projet LPPP** (même environnement que SquidResearch, WSL/Linux ou terminal où l’agent SSH est chargé) :

```bash
git init
git branch -M main
git remote add origin git@github.com:LucasTymen/landingPageCreatorForProspection.git
git remote add gitlab git@gitlab.com:LucasTymen/landingpagecreatorforprospection.git
git add .
git status
git commit -m "Initial commit — LPPP (landings, landingsgenerator, docs)"
git push -u origin main
git push -u gitlab main
```

Vérifier avant le commit qu’**aucun fichier sensible** n’est ajouté (`.env`, `secrets/`, etc.) — le `.gitignore` doit les exclure. En cas d’erreur sur GitLab (conflit), s’assurer que le dépôt GitLab est bien vide (sans README créé par défaut).

**Commit + push sur les deux remotes (à lancer depuis WSL ou Git Bash)** :
```bash
git add .
git status
git commit -m "docs: DevOps + Architecte réseau, procédure fin de landing, fiche P4S"
make push-both
```
Ou en une commande : `make commit-push MSG="docs: description du commit"`.

---

## 1. Stratégie

- **GitHub** = remote **principal** (pilotage) : `origin`. Push/pull par défaut, CI (GitHub Actions), déploiement lié si besoin.
- **GitLab** = remote **secondaire** (miroir) : `gitlab`. Push en miroir pour backup ou CI GitLab.
- Contrairement à SquidResearch (où GitLab pilotait), **c’est GitHub qui pilote** pour LPPP.

---

## 2. Initialisation Git (si pas encore fait)

À la **racine du projet LPPP** (où se trouve `docker-compose.yml`, `.gitignore`) :

```bash
git init
git branch -M main
```

Vérifier que `.gitignore` est bien là (ne pas committer `.env`, `staticfiles/`, `media/`, etc.).

---

## 3. Ajouter les remotes (SSH recommandé — clés SquidResearch)

**LPPP utilise les mêmes clés SSH que SquidResearch** (voir section « Clés et stratégie SSH » en tête de doc).

**GitHub = origin (pilote)** :

```bash
git remote add origin git@github.com:LucasTymen/landingPageCreatorForProspection.git
```

**GitLab = secondaire** :

```bash
git remote add gitlab git@gitlab.com:LucasTymen/landingpagecreatorforprospection.git
```

**Fallback HTTPS** (si SSH non configuré pour LPPP) : remplacer par les URLs `https://github.com/...` et `https://gitlab.com/...` (voir section URLs LPPP ci-dessus).

Vérifier :

```bash
git remote -v
# origin   https://github.com/... (fetch)
# origin   https://github.com/... (push)
# gitlab   https://gitlab.com/... (fetch)
# gitlab   https://gitlab.com/... (push)
```

---

## 4. Premier commit et push

```bash
git add .
git status   # vérifier qu'aucun .env ni fichier sensible n'est ajouté
git commit -m "Initial commit — LPPP (landings, landingsgenerator, docs)"
git push -u origin main
```

Puis pousser aussi vers GitLab (miroir) :

```bash
git push -u gitlab main
```

---

## 5. Usage courant

- **Push principal** : `git push origin main` (GitHub pilote).
- **Miroir GitLab** : `git push gitlab main` (après chaque push origin, ou configurer un push vers les deux remotes).
- **Push vers les deux d’un coup** (optionnel) :

```bash
git remote set-url --add --push origin git@github.com:LucasTymen/landingPageCreatorForProspection.git
git remote set-url --add --push origin git@gitlab.com:LucasTymen/landingpagecreatorforprospection.git
```

Après ça, `git push origin main` enverra vers GitHub puis GitLab. Sinon, deux commandes : `git push origin main` puis `git push gitlab main`.

---

## 6. Création des dépôts côté plateforme

- **GitHub** : New repository → nom du repo (ex. `LPPP` ou `landings-pages-prospection`) → ne pas initialiser avec README si le projet existe déjà localement.
- **GitLab** : New project → Create blank project → même remarque.

Ne pas committer de secrets : `.env` doit rester ignoré (déjà dans `.gitignore`).

---

*Document créé par le Conseiller. Dernière mise à jour : 2025-01-30.*
