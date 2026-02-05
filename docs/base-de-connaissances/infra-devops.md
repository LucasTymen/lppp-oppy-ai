# Infra & DevOps LPPP

Document de référence pour l’architecte DevOps / ingénieur système : flux, secrets, déploiement, orchestration. Aligné avec les règles du projet (anti-hallucination, data-driven).

**Règles de sécurité** : voir `docs/base-de-connaissances/regles-securite.md` (secrets, Django prod, CSRF/XSS/injection, auth, API, checklist prod).

**Environnement préféré** : Windows + WSL (travail dans WSL, bash) — voir `docs/base-de-connaissances/environnement-wsl-linux.md`. PowerShell en secours seulement.

---

## 1. SquidResearch et credentials

- **Priorité SquidResearch** : pour toute modification de **conteneurs** ou de **credentials**, **SquidResearch a la priorité**. LPPP **s’adapte** à son contexte. SquidResearch a déjà une prod et un écosystème ; **ne pas risquer de les endommager**. En cas de conflit (ports, noms, .env), c’est LPPP qui change — jamais modifier ni supprimer les conteneurs ou credentials SquidResearch. Règle pour toute l’équipe et les agents.
- **On ne remplace pas le conteneur SquidResearch** — tu en as encore besoin. **SquidResearch reste un projet à part** avec son propre Docker ; **LPPP a son propre Docker** (docker-compose à la racine de LPPP). Les deux **coexistent** : tu peux faire tourner SquidResearch quand tu veux (référence, API, charte) et LPPP indépendamment.
- **SquidResearch** est une **référence externe** (architecture, bonnes pratiques). Il n’est **pas dans le workspace LPPP** ; chemin pour outils (template, copie de code) : **absolu** `/home/lucas/tools/squidResearch` (cf. `sources.md`).
- **Log commun LPPP ↔ SquidResearch** : adresses, ports, variables d’env, chemins, coexistence et état des projets Docker sont décrits dans **`docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md`** du dépôt SquidResearch (chemin absolu : `/home/lucas/tools/squidResearch/docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md`). Pointeur dans LPPP : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md`. À consulter pour éviter conflits de ports et mélange des .env.
- Les **clés SSH, logs et credentials** permettant de travailler sur GitHub, GitLab, Vercel ou Contabo **ne sont pas stockés dans ce dépôt** et ne doivent **jamais** y être committés.
- **LPPP réutilise les clés et la stratégie SSH de SquidResearch** : même machine, même `~/.ssh`, même agent SSH pour GitHub et GitLab (voir `git-remotes-github-gitlab.md`). Pas de nouvelle config nécessaire.
- Si tu utilises un environnement ou un dépôt SquidResearch séparé : les secrets restent dans ce contexte (machine locale, vault, CI secrets) ou dans les plateformes cibles (GitHub Secrets, Vercel, Contabo). Aucune copie de clés privées ou de mots de passe dans LPPP.

---

## 1.1 Comment faire tourner LPPP (conteneurs)

**LPPP a ses propres conteneurs** — pas besoin de créer un nouveau container ni d’utiliser celui de SquidResearch pour faire tourner LPPP.

- **Où** : à la racine du projet LPPP (`docker-compose.yml`, `docker/Dockerfile.web`, `Makefile`).
- **Lancer** : `docker compose up -d` ou `make up`. Services démarrés : **db** (PostgreSQL), **redis**, **web** (Django/Gunicorn), **celery**, **celery-beat**, **n8n**, **flowise**. Optionnel (profil `full`) : **enriched**, **kalilinux**. **Stratégie opérationnelle Make** : voir `strategie-operationnelle-make.md` (catalogue commandes, workflows, répartition DevOps/Dev Django/Chef Projet). `make help` pour l'aide.
- **Première fois** : créer un `.env` depuis `.env.example`, puis `make build` puis `make up` puis `make createsuperuser` pour accéder à l’admin et à `/essais/`. **Guide complet** (venv, Docker, dev local avec PostgreSQL, tester l’admin) : `docs/base-de-connaissances/pret-a-demarrer.md`.
- **Dev local avec PostgreSQL** : lancer uniquement `db` et `redis` (`docker compose up -d db redis`), exposer les ports 5432 et 6379 ; dans `.env` mettre `DB_HOST=localhost`, `REDIS_URL=redis://127.0.0.1:6379/0`, etc. ; venv, `pip install`, `migrate`, `createsuperuser`, `make runserver`. PostgreSQL uniquement (pas de SQLite, incompatible). Voir `pret-a-demarrer.md` § Option B.
- **SquidResearch** : c’est un **autre projet** (référence externe, hors workspace). Tu peux :
  - **Faire tourner uniquement LPPP** : utiliser uniquement le `docker-compose` du dépôt LPPP — tout fonctionne dans les conteneurs LPPP (web, db, redis, celery, n8n, flowise, etc.).
  - **Optionnel** : si le **stack SquidResearch** tourne ailleurs et expose une API (ex. ENRICHED), tu peux configurer LPPP pour l’appeler (ex. `ENRICHED_API_URL` dans `.env`) — mais pour faire tourner Django LPPP, l’admin et `/essais/`, tu utilises **les conteneurs LPPP**, pas le container SquidResearch.

