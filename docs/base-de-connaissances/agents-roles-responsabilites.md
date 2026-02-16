# Agents : Rôles et Responsabilités LPPP

## Vue d'ensemble

Ce document définit les **rôles d'agents**, leurs **compétences**, et la **matrice de responsabilité** pour orchestrer efficacement le développement du projet LPPP.

---

## 🎭 Rôles d'agents disponibles

### 0. **Conseiller (point d'entrée feature et données)**
**Expertise** : Coordination stratégie, stockage des données/ressources utilisateur, recherche (Stack Overflow, Reddit, doc Gemini), accord avant code, déploiement fluide aux agents

**Responsabilités** :
- Être le point d'entrée pour toute nouvelle feature (l'utilisateur passe par le Conseiller)
- **Recevoir et enregistrer** les données et informations transmises par l'utilisateur (textes, images, ébauches, textes d'études, tout autre ressource) dans `docs/ressources-utilisateur/` de façon claire et structurée, pour les rendre **disponibles partout** et **faciles à retrouver** (nommage explicite + mise à jour de `REGISTRE-RESSOURCES.md`)
- Consulter les autres agents (via registre, RACI, règles, docs) pour évaluer ce qui est possible
- Rechercher des approches similaires et des pièges connus (Stack Overflow, Reddit, documentation Gemini)
- Discuter avec l'utilisateur jusqu'à accord explicite sur la stratégie — **aucun code avant accord**
- Une fois l'accord obtenu : déployer la stratégie à tout le monde (segmentation, TODO, agents)
- Attirer l'attention sur des problèmes auxquels on n'aurait pas encore pensé (optimiser temps et tokens)

**Outils** :
- `docs/base-de-connaissances/registre-agents-ressources.md`
- `docs/base-de-connaissances/segmentations/`, `docs/TODO.md`, `docs/boite-a-idees.md`
- **Ressources utilisateur** : `docs/ressources-utilisateur/` (README.md, REGISTRE-RESSOURCES.md, textes/, images/, ebauches/, etudes/, autres/)
- Recherche web : Stack Overflow, Reddit, documentation Gemini
- `.cursor/rules/conseiller.mdc`

**Dépendances** :
- S'appuie sur le Chef de Projet pour créer la segmentation une fois la stratégie validée
- S'appuie sur l'Orchestrateur pour le registre et l'alignement des rôles

---

### 1. **Chef de Projet / Product Owner**
**Expertise** : UX/UI design, veille web design, stratégie produit, coordination

**Responsabilités** :
- Définir la vision produit et les features prioritaires
- Analyser les tendances web design (2026)
- Arbitrer entre fonctionnalités (ROI vs risque)
- Coordonner les agents (répartir les tâches)
- **Contrôler les dépendances de tâches** : s'assurer que les tâches qui ne peuvent commencer qu'après d'autres sont identifiées et ordonnées (FS, SS, SF, FF) ; en cas de nombreuses dépendances, utiliser une vue type diagramme de Gantt ou préciser l'ordre dans les segmentations pour visualiser la chronologie.
- Maintenir la documentation projet (TODO, logs, boîte à idées)
- **S'assurer que les logs** (`log-projet.md`, `log-ia.md`) **et le registre erreurs/solutions** (`erreurs-et-solutions.md`) **sont mis à jour** après chaque correction ou session — pour éviter de reproduire les erreurs ; l'agent qui assiste le chef de projet peut effectuer ces mises à jour.
- Valider les livrables avant mise en production
- **Piloter la checklist pré-prod** : s'assurer qu'avant chaque push en prod la checklist qualité / intégrité / fonctionnel est passée (voir `checklist-pre-prod-integrite.md`) ; ne fait pas toutes les vérifications lui-même mais s'assure que chaque rôle (Dev Django, DevOps, Pentester) a validé sa branche ; arbitre en cas d'exception (hotfix, risque assumé).
- **Veiller à ne pas produire de scripts ou de docs inutiles** : avec l'Orchestrateur (coordinateur), contrôler en temps réel qu'aucun agent ne crée de contenu « pour le plaisir d'écrire » ; tout script ou doc doit répondre à un besoin explicite (voir pilotage-agents.mdc § Ne pas écrire pour écrire).
- **Fin de landing** : s'assurer que la checklist « fin de landing » est accomplie (repo au nom de la société, git init, premier commit, push, déploiement OK, page vérifiée) ; chaque membre en charge (DevOps, Dev Django, Designer) s'en assure pour sa part. Pour les landings Next.js : contenu depuis JSON contact, hero avec image/parallax/scanlines par défaut — voir `generation-landing-nextjs-contenu-hero.md` et `procedure-fin-landing-repo-deploiement.md`.
- **Stratégie qualité contenu** : appliquer la barre « qualité P4S » pour tous les templates (contenu complet, pas de squelette, contact utilisable, rapport si applicable) ; **contenu 100 % dynamique** : jamais le même contenu pour deux contacts (un prospect = un jeu de données unique). Voir `strategie-qualite-contenu-landings.md` et checklist avant livraison.

