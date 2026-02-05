# Registre erreurs et solutions LPPP

**Objectif** : Répertorier les erreurs rencontrées et les solutions trouvées pour éviter de les reproduire et guider les agents qui rencontrent des soucis.

**Maintenu par** : Agent qui assiste le Chef de Projet (mise à jour au fur et à mesure des corrections).  
**Consulté par** : Tous les agents — en cas de blocage ou d’erreur, consulter ce registre avant de réinventer ; après une correction, ajouter une entrée.  
**Référence** : `agents-roles-responsabilites.md` (§ Chef de Projet, RACI « Documenter erreurs et solutions »), `pilotage-agents.mdc` (Data-driven et logs).

---

## Comment utiliser ce registre

### Pour un agent qui rencontre une erreur
1. **Consulter ce fichier** : chercher une entrée similaire (contexte, message d’erreur, stack).
2. Si une entrée existe : appliquer la solution et les précautions indiquées.
3. Si aucune entrée : après résolution, **ajouter une entrée** (voir format ci‑dessous) et mettre à jour les logs (`log-projet.md` ou `log-ia.md`).

### Pour l’agent qui assiste le Chef de Projet
- **À chaque correction d’erreur** : ajouter ou compléter une entrée dans ce registre et mettre à jour les logs pour que l’équipe ne reproduise pas l’erreur.
- **Interaction** : le Chef de Projet valide que la doc est à jour ; l’Orchestrateur peut référencer ce doc dans le registre agents/ressources.

---

## Format d’une entrée

Pour chaque erreur documentée, indiquer :

| Champ | Description |
|-------|-------------|
| **Date** | Date de la correction ou de la première occurrence documentée |
| **Contexte** | Où / quand ça se produit (WSL, Docker, commande, page, etc.) |
| **Erreur** | Message d’erreur ou symptôme (copier-coller si pertinent) |
| **Cause** | Cause identifiée (optionnel mais utile) |
| **Solution** | Étapes ou correctif appliqué |
| **Prévention** | Comment éviter que ça se reproduise (doc, procédure, checklist) |
| **Lien(s)** | Vers une doc ou procédure dédiée (ex. `environnement-wsl-linux.md`) |

---

## Entrées

*(Les entrées seront ajoutées au fur et à mesure des corrections.)*

### Exemple (template) — ModuleNotFoundError: No module named 'environ'

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | WSL, lancement `make runserver` ou `python manage.py runserver` |
| **Erreur** | `ModuleNotFoundError: No module named 'environ'` |
| **Cause** | Environnement virtuel absent ou dépendances non installées (django-environ dans requirements.txt) |
| **Solution** | `make venv-install` puis `make runserver` |
| **Prévention** | Utiliser `make venv-install` après clône ou changement de branche ; doc `environnement-wsl-linux.md` § 6, Option B |
| **Lien(s)** | `environnement-wsl-linux.md`, `strategie-operationnelle-make.md` § 3.7, `2025-01-30-correction-relance-wsl.md` |

---

### Docker — « The container name "/lppp_xxx" is already in use »

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | WSL ou Linux, `make up` ou `make start` dans le projet LPPP |
| **Erreur** | `Error response from daemon: Conflict. The container name "/lppp_db" is already in use by container "..."` (ou lppp_redis, lppp_web, etc.) |
| **Cause** | Conteneurs LPPP orphelins (créés lors d’une exécution précédente, éventuellement depuis un autre répertoire ou projet Compose). `make down` ne les supprime pas car ils ne sont plus associés au projet Compose actuel. |
| **Solution** | Supprimer **uniquement les conteneurs LPPP** par leur nom, puis relancer : `docker rm -f lppp_db lppp_redis lppp_web lppp_celery lppp_celery_beat lppp_n8n lppp_flowise 2>/dev/null; make up`. **Ne jamais** supprimer ou modifier les conteneurs SquidResearch (django, worker, react, n8n, flowise, postgres, redis, etc.) : SquidResearch a la priorité (prod, écosystème). Décision : `decisions.md` « Priorité SquidResearch ». |
| **Prévention** | Lancer `make down` depuis la racine LPPP avant de quitter ou en cas de changement de branche. En cas de conflit, ne toucher qu’aux conteneurs dont le nom commence par `lppp_`. |
| **Lien(s)** | `infra-devops.md` § 1 (Priorité SquidResearch), `log-commun-lppp-squidresearch.md` |

---