**Résumé** : pour faire tourner LPPP, tu lances le stack **LPPP** (`make up` ou `docker compose up -d`). SquidResearch n’est **pas remplacé** — il garde son propre conteneur ; tu le lances à part quand tu en as besoin (référence, flux, API, charte).

### Avis : notre propre Docker pour LPPP (déjà en place)

**C’est plus sain d’avoir notre propre Docker pour LPPP** (ce qu’on a déjà) et de garder SquidResearch comme projet séparé avec son propre conteneur :

- **Indépendance** : LPPP ne dépend pas du flux ou du conteneur SquidResearch pour démarrer ; tu peux faire tourner LPPP seul.
- **Clarté** : deux projets, deux stacks ; pas de mélange de config ni de dépendances croisées.
- **SquidResearch disponible** : tu peux lancer SquidResearch quand tu veux (référence, copie de code, API ENRICHED, charte graphique) sans que LPPP en dépende.
- **Évolution** : si tu déplaces ou fais évoluer SquidResearch, LPPP continue de tourner avec son propre `docker-compose` et ses propres images.

---

## 2. Où stocker les secrets (bonnes pratiques)

| Contexte | Où stocker | À ne pas faire |
|----------|------------|-----------------|
| **Local / Docker** | Fichier `.env` à la racine (non versionné), généré depuis `.env.example` | Ne jamais committer `.env` ni clés privées |
| **GitHub** | Repository → Settings → Secrets and variables → Actions | Pas de secrets dans le code ni dans les workflows en clair |
| **GitLab** | Settings → CI/CD → Variables (masked) | Idem |
| **Vercel** | Project → Settings → Environment Variables | Idem |
| **Contabo (VPS)** | SSH sur le serveur ; `.env` ou variables d’environnement côté serveur ; clés SSH dans `~/.ssh` (agent SSH) | Pas de clés privées dans le dépôt |

- **SSH** : utiliser l’agent SSH (`ssh-add`) et des clés dédiées par usage (GitHub, GitLab, Contabo). Les clés sont créées/configurées en dehors du dépôt.
- **.gitignore** : vérifier que `.env`, `*.pem`, `*.key` et dossiers de secrets sont ignorés.

---

## 2.1 Conventions : rien de sensible committé

- **Règle** : aucun fichier contenant des secrets, mots de passe, clés privées, tokens ou données personnelles ne doit être versionné.
- **.gitignore** (racine du dépôt) : liste exhaustive des patterns à ignorer. Ne pas retirer d’entrées sans validation. Voir sections :
  - **Secrets et credentials** : `.env`, `.env.*`, `*.pem`, `*.key`, `secrets/`, `credentials/`, `.vercel`, etc.
  - **Logs et dumps** : `*.log`, `*.dump`, `*.sql`, `*.bak` (les logs et dumps peuvent contenir des données sensibles).
  - **Django** : `staticfiles/`, `media/`, `*.sqlite3`, `local_settings.py`.
  - **Python / IDE / OS** : venv, `__pycache__`, `.idea`, `.vscode`, `.DS_Store`, etc.
