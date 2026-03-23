# LPPP-generator — Raccordement chatbot Flowise + OpenClaw

But: brancher une landing demo LPPP au chat RAG Flowise sans exposer la cle API, puis proposer OpenClaw/Telegram comme relais conversation.

## Principe retenu

- Frontend landing: `fetch('/api/chat/flowise')` (meme origine Django).
- Backend Django LPPP: proxy serveur vers Flowise `POST /api/v1/prediction/{chatflow_id}`.
- Cle API Flowise gardee uniquement cote serveur (`FLOWISE_API_KEY`).
- OpenClaw: lien Telegram / tunnel UI; integration API avancee a traiter via workflow n8n ou outil dedie.

## Endpoint LPPP ajoute

- Route: `POST /api/chat/flowise`
- Body JSON: `{"question":"..."}`
- Supporte aussi: `{"message":"..."}`
- Reponse: `{ status, question, answer, payload }`
- Fichier: `apps/scraping/views.py` (`flowise_chat_proxy_view`)
- Routage: `apps/scraping/urls.py`

## Variables d'environnement

- `FLOWISE_URL` (ex: `http://localhost:3010`, `http://127.0.0.1:43001`)
- `FLOWISE_CHATFLOW_ID` (UUID du chatflow RAG)
- `FLOWISE_API_KEY` (optionnel selon instance Flowise)
- `FLOWISE_CHAT_TIMEOUT` (defaut 45s)

## Ports de reference (rappel)

- LPPP autonome (hote): Django `8000`, Flowise `3000`.
- LPPP coexistence proposee: Django `8010`, Flowise `3010`, Postgres `5433`, Redis `6380`.
- Tunnel stack dediee Contabo n8n+Flowise: Flowise local `127.0.0.1:43001`.

## Validation rapide

Exemple de test:

```bash
curl -sS -X POST "http://localhost:8000/api/chat/flowise" \
  -H "Content-Type: application/json" \
  -d '{"question":"test"}'
```

Si erreur 502, verifier `FLOWISE_URL`, `FLOWISE_CHATFLOW_ID`, accessibilite reseau et eventuelle cle API.

## OpenClaw (etat pratique)

- Usage stable immediat: lien Telegram (`https://t.me/<bot>`), tunnel UI OpenClaw si besoin de debug.
- Bridge avance OpenClaw -> Flowise: passer par un outil HTTP / n8n (roadmap, a valider selon infra active).
