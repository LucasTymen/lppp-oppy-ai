# Registre des agents et ressources LPPP

**Rôle** : Source de vérité temps réel pour les agents, la stratégie et le pilotage.  
**Maintenu par** : Orchestrateur (règle `.cursor/rules/orchestrateur.mdc`).  
**Consommé par** : Conseiller, Chef de Projet, agent en charge de la stratégie de fonctionnement, DevOps, et tous les agents pilotes.

---

## Vue d’ensemble

Ce registre recense **tous les agents** (rôles + règles Cursor) et **toutes les ressources** (docs, règles, APIs) à leur disposition. Il est mis à jour dès qu’un nouvel agent ou une nouvelle règle est créé, afin que :

- le **Chef de Projet** et l’**agent stratégie** sachent quels agents et quelles capacités utiliser ;
- le **DevOps** connaisse les impacts infra et les dépendances ;
- chaque **agent pilote** sache quelles ressources il peut utiliser et à qui s’adresser.

---

## 1. Rôles d’agents (stratégie et RACI)

| # | Rôle | Référence détaillée | Règles Cursor associées |
|---|------|---------------------|-------------------------|
| 0 | Conseiller (point d’entrée feature) | `agents-roles-responsabilites.md` § Conseiller | `pilotage-agents.mdc`, `conseiller.mdc` |
| 1 | Chef de Projet / Product Owner | `agents-roles-responsabilites.md` § Chef de Projet | `pilotage-agents.mdc`, `coordination-agents.mdc` |
| 2 | Développeur Full-Stack Django | `agents-roles-responsabilites.md` § Dev Django | `pilotage-agents.mdc` |
| 3 | Designer UI/UX & Front-End | `agents-roles-responsabilites.md` § Designer | `pilotage-agents.mdc`, `editorial.mdc` (contenus) |
| 4 | Data Analyst / Data Engineer | `agents-roles-responsabilites.md` § Data Analyst | `pilotage-agents.mdc` |
| 5 | Growth Hacker / OSINT Specialist | `agents-roles-responsabilites.md` § Growth | `pilotage-agents.mdc`, `growth.mdc`, `growth-analyst.mdc`, `expert-google-dorks-linkedin.mdc`, `pentester.mdc` |
| 6 | DevOps / Infrastructure | `agents-roles-responsabilites.md` § DevOps | `pilotage-agents.mdc`, `devops.mdc` |
| 7 | Rédacteur / Content Strategist | `agents-roles-responsabilites.md` § Rédacteur | `pilotage-agents.mdc`, `editorial.mdc` |
| 8 | Expert SEO / AI-GEO | `agents-roles-responsabilites.md` § Expert SEO | `pilotage-agents.mdc`, `expert-seo-ai-geo.mdc` |
| 9 | Automatizer (workflows, N8N, Flowise, MCP, API) | `agents-roles-responsabilites.md` § Automatizer | `pilotage-agents.mdc`, `automatizer.mdc` |
| 10 | **Assistant Entretien Emploi** (copilote recherche d’emploi, fiches Résumé HTML) | `agents-roles-responsabilites.md` § Assistant Entretien Emploi | `pilotage-agents.mdc`, `assistant-entretien-emploi.mdc` |
| — | **Orchestrateur** (rôle transverse) | `agents-roles-responsabilites.md` § Communication entre agents | `orchestrateur.mdc` |

---

## 2. Règles Cursor (capacités par fichier)