- **Bonnes pratiques** :
  - Utiliser **uniquement** `.env.example` (sans valeurs réelles) en dépôt ; chaque environnement a son `.env` local non versionné.
  - Ne jamais coller de token, clé API ou mot de passe dans le code, les issues ou les messages de commit.
  - En CI/CD : utiliser les **Secrets** / **Variables** du dépôt (GitHub Secrets, GitLab CI variables, Vercel env), jamais en clair dans les workflows.
- **Vérification** : avant chaque commit, s’assurer qu’aucun fichier listé dans `.gitignore` n’est ajouté (`git status` ; en cas de doute, `git check-ignore -v <fichier>`).

---

## 3. Flux et plateformes

### 3.1 Source de code et remotes Git

- **Git** : initialisation et remotes (GitHub + GitLab) décrits dans `docs/base-de-connaissances/git-remotes-github-gitlab.md`. **GitHub pilote** (remote `origin`), **GitLab** en miroir (remote `gitlab`). Contrairement à SquidResearch où GitLab pilotait, c’est GitHub qui pilote pour LPPP.
- **GitHub / GitLab** : dépôt source du projet. Branche par défaut protégée (ex. `main`), PR/MR pour les changements.
- Les agents ne doivent pas pousser directement sur la branche de prod sans processus défini (cf. règle `devops.mdc`).

### 3.2 Déploiement