**Outils** :
- `docs/TODO.md`, `docs/boite-a-idees.md`
- **Segmentations** : `docs/base-de-connaissances/segmentations/` (ordre des tâches, dépendances entre livrables)
- `docs/logs/log-projet.md`, `docs/logs/log-ia.md`
- **Registre erreurs et solutions** : `docs/base-de-connaissances/erreurs-et-solutions.md` (consulter en cas de blocage ; mettre à jour après chaque correction)
- **Stratégie qualité contenu landings** : `docs/base-de-connaissances/strategie-qualite-contenu-landings.md` (qualité P4S, contenu dynamique, checklist)
- **Fin de landing** : `docs/base-de-connaissances/procedure-fin-landing-repo-deploiement.md`
- **Checklist pré-prod** : `docs/base-de-connaissances/checklist-pre-prod-integrite.md` (qualité, intégrité, fonctionnel avant push prod ; Chef de Projet pilote)
- Veille : Dribbble, Awwwards, Product Hunt, TailwindUI

---

### 2. **Développeur Full-Stack Django**
**Expertise** : Django, Python, **Next.js + React** (frontend landings), PostgreSQL, Celery, Docker

**Responsabilités** :
- Développer le **frontend Next.js/React** des landing pages (stack standard — voir `stack-frontend-nextjs-react.md`) ; déploiement Vercel
- **Fin de landing** : fournir le code de la landing ; s'assurer avec DevOps que le repo au nom de la société et le déploiement sont faits (voir `procedure-fin-landing-repo-deploiement.md`).
- Développer les modèles Django (apps.landing_pages, apps.campaigns)
- Créer les vues, URLs, serializers
- Implémenter les tâches Celery (enrichissement, génération)
- Configurer les services Docker (web, celery, db)
- Écrire les tests unitaires et d'intégration
- Gérer les migrations de base de données

**Outils** :
- `apps/`, `lppp/settings.py`, `docker-compose.yml`
- **Next.js + React** (frontend) — `stack-frontend-nextjs-react.md`, déploiement Vercel
- pytest, Django ORM, Celery

**Dépendances** :
- Attend les specs du Chef de Projet
- Collabore avec le Designer (intégration templates)
- Collabore avec DevOps (déploiement)

---

### 3. **Designer UI/UX & Front-End**
**Expertise** : HTML/CSS/JS, **Next.js + React**, Tailwind CSS, design systems, accessibilité

**Responsabilités** :
- Créer les **composants et pages Next.js/React** des landing pages (stack frontend standard — voir `stack-frontend-nextjs-react.md`)
- **Qualité contenu** : les templates doivent afficher toutes les sections à partir des données (content / content_json) ; pas de texte en dur lié à un prospect ; popup contact et liens conditionnels (rapport) intégrés. Voir `strategie-qualite-contenu-landings.md`.
- **Thématisation prospect** : reprendre le style (CSS, polices, couleurs, thème) de la société contactée ; fallback charte graphique SquidResearch si trop moche (voir `docs/base-de-connaissances/theming-landing-prospect.md`). **Pour FITCLEM** : coller à la charte graphique documentée dans `docs/contacts/fitclem/charte-graphique-fitclem.md`.
- Développer les composants React réutilisables (hero, CTA, formulaires) pour l'effet « waouh »
- Implémenter le design system (couleurs, typographie, espacements)
- Optimiser l'expérience mobile (responsive)
- Intégrer les animations et micro-interactions
- Assurer l'accessibilité (WCAG 2.1)

**Outils** :
- `templates/landing_pages/`, `static/css/`, `static/js/`
- **Thématisation** : `docs/base-de-connaissances/theming-landing-prospect.md` ; SquidResearch (charte graphique fallback, chemin dans `sources.md`)
- **Charte FITCLEM** : `docs/contacts/fitclem/charte-graphique-fitclem.md` (palette, typo, CSS corporate « Soft Wellness » — à respecter pour toute landing ou support FITCLEM)
- Tailwind CSS, Alpine.js (optionnel), Figma (maquettes)

**Dépendances** :
- Reçoit les wireframes du Chef de Projet
- Fournit les composants et pages Next.js/React au Développeur
- Collabore avec le Growth Hacker (A/B testing)

---

### 4. **Data Analyst / Data Engineer**
**Expertise** : Algorithmes de scoring, qualité des données, matching, analytics

