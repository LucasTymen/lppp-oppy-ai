# Enrichissement OSINT, guide-rails et pilotage Flowise / N8N

Document de référence pour **récupérer les algorithmes et le codage SquidResearch** (OSINT / ENRICHED), **enrichir une liste de prospects** rapidement, et **piloter les robots Flowise et N8N** via API et guide-rails.

---

## 1. Récupération des algorithmes SquidResearch

SquidResearch est une référence externe (monorepo hors workspace LPPP). Chemin documenté dans `sources.md` :

- **WSL/Linux** : `/home/lucas/tools/squidResearch`
- **Windows (WSL)** : `\\wsl.localhost\Ubuntu-22.04\home\lucas\tools\squidResearch`
- **Depuis $HOME** : `tools/squidResearch`

### Fichiers récupérés automatiquement (intégrés dans LPPP)

| Fichier SquidResearch | Emplacement LPPP | Statut |
|------------------------|-----------------|--------|
| `apps/scrapper/enriched/network/proxy_manager.py` | `apps/scraping/enriched/network/proxy_manager.py` | **Récupéré** — ProxyManager, ProxyStrategy, proxy_manager (Tor optionnel via TorManager). |
| `apps/enrichment/security.py` (RateLimiter) | `apps/scraping/enriched/security.py` | **Adapté** — EnrichmentRateLimiter (Django cache ou fallback mémoire), utilisé sur l’API enrich. |

### Fichiers à copier ou adapter (optionnel)

| Fichier SquidResearch | Usage LPPP | Emplacement LPPP |
|-----------------------|------------|-------------------|
| `apps/campaigns/nodes/data_nodes.py` | `_safe_eval_expression`, noeud ENRICHED | Déjà adapté dans `apps.intelligence.scoring` et `apps.campaigns.nodes.data_nodes`. |
| CompanyEnriched, PersonEnriched, PersonSearchAgent, etc. | Sources d’enrichissement réelles | À brancher dans `apps.scraping.enriched.osint_sources` (classes héritant de `BaseOSINTSource`) ou appeler via `ENRICHED_API_URL` si le container SquidResearch tourne. |
| idFinder (TorManager) | Rotation Tor | Optionnel ; `proxy_manager` utilise TorManager si `scrapper.idfinder.tor_manager` disponible. |

### Implémentation actuelle LPPP

- **Scoring** : `apps.intelligence.scoring` — `safe_eval_expression`, `score_prospect` (formule configurable).
- **Qualité** : `apps.intelligence.quality` — `prospect_completeness`, normalisation noms/email.
- **Pipeline enrichissement** : `apps.scraping.enriched.pipelines` — `run_enrichment_pipeline`, `run_batch_enrichment`.
- **Sources OSINT** : `apps.scraping.enriched.osint_sources` — `BaseOSINTSource`, `PlaceholderOSINTSource`, `get_proxy_strategy_for_domain(domain)` pour stratégie proxy (ProxyManager).
- **Réseau** : `apps.scraping.enriched.network` — `ProxyManager`, `ProxyStrategy`, `proxy_manager` (récupéré SquidResearch).
- **Sécurité** : `apps.scraping.enriched.security` — `EnrichmentRateLimiter` sur l’API `/api/enriched/enrich` (429 si dépassement).

---

## 2. Guide-rails (robots Flowise / N8N)

Pour que les robots ne dégradent pas le système ni n’exposent de risques :

| Guide-rail | Implémentation |
|------------|-----------------|
| **Validation des entrées** | Longueurs max : company 500, contact 200, email 254. Normalisation dans `osint_sources._validate_*`. |
| **Rate limiting** | Délai minimal entre appels source (`RATE_LIMIT_DELAY_SEC`), max 50 lignes ou IDs par requête batch. API : `EnrichmentRateLimiter` (requests/min + burst), retour 429 si dépassement. Variable `ENRICHMENT_RPM` pour limiter (défaut 30/min). |
| **Pas d’exécution de code arbitraire** | Scoring via `safe_eval_expression` (AST, opérateurs et fonctions autorisés uniquement). |
| **Limite batch** | `enrich_batch` : max 50 prospect_ids ; API `rows` : max 50 lignes. |
| **Logs** | Logging des runs pipeline et des échecs sources (pas de données sensibles en clair). |
| **API** | Endpoints dédiés (`/api/enriched/enrich`, `/api/enriched/enrich-one`) ; en production, protéger par secret header ou firewall. |

