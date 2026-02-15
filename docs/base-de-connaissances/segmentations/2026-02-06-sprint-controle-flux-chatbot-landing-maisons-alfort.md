# Sprint — Contrôle des flux et affichage du chatbot (landing /p/maisons-alfort/)

**Date** : 2026-02-06  
**Statut** : 🟡 En cours  
**Objectif** : La page **n’est plus un écran blanc** (hero, intro, message de dépannage visibles) mais le **contenu du chatbot ne s’affiche toujours pas**. Ce sprint mobilise **DevOps, Architecte, Ingénieur système, Pentester** pour mettre en place des **stratégies et des tests de contrôle des flux**, afin d’identifier et corriger la cause (embed script, API Flowise, CORS, CSP, réseau).

**Règle** : coordination multi-rôles ; chaque rôle documente ses constats dans le registre erreurs ou ce document.

---

## Demande à tous les agents

**Deux questions sont posées à chaque rôle concerné :**

1. **Pourquoi ça ne marche pas ?** — Selon votre périmètre, quelle(s) cause(s) possible(s) identifiez-vous ? Qu’avez-vous déjà constaté ou vérifié ?
2. **Comment en finir et réussir à utiliser le chatbot complètement dans la landing ?** — Quelles actions concrètes proposez-vous pour que le chat s’affiche et réponde sur `/p/maisons-alfort/` ?

Chaque agent est invité à documenter sa réponse dans ce sprint (paragraphe « Diagnostic [Rôle] » ou « Réponse [Rôle] »), ou dans le document dédié : **`2026-02-06-demande-agents-chatbot-landing-pourquoi-comment.md`** (tableau par rôle + où répondre). Le Chef de Projet synthétisera les réponses pour dégager la cause racine et le plan d’action.

---

## Contexte et progrès

- **Avant** : écran entièrement blanc sur `/p/maisons-alfort/`.
- **Actuel** : la page s’affiche (titre, sous-titre, intro, zone chat avec message « Le cadre ci-dessus est vide ? » + lien « Ouvrir le chat dans un nouvel onglet ») — **la zone du chat reste vide** (pas de widget, pas d’iframe visible ou iframe/script sans contenu).
- **Cible** : le chatbot (Flowise) s’affiche et répond sur la landing.

**Flux à contrôler** :
1. **Navigateur** → **Django** (8010) : page HTML avec embed (script `flowise-embed` ou iframe).
2. **Navigateur** → **Flowise** (3010) : chargement du widget (script) ou iframe ; appels API (ex. `/api/v1/prediction/{chatflowId}`).
3. **Sécurité** : CORS, CSP, X-Frame-Options, pas d’exposition de secrets.

---

## Tâches par rôle

### DevOps (infra, ports, santé des services)

- [ ] **Vérifier que Flowise écoute sur 3010** : `docker compose ps` → `lppp_flowise` en état **Up** avec mapping **3010:3000** ; `curl -s -o /dev/null -w "%{http_code}" http://localhost:3010/` → **200** (ou 302 si redirect login).
- [ ] **Vérifier que le service web reçoit les variables d’embed** : `docker compose exec web python manage.py check_flowise_embed` ; l’URL d’embed doit contenir le bon `chatflowid` (ex. `67206a96-470e-4607-ba8b-5955e97aa116`). Si vide ou ancien ID → `.env` avec `FLOWISE_URL=http://localhost:3010` et `FLOWISE_CHATFLOW_ID=<id>` puis `docker compose restart web`.
- [ ] **Test de flux direct** : depuis l’hôte, `curl -X POST http://localhost:3010/api/v1/prediction/67206a96-470e-4607-ba8b-5955e97aa116 -H "Content-Type: application/json" -d '{"question":"test"}'` → réponse JSON (pas de connexion refusée, pas de 404). Documenter le résultat (OK / erreur) dans ce sprint ou `erreurs-et-solutions.md`.
- [ ] **Stratégie de contrôle** : ajouter si besoin une commande ou un script de santé « landing → Flowise » (ex. `make check-flowise-embed` déjà en place ; optionnel : test POST prediction) et le documenter dans `strategie-operationnelle-make.md` ou `flowise-chatbot-ecran-vide-diagnostic.md`.
- [ ] **Logs** : en cas d’erreur, relever `docker compose logs web` et `docker compose logs flowise` sur la plage concernée et les consigner (anonymisés si nécessaire).

**Livrable** : paragraphe « Diagnostic DevOps » dans ce document ou dans `flowise-chatbot-ecran-vide-diagnostic.md` (ports, env, curl prediction, conclusion).

---

### Architecte (chaîne d’intégration, points de défaillance)

- [ ] **Vérifier la chaîne complète** : `lppp/urls.py` → `landing_public` avec `slug=maisons-alfort` → template `concierge_maisons_alfort.html` ; contexte : `flowise_embed_url`, `flowise_api_host`, `flowise_chatflow_id` bien passés (vue `landing_public` et vue `concierge_maisons_alfort_public`). Vérifier qu’aucune autre route ne capture `/p/maisons-alfort/`.
- [ ] **Points de défaillance** : documenter dans ce sprint la liste des points où le flux peut casser (Django ne renvoie pas les variables, template n’injecte pas le script, script CDN bloqué, API Flowise injoignable depuis le navigateur, CORS, etc.) et indiquer pour chacun qui peut le vérifier (DevOps, Pentester, Dev Django).
- [ ] **Stratégie de test** : proposer un ordre de tests (1. page source → présence de `Chatbot.init` et `apiHost`/`chatflowid` ; 2. onglet Réseau → requêtes vers 3010 ; 3. console navigateur → erreurs CORS/CSP/script). Documenter dans `flowise-chatbot-ecran-vide-diagnostic.md` ou ce fichier.