### Flowise — incompatibilités de types entre nœuds / difficulté à raccorder

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Flowise, canvas Chatflow ou flow d'ingestion ; tentative de relier des nœuds entre eux |
| **Erreur** | Connexion refusée entre nœuds, message d'incompatibilité de type, ou flow qui ne s'exécute pas après câblage |
| **Cause** | Flowise impose des types de flux (Document, ChatMessage, etc.) : une sortie ne peut aller que vers une entrée du même type. Câbler « Document » vers « ChatMessage » (ou l'inverse) provoque des erreurs. |
| **Solution** | Pour le RAG Concierge Maisons-Alfort : **ne pas câbler** les nœuds. Utiliser la section **Document Stores** pour l'ingestion (Loader → Splitter → Embedding → Vector Store, sans fils). Sur le **Chatflow**, mettre un seul nœud **Agent** et configurer **Knowledge** via la liste déroulante (sélection du Document Store), pas par un câble. |
| **Prévention** | Suivre la recette `docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md` § « Pourquoi les nœuds ne se raccordent pas ». Règle : Document → Document uniquement ; ChatMessage/string → même type. Vérifier les libellés des prises avant de connecter. |
| **Lien(s)** | `docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md`, `flowise-concierge-ia-maisons-alfort-guide.md` |

---

### make migrate / makemigrations — « service "web" is not running »

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | WSL (ou autre), après commit/push ; `make makemigrations` ou `make migrate` |
| **Erreur** | `service "web" is not running` — Makefile:309 (makemigrations) ou Makefile:299 (migrate) Error 1 |
| **Cause** | Les commandes exécutent `docker compose exec web python manage.py ...` ; le conteneur `web` n’existe pas tant que le stack n’est pas démarré. |
| **Solution** | Démarrer le stack : **`make start`** (recommandé : démarre db, redis, web, etc. puis applique migrate automatiquement) ou **`make up`** puis **`make migrate`**. |
| **Prévention** | Avant toute commande `make migrate` / `make makemigrations`, s’assurer que les services tournent (`make ps`). Procédure : `procedure-avant-migrations-relance.md` — l’ordre est : 1) commit+push, 2) **démarrer le stack** si besoin, 3) migrations, 4) relance si nécessaire. |
| **Lien(s)** | `procedure-avant-migrations-relance.md`, `strategie-operationnelle-make.md` |

---

### Docker — « The container name "/lppp_redis" is already in use »

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | `make start` ou `docker compose up -d db redis` ; WSL ou autre |
| **Erreur** | `Error response from daemon: Conflict. The container name "/lppp_redis" is already in use by container "…". You have to remove (or rename) that container to be able to reuse that name.` |
| **Cause** | Un conteneur nommé `lppp_redis` (ou autre `lppp_*`) existe déjà — créé par un ancien `docker compose` ou par un autre répertoire/projet utilisant les mêmes noms. |
| **Solution** | Supprimer les conteneurs LPPP par nom : **`make clean-containers`** puis **`make start`**. (Ne supprime pas les **volumes** : les données db/redis/n8n/flowise restent ; seuls les conteneurs sont retirés.) |
| **Prévention** | Après un `make down` dans un autre répertoire ou un changement de branche, en cas de conflit utiliser `make clean-containers` avant `make start`. |
| **Lien(s)** | `Makefile` (cible `clean-containers`), `strategie-operationnelle-make.md` |

---

### Admin Django — impossible de se connecter / « il n’y a rien »

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-04 |
| **Contexte** | Ouverture de `http://localhost:8010/admin/` (Docker LPPP) : page blanche, timeout, connexion refusée ou aucun formulaire de login. |
| **Erreur** | Rien ne s’affiche, ou « This site can’t be reached », ou page vide. |
| **Cause** | (1) **Stack non démarré** : conflit Docker (`lppp_db` / `lppp_redis` already in use) → `make up` échoue, le conteneur `web` ne tourne pas. (2) **Aucun superutilisateur** : aucun compte admin n’a été créé (ou mot de passe oublié). |
| **Solution** | **(1)** Supprimer les conteneurs LPPP puis relancer : **`make clean-containers`** puis **`make start`**. Attendre la fin (migrate, static). **(2)** Créer un compte admin : **`make createsuperuser`** (dans le terminal, saisir username, email, mot de passe). Puis ouvrir `http://localhost:8010/admin/` et se connecter. |
| **Prévention** | Après un conflit Docker, toujours utiliser `make clean-containers` avant `make start`. À la première installation ou sur une base vide, exécuter `make createsuperuser` avant d’aller sur l’admin. |
| **Lien(s)** | `Makefile` (clean-containers, createsuperuser), `pret-a-demarrer.md`, entrée « Docker — container name already in use » ci-dessus. |

---

### make start — « Django pas encore prêt » en boucle puis interruption

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | `make start` après `make clean-containers` ; conteneurs démarrés mais la boucle d’attente de Django ne se termine pas. |
| **Erreur** | Message répété « Django pas encore prêt, attente 5s... » pendant plusieurs minutes ; pas de message d’erreur visible. |
| **Cause** | `python manage.py check` échoue ou bloque dans le conteneur `web` (sortie masquée par le Makefile). Causes fréquentes : migrations non appliquées, DB injoignable, erreur d’import ou de config Django. |
| **Solution** | (1) **Diagnostiquer** : `docker compose exec web python manage.py check` (voir l’erreur réelle) et `docker compose logs web --tail 80` (logs Gunicorn). (2) **Makefile mis à jour** : `make start` applique maintenant les migrations tôt (après 15 s) puis refait le check ; après 12 échecs (1 min) il affiche la sortie de `check` puis quitte. Relancer `make start` après correction. (3) Si la DB est vide ou corrompue : `make migrate` à la main après avoir vérifié que `web` et `db` tournent. |
| **Prévention** | Utiliser `make start` à jour ; en cas de boucle, ne pas attendre indéfiniment : Ctrl+C puis exécuter les commandes de diagnostic ci‑dessus. |
| **Lien(s)** | `Makefile` (cible `start`), `procedure-avant-migrations-relance.md` |

---

