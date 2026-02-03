# Concordance stack / documentation LPPP

**Objectif** : vérifier que la documentation (présentation partenaires, roadmap, workflows) est **raccord** avec le code et les modèles réels. Aucune API, aucun champ ni workflow ne doit être décrit comme existant s’il n’existe pas — tout ce qui est « à prévoir » doit être explicite.

**Pilotes** : Architecte, DevOps, Intelligence métier. **Dernière mise à jour** : 2025-01-30.

---

## 1. Backend Django — ce qui existe

| Élément | Statut | Détail |
|--------|--------|--------|
| **Apps** | ✅ Existant | `campaigns`, `landing_pages`, `landingsgenerator`, `scraping` (dont `scraping.enriched`), `intelligence` |
| **Modèles** | ✅ Existant | `Campaign`, `Prospect` (campaigns) ; `LandingPage` (landing_pages). Prospect : `enriched_data` (JSONField), pas de champ `score` ni `state` en base. |
| **LandingPage** | ✅ Existant | `deploy_url`, `content_json`, `sector`, `category`, `template_key`, etc. |
| **API** | ✅ Existant | `POST /api/enriched/enrich` (webhook), `POST /api/enriched/enrich-one` (sync). Voir `apps/scraping/urls.py`. |
| **Routes landing_pages** | ✅ Existant | `/`, `/console/`, `/p/<slug>/`, `/p/<slug>/rapport/`, `/p/<slug>/prospects/`, `/p/<slug>/proposition/`. |
| **Tâches Celery** | ✅ Existant | `enrich_prospect_single_source`, `enrich_prospect_merge_and_save`, `enrich_prospect_decomposed`, `enrich_prospect`, `enrich_batch`. Score calculé dans merge, **retourné** par la tâche, **non persisté** sur Prospect (enriched_data seul est sauvegardé). |
| **Intelligence** | ✅ Existant | `apps.intelligence.scoring.score_prospect()`, `quality.prospect_completeness()`, `matching` ; utilisés dans merge_and_save. |
| **Health check** | ❌ Absent | Pas d’endpoint `/api/health/` dans le projet. |
| **Ingest métriques** | ❌ Absent | Pas d’endpoint `/api/metrics/ingest/` ni modèle pour stocker events (page_view, scroll, clics). |
| **Finalize enrichissement** | ⚠️ Indirect | Pas d’API REST dédiée « finalize » ; le flux est : webhook → tâches Celery → merge_and_save écrit en base. n8n peut appeler le webhook existant. |

---

## 2. Tracking & mesure — ce qui existe

| Élément | Statut | Détail |
|--------|--------|--------|
| **GTM / GA4 / Clarity** | ❌ Absent | Aucune implémentation dans le code. Mentionné dans TODO (« Analytics et tracking »), boîte à idées (scroll tracking, heatmaps), positionnement freelance. |
| **Events / métriques en base** | ❌ Absent | Aucun modèle Django pour page_view, scroll_depth, clics CTA, etc. |

→ Toute doc qui décrit GTM/GA4/Clarity ou un pipeline de métriques doit le marquer comme **prévu / à prévoir**, pas comme en place.

---

## 3. n8n & orchestration — ce qui existe

| Élément | Statut | Détail |
|--------|--------|--------|
| **Webhook enrichissement** | ✅ Existant | n8n peut appeler `POST /api/enriched/enrich` (body : `prospect_id` ou `prospect_ids` ou `rows`). |
| **Workflows « tracking_ingest »** | ❌ Absent | Pas d’API Django pour recevoir les métriques ; pas de workflow n8n décrit dans le dépôt. |
| **Workflows « landing_generate »** | ❌ Absent | Pas d’API de génération automatique de landing (création depuis prospect/template). Procédure manuelle + console documentée. |
| **Workflows « linkedin_publish »** | ❌ Absent | Pas d’intégration LinkedIn dans le code. |
| **Workflows « report_generate »** | ❌ Absent | Pas de génération automatique de rapports (MD/PDF) ni d’API dédiée. |

→ Les workflows n8n détaillés dans une roadmap doivent être en **« à prévoir »** sauf celui qui s’appuie sur le webhook enrichissement existant.

---

## 4. State machine & temporalité — ce qui existe

| Élément | Statut | Détail |
|--------|--------|--------|
| **État prospect (state machine)** | ❌ Absent | Pas de champ `state` / `ProspectState` sur `Prospect`. Pas de machine à états (created → enriched → scored → …) en base. |
| **Règles temporelles (T+24h, T+72h…)** | ❌ Absent | Aucun scheduler métier documenté ou implémenté. |
| **Versioning des règles** | ❌ Absent | Pas de champ `scoring_version` ou `report_model` sur les modèles. Formules documentées dans `formules-et-algorithmes-reference.md`. |

→ Toute spec « state machine » ou « temporalité » ou « versioning » = **objectif / à prévoir**, pas existant.

---

## 5. Références documentaires à jour

| Document | À aligner |
|----------|-----------|
| **routes-back-lppp.md** | Ajouter la route `console/` (liste + nom `console_landings`). |
| **presentation-stack-et-objectifs-partenaires.md** | Différencier clairement existant (Django, Celery, intelligence, enrichissement, console) et prévu (tracking GTM/GA4/Clarity, workflows n8n avancés, rapports auto, LinkedIn). |
| **roadmap-technique-et-workflows.md** | Pour chaque phase/workflow : indiquer « existant » vs « à prévoir » ; ne pas citer d’URL d’API inexistantes sans les marquer à prévoir. |

---

## 6. Récap — ne pas coder dans le vide

- **Existant** : Django (campaigns, prospects, landing_pages, scraping.enriched), Celery (enrich single source + merge_and_save + decomposed), intelligence (scoring, quality), API `/api/enriched/enrich` et `/api/enriched/enrich-one`, console `/console/`, champ `deploy_url`.
- **À prévoir (doc uniquement tant que pas implémenté)** : `/api/health/`, `/api/metrics/ingest/`, modèles ou stockage pour métriques, GTM/GA4/Clarity sur les landings, workflows n8n (ingest, landing_generate, linkedin, report), state machine prospect, règles temporelles, versioning règles/rapports, kill switch, frontière humain/automatisation, KPI business (ROI, coût par prospect).

---

*Document de vérification pour garder la stack et la doc raccord. À mettre à jour à chaque évolution majeure du code ou des objectifs.*
