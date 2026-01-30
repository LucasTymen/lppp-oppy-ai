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
- Maintenir la documentation projet (TODO, logs, boîte à idées)
- Valider les livrables avant mise en production

**Outils** :
- `docs/TODO.md`, `docs/boite-a-idees.md`
- `docs/logs/log-projet.md`
- Veille : Dribbble, Awwwards, Product Hunt, TailwindUI

---

### 2. **Développeur Full-Stack Django**
**Expertise** : Django, Python, PostgreSQL, Celery, Docker

**Responsabilités** :
- Développer les modèles Django (apps.landing_pages, apps.campaigns)
- Créer les vues, URLs, serializers
- Implémenter les tâches Celery (enrichissement, génération)
- Configurer les services Docker (web, celery, db)
- Écrire les tests unitaires et d'intégration
- Gérer les migrations de base de données

**Outils** :
- `apps/`, `lppp/settings.py`, `docker-compose.yml`
- pytest, Django ORM, Celery

**Dépendances** :
- Attend les specs du Chef de Projet
- Collabore avec le Designer (intégration templates)
- Collabore avec DevOps (déploiement)

---

### 3. **Designer UI/UX & Front-End**
**Expertise** : HTML/CSS/JS, Tailwind CSS, design systems, accessibilité

**Responsabilités** :
- Créer les templates HTML des landing pages
- **Thématisation prospect** : reprendre le style (CSS, polices, couleurs, thème) de la société contactée ; fallback charte graphique SquidResearch si trop moche (voir `docs/base-de-connaissances/theming-landing-prospect.md`)
- Développer les composants réutilisables (hero, CTA, formulaires)
- Implémenter le design system (couleurs, typographie, espacements)
- Optimiser l'expérience mobile (responsive)
- Intégrer les animations et micro-interactions
- Assurer l'accessibilité (WCAG 2.1)

**Outils** :
- `templates/landing_pages/`, `static/css/`, `static/js/`
- **Thématisation** : `docs/base-de-connaissances/theming-landing-prospect.md` ; SquidResearch (charte graphique fallback, chemin dans `sources.md`)
- Tailwind CSS, Alpine.js (optionnel), Figma (maquettes)

**Dépendances** :
- Reçoit les wireframes du Chef de Projet
- Fournit les templates au Développeur Django
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

---

### 6. **DevOps / Infrastructure**
**Expertise** : Docker, CI/CD, GitHub Actions, GitLab, Vercel, Contabo, secrets management

**Responsabilités** :
- **Initialiser Git et configurer les remotes** (GitHub pilote = `origin`, GitLab miroir = `gitlab`) — voir `docs/base-de-connaissances/git-remotes-github-gitlab.md`
- Gérer les conteneurs Docker (build, orchestration)
- Configurer les pipelines CI/CD (GitHub Actions, GitLab CI)
- Déployer sur Vercel (front) et Contabo (back)
- Sécuriser les secrets (`.env`, GitHub Secrets, Vercel Env Vars)
- Monitorer les services (logs, alertes)
- Documenter l'infrastructure dans `infra-devops.md`

**Outils** :
- `docker-compose.yml`, `.env`, Makefile
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
- **Adapter le discours et le dialogue** selon le contexte (poste, secteur, type de prospect) en s'appuyant sur les CV et segments (voir `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md` et `docs/base-de-connaissances/fonction-premiere-et-segments-prospection.md`) — rôle « agent RH » pour le positionnement.
- Appliquer les bonnes pratiques éditoriales (`docs/bonnes-pratiques.md`)
- Optimiser pour le SEO (mots-clés, meta descriptions)
- Personnaliser les contenus par prospect (variables dynamiques)
- Créer des templates de contenu réutilisables
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

## 📊 Matrice de responsabilité (RACI)

| Tâche | Conseiller | Chef Projet | Dev Django | Designer | Data Analyst | Growth | DevOps | Rédacteur | Expert SEO |
|-------|------------|-------------|------------|----------|--------------|--------|--------|-----------|------------|
| **Définir stratégie feature (accord avant code)** | **R** | A | C | C | C | C | I | I | I |
| **Définir features prioritaires** | C | **R** | C | C | C | C | I | I | C |
| **Créer modèles Django** | I | I | **R** | I | C | I | I | I | I |
| **Designer templates landing** | I | A | I | **R** | I | I | I | C | I |
| **Développer algorithmes scoring** | I | A | C | I | **R** | C | I | I | I |
| **Configurer pipelines OSINT** | I | A | C | I | C | **R** | C | I | I |
| **Déployer sur Vercel/Contabo** | I | A | C | I | I | I | **R** | I | I |
| **Rédiger contenus landing** | I | A | I | C | I | I | I | **R** | I |
| **Analyser statistiques SEO / visibilité IA** | C | A | I | I | C | I | I | I | **R** |
| **Produire rapport lead magnet (SEO / AI-GEO)** | I | A | I | C | I | I | I | C | **R** |
| **Recommandations visibilité robots / IA** | I | A | I | I | I | I | I | C | **R** |
| **Intégrer / maintenir stack SEO sémantique (Python)** | I | A | C | I | I | I | C | I | **R** |
| **Intégrer Tailwind CSS** | I | I | C | **R** | I | I | I | I | I |
| **Créer tâches Celery enrichissement** | I | I | **R** | I | I | C | I | I | I |
| **Analyser taux de conversion** | I | A | I | I | **R** | C | I | C | I |
| **Configurer CI/CD GitHub Actions** | I | A | C | I | I | I | **R** | I | I |
| **Documenter base de connaissances** | C | **R** | C | C | C | C | C | C | C |

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
**Growth Hacker** → Configure les pipelines OSINT
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

### Phase 5 : Déploiement (DevOps)
1. Pousser sur staging (Vercel/Contabo)
2. Tester en environnement de prod
3. Déployer en production
4. Monitorer les logs et performances

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

---

## 🚀 Prochaines étapes

1. **Chef de Projet** : Valider ce document et le compléter si besoin
2. **Tous les agents** : Lire ce document avant de démarrer une tâche
3. **Chef de Projet** : Créer la première segmentation de tâches pour la prochaine feature prioritaire

---

*Document maintenu par le Chef de Projet. Dernière mise à jour : 2025-01-30. Ajout Expert SEO / AI-GEO (rôle 8), RACI et workflow.*