Aucun credential SquidResearch ou API tierce ne doit être mis en dur ; utiliser des variables d’environnement (ex. `ENRICHED_API_KEY`, `CLEARBIT_API_KEY`) si des APIs payantes sont branchées.

---

## 3. Pilotage Flowise et N8N

### Endpoints API

| Méthode | URL | Body (JSON) | Comportement |
|---------|-----|-------------|--------------|
| POST | `/api/enriched/enrich` | `{ "prospect_id": 1 }` | Enqueue Celery, enrichit le prospect 1 en async. |
| POST | `/api/enriched/enrich` | `{ "sync": true, "prospect_id": 1 }` | Enrichit en synchrone, retourne le payload enrichi. |
| POST | `/api/enriched/enrich` | `{ "prospect_ids": [1, 2, 3] }` | Enqueue Celery batch (max 50). |
| POST | `/api/enriched/enrich` | `{ "rows": [ { "company_name": "Acme", "contact_name": "John", "email": "j@acme.com" } ] }` | Enrichit les lignes en synchrone, retourne `payloads`. Clés personnalisables : `company_key`, `contact_key`, `email_key`, `domain_key`. |
| POST | `/api/enriched/enrich-one` | `{ "company_name": "", "contact_name": "", "email": "" }` | Une ligne en sync, retourne payload sans sauvegarder en base. |

Base URL : même origine que Django (ex. `http://localhost:8000` ou l’URL du serveur). CORS autorisé pour n8n/Flowise (voir `lppp.settings`).

### N8N

- **Webhook** : noeud « Webhook » qui reçoit un POST avec `rows` ou `prospect_id` / `prospect_ids`, puis appelle `POST /api/enriched/enrich` sur LPPP.
- **Flow** : après enrichissement, récupérer la réponse (ex. `payloads`) et l’envoyer au noeud suivant (Flowise, CRM, etc.).

### Flowise

- **API / Tool** : appeler l’URL d’enrichissement depuis un agent Flowise (HTTP Request ou outil personnalisé) avec le body JSON.
- **Chaînage** : Flowise peut décider quels prospects enrichir (ex. liste filtrée) puis appeler LPPP pour enrichir ; les résultats peuvent alimenter le contexte du LLM.

### Tâches Celery

- `apps.scraping.enriched.tasks.enrich_prospect(prospect_id, sources=[])` — une tâche par prospect.
- `apps.scraping.enriched.tasks.enrich_batch(prospect_ids, sources=[])` — une tâche qui traite jusqu’à 50 IDs (séquentiel pour respecter le rate limit).

Queue Celery : `enriched`. Worker : conteneur `enriched` (voir `docker-compose.yml`, `Dockerfile.enriched`).

---

## 4. Résumé des fichiers Python

| Fichier | Rôle |
|---------|------|
| `apps/scraping/enriched/osint_sources.py` | Sources OSINT (abstractions + guide-rails + placeholder), `get_proxy_strategy_for_domain()`. |
| `apps/scraping/enriched/pipelines.py` | Pipeline : sources → fusion → intelligence (quality, score). |
| `apps/scraping/enriched/tasks.py` | Tâches Celery : enrich_prospect, enrich_batch. |
| `apps/scraping/enriched/security.py` | EnrichmentRateLimiter (SquidResearch). |
| `apps/scraping/enriched/network/proxy_manager.py` | ProxyManager, ProxyStrategy, proxy_manager (SquidResearch). |
| `apps/scraping/enriched/network/__init__.py` | Export ProxyManager, ProxyStrategy, proxy_manager. |
| `apps/scraping/views.py` | Vues API webhook + rate limit sur enrich. |
| `apps/scraping/urls.py` | Routes `/api/enriched/enrich`, `/api/enriched/enrich-one`. |
| `apps/intelligence/scoring.py` | safe_eval, score_prospect. |
| `apps/intelligence/quality.py` | prospect_completeness, normalisation. |
| `apps/campaigns/nodes/data_nodes.py` | ENRICHEDEnrichmentNode (payload → quality + score). |

---

*Dernière mise à jour : 2025-01-30. Référence : SquidResearch (ENRICHED, data_nodes), LPPP apps.scraping.enriched, intelligence.*