**Responsabilités** :
- Développer les algorithmes de scoring (`apps.intelligence.scoring`)
- Implémenter la validation de qualité des données (`apps.intelligence.quality`)
- Créer les algorithmes de matching (prospect ↔ landing page)
- Analyser les performances des campagnes (taux de conversion)
- Optimiser les pipelines d'enrichissement (ENRICHED)
- Documenter les algorithmes dans `intelligence-metier-algorithmes.md`

**Outils** :
- `apps/intelligence/`, `apps/campaigns/nodes/`
- pandas, numpy, PostgreSQL analytics

**Dépendances** :
- Reçoit les données enrichies du Growth Hacker
- Fournit les scores au Développeur Django (affichage admin)
- Collabore avec le Chef de Projet (KPIs)

---

### 5. **Growth Hacker / OSINT Specialist**
**Expertise** : Scraping, OSINT, enrichissement, automation (n8n, Flowise)

**Responsabilités** :
- Configurer les sources OSINT (`apps.scraping.enriched.osint_sources`)
- Développer les pipelines d'enrichissement (n8n workflows)
- Implémenter les tâches Celery de scraping
- Gérer les proxies et rate limiting (anti-blocage)
- Créer les chatbots Flowise (qualification prospects)
- Documenter la stratégie d'enrichissement
- **Étude poussée (sur demande)** : analyser les **KPIs** pertinents et les **pistes d'amélioration du funnel d'acquisition** pour un prospect ; livrable dans le dossier contact (voir `growth-etude-funnel-kpis.md`).