### ModuleNotFoundError: No module named 'markdown' (conteneur web)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | `make start` ou `docker compose logs web` ; conteneur `web` en boucle de redémarrage. |
| **Erreur** | `ModuleNotFoundError: No module named 'markdown'` dans `apps/landing_pages/views.py` (ou autre module). |
| **Cause** | La dépendance est dans `requirements.txt` mais l’**image Docker** du service `web` a été construite avant son ajout (ou jamais reconstruite). |
| **Solution** | **Reconstruire l’image** : `make build` puis `make start`. Ou `docker compose build web` puis `docker compose up -d web`. Le conteneur récupère alors les paquets à jour. |
| **Prévention** | Après ajout ou modification de `requirements.txt`, exécuter `make build` (ou `docker compose build`) avant de relancer les services. |
| **Lien(s)** | `requirements.txt`, `Makefile` (build), `strategie-operationnelle-make.md` |

---

### Landing /p/maisons-alfort/ — Écran blanc

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Page **/p/maisons-alfort/** (ou /maisons-alfort/ après redirection) : écran blanc, rien ne s’affiche ou le contenu n’est pas visible. |
| **Erreur** | Écran blanc (page entière ou zone chat uniquement). |
| **Causes possibles** | (1) **Dev Django** : exception dans la vue, template manquant ou mal nommé, contexte incomplet ; (2) **DevOps** : Django non servi sur l’URL, Flowise non exposé sur 3000, `.env` sans FLOWISE_CHATFLOW_ID / FLOWISE_URL ; (3) **Architecte** : route manquante ou conflit, LandingPage `maisons-alfort` absente en base (migration 0004 non appliquée) ; (4) **Designer** : CSS qui masque le contenu (fond blanc + texte blanc, overflow hidden) ; (5) **Automatizer** : Flowise ne répond pas sur /embed/{id}, chatflow absent ou ID incorrect. |
| **Solution** | **Sprint multi-agents** : suivre `segmentations/2026-01-30-sprint-ecran-blanc-landing-chatbot.md`. **Architecte** : vérifier chaîne route → vue → template, existence de la LandingPage en base. **DevOps** : vérifier que Django répond (curl /p/maisons-alfort/ → 200), Flowise sur 3000, .env FLOWISE_CHATFLOW_ID et FLOWISE_URL. **Dev Django** : s’assurer que flowise_embed_url est passé (ou "" pour placeholder), template toujours visible (hero + intro + zone chat). **Designer** : vérifier styles (contraste, pas de contenu masqué). **Automatizer** : vérifier chatflow déployé et URL /embed/{id} joignable. |
| **Prévention** | Toujours afficher au minimum hero + intro + message « Chat en cours de configuration » si pas d’URL embed ; ne jamais renvoyer une page vide. Voir template `concierge_maisons_alfort.html` et vue `landing_public`. |
| **Lien(s)** | `segmentations/2026-01-30-sprint-ecran-blanc-landing-chatbot.md`, `flowise-concierge-ia-maisons-alfort-guide.md`, `conciergerie-maisons-alfort-architecture-et-onboarding.md` |

---

### Landing /maisons-alfort/ — « Impossible de trouver l'adresse IP du serveur de flowise »

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Page **http://127.0.0.1:8082/maisons-alfort/** (ou /essais/concierge/) : iframe du chatbot Flowise affiche une erreur « Impossible de trouver l'adresse IP du serveur de flowise ». |
| **Erreur** | « Impossible de trouver l'adresse IP du serveur de flowise » (navigateur, dans la zone de l'iframe). |
| **Cause** | L'URL d'embed envoyée au navigateur pointait vers **http://flowise:3000** (nom d'hôte Docker). Le navigateur tourne sur l'hôte et ne peut pas résoudre « flowise » (résolution DNS du réseau Docker). |
| **Solution** | **Correctif code** : `get_flowise_chat_embed_url()` (apps/scraping/flowise_client.py) utilise maintenant une URL joignable par le navigateur : si `DB_HOST` est `localhost` ou `127.0.0.1` (Django sur l'hôte), l'URL par défaut est **http://localhost:3010** (port LPPP). Sinon définir **`FLOWISE_URL=http://localhost:3010`** dans `.env` et redémarrer le runserver. Vérifier que Flowise écoute sur le port 3000 (`docker compose up -d flowise` ou instance locale). |
| **Prévention** | En dev avec runserver sur l'hôte : définir `FLOWISE_URL=http://localhost:3010` si besoin. En Docker full stack LPPP : l'iframe pointe vers http://localhost:3010 (port dédié). |
| **Lien(s)** | `flowise-concierge-ia-maisons-alfort-guide.md`, `segmentations/2026-01-30-sprint-chatbot-landing-flowise.md` |

---

### Landing /p/maisons-alfort/ — iframe du chatbot vide (cadre blanc)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-04 |
| **Contexte** | La **landing** s’affiche correctement (titre, intro) mais le **cadre (iframe) du chatbot** reste blanc, sans interface de chat. |
| **Erreur** | Zone dédiée au chat visible mais vide (rectangle blanc dans l’iframe). |
| **Causes possibles** | (1) **Flowise n’est pas démarré** sur le port 3000 (ou autre si `FLOWISE_URL` est défini). (2) **Mauvais `FLOWISE_CHATFLOW_ID`** : l’ID dans `.env` ne correspond pas au chatflow Conciergerie dans Flowise (récupérer l’ID dans Flowise → chatflow → onglet **Embed**). (3) **URL d’embed non joignable par le navigateur** : si Django tourne sur l’hôte (runserver 127.0.0.1:8082) sans `FLOWISE_URL`, le code utilise `http://localhost:3010` si `DB_HOST=localhost` (port LPPP) ; si `DB_HOST=db`, l’URL devient `http://flowise:3000` et le navigateur ne peut pas la résoudre → iframe vide. (4) Flowise répond mais la page **/embed/{id}** renvoie une page vide (chatflow inexistant ou erreur côté Flowise). |
| **Solution** | **Étape 1** : Sous l’iframe, cliquer sur **« Ouvrir le chat dans un nouvel onglet »** (lien ajouté sur la page). Si le chat **s’affiche** dans l’onglet → problème d’affichage en iframe (CORS / X-Frame-Options à vérifier côté Flowise). Si le nouvel onglet est **vide ou erreur** → **Étape 2** : Vérifier que Flowise tourne (`docker compose ps` → `lppp_flowise` ou processus sur 3000 ; `curl -s -o /dev/null -w "%{http_code}" http://localhost:3000` → 200). **Étape 3** : Dans Flowise (http://localhost:3010), ouvrir le chatflow Conciergerie Maisons-Alfort → onglet **Embed** → copier l’**ID** et le mettre dans `.env` : `FLOWISE_CHATFLOW_ID=<id>`. **Étape 4** : Si Django est en runserver sur l’hôte (127.0.0.1:8082), forcer l’URL pour le navigateur : dans `.env` définir `FLOWISE_URL=http://localhost:3000` (ou `http://127.0.0.1:3000`), redémarrer le runserver, recharger la page. |
| **Prévention** | En dev local (runserver sur l’hôte) : avoir `FLOWISE_URL=http://localhost:3010` et `FLOWISE_CHATFLOW_ID` correct dans `.env`, et Flowise démarré sur le port 3010 (LPPP). Voir `flowise-concierge-ia-maisons-alfort-guide.md`, `conciergerie-maisons-alfort-architecture-et-onboarding.md`. |
| **Lien(s)** | `flowise-concierge-ia-maisons-alfort-guide.md`, `conciergerie-maisons-alfort-architecture-et-onboarding.md`, entrée « Impossible de trouver l'adresse IP du serveur de flowise » ci-dessus |

---

### Flowise — « No Chatflows Yet » / plus de workflows après reconnexion ou changement de credentials

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Après reconnexion (Flowise demande identifiants) ou après changement de `FLOWISE_USERNAME` / `FLOWISE_PASSWORD` dans `.env`, l’interface Flowise sur localhost:3000 affiche **« No Chatflows Yet »** — plus aucune trace des chatflows créés. Flowise ne permet qu'un seul utilisateur (même email avant/après). |
| **Erreur** | « No Chatflows Yet » ; liste des Chatflows vide. |
| **Cause** | (1) **Deux Flowise** : le port 3000 peut être utilisé par **LPPP** (`lppp_flowise`, volume `flowise_data`) ou par **SquidResearch** (autre conteneur, autre volume). Selon quel stack est démarré, localhost:3000 affiche l’un ou l’autre — les chatflows LPPP ne sont que dans le Flowise LPPP. (2) **Changement de credentials** : en activant ou modifiant `FLOWISE_USERNAME`/`FLOWISE_PASSWORD`, Flowise peut associer les données à un « utilisateur » ; si l’app considère que c’est un nouvel utilisateur, l’espace peut apparaître vide alors que les données sont toujours dans le volume. |
| **Solution** | **Étape 1 — Quel Flowise tourne ?** `docker ps --format "table {{.Names}}\t{{.Ports}}"` et repérer qui expose `3000/tcp`. Si c’est **lppp_flowise** → les données LPPP sont dans le volume `flowise_data` (non supprimé par `docker rm` ni `make down`). Si c’est un autre conteneur (ex. SquidResearch) → tu regardes l’autre instance ; pour retrouver les chatflows LPPP, arrêter l’autre stack et lancer LPPP : `docker compose up -d flowise` depuis la racine LPPP. **Étape 2 — Recréer l’ancien identifiant** : remettre temporairement dans `.env` les **anciennes** valeurs `FLOWISE_USERNAME` et `FLOWISE_PASSWORD` (celles utilisées quand tu avais créé les chatflows), redémarrer Flowise (`docker compose restart flowise`), puis recharger localhost:3010 — les chatflows peuvent réapparaître. **Étape 2 — Recréer le chatflow** : Flowise est single-user ; si les chatflows ont disparu, les recréer avec **`docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md`**, puis mettre le nouvel ID (onglet Embed) dans `.env` : **`FLOWISE_CHATFLOW_ID=<nouvel-id>`**. |
| **Prévention** | Ne pas modifier `FLOWISE_USERNAME`/`FLOWISE_PASSWORD` sans nécessité (risque de réinitialisation). Un seul utilisateur Flowise. Vérifier quel conteneur utilise le port 3000 avant de conclure à une perte de données. Rappel : **`make go`** seul supprime les volumes ; `make down` et `docker rm -f lppp_flowise` ne touchent pas à `flowise_data`. |
| **Lien(s)** | `flowise-concierge-ia-maisons-alfort-guide.md` § Démarrer sans perdre de données, **`sauvegarde-workflows-flowise-n8n.md`** (exporter chatflows dans `docs/flowise-workflows/backups/` pour réinjection), `docker-compose.yml` |

---

### Flowise — 401 Invalid model key or Incorrect local model configuration

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Flowise, chargement d'une page ou exécution d'un chatflow / ingestion |
| **Erreur** | Status 500 — « 401 Invalid model key or Incorrect local model configuration » |
| **Cause** | Problème de configuration du **LLM** ou de l'**embedding** : clé API OpenAI (ou autre) invalide, expirée ou mal renseignée ; ou modèle local (Ollama, etc.) mal configuré (URL, nom du modèle). |
| **Solution** | Vérifier dans Flowise : (1) Credentials / clé API du nœud OpenAI (Chat ou Embeddings) — clé valide et avec les bons droits ; (2) Nom du modèle exact (ex. `gpt-4o-mini`, `text-embedding-3-small`) ; (3) Si modèle local : URL de base (ex. `http://host.docker.internal:11434`) et nom du modèle. Corriger la config puis recharger la page. |
| **Prévention** | Documenter les modèles utilisés dans `data/flowise/comptes-et-llm.md` ; ne pas committer les clés (`.env` / UI Flowise uniquement). |
| **Lien(s)** | `data/flowise/comptes-et-llm.md`, `flowise-faiss-base-path-infra.md` § 5 |

---

### Vercel 404 / DEPLOYMENT_NOT_FOUND — page ne s’affiche pas

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Déploiement Vercel après push sur GitHub ; ouverture de l’URL du projet (ex. `https://<projet>.vercel.app/` ou `/p4s-archi`) |
| **Erreur** | 404, « 404: NOT_FOUND », « DEPLOYMENT_NOT_FOUND » ou page blanche |
| **Cause** | **Root Directory** Vercel incorrect : Vercel build depuis la racine du dépôt au lieu du dossier qui contient l’app Next.js (ex. `frontend/` en monorepo, ou `./` pour un repo standalone où l’app est à la racine). |
| **Solution** | 1) Vercel Dashboard → projet → **Settings** → **General** → **Root Directory** : **Edit** → saisir `frontend` (monorepo) ou `./` / laisser vide (repo standalone à la racine) → **Save**. 2) **Redeploy** : Deployments → **…** sur le dernier déploiement → **Redeploy** (ou pousser un commit). 3) Attendre build **Ready**, réessayer l’URL. |
| **Prévention** | À la création du projet Vercel, configurer tout de suite le **Root Directory** selon le type de repo (standalone = `./`, monorepo = `frontend`). Voir `strategie-deploiement-git-vercel.md` et `deploiement-vercel-frontend.md`. |
| **Lien(s)** | `deploiement-vercel-frontend.md` § 6, `strategie-deploiement-git-vercel.md` (Pièges à éviter) |

