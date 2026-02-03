# Roadmap technique et workflows LPPP

**Objectif** : roadmap exécutable et workflows n8n concrets, **raccord au code réel**. Chaque phase et chaque workflow indique ce qui **existe** vs ce qui est **à prévoir**. Référence : **concordance-stack-doc.md**.

**Pilotes** : Architecte, DevOps, Intelligence métier. **Dernière mise à jour** : 2025-01-30.

---

## 1. Concordance

- **Existant** : Django (campaigns, prospects, landing_pages, scraping.enriched), Celery (enrich single source + merge_and_save + decomposed), intelligence (scoring, quality), API `/api/enriched/enrich` et `/api/enriched/enrich-one`, console `/console/`, champ `deploy_url`.
- **À prévoir** : `/api/health/`, `/api/metrics/ingest/`, modèles pour métriques, GTM/GA4/Clarity sur les landings, workflows n8n (ingest, landing_generate, linkedin, report), state machine prospect, règles temporelles, versioning, kill switch, frontière humain/automatisation, KPI business.

---

## 2. Roadmap technique (phases)

### Phase 0 — Pré-requis

| Élément | Statut | Détail |
|--------|--------|--------|
| n8n opérationnel | ✅ Existant | Docker Compose (n8n 5678). |
| Django expose API enrichissement | ✅ Existant | `POST /api/enriched/enrich`, `POST /api/enriched/enrich-one`. |
| Console landings | ✅ Existant | `/console/` — tableau URL Django + URL déployée. |
| GTM / GA4 / Clarity sur landings | ❌ À prévoir | Non implémenté. |
| Endpoint `/api/health/` | ❌ À prévoir | Non présent dans le projet. |

**Livrable Phase 0 (à prévoir)** : GTM installé sur les landings, GA4 + Clarity configurés, events visibles ; n8n reçoit des webhooks ; `/api/health/` OK.

---

### Phase 1 — Tracking unifié (fondation)

