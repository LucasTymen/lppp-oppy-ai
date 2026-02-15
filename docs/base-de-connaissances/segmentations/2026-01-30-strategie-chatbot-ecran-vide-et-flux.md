# Stratégie chatbot : écran vide vs flux ne remonte pas

**Date** : 2026-01-30  
**Contexte** : Résolution systématique des problèmes d’affichage et de conversation sur la landing Conciergerie (/p/maisons-alfort/).

---

## Principe

| Symptôme | Cause principale | Où agir |
|----------|------------------|--------|
| **Écran vide** (page ou iframe) | URL d’embed absente ou inaccessible ; Flowise pas sur le bon port | Django (.env), restart web, Flowise port **3010** |
| **Flux ne remonte pas** (chat visible mais pas de réponses) | RAG, LLM ou chaîne Flowise | Configuration Flowise (RAG, FAISS, clés API, logs) |

---

## 1. Stratégie « Écran vide »

**Objectif** : S’assurer que l’iframe a une URL valide et que Flowise est joignable par le navigateur.

### 1.1 Vérifications automatisées (à lancer en premier)

- **Commande diagnostic** (depuis la racine du projet) :
  ```bash
  docker compose exec web python manage.py check_flowise_embed
  ```
  ou en runserver local :
  ```bash
  python manage.py check_flowise_embed
  ```
  La commande affiche : `FLOWISE_URL`, `FLOWISE_CHATFLOW_ID`, URL d’embed construite, et optionnellement un test de connexion vers Flowise (port 3010).

- **Tests unitaires** (stratégie encodée dans les tests) :
  ```bash
  make test-cov-docker
  ```
  Les tests vérifient notamment :
  - `get_flowise_chat_embed_url()` retourne une URL avec `/embed/{id}` quand `FLOWISE_CHATFLOW_ID` est défini ;
  - retourne une chaîne vide quand `FLOWISE_CHATFLOW_ID` est vide ou uniquement des espaces ;
  - la vue landing injecte `flowise_embed_url` dans le contexte et le template affiche l’iframe ou le placeholder.

### 1.2 Vérifications manuelles (si la commande signale un problème)

1. **`.env`** (lu par le conteneur `web`) :
   - `FLOWISE_URL=http://localhost:3010` (port **3010** pour LPPP, pas 3000).
   - `FLOWISE_CHATFLOW_ID=<id>` : ID du chatflow (Flowise → chatflow Conciergerie → onglet **Embed**).
2. **Redémarrer le service web** après toute modification du `.env` :
   ```bash
  docker compose restart web
  ```
3. **Flowise démarré** :
   ```bash
  docker compose ps
  ```
   → `lppp_flowise` doit être **Up** (mapping **3010:3000**). Ouvrir http://localhost:3010/.
4. **Checklist détaillée** : suivre **`flowise-chatbot-ecran-vide-diagnostic.md`** (code source de la page, console navigateur, etc.).

---

## 2. Stratégie « Flux ne remonte pas »

**Objectif** : Corriger la chaîne RAG / LLM côté Flowise lorsque le chat s’affiche mais ne répond pas.

- **Périmètre** : Uniquement Flowise (pas Django). Aucun test Django ne peut « remonter » les réponses du modèle.
- **Actions** :
  1. Vérifier dans Flowise que le chatflow est sauvegardé et que l’ID d’embed correspond à celui dans `.env`.
  2. RAG / FAISS : documents ingérés, chemin FAISS, document store configuré. Voir `docs/flowise-workflows/conciergerie-maisons-alfort-architecture-et-onboarding.md`.
  3. Clés API (OpenAI ou autre) configurées dans les nœuds du chatflow.
  4. **Logs Flowise** au moment d’envoyer un message :
     ```bash
     docker compose logs -f flowise
     ```

---

## 3. Tests et stratégies nécessaires (réalisés)

| Élément | Rôle | Fichier / commande |
|--------|------|---------------------|
| URL d’embed vide → placeholder | Tests | `apps/landing_pages/tests/test_views_concierge.py` |
| URL d’embed renseignée → iframe | Tests | `apps/landing_pages/tests/test_views_concierge.py`, `apps/scraping/tests/test_flowise_client.py` |
| Port 3010 dans fallback | Tests | `apps/scraping/tests/test_flowise_client.py` (DB_HOST=db ou 127.0.0.1 → localhost:3010) |
| Diagnostic en une commande | Commande | `python manage.py check_flowise_embed` |
| Checklist manuelle | Doc | `flowise-chatbot-ecran-vide-diagnostic.md` |

---

## 4. Références

- **Diagnostic pas à pas** : `docs/base-de-connaissances/flowise-chatbot-ecran-vide-diagnostic.md`
- **Registre erreurs** : `docs/base-de-connaissances/erreurs-et-solutions.md` (entrée « iframe du chatbot vide »)
- **Construction de l’URL** : `apps/scraping/flowise_client.py` → `get_flowise_chat_embed_url()`
- **Port LPPP** : Flowise = **3010** (`docker-compose.yml`, `log-commun-lppp-squidresearch.md`)
