# Prêt à démarrer — environnement, admin, première landing

**Rôle** : Mettre en place l’environnement (venv, Docker ou dev local), tester l’admin et lancer le projet avec la première landing page.  
**Référence** : `README.md`, `docs/base-de-connaissances/infra-devops.md`, `Makefile`.  
**Environnement préféré** : WSL ou Linux — voir `docs/base-de-connaissances/environnement-wsl-linux.md`.

**Environnement choisi pour LPPP** : **Docker web** (Option A — conteneur web sur port 8000). Option B (runserver local) reste en dépannage si accès impossible sous Windows (voir § 5).

---

## 1. Environnement virtuel (Python)

À la **racine du projet** (où se trouvent `manage.py`, `requirements.txt`) :

```bash
# Créer le venv (une seule fois)
python3 -m venv .venv

# Activer (Linux / WSL / macOS) — environnement préféré
source .venv/bin/activate

# Activer (Windows PowerShell) : .venv\Scripts\Activate.ps1
# Activer (Windows CMD) : .venv\Scripts\activate.bat

# Installer les dépendances
pip install -r requirements.txt
```

Le venv sert à : lancer Django en local (option B ci‑dessous), lancer les tests (`make test` ou `pytest`), et utiliser les outils (pandas, etc.) dans l’IDE.

---

## 2. Tester le projet : deux options

### Option A — Docker (recommandé : tout le stack)

Idéal pour avoir PostgreSQL, Redis, Celery, n8n, Flowise et tester l’admin comme en conditions réelles.

```powershell
# 1. Copier le fichier d’environnement
copy .env.example .env
# Éditer .env si besoin (SECRET_KEY, mots de passe).

# 2. Lancer les conteneurs
make start
# Ou : make go   (démarrage à froid complet, inclut build + migrate + collectstatic)
# make start = une seule commande pour tout lancer (pas de venv requis)

# 3. Les migrations sont appliquées au démarrage du service web.
# Créer un superutilisateur pour l’admin :
make createsuperuser

# 4. Ouvrir dans le navigateur
# Admin : http://localhost:8000/admin/
# Interface essais : http://localhost:8000/essais/
# Landing pages (liste) : http://localhost:8000/
```

**Arrêter** : `make down`.

---

### Option B — Dev local avec PostgreSQL (db + redis dans Docker)

Django et Celery tournent sur ta machine ; PostgreSQL et Redis restent dans Docker. Utile pour développer sans reconstruire le conteneur web à chaque fois.

```bash
# 1. Lancer uniquement la base et Redis
docker compose up -d db redis
# Les ports 5432 (PostgreSQL) et 6379 (Redis) sont exposés sur localhost.

# 2. Copier et adapter .env pour la machine locale (Linux : cp)
cp .env.example .env
# Dans .env : DB_HOST=localhost (ou 127.0.0.1), REDIS_URL=redis://127.0.0.1:6379/0,
# CELERY_BROKER_URL=redis://127.0.0.1:6379/1, CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/2

# 3. Créer et activer le venv (voir § 1)
python3 -m venv .venv
source .venv/bin/activate   # Linux/WSL — ou .venv\Scripts\Activate.ps1 (Windows)
pip install -r requirements.txt

# 4. Migrations et superutilisateur
python manage.py migrate --noinput
python manage.py createsuperuser

# 5. Lancer le serveur de dev
make runserver
# Ou : python manage.py runserver

# 6. (Optionnel) Dans un autre terminal : Celery worker
# source .venv/bin/activate puis : celery -A lppp worker -l info

# 7. Ouvrir dans le navigateur
# Admin : http://127.0.0.1:8000/admin/
# Interface essais : http://127.0.0.1:8000/essais/
# Landing pages (liste) : http://127.0.0.1:8000/
```

**Note** : On reste sur **PostgreSQL** partout (hors tests pytest) ; pas de SQLite en dev, pour ne pas être bloqué si le projet devient une appli à part entière.

---

## 3. Tester l’interface admin

1. Aller sur **http://localhost:8000/admin/** (ou http://127.0.0.1:8000/admin/ en local).
2. Se connecter avec le compte créé par `createsuperuser`.
3. Modèles disponibles :
   - **Campagnes** (apps.campaigns) : campagnes de prospection.
   - **Prospects** (apps.campaigns) : prospects par campagne.
   - **Landing pages** (apps.landing_pages) : landing pages (titre, slug, prospect, template, `content_json`, publication).

Tu peux créer une campagne, un prospect, puis une landing page associée pour préparer la première landing.

---

## 4. Première landing page (prêt à commencer)

- **Template relance événement** : `templates/landing_pages/relance-evenement.html` (structure hero, CTA, `content_json`).
- **Structure `content_json`** : voir `docs/base-de-connaissances/structure-content-json-relance-evenement.md`.
- **Segmentation premier rapport + landing** : `docs/base-de-connaissances/segmentations/2025-01-30-premier-rapport-seo-landing-p4s-archi.md` (Expert SEO, Growth, Rédacteur, Designer, Chef de Projet).