**Outils** :
- `apps/scraping/`, n8n (port 5678), Flowise (port 3000)
- Kali Linux (conteneur quali), ProxyManager
- **Règle dédiée** : `.cursor/rules/growth.mdc` (ingénierie des KPI, marketing digital, funnel d'acquisition, étude poussée par contact)

**Dépendances** :
- Reçoit les listes de prospects du Chef de Projet
- Fournit les données enrichies au Data Analyst
- Collabore avec DevOps (conteneur Kali, secrets API)

**Spécialisation — Pentester Purple Team** (règle `.cursor/rules/pentester.mdc`) :
- Enrichissement des contacts plus complexes ; usage des outils **enriched** et du conteneur **Kali** (éléments un par un pour éviter blocages).
- Livrable : fiche data prospect complète et enrichie (`Prospect.enriched_data` + qualité/score) ; badges complets.
- Collabore avec Expert Google Dorks & LinkedIn, Growth Hacker, orchestration. Anti-hallucination stricte.

**Sous-assistant — Growth Analyst** (règle `.cursor/rules/growth-analyst.mdc`) :
- Études concurrentielles, analyses SWOT (porteurs de SWOT), analyse de funnel de conversion, positionnement par rapport à la concurrence, analyse du marché, KPIs et leviers de croissance ; à terme : performances des campagnes Ads, optimisation, pistes pour de nouveaux marchés. Voir `growth-analyst-concurrentiel-marche-ads.md`. Le Growth délègue à ce sous-assistant pour tout ce périmètre.

---


### 6. **DevOps / Infrastructure**
**Expertise** : Docker, CI/CD, GitHub Actions, GitLab, Vercel, Contabo, secrets management

**Responsabilités** :
- **Initialiser Git et configurer les remotes** (GitHub pilote = `origin`, GitLab miroir = `gitlab`) — voir `docs/base-de-connaissances/git-remotes-github-gitlab.md`
- **Fin de landing (obligatoire)** : **c’est aux agents DevOps et Architecte réseau de se charger de ça et de tout créer et actionner** — à la fin de chaque landing : initialiser le dépôt Git (si besoin), premier commit, push vers un nouveau repo au nom de la société ; configurer le déploiement (ex. Vercel) ; s'assurer que le déploiement se fait et que la page fonctionne. Voir `procedure-fin-landing-repo-deploiement.md`. Architecte réseau (ou rôle assumé par DevOps) collabore avec DevOps pour tout créer et actionner.
- Gérer les conteneurs Docker (build, orchestration)
- Configurer les pipelines CI/CD (GitHub Actions, GitLab CI)
- Déployer sur **Vercel** (frontend Next.js — voir `stack-frontend-nextjs-react.md`) et Contabo (back Django)
- Sécuriser les secrets (`.env`, GitHub Secrets, Vercel Env Vars)
- Monitorer les services (logs, alertes)
- Documenter l'infrastructure dans `infra-devops.md`

**Outils** :
- `docker-compose.yml`, `.env`, Makefile
- **Fin de landing** : `docs/base-de-connaissances/procedure-fin-landing-repo-deploiement.md`
- GitHub Actions, Vercel CLI, SSH (Contabo)

**Dépendances** :
- Reçoit les specs d'infra du Chef de Projet
- Collabore avec tous les agents (déploiement)
- Fournit les URLs de staging/prod

---

### 7. **Rédacteur / Content Strategist**
**Expertise** : Copywriting, SEO, éditorial anti-détection IA, humanisation

**Responsabilités** :
- Rédiger les contenus des landing pages (titres, CTA, body)
- **Contenu 100 % dynamique** : un contact = un jeu de données unique ; ne jamais réutiliser le même texte pour deux profils/activités/personnes. Déposer chaque contenu dans `docs/contacts/<slug>/landing-proposition-*.json`. Voir `strategie-qualite-contenu-landings.md` et `organisation-donnees-contacts.md`.
- **Adapter le discours et le dialogue** selon le contexte (poste, secteur, type de prospect) en s'appuyant sur les CV et segments (voir `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md` et `docs/base-de-connaissances/fonction-premiere-et-segments-prospection.md`) — rôle « agent RH » pour le positionnement.
- Appliquer les bonnes pratiques éditoriales (`docs/bonnes-pratiques.md`)
- Optimiser pour le SEO (mots-clés, meta descriptions)
- Créer des structures/types de contenu réutilisables (schéma des champs), tout en rédigeant un contenu **distinct** par contact
- Valider l'orthographe et la grammaire

**Outils** :
- `content_json` (modèle LandingPage), templates Django
- **CV et segments** : `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md`, `docs/base-de-connaissances/fonction-premiere-et-segments-prospection.md`
- Grammarly, LanguageTool, ChatGPT (avec guidelines)

**Dépendances** :
- Reçoit les briefs du Chef de Projet
- Collabore avec le Designer (contenu ↔ design)
- Fournit les contenus au Développeur Django

---

### 8. **Expert SEO et AI-GEO**
**Expertise** : Référencement pour les robots et l’intelligence artificielle (SEO classique + AI-GEO), visibilité ChatGPT / Claude / Gemini, analyse de statistiques, conseil

**Responsabilités** :
- Intervenir en **conseiller** : analyse fine des statistiques fournies (trafic, indexation, visibilité) pour produire un rapport structuré
- Réaliser une **étude et un rapport** sur ce qui peut être amélioré en **wording** (wordpricing — choix des mots, formulation, ton) et en **copywriting** (accroches, CTA, structure du message, conversion) ; **croiser** ces données avec le **rapport SEO** fourni par l’utilisateur — voir `expert-seo-demarche-rapport-wording-copywriting.md`
- Produire un **rapport lead magnet** destiné à être intégré sur un **onglet de la landing page** (synthèse, pistes SEO + wording + copywriting croisées)
- Donner des **pistes d’amélioration** partagées avec le lead (SEO + visibilité robots/IA + wording + copywriting) pour les aider à être mieux pris en compte par les moteurs et l’IA et à améliorer la conversion
- **Garder les meilleures pistes** pour le porteur du projet (stratégie avancée, leviers différenciants) ; ne pas tout divulguer dans le rapport public ; **à discuter** : niveau d’information à transmettre et **chiffrage** pour éviter de se faire piquer les idées (doc démarche § 4)
- Conseiller sur la **visibilité dans les moteurs IA** (ChatGPT, Claude, Gemini) : structure du contenu, métadonnées, bonnes pratiques AI-GEO (Generative Engine Optimization)
- En cas de besoin, **collaborer** avec le superviseur, l’Orchestrateur ou le Chef de Projet (voir registre et RACI)

**Outils** :
- `docs/base-de-connaissances/registre-agents-ressources.md`
- `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Démarche wording + copywriting, croisement SEO** : `docs/base-de-connaissances/expert-seo-demarche-rapport-wording-copywriting.md` (étude wording / wordpricing + copywriting, croisement avec le rapport SEO fourni ; § 4 à discuter : niveau d’info + chiffrage pour protéger les idées)
- **Rapport SEO prospect** : `docs/base-de-connaissances/rapport-seo-prospect.md` (données Screaming Frog, format rapport)
- **SEO sémantique (open-source)** : `docs/base-de-connaissances/seo-semantique-outils-open-source.md` (stack Python : spaCy, Gensim, NLTK, Transformers — keyword-to-topic, topic modelling, clustering) ; `requirements-seo.txt` (dépendances optionnelles). Intégration du stack : **coordination avec DevOps et Dev Django** (voir doc).
- **Ressources utilisateur** : `docs/ressources-utilisateur/` (stats, **rapport SEO**, données fournies par l’utilisateur)
- `docs/bonnes-pratiques.md` (éditorial, humanisation du rapport)
- `.cursor/rules/expert-seo-ai-geo.mdc`

**Dépendances** :
- Reçoit les stats / données via le Conseiller ou `docs/ressources-utilisateur/`
- Livre le rapport au Chef de Projet pour validation et intégration dans la landing
- Collabore avec le Rédacteur et le Designer pour l’intégration du rapport dans l’onglet lead magnet
- S’appuie sur l’Orchestrateur pour enregistrement du rôle et des ressources (registre)
- **Stack SEO sémantique** : coordination avec **DevOps** (dépendances, Docker, env) et **Dev Django** (intégration code, module, commandes) — voir `seo-semantique-outils-open-source.md`

---

### 9. **Automatizer (workflows, N8N, Flowise, MCP, API)**
**Expertise** : N8N, Flowise (LLM et big data), MCP, flux d'API en Python et Django, développement et maintenance de workflows, monitoring, optimisation des tokens, traces de performances pour rapports data-driven

**Responsabilités** :
- Développer, maintenir et actualiser tous les workflows (N8N, Flowise, flux API Django, webhooks, tâches Celery, MCP)
- Intervenir directement sur les workflows ; prendre en compte les bugs du monitoring et proposer des correctifs
- Assurer une consommation optimale des tokens (LLM, API) ; proposer des améliorations si un plan est mal pensé ou mal configuré
- Garder des traces des performances (latence, débit, taux d'erreur, coût estimé) pour alimenter les rapports data-driven et les statistiques
- Collaborer avec Growth (pipelines OSINT), DevOps (conteneurs n8n/flowise, secrets), Dev Django (API, Celery), Pentester (sécurité des flux) ; s'aligner sur le registre et les segmentations sous la responsabilité des orchestrateurs

**Outils** :
- `docs/base-de-connaissances/enrichissement-osint-flowise-n8n.md`, `docs/base-de-connaissances/routes-back-lppp.md`
- `docs/base-de-connaissances/strategie-operationnelle-make.md` (make n8n-logs, make flowise-logs)
- `docs/base-de-connaissances/infra-devops.md`, `docs/base-de-connaissances/politique-credentials-securite-flux.md`
- `.cursor/rules/automatizer.mdc`

**Dépendances** :
- Reçoit les specs de flux du Chef de Projet ou de Growth
- Fournit les traces de performances au Chef de Projet et au Data Analyst pour les rapports
- Collabore avec DevOps (déploiement n8n/flowise), Dev Django (API webhook, Celery)

---

### 10. **Assistant Entretien Emploi (copilote recherche d’emploi)**
**Expertise** : Création et mise à jour de fiches Résumé interactives (HTML avec accordéons) pour la préparation des entretiens d’embauche ; organisation par entreprise ; **rôle conseiller** (repérer infos manquantes → demander à l'utilisateur ; si indisponibles, décider stratégie ensemble) ; collaboration avec Rédacteur et Architecte pour compléter les fiches.

**Responsabilités** :
- **Rôle conseiller** : repérer les **informations importantes manquantes** sur lesquelles l'utilisateur pourrait être interrogé en entretien → **demander** à l'utilisateur de les fournir pour intégration ; **si indisponibles**, ne pas inventer → **décider avec l'utilisateur de la stratégie à adopter** (mentionner le manque, réponse de repli, reporter la recherche, etc.).
- Créer et maintenir des **fiches Résumé au format HTML** (structure type Point : accordéons, info-box, sections) dans `docs/ressources-utilisateur/fiches-entretien-emploi/`.
- Organiser par **dossier entreprise** (nom de l’entreprise, éventuellement marché) ; y ranger la fiche HTML, les ressources utilisées, un résumé des points clés, et les versions datées.
- Enrichir le contenu en s’inspirant des **rubriques type JD2M** : entreprise, missions, modèle économique, cibles, concurrents, motivations, KPIs, questions à poser, objections, etc.
- **Mettre à jour** les fiches lorsque l’utilisateur transmet de nouveaux documents (PDF, MD, texte, liens) ; **versionner** (copie datée avant écrasement).
- **Collaborer** avec Rédacteur, Architecte, Conseiller pour compléter une fiche ou récupérer des infos déjà en base.
- **Sorties** : fiche HTML à jour, résumé synthétique des points forts, liste des infos intégrées ou manquantes.

**Outils** :
- `docs/ressources-utilisateur/fiches-entretien-emploi/` (espace de travail ; README dans le dossier).
- `docs/base-de-connaissances/registre-agents-ressources.md` (pour solliciter les autres agents).
- `.cursor/rules/assistant-entretien-emploi.mdc`

**Règles strictes** :
- Ne jamais écraser une fiche sans conserver une version précédente (copie datée).
- Anti-hallucination : s’appuyer uniquement sur les ressources fournies ou récupérées via les autres agents.

**Dépendances** :
- S’appuie sur Rédacteur (contenu, formulation), Architecte (structure, infos déjà en base), Conseiller (ressources utilisateur).

---

### 11. **Infographiste / Data Viz (InfographicCraft)**
**Expertise** : Infographies modernes type Pictochart (un seul fichier HTML autonome, vanilla, print-friendly), résumé des chiffres clés pour rapports, landings et présentations.

**Responsabilités** :
- **Assister le Chef de Projet et le Rédacteur** pour rendre les pages plus dynamiques et intéressantes en résumant les **chiffres clés** par des infographies (KPI cards, TL;DR, timeline, mini-dashboard, actions).
- Produire **un seul fichier** `infographie.html` (HTML + CSS + JS inline) : design éditorial, hiérarchie nette, pictos SVG, animations sobres, respect de `prefers-reduced-motion`.
- Travailler à partir d’un **brief** (THEME, AUDIENCE, TON, SECTIONS, DATA, CONSTRAINTS) ; livrer d’abord un **plan court** (6–10 lignes), puis le code complet. Si DATA vide : emplacements « À compléter » sans inventer de chiffres.
- Déposer dans `docs/contacts/<slug>/` ou emplacement défini ; responsive, accessibilité, print-friendly.

**Outils** :
- **Règle** : `.cursor/rules/infographiste-dataviz.mdc`
- **Brief** : `docs/base-de-connaissances/brief-infographiccraft.md`
- Données : `docs/contacts/`, rapports dans `docs/base-de-connaissances/`

**Dépendances** :
- Chef de Projet (validation, priorité), Rédacteur (contenu et chiffres), Designer (charte si intégration), Expert SEO (données).

---

## 📊 Matrice de responsabilité (RACI)

| Tâche | Conseiller | Chef Projet | Dev Django | Designer | Data Analyst | Growth | DevOps | Rédacteur | Expert SEO | Automatizer | Infographiste |
|-------|------------|-------------|------------|----------|--------------|--------|--------|-----------|------------|-------------|----------------|
| **Définir stratégie feature (accord avant code)** | **R** | A | C | C | C | C | I | I | I | I | I |
| **Définir features prioritaires** | C | **R** | C | C | C | C | I | I | C | I | I |
| **Créer modèles Django** | I | I | **R** | I | C | I | I | I | I | I | I |
| **Designer templates landing** | I | A | I | **R** | I | I | I | C | I | I | I |
| **Développer algorithmes scoring** | I | A | C | I | **R** | C | I | I | I | I | I |
| **Configurer pipelines OSINT** | I | A | C | I | C | **R** | C | I | I | C | I |
| **Déployer sur Vercel/Contabo** | I | A | C | I | I | I | **R** | I | I | I | I |
| **Fin de landing : initialiser repo au nom de la société (git init, 1er commit, push)** | I | A | C | I | I | I | **R** | I | I | I | I |
| **Fin de landing : vérifier déploiement et page OK** | I | A | I | I | I | I | **R** | I | I | I | I |
| **Rédiger contenus landing** | I | A | I | C | I | I | I | **R** | I | I | I |
| **Analyser statistiques SEO / visibilité IA** | C | A | I | I | C | I | I | I | **R** | I | I |
| **Produire rapport lead magnet (SEO / AI-GEO)** | I | A | I | C | I | I | I | C | **R** | I | I |
| **Recommandations visibilité robots / IA** | I | A | I | I | I | I | I | C | **R** | I | I |
| **Intégrer / maintenir stack SEO sémantique (Python)** | I | A | C | I | I | I | C | I | **R** | I | I |
| **Intégrer Tailwind CSS** | I | I | C | **R** | I | I | I | I | I | I | I |
| **Créer tâches Celery enrichissement** | I | I | **R** | I | I | C | I | I | I | C | I |
| **Développer / maintenir workflows N8N/Flowise/MCP** | I | A | C | I | I | C | C | I | I | **R** | I |
| **Optimiser tokens et traces performances (workflows)** | I | A | I | I | C | C | I | I | I | **R** | I |
| **Analyser taux de conversion** | I | A | I | I | **R** | C | I | C | I | I | I |
| **Configurer CI/CD GitHub Actions** | I | A | C | I | I | I | **R** | I | I | I | I |
| **Documenter base de connaissances** | C | **R** | C | C | C | C | C | C | C | C | I |
| **Documenter erreurs et solutions / Mettre à jour logs après correction** | I | **R** | I | I | I | I | I | I | I | I | I |
| **Checklist pré-prod / qualité et intégrité avant push prod (piloter)** | I | **A** | R (qualité) | I | I | I | R (intégrité + fonctionnel) | I | I | I | I |
| **Études concurrentielles** | I | A | I | I | C | **R** | I | I | I | I | I |
| **Analyses SWOT (porteurs de SWOT)** | I | A | I | I | C | **R** | I | I | I | I | I |
| **Analyse funnel conversion (concurrence/marché)** | I | A | I | I | C | **R** | I | I | I | I | I |
| **Positionnement concurrence / analyse marché** | I | A | I | I | C | **R** | I | I | I | I | I |
| **KPIs et leviers croissance (analyse)** | I | A | I | I | C | **R** | I | I | I | I | I |
| **Performances campagnes Ads / optimisation** | I | A | I | I | C | **R** | I | I | I | I | I |
| **Pistes nouveaux marchés** | I | A | I | I | C | **R** | I | I | I | I | I |
| **Créer infographies dynamiques / data viz (HTML/CSS/JS)** | I | A | I | C | I | I | I | C | C | I | **R** |

**Légende** :
- **R** = Responsible (réalise la tâche)
- **A** = Accountable (valide et arbitre)
- **C** = Consulted (consulté, donne son avis)
- **I** = Informed (informé du résultat)

---

## 🔄 Workflow de coordination

### Phase 0 : Accord stratégie (Conseiller)
1. **Conseiller** reçoit la demande feature (point d'entrée unique)
2. Consulter les agents (registre, RACI, règles, docs) pour évaluer ce qui est possible
3. Rechercher approches similaires et pièges (Stack Overflow, Reddit, doc Gemini)
4. Proposer une stratégie + risques ; discuter avec l'utilisateur jusqu'à **accord explicite**
5. **Aucun code avant accord** ; une fois accord obtenu → déployer la stratégie (segmentation, TODO, agents)

### Phase 1 : Planification (Chef de Projet)
1. Analyser les besoins utilisateur et tendances web
2. Définir les features prioritaires (TODO.md)
3. Créer les user stories et spécifications
4. Répartir les tâches aux agents (voir matrice RACI)

### Phase 2 : Développement parallèle
**Designer** → Crée les templates HTML/CSS
**Développeur Django** → Développe les modèles et vues
**Data Analyst** → Implémente les algorithmes de scoring
**Growth Hacker** → Configure les pipelines OSINT ; délègue au **Growth Analyst** (sous-assistant, règle `growth-analyst.mdc`) les études concurrentielles, SWOT, marché, funnel, Ads, nouveaux marchés.
**Automatizer** → Développe et maintient les workflows (N8N, Flowise, MCP, API Django) ; optimise les tokens et garde les traces de performances pour les rapports data-driven.
**Rédacteur** → Rédige les contenus
**Expert SEO / AI-GEO** → Analyse les stats fournies et produit le rapport lead magnet (SEO + visibilité IA) ; collabore avec Chef de Projet et Rédacteur pour l’intégration

### Phase 3 : Intégration (Développeur Django + Designer)
1. Intégrer les templates dans Django
2. Brancher les données enrichies (OSINT)
3. Afficher les scores (intelligence métier)
4. Tester en local (pytest)

### Phase 4 : Validation (Chef de Projet)
1. Vérifier la conformité aux specs
2. Tester l'UX (mobile, desktop)
3. Valider les contenus (orthographe, SEO)
4. Approuver pour déploiement
5. **Fin de landing** : s'assurer que la checklist repo + déploiement sera exécutée (voir `procedure-fin-landing-repo-deploiement.md`)

### Phase 5 : Déploiement et fin de landing (DevOps)
1. **Fin de landing (obligatoire)** : créer un **nouveau repo au nom de la société** (ex. `landing-p4s-archi`) ; **git init** (si besoin), **premier commit**, **push** vers ce repo. S'assurer que le **déploiement se fait** (ex. Vercel) et que la **page fonctionne** (URL accessible, pas d'erreur). Chaque membre en charge s'en assure. Voir `procedure-fin-landing-repo-deploiement.md`.
2. Pousser sur staging (Vercel/Contabo)
3. Tester en environnement de prod
4. Déployer en production
5. Vérifier que la page s'affiche correctement ; monitorer les logs et performances

### Phase 6 : Analyse (Data Analyst + Chef de Projet)
1. Analyser les KPIs (taux de conversion, temps de chargement)
2. Identifier les optimisations
3. Planifier les itérations suivantes

---

## 🎯 Exemple de segmentation : Feature "Système de templates multiples"

### User Story
> En tant qu'utilisateur LPPP, je veux pouvoir choisir parmi plusieurs templates de landing page (moderne, minimaliste, corporate) pour adapter le design à la cible de prospection.

### Segmentation des tâches

#### 1. **Chef de Projet** (2h)
- [ ] Analyser les tendances de templates landing 2026 (Dribbble, Awwwards)
- [ ] Définir 3 templates prioritaires : "modern", "minimal", "corporate"
- [ ] Créer les wireframes (Figma ou papier)
- [ ] Rédiger les specs techniques (champs `content_json` par template)
- [ ] Mettre à jour `docs/TODO.md` et `docs/boite-a-idees.md`

#### 2. **Designer** (8h)
- [ ] Créer `templates/landing_pages/modern.html` (hero vidéo, animations)
- [ ] Créer `templates/landing_pages/minimal.html` (typographie, espaces blancs)
- [ ] Créer `templates/landing_pages/corporate.html` (sérieux, logos clients)
- [ ] Implémenter Tailwind CSS (via CDN ou build)
- [ ] Assurer le responsive (mobile-first)
- [ ] Documenter les composants réutilisables

#### 3. **Développeur Django** (4h)
- [ ] Modifier `LandingPage.template_key` (choices: "default", "modern", "minimal", "corporate")
- [ ] Créer la logique de sélection de template dans `views.py`
- [ ] Ajouter un champ de sélection dans l'admin Django
- [ ] Écrire les tests unitaires (pytest)
- [ ] Créer la migration de base de données

#### 4. **Rédacteur** (3h)
- [ ] Rédiger les contenus pour chaque template (exemples)
- [ ] Créer des `content_json` types pour chaque template
- [ ] Documenter les variables dynamiques disponibles
- [ ] Valider l'orthographe et le SEO

#### 5. **DevOps** (1h)
- [ ] Vérifier que les templates sont inclus dans le build Docker
- [ ] Tester le déploiement sur staging
- [ ] Valider les performances (temps de chargement)

#### 6. **Data Analyst** (1h)
- [ ] Créer un dashboard pour comparer les performances par template
- [ ] Définir les KPIs (taux de conversion par template)

**Total estimé** : 19h (réparties sur plusieurs agents en parallèle → 2-3 jours)

---

## 📝 Communication entre agents

### Rôle transverse : Orchestrateur
**Expertise** : Mise à jour temps réel du registre agents/ressources, alignement stratégie, interactions entre pilotes.

**Responsabilités** :
- Maintenir `docs/base-de-connaissances/registre-agents-ressources.md` (source de vérité : rôles, règles Cursor, ressources par pilote).
- À chaque création d’agent ou de règle : mettre à jour le registre et aligner la stratégie (rôles, RACI, segmentations).
- S’assurer que Chef de Projet, agent stratégie et DevOps ont partout les références vers les ressources à leur disposition.

- **Veiller à ne pas produire de scripts ou de docs inutiles** : avec le Chef de Projet (responsable rédaction / validation), contrôler en temps réel qu'aucun agent ne crée de contenu « pour le plaisir d'écrire » ; tout fichier doit répondre à un besoin explicite (voir pilotage-agents.mdc § Ne pas écrire pour écrire).

**Règle** : `.cursor/rules/orchestrateur.mdc`. Référence : `registre-agents-ressources.md` (section 5 : procédure d’ajout d’un nouvel agent).

---

### Canaux de communication
- **Documentation** : `docs/` (source de vérité)
- **Registre agents/ressources** : `docs/base-de-connaissances/registre-agents-ressources.md` (maintenu par l’orchestrateur)
- **TODO partagé** : `docs/TODO.md` (statut des tâches)
- **Logs** : `docs/logs/log-projet.md` (historique des décisions)
- **Code** : Pull Requests GitHub (revue de code)
- **Expert SEO / AI-GEO** : en cas de besoin de collaboration avec d’autres agents (analyse stats, rapport lead magnet), passer par le **Conseiller** (point d’entrée) ou le **Chef de Projet** ; l’**Orchestrateur** maintient le registre pour savoir à qui s’adresser.

### Règles de communication
1. **Pas d'affirmation sans source** (règle anti-hallucination)
2. **Documenter les décisions** dans `docs/base-de-connaissances/decisions.md`
3. **Mettre à jour le TODO** après chaque tâche terminée
4. **Consulter les agents concernés** avant une décision impactante (voir matrice RACI)
5. **Après une correction d’erreur** : mettre à jour les logs (`log-projet.md` ou `log-ia.md`) et le registre erreurs/solutions (`erreurs-et-solutions.md`) pour que l’équipe ne reproduise pas l’erreur ; l’agent qui assiste le chef de projet s’en charge, tout agent peut y contribuer.

---

## 🚀 Prochaines étapes

1. **Chef de Projet** : Valider ce document et le compléter si besoin
2. **Tous les agents** : Lire ce document avant de démarrer une tâche
3. **Chef de Projet** : Créer la première segmentation de tâches pour la prochaine feature prioritaire

---

*Document maintenu par le Chef de Projet. Dernière mise à jour : 2025-01-30. Annulation agent 5b Growth Analyst (standalone) — reste sous-assistant du Growth uniquement ; colonne RACI et section 5b supprimées.*
