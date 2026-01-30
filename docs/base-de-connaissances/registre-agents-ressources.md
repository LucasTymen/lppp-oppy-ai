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
| 5 | Growth Hacker / OSINT Specialist | `agents-roles-responsabilites.md` § Growth | `pilotage-agents.mdc`, `growth.mdc`, `expert-google-dorks-linkedin.mdc`, `pentester.mdc` |
| 6 | DevOps / Infrastructure | `agents-roles-responsabilites.md` § DevOps | `pilotage-agents.mdc`, `devops.mdc` |
| 7 | Rédacteur / Content Strategist | `agents-roles-responsabilites.md` § Rédacteur | `pilotage-agents.mdc`, `editorial.mdc` |
| 8 | Expert SEO / AI-GEO | `agents-roles-responsabilites.md` § Expert SEO | `pilotage-agents.mdc`, `expert-seo-ai-geo.mdc` |

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

---

## 3. Ressources par pilote (Chef de Projet, Stratégie, DevOps)

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
- **SEO sémantique (outils open-source)** : `docs/base-de-connaissances/seo-semantique-outils-open-source.md` — stack Python (spaCy, Gensim, NLTK, Transformers), keyword-to-topic, topic modelling, clustering ; coordination DevOps / Dev Django.
- **Dépendances optionnelles** : `requirements-seo.txt` (racine) — à intégrer dans l’env ou Docker en accord avec DevOps.
- **Ressources utilisateur** : `docs/ressources-utilisateur/` (stats, données fournies par l’utilisateur pour l’analyse)
- **Bonnes pratiques** : `docs/bonnes-pratiques.md` (éditorial, humanisation du rapport lead magnet)
- **Décisions** : `docs/base-de-connaissances/decisions.md`
- **Règle** : `.cursor/rules/expert-seo-ai-geo.mdc`
- **Collaboration** : Conseiller (point d’entrée, stats), Chef de Projet (validation, intégration landing), Orchestrateur (registre), Rédacteur / Designer (intégration onglet lead magnet), **DevOps** (stack SEO sémantique, dépendances, Docker), **Dev Django** (intégration code, module, commandes)

### Chef de Projet / Stratégie

- **Rôles et RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Registre (ce fichier)** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Segmentations** : `docs/base-de-connaissances/segmentations/` (TEMPLATE.md + fichiers `YYYY-MM-DD-nom-feature.md`)
- **TODO et idées** : `docs/TODO.md`, `docs/boite-a-idees.md`
- **Logs** : `docs/logs/log-projet.md`, `docs/logs/log-ia.md`
- **Décisions et sources** : `docs/base-de-connaissances/decisions.md`, `sources.md`
- **Guides** : `docs/GUIDE-CHEF-PROJET.md`, `docs/GUIDE-AGENTS.md`
- **Règles** : `.cursor/rules/pilotage-agents.mdc`, `coordination-agents.mdc`, `orchestrateur.mdc`

### DevOps

- **Environnement WSL/Linux** : `docs/base-de-connaissances/environnement-wsl-linux.md` — environnement préféré, chemins, prérequis, démarrage.
- **Infra et secrets** : `docs/base-de-connaissances/infra-devops.md`
- **Stratégie opérationnelle Make** : `docs/base-de-connaissances/strategie-operationnelle-make.md` — catalogue des commandes `make`, workflows (lancement, migrations, mise à jour, contrôle), répartition des responsabilités (DevOps, Dev Django, Chef de Projet). `make help` pour l'aide.
- **Tâche prioritaire (mobilisation système et connexions)** : `docs/base-de-connaissances/segmentations/2025-01-30-lancement-docker-projet.md` — réparer et lancer conteneur, backend, front, admin (avec Dev Django, Pentester) ; Option B runserver si ERR_EMPTY_RESPONSE sous Windows.
- **URGENT — Git (init, remotes GitHub/GitLab)** : `docs/base-de-connaissances/git-remotes-github-gitlab.md` — GitHub pilote (`origin`), GitLab miroir (`gitlab`) ; tâche **à exécuter en priorité** : `2025-01-30-devops-git-init-remotes.md` (signalé par l’utilisateur).
- **Règle** : `.cursor/rules/devops.mdc`
- **Orchestration** : `docker-compose.yml`, `.env` (non versionné), CI/CD (GitHub Actions, etc.)
- **Registre** : ce fichier (pour connaître les agents et impacts sur les services)

### Tous les agents

- **Fiche de rôle** : `docs/base-de-connaissances/agents-roles-responsabilites.md`
- **Registre des ressources** : ce fichier
- **Segmentations** : `docs/base-de-connaissances/segmentations/` (dont `2025-01-30-montage-projet-ecrans-routes-logique.md` — **montage projet** : Orchestrateur, Chef de Projet, Data Analyst, Dev Django, DevOps pour écrans, concordance des routes back, logique métier ; `2025-01-30-lancement-docker-projet.md` — mobilisation système et connexions ; `2025-01-30-premier-rapport-seo-landing-p4s-archi.md` ; `2025-01-30-interface-landingsgenerator.md`, `2025-01-30-devops-git-init-remotes.md`, `2025-01-30-relance-evenements.md`)
- **Concordance des routes back** : `docs/base-de-connaissances/routes-back-lppp.md` — source de vérité URLs ; maintenu par Dev Django et DevOps.
- **Prêt à démarrer** : `docs/base-de-connaissances/pret-a-demarrer.md` — venv, Docker, dev local SQLite, tester l’admin, première landing
- **Réponses validées** : `docs/base-de-connaissances/reponses-validees-strategie.md`
- **Rapport SEO prospect** : `docs/base-de-connaissances/rapport-seo-prospect.md`
- **Dossiers contacts** : `docs/contacts/` — un dossier par contact (prospect) pour ses données ; règle `organisation-donnees-contacts.md`, registre `docs/contacts/REGISTRE-CONTACTS.md`
- **Ressources utilisateur** : `docs/ressources-utilisateur/` (REGISTRE-RESSOURCES.md pour retrouver textes, images, ébauches, études transmis par l’utilisateur)
- **Bonnes pratiques** : `docs/bonnes-pratiques.md`
- **Règles** : `.cursor/rules/` (voir tableau § 2)

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
| `bibliotheques-agents-techniques.md` | Tour des libs spécialisées (pandas, numpy, scraping, viz) — besoins agents techniques, sans overkill | Chef de Projet, DevOps, Data Analyst, Expert SEO, Growth |
| `strategie-enrichissement.md` | Anti-blocage, une tâche = un outil, fusion + intelligence métier | Growth, Expert Google Dorks, Pentester |
| `enrichissement-osint-flowise-n8n.md` | API webhook, N8N/Flowise, guide-rails | Growth, DevOps |
| `intelligence-metier-algorithmes.md` | Scoring, qualité, matching | Data Analyst, Dev Django |
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

## 6. Dernière mise à jour

- **Date** : 2025-01-30  
- **Modifications** : Synchronisation avant premier commit : base de connaissances (decisions.md : environnement Docker web, Git LPPP + SSH SquidResearch, politique credentials, montage projet), logs (log-projet, log-ia), TODO (Git init + premier commit + push en cours), boîte à idées (dernière sync). Git : URLs GitHub/GitLab configurées, réutilisation clés SSH SquidResearch (git-remotes-github-gitlab.md, environnement-wsl-linux.md, infra-devops.md). Montage projet : segmentation ecrans-routes-logique, doc routes-back-lppp.md.

*Document maintenu par l’Orchestrateur. Consulter `.cursor/rules/orchestrateur.mdc` pour le rôle et les responsabilités.*