---

### Vercel — No Output Directory named "public" after Build

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Déploiement Vercel d’une app Next.js (ex. standalone P4S, frontend) ; build réussit (Route (app), First Load JS) puis échec au final. |
| **Erreur** | `Error: No Output Directory named "public" found after the Build completed. Configure the Output Directory in your Project Settings. Alternatively, configure vercel.json#outputDirectory.` ([Learn More](https://vercel.link/missing-public-directory)) |
| **Cause** | Vercel cherche un répertoire de sortie nommé **public**, alors que Next.js produit **`.next`** (et non `public` — `public` est le dossier d’entrée des assets statiques). Souvent dû à un réglage **Output Directory: public** dans les paramètres du projet Vercel ou à un framework mal détecté. |
| **Solution** | 1) **Dans le repo** : dans le `vercel.json` à la racine de l’app Next.js déployée (ex. `deploy/standalone-p4s/vercel.json` pour P4S), ajouter `"outputDirectory": ".next"` et conserver `"framework": "nextjs"`. 2) **Dans Vercel** : Project → **Settings** → **General** → **Build & Development Settings** → **Output Directory** : laisser **vide** (ou `.next`) et **Framework Preset** = **Next.js** → **Save**. 3) **Redeploy** (push ou Redeploy depuis les Deployments). |
| **Prévention** | Pour tout nouveau projet Vercel lié à une app Next.js : ne pas définir Output Directory sur `public` ; laisser le framework Next.js gérer la sortie, ou fixer `outputDirectory` dans `vercel.json` à `.next`. |
| **Lien(s)** | `deploy/standalone-p4s/vercel.json`, `strategie-deploiement-git-vercel.md`, [Vercel missing public directory](https://vercel.link/missing-public-directory) |

---

### localhost:8000 inaccessible — ERR_CONNECTION_RESET / connexion réinitialisée

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 (enrichi 2025-02-04) |
| **Contexte** | Windows (ou WSL), accès à http://localhost:8010/admin/ (ou /, /essais/) après avoir lancé Docker ou runserver. Navigateur : « Ce site est inaccessible », « La connexion a été réinitialisée », **ERR_CONNECTION_RESET**. |
| **Erreur** | « Ce site est inaccessible », « La connexion a été réinitialisée », **ERR_CONNECTION_RESET** |
| **Cause** | (1) Conteneur `web` non démarré ou en crash (conflit Docker, Django qui plante au démarrage). (2) Sous Windows, le port forward Docker (8000) peut provoquer une connexion réinitialisée. (3) Résolution `localhost` (IPv6 vs IPv4) ou pare-feu. |
| **Solution** | **Diagnostic** : `docker ps` → vérifier que `lppp_web` est « Up ». Si absent ou « Restarting » : `docker compose logs web --tail 50` (erreur Django/Gunicorn ?). Corriger les conflits : `make clean-containers` puis `make start`. **Essai rapide** : en Docker LPPP utiliser **http://127.0.0.1:8010** (Django LPPP = lppp_web). En Option B runserver : 127.0.0.1:8000 ou 8080. **Si toujours ERR_CONNECTION_RESET** : **Option B (runserver local)** : 1) `docker compose up -d db redis` (et `docker compose stop web` pour libérer le port). 2) Dans `.env` : `DB_HOST=localhost`, `REDIS_URL=redis://127.0.0.1:6379/0`, `CELERY_BROKER_URL=redis://127.0.0.1:6379/1`. 3) Venv : `pip install -r requirements.txt`, `python3 manage.py migrate --noinput`, `python3 manage.py runserver 127.0.0.1:8080` (WSL : **python3**). 4) Ouvrir **http://127.0.0.1:8080/admin/** (ou /essais/). |
| **Prévention** | Sous Windows : privilégier Option B pour le dev (runserver sur 8080). Sous WSL : Docker LPPP = **lppp_web sur 8010** (jamais 8000, réservé SquidResearch) ; en cas de reset, tester 127.0.0.1:8010 puis Option B. |
| **Lien(s)** | `pret-a-demarrer.md` § 5.2, `demarrage-projet-equipe-tech.md`, entrée « Admin Django — impossible de se connecter » |

---

### Django inaccessible — problème réseau (sprint Architecte / DevOps / Pentester)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Impossible d’accéder à l’admin Django ni à Django en général ; problème réseau, aucune différence entre admin et reste du site. SquidResearch est prioritaire : on ne touche pas à sa stack. |
| **Erreur** | Site inaccessible (timeout, connexion refusée, reset), admin et pages Django inaccessibles. |
| **Cause** | Plusieurs causes possibles : (1) Conflit de ports si SquidResearch occupe 8000 (ou 3000, 5432) ; (2) Conteneur `lppp_web` non démarré ou en crash ; (3) Sous Windows : port forward Docker 8000 (ERR_CONNECTION_RESET) ; (4) localhost vs 127.0.0.1 (IPv6/IPv4). |
| **Solution** | **Sprint multi-agents** : suivre `segmentations/2026-01-30-sprint-resolution-reseau-django.md`. **Architecte réseau** : consulter le log commun SquidResearch (`log-commun-lppp-squidresearch.md`), identifier conflits de ports, recommander port alternatif LPPP (ex. 8001) si 8000 est pris. **DevOps** : `docker ps` → état `lppp_web` ; `make clean-containers` (conteneurs LPPP uniquement) puis `make start` ; tester http://127.0.0.1:8010 (Django LPPP) ; sinon Option B runserver (voir entrée « localhost:8000 inaccessible »). **Pentester** : vérifier ALLOWED_HOSTS et politique sécurité après toute modification. |
| **Prévention** | Consulter le log commun avant de lancer les deux stacks ; documenter le port Django LPPP si différent de 8000 ; sous Windows privilégier Option B (runserver 8080) si Docker 8000 pose problème. |
| **Lien(s)** | `segmentations/2026-01-30-sprint-resolution-reseau-django.md`, `log-commun-lppp-squidresearch.md`, `infra-devops.md` § 1 et § 3.4, entrée « localhost:8000 inaccessible » ci-dessus |

---

### « LPPP n'a pas son propre Django » — vérifier stack autonome (lppp_web sur 8010)

| Champ | Contenu |
|-------|---------|
| **Contexte** | LPPP doit utiliser **uniquement** sa propre stack : **lppp_web** (Django) sur port **8010**, jamais le port 8000 (SquidResearch). Si la doc ou la config laisse penser le contraire, ou si l'accès se fait encore sur 8000, corriger. |
| **Checklist** | (1) **docker-compose.yml** : service `web` doit avoir `ports: - "8010:8000"` (hôte:conteneur). (2) **README.md**, **pret-a-demarrer.md** : URLs Django = localhost:8010 (Option A Docker). (3) **Makefile** : `services-urls` affiche 8010. (4) Aucune URL dans .env ou le code LPPP ne pointe vers 8000, 5679, 3001 (SquidResearch). (5) Après modification du port : `docker compose up -d --force-recreate web` puis tester http://localhost:8010/. |
| **Prévention** | Toute nouvelle doc ou procédure qui mentionne « Django » pour LPPP en Docker doit indiquer le port **8010** et le conteneur **lppp_web**. Réf. `log-commun-lppp-squidresearch.md` § 5.3, `avis-et-solutions-routage-lppp-reference.md`. |

---

### GitLab désynchronisé — push oublié sur un remote

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Après `git push origin main` ; ou vérification des deux remotes (GitHub + GitLab) |
| **Erreur** | GitLab ne contient pas les derniers commits ; ou « on galère entre GitHub, GitLab et Vercel » (miroir incomplet). |
| **Cause** | Push effectué seulement sur `origin` (GitHub), pas sur `gitlab`. Vercel peut être lié à GitHub ; GitLab sert de backup/miroir — s’il n’est pas poussé, le miroir est faux. |
| **Solution** | Après chaque push sur `origin` : `git push gitlab main`. Si le remote `gitlab` n’existe pas : `git remote add gitlab git@gitlab.com:LucasTymen/<repo>.git` puis `git push -u gitlab main`. Utiliser `make push-both` (LPPP) si configuré, ou exécuter les deux pushes à la suite. |
| **Prévention** | Toujours pousser sur **les deux** remotes (origin + gitlab) après un commit. Checklist : `strategie-deploiement-git-vercel.md` (étape 3 : push origin puis push gitlab). Scripts type `push-standalone-p4s.sh` font les deux ; en manuel, ne pas oublier le second push. |
| **Lien(s)** | `git-remotes-github-gitlab.md`, `strategie-deploiement-git-vercel.md`, `pilotage-agents.mdc` (Git — commit + push sur les deux remotes) |

---

### Repo GitHub/GitLab créé avec README — conflit au premier push

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Premier push vers un repo fraîchement créé (GitHub ou GitLab) |
| **Erreur** | `! [rejected] main -> main (non-fast-forward)` ou refus de push car les historiques divergent (repo distant a un commit README, local a un autre premier commit). |
| **Cause** | Le repo a été créé avec « Initialize with README » (ou .gitignore / license), donc il a déjà un commit ; le dépôt local a un autre premier commit → deux historiques différents. |
| **Solution** | Option A : recréer le repo **sans** README, sans .gitignore, sans license, puis refaire `git push -u origin main` (et idem pour GitLab). Option B (si on ne peut pas recréer) : `git pull origin main --allow-unrelated-histories`, résoudre les conflits si besoin, puis `git push origin main`. Préférer Option A pour garder un historique propre. |
| **Prévention** | Toujours créer les repos **Create blank repository** / **Create blank project** **sans** cocher « Add README », « Add .gitignore », « Add license ». Voir `strategie-deploiement-git-vercel.md` (étape 1) et `git-remotes-github-gitlab.md`. |
| **Lien(s)** | `git-remotes-github-gitlab.md` § 6, `strategie-deploiement-git-vercel.md` (Pièges à éviter) |

---

### Vercel — Build Failed : Vulnerable version of Next.js (CVE-2025-66478)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Déploiement Vercel (LPPP_Ackuracy, LPPP_P4S-Architecture) ; build échoue avec message « Vulnerable version of Next.js detected, please update immediately ». |
| **Erreur** | Build Failed ; CVE-2025-66478 (React2Shell) — Next.js 15.0.0 à 16.0.6 affectés. |
| **Cause** | `next@15.1.3` (et versions similaires) dans `package.json` est vulnérable. |
| **Solution** | Mettre à jour Next.js vers une **version corrigée** : pour la branche 15.1.x utiliser **15.1.9** (`"next": "15.1.9"` dans package.json). Mettre à jour dans : `deploy/standalone-ackuracy/package.json`, `deploy/standalone-p4s/package.json`, `frontend/package.json`. Puis **commit + push** sur les repos concernés (ACKURACY, P4S) pour déclencher un nouveau build Vercel. |
| **Prévention** | Vérifier régulièrement [Next.js Security](https://nextjs.org/blog/CVE-2025-66478) et les alertes Vercel ; figer une version patchée (ex. 15.1.9) dans les package.json. |
| **Lien(s)** | [Next.js CVE-2025-66478](https://nextjs.org/blog/CVE-2025-66478), [Vercel CVE-2025-55182](https://vercel.com/changelog/cve-2025-55182) |

---

### Scripts bash push standalone — erreur CRLF ($'\r': command not found)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | WSL ou Git Bash, exécution de `bash deploy/push-standalone-p4s.sh` ou `bash deploy/push-standalone-ackuracy.sh` |
| **Erreur** | `$'\r': command not found`, `set: -: invalid option`, `cd: $'deploy/..\r': No such file or directory`, `fatal: remote error: is not a valid repository name`, `fatal: invalid refspec 'main?'`, `syntax error: unexpected end of file` |
| **Cause** | Fins de ligne **CRLF** (Windows) dans les fichiers `.sh` ; bash interprète le `\r` comme caractère, ce qui casse les commandes et les variables (REPO_DIR, refspec `main`). |
| **Solution** | 1) Convertir les scripts en **LF uniquement** : sous PowerShell `[System.IO.File]::ReadAllText("deploy\push-standalone-p4s.sh") -replace "`r`n", "`n" -replace "`r", "`n"` puis `WriteAllText` ; ou sous WSL `sed -i 's/\r$//' deploy/push-standalone-p4s.sh deploy/push-standalone-ackuracy.sh`. 2) `.gitattributes` avec `deploy/*.sh text eol=lf` pour que Git conserve le LF à l’avenir. |
| **Prévention** | Ne pas éditer les `.sh` avec un éditeur qui force le CRLF ; laisser `.gitattributes` gérer `eol=lf` pour `deploy/*.sh`. Après correction, les scripts s’exécutent correctement (push P4S et ACKURACY vers GitHub + GitLab, Vercel rebuild). |
| **Lien(s)** | `deploy/README-standalone.md`, `deploy/push-standalone-p4s.sh`, `deploy/push-standalone-ackuracy.sh` |

---

---

### Push GitHub/GitLab — authentification échouée (Windows / agent)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Déploiement P4S (ou autre standalone) : clone + copie + commit OK ; `git push origin main` échoue (PowerShell, Cursor, CI sans credentials). |
| **Erreur** | `Invalid username or token. Password authentication is not supported` (HTTPS) ou `Host key verification failed` (SSH). |
| **Cause** | GitHub n’accepte plus les mots de passe ; le terminal/agent n’a pas de PAT (Personal Access Token) ni de clé SSH configurée. |
| **Solution** | **Étape manuelle** : ouvrir un terminal où vous êtes déjà authentifié (Git Bash, GitHub Desktop, ou PowerShell après `gh auth login` / config SSH), puis `cd deploy/repo-p4s` (ou le repo concerné), `git push -u origin main`, puis `git push gitlab main`. Alternative : exécuter `.\deploy\push-standalone-p4s.ps1` (clone + commit), puis faire le push à la main depuis `deploy/repo-p4s`. |
| **Prévention** | Configurer un PAT (GitHub → Settings → Developer settings → Personal access tokens) pour HTTPS, ou SSH (clés + `ssh-add`), puis utiliser ce terminal pour le push final. |
| **Lien(s)** | `deploy/README-standalone.md`, `deploy/push-standalone-p4s.ps1` |

---

### CTA / Gmail sur landing statique — mailto: n’ouvre rien (Windows)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Landing P4S déployée en statique (Vercel) ; clic sur « Me contacter », CTA « Reprendre la conversation » ou lien Gmail. |
| **Erreur** | Rien ne se passe, ou message Windows « Ce fichier ne contient pas d’application associée » (pas de client mail par défaut pour `mailto:`). |
| **Cause** | Lien `mailto:` dépend du client mail configuré sur la machine du visiteur ; sous Windows sans client associé, le lien échoue. CTA et Gmail « en dur » ne déclenchaient aucune action. |
| **Solution** | **Popup (modal) contact** : tous les liens « Me contacter », CTA hero, CTA final et ligne Gmail ouvrent un **popup** (modal CSS `:target`) avec le texte : « Vous pouvez me contacter par Mail à cette adresse : [email] ». L’email est affiché en dur (sélectionnable/copiable). Fermeture par lien « Fermer » ou clic sur l’overlay. Aucun JavaScript ; compatible page statique. Template : `templates/landing_pages/proposition.html` (`.contact-modal`, `#contact-email-modal`). |
| **Prévention** | Sur les landings statiques (export Django → HTML), ne pas compter sur `mailto:` seul : proposer systématiquement le popup avec l’adresse en clair pour que le visiteur puisse copier. Tenir compte de cette contrainte dans tout nouveau template ou export. |
| **Lien(s)** | `deploy/PUSH-POUR-VERSION-COMPLETE.md`, `templates/landing_pages/proposition.html` |

---

### localhost:3010 — Flowise LPPP (pas aux landings Next.js)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Indication d’ouvrir une landing Next.js (ex. Ackuracy) sur http://localhost:3000. |
| **Erreur** | Confusion : le port 3000 est celui de **Flowise**, pas des apps Next.js standalone. |
| **Cause** | Next.js utilise 3000 par défaut ; dans LPPP, 3000 est attribué à Flowise. |
| **Solution** | Landings Next.js en local : **port 3001**. Ex. `cd deploy/standalone-ackuracy && npm run dev` → http://localhost:3001. Le script `dev` est configuré avec `-p 3001` dans `package.json`. Référence ports : `infra-devops.md` § 3.4. |
| **Prévention** | Ne jamais indiquer localhost:3010 pour une landing Next.js (3010 = Flowise LPPP) ; consulter `infra-devops.md` § 3.4 Ports avant de documenter ou proposer une URL de dev. |
| **Lien(s)** | `docs/base-de-connaissances/infra-devops.md` (§ 3.4), `deploy/standalone-ackuracy/README.md` |

---

---

### Fiche entretien emploi — section « Tests techniques » oubliée

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-05 |
| **Contexte** | Génération d'une fiche de préparation d'entretien (Assistant Entretien Emploi) pour une entreprise (ex. 0Flow). |
| **Erreur** | La section **Tests techniques** (programmation, growth, marketing, mix dev/growth) est absente de la fiche générée. L'utilisateur ne sait pas à l'avance si l'entretien sera orienté dev, marketing ou mix ; cette section est indispensable pour se préparer à tous les cas. |
| **Cause** | Le modèle canonique n'a pas été appliqué en entier : la section « 2. PROGRAMMATION – Questions techniques » du modèle (avec sous-parties programmation, growth, marketing, mix) a été omise lors de la génération. |
| **Solution** | Réintégrer la section complète depuis `_modele-canonique_prepa_entretien.html` (accordéon « TESTS TECHNIQUES — Programmation & Growth » et tout son contenu), puis renuméroter les sections suivantes (Questions à poser, Entreprise — Ce que vous devez savoir). |
| **Prévention** | **Toujours générer la fiche à partir du modèle canonique COMPLET** dès la première livraison. Inclure **toutes** les sections : 0 Présentation, 1 Formalités, 2 Q/R stratégiques, **3 Tests techniques** (programmation, growth, marketing, mix), 4 Questions à poser, 5 [Entreprise] — Ce que vous devez savoir. Inclure **tous** les textes, lexique, abréviations (KPI, CPA, CPL, CTA, etc.), questions à poser et tout ce qui peut être utile. Consulter `fiches-entretien-emploi-modele-et-veille.md` et la règle `assistant-entretien-emploi.mdc` ; l'Assistant Entretien Emploi doit s'assurer que le modèle canonique est copié en entier (structure + contenu type) avant d'adapter au cas par cas. |
| **Lien(s)** | `.cursor/rules/assistant-entretien-emploi.mdc`, `fiches-entretien-emploi-modele-et-veille.md`, `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html` |

---

*Dernière mise à jour : 2026-02-05 — Fiche entretien : section tests techniques obligatoire. Précédent : Port 3000 = Flowise. Stratégie fluide : `strategie-deploiement-git-vercel.md`.*
