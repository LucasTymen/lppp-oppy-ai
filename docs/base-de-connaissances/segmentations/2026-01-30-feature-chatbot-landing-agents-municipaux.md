# Feature — Chatbot fonctionnel dans la landing Agents municipaux (Maisons-Alfort)

**Date** : 2026-01-30  
**Statut** : 🟡 En cours  
**Priorité** : Important (mécanisme réutilisable pour bots de scraping)

**Équipe** : Assistant (rédaction / coordination), **Architecte**, **Expert en automatisation (Automatizer)**, **Pentester**. Collaboration pour rendre le chatbot opérationnel dans la landing et définir des stratégies de test **non destructives**.

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both` ou `make commit-push MSG="..."`).

---

## 1. User Story

> En tant que **équipe municipale** (ou visiteur de la landing), je veux **utiliser le chatbot intégré** sur la page Assistant Ville de Maisons-Alfort pour poser des questions sur les démarches, horaires, déchets, état civil, et obtenir des réponses basées sur les contenus officiels (RAG), **afin de** valider le mécanisme d’embed Flowise et le réutiliser pour d’autres landings et pour mes propres bots de scraping.

**Contexte** :
- La landing **Agents municipaux** correspond à la page **Conciergerie IA Maisons-Alfort** : `/p/maisons-alfort/` (template `concierge_maisons_alfort.html`).
- Le chatbot est affiché via une **iframe** dont l’URL est construite par `get_flowise_chat_embed_url()` (Django) : `{FLOWISE_URL}/embed/{FLOWISE_CHATFLOW_ID}`.
- **Flowise LPPP** : port **3010** (stack autonome). Variables : `FLOWISE_URL=http://localhost:3010`, `FLOWISE_CHATFLOW_ID` = ID du chatflow Conciergerie dans Flowise.
- Ce mécanisme (embed + chatflow + RAG) doit rester **stable et reproductible** pour servir aussi à créer d’autres bots (ex. scraping, autres landings).

---

## 2. Objectifs

- **Rendre le chatbot visible et fonctionnel** dans la landing `/p/maisons-alfort/` (iframe qui charge le chatflow Flowise).
- **Tester et agencer des stratégies non destructives** : pas de reset des chatflows, pas de suppression des volumes Flowise/FAISS, pas de modification des credentials sans traçabilité.
- **Documenter** le flux (Django → Flowise → embed) et les points de défaillance possibles pour que l’Architecte, l’Automatizer et le Pentester puissent intervenir sans casser l’existant.
- **Préparer la réutilisation** du même schéma pour d’autres landings et pour les bots de scraping du porteur de projet.

---

## 3. Références techniques (état actuel)

| Élément | Détail |
|--------|--------|
| **Landing** | `/p/maisons-alfort/` — vue `landing_public` avec `template_key=concierge_maisons_alfort` |
| **Template** | `templates/landing_pages/concierge_maisons_alfort.html` — bloc `#chat-embed` avec `{% if flowise_embed_url %}<iframe src="{{ flowise_embed_url }}">` |
| **Construction URL** | `apps/scraping/flowise_client.py` → `get_flowise_chat_embed_url()` ; défaut `FLOWISE_URL` = `http://localhost:3010`, `FLOWISE_CHATFLOW_ID` (ou `DEFAULT_CHATFLOW_ID`) |
| **Flowise** | Conteneur `lppp_flowise`, port hôte **3010** ; volume `flowise_data` (chatflows, config) ; données RAG dans `data/flowise` (monté) + FAISS selon config Flowise |
| **Page de test** | `/essais/concierge/` (concierge_chat.html) — même embed, accès authentifié |
| **Docs** | `docs/flowise-workflows/conciergerie-maisons-alfort-architecture-et-onboarding.md`, `docs/base-de-connaissances/flowise-concierge-ia-maisons-alfort-guide.md` |

---

## 4. Stratégies non destructives (règles équipe)

- **Pas de reset** : ne pas réinitialiser le projet Flowise Conciergerie, les credentials ni le chemin FAISS sans accord explicite (cf. onboarding Conciergerie).
- **Tests en lecture / diagnostic d’abord** : vérifier que Flowise répond sur `http://localhost:3010`, que le chatflow existe, que l’URL d’embed est valide ; ne pas écraser les documents ingérés ni le vector store sans backup.
- **Changements configurables** : privilégier `.env` (FLOWISE_URL, FLOWISE_CHATFLOW_ID) et paramètres Flowise plutôt que de modifier le code en dur.
- **Traçabilité** : toute modification de sécurité (CSP, X-Frame-Options, CORS) ou d’URL doit être documentée dans la base de connaissances et dans ce document.

---

## 5. Segmentation des tâches par rôle

### Assistant (rédaction / coordination)
- [ ] Tenir à jour ce document (décisions, blocages, statut).
- [ ] Rédiger ou mettre à jour les pas-à-pas « vérifier le chatbot sur la landing » dans la base de connaissances.
- [ ] Coordonner les retours Architecte / Automatizer / Pentester (synthèse des causes possibles si l’iframe est vide ou le chat ne répond pas).

