# Sprint — Écran blanc landing chatbot Conciergerie (/p/maisons-alfort/)

**Date** : 2026-01-30  
**Statut** : 🟡 En cours  
**Objectif** : Corriger l’écran blanc sur la landing Conciergerie Maisons-Alfort, rendre la page intégrée et stylisée, et s’assurer que le chatbot est fonctionnel. **Coordination multi-agents** : Architecte (structure, intégration), DevOps (infra, Flowise, ports), Dev Django (vue, template, contexte), Designer (stylisation), Automatizer (Flowise embed).

**Règle** : ne pas rester seul — faire intervenir tous les agents concernés (voir registre, `agents-roles-responsabilites.md`).

---

## Problème

Sur **/p/maisons-alfort/** (ou **/maisons-alfort/** après redirection), l’utilisateur constate un **écran blanc** : la page ne s’affiche pas ou le contenu n’est pas visible.

**Causes possibles** (à vérifier par chaque rôle) :
- **Dev Django** : vue qui lève une exception, template manquant ou mal nommé, contexte incomplet, URL incorrecte.
- **DevOps** : Django non servi sur l’URL attendue, reverse proxy ou port, Flowise non exposé sur 3000, `.env` manquant (FLOWISE_CHATFLOW_ID, FLOWISE_URL).
- **Architecte** : chaîne d’intégration (route → vue → template → embed) incohérente ; ordre des includes dans `lppp/urls.py` ou `apps/landing_pages/urls.py`.
- **Designer** : styles qui masquent le contenu (couleur de fond blanche, texte blanc sur blanc, z-index, overflow hidden).
- **Automatizer** : Flowise ne répond pas sur `/embed/{id}`, chatflow absent ou ID incorrect ; CORS / X-Frame-Options si iframe bloquée.

---

## Tâches par agent

### Architecte (structure, intégration)
- [ ] Vérifier la **chaîne d’intégration** : `lppp/urls.py` → `apps.landing_pages.urls` → `path("p/<slug:slug>/", landing_public)` ; pas de conflit avec une autre route qui capturerait l’URL.
- [ ] Confirmer que la **LandingPage** avec `slug=maisons-alfort` et `template_key=concierge_maisons_alfort` existe en base (migration `0004_add_conciergerie_maisons_alfort_landing` appliquée).
- [ ] S’assurer que le template `landing_pages/concierge_maisons_alfort.html` est bien le rendu utilisé (pas d’extends cassé, pas de block manquant).

### DevOps (infra, Flowise, .env)
- [ ] Vérifier que le service **Django** répond sur l’URL utilisée (ex. http://127.0.0.1:8000 ou 8080) : `curl -I http://127.0.0.1:8000/p/maisons-alfort/` → 200.
- [ ] Vérifier que **Flowise** est démarré et exposé sur le port **3000** : `docker compose ps` (ou processus local), `curl -s -o /dev/null -w "%{http_code}" http://localhost:3000`.
- [ ] Vérifier le **.env** (local, non versionné) : `FLOWISE_CHATFLOW_ID` renseigné (ID du chatflow Conciergerie, onglet Embed dans Flowise) ; optionnel `FLOWISE_URL=http://localhost:3000` si runserver sur l’hôte. Rappel : en local runserver, l’URL d’embed doit être joignable par le **navigateur** (localhost:3000). Voir `infra-devops.md` § 3.4, `flowise-concierge-ia-maisons-alfort-guide.md`.
- [ ] Documenter dans `erreurs-et-solutions.md` toute cause infra identifiée (écran blanc lié à Flowise down, port, .env).

### Dev Django (vue, template, contexte)
- [ ] S’assurer que **landing_public** reçoit bien `slug=maisons-alfort` et que **get_object_or_404(LandingPage, slug=slug)** trouve la page (sinon 404).
- [ ] Pour le template **concierge_maisons_alfort** : passer **flowise_embed_url** dans le contexte (déjà fait si `lp.template_key == "concierge_maisons_alfort"`). Ne jamais passer `None` : utiliser `""` si pas d’URL pour afficher le placeholder « Chat en cours de configuration ».
- [ ] Vérifier que le **template** affiche toujours au moins la structure visible (hero, intro, zone chat ou placeholder) : pas de body vide, pas de CSS qui cache tout le contenu. Renforcer si besoin : fond sombre par défaut, message explicite si `flowise_embed_url` vide.
- [ ] Tester en local : runserver + Flowise sur 3000, ouvrir /p/maisons-alfort/ → la page doit afficher le hero, l’intro et l’iframe (ou le placeholder).

### Designer (stylisation)
- [ ] Vérifier les **styles** du template `concierge_maisons_alfort.html` : pas de `color: white` sur fond blanc, pas de `opacity: 0` ou `visibility: hidden` sur le contenu principal. Contraste suffisant (texte lisible sur fond sombre).
- [ ] S’assurer que la **zone chat** (iframe ou placeholder) est visible : dimensions (min-height, height iframe), pas de overflow caché. Si l’iframe est blanche (Flowise ne charge pas), le reste de la page (hero, intro) doit rester visible.
- [ ] Proposer si besoin des ajustements (espacement, typo, états « chat indisponible ») pour une UX claire.

### Automatizer (Flowise, embed)
- [ ] Confirmer que le **chatflow** Conciergerie Maisons-Alfort est bien déployé dans Flowise et que l’**ID** (onglet Embed) correspond à `FLOWISE_CHATFLOW_ID` dans `.env`.
- [ ] Vérifier que **http://localhost:3000/embed/{FLOWISE_CHATFLOW_ID}** répond (200) et affiche le chat dans le navigateur (pas de CORS bloquant l’iframe si même origine ou Flowise autorise le frame).
- [ ] En cas d’iframe blanche : vérifier les logs Flowise, configuration CORS / X-Frame-Options si documentée.

### Chef de Projet
- [ ] Valider que **/p/maisons-alfort/** affiche une page lisible (hero + intro + chat ou placeholder), sans écran blanc.
- [ ] Mettre à jour ce sprint (statut 🟢 Terminé) et `docs/logs/log-projet.md` une fois la validation OK.
- [ ] S’assurer que `erreurs-et-solutions.md` contient l’entrée « Écran blanc landing chatbot » avec le diagnostic et les solutions par rôle.

---

## Critères de succès

- [ ] Ouvrir **http://127.0.0.1:8000/p/maisons-alfort/** (ou l’URL Django utilisée) : la page affiche **au minimum** le hero, l’intro et soit l’iframe du chat soit le message « Chat en cours de configuration » — **jamais d’écran entièrement blanc**.
- [ ] Si Flowise est démarré et `FLOWISE_CHATFLOW_ID` est correct : l’iframe charge le chatbot et l’utilisateur peut échanger.
- [ ] Styles cohérents, contraste et lisibilité validés par le Designer.

---

## Références

- **Registre** : `registre-agents-ressources.md` (rôles Architecte, DevOps, Dev Django, Designer, Automatizer).
- **Erreurs** : `erreurs-et-solutions.md` (entrée « Écran blanc landing chatbot » ; « Impossible de trouver l’adresse IP du serveur de flowise »).
- **Code** : `apps/landing_pages/views.py` (landing_public), `apps/scraping/flowise_client.py` (get_flowise_chat_embed_url), `templates/landing_pages/concierge_maisons_alfort.html`.
- **Infra** : `infra-devops.md` § 3.4 (ports Flowise 3000), `flowise-concierge-ia-maisons-alfort-guide.md`, `conciergerie-maisons-alfort-architecture-et-onboarding.md`.
