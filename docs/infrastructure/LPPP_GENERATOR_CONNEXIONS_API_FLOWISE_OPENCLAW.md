# LPPP-generator — Adresses API, Flowise, OpenClaw (feuille de raccordement)

**But** : relier une landing demo (LPPP) au bot / RAG Flowise et a OpenClaw ("le pote") sans se tromper de ports ni d'hotes.

**Typo corrigee** : OpenClaw (pas OpenCloud).

**Sources repo** : `LOG_COMMUN_LPPP_SQUIDRESEARCH.md`, `PROPOSITION_LPPP_ROUTAGE_CONTENEURS.md`, `docs/openclaw/OPENCLAW_GATEWAY_QUICK_TEST.md`, `CONTABO_N8N_FLOWISE.md`, `apps/documents/services_n8n_flowise.py`, `PONT_FLOWISE_TELEGRAM_OPENCLAW.md`.

---

## 1) Ports selon le contexte

### A. LPPP seul (compose d'origine LPPP)

| Service | URL depuis l'hote | Conteneur |
|---|---|---|
| Django LPPP | `http://localhost:8000` | `lppp_web` |
| Flowise LPPP | `http://localhost:3000` | `lppp_flowise` |
| n8n LPPP | `http://localhost:5678` | `lppp_n8n` |
| PostgreSQL | `localhost:5432` | `lppp_db` |
| Redis | `localhost:6379` | `lppp_redis` |

### B. Coexistence LPPP + SquidResearch (meme machine)

| Service LPPP | Port hote propose | Remplace |
|---|---|---|
| Django | `http://localhost:8010` | 8000 |
| Flowise | `http://localhost:3010` | 3000 |
| PostgreSQL | `localhost:5433` | 5432 |
| Redis | `localhost:6380` | 6379 |
| n8n | `5678` ou `5681` | selon conflit |

SquidResearch conserve en general : Django `8000`, Flowise `3001`, n8n `5679`, frontend `3000/3001` selon compose.

### C. SquidResearch dev (`docker-compose.dev.yml`)

| Service | URL hote (typique) |
|---|---|
| Django | `http://localhost:8000` |
| Flowise | `http://localhost:3002` (interne conteneur: 3000) |
| n8n | `http://localhost:5680` |
| Frontend | `http://localhost:3001` |

### D. Contabo (prod SquidResearch)

| Service | Acces |
|---|---|
| Django | `http://173.249.4.106:8000` (si expose) |
| Flowise | `http://173.249.4.106:3001` |
| n8n | `http://173.249.4.106:5679` (ou DNS dedie) |

### E. Contabo stack dediee n8n + Flowise (avec tunnel)

Apres `make contabo-tunnel-n8n-flowise` :

| Service | URL locale |
|---|---|
| n8n | `http://127.0.0.1:5679` |
| Flowise | `http://127.0.0.1:43001` |

---

## 2) API Flowise a utiliser pour la demo RAG

### Prediction chatflow (standard)

```http
POST {FLOWISE_BASE}/api/v1/prediction/{CHATFLOW_ID}
Content-Type: application/json
Authorization: Bearer {FLOWISE_API_KEY}   # si activee
```

Body usuel :

```json
{
  "question": "Texte utilisateur"
}
```

### Quelle valeur pour `FLOWISE_BASE` ?

| Contexte | Exemple |
|---|---|
| LPPP seul (hote) | `http://localhost:3000` |
| LPPP coexistence | `http://localhost:3010` |
| Depuis `lppp_web` vers Flowise meme stack | `http://lppp_flowise:3000` |
| SquidResearch hote | `http://localhost:3001` ou `http://localhost:3002` |
| Depuis conteneur web SquidResearch | `http://flowise:3000` |
| Tunnel Contabo | `http://127.0.0.1:43001` |

---

## 3) Variables .env cote landing / LPPP

### Valeurs officielles pour CE repo (compose actuel)

`docker-compose.yml` expose actuellement :
- Django LPPP : `8010:8000`
- Flowise LPPP : `3010:3000`
- n8n LPPP : `5681:5678`

Donc, par defaut dans ce projet :

```bash
FLOWISE_URL=http://localhost:3010
FLOWISE_CHATFLOW_ID=<uuid-chatflow-rag>
FLOWISE_API_KEY=
FLOWISE_CHAT_TIMEOUT=120
```

Depuis le conteneur web de la meme stack :

```bash
FLOWISE_URL=http://lppp_flowise:3000
```

(`lppp_flowise` est le service/host Docker vu dans `docker-compose.yml`.)

### Variantes (autres contextes)

```bash
FLOWISE_URL=http://localhost:3010
FLOWISE_CHATFLOW_ID=<uuid-chatflow-rag>
FLOWISE_API_KEY=
FLOWISE_CHAT_TIMEOUT=120
```

**Securite** : eviter un appel Flowise direct depuis le navigateur avec cle API. Preferer un proxy Django.

Dans ce repo, le proxy est :
- `POST /api/chat/flowise`
- route: `apps/scraping/urls.py`
- vue: `apps/scraping/views.py` (`flowise_chat_proxy_view`)

---

## 4) OpenClaw ("le pote") : points d'entree utiles

### UI Chat via tunnel

| Element | Valeur |
|---|---|
| Host | `173.249.4.106` |
| Tunnel local | `ssh -L 18790:127.0.0.1:18790 -i ~/.ssh/contabo_key root@173.249.4.106` |
| Health | `http://127.0.0.1:18790/healthz` |
| Chat token | `http://127.0.0.1:18790/#token=TOKEN` |
| Conteneur | `openclaw_secure` |

### Telegram

Sur landing statique, chemin le plus stable :
- bouton/lien `https://t.me/<ton_bot>`
- texte type "Continuer la discussion sur Telegram"

### Pont OpenClaw -> Flowise

Pour reutiliser le meme "cerveau" RAG :
- tool HTTP OpenClaw ou workflow n8n
- qui appelle le meme endpoint Flowise prediction
- reference : `docs/openclaw/PONT_FLOWISE_TELEGRAM_OPENCLAW.md`

---

## 5) API `/api/openclaw/` cote SquidResearch

Le brief interne mentionne une base `{BASE_URL}/api/openclaw/...` (health, company-search, etc.).

A traiter comme **roadmap/brief** tant que non verifie dans les `urls.py` et sans test `curl` concluant.

---

## 6) Checklist de mise en route rapide (LPPP-generator)

1. Choisir la stack Flowise source (LPPP, SquidResearch, ou tunnel Contabo).
2. Tester prediction Flowise en direct (`curl`) :

```bash
curl -sS -X POST "$FLOWISE_URL/api/v1/prediction/$FLOWISE_CHATFLOW_ID" \
  -H "Content-Type: application/json" \
  -d '{"question":"test"}'
```

3. Cote landing : appeler `POST /api/chat/flowise` (proxy Django).
4. OpenClaw : lien Telegram immediat + bridge avance via tool/n8n si necessaire.
5. Apres modif `.env` : redemarrer les services concernes (`web`, `flowise`, etc.).

---

## 7) Raccourci local (LPPP seul / coexistence)

| Besoin | Adresse type |
|---|---|
| Flowise RAG | `http://localhost:3000` ou `http://localhost:3010` |
| Appel API | `POST http://localhost:3010/api/v1/prediction/<CHATFLOW_ID>` |
| Django LPPP | `http://localhost:8000` ou `http://localhost:8010` |
| Depuis `lppp_web` vers Flowise | `http://lppp_flowise:3000` |

