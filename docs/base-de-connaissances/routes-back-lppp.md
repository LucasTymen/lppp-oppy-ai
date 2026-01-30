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
| `campaigns/` | `apps.campaigns.urls` | Campagnes (à développer) |
| `api/` | `apps.scraping.urls` | API scraping / enrichissement |

---

## 2. Détail par app

### `apps.landing_pages`

| Route | Vue | Nom | Usage |
|-------|-----|-----|--------|
| `""` | `views.landing_list` | — | Liste des landing pages (racine `/`) |
| `p/<slug:slug>/` | `views.landing_public` | `landing_public` | Page publique d’une landing (`/p/<slug>/`) |

### `apps.landingsgenerator`

| Route | Vue | Nom | Usage |
|-------|-----|-----|--------|
| `""` | `views.EssaisIndexView` | `index` | Premier écran essais : présentation relance salon (`/essais/`) |

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

---

## 3. URLs complètes (résumé)

| URL complète | Méthode | Usage |
|--------------|---------|--------|
| `/admin/` | GET | Admin Django |
| `/` | GET | Liste des landing pages |
| `/p/<slug>/` | GET | Page publique landing |
| `/essais/` | GET | Index essais (relance salon) |
| `/campaigns/` | — | À définir |
| `/api/enriched/enrich` | POST | Webhook enrichissement |
| `/api/enriched/enrich-one` | POST | Enrichissement un par un |

---

## 4. Maintenance

- **Dev Django** : à chaque ajout ou modification de route, mettre à jour ce document et les `urls.py` concernés.
- **DevOps** : vérifier que static, redirects et éventuel reverse proxy sont cohérents avec ces routes (notamment `/`, `/essais/`, `/admin/`).

---

*Document créé pour la concordance des routes back. Référence : segmentation `2025-01-30-montage-projet-ecrans-routes-logique.md`.*