| Cible | Usage typique | Secrets / config |
|-------|----------------|------------------|
| **Vercel** | **Frontend Next.js** (landing pages) — déploiement natif Next.js, liaison Git, déploiement auto. **Espace projet** : [vercel.com/lucas-tymens-projects](https://vercel.com/lucas-tymens-projects). Voir `stack-frontend-nextjs-react.md`. | Env vars dans le dashboard Vercel ; token CLI créé dans Vercel (Account → Tokens), jamais dans le dépôt |
| **Contabo** | VPS pour Django, Docker, PostgreSQL, Redis, Celery, n8n, Flowise | SSH + `.env` sur le serveur ; docker-compose ou stack déployée via CI ou manuellement |

- **CI (optionnel)** : GitHub Actions / GitLab CI pour tests, lint, puis déploiement (build Docker, push, ou SSH vers Contabo). Les secrets (tokens, clés SSH déploy) sont dans les variables CI, jamais dans le code.

#### Connexion et déploiement Vercel (automatique ou manuel)

- **Connexion** : se connecter sur [vercel.com/lucas-tymens-projects](https://vercel.com/lucas-tymens-projects) (email, Google, GitHub, etc.). Aucun token ni mot de passe ne doit être stocké dans LPPP ou dans les fichiers de SquidResearch versionnés.
- **Déploiement automatique (recommandé)** : lier le dépôt LPPP à Vercel (Import Git Repository) ; chaque push sur la branche choisie déclenche un déploiement. **Stack frontend** : Next.js + React (voir `stack-frontend-nextjs-react.md`) — Vercel détecte Next.js automatiquement. Variables d’environnement à configurer dans **Project → Settings → Environment Variables**.
- **Déploiement CLI** : `npx vercel` ou `vercel --prod` après `vercel login` ; le token est géré par Vercel (Account → Tokens), à utiliser en local ou en CI via une variable d’environnement (ex. `VERCEL_TOKEN`), jamais committée.
- Les logs et fichiers de paramètres d’un autre projet (ex. SquidResearch) ne doivent pas servir à extraire des credentials pour LPPP : chaque projet utilise ses propres tokens, créés dans le dashboard Vercel.

### 3.3 Organisation des flux

1. Développement sur branche feature → PR/MR → revue.
2. Merge sur `main` (ou branche de déploiement) après validation.
3. Déploiement déclenché par tag, merge ou manuel, selon la stratégie choisie.
4. En prod : pas de `DEBUG=True`, `SECRET_KEY` fort, `ALLOWED_HOSTS` explicite, base et Redis sécurisés.

### 3.4 Ports (référence — ne pas confondre)

| Port | Service | Contexte |
|------|---------|----------|
| **3000** | **Flowise** | Réservé. En local : http://localhost:3000. Ne pas utiliser 3000 pour les landings Next.js. |
| **3001** | Landings Next.js (standalone-ackuracy, etc.) | En local : `cd deploy/standalone-ackuracy && npm run dev` → http://localhost:3001. Script `dev` avec `-p 3001` dans `package.json`. |
| 5678 | n8n | Workflows, API. |
| 8000 | Django (conteneur web) | Option A Docker. Option B runserver : 8080 (voir `erreurs-et-solutions.md` § localhost:8000). |

**Règle** : ne jamais indiquer http://localhost:3000 pour une landing Next.js ; le port 3000 est celui de Flowise.

---

## 4. Variables d’environnement LPPP (référence)

Voir `.env.example` à la racine. Résumé des variables utilisées par le projet (Django, docker-compose) :

- **Django** : `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DB_*`, `CELERY_BROKER_URL`, `CELERY_RESULT_BACKEND`, `TIME_ZONE`, `CORS_ALLOWED_ORIGINS`.
- **Docker / services** : `DB_*`, `N8N_*`, `FLOWISE_*`, `TZ`.

En prod : générer une `SECRET_KEY` forte, utiliser des mots de passe robustes pour DB et services.

---

## 5. Données : pandas, numpy (requirements.txt)

- **Libs** : `pandas`, `numpy` dans `requirements.txt` — CSV (rapport SEO Screaming Frog), analytics, KPIs, études Growth/Data Analyst. Voir `docs/base-de-connaissances/bibliotheques-agents-techniques.md` (tour des besoins agents techniques, sans overkill).
- **Viz** : pas de matplotlib/plotly pour l’instant ; rapports visuels via templates HTML et données préparées avec pandas.

---

## 6. Stack optionnel : SEO sémantique (Python, open-source)

- **Doc** : `docs/base-de-connaissances/seo-semantique-outils-open-source.md` — stack pour keyword-to-topic, topic modelling, clustering (spaCy, Gensim, NLTK, Transformers). Pilote fonctionnel : **Expert SEO / AI-GEO** ; pilotes technique / infra : **Dev Django**, **DevOps**.
- **Dépendances optionnelles** : `requirements-seo.txt` à la racine. **Ne pas** les ajouter au `requirements.txt` principal sans accord : elles alourdissent l’env (NLP, transformers). Options :
  - **Venv dédié** : pour analyses ponctuelles (notebooks, scripts) sans toucher au conteneur web/celery.
  - **Intégration Docker** : si le stack est intégré dans le flux (commande Django, tâche Celery), ajouter `requirements-seo.txt` dans le Dockerfile (ex. étape dédiée ou cible `seo`) pour limiter la taille de l’image prod si besoin.
- **Modèles** : spaCy (ex. `fr_core_news_sm`, `en_core_web_sm`) et Hugging Face (sentence-transformers) peuvent être lourds ; documenter le cache (variables d’env, volume Docker) si pertinent. Voir la doc SEO sémantique.

---

## 7. Rôle DevOps et orchestration

- **Contrôle des flux** : s’assurer que les changements (code, config, autres agents) respectent les branches, les secrets et la prod.
- **Conseils des autres agents** : les intégrer sans casser la prod (tests, migrations, rollback possible, pas de push direct sur `main` sans processus).
- **Temps réel** : avant tout déploiement ou modification critique, vérifier : migrations Django, variables d’env, santé des services (DB, Redis, Celery).

Les règles détaillées pour les agents (orchestration, protection prod) sont dans `.cursor/rules/devops.mdc`.

---

*Dernière mise à jour : 2025-01-30. Ajout § 5 Stack optionnel SEO sémantique (requirements-seo.txt, coordination Expert SEO / Dev Django). Source : projet LPPP, README, docker-compose, settings Django.*
