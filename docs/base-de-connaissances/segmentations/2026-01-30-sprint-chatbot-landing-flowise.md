# Sprint — Chatbot Flowise sur la landing LPPP (/maisons-alfort/)

**Date** : 2026-01-30  
**Statut** : 🟡 En cours  
**Objectif** : Faire fonctionner le chatbot Flowise sur la page publique `/maisons-alfort/` (et /essais/concierge/) — résolution IP / URL d'embed, validation multi-agents.

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both`). Réf. `git-remotes-github-gitlab.md`.

---

## Problème

Sur **http://127.0.0.1:8082/maisons-alfort/** (runserver sur l'hôte), l'iframe du chatbot affiche :  
**« Impossible de trouver l'adresse IP du serveur de flowise »**.

**Cause** : L'URL d'embed générée pointait vers `http://flowise:3000`. Le nom `flowise` n'est résolu que dans le réseau Docker ; le **navigateur** (sur l'hôte) ne peut pas le résoudre.

---

## Correctif appliqué (Dev Django)

- **Fichier** : `apps/scraping/flowise_client.py` — `get_flowise_chat_embed_url()`.
- **Logique** : Si `FLOWISE_URL` n'est pas défini et que `DB_HOST` est `localhost` ou `127.0.0.1`, l'URL d'embed par défaut est **http://localhost:3000** (accessible par le navigateur). Sinon `http://flowise:3000` (contexte Docker).
- **Override** : `FLOWISE_URL` et `FLOWISE_CHATFLOW_ID` dans `.env` restent prioritaires.

---

## Tâches par agent (sprint)

### Dev Django
- [x] Adapter `get_flowise_chat_embed_url()` pour URL navigateur (localhost quand runserver sur l'hôte).
- [ ] Vérifier que le template `concierge_maisons_alfort.html` reçoit bien `flowise_embed_url` et affiche l'iframe.
- [ ] Tester en local : runserver 127.0.0.1:8082, DB_HOST=localhost, Flowise sur 3000 → ouvrir /maisons-alfort/ et confirmer que le chat s'affiche.

### DevOps
- [ ] Vérifier que le service **flowise** est exposé sur le port **3000** (`docker compose ps`, `docker compose up -d flowise`).
- [ ] Documenter dans `infra-devops.md` ou `.env.example` : en dev runserver sur l'hôte, Flowise doit être joignable sur **localhost:3000** (exposition du port du conteneur flowise).
- [ ] Si besoin : rappeler la procédure Option B (db + redis + runserver) et que Flowise reste dans Docker sur 3000.

### Automatizer (Flowise / n8n)
- [ ] Confirmer que le chatflow Concierge Maisons-Alfort (ID par défaut dans le code) est bien déployé et répond sur `/embed/{id}`.
- [ ] En cas d'erreur CORS ou de refus d'iframe : vérifier la config Flowise (exposition, CORS si doc Flowise le mentionne).

### Chef de Projet
- [ ] Valider que la page /maisons-alfort/ affiche le chatbot sans message d'erreur IP.
- [ ] Mettre à jour `docs/logs/log-projet.md` et ce sprint (statut 🟢 Terminé) une fois la validation OK.
- [ ] S'assurer que `erreurs-et-solutions.md` et `flowise-concierge-ia-maisons-alfort-guide.md` sont à jour (fait : entrée « Impossible de trouver l'adresse IP », § Dépannage).

---

## Critères de succès

- [ ] Ouvrir **http://127.0.0.1:8082/maisons-alfort/** (avec runserver + Flowise sur 3000) : l'iframe charge le chat Flowise, pas d'erreur « adresse IP du serveur de flowise ».
- [ ] Optionnel : même test avec tout le stack en Docker (web + flowise) en s'assurant que l'URL d'embed reste joignable par le navigateur (ex. FLOWISE_URL=http://localhost:3000 si Flowise exposé sur l'hôte).

---

## Références

- **Erreur** : `docs/base-de-connaissances/erreurs-et-solutions.md` § « Landing /maisons-alfort/ — Impossible de trouver l'adresse IP du serveur de flowise ».
- **Écran blanc** : si la page affiche un écran blanc, suivre le sprint **`segmentations/2026-01-30-sprint-ecran-blanc-landing-chatbot.md`** (Architecte, DevOps, Dev Django, Designer, Automatizer).
- **Guide Flowise** : `flowise-concierge-ia-maisons-alfort-guide.md` (§ Dépannage rapide).
- **Code** : `apps/scraping/flowise_client.py` (`get_flowise_chat_embed_url`), `apps/landing_pages/views.py` (`landing_public`, template_key concierge_maisons_alfort), `templates/landing_pages/concierge_maisons_alfort.html`.
- **Registre** : `registre-agents-ressources.md` (rôles Dev Django, DevOps, Automatizer, Chef de Projet).
