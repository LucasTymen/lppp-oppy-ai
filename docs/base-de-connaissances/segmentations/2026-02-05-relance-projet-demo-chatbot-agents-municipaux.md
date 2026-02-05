# Sprint — Relance projet pour démo + Chatbot Flowise/n8n opérationnel (LPP agents municipaux)

**Date** : 2026-02-05  
**Statut** : 🟡 En cours  
**Objectif** : (1) Relancer le projet LPPP pour une **démonstration** ; (2) **Solutionner l’intégration Flowise/n8n** pour que le **chatbot soit opérationnel** sur la landing des agents municipaux (Conciergerie Maisons-Alfort — `/maisons-alfort/` ou `/p/maisons-alfort/`).

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both` ou `make commit-push MSG="..."`). Réf. `git-remotes-github-gitlab.md`.

**Log commun** : Toute décision touchant Docker, ports ou .env doit s’appuyer sur `log-commun-lppp-squidresearch.md` (pointeur) ; **SquidResearch a la priorité** ; ne modifier que les conteneurs **lppp_***.

---

## Contexte

- **Démo** : le projet doit être relançable et présentable (stack disponible, page agents municipaux avec chatbot visible).
- **Chatbot LPP agents municipaux** : la page publique Conciergerie Maisons-Alfort doit afficher le chatbot Flowise (iframe) et, en amont, la chaîne n8n → scrape → push Flowise doit être opérationnelle pour alimenter le RAG.

---

## Partie 1 — Relance projet (démo)

### DevOps
- [ ] **Vérifier le .env** : présent à la racine (copie depuis `.env.example` si absent) ; pas de conflit avec SquidResearch (ne pas toucher au .env SquidResearch). Réf. `log-commun-lppp-squidresearch.md`.
- [ ] **Relancer le stack LPPP** : depuis la racine LPPP (WSL) — `make ensure-env` puis `make up` (ou `make start` pour démarrage séquentiel + migrations). En cas de conflit de conteneurs : `make clean-containers` puis `make start`. **Ne supprimer que les conteneurs lppp_***.
- [ ] **Vérifier les services** : `make health-check` ou `make services-urls` ; Django (8000), n8n (5678), Flowise (3000) accessibles. Documenter dans `infra-devops.md` ou `erreurs-et-solutions.md` toute anomalie.
- [ ] **Option démo sans tout Docker** : si démo en runserver sur l’hôte : lancer uniquement `db` et `redis` + **flowise** (`docker compose up -d db redis flowise`), exposer Flowise sur **3000** ; dans `.env` : `DB_HOST=localhost`, `FLOWISE_URL=http://localhost:3000` ; runserver sur 127.0.0.1:8082. Réf. `pret-a-demarrer.md` § Option B, `flowise-concierge-ia-maisons-alfort-guide.md`.

