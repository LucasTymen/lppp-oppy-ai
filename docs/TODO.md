# TODO LPPP

Liste de tâches (maintenue par le chef de projet / agent pilote).

**Environnement choisi** : **Docker web** (conteneur web, pas runserver local). **Git init + premier commit + push** : fait (GitHub origin + GitLab gitlab, SSH SquidResearch).

**Sprint en cours** : **URGENT — Revoir les routages des conteneurs** (toute l’équipe) — `segmentations/2026-02-05-sprint-urgent-routage-conteneurs.md`. Consulter le log commun SquidResearch et appliquer sa recommandation ; étude d’impact : `etude-impact-risques-routage-conteneurs-lppp.md`. En parallèle : relance démo + chatbot LPP agents municipaux. — voir `docs/base-de-connaissances/segmentations/2026-02-05-relance-projet-demo-chatbot-agents-municipaux.md`. Coordination : DevOps (relance stack, Flowise, .env), Automatizer (Flowise + n8n), Dev Django (embed, vue, template), Architecte, Designer, Chef de Projet.

**Mobilisation agents système et connexions** : **DevOps, Dev Django, Pentester** sont mobilisés pour **réparer et lancer** le conteneur, le backend, le front et l’admin. Voir `2025-01-30-lancement-docker-projet.md`. **Montage du projet** : Orchestrateur, Chef de Projet, Data Analyst, Dev Django, DevOps — écrans, concordance des routes back, logique métier. Voir `2025-01-30-montage-projet-ecrans-routes-logique.md` et `routes-back-lppp.md`.

