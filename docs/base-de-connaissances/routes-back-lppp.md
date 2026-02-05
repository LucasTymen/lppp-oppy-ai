# Concordance des routes (back) LPPP

**Rôle** : Source de vérité pour les **URLs et routes** du projet. À maintenir par **Dev Django** et **DevOps** pour assurer la concordance front / back.

**Consommé par** : Dev Django, DevOps, Chef de Projet, Orchestrateur.

---

## 1. Racine des URLs (`lppp/urls.py`)

| Préfixe | Include | Description |
|---------|---------|-------------|
| `admin/` | Django admin | Interface d’administration |
| `""` | `apps.landing_pages.urls` | Landing pages (liste, page publique) |
| `essais/` | `apps.landingsgenerator.urls` | Interface essais / prospection |
| `campaigns/` | `apps.campaigns.urls` | Campagnes (liste, détail) |
| `api/` | `apps.scraping.urls` | API scraping / enrichissement |

---

## 2. Détail par app

### `apps.landing_pages`

| Route | Vue | Nom | Usage |
|-------|-----|-----|--------|
| `""` | `views.landing_list` | — | Liste des landing pages (racine `/`) avec filtres `?sector=` et `?category=` |
| `console/` | `views.console_landings` | `console_landings` | Console landings : tableau URL Django + URL déployée (Vercel), filtres secteur/catégorie |
| `maisons-alfort/` | `views.concierge_maisons_alfort_public` | `concierge_maisons_alfort_public` | Landing publique Concierge IA pour les équipes municipales (chatbot Flowise intégré) |
| `p/<slug:slug>/` | `views.landing_public` | `landing_public` | Page publique d’une landing (`/p/<slug>/`) |

| `p/<slug:slug>/rapport/` | `views.landing_rapport` | `landing_rapport` | Page « Consulter le rapport » : rendu Markdown depuis `docs/contacts/<slug>/rapport-complet*.md` |
| `p/<slug:slug>/prospects/` | `views.landing_prospects` | `landing_prospects` | Page « Prospects » : échantillon (`content_json.prospects`) |
| `p/<slug:slug>/proposition/` | `views.landing_proposition_value` | `landing_proposition_value` | Page « Proposition de valeur » : vue structurée depuis `content_json` |

### `apps.landingsgenerator`

| Route | Vue | Nom | Usage |
|-------|-----|-----|--------|
| `""` | `views.EssaisIndexView` | `index` | Premier écran essais : présentation relance salon (`/essais/`) |
| `concierge/` | `views.ConciergeChatView` | `concierge_chat` | Interface de test du chatbot Concierge IA (embed Flowise) — authentification requise |

*Écrans à venir* : à définir dans la segmentation interface landingsgenerator (wizard, choix template, etc.).

### `apps.campaigns`

| Route | Vue | Nom | Usage |
|-------|-----|-----|--------|
| *(aucune pour l’instant)* | — | — | Prévoir liste campagnes, détail, etc. |

### `apps.scraping` (sous préfixe `api/`)

| Route | Vue | Nom | Usage |
|-------|-----|-----|--------|
| `enriched/enrich` | `EnrichWebhookView` | `enrich_webhook` | Webhook enrichissement (n8n/Flowise) |
| `enriched/enrich-one` | `enrich_single_sync_view` | `enrich_one` | Enrichissement synchrone single |
| `concierge/scrape` | `ConciergeScrapeView` | `concierge_scrape` | Scrape pages web pour RAG Concierge IA (GET = URLs défaut Maisons-Alfort, POST = `{"urls": ["..."]}`) |

---

## 3. URLs complètes (résumé)

| URL complète | Méthode | Usage |
|--------------|---------|--------|
| `/admin/` | GET | Admin Django |
| `/` | GET | Liste des landing pages |
| `/console/` | GET | Console landings (URL Django + URL déployée) |
| `/maisons-alfort/` | GET | Landing Concierge IA Maisons-Alfort (équipes municipales, chatbot intégré) |
| `/p/<slug>/` | GET | Page publique landing |
| `/essais/` | GET | Index essais (relance salon) |
| `/essais/concierge/` | GET | Test chatbot Concierge IA (embed Flowise, authentifié) |
| `/campaigns/` | GET | Liste des campagnes (authentifié) |
| `/campaigns/<slug>/` | GET | Détail campagne (authentifié) |
| `/api/enriched/enrich` | POST | Webhook enrichissement |
| `/api/enriched/enrich-one` | POST | Enrichissement un par un |
| `/api/concierge/scrape` | GET, POST | Scrape pages (Concierge IA Maisons-Alfort) |
| `/api/concierge/save-content` | POST | Écrit le contenu scrapé dans data/flowise (body: pages ou content) |
| `/api/concierge/push-to-flowise` | POST | Pousse le fichier data/flowise vers Document Store Flowise |

---

## 4. Maintenance

- **Dev Django** : à chaque ajout ou modification de route, mettre à jour ce document et les `urls.py` concernés.
- **DevOps** : vérifier que static, redirects et éventuel reverse proxy sont cohérents avec ces routes (notamment `/`, `/essais/`, `/admin/`).

---

*Document créé pour la concordance des routes back. Référence : segmentation `2025-01-30-montage-projet-ecrans-routes-logique.md`.*
