# Base de connaissances LPPP

Dépôt des **faits vérifiés**, **sources** et **décisions** du projet. Toute affirmation doit pouvoir être rattachée à une source ou une décision enregistrée ici.

## Règles d’usage

- **Pas d’affirmation sans source** : chiffres, fonctionnalités, stack → document ou décision écrite.
- **Mise à jour** : le chef de projet / agent pilote actualise après chaque session ou décision.
- **Fichiers** :
  - `registre-agents-ressources.md` : **registre temps réel** — tous les agents, règles Cursor, ressources par pilote (maintenu par l’orchestrateur ; à consulter pour savoir quelles ressources sont à disposition).
  - `decisions.md` : décisions d’architecture, de stack, de process.
  - `sources.md` : liens et refs (SquidResearch, Django, etc.).
  - `agents-roles-responsabilites.md` : 7 rôles, matrice RACI, workflow.
  - `intelligence-metier-algorithmes.md` : stratégie matching, scoring, qualité données, implantation des algorithmes (app `apps.intelligence`).

## Référence projet

- **LPPP** : Landings Pages Pour Prospections — prospection via landing pages personnalisées + scraping/enrichment.
- **Environnement** : WSL ou Linux préféré — voir `environnement-wsl-linux.md`.
- **Stack** : Django, Celery, PostgreSQL, Redis, n8n, Flowise, ENRICHED (scraping), Docker. Voir `README.md` racine.
- **SquidResearch** : référence d’architecture (monorepo `apps/`, conteneurs, ENRICHED). Hors workspace LPPP ; chemin pour outils (template, copie de code) : **absolu** `/home/lucas/tools/squidResearch` (WSL : `\\wsl.localhost\Ubuntu-22.04\home\lucas\tools\squidResearch`). Bonnes pratiques éditoriales dans `../bonnes-pratiques.md`. Détail dans `sources.md`.
