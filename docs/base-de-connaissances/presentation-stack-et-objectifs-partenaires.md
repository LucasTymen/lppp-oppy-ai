# LPPP — Stack technique et objectifs (document partenaire)

**Public** : lecteurs externes (partenaires, équipes achat, fournisseurs) qui ont besoin de comprendre en une lecture **ce qu’est le projet**, **quelle est notre stack** et **ce que nous voulons obtenir**, avec suffisamment de détails pour aligner offres, contrats ou intégrations.

**Pilotes** : Chef de Projet (vision), Architecte (stack), DevOps (infra), Intelligence métier (données et objectifs).  
**Dernière mise à jour** : 2025-01-30.

**Concordance** : pour l'état réel du code vs prévu, voir **concordance-stack-doc.md**.

---

## 1. En une phrase

**LPPP (Landings Pages Pour Prospections)** est un programme de **prospection B2B** piloté par une **stack centrale Django** : landing pages dédiées par prospect, données enrichies (entreprises, contacts), intelligence métier (scoring, qualité, matching), orchestration via n8n et (prévu) tracking et rapports mesurés. Backend Django, frontend Next.js (Vercel), Docker.

---

## 1bis. Principe fondamental (clé de lecture)

- **La stack LPPP (Django) est le système maître.** Les outils externes (tracking, LinkedIn, enrichissement, LLM) sont des **sources ou exécutants**, pas des centres de décision.
- **Django** = source de vérité (données, règles, scoring). **n8n** = orchestration (déclenchement, enchaînement), pas de logique métier critique.

---

## 2. Ce que nous voulons obtenir (objectifs)

### 2.1 Objectif principal

- **Générer des landing pages dédiées** à chaque prospect (société, contact), avec un contenu **cas par cas** (pas de texte générique) pour un positionnement **one-to-one** en B2B.
- Chaque prospect reçoit **une URL dédiée** (landing standalone), sans hub listant les autres — effet « page faite pour eux », pas « catalogue ».

### 2.2 Objectifs métier

- **Positionnement** : présenter nos prestations (Growth, SEO, acquisition B2B, data) de façon ciblée selon le secteur et le type de prospect (cabinets avocats, boîtes low tech, relance après événement, etc.).
- **Prospection** : alimenter les campagnes avec des **prospects enrichis** (données entreprise, contact, email, score de qualité) pour prioriser et personnaliser les messages.
- **Qualité des données** : scoring et complétude (email, entreprise, contact) pour filtrer, trier et adapter le niveau de personnalisation des contenus.
- **Relance et lead magnets** : priorité 1 = relance après événement ; puis variantes (positionnement direct, A/B testing ultérieur).

### 2.3 Objectifs techniques

- **Stack unifiée** : backend Django (admin, API, campagnes, enrichment), frontend Next.js + React (landings, effet « waouh »), déploiement reproductible (Docker, Vercel).
- **Enrichissement fiable** : récupérer des données (OSINT, entreprises, contacts) sans se faire bloquer (Google, LinkedIn) — stratégie « une tâche = un outil », puis fusion des résultats avec l’intelligence métier.
- **Mesure et rapports (prévu)** : tracking unifié (GTM, GA4, outil UX type Clarity), métriques rapatriées dans Django, rapports explicables et partageables sans dépendre aux données internes des plateformes tierces.
- **Sécurité et conformité** : aucun secret en dépôt ; configuration prod (HTTPS, DEBUG off, rate limiting sur les API) ; bonnes pratiques documentées.

---

## 3. Stack technique (détail)

### 3.1 Backend (cœur métier)

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| **Framework web** | Django 5.x | Admin, API, modèles (campagnes, prospects, landing pages), authentification, logique métier. |
| **Base de données** | PostgreSQL 16 | Données persistantes (prospects, campagnes, landing pages, enriched_data). |
| **Cache / files d’attente** | Redis 7 | Broker Celery, cache, stockage temporaire des résultats partiels d’enrichissement. |
| **Tâches asynchrones** | Celery (+ Celery Beat) | Enrichissement prospects, pipelines OSINT, jobs planifiés. |
| **Applications métier** | `apps/` (monorepo) | `landing_pages`, `campaigns`, `scraping` (enriched), `intelligence`, `landingsgenerator`. |

- **Hébergement backend** : Docker (dev/local) ; production typiquement sur VPS (ex. Contabo) avec Docker ou stack classique (Gunicorn, PostgreSQL, Redis, Celery).

### 3.2 Intelligence métier (données et algorithmes)

| Composant | Rôle |
|-----------|------|
| **`apps.intelligence`** | Scoring des prospects (formules configurables, plage 0–100), qualité des données (complétude, normalisation email/noms entreprise/contact), matching prospect ↔ landing page. |
| **Qualité** | Validation, normalisation, déduplication ; alimente le scoring et les stratégies d’affichage. |
| **Scoring** | Combinaison email, entreprise, contact, enriched_data ; seuils pour personnalisation (ex. score > 80 → message très personnalisé). |

- **Référence** : algorithmes centralisés, documentés (formules-et-algorithmes-reference.md, intelligence-metier-algorithmes.md) ; pas de logique dupliquée dans les autres apps.

### 3.3 Enrichissement (données prospects)