| Statut   | Tâche | Priorité |
|----------|--------|----------|
| **À faire** | **Designer — Landing Promovacances (nav fixe, vidéo 100% + parallaxe, logo officiel)** : Brief `docs/contacts/promovacances/brief-designeur-nav-video-logo.md`. Navbar fixed top, vidéo hero 100% sans cadre noir, effet parallaxe, logo `https://upload.wikimedia.org/wikipedia/commons/8/8d/Promovacances.svg`. | **Haute** |
| **À faire** | **Rangement projet, landings et ressources (avis équipe)** : appliquer bonnes pratiques § 5 et 6 ; ranger racine, deploy/, docs/contacts, docs/ressources-utilisateur ; chaque agent nettoie derrière lui. Avis : `avis-equipe-rangement-projet-landings-ressources.md` ; tâches par rôle : `segmentations/2026-01-30-rangement-projet-landings-ressources.md`. | Moyenne |
| **À faire** | **Rapport synthétique Casapy (présentation)** : rapport pour responsable placement, patron / responsable alternance, référents. Rédacteur (responsable), Expert SEO (référent technique), Infographiste + chargé chiffres (illustrations). Brief `casapy/brief-rapport-synthetique-presentation.md`, sprint `segmentations/2026-01-30-rapport-synthetique-casapy-presentation.md`. Livrable : `rapport-synthetique-casapy-presentation.md` + visuels. | Moyenne |
| **À faire** | **Rapport SEO complet Casapy (pour moi seul)** : sprint commun pour agréger toutes les sources du dossier `docs/contacts/casapy/` en un rapport complet interne. Livrable : `rapport-seo-complet-casapy-interne.md`. Version présentation (résumée) plus tard. Segmentation : `segmentations/2026-01-30-sprint-rapport-seo-complet-casapy-pour-moi-seul.md`. | Moyenne |
| **À faire** | **Projet Casapy (LPPP)** : objectif et livrables à préciser — dossier `docs/contacts/casapy/`, segmentation `segmentations/2026-01-30-projet-casapy-lppp.md`. | Moyenne |
| **À faire** | **Portfolio Yuwell — remplissage contenu** : Rédacteur (textes 5 pages, Study case 2, À propos), Designer (hiérarchie, responsive, accessibilité), Expert SEO (titres, meta). Brief : `segmentations/2026-02-08-remplissage-contenu-portfolio-yuwell.md` ; source PDF + `etudes/yuwell-portfolio-etude-graphique.md`. | Moyenne |
| **À faire (priorité démo)** | **Relance projet** : `make ensure-env` puis `make up` (ou `make start`) ; en cas de conflit conteneurs : `make clean-containers` puis `make start`. Vérifier Django (8000), n8n (5678), Flowise (3000). Réf. segmentation `2026-02-05-relance-projet-demo-chatbot-agents-municipaux.md`. | **Haute** |
| Fait | **Landing Conciergerie dans l’admin** : migration 0004 (LandingPage maisons-alfort), redirection /maisons-alfort/ → /p/maisons-alfort/, flowise_embed_url dans landing_public. Template + vue renforcés (écran blanc / iframe vide) ; erreurs-et-solutions + sprint écran blanc. | — |
| **À faire (priorité démo)** | **Chatbot Flowise/n8n opérationnel sur LPP agents municipaux** : page `/p/maisons-alfort/` (ou `/maisons-alfort/`) doit afficher le chatbot (iframe Flowise), pas d’écran blanc ni erreur « adresse IP flowise ». Flowise LPPP = port **3010** ; `FLOWISE_CHATFLOW_ID` + `FLOWISE_URL=http://localhost:3010` dans .env. **Feature** : `segmentations/2026-01-30-feature-chatbot-landing-agents-municipaux.md` (Assistant, Architecte, Automatizer, Pentester ; non destructif ; réutilisable bots scraping). Chaîne n8n scrape → push Flowise. Voir même segmentation + `flowise-concierge-ia-maisons-alfort-guide.md`. | **Haute** |
| **À faire (reprise)** | **Scraper Concierge IA (n8n)** : réimporter le workflow `docs/n8n-workflows/concierge-ia-aspiration-maisons-alfort.json` dans n8n, exécuter bout en bout, vérifier que le dernier nœud « Rapport run (scrape + Flowise) » produit `{ run, scrape, flowise }`. Optionnel : exporter/conserver les rapports run pour traçabilité. Voir `guide-equipe-scraper-n8n-flowise.md`. | Moyenne |
| **À faire immédiatement** | **Modifications landing visibles** : appliquer la procédure `procedure-modifications-landing-visible.md` — après édition du JSON lancer `create_landing_p4s --update` ; recharger sans cache (Ctrl+Shift+R). Headers anti-cache déjà ajoutés sur la vue landing. | **Urgent** |
| Fait     | **Git init + premier commit + push** : Git initialisé, remotes SSH (origin GitHub, gitlab GitLab), commit 67a2055 (125 fichiers), push origin main et push gitlab main réussis. | — |
| À faire  | **Montage projet** : Orchestrateur, Chef de Projet, Data Analyst, Dev Django, DevOps — écrans, concordance des routes back, logique métier ; segmentation `2025-01-30-montage-projet-ecrans-routes-logique.md`, doc `routes-back-lppp.md` | Haute |
| À faire  | **Lancement stack** : DevOps + Dev Django + Pentester — réparer et lancer conteneur, backend, front, admin (localhost/127.0.0.1:8080 ou 8000) ; segmentation `2025-01-30-lancement-docker-projet.md` | Haute |
| À faire  | **Premier rapport SEO P4S-archi** : Expert SEO — rapport à partir des 5 CSV Screaming Frog + analyse sémantique ; livrable `docs/contacts/p4s-archi/rapport-seo.md` | Haute |
| À faire  | **Étude Growth P4S-archi** : Growth — étude poussée KPIs + funnel d'acquisition ; livrable `docs/contacts/p4s-archi/etude-growth-funnel-kpis.md` | Haute |
| Fait     | **Template proposition + landing P4S** : structure Full-Stack Conversion (hero, pain points, solution, services onglets, expertise stack, mission flash, why GE), CSS Vampire, Google Fonts, liste landings par secteur/société ; commande create_landing_p4s ; doc schema-landing-proposition.md, css-vampire.md | — |
| —        | *(Git init : voir tâche « Git init + premier commit + push » en tête)* | — |
| À faire  | Relance événements : template landing relance salon + structure content_json (hero, CTA, positionnement freelance/alternant) | Haute |
| À faire  | Interface landingsgenerator : app Django /essais/, mobile-first, dark + switch clair/sombre, premier écran présentation relance salon | Haute |
| À faire  | Rapport SEO prospect : rapport présentable (pas stockage), CSV Screaming Frog, manque à gagner, coût SEO pourri | Moyenne |
| Fait     | Système de coordination des agents (rôles, RACI, segmentation) | — |
| À faire  | **Stack frontend Next.js + React** : migrer/développer les landings en Next.js + React (effet waouh, déploiement Vercel) — voir `stack-frontend-nextjs-react.md` | Haute |
| À faire  | Moderniser les landing pages (système de templates multiples, composants React) | Haute |
| À faire  | Implémenter Tailwind CSS (design system moderne, avec Next.js) | Haute |
| À faire  | Créer composants React réutilisables (hero, CTA, formulaires) pour Next.js | Haute |
| À faire  | Ajouter analytics et tracking (taux de conversion) | Moyenne |
| À faire  | Appliquer l'éditorial anti-détection aux contenus des landing pages existantes (si besoin) | Moyenne |
| À faire  | Exposer score / qualité dans l'admin (Prospect, campagnes) ou vues (optionnel) | Basse |
| Fait     | Créer base de connaissances, logs, bonnes pratiques, règles agent | — |
| Fait     | Rédiger bonnes pratiques éditoriales (anti-détection IA, humanisation) | — |
| Fait     | Créer règles .cursor/rules (anti-hallucination, data-driven) | — |
| Fait     | Créer log projet, log IA, TODO, boîte à idées | — |
| Fait     | Intelligence métier : app apps.intelligence (scoring, qualité, matching), doc intelligence-metier-algorithmes.md, branchement nodes | — |
| Fait     | Créer .env.example et .gitignore (infra DevOps) | — |
| Fait     | **Scraper Concierge IA finalisé (n8n)** : workflow `concierge-ia-aspiration-maisons-alfort.json` avec collecte des deux résultats (scrape Django + Flowise) via nœud Merge + « Rapport run » ; sortie finale `{ run, scrape: { pageCount, urls, errors }, flowise: { file, numAdded } }`. Guide équipe et README n8n-workflows mis à jour. | — |

*Ajouter les nouvelles tâches en tête du tableau ; marquer « Fait » quand terminé.*