### Chef de Projet
- [ ] Valider que la **démo** est possible : au moins une URL (ex. http://127.0.0.1:8000/ ou 8082) affiche l’app ; admin et landing accessibles.
- [ ] Mettre à jour `docs/logs/log-projet.md` et ce sprint après validation.

---

## Partie 2 — Intégration Flowise/n8n — Chatbot opérationnel sur la LPP agents municipaux

La landing **agents municipaux** = **Conciergerie Maisons-Alfort** : routes `/maisons-alfort/` (redirection) et `/p/maisons-alfort/`, template `concierge_maisons_alfort.html`, chatbot en iframe (Flowise).

### DevOps
- [ ] **Flowise** : service **lppp_flowise** démarré, exposé sur le port **3000** (`docker compose ps` ; `curl -s -o /dev/null -w "%{http_code}" http://localhost:3000` → 200 ou 302).
- [ ] **.env** : `FLOWISE_CHATFLOW_ID` = ID du chatflow Conciergerie (onglet Embed dans Flowise) ; `FLOWISE_URL=http://localhost:3000` si le **navigateur** doit charger l’iframe (runserver sur l’hôte). Réf. `flowise-concierge-ia-maisons-alfort-guide.md`.
- [ ] Documenter toute cause infra (écran blanc, « Impossible de trouver l’adresse IP du serveur de flowise ») dans `erreurs-et-solutions.md`.

### Automatizer (Flowise / n8n)
- [ ] **Chatflow Flowise** : Conciergerie Maisons-Alfort déployé ; **ID Embed** cohérent avec `FLOWISE_CHATFLOW_ID` dans `.env`. Vérifier que `http://localhost:3000/embed/{ID}` répond et affiche le chat (CORS / X-Frame-Options si iframe bloquée).
- [ ] **n8n** : workflow **Concierge IA – Aspiration Maisons-Alfort** (`docs/n8n-workflows/concierge-ia-aspiration-maisons-alfort.json`) importé et exécutable ; chaîne scrape → save-content → push-to-flowise opérationnelle. Réf. `guide-equipe-scraper-n8n-flowise.md`, `workflow-complet-concierge-maisons-alfort.md`.
- [ ] **Document Store Flowise** : alimenté (au moins une ingestion) pour que le RAG réponde avec le contenu Maisons-Alfort.

### Dev Django
- [ ] **URL d’embed** : `get_flowise_chat_embed_url()` (`apps/scraping/flowise_client.py`) renvoie une URL joignable par le **navigateur** (ex. `http://localhost:3000` quand runserver sur l’hôte, pas `http://flowise:3000`). Déjà corrigé si `DB_HOST=localhost` et `FLOWISE_URL` non défini → défaut localhost:3000. Réf. sprint `2026-01-30-sprint-chatbot-landing-flowise.md`.
- [ ] **Vue / template** : `landing_public` avec `slug=maisons-alfort` et `template_key=concierge_maisons_alfort` ; contexte `flowise_embed_url` passé au template ; pas de `None` (utiliser `""` et afficher « Chat en cours de configuration » si vide).
- [ ] **Test** : runserver (ou stack Docker) + Flowise sur 3000 → ouvrir `/p/maisons-alfort/` ou `/maisons-alfort/` → page visible (hero, intro, iframe ou placeholder), **pas d’écran blanc**.

### Architecte
- [ ] **Chaîne d’intégration** : `lppp/urls.py` → `apps.landing_pages.urls` → `path("p/<slug:slug>/", landing_public)` ; landing `maisons-alfort` avec `template_key=concierge_maisons_alfort` en base (migration `0004_add_conciergerie_maisons_alfort_landing` appliquée).
- [ ] Template `landing_pages/concierge_maisons_alfort.html` utilisé ; pas d’extends cassé ni de block manquant.

### Designer
- [ ] **Styles** : pas d’écran blanc (pas de `color: white` sur fond blanc, pas d’opacité 0 sur le contenu) ; zone chat (iframe ou placeholder) visible ; contraste et lisibilité. Réf. sprint `2026-01-30-sprint-ecran-blanc-landing-chatbot.md`.

### Chef de Projet
- [ ] Valider que **/p/maisons-alfort/** (ou **/maisons-alfort/**) affiche une page lisible (hero + intro + chatbot ou « Chat en cours de configuration »), **sans écran blanc** et **sans erreur « adresse IP du serveur de flowise »**.
- [ ] Si Flowise et `FLOWISE_CHATFLOW_ID` sont OK : valider que l’utilisateur peut **échanger** dans le chat.
- [ ] Mettre à jour les sprints `2026-01-30-sprint-chatbot-landing-flowise.md` et `2026-01-30-sprint-ecran-blanc-landing-chatbot.md` (statut 🟢 si résolu) et `docs/logs/log-projet.md`.
- [ ] S’assurer que `erreurs-et-solutions.md` et `flowise-concierge-ia-maisons-alfort-guide.md` sont à jour.

---

## Critères de succès

### Relance (démo)
- [ ] Stack LPPP relançable (`make up` ou Option B) ; au moins une URL (Django) répond ; démo présentable.

### Chatbot LPP agents municipaux
- [ ] **http://127.0.0.1:8000/p/maisons-alfort/** (ou l’URL Django utilisée) affiche la page (hero, intro, iframe ou placeholder) — **jamais d’écran entièrement blanc**.
- [ ] **Pas d’erreur** « Impossible de trouver l’adresse IP du serveur de flowise » dans l’iframe.
- [ ] Si Flowise est démarré et `FLOWISE_CHATFLOW_ID` correct : **l’iframe charge le chatbot** et l’utilisateur peut poser des questions (RAG Maisons-Alfort).
- [ ] (Optionnel) Chaîne n8n (scrape → save → push Flowise) exécutée au moins une fois pour alimenter le Document Store.

---

## Références

- **Log commun** : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md`
- **Infra** : `infra-devops.md` (§ 1.1, § 3.4 ports), `pret-a-demarrer.md`, `strategie-operationnelle-make.md`
- **Flowise / chatbot** : `flowise-concierge-ia-maisons-alfort-guide.md`, `conciergerie-maisons-alfort-architecture-et-onboarding.md`, `workflow-complet-concierge-maisons-alfort.md`
- **n8n** : `guide-equipe-scraper-n8n-flowise.md`, `docs/n8n-workflows/concierge-ia-aspiration-maisons-alfort.json`
- **Sprints liés** : `2026-01-30-sprint-chatbot-landing-flowise.md`, `2026-01-30-sprint-ecran-blanc-landing-chatbot.md`
- **Erreurs** : `erreurs-et-solutions.md` (§ Landing /maisons-alfort/ — IP flowise ; § Écran blanc landing chatbot)
- **Code** : `apps/scraping/flowise_client.py`, `apps/landing_pages/views.py`, `templates/landing_pages/concierge_maisons_alfort.html`, `apps/landing_pages/urls.py`
- **Registre** : `registre-agents-ressources.md` (DevOps, Dev Django, Automatizer, Architecte, Designer, Chef de Projet)
