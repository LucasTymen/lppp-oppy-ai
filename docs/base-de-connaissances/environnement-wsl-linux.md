# Environnement Linux Ubuntu — LPPP

**Contexte LPPP (contrairement à SquidResearch)** : on est sur un **environnement Windows avec WSL installé**, et le travail se fait **notamment dans WSL**. PowerShell est possible mais personnellement beaucoup moins prisé.

**Environnement préféré** : **Linux Ubuntu, dernier LTS en cours** (ex. Ubuntu 24.04 LTS), en machine native ou via WSL — préférence explicite de l’utilisateur. Tous les scripts, le Makefile et la documentation privilégient WSL. Les commandes et procédures sont données en **bash / WSL** en premier.

**PowerShell** : documenté en fallback si besoin ; à éviter comme canal principal pour le dev LPPP (l’utilisateur préfère WSL).

**Python sur WSL** : sous WSL (Ubuntu), la commande disponible est **`python3`** et non `python`. Pour les commandes sur l'hôte WSL (migrate, runserver, scripts), utiliser **`python3`**. Ex. : `python3 manage.py runserver 127.0.0.1:8082`, `python3 scripts/set_superuser.py`. (Dans les conteneurs : `docker compose exec web python ...` reste valide.)

---

## 1. Chemins du projet

### LPPP (workspace actuel)

**Répertoire de travail d’origine (référence)** : c’est le scope à utiliser pour travailler. Les commandes, scripts et procédures supposent ce chemin.

| Contexte | Chemin |
|----------|--------|
| **WSL — répertoire de travail historique** | `/mnt/wsl/docker-desktop-/U/0c7104cdaed2e52d3be34327ae75a4c7c5cbac6068ff2537ab8a9a4b4ed6eb83` |
| **Windows (accès WSL)** | `\\wsl.localhost\Ubuntu-22.04\...` (équivalent du chemin ci-dessus) |

Pour se placer à la racine du projet depuis WSL : `cd /mnt/wsl/docker-desktop-/U/0c7104cdaed2e52d3be34327ae75a4c7c5cbac6068ff2537ab8a9a4b4ed6eb83`

### SquidResearch (référence externe)

| Contexte | Chemin |
|----------|--------|
| **WSL / Linux** | `/home/lucas/tools/squidResearch` |
| **Windows (accès WSL)** | `\\wsl.localhost\Ubuntu-22.04\home\lucas\tools\squidResearch` |
| **Depuis $HOME** | `~/tools/squidResearch` |

### Structure des outils

```
/home/lucas/tools/
├── homelucastoolsLandingsPagesPourProspections/   ← LPPP (ce projet)
├── squidResearch/                                 ← Référence externe
└── squidCommunication/                            ← Autre projet
```

### Git et SSH (LPPP — réutiliser SquidResearch)

LPPP **réutilise les clés et la stratégie SSH de SquidResearch** : même `~/.ssh`, même agent. Depuis WSL/Linux (ou le terminal où SquidResearch push/pull fonctionne), utiliser les remotes en **SSH** :

- **origin** : `git@github.com:LucasTymen/landingPageCreatorForProspection.git`
- **gitlab** : `git@gitlab.com:LucasTymen/landingpagecreatorforprospection.git`

**Référence** : `docs/base-de-connaissances/git-remotes-github-gitlab.md`

---

## 2. Prérequis (Ubuntu LTS)

- **Ubuntu** : dernier LTS en cours (ex. **24.04 LTS**). Sous Windows : WSL 2 avec distribution Ubuntu
- **Docker** : Docker Engine dans WSL ou Docker Desktop avec intégration WSL
- **Make** : `sudo apt install build-essential`
- **Python 3.12** : pour tests locaux et venv (Django dans Docker utilise l’image Python)
- **Git** : `sudo apt install git`

### Vérifier l’environnement

```bash
# WSL
wsl --version

# Make
make --version

# Docker
docker --version
docker compose version

# Python (optionnel, pour tests locaux)
python3 --version
```

---

## 3. Démarrage rapide (WSL / Linux)

### Option A — Docker complet (recommandé)

