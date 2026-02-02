# TODO LPPP

Liste de tâches (maintenue par le chef de projet / agent pilote).

**Environnement choisi** : **Docker web** (conteneur web, pas runserver local). **Git init + premier commit + push** : fait (GitHub origin + GitLab gitlab, SSH SquidResearch).

**Sprint en cours** : toute l'équipe technique mobilisée — voir `docs/base-de-connaissances/segmentations/2025-01-30-sprint-equipe-technique.md`.

**Mobilisation agents système et connexions** : **DevOps, Dev Django, Pentester** sont mobilisés pour **réparer et lancer** le conteneur, le backend, le front et l’admin. Voir `2025-01-30-lancement-docker-projet.md`. **Montage du projet** : Orchestrateur, Chef de Projet, Data Analyst, Dev Django, DevOps — écrans, concordance des routes back, logique métier. Voir `2025-01-30-montage-projet-ecrans-routes-logique.md` et `routes-back-lppp.md`.

| Statut   | Tâche | Priorité |
|----------|--------|----------|
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

*Ajouter les nouvelles tâches en tête du tableau ; marquer « Fait » quand terminé.*
