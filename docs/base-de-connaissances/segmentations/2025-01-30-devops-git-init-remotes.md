# DevOps — Initialisation Git et remotes (GitHub + GitLab)

**Date** : 2025-01-30  
**Pilote** : **DevOps** (règle `.cursor/rules/devops.mdc`)  
**Statut** : 🟢 **Terminé** — Git init, remotes SSH (origin + gitlab), premier commit 67a2055 (125 fichiers), push origin main et push gitlab main réussis. (signalé par l’utilisateur)

---

## Objectif

Initialiser le dépôt Git LPPP et configurer les deux remotes : **GitHub** (pilote = `origin`), **GitLab** (miroir = `gitlab`). Tâche du ressort DevOps uniquement.

**Doc de référence** : `docs/base-de-connaissances/git-remotes-github-gitlab.md`

---

## Tâches DevOps à exécuter

### 1. Vérifier l’état du dépôt

- [ ] Vérifier si `.git` existe à la racine du projet. Si non → initialiser.
- [ ] Vérifier que `.gitignore` est présent et couvre secrets, `.env`, `staticfiles/`, `media/`, etc.

### 2. Initialiser Git (si pas déjà fait)

À la **racine du projet** (où se trouvent `docker-compose.yml`, `.gitignore`) :

```bash
git init
git branch -M main
```

### 3. Ajouter les remotes

**GitHub = origin (pilote)** — SSH (clés SquidResearch) :

```bash
git remote add origin git@github.com:LucasTymen/landingPageCreatorForProspection.git
```

**GitLab = secondaire** — SSH (clés SquidResearch) :

```bash
git remote add gitlab git@gitlab.com:LucasTymen/landingpagecreatorforprospection.git
```

**Note** : Réutiliser les clés et la stratégie SSH de SquidResearch (même `~/.ssh`, même agent). GitLab doit être un dépôt **vide** (sans README par défaut) pour éviter les conflits au premier push.

**URLs LPPP — SSH (réutiliser clés et stratégie SquidResearch)** :
- **origin** : `git@github.com:LucasTymen/landingPageCreatorForProspection.git`
- **gitlab** : `git@gitlab.com:LucasTymen/landingpagecreatorforprospection.git`

- [ ] Vérifier : `git remote -v` (origin → GitHub, gitlab → GitLab).

### 4. Premier commit et push

- [ ] `git add .` puis `git status` (vérifier qu’aucun fichier sensible n’est ajouté).
- [ ] `git commit -m "Initial commit — LPPP (landings, landingsgenerator, docs)"`
- [ ] `git push -u origin main`
- [ ] `git push -u gitlab main`

### 5. Documenter

- [ ] Mettre à jour ce fichier : statut → 🟢 Terminé quand c’est fait.
- [ ] Mettre à jour `docs/TODO.md` : tâche Git → Fait.

---

## Note d’exécution

Les commandes Git doivent être lancées dans un terminal où **Git est installé** (PowerShell, CMD, Git Bash sur la machine de l’utilisateur). Si l’agent ne peut pas exécuter `git` dans son environnement, DevOps fournit à l’utilisateur la checklist et les commandes exactes à lancer (voir `git-remotes-github-gitlab.md`).

---

## Références

- **Procédure complète** : `docs/base-de-connaissances/git-remotes-github-gitlab.md`
- **Infra** : `docs/base-de-connaissances/infra-devops.md`
- **Règle DevOps** : `.cursor/rules/devops.mdc`

---

*Tâche assignée au DevOps. Dernière mise à jour : 2025-01-30.*