| Composant | Technologie / méthode | Rôle |
|-----------|------------------------|------|
| **Pipeline OSINT** | `apps.scraping.enriched` (pipelines, osint_sources, tasks) | Enrichir les prospects (entreprise, contact) à partir de sources externes ; résultats fusionnés et scorés par l’intelligence métier. |
| **Stratégie anti-blocage** | Une tâche Celery = une source | Éviter les blocages Google/LinkedIn ; exécution outil par outil, puis fusion des résultats partiels (Redis) et sauvegarde via tâche dédiée. |
| **Conteneur quali** | Kali Linux (Docker, profil `full`) | Environnement et outils OSINT / réseau pour l’enrichissement. |
| **Rate limiting** | `apps.scraping.enriched.security` | Limiter les abus sur les API d’enrichissement (webhooks N8N, Flowise). |

### 3.4 Automatisation et LLM

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| **Workflows** | n8n | Orchestration : webhook existant `POST /api/enriched/enrich` pour enrichissement ; autres workflows à prévoir). |
| **LLM / chatbots** | Flowise | Intégration de modèles LLM pour usages métier (dialogue, génération de texte si besoin). |

- Ports typiques : n8n 5678, Flowise 3000 (interne ou exposé selon l’env). **Règle** : n8n n’héberge pas de logique métier critique ; Django reste la source de vérité.

### 3.5 Tracking et mesure (prévu)

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| **Tag manager** | Google Tag Manager | Point d'entrée unique (à prévoir sur les landings). |
| **Analytics** | GA4 | Mesure trafic et événements (à prévoir). |
| **UX / comportement** | ex. Microsoft Clarity | Heatmaps, scroll, session replay (à prévoir). |

- **État** : non implémenté dans le code actuel ; objectif documenté (TODO, concordance-stack-doc.md). Les métriques seraient rapatriées dans Django puis exploitées par l'intelligence métier et les rapports.

### 3.6 Frontend (landing pages)

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| **Framework** | Next.js (App Router) + React | Pages des landing pages, composants réutilisables, effets visuels (« waouh »), responsive. |
| **Déploiement** | Vercel | Déploiement automatique (Git), une URL par landing ou un projet par prospect (standalone). |
| **Contenu** | Données injectées (content_json, API Django si besoin) | Personnalisation cas par cas ; même schéma de données, contenus rédigés par prospect. |

- **Stratégie** : landings **standalone** (un lien = une landing, pas de hub listant les autres prospects) pour confidentialité et positionnement B2B.

### 3.7 Infrastructure et DevOps

| Composant | Rôle |
|-----------|------|
| **Conteneurs** | Docker Compose (db, redis, web, celery, celery-beat, n8n, flowise, enriched, kalilinux en option). |
| **Source de code** | GitHub (origin), GitLab (miroir) ; pas de secrets dans le dépôt (.gitignore, .env non versionné). |
| **CI/CD** | Déploiement Vercel (frontend) ; backend déployé manuellement ou via CI (Contabo, SSH, Docker). |
| **Sécurité** | Règles documentées (regles-securite.md) : DEBUG=False en prod, SECRET_KEY forte, ALLOWED_HOSTS explicite, HTTPS, CSRF/XSS/injection, rate limiting API. |

---

## 4. Architecture haute niveau (schéma verbal)

```
[Utilisateur / Prospect]
        │
        ▼
[Landing Next.js] ← Vercel (URL dédiée par prospect)
        │
        │ (données statiques ou API si besoin)
        ▼
[Django Backend] ← Contabo / VPS (admin, API, campagnes)
        │
        ├── PostgreSQL (prospects, campagnes, landing_pages, enriched_data)
        ├── Redis (Celery, cache, résultats partiels enrichissement)
        ├── Celery (tâches enrichissement, une tâche = une source OSINT)
        ├── apps.intelligence (scoring, qualité, matching)
        └── apps.scraping.enriched (pipelines OSINT, merge + sauvegarde)
        │
        ├── n8n (workflows, webhooks)
        ├── Flowise (LLM)
        └── Kali / enriched (conteneur quali, outils OSINT)
```

- **Flux typique** : création de prospect → enrichissement (Celery, sources OSINT une par une) → fusion + scoring (intelligence métier) → sauvegarde enriched_data → utilisation pour personnaliser la landing (contenu, template).

---

## 5. Points importants pour un partenaire (ex. Achat GPT)

- **Périmètre** : prospection B2B, landing pages personnalisées, enrichissement de données (entreprises, contacts), scoring et qualité des données. Pas un produit grand public ; ciblage secteurs (avocats, low tech, relance événements, etc.).
- **Stack** : Django + PostgreSQL + Redis + Celery (backend), Next.js + React (frontend), Docker (backend + services), Vercel (frontend). Enrichissement avec stratégie anti-blocage (une tâche = un outil) et intelligence métier (scoring, qualité, matching).
- **Ce que nous voulons** : des landing pages **cas par cas** (contenu rédigé par prospect), une **URL dédiée** par prospect (standalone), des **données enrichies et scorées** pour prioriser et personnaliser, une **stack reproductible et sécurisée** (secrets hors dépôt, prod avec HTTPS, rate limiting).
- **Références internes** : README (racine), concordance-stack-doc.md (état réel vs prévu), fonction-premiere-et-segments-prospection.md, strategie-enrichissement.md, intelligence-metier-algorithmes.md, infra-devops.md, stack-frontend-nextjs-react.md, regles-securite.md.

---

*Document rédigé en coordination avec les rôles Chef de Projet (vision, objectifs), Architecte (stack, schéma), DevOps (infra, déploiement), Intelligence métier (données, scoring, objectifs métier). À mettre à jour lors d’évolutions majeures de la stack ou des objectifs.*