| Élément | Statut | Détail |
|--------|--------|--------|
| GTM events (lp_view, lp_scroll_*, lp_cta_click, etc.) | ❌ À prévoir | À définir sur les landings. |
| GA4 custom dimensions (prospect_id, campaign_id, etc.) | ❌ À prévoir | À configurer. |
| Workflow n8n **tracking_ingest** | ❌ À prévoir | Trigger : webhook ou pull GA4. Steps : fetch métriques, normalisation, POST → Django. |
| Endpoint Django **POST /api/metrics/ingest/** | ❌ À prévoir | N'existe pas ; à créer (modèle pour stocker events, vue API). |

**Livrable Phase 1** : Les comportements (views, scroll, clics) alimentent la base Django ; pas encore de décision automatique basée sur ces métriques.

---

### Phase 2 — Enrichissement et scoring (existant, stabilisé)

| Élément | Statut | Détail |
|--------|--------|--------|
| Workflow n8n **prospect_enrichment_trigger** | ⚠️ Partiel | n8n peut appeler `POST /api/enriched/enrich` (existant) ; pas de workflow « décomposé » n8n documenté (le décomposé est côté Celery). |
| Tâches Celery | ✅ Existant | `enrich_prospect_single_source`, `enrich_prospect_merge_and_save`, `enrich_prospect_decomposed`. |
| Scoring dans merge_and_save | ✅ Existant | `apps.intelligence.scoring.score_prospect()` ; score **retourné** par la tâche, **non persisté** sur Prospect (seul `enriched_data` est sauvegardé). |
| Seuils landing (light / standard / premium) | ❌ À prévoir | Logique documentée (formules-et-algorithmes-reference.md) ; pas de champ `landing_type` ou équivalent sur Prospect. |

**Livrable Phase 2** : Prospect enrichi et scoré (score dans résultat tâche) ; type de landing déterminé côté intelligence (à exposer en base si besoin).

---

### Phase 3 — Génération landing (automatisée)

| Élément | Statut | Détail |
|--------|--------|--------|
| Workflow n8n **landing_generate** | ❌ À prévoir | Trigger : prospect status = ready (état à définir). Steps : GET prospect, build content_json, push repo / API Next.js, déploiement Vercel. |
| API ou commande création landing depuis prospect | ❌ À prévoir | Documenté dans console-landings-automatisation-tracking.md ; pas d'endpoint `POST /api/landings/` ou équivalent. |
| Traçage deploy_url après déploiement | ⚠️ Manuel | Champ `deploy_url` sur LandingPage ; renseignement manuel dans l'admin. Webhook post-déploiement Vercel à prévoir. |

**Livrable Phase 3** : URL dédiée live par prospect, tracking actif (dès que Phase 1 est en place).

---

### Phase 4 — Publication LinkedIn (cadre contrôlé)

| Élément | Statut | Détail |
|--------|--------|--------|
| Workflow n8n **linkedin_publish** | ❌ À prévoir | Trigger : JSON campagne validé. Steps : lecture JSON, publication post (page ou compte propre), sauvegarde post_id, planification récup stats. |
| Intégration LinkedIn dans le code | ❌ Absent | Aucune API LinkedIn dans le dépôt. Publication et stats **propres uniquement**, pas d'automatisation agressive. |

**Livrable Phase 4** : Post publié, lien landing tracké ; limites respectées (publication uniquement, stats propres).

---

### Phase 5 — Analyse et décision

| Élément | Statut | Détail |
|--------|--------|--------|
| Workflow n8n **behavior_analysis** | ❌ À prévoir | Trigger : mise à jour métriques. Règles côté **Django** (ex. si views > 1 et scroll_75 et pas cta → flag `interest_without_action`). Actions : enrichir rapport, déclencher relance humaine. |
| Règles métier (comportement → interprétation) | ❌ À prévoir | À centraliser dans Django (intelligence métier), pas dans n8n. |

**Livrable Phase 5** : Insights exploitables, pas d'automatisme agressif ; frontière humain/automatisation explicite.

---

### Phase 6 — Rapport automatique

| Élément | Statut | Détail |
|--------|--------|--------|
| Workflow n8n **report_generate** | ❌ À prévoir | Trigger : fin campagne ou seuil atteint. Steps : collecte données, calcul KPIs, génération MD/PDF, stockage + notification. |
| Modèle de rapport (structure, métriques) | ⚠️ Documenté | template-rapport-complet-prospect.md, etc. ; pas de génération automatique côté code. |

**Livrable Phase 6** : Rapport contenant trafic, comportement, score initial vs réel, recommandations ; stocké et notifié.

---

## 3. Récap workflows n8n

| # | Nom | Objectif | Statut backend |
|---|-----|----------|----------------|
| 01 | tracking_ingest | Centraliser métriques (GA4 → Django) | À prévoir : `POST /api/metrics/ingest/`, modèle events. |
| 02 | prospect_enrichment_trigger | Enrichir + scorer | Existant : `POST /api/enriched/enrich` ; Celery fait le décomposé. |
| 03 | landing_generate | Produire URL dédiée | À prévoir : API/commande création landing, déploiement Vercel. |
| 04 | linkedin_publish | Diffusion (cadre contrôlé) | À prévoir : pas d'API LinkedIn dans le dépôt. |
| 05 | behavior_analysis | Interprétation comportement → flags | À prévoir : règles Django, pas de logique dans n8n. |
| 06 | report_generate | Restitution rapport | À prévoir : génération MD/PDF, stockage. |

---

## 4. Spécifications « oubliées » (objectifs à intégrer)

Ces points sont **structurants** et doivent être pris en compte avant de coder dans le vide. Ils sont listés comme **objectifs de spécification** ; l'implémentation suit la concordance (existant vs à prévoir).

1. **Contrôle d'état global (state machine)**  
   État prospect explicite en base (ex. created → enriched_partial → enriched_complete → scored → landing_generated → exposed → engaged → …). Les workflows n8n **ne décident pas** : ils lisent l'état, demandent une transition à Django, reçoivent OK/KO.

2. **Gestion du temps et latence métier**  
   Règles temporelles : T+0h exposition, T+24h première analyse comportementale, T+72h relance possible, T+7j clôture campagne. Scheduler métier distinct de Celery technique.

3. **Gestion de l'incertitude (confidence)**  
   Indicateur de confiance sur les métriques (ex. `confidence`, `sample_size`) pour éviter de traiter une landing vue 1 fois comme une vérité. Format type : `{ "score": 78, "confidence": 0.32, "sample_size": 3 }`.

4. **Versioning des règles et rapports**  
   Version des règles de scoring, des templates de landing, des modèles de rapport (ex. `scoring_version`, `landing_template`, `report_model`) pour cohérence des rapports et audit.

5. **Séparation signal / interprétation / action**  
   Trois couches distinctes : **Signal** (page_view, scroll_75, time_on_page), **Interprétation** (intérêt fort/faible, friction UX), **Action** (relance, changement CTA, clôture). Système explicable et auditable.

6. **Gestion des erreurs et zones grises**  
   Qualité des données explicite : `data_quality` (complete / partial / unreliable). Cas : GA4 down, Clarity non chargé, landing vue via bloqueur, données partielles.

7. **Stratégie d'arrêt (kill switch)**  
   Possibilité de stopper une campagne, geler des workflows, invalider des données, rétracter un rapport, sans redéployer toute la stack.

8. **Frontière humain / automatisation**  
   Définir où l'humain intervient : validation de relance, validation de rapport, validation d'angle. « À partir d'ici, décision humaine requise. »

9. **Preuve de valeur business**  
   Indicateurs business lisibles : landing → réponse, landing → rendez-vous, score initial vs outcome réel, coût par prospect activé. Pas que des métriques techniques.

---

## 5. Références

- **Concordance** : concordance-stack-doc.md (état réel du code vs prévu).
- **Présentation partenaires** : presentation-stack-et-objectifs-partenaires.md.
- **Routes** : routes-back-lppp.md.
- **Enrichissement** : strategie-enrichissement.md.
- **Console landings** : console-landings-automatisation-tracking.md.
- **Intelligence** : intelligence-metier-algorithmes.md, formules-et-algorithmes-reference.md.

---

*Document de roadmap et workflows, aligné sur la concordance stack/doc. À mettre à jour à chaque évolution majeure du code ou des objectifs.*