### Architecte
- [ ] Vérifier la **chaîne d’appel** : requête navigateur → Django (rendu HTML avec `flowise_embed_url`) → iframe → Flowise (port 3010) ; confirmer qu’aucune URL ne pointe vers un autre stack (ex. SquidResearch 3000/3001).
- [ ] Documenter les **points de défaillance** : `.env` manquant ou erroné, Flowise arrêté, chatflow ID invalide, iframe bloquée (CSP / X-Frame-Options), chemin FAISS incorrect dans Flowise.
- [ ] Proposer une **stratégie de test en couches** (santé Flowise → embed en direct → embed dans la landing) sans modifier les données existantes.
- [ ] S’assurer que le **mécanisme d’embed** (URL construite côté serveur, iframe côté client) est réutilisable pour d’autres landings et pour des bots (scraping, autres chatflows).

### Expert en automatisation (Automatizer)
- [ ] Vérifier que **Flowise** et le **chatflow Conciergerie** sont accessibles (health, embed, prédiction) ; que les variables `FLOWISE_URL` et `FLOWISE_CHATFLOW_ID` dans `.env` sont cohérentes avec l’instance LPPP (port 3010).
- [ ] Tester l’**embed en isolation** : ouvrir `http://localhost:3010/embed/{FLOWISE_CHATFLOW_ID}` dans le navigateur ; si le chat fonctionne là mais pas dans la landing, le problème est côté intégration (iframe, CSP, origine).
- [ ] Documenter les **workflows n8n** ou scripts éventuels qui alimentent Flowise (push de documents, sources) sans les exécuter de façon destructive ; proposer des tests en lecture ou sur copie si besoin.
- [ ] Préparer la **réutilisation du flux** pour d’autres bots (scraping, autres RAG) : même schéma URL embed + chatflow ID, ou API de prédiction si besoin.

### Pentester
- [ ] Vérifier que l’**iframe** et l’**origine Flowise** (localhost:3010 en dev) n’introduisent pas de risque (ex. pas de wildcard dans les en-têtes de sécurité, pas d’exposition inutile d’API).
- [ ] Valider les **en-têtes** côté Django pour l’affichage en iframe (CSP, X-Frame-Options) : s’assurer que l’embed Flowise est autorisé sur la page landing sans ouvrir de brèche (pas de `X-Frame-Options: DENY` bloquant l’iframe si l’on souhaite l’afficher ; CSP frame-ancestors / frame-src cohérents).
- [ ] Documenter les **recommandations** (et toute modification proposée) dans `docs/base-de-connaissances/regles-securite.md` ou dans ce document, sans appliquer de changement destructif aux données ou aux credentials.

---

## 6. Checklist de vérification rapide (non destructive)

1. **Flowise démarré** : `docker compose ps` → `lppp_flowise` en état running ; `curl -s -o /dev/null -w "%{http_code}" http://localhost:3010/` → 200 ou redirection attendue.
2. **Chatflow existant** : dans Flowise (http://localhost:3010), ouvrir le chatflow Conciergerie → onglet **Embed** → noter l’ID (ex. `c95b70d6-c7b7-49a8-920f-de00615b0176`).
3. **.env** : `FLOWISE_URL=http://localhost:3010`, `FLOWISE_CHATFLOW_ID=<id du chatflow>` ; redémarrer le conteneur `web` si besoin pour recharger les variables.
4. **Embed direct** : ouvrir `http://localhost:3010/embed/<FLOWISE_CHATFLOW_ID>` dans le navigateur → le chat s’affiche et répond.
5. **Landing** : ouvrir `http://localhost:8010/p/maisons-alfort/` → l’iframe doit afficher le même chat ; si cadre vide, vérifier la console navigateur (CSP, mixed content, blocage iframe).

---

## 7. Réutilisation pour d’autres bots (scraping, autres landings)

- Le **même mécanisme** (Django fournit une URL d’embed ou un chatflow ID ; la landing affiche une iframe ou appelle l’API de prédiction) peut servir pour :
  - d’autres landings avec chatbot ;
  - des bots dédiés au scraping / qualification, en exposant un chatflow Flowise dédié et en l’intégrant via embed ou API.
- L’Architecte et l’Automatizer documentent les **variantes** (embed vs API, un chatflow par bot vs un chatflow multi-usage) dans la base de connaissances pour éviter les régressions sur la Conciergerie Maisons-Alfort.

---

## 8. Tests, coverage et benchmark

- **Objectif** : pousser la couverture à 100 % sur la feature (flowise_client, vues concierge), tester l’intégration et les flux.
- **Rapport benchmark** : `segmentations/2026-01-30-rapport-benchmark-coverage-flux-robots.md` — métriques coverage, nombre de flux, actions des robots ; template à remplir par l’équipe ; preuves data-driven.
- **Commandes** : `make test-cov-docker` (tests + coverage dans le conteneur, DB dispo), `make test-cov` (local).

---

## 9. Références

- **Onboarding Conciergerie** : `docs/flowise-workflows/conciergerie-maisons-alfort-architecture-et-onboarding.md`
- **Guide Flowise Concierge** : `docs/base-de-connaissances/flowise-concierge-ia-maisons-alfort-guide.md`
- **Client Flowise (Django)** : `apps/scraping/flowise_client.py` — `get_flowise_chat_embed_url()`
- **Vue landing** : `apps/landing_pages/views.py` (concierge_maisons_alfort → `flowise_embed_url`)
- **Template** : `templates/landing_pages/concierge_maisons_alfort.html`
- **Ports LPPP** : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md` — Flowise LPPP = 3010

---

*Document créé pour la feature chatbot landing agents municipaux. Dernière mise à jour : 2026-01-30.*