**Workflow** : créer une campagne et un prospect dans l’admin → créer une landing page (template `relance-evenement`, remplir `content_json` ou le laisser pour le Rédacteur) → publier (`is_published=True`) → afficher via l’URL de la landing (voir `apps.landing_pages.urls`).

---

## 5. Dépannage

### 5.1 ModuleNotFoundError: No module named 'environ' (WSL / Linux)

En WSL ou Linux, si tu lances `python3 manage.py runserver` **sans avoir installé les dépendances**, Django plante au chargement de `lppp/settings.py` (qui utilise `django-environ`).

**À faire** : à la racine du projet (là où se trouvent `manage.py` et `requirements.txt`) :

```bash
# Option 1 : venv (recommandé)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Option 2 : sans venv (Python système)
pip3 install -r requirements.txt
```

Puis lancer le serveur :

```bash
# Avec python3 (WSL / Linux n’a souvent pas de commande « python »)
python3 manage.py runserver
```

Pour activer le mode debug (traceback détaillée en cas d’erreur 500) :

```bash
export DEBUG=True
python3 manage.py runserver
# ou en une ligne : DEBUG=True python3 manage.py runserver
```

### 5.2 localhost / admin ne répond pas (connexion réinitialisée, ERR_EMPTY_RESPONSE)

**Environnement virtuel** : avec Docker (`make start`, `make go`), aucun venv n'est requis — tout tourne dans les conteneurs. Le venv sert uniquement à l'Option B (runserver local).

**Sous Windows** (Docker Desktop), le port forward vers le conteneur web peut provoquer une **connexion réinitialisée** (« La connexion avec le serveur a été réinitialisée ») alors que Django répond dans le conteneur.

**Solution recommandée** : utiliser l’**Option B (dev local)** pour accéder à l’admin et à /essais/ depuis le navigateur :

1. Arrêter le conteneur web : `docker compose stop web` (libère le port pour runserver).
2. Dans `.env` : `DB_HOST=localhost` (ou `127.0.0.1`), `REDIS_URL=redis://127.0.0.1:6379/0`, `CELERY_BROKER_URL=redis://127.0.0.1:6379/1`, `CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/2`.
3. Venv activé (ou Python système) : `python manage.py migrate --noinput`, puis `python manage.py runserver 127.0.0.1:8080` (si le port 8000 est refusé sous Windows, utiliser **8080**).
4. Ouvrir **http://127.0.0.1:8080/admin/** et **http://127.0.0.1:8080/essais/** (ou 8000 si runserver a réussi sur 8000).

Voir § 2 Option B pour le détail.

### 5.3 Docker planté / conteneurs qui redémarrent (web en crash loop)

Si le stack Docker ne répond pas ou que le conteneur **web** redémarre en boucle :

1. **Vérifier que `.env` existe** (obligatoire pour `docker compose` — les services web, celery utilisent `env_file: .env`) :
   ```bash
   make ensure-env   # Crée .env depuis .env.example si absent
   ```

2. **Voir les logs du service web** pour identifier l’erreur :
   ```bash
   make logs-web
   # ou : docker compose logs web
   # ou : docker compose logs --tail=100 web
   ```
   Erreurs fréquentes : fichier `.env` absent, `ModuleNotFoundError` (image non reconstruite), connexion DB refusée (attendre que `db` soit healthy).

3. **Reconstruire les images** si le code ou les dépendances ont changé :
   ```bash
   make build
   make start
   ```
   Si le cache pose problème : `make build-no-cache` puis `make start`.

4. **Conflit « container name already in use »** (conteneurs lppp_db, lppp_web, etc. déjà présents) :  
   Cela arrive quand les conteneurs ont été créés depuis un autre répertoire ou projet Compose. `make down` ne les supprime pas. **Solution** :
   ```bash
   make clean-containers   # Supprime les conteneurs lppp_* par nom
   make start
   ```

5. **Relancer proprement** (WSL recommandé, projet sous `/home/...` pour éviter soucis de montage) :
   ```bash
   make down
   make ensure-env
   make start
   ```
   Si erreur « name already in use » : `make clean-containers` puis `make start`.

---

## 6. Récap URLs

| URL | Usage |
|-----|--------|
| http://localhost:8000/admin/ | Interface admin Django (campagnes, prospects, landing pages) |
| http://localhost:8000/essais/ | Interface landingsgenerator (premier écran relance salon) |
| http://localhost:8000/ | Liste des landing pages (selon `apps.landing_pages.urls`) |
| http://localhost:8000/p/<slug>/ | Page publique d’une landing (si `is_published=True`) |

---

## 7. Références

- **Environnement WSL/Linux** : `docs/base-de-connaissances/environnement-wsl-linux.md` (environnement préféré)
- **Infra** : `docs/base-de-connaissances/infra-devops.md`
- **Makefile** : `make help`, `make up`, `make migrate`, `make createsuperuser`
- **README** : `README.md` (stack, démarrage rapide Docker)
- **Première landing P4S-archi** : `docs/base-de-connaissances/segmentations/2025-01-30-premier-rapport-seo-landing-p4s-archi.md`

---

*Document créé par le Conseiller. Dernière mise à jour : 2025-01-30.*
