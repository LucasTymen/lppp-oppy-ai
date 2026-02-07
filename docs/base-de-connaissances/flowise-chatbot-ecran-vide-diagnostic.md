# Chatbot écran vide / flux ne remonte pas — Diagnostic

**Contexte** : page `/p/maisons-alfort/` (ou `/essais/concierge/`) : l’iframe du chatbot reste vide ou le flux (conversation) ne remonte pas.

**Stratégie** : écran vide → URL d’embed (.env + restart web) ou Flowise pas sur 3010 ; flux ne remonte pas → config Flowise (RAG, LLM, logs). Voir **`segmentations/2026-01-30-strategie-chatbot-ecran-vide-et-flux.md`**.

---

## 0. Diagnostic en une commande (à lancer en premier)

```bash
docker compose exec web python manage.py check_flowise_embed
# optionnel : tester la connexion Flowise
docker compose exec web python manage.py check_flowise_embed --ping
```

La commande affiche `FLOWISE_URL`, `FLOWISE_CHATFLOW_ID` et l’URL d’embed construite. Si l’URL d’embed est vide → renseigner `.env` puis `docker compose restart web`.

---

## 1. Vérifier que l’URL d’embed est bien fournie

- Ouvrir **http://localhost:8010/p/maisons-alfort/** (ou l’URL de ta landing).
- **Afficher le code source** (Ctrl+U ou clic droit → Afficher le code source).
- Chercher **`flowise_embed_url`** ou **`iframe`** :
  - Si tu vois **« Chat en cours de configuration »** (sans iframe avec `src=`) → **`flowise_embed_url` est vide** côté Django.
  - Si tu vois **`<iframe src="http://localhost:3010/embed/...">`** → l’URL est bien injectée ; le problème est en aval (Flowise ou navigateur).

**Quand `flowise_embed_url` est vide :**

- Le conteneur **web** lit le `.env`. Vérifier :
  - **`FLOWISE_URL`** = `http://localhost:3010` (port **3010** pour LPPP). **Important** : l’URL d’embed est chargée par le **navigateur** ; si tu mets `http://flowise:3000`, le navigateur ne peut pas joindre ce host. Le code réécrit automatiquement `flowise:3000` en `http://localhost:3010` pour l’embed, mais pour être explicite, mets `FLOWISE_URL=http://localhost:3010` dans `.env`.
  - **`FLOWISE_CHATFLOW_ID`** = l’ID du chatflow (Flowise → ton chatflow → onglet **Embed**). Si vide, Django utilise un ID par défaut ; si tu as recréé le chatflow, remplace par l’ID actuel.
- Redémarrer le conteneur web après modification du `.env` :  
  `docker compose restart web`.

---

## 2. Vérifier que Flowise tourne et répond (port 3010)

- **Conteneur** :  
  `docker compose ps`  
  → **lppp_flowise** doit être **Up** (et port **3010:3000**).
- **Depuis l’hôte** :  
  Ouvrir **http://localhost:3010/** dans le navigateur.  
  → Tu dois voir l’interface Flowise (login éventuel). Si la page ne charge pas : Flowise n’est pas joignable (conteneur arrêté, mauvais port, pare-feu).
- **Embed seul** :  
  Ouvrir **http://localhost:3010/embed/TA_CHATFLOW_ID** (remplacer par l’ID de ton chatflow, ou par celui affiché dans le code source de la landing).  
  → Si le **chat s’affiche dans cet onglet** mais reste **vide dans la landing** : problème d’**iframe** (voir § 3).  
  → Si cet onglet reste **blanc ou en erreur** : problème **Flowise** (chatflow inexistant, ID incorrect, ou erreur dans le chatflow / RAG).

---

## 3. Iframe vide alors que l’URL d’embed charge dans un onglet

- **Console du navigateur** (F12 → Console) sur la page **landing** :  
  Regarder erreurs **CSP**, **X-Frame-Options**, **CORS**, **404**, **blocage d’iframe**.
- **Onglet « Réseau »** (F12 → Network) :  
  Recharger la page, vérifier la requête vers **localhost:3010/embed/...** : statut **200** ou **404** / **403** ?
- Si Flowise renvoie **X-Frame-Options: DENY** (ou équivalent) : l’embed peut être bloqué ; il faut adapter la config Flowise (ou le reverse proxy) pour autoriser le frame depuis ta landing (ou depuis ton domaine).

---

## 4. Le flux ne remonte pas (chat affiché mais pas de réponses / pas de conversation)

- Problème **côté Flowise** (RAG, chaîne, credentials) :
  - **Chatflow** : vérifier dans Flowise que le chatflow Conciergerie est **sauvegardé**, **publié** si besoin, et que l’**ID d’embed** utilisé dans `.env` correspond bien à ce chatflow.
  - **RAG / FAISS** : chemin FAISS, document store, et **clés API** (OpenAI, etc.) configurés dans Flowise. Voir `docs/flowise-workflows/conciergerie-maisons-alfort-architecture-et-onboarding.md`.
  - **Logs Flowise** :  
    `docker compose logs flowise`  
    pour voir erreurs au moment où tu envoies un message dans le chat.

---

## 5. Checklist rapide

| Étape | Commande / action |
|--------|-------------------|
| 1. URL dans la page ? | Code source de `/p/maisons-alfort/` → présence de `iframe` avec `src="http://localhost:3010/embed/..."` |
| 2. `.env` | `FLOWISE_URL=http://localhost:3010`, `FLOWISE_CHATFLOW_ID=<id du chatflow>` (ID copié depuis Flowise → Embed) |
| 3. Redémarrer web | `docker compose restart web` |
| 4. Flowise up ? | `docker compose ps` → lppp_flowise ; http://localhost:3010/ |
| 5. Embed direct | http://localhost:3010/embed/<FLOWISE_CHATFLOW_ID> → le chat s’affiche ? |
| 6. Console navigateur | F12 sur la landing → erreurs liées à l’iframe ou à 3010 ? |

---

## 6. Références

- **Sprint contrôle des flux** (DevOps, Architecte, Ingénieur système, Pentester) : `segmentations/2026-02-06-sprint-controle-flux-chatbot-landing-maisons-alfort.md`.
- **Stratégie** : `segmentations/2026-01-30-strategie-chatbot-ecran-vide-et-flux.md`.
- **Port LPPP** : Flowise = **3010** (pas 3000). Voir `log-commun-lppp-squidresearch.md`, `docker-compose.yml`.
- **Construction de l’URL** : `apps/scraping/flowise_client.py` → `get_flowise_chat_embed_url()`.
- **Onboarding Conciergerie** : `docs/flowise-workflows/conciergerie-maisons-alfort-architecture-et-onboarding.md`.