**Livrable** : schéma ou liste « Flux landing → Flowise » + « Points de défaillance et qui teste quoi ».

---

### Ingénieur système (réseau, processus, observabilité)

- [ ] **Réseau** : depuis la machine hôte (où le navigateur tourne), confirmer que **localhost:3010** est bien joignable (ping TCP ou curl). Si le navigateur est sur une autre machine (ex. VM, autre poste), l’URL d’embed ne doit pas être `localhost` mais l’hôte ou le domaine accessible depuis ce navigateur — documenter la règle dans `flowise-faiss-base-path-infra.md` ou `infra-devops.md`.
- [ ] **Processus** : vérifier que les conteneurs `lppp_web` et `lppp_flowise` sont bien ceux utilisés (pas un autre stack sur les mêmes ports). `docker compose ps` et si besoin `docker compose logs flowise --tail 50` pour confirmer que Flowise répond aux requêtes.
- [ ] **Contrôle des flux** : proposer une checklist minimale « avant chaque démo ou livraison » : (1) Flowise up sur 3010, (2) `check_flowise_embed` OK, (3) ouverture de l’URL d’embed en direct dans le navigateur → chat visible. Documenter dans `strategie-operationnelle-make.md` ou dans ce sprint.

**Livrable** : paragraphe « Diagnostic système » (réseau, processus) + checklist de contrôle des flux (optionnel, à intégrer au Makefile ou à la doc).

---

### Pentester (sécurité des flux, tests non destructifs)

- [ ] **CORS / CSP** : vérifier si les en-têtes CORS de Flowise (3010) ou la Content-Security-Policy de la page Django bloquent le chargement du script `flowise-embed` ou les appels vers `localhost:3010`. Ouvrir la console navigateur (F12) sur `/p/maisons-alfort/` et relever les erreurs éventuelles (CORS, CSP, script blocked). Documenter le constat (blocage ou pas) et, si blocage, proposer une évolution de config (côté Flowise ou Django) sans dégrader la sécurité (whitelist explicite).
- [ ] **X-Frame-Options / iframe** : si l’embed utilisait une iframe et qu’elle est bloquée, le Pentester note si Flowise renvoie `X-Frame-Options: DENY` (ou équivalent) et propose une configuration autorisant le frame uniquement depuis l’origine de la landing (ex. same-origin ou liste de domaines). Tests **non destructifs** uniquement (pas de modification de prod sans accord).
- [ ] **Exposition de secrets** : s’assurer qu’aucun token, clé API ou `FLOWISE_CHATFLOW_ID` n’est exposé côté client au-delà de ce qui est nécessaire (l’ID du chatflow dans la page est acceptable ; pas de clé API dans le HTML/JS). Consulter `regles-securite.md` et `politique-credentials-securite-flux.md`.
- [ ] **Stratégie de contrôle** : rédiger une courte « fiche sécurité flux chatbot » (ce qui est autorisé, ce qui est bloqué, comment tester) et la référencer depuis `erreurs-et-solutions.md` ou ce sprint.

**Livrable** : paragraphe « Diagnostic Pentester » (CORS, CSP, X-Frame-Options, secrets) + fiche sécurité flux chatbot (lien ou section dans la base de connaissances).

---

### Chef de Projet

- [ ] Valider que les livrables des quatre rôles (DevOps, Architecte, Ingénieur système, Pentester) sont déposés ou documentés (dans ce sprint ou dans les docs référencées).
- [ ] Une fois la cause identifiée et corrigée : mettre à jour le **statut** de ce sprint (🟢 Terminé ou 🔴 Bloqué) et les logs (`log-projet.md`, `log-ia.md`).
- [ ] S’assurer que le **registre erreurs et solutions** (`erreurs-et-solutions.md`) contient une entrée décrivant la cause racine et la solution (ex. « Chatbot ne s’affiche pas sur la landing — CORS / script embed ») avec renvoi vers ce sprint et vers `flowise-chatbot-ecran-vide-diagnostic.md`.

---

## Critères de succès du sprint

- [ ] **Flux documentés** : chaîne « Landing → Flowise » et points de défaillance décrits (Architecte + DevOps).
- [ ] **Tests de contrôle exécutés** : au moins un test par rôle (DevOps : curl prediction ; Architecte : vérif contexte template ; Ingénieur système : réseau/processus ; Pentester : CORS/CSP/console).
- [ ] **Cause racine identifiée** : la raison pour laquelle le contenu du chat ne s’affiche pas est consignée (ex. script bloqué par CSP, API injoignable, mauvais ID).
- [ ] **Correctif appliqué ou planifié** : soit un correctif est déployé (config, template, .env), soit un ticket/plan est rédigé pour la suite.
- [ ] **Sécurité** : le Pentester a validé qu’aucun flux ni configuration proposée ne dégrade la sécurité (pas de secrets exposés, CORS/CSP maîtrisés).

---

## Références

- **Diagnostic chatbot** : `flowise-chatbot-ecran-vide-diagnostic.md`, `segmentations/2026-01-30-strategie-chatbot-ecran-vide-et-flux.md`
- **Résumé setup/config** : `chatbot-conciergerie-resume-probleme-setup-config.md`
- **Registre erreurs** : `erreurs-et-solutions.md`
- **Rôles** : `agents-roles-responsabilites.md`, `registre-agents-ressources.md`
- **Code** : `apps/landing_pages/views.py`, `apps/scraping/flowise_client.py`, `templates/landing_pages/concierge_maisons_alfort.html`
- **Infra / ports** : `infra-devops.md` § 3.4 (Flowise 3010), `log-commun-lppp-squidresearch.md`