```bash
cd ~/tools/homelucastoolsLandingsPagesPourProspections

cp .env.example .env
# Éditer .env : SECRET_KEY, DB_PASSWORD, etc.

make go   # Démarrage à froid complet (stratégie SquidResearch)
# OU
make build && make up
make migrate
make createsuperuser

# Ouvrir http://localhost:8010/admin/  (Django LPPP = lppp_web sur 8010)
make services-urls   # Afficher toutes les URLs
```

### Option B — Dev local (db + redis dans Docker, Django en local)

```bash
make dev
make venv-install   # Crée .venv + installe toutes les deps (dont django-environ)
make runserver      # Utilise automatiquement .venv/bin/python si présent
# Ouvrir http://127.0.0.1:8000/admin/ (runserver) ou 8010 en Docker
# Migrations / superuser : make migrate (dans Docker) ou .venv/bin/python manage.py migrate
```

---

## 4. Commandes Make (toutes compatibles Linux/WSL)

Le Makefile est conçu pour bash/sh (Linux, Mac, WSL). Toutes les commandes fonctionnent sans adaptation :

| Commande | Usage |
|----------|-------|
| `make go` | Démarrage à froid complet |
| `make relance` | Redémarrer sans rebuild |
| `make up` | Lancer le stack |
| `make down` | Arrêter le stack |
| `make migrate` | Appliquer les migrations |
| `make backup` | Sauvegarder la base |
| `make services-urls` | Afficher les URLs |
| `make help` | Liste complète |

**Référence** : `docs/base-de-connaissances/strategie-operationnelle-make.md`

---

## 5. Venv (Linux / WSL)

```bash
# Créer
python3 -m venv .venv

# Activer (Linux / WSL / Mac)
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Désactiver
deactivate
```

---

## 6. Erreurs connues et solutions

### ModuleNotFoundError: No module named 'environ' (WSL / Linux sans Docker)

En WSL ou Linux, si tu lances `python3 manage.py runserver` (ou `make runserver`) **sans avoir installé les dépendances**, Django plante au chargement de `lppp/settings.py` (qui utilise `django-environ`).

**Solution** : à la racine du projet :

```bash
make venv-install   # Crée .venv + pip install -r requirements.txt
make runserver      # Lance Django (utilise .venv automatiquement)
```

**Référence détaillée** : `docs/base-de-connaissances/pret-a-demarrer.md` § 5.1.

### Terminal : WSL (bash) en premier, pas PowerShell

Pour LPPP, l’utilisateur travaille **dans WSL** ; **PowerShell est possible mais beaucoup moins prisé**. Les agents et la doc doivent **privilégier les commandes bash / WSL** (make, docker, curl, etc.) et ne proposer PowerShell qu’en secours si vraiment nécessaire.

### ERR_EMPTY_RESPONSE (problème Windows natif)

Sous **Windows natif** (hors WSL), Docker peut provoquer ERR_EMPTY_RESPONSE sur localhost. **Solution** : utiliser **WSL** pour le développement. Sous WSL, ce problème n’apparaît pas.

### Permissions / chemins

En WSL, le projet doit résider dans le système de fichiers Linux (`/home/lucas/...`), pas sur le lecteur Windows monté (`/mnt/c/...`), pour de meilleures performances Docker et éviter les soucis de permissions.

### Docker dans WSL

- **Docker Desktop** : activer « Use the WSL 2 based engine » et l’intégration avec la distro Ubuntu.
- **Docker Engine natif WSL** : installer Docker directement dans WSL (sans Docker Desktop).

---

## 7. Références croisées

- **Prêt à démarrer** : `docs/base-de-connaissances/pret-a-demarrer.md` (Linux en premier)
- **Infra DevOps** : `docs/base-de-connaissances/infra-devops.md`
- **Stratégie Make** : `docs/base-de-connaissances/strategie-operationnelle-make.md`
- **Règle DevOps** : `.cursor/rules/devops.mdc`

---

*Environnement cible : **Ubuntu (dernier LTS)** — natif ou WSL. PowerShell en secours seulement. Dernière mise à jour : 2026-02-05.*