| Fichier | Description | Rôle(s) concerné(s) | Toujours appliquée |
|---------|-------------|----------------------|---------------------|
| `pilotage-agents.mdc` | Anti-hallucination, data-driven, référence éditoriale | Tous | Oui |
| `coordination-agents.mdc` | Workflow de segmentation, RACI, format segmentation | Chef de Projet, tous | Non |
| `editorial.mdc` | Éditorial anti-détection IA, humanisation (landing, contenu) | Rédacteur, Designer | Non (globs templates/content) |
| `devops.mdc` | Orchestration, flux, protection prod, secrets (GitHub, GitLab, Vercel, Contabo) | DevOps | Non |
| `growth.mdc` | Ingénierie des KPI, marketing digital, funnel d'acquisition, étude poussée par contact, enrichissement OSINT | Growth Hacker / OSINT | Non |
| `expert-google-dorks-linkedin.mdc` | Noms et coordonnées, anti-blocage, une requête = une source | Growth Hacker / OSINT | Non |
| `pentester.mdc` | Enrichissement contacts complexes, Kali, fiche data prospect, purple team | Growth Hacker (spécialisation) | Non |
| `orchestrateur.mdc` | Mise à jour du registre et de la stratégie, interactions entre pilotes | Orchestrateur | Non |
| `conseiller.mdc` | Point d'entrée feature et données, stockage ressources utilisateur (docs/ressources-utilisateur/), recherche (Stack Overflow, Reddit, Gemini), accord stratégie avant code, déploiement fluide | Conseiller | Non |
| `expert-seo-ai-geo.mdc` | Référencement robots/IA, visibilité ChatGPT/Claude/Gemini, analyse stats, rapport lead magnet (onglet landing), pistes d'amélioration (partagées vs réservées), conseil | Expert SEO / AI-GEO | Non |
| `automatizer.mdc` | N8N, Flowise, LLM/big data, MCP, flux API Python/Django, développement et maintenance workflows, monitoring, optimisation tokens, traces performances pour rapports data-driven | Automatizer | Non |
| `growth-analyst.mdc` | Études concurrentielles, SWOT, funnel conversion, positionnement concurrence, analyse marché, KPIs et leviers croissance ; performances campagnes Ads, optimisation, pistes nouveaux marchés (sous-assistant du Growth) | Growth Hacker (sous-assistant) | Non |
| `assistant-entretien-emploi.mdc` | **Assistant / Copilote recherche d’emploi** : fiches Résumé HTML (accordéons), préparation entretiens, organisation par entreprise dans `fiches-entretien-emploi/`, collaboration Rédacteur / Architecte, **rôle conseiller** (infos manquantes → demander à l'utilisateur ; si indisponibles, stratégie ensemble), versioning | **Assistant Entretien Emploi** | Non |

---

## 3. Ressources par pilote (Chef de Projet, Stratégie, DevOps)

### Assistant Entretien Emploi

- **Espace de travail** : `docs/ressources-utilisateur/fiches-entretien-emploi/` — un dossier par entreprise ; fiches HTML (accordéons), ressources, résumés, versions datées.
- **Modèle canonique** : `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html` (structure à appliquer à chaque nouvelle préparation).
- **Doc modèle + veille + checklist** : `docs/base-de-connaissances/fiches-entretien-emploi-modele-et-veille.md` (modèle, veille par onglet, coordination Chef de Projet / Architecte / DevOps / Pentester / Rédacteur, checklist « nouvelle société »).
- **Registre (ce fichier)** : `docs/base-de-connaissances/registre-agents-ressources.md` (pour solliciter Rédacteur, Architecte, Conseiller, Chef de Projet, Pentester, DevOps).
- **Ressources utilisateur** : `docs/ressources-utilisateur/` (README, REGISTRE-RESSOURCES.md) ; fiches entretien dans `fiches-entretien-emploi/README.md`.
- **Règle** : `.cursor/rules/assistant-entretien-emploi.mdc`
- **Collaboration** : Rédacteur (contenu, formulation, **questions RH / orientation poste / conventions** = rôle agent RH), Architecte (structure, infos en base), Conseiller (ressources utilisateur), Chef de Projet (rappels, fiches mémoire), Pentester (questions techniques, tests), DevOps (stacks, conventions).
- **Rôle conseiller** (intégré en coordination avec l'Orchestrateur) : repérer les **informations importantes manquantes** sur lesquelles l'utilisateur pourrait être interrogé en entretien → **demander** à l'utilisateur de les fournir pour intégration ; **si indisponibles**, ne pas inventer → **décider avec l'utilisateur de la stratégie à adopter** (mentionner le manque, réponse de repli, reporter la recherche, etc.). Doc : `fiches-entretien-emploi-modele-et-veille.md` § 4.

### Conseiller

- **Registre (ce fichier)** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Rôles et RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Segmentations** : `docs/base-de-connaissances/segmentations/` (TEMPLATE.md + fichiers `YYYY-MM-DD-nom-feature.md`)
- **TODO et idées** : `docs/TODO.md`, `docs/boite-a-idees.md`
- **Décisions** : `docs/base-de-connaissances/decisions.md`
- **Ressources utilisateur** : `docs/ressources-utilisateur/` (REGISTRE-RESSOURCES.md + textes/, images/, ebauches/, etudes/, autres/) — données et infos transmises par l’utilisateur ; le Conseiller les enregistre ici et met à jour le registre des ressources.
- **Règle** : `.cursor/rules/conseiller.mdc`

### Expert SEO / AI-GEO

- **Registre (ce fichier)** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Rôles et RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Démarche wording + copywriting, croisement SEO** : `docs/base-de-connaissances/expert-seo-demarche-rapport-wording-copywriting.md` — étude wording (wordpricing) + copywriting, croisement avec le rapport SEO fourni ; § 4 à discuter : niveau d’info + chiffrage pour protéger les idées.
- **Rapport SEO prospect** : `docs/base-de-connaissances/rapport-seo-prospect.md` (données Screaming Frog, format rapport, croisement avec wording + copywriting).
- **Template rapport complet prospect** : `docs/base-de-connaissances/template-rapport-complet-prospect.md` — rapport uniforme (fiche société + concurrence + PESTEL/SWOT/Porter + SEO) ; copier dans `docs/contacts/<slug>/rapport-complet-<slug>.md` et remplir. Voir `organisation-donnees-contacts.md`.
- **SEO sémantique (outils open-source)** : `docs/base-de-connaissances/seo-semantique-outils-open-source.md` — stack Python (spaCy, Gensim, NLTK, Transformers), keyword-to-topic, topic modelling, clustering ; coordination DevOps / Dev Django.
- **Dépendances optionnelles** : `requirements-seo.txt` (racine) — à intégrer dans l’env ou Docker en accord avec DevOps.
- **Ressources utilisateur** : `docs/ressources-utilisateur/` (stats, données fournies par l’utilisateur pour l’analyse)
- **Bonnes pratiques** : `docs/bonnes-pratiques.md` (éditorial, humanisation du rapport lead magnet)
- **Décisions** : `docs/base-de-connaissances/decisions.md`
- **Règle** : `.cursor/rules/expert-seo-ai-geo.mdc`
- **Collaboration** : Conseiller (point d’entrée, stats), Chef de Projet (validation, intégration landing), Orchestrateur (registre), Rédacteur / Designer (intégration onglet lead magnet), **DevOps** (stack SEO sémantique, dépendances, Docker), **Dev Django** (intégration code, module, commandes)

### Automatizer

- **Registre (ce fichier)** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Rôles et RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Enrichissement OSINT / Flowise / N8N** : `docs/base-de-connaissances/enrichissement-osint-flowise-n8n.md` — guide-rails, API webhook, rate limiting.
- **Routes back** : `docs/base-de-connaissances/routes-back-lppp.md` — webhook enrichissement (`/api/enriched/enrich`, `/api/enriched/enrich-one`).
- **Stratégie opérationnelle Make** : `docs/base-de-connaissances/strategie-operationnelle-make.md` — `make n8n-logs`, `make flowise-logs`, démarrage n8n/flowise.
- **Infra** : `docs/base-de-connaissances/infra-devops.md` — services n8n (5678), flowise (3000), variables `N8N_*`, `FLOWISE_*`.
- **Identifiants Flowise** : connexion UI et API via `.env` uniquement (`FLOWISE_USERNAME`, `FLOWISE_PASSWORD`, `FLOWISE_URL`, `FLOWISE_DOCUMENT_STORE_ID`, `FLOWISE_CHATFLOW_ID` pour l’interface de test `/essais/concierge/`) — ne jamais les committer ; voir `flowise-push-documents-informatique.md` § Identifiants et anti-leak.
- **Sécurité des flux** : `docs/base-de-connaissances/politique-credentials-securite-flux.md`, `regles-securite.md`
- **Règle** : `.cursor/rules/automatizer.mdc`
- **Info pour l’équipe** : `docs/base-de-connaissances/info-automatizer-pour-equipe.md` — document à partager avec les rôles qui collaborent (Growth, DevOps, Dev Django, Pentester, Chef de Projet, Data Analyst) pour savoir quand et comment solliciter l’Automatizer.
- **Collaboration** : Growth (pipelines OSINT), DevOps (conteneurs, secrets), Dev Django (API, Celery), Pentester (sécurité flux), Orchestrateur (registre, segmentations). Traces de performances pour rapports data-driven (Chef de Projet, Data Analyst).

### Chef de Projet / Stratégie

- **Rôles et RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Registre (ce fichier)** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Log commun LPPP ↔ SquidResearch** : **consulter systématiquement** `docs/base-de-connaissances/log-commun-lppp-squidresearch.md` (pointeur vers le document canonique dans SquidResearch : adresses, ports, .env, coexistence, état Docker). Obligatoire pour toute décision ou tâche touchant l’infra, Docker ou les deux projets.
- **Stratégie qualité contenu landings** : `docs/base-de-connaissances/strategie-qualite-contenu-landings.md` — barre « qualité P4S » pour tous les templates ; contenu 100 % dynamique (un contact = un jeu de données unique) ; checklist avant livraison.
- **Génération landing (contenu + hero)** : `docs/base-de-connaissances/generation-landing-nextjs-contenu-hero.md` — à appliquer automatiquement à chaque nouvelle landing Next.js (contenu depuis JSON contact, hero image/parallax/scanlines par défaut).
- **Segmentations** : `docs/base-de-connaissances/segmentations/` (TEMPLATE.md + fichiers `YYYY-MM-DD-nom-feature.md`)
- **TODO et idées** : `docs/TODO.md`, `docs/boite-a-idees.md`
- **Logs** : `docs/logs/log-projet.md`, `docs/logs/log-ia.md`
- **Registre erreurs et solutions** : `docs/base-de-connaissances/erreurs-et-solutions.md` — consulter en cas de blocage ; mettre à jour après chaque correction (agent qui assiste le Chef de Projet).
- **Décisions et sources** : `docs/base-de-connaissances/decisions.md`, `sources.md`
- **Guides** : `docs/GUIDE-CHEF-PROJET.md`, `docs/GUIDE-AGENTS.md`
- **Règles** : `.cursor/rules/pilotage-agents.mdc`, `coordination-agents.mdc`, `orchestrateur.mdc`

### DevOps

- **Log commun LPPP ↔ SquidResearch** : **consulter systématiquement** `docs/base-de-connaissances/log-commun-lppp-squidresearch.md` avant toute action ou recommandation sur Docker, ports, .env ou coexistence des deux stacks.
- **Stratégie fluide Git + Vercel** : `docs/base-de-connaissances/strategie-deploiement-git-vercel.md` — checklist par projet (GitHub + GitLab + Vercel), réutilisable pour 10+ landings ; pièges : `erreurs-et-solutions.md`.
- **Environnement WSL/Linux** : `docs/base-de-connaissances/environnement-wsl-linux.md` — **LPPP = Windows + WSL** (travail dans WSL) ; **WSL (bash) par défaut**, PowerShell en secours seulement (utilisateur préfère beaucoup moins PowerShell). Privilégier les commandes bash/WSL dans les procédures et la doc.
- **Infra et secrets** : `docs/base-de-connaissances/infra-devops.md`
- **Stratégie opérationnelle Make** : `docs/base-de-connaissances/strategie-operationnelle-make.md` — catalogue des commandes `make`, workflows (lancement, migrations, mise à jour, contrôle), répartition des responsabilités (DevOps, Dev Django, Chef de Projet). `make help` pour l'aide.
- **Tâche prioritaire (mobilisation système et connexions)** : `docs/base-de-connaissances/segmentations/2025-01-30-lancement-docker-projet.md` — réparer et lancer conteneur, backend, front, admin (avec Dev Django, Pentester) ; Option B runserver si ERR_EMPTY_RESPONSE sous Windows.
- **URGENT — Git (init, remotes GitHub/GitLab)** : `docs/base-de-connaissances/git-remotes-github-gitlab.md` — GitHub pilote (`origin`), GitLab miroir (`gitlab`) ; tâche **à exécuter en priorité** : `2025-01-30-devops-git-init-remotes.md` (signalé par l’utilisateur).
- **Règle** : `.cursor/rules/devops.mdc`
- **Orchestration** : `docker-compose.yml`, `.env` (non versionné), CI/CD (GitHub Actions, etc.)
- **Registre** : ce fichier (pour connaître les agents et impacts sur les services)

### Tous les agents

- **Agents de coordination** (Chef de Projet, Orchestrateur, Conseiller en mode coordination, DevOps) : **consulter systématiquement** le **log commun LPPP ↔ SquidResearch** (`docs/base-de-connaissances/log-commun-lppp-squidresearch.md`) dès que le contexte concerne Docker, ports, variables d’env ou coexistence LPPP / SquidResearch.
- **Agir en équipe** : l’agent en conversation est l’**interface** (coordination), pas le seul exécutant. Consulter le registre et le RACI ; déléguer aux rôles concernés (DevOps, Chef de Projet, Rédacteur, Designer, Dev Django, etc.) au lieu de tout faire soi-même. Règle détaillée : `pilotage-agents.mdc` § « Agir en équipe ».
- **Préférence utilisateur** : **Windows + WSL** (travail dans WSL) ; **bash/WSL par défaut**, PowerShell possible mais beaucoup moins prisé. Privilégier les commandes bash/WSL ; ne proposer PowerShell qu’en secours. Décision : `decisions.md` ; doc : `environnement-wsl-linux.md`.
- **Fiche de rôle** : `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Registre des ressources** : ce fichier
- **Registre erreurs et solutions** : `docs/base-de-connaissances/erreurs-et-solutions.md` — en cas d’erreur ou de blocage, consulter ce fichier ; après une correction, ajouter une entrée et mettre à jour les logs.
- **Sprint en cours** : `docs/base-de-connaissances/segmentations/2025-01-30-sprint-equipe-technique.md` (matrice d'assignation — toute l'équipe technique mobilisée)
- **Segmentations** : `docs/base-de-connaissances/segmentations/` (dont `2025-01-30-montage-projet-ecrans-routes-logique.md` — **montage projet** : Orchestrateur, Chef de Projet, Data Analyst, Dev Django, DevOps pour écrans, concordance des routes back, logique métier ; `2025-01-30-lancement-docker-projet.md` — mobilisation système et connexions ; `2025-01-30-premier-rapport-seo-landing-p4s-archi.md` ; `2025-01-30-interface-landingsgenerator.md`, `2025-01-30-devops-git-init-remotes.md`, `2025-01-30-relance-evenements.md`)
- **Concordance des routes back** : `docs/base-de-connaissances/routes-back-lppp.md` — source de vérité URLs ; maintenu par Dev Django et DevOps.
- **Prêt à démarrer** : `docs/base-de-connaissances/pret-a-demarrer.md` — venv, Docker, dev local PostgreSQL, tester l’admin, première landing
- **Réponses validées** : `docs/base-de-connaissances/reponses-validees-strategie.md`
- **Rapport SEO prospect** : `docs/base-de-connaissances/rapport-seo-prospect.md`
- **Dossiers contacts** : `docs/contacts/` — un dossier par contact (prospect) pour ses données ; règle `organisation-donnees-contacts.md`, registre `docs/contacts/REGISTRE-CONTACTS.md`
- **Ressources utilisateur** : `docs/ressources-utilisateur/` (REGISTRE-RESSOURCES.md pour retrouver textes, images, ébauches, études transmis par l’utilisateur)
- **Bonnes pratiques** : `docs/bonnes-pratiques.md`
- **Règles** : `.cursor/rules/` (voir tableau § 2)
- **Workflows N8N et automatisation** : pour collaborer avec le spécialiste workflows N8N/automatisation, voir **`docs/base-de-connaissances/info-automatizer-pour-equipe.md`** (qui est l’Automatizer, quand le solliciter, quelles ressources). Rôle détaillé : § Automatizer dans `agents-roles-responsabilites.md`, règle `automatizer.mdc`.

---

## 4. SEO sémantique (Expert SEO, DevOps, Dev Django)

| Ressource | Contenu | Utilisé par |
|-----------|---------|-------------|
| `seo-semantique-outils-open-source.md` | Stack Python (spaCy, Gensim, NLTK, Transformers), keyword-to-topic, topic modelling, clustering ; collaboration Expert SEO ↔ DevOps ↔ Dev Django | Expert SEO, DevOps, Dev Django |
| `requirements-seo.txt` | Dépendances optionnelles (spaCy, Gensim, NLTK, transformers, sentence-transformers) ; intégration en accord avec DevOps | Expert SEO, DevOps, Dev Django |

---

## 5. Stratégie et enrichissement (Growth, OSINT, Pentester)

| Ressource | Contenu | Utilisé par |
|-----------|---------|-------------|
| `growth-etude-funnel-kpis.md` | Étude poussée Growth : KPIs pertinents + pistes d'amélioration funnel d'acquisition (par prospect, sur demande) | Growth, Chef de Projet |
| `growth-analyst-concurrentiel-marche-ads.md` | Cadre Growth Analyst (sous-assistant) : études concurrentielles, SWOT, funnel, positionnement, marché, KPIs/leviers, campagnes Ads, nouveaux marchés | Growth, Chef de Projet |
| `bibliotheques-agents-techniques.md` | Tour des libs spécialisées (pandas, numpy, scraping, viz) — besoins agents techniques, sans overkill | Chef de Projet, DevOps, Data Analyst, Expert SEO, Growth |
| `strategie-enrichissement.md` | Anti-blocage, une tâche = un outil, fusion + intelligence métier | Growth, Expert Google Dorks, Pentester |
| `enrichissement-osint-flowise-n8n.md` | API webhook, N8N/Flowise, guide-rails | Growth, DevOps, **Automatizer** |
| `concierge-ia-maisons-alfort-n8n-flowise.md` | **Quick Win Concierge IA** : plan technique n8n + Flowise (aspiration maisons-alfort.fr, RAG, démo élu). Maquette exécutable pour Automatizer, DevOps, Dev Django, Pentester. Segmentation : `segmentations/2025-01-30-quick-win-concierge-ia-maisons-alfort.md`. | **Automatizer**, DevOps, Dev Django, Pentester, Chef de Projet |
| `sauvegarde-workflows-flowise-n8n.md` | **Règle projet** : tout workflow Flowise (chatflow) et n8n doit être exporté et versionné (Flowise : `docs/flowise-workflows/backups/` ; n8n : `docs/n8n-workflows/`). Réinjection en cas de perte. RACI : Automatizer (R), Chef de Projet (vérif.). | **Automatizer**, **Chef de Projet**, DevOps, Dev Django |
| `utilisation-flowise-n8n-prod-squidresearch-contabo.md` | **Utiliser Flowise et n8n hébergés sur prod Squid Research (Contabo)** : LPPP en client uniquement (FLOWISE_URL, FLOWISE_CHATFLOW_ID, N8N_WEBHOOK_URL) ; règles d’intégrité (aucun déploiement ni modification de la prod depuis LPPP). | **DevOps**, **Automatizer**, **Chef de Projet** |
| `guide-equipe-scraper-n8n-flowise.md` | **Faire fonctionner la chaîne** : scraper Django → n8n (workflow complet) → save-content → push-to-flowise. Prérequis, URLs (web:8000 vs localhost), checklist, dépannage. À utiliser après que Flowise soit OK. | **Automatizer**, DevOps, Dev Django |
| `google-cloud-oauth-n8n.md` | **Google Cloud OAuth pour n8n** : Origines JavaScript et URI de redirection à renseigner pour éviter les blocages (Gmail, Sheets, etc.) | **Automatizer**, DevOps |
| `info-automatizer-pour-equipe.md` | Briefing : qui est l’Automatizer, quand le solliciter, quelles ressources (pour Growth, DevOps, Dev Django, Pentester, Chef de Projet, Data Analyst) | Growth, DevOps, Dev Django, Pentester, Chef de Projet, Data Analyst |
| `intelligence-metier-algorithmes.md` | Scoring, qualité, matching — où brancher, stratégie d'implantation | Data Analyst, Dev Django |
| `stack-frontend-nextjs-react.md` | **Stack frontend standard** : Next.js + React pour landings, effet waouh, déploiement Vercel — à appliquer systématiquement | Designer, Dev Django, DevOps |
| `demarrage-projet-equipe-tech.md` | Checklist et diagnostic pour faire redémarrer le projet (Docker / Option B), voir les rendus des landings | DevOps, Dev Django |
| `procedure-modifications-landing-visible.md` | **URGENT** : faire apparaître les modifications sur les landings — après édition du JSON lancer `create_landing_p4s --update` ; recharger sans cache ; headers anti-cache déjà sur la vue landing | **Dev Django, DevOps** |
| `procedure-fin-landing-repo-deploiement.md` | **Fin de landing** : git init, premier commit, push vers un **repo au nom de la société** ; s'assurer que le déploiement se fait et que la page fonctionne ; chaque membre en charge (DevOps, Dev Django, Chef de Projet) s'en assure | **DevOps** (R), Chef de Projet (A), Dev Django, Designer |
| `checklist-pre-prod-integrite.md` | **Checklist pré-prod** : qualité, intégrité, fonctionnel avant push prod ; Chef de Projet pilote (A), Dev Django (qualité), DevOps (intégrité + fonctionnel), Pentester (C sécurité) ; pas d'agent dédié unique | **Chef de Projet** (A), DevOps, Dev Django, Pentester |
| `procedure-avant-migrations-relance.md` | **Avant migrations / relance** : commit + push pour sauvegarder l'état, puis migrations, puis relance ; rôles Architecte, DevOps, Dev Django | **DevOps**, Dev Django, Architecte |
| `segmentations/2026-01-30-sprint-resolution-reseau-django.md` | **Sprint résolution réseau Django** : Django/admin inaccessible ; coordination Architecte réseau (ports, log commun SquidResearch), DevOps (diagnostic conteneurs, Option B, port alternatif), Pentester (ALLOWED_HOSTS, sécurité). SquidResearch prioritaire — LPPP s'adapte. | **Architecte réseau**, **DevOps**, **Pentester** |
| `segmentations/2026-01-30-sprint-chatbot-landing-flowise.md` | **Sprint chatbot Flowise sur landing** : faire fonctionner l'iframe sur /maisons-alfort/ (erreur « adresse IP du serveur de flowise »). Dev Django (URL embed navigateur), DevOps (Flowise port 3000), Automatizer (chatflow), Chef de Projet (validation). | **Dev Django**, **DevOps**, **Automatizer**, **Chef de Projet** |
| `segmentations/2026-01-30-sprint-ecran-blanc-landing-chatbot.md` | **Sprint écran blanc landing chatbot** : corriger l’écran blanc sur /p/maisons-alfort/ ; intégration, stylisation, rendre fonctionnel. Coordination **Architecte** (structure, intégration), **DevOps** (infra, Flowise, .env), **Dev Django** (vue, template), **Designer** (stylisation), **Automatizer** (Flowise embed), Chef de Projet (validation). | **Architecte**, **DevOps**, **Dev Django**, **Designer**, **Automatizer**, **Chef de Projet** |
| `strategie-deploiement-git-vercel.md` | **Stratégie fluide Git (GitHub + GitLab) + Vercel** : checklist unique par projet, réutilisable sans erreur pour 1, 2, … 10+ landings ; pièges à éviter (Root Directory, push les deux remotes, repo sans README) | **DevOps**, Chef de Projet |
| `classification-landings-secteur-categorie.md` | Classer les landings par secteur et catégorie ; liste avec filtres pour voir les rendus par type | Chef de Projet, Dev Django, Designer |
| `strategie-qualite-contenu-landings.md` | **Qualité P4S pour tous les templates** : barre qualité (contenu complet, pas de squelette, contact utilisable, rapport si applicable) ; **contenu 100 % dynamique** (un contact = un jeu de données unique) ; checklist avant livraison ; rôles équipe | Chef de Projet, Rédacteur, Designer, Dev Django, DevOps |
| `brief-contenu-vivant-humanisation-landings.md` | **Contenu vivant et humanisation** : rendre les landings plus vivantes et humaines (positionnement, enjeux_lead, rapport_url, callout Why GE) ; missions Rédacteur + Designer ; champs optionnels `enjeux_lead`, `coordonnees_intro` | **Rédacteur**, **Designer**, Chef de Projet |
| `schema-landing-proposition.md` | **Structure Full-Stack Conversion** : champs content_json (hero, pain points, solution, services onglets, expertise stack, mission flash, why GE), template proposition, mobile-first, Google Fonts ; contenu toujours par contact ; champs vivant : positionnement, enjeux_lead, coordonnees_intro | Chef de Projet, Dev Django, Rédacteur, Designer |
| `template-hero-aerosection.md` | **Hero réutilisable** : image fond 100 %, parallaxe, scanlines (par défaut sur Next.js) — à appliquer aux autres landings et rapports ; référence Next.js = `deploy/standalone-ackuracy/` | Dev Django, Designer |
| `generation-landing-nextjs-contenu-hero.md` | **Génération landing Next.js** : contenu depuis JSON contact → `src/content/landing.json` ; hero avec image (JSON ou défaut), parallax + scanlines **actifs par défaut** ; template = `standalone-ackuracy` — à appliquer automatiquement à chaque nouvelle landing | **Chef de Projet** (vérif.), Dev Django, Designer |
| `reconstitution-landing-p4s-personnalisation.md` | **Reconstitution landing P4S** : tous les degrés de personnalisation (hero background, thème CSS Vampire, style perso, contenu complet) ; export statique aligné sur la vue Django ; procédure pour ne plus déployer un squelette | **DevOps**, Dev Django, Chef de Projet |
| `css-vampire.md` | **CSS Vampire** : extraction du style du site cible (polices, couleurs, logo, fond) ; commande `css_vampire <url> [--slug] [--apply]` ; thème injecté dans content_json | Dev Django, Designer |
| `design-brief-landing-reference-cv.md` | **Brief design** : référence visuelle (landing CV / page perso Vercel) pour aligner la landing proposition sur ce niveau de design + style société (CSS Vampire) | **Designer** (priorité), Dev Django |
| `docs/contacts/0flow/style-voix-et-design-0flaw.md` | **Style voix + design 0Flaw** : brief Rédacteur & Designer pour la landing 0flow — ton, vocabulaire, CTA alignés sur 0flaw.fr ; procédure CSS Vampire (https://0flaw.fr/ --slug 0flow --apply) | **Rédacteur**, **Designer**, Chef de Projet |
| `formules-et-algorithmes-reference.md` | **Spec canonique** : formules mathématiques et algorithmes (score prospect, complétude, matching, normalisation) — s'en inspirer pour implémenter | Data Analyst (logique métier + algorithmes), Dev Django |
| `osint_sources.py`, `proxy_manager.py` | Contrat de données, stratégies proxy | Expert Google Dorks, Pentester |
| Tâches Celery : `enrich_prospect_decomposed`, `single_source`, `merge_and_save` | Flux décomposé recommandé | Pentester, orchestration |

---

## 6. Procédure : ajouter un nouvel agent ou une nouvelle règle

Lorsqu’un **nouvel agent** (rôle) ou une **nouvelle règle** Cursor est créé :

1. **Orchestrateur** (ou Chef de Projet) met à jour ce registre :
   - Ajouter le rôle dans la table § 1 et/ou le fichier dans la table § 2.
   - Renseigner les ressources associées (§ 3 ou § 4 si pertinent).
2. **Stratégie** : si le nouvel agent participe aux tâches projet, mettre à jour :
   - `docs/base-de-connaissances/agents-roles-responsabilites.md` (rôle, matrice RACI, workflow).
   - Les segmentations existantes ou à venir si le rôle intervient sur des features.
3. **Documentation** : ajouter les décisions/sources dans `decisions.md` et `sources.md` si besoin.
4. **Guides** : mettre à jour `GUIDE-CHEF-PROJET.md` et `GUIDE-AGENTS.md` pour pointer vers le nouveau rôle/règle et vers ce registre.
5. **Logs** : inscrire la création dans `docs/logs/log-projet.md` ou `log-ia.md`.

---

## 7. Application de la stratégie d'agents

Pour **appliquer** cette stratégie au quotidien :

1. **Tous les agents** : respecter `pilotage-agents.mdc` (anti-hallucination, data-driven, ne pas écrire pour écrire, rangement).
2. **Nouvelle feature** : passer par le **Conseiller** (point d'entrée) → accord stratégie → **Chef de Projet** crée la segmentation → agents réalisent selon RACI (`agents-roles-responsabilites.md`).
3. **Rôles et règles** : les 12 règles Cursor listées en § 2 correspondent aux rôles § 1 ; chaque agent s'appuie sur sa règle dédiée + `pilotage-agents.mdc`.
4. **Orchestrateur** : met à jour ce registre à chaque création d'agent/règle ; avec le Chef de Projet, veille à ce qu'aucun agent ne produise de scripts ou docs inutiles.
5. **Référence complète** : `agents-roles-responsabilites.md` (rôles détaillés, RACI, workflow Phases 0–6, exemples de segmentation).

---

## 8. Dernière mise à jour

- **Date** : 2026-02-05  
- **Modifications** : **Rôle conseiller Assistant Entretien Emploi** (intégré en coordination avec l'Orchestrateur) — repérer les infos importantes manquantes (risque d'être interrogé en entretien), demander à l'utilisateur de les fournir pour intégration ; si indisponibles, décider avec l'utilisateur de la stratégie à adopter. Règle `assistant-entretien-emploi.mdc` et doc `fiches-entretien-emploi-modele-et-veille.md` § 4 mis à jour ; registre § 2 (description règle), § 3 (Assistant Entretien Emploi) mis à jour.
- *Précédent* — **Date** : 2025-01-30  
- **Modifications** : **Annulation agent 5b** — retrait de l’agent standalone Growth Analyst ; reste uniquement comme sous-assistant du Growth (règle `growth-analyst.mdc`, doc `growth-analyst-concurrentiel-marche-ads.md`). Registre § 1 (ligne 5b supprimée, growth-analyst.mdc rattaché à Growth), § 2, § 5 mis à jour ; agents-roles-responsabilites (section 5b supprimée, colonne RACI Growth Analyst supprimée, tâches concurrentiel/SWOT/Ads → Growth).
- *Précédent* : **Application de la stratégie d'agents** — tableau § 1 complété : ligne **5b Growth Analyst** (règle `growth-analyst.mdc`), ligne **Orchestrateur** (rôle transverse, règle `orchestrateur.mdc`). Nouvelle section **§ 7 Application de la stratégie d'agents** (checklist quotidienne : pilotage-agents, Conseiller → Chef de Projet → RACI, 12 règles Cursor, Orchestrateur + Chef de Projet veillent au « ne pas écrire pour écrire »). Les 12 règles Cursor (automatizer, conseiller, coordination-agents, devops, editorial, expert-google-dorks-linkedin, expert-seo-ai-geo, growth, growth-analyst, orchestrateur, pentester, pilotage-agents) sont alignées avec `agents-roles-responsabilites.md`.
- *Précédent* (2025-02-02) : Création du **registre erreurs et solutions** (`erreurs-et-solutions.md`) — répertorier les erreurs rencontrées et les solutions trouvées pour guider les agents et éviter de reproduire les erreurs. Responsabilité : agent qui assiste le Chef de Projet (mise à jour au fil des corrections) ; tous les agents consultent et peuvent contribuer. Références dans agents-roles-responsabilites (Chef de Projet, RACI), registre (§ 3 Chef de Projet, § Tous les agents), pilotage-agents.mdc.
- *Précédent* : 2025-01-30 — Ajout **Growth Analyst** (sous-assistant du Growth) : règle `growth-analyst.mdc`, doc `growth-analyst-concurrentiel-marche-ads.md` (études concurrentielles, SWOT, funnel, positionnement, marché, KPIs/leviers, campagnes Ads, nouveaux marchés). Registre § 1, § 2, § 3, § 5 mis à jour ; agents-roles-responsabilites (rôle 5b, RACI, workflow Phase 2, § Growth) et growth.mdc (sous-assistant) mis à jour.
- *Précédent* : Création de **`info-automatizer-pour-equipe.md`** (briefing pour l'équipe : qui est l'Automatizer, quand le solliciter, quelles ressources). Registre § 3 (Tous les agents, DevOps, Automatizer, tableau Stratégie et enrichissement) mis à jour ; sprint équipe technique et segmentations lancement/montage mis à jour pour que Growth, DevOps, Dev Django, Pentester collaborent avec Automatizer.
- *Précédent* : Ajout rôle **Automatizer** (règle `automatizer.mdc`) : N8N, Flowise, LLM/big data, MCP, flux API Python/Django, développement et maintenance workflows, monitoring, optimisation tokens, traces performances pour rapports data-driven. Registre § 1, § 2, § 3 mis à jour ; agents-roles-responsabilites et RACI à jour.
- *Précédent* : Synchronisation avant premier commit : base de connaissances (decisions.md : environnement Docker web, Git LPPP + SSH SquidResearch, politique credentials, montage projet), logs (log-projet, log-ia), TODO (Git init + premier commit + push en cours), boîte à idées (dernière sync). Git : URLs GitHub/GitLab configurées, réutilisation clés SSH SquidResearch (git-remotes-github-gitlab.md, environnement-wsl-linux.md, infra-devops.md). Montage projet : segmentation ecrans-routes-logique, doc routes-back-lppp.md.

*Document maintenu par l’Orchestrateur. Consulter `.cursor/rules/orchestrateur.mdc` pour le rôle et les responsabilités.*
