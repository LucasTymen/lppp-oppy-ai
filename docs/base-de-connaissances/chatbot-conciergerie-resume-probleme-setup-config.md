# Chatbot Conciergerie (GPT / Flowise) — Résumé problème, setup et config

**Landing** : `/p/maisons-alfort/` — iframe Flowise avec RAG (FAISS) + OpenAI (embedding + chat).

---

## 1. Problèmes rencontrés (résumé)

| Symptôme | Cause | Solution rapide |
|----------|--------|------------------|
| **Écran vide** (page ou iframe blanche) | URL d’embed vide ou Flowise pas joignable | `.env` : `FLOWISE_URL=http://localhost:3010`, `FLOWISE_CHATFLOW_ID=<id>` → `docker compose restart web` ; vérifier que Flowise tourne (port 3010). |
| **Erreur « faiss.index No such file or directory »** | Nœud Faiss avec chemin **Windows** (`C:\flowise-data\...`) alors que Flowise tourne en **Docker** (Linux) | Dans Flowise, nœud **Faiss** → **Base Path to load** = **`/data/flowise/faiss/maisons-alfort`**. Sauvegarder. Si besoin, relancer un upsert (Document Store). |
| **« Missing credentials… OPENAI_API_KEY »** | Les nœuds **OpenAI Embeddings** et **ChatOpenAI** ne sont pas reliés à la credential OpenAI (souvent après réimport du workflow) | Dans Flowise : ouvrir le chatflow → sur chaque nœud OpenAI (Embeddings, ChatOpenAI), **Connect Credential** → sélectionner la credential **OpenAI API** (celle où la clé est renseignée). Sauvegarder. |

---

## 2. Setup (ce qui doit tourner)

- **Django** : conteneur `lppp_web`, port **8010** (landing servie ici).
- **Flowise** : conteneur `lppp_flowise`, port **3010** (LPPP ; pas 3000).
- **PostgreSQL, Redis** : pour Django/Celery.
- **Montage** : `./data/flowise` monté dans Flowise en `/data/flowise` (pour FAISS et fichiers).

Commandes utiles :
- `docker compose ps` — vérifier que `lppp_flowise` est Up (3010:3000).
- `make check-flowise-embed` — diagnostic URL d’embed côté Django.

---

## 3. Config pour le chat (GPT / Flowise)

### 3.1 Côté projet (`.env` à la racine)

| Variable | Rôle | Exemple |
|----------|------|--------|
| `FLOWISE_URL` | URL Flowise pour le navigateur (iframe) | `http://localhost:3010` |
| `FLOWISE_CHATFLOW_ID` | ID du chatflow (onglet Embed dans Flowise) | UUID du chatflow Conciergerie |
| `FLOWISE_API_KEY` | Optionnel : clé API Flowise (API Keys dans l’UI) si tu appelles l’API (ex. push documents) | À mettre dans `.env` uniquement, jamais en dépôt |

Après modification du `.env` : `docker compose restart web`.

### 3.2 Côté Flowise (UI localhost:3010)

| Élément | Où | Valeur / action |
|---------|-----|------------------|
| **Port** | `docker-compose.yml` | Flowise exposé sur **3010** (LPPP). |
| **Chatflow** | Chatflows → conciergerie-maisons-alfort | Sauvegardé ; ID copié dans `FLOWISE_CHATFLOW_ID`. |
| **Nœud Faiss** | Canvas → nœud « Faiss » | **Base Path to load** = **`/data/flowise/faiss/maisons-alfort`** (pas `C:\...` en Docker). |
| **OpenAI Embeddings** | Canvas → nœud Embeddings | **Connect Credential** = credential OpenAI (clé API renseignée). Modèle ex. `text-embedding-3-small`. |
| **ChatOpenAI** | Canvas → nœud Chat | **Connect Credential** = même credential OpenAI. Modèle ex. `gpt-4o-mini`, température 0. |
| **Credentials** | Menu **Credentials** | Une credential **OpenAI API** avec ta clé ; les nœuds y sont **reliés**. |
| **Document Store** | Document Stores | Conciergerie alimenté (upsert) ; si FAISS vide, relancer l’ingestion vers `/data/flowise/faiss/maisons-alfort`. |

### 3.3 Récap « checklist chat OK »

- [ ] Flowise Up sur 3010.
- [ ] `.env` : `FLOWISE_URL=http://localhost:3010`, `FLOWISE_CHATFLOW_ID=<id>`.
- [ ] Nœud Faiss : Base Path = `/data/flowise/faiss/maisons-alfort`.
- [ ] Nœuds OpenAI (Embeddings + ChatOpenAI) : credential OpenAI connectée.
- [ ] Document Store upserté (index FAISS présent ou ingestion relancée).
- [ ] Test : ouvrir `http://localhost:3010/embed/<FLOWISE_CHATFLOW_ID>` puis poser une question (ex. « passeport »).

---

## 4. Références

- **Stratégie écran vide / flux** : `segmentations/2026-01-30-strategie-chatbot-ecran-vide-et-flux.md`
- **Diagnostic pas à pas** : `flowise-chatbot-ecran-vide-diagnostic.md`
- **FAISS (Base Path)** : `flowise-faiss-base-path-infra.md`
- **Onboarding Conciergerie** : `docs/flowise-workflows/conciergerie-maisons-alfort-architecture-et-onboarding.md`
- **Comptes / LLM / clé API Flowise** : `data/flowise/comptes-et-llm.md`
- **Erreurs et solutions** : `erreurs-et-solutions.md` (entrées « iframe vide », « faiss.index », « 401 Invalid model key »)
