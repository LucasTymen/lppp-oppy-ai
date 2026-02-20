# Registre erreurs et solutions LPPP

**Objectif** : Répertorier les erreurs rencontrées et les solutions trouvées pour éviter de les reproduire et guider les agents qui rencontrent des soucis.

**Maintenu par** : **Agent en charge des erreurs** (qui assiste le Chef de Projet) — mise à jour au fur et à mesure des corrections ; il actualise aussi la base de connaissances (voir § ci-dessous).  
**Consulté par** : Tous les agents — en cas de blocage ou d’erreur, consulter ce registre avant de réinventer ; après une correction, ajouter une entrée.  
**Référence** : `agents-roles-responsabilites.md` (§ Chef de Projet, RACI « Documenter erreurs et solutions »), `pilotage-agents.mdc` (Data-driven et logs).

---

## Comment utiliser ce registre

### Pour un agent qui rencontre une erreur
1. **Consulter ce fichier** : chercher une entrée similaire (contexte, message d’erreur, stack).
2. Si une entrée existe : appliquer la solution et les précautions indiquées.
3. Si aucune entrée : après résolution, **ajouter une entrée** (voir format ci‑dessous) et mettre à jour les logs (`log-projet.md` ou `log-ia.md`).

### Pour l’agent en charge des erreurs (qui assiste le Chef de Projet)
- **À chaque correction d’erreur** : ajouter ou compléter une entrée dans ce registre et mettre à jour les logs pour que l’équipe ne reproduise pas l’erreur.
- **Sauvegarde incrémentale et reprise** : s’assurer que les agents appliquent la règle « Sauvegarde incrémentale obligatoire » (`pilotage-agents.mdc`) : sauvegarder à chaque étape, marquer la progression avec des timestamps en commentaire, retirer les marqueurs une fois la tâche terminée. En cas de crash ou de reprise (ex. création landing interrompue 4–5 fois), **reprendre au dernier marqueur** au lieu de recommencer du début ; documenter l’état dans ce registre si besoin.
- **Actualiser la base de connaissances** : selon le cas — mettre à jour ou créer les docs concernés dans `docs/base-de-connaissances/` : `decisions.md` (décision liée à l’erreur ou à la prévention), `sources.md` si une source externe est utilisée, procédures dédiées, segmentations si une équipe est mobilisée, et le **registre agents/ressources** si une nouvelle ressource ou référence est créée. L’objectif est que la correction et sa prévention soient retrouvables par tous les agents.
- **Interaction** : le Chef de Projet valide que la doc est à jour ; l’Orchestrateur peut référencer ce doc dans le registre agents/ressources.
- **Lors de cartographies ou diagnostics** (Pentester, DevOps, Ingénieur système & réseaux) : toute erreur identifiée pendant une cartographie (nmap, tests de flux, analyse réseau) doit être **remontée au responsable de la consignation des erreurs** pour **répertoriation** dans ce registre (nouvelle entrée ou complément). Chaque rôle contribue avec ses tests et son expertise ; le responsable consignation centralise et documente ici.
- **Règle projet — barres de navigation** : les **barres de navigation** doivent **toujours être en sticky** (rester visibles en haut au scroll). À appliquer **systématiquement** sur toute page publique qui a une nav ; quand ce n’est pas fait, **le noter et le corriger**. Voir l’entrée « Barres de navigation — toujours en sticky » ci‑dessous.

---

## Format d’une entrée

Pour chaque erreur documentée, indiquer :

| Champ | Description |
|-------|-------------|
| **Date** | Date de la correction ou de la première occurrence documentée |
| **Contexte** | Où / quand ça se produit (WSL, Docker, commande, page, etc.) |
| **Erreur** | Message d’erreur ou symptôme (copier-coller si pertinent) |
| **Cause** | Cause identifiée (optionnel mais utile) |
| **Solution** | Étapes ou correctif appliqué |
| **Prévention** | Comment éviter que ça se reproduise (doc, procédure, checklist) |
| **Lien(s)** | Vers une doc ou procédure dédiée (ex. `environnement-wsl-linux.md`) |

---

## Entrées

*(Les entrées seront ajoutées au fur et à mesure des corrections.)*

### Page instable (local ou Vercel) — diagnostic DevOps / Architecte / Ingénieur Sys

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Landing Promovacances (ou autre) : page « instable » — connexion intermittente, layout shift, 404, lenteur, erreur réseau. |
| **Erreur** | Connexion refusée / reset (local) ; layout qui bouge (CLS) ; 404 ; contenu qui ne se charge pas ou s’affiche lentement. |
| **Cause** | Local : conteneurs orphelins, port occupé, web en crash loop, base vide. Vercel : rewrites manquants, images sans dimensions, cache, build échoué. |
| **Solution** | Suivre la **segmentation** `segmentations/2026-01-30-sprint-page-instable-promovacances-devops-archi.md` : checklist diagnostic (local vs Vercel), actions correctives (clean-containers, landings-restore, vercel.json, CLS/LCP). |
| **Prévention** | DevOps / Architecte / Ingénieur Sys appliquent la checklist dès signalement « page instable » ; documenter toute nouvelle cause dans ce registre. |
| **Lien(s)** | `segmentations/2026-01-30-sprint-page-instable-promovacances-devops-archi.md`, `erreurs-et-solutions.md` (Docker, 404, Postgres), `procedure-modifications-landing-visible.md` |

### Barres de navigation — toujours en sticky

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Toute page publique avec une barre de navigation (landings, rapport, prospects, proposition de valeur, dashboard audit, Yuwell, etc.). |
| **Erreur** | Nav qui défile avec la page au lieu de rester visible en haut — mauvaise UX pour la navigation. |
| **Cause** | Oubli de `position: sticky; top: 0` (et z-index si besoin) sur l’élément nav/header. |
| **Solution** | Appliquer sur la nav : `position: sticky; top: 0; z-index: 100` (ou équivalent), et un fond/backdrop pour la lisibilité. |
| **Prévention** | **L’agent en charge des erreurs** (et tout agent qui crée ou modifie un template avec barre de navigation) doit **prendre en note** : les **barres de navigation doivent toujours être en sticky** ; appliquer **systématiquement** ; quand ce n’est pas fait, **le corriger**. Règle projet pour une navigation optimale. |
| **Lien(s)** | Templates : `proposition.html`, `rapport.html`, `prospects.html`, `proposition_value.html`, `includes/nav_landing_annexes.html`, `yuwell_base.html`, `yuwell_portfolio.html`, `seo_audit_dashboard.html`, `casapy_audit_dashboard.html`. |

### Barre de navigation décalée — body padding-top à 0

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-20 |
| **Contexte** | Pages positionnement-marketing, infographie-\*-7-formats et toute page avec nav sticky/fixed. |
| **Erreur** | Nav visuellement décalée (bande blanche ou vide au-dessus) — la nav n'est pas collée tout en haut du viewport. |
| **Cause** | `body { padding-top: 60px }` (ou autre valeur) qui pousse tout le contenu vers le bas. La nav est bien sticky/fixed mais le body a un décalage inutile. |
| **Solution** | **Remplacer** `body { padding-top: 60px }` par `body { padding-top: 0 }`. Pour la nav fixed, le contenu sous la nav doit avoir son propre `padding-top` (ex. `.site-content-inner { padding-top: 80px }` ou `main { padding-top: 52px }`), pas sur le body. |
| **Prévention** | **Graphiste / Designer** : vérifier chaque nouvelle page — nav collée en haut = `body { padding-top: 0 }`. **Chef de Projet / Architecte** : auditer toutes les pages du site (Infopro, Promovacances, Casapy, etc.) et corriger systématiquement. |
| **Lien(s)** | `docs/contacts/infopro/positionnement-marketing.html`, `docs/contacts/promovacances/positionnement-marketing.html`, `decisions.md` (Barres de navigation toujours en sticky). |

### Django / Docker — failed to resolve host 'db' ; service "web" is not running

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-19 |
| **Contexte** | LPPP — commande `python3 manage.py create_landing_promovacances --publish` en WSL, ou `make landing-promovacances` sans stack démarré. |
| **Erreur** | `psycopg.OperationalError: failed to resolve host 'db': [Errno -3] Temporary failure in name resolution` ; ou `service "web" is not running`. |
| **Cause** | La config Django utilise le host `db` (service Docker). En dehors du réseau Docker, ce hostname n'existe pas. La commande doit être exécutée **dans le conteneur** `web`. De plus, le stack (db, redis, web) doit être démarré avant. |
| **Solution** | 1. Se placer à la **racine LPPP** (répertoire contenant `Makefile`, `manage.py`, `docker-compose.yml`). 2. Démarrer le stack : `make start`. 3. Créer la landing : `make landing-promovacances`. **En une commande** : `make landing-promovacances-full` (enchaîne start puis création). |
| **Prévention** | Toute commande Django qui touche à la base doit être lancée soit dans le conteneur (`docker compose exec web python manage.py ...`), soit via une cible Make qui le fait. Voir stratégie opérationnelle Make. |
| **Lien(s)** | `segmentations/2026-02-19-landing-promovacances-creation-coordonnee.md`, `strategie-operationnelle-make.md`, `docs/contacts/promovacances/README.md` |

### Docker — container name "/lppp_redis" (or lppp_db, etc.) already in use

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-19 |
| **Contexte** | LPPP — `make start` ou `make landing-promovacances-full` ; démarrage séquentiel `docker compose up -d db redis`. |
| **Erreur** | `Error response from daemon: Conflict. The container name "/lppp_redis" is already in use by container "c8bb53441ae6...". You have to remove (or rename) that container to be able to reuse that name.` |
| **Cause** | Conteneur orphelin (ancienne session, arrêt brutal, ou autre projet) qui garde le nom attendu par ce projet. |
| **Solution** | Supprimer les conteneurs LPPP concernés puis relancer : `make clean-containers` puis `make start` (ou `make landing-promovacances-full`). En une ligne : `make clean-containers && make landing-promovacances-full`. |
| **Prévention** | En fin de session, privilégier `make down` pour arrêter proprement. En cas de conflit, `make clean-containers` est idempotent (ignore les conteneurs déjà absents). |
| **Lien(s)** | `segmentations/2026-02-19-landing-promovacances-creation-coordonnee.md`, Makefile cible `clean-containers` |

### 404 « No LandingPage matches the given query » après base vide (ex. volume recréé)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-19 |
| **Contexte** | Après `make clean-containers` puis `make start`, ou volume Postgres recréé. Les URLs /p/casapy/, /p/fitclem/ renvoient 404. |
| **Erreur** | `Page not found (404)` — `No LandingPage matches the given query.` (vue `landing_public`). |
| **Cause** | La base a été recréée vide. Les entrées `LandingPage` (Casapy, FitClem, etc.) sont créées par des **commandes** ou des **migrations**. Les migrations recréent Maisons-Alfort et Yuwell ; Casapy, FitClem et Promovacances doivent être recréés par les commandes. |
| **Solution** | À la racine LPPP, stack démarré : `make landings-restore`. Recrée Casapy, FitClem et Promovacances en base (--update --publish). Pour une seule landing : `make landing-promovacances` ou `docker compose exec web python manage.py create_landing_casapy --update --publish`, etc. |
| **Prévention** | Avant `make clean-containers`, faire `make backup` si tu veux restaurer les données. Sinon, après un start sur base vide, exécuter `make landings-restore`. |
| **Lien(s)** | Makefile cible `landings-restore`, `landing-promovacances`, `create_landing_casapy` |

### Next.js — Avis Red Hat / CVE (failles de sécurité, correctifs)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Avis Red Hat (ou autre scan de vulnérabilités) signalant des CVE sur Next.js (ex. 2 vulnérabilités medium sur `next@16.0.7`). |
| **Erreur** | Rapport du type : « 2 Unique vulnerabilities » sur `next`, « No remediations available » (Red Hat TPA). |
| **Cause** | Next.js 15.x / 16.x a connu des CVE (RSC DoS CVE-2025-55184, exposition de code source CVE-2025-55183, Image Optimizer DoS CVE-2025-59471). Les versions non mises à jour restent signalées comme vulnérables. |
| **Solution** | **Dans LPPP** (Next.js 15.1.x) : passer à **`next@15.1.11`** minimum (correctifs du 11 déc. 2025). **Si un autre projet utilise Next.js 16.0.7** : passer à **`next@16.1.5`** ou **`next@16.1.6`** (corrige 16.0.10 + Image Optimizer). Commandes : `npm install next@15.1.11` ou `npm install next@16.1.5` ; puis `npm audit` et redéploiement (ex. Vercel). Outil officiel : `npx fix-react2shell-next` pour vérifier et mettre à jour. |
| **Prévention** | Suivre les advisories Next.js : [nextjs.org/blog/security-update-2025-12-11](https://nextjs.org/blog/security-update-2025-12-11), [CVE-2025-66478](https://nextjs.org/blog/CVE-2025-66478). Vérifier périodiquement `npm audit` et les alertes Red Hat / Snyk sur les projets Next.js (LPPP et landings Vercel). |
| **Lien(s)** | `regles-securite.md`, `stack-frontend-nextjs-react.md`, [Next.js Security Advisories](https://github.com/vercel/next.js/security/advisories) |

### Vercel — Duplication de projets pointant vers le même repo GitHub

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Sur Vercel, plusieurs projets (ex. LPPP_promovacances, variantes) pointent vers le **même** repo GitHub. |
| **Erreur** | Doublons : plusieurs URLs (xxx.vercel.app) pour un même contenu ; confusion, dépenses ou build redondants. |
| **Cause** | Import multiple du même repo, ou projet recréé sans supprimer l’ancien. |
| **Solution** | 1) Vercel → Projects → lister les projets liés au repo concerné. 2) Conserver **un seul** (config correcte, déploiement récent). 3) Settings → General → **Delete Project** pour les doublons. 4) Documenter l’URL finale dans la fiche contact. Règle : **1 repo = 1 projet Vercel**. |
| **Prévention** | Avant de créer un nouveau projet Vercel, vérifier qu’aucun projet n’est déjà lié au repo. Voir `strategie-deploiement-git-vercel.md`. |
| **Lien(s)** | `segmentations/2026-01-30-sprint-urls-vercel-promovacances.md`, `strategie-deploiement-git-vercel.md` |

### Vercel — Incohérence URLs (Django vs statique)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Landing statique Promovacances sur Vercel : mélange d’URLs Django (`/p/promovacances/...`) et statiques (`rapport.html`). |
| **Erreur** | Liens cassés ou redondants ; texte qui mentionne une URL inexistante (ex. `/p/promovacances/audit-dashboard/`). |
| **Cause** | Contenu généré pour Django puis exporté en statique ; certains liens ou mentions restent en format Django. |
| **Solution** | Sur Vercel statique : **liens internes** = chemins relatifs (`rapport.html`, `positionnement-marketing.html`, etc.). Les rewrites `vercel.json` (`/p/promovacances/rapport/` → `/rapport.html`) servent aux liens externes. Corriger les mentions textuelles d’URL Django par l’équivalent statique (ex. `rapport.html#...`). |
| **Prévention** | Export statique : utiliser systématiquement des URLs relatives ; pas de `/p/<slug>/` dans les href sauf si rewrites prévus. |
| **Lien(s)** | `segmentations/2026-01-30-sprint-urls-vercel-promovacances.md`, `deploy/static-promovacances-vercel/vercel.json` |

### Vercel — Projets LPPP_* qui ne s'affichent plus dans le dashboard s’affichent plus dans le dashboard

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Sur Vercel (Lucas Tymen's projects), des projets dont le nom commence par **LPPP_** semblent avoir disparu de la liste (comparaison avec une vue antérieure ou « 4 commits avant »). |
| **Erreur** | Projets landing LPPP_* absents de la liste des projets Vercel. |
| **Cause** | Les commits Git ne modifient pas la liste des projets Vercel. Une disparition vient en général de : projet **supprimé** ou **déconnecté** sur Vercel, filtre/vue (list vs grid), ou autre compte/équipe. Les 7 projets LPPP_* documentés (P4S, Ackuracy, Yuwell, FitClem, 0flow, Maisons-Alfort, Orsys) sont listés dans `deploy/README-standalone.md` et `strategie-deploiement-git-vercel.md`. |
| **Solution** | 1) **Vérifier sur GitHub** : [github.com/LucasTymen](https://github.com/LucasTymen?tab=repositories) → filtrer par « LPPP » ; lister tous les repos `LPPP_*`. 2) **Réimporter sur Vercel** : Add New → Project → Import Git Repository → choisir le repo GitHub manquant ; configurer (Root Directory, Framework Other si statique). 3) Vérifier la vue (list/grid) et qu’aucun filtre ne cache des projets. |
| **Prévention** | Documenter tout nouveau repo LPPP_* dans `deploy/README-standalone.md` et dans la stratégie Git/Vercel ; en cas de doute, comparer la liste GitHub (LPPP_*) à la liste des projets Vercel. |
| **Lien(s)** | `deploy/README-standalone.md`, `strategie-deploiement-git-vercel.md` |

### WSL/Linux : « python: command not found » — toujours utiliser python3

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-06 |
| **Contexte** | WSL (ou Linux), exécution de commandes Django depuis l’hôte (migrate, runserver, etc.). |
| **Erreur** | `zsh: command not found: python` ou `python: command not found`. |
| **Cause** | Sur WSL/Ubuntu (et beaucoup de distributions Linux), la commande système officielle est **`python3`**. La commande `python` n’est pas installée ou n’est pas dans le PATH. |
| **Solution** | **Toujours** utiliser **`python3`** pour les commandes sur l’hôte : `python3 manage.py migrate`, `python3 manage.py runserver`, `python3 -c "..."`. Ne jamais donner d’instruction avec `python` seul. |
| **Prévention** | Règle projet : **ne jamais proposer ou documenter une commande Python sur l’hôte sans utiliser `python3`**. Voir `.cursor/rules/pilotage-agents.mdc` (§ Terminal — Python sur l’hôte), `environnement-wsl-linux.md`. Dans les conteneurs Docker, `docker compose exec web python ...` reste valide (image avec `python` en symlink). **Si en plus** `python3 manage.py migrate` échoue avec « Connection refused » (port 5432) : la base PostgreSQL n’est pas démarrée — lancer `make up` ou `docker compose up -d db redis`, attendre quelques secondes, puis réessayer ; ou exécuter la migration dans le conteneur : `docker compose exec web python manage.py migrate`. |
| **Lien(s)** | `environnement-wsl-linux.md`, `pilotage-agents.mdc` |

### Infographies Casapy ne s'affichent pas (localhost ou page vide)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-19 |
| **Contexte** | Landing Casapy (`/p/casapy/`) : les infographies (slide*.png, one-pager, wave) sont codées mais ne s'affichent pas dans le navigateur. |
| **Erreur** | Images cassées (icône broken) ou emplacements vides ; ou requêtes vers `/p/casapy/assets/slide1.png` qui renvoient du HTML au lieu du PNG. |
| **Cause** | **Ordre des routes Django** : la route générique `p/<slug:slug>/` était déclarée **avant** `p/casapy/assets/<path:filename>`. Certaines résolutions d’URL faisaient matcher la page landing au lieu de la vue qui sert les PNG. Aucun module ou dépendance manquant (FileResponse et Path sont dans Django / stdlib). |
| **Solution** | 1) **Mettre la route des assets en premier** dans `apps/landing_pages/urls.py` : `path("p/casapy/assets/<path:filename>", views.serve_casapy_asset, ...)` **avant** `path("p/<slug:slug>/", ...)`. 2) Vérifier que les PNG existent dans `docs/contacts/casapy/` (sinon lancer `python scripts/generate_visuels_casapy.py --output docs/contacts/casapy`). 3) Landing publiée : `python manage.py create_landing_casapy --publish`. 4) Tester un asset : `http://localhost:8010/p/casapy/assets/slide1-impact-perf-business.png` doit renvoyer l’image. |
| **Prévention** | Règle : **routes les plus spécifiques avant les génériques** (ex. `p/casapy/assets/` avant `p/<slug>/`). Voir sprint `segmentations/2026-02-19-sprint-infographies-casapy-ne-saffichent-pas.md` pour la checklist équipe (Ingénieur système, Chef de projet, DevOps). |
| **Lien(s)** | `segmentations/2026-02-19-sprint-infographies-casapy-ne-saffichent-pas.md`, `deploy/PUSH-CASAPY.md` |

### Docker — « Container … is restarting, wait until the container is running » (make migrate)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-09 |
| **Contexte** | Après `make up`, exécution de `make migrate` ; le conteneur **lppp_web** redémarre en boucle. |
| **Erreur** | `Error response from daemon: Container ... is restarting, wait until the container is running` — `make migrate` échoue car il ne peut pas exécuter de commande dans le conteneur. |
| **Cause** | Le conteneur **web** (Django/Gunicorn) plante au démarrage (erreur Python, import, connexion DB, etc.) et Docker le relance en boucle. |
| **Solution** | 1) **Voir la cause** : `docker compose logs web --tail 100` (ou `docker compose logs web -f` pour suivre). Corriger l’erreur affichée (souvent ImportError, OperationalError DB, ou variable d’environnement). 2) **Attendre que Django soit prêt** : utiliser **`make migrate-wait`** au lieu de `make migrate` — la cible attend que `python manage.py check` réussisse puis lance les migrations. 3) Si le conteneur reste en crash loop : corriger le bug (logs), puis `make clean-containers` et `make up` avant de relancer `make migrate-wait`. |
| **Prévention** | Après `make up`, attendre 20–30 s avant la première commande dans le conteneur ; privilégier **`make migrate-wait`** pour les migrations. |
| **Lien(s)** | Makefile (migrate-wait), `pret-a-demarrer.md` |

### PostgreSQL — « password authentication failed for user "…" » (conteneur web en crash loop)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-09 |
| **Contexte** | Stack Docker LPPP (`make up`) ; conteneur **lppp_web** en crash loop ; logs : `OperationalError: password authentication failed for user "Lucas@dmin"` (ou autre user). |
| **Erreur** | `FATAL: password authentication failed for user "Lucas@dmin"` — Django (conteneur web) ne peut pas se connecter à PostgreSQL. |
| **Cause** | **.env** : `DB_USER` / `DB_PASSWORD` doivent être **ceux avec lesquels le volume Postgres a été initialisé** (docker-compose utilise `POSTGRES_USER=${DB_USER:-lpppuser}` au premier démarrage). Si vous voyez **« role "X" does not exist »** : le volume a été créé avec un **autre** user (souvent **lpppuser** par défaut) → mettre dans .env **DB_USER=lpppuser**, **DB_PASSWORD=lppppass123**. Si vous voyez **« password authentication failed »** : le user existe mais le mot de passe est faux. En outre : **DB_HOST=localhost** ou **REDIS_URL=127.0.0.1** empêchent le conteneur web de joindre **db** et **redis** (en Docker : **DB_HOST=db**, **redis://redis:6379**). |
| **Solution** | **Principe : ne pas détruire les données.** 1) Garder les credentials **existants** du volume : si la base a été créée avec `Lucas@dmin` / `Lucas@dm1n`, laisser **`DB_USER=Lucas@dmin`**, **`DB_PASSWORD=Lucas@dm1n`** dans le .env. 2) En Docker : **`DB_HOST=db`**, **`DB_PORT=5432`**, **`REDIS_URL=redis://redis:6379/0`** (et idem pour Celery). 3) Si l’on souhaite passer à un autre user : d’abord **`make backup`**, puis soit créer l’utilisateur côté Postgres (sans recréer le volume), soit — uniquement sur demande explicite de l’utilisateur — réinitialisation (down -v) après sauvegarde. **Ne jamais proposer `docker compose down -v`** sans sauvegarde et accord explicite. |
| **Prévention** | **DB_USER** / **DB_PASSWORD** = ceux avec lesquels le volume Postgres a été initialisé (ne pas les changer sans créer l’user côté Postgres ou sans backup + accord). En Docker : **DB_HOST=db**, Redis/Celery avec host **redis**. Voir `protection-donnees-et-sauvegardes.md`, `2026-02-09-brief-devops-auth-postgres-conteneur-web.md`. |
| **Lien(s)** | `.env.example`, `docker-compose.yml`, `infra-devops.md`, `2026-02-09-brief-devops-auth-postgres-conteneur-web.md` |

### Django — « Your models in app(s): '…' have changes that are not yet reflected in a migration »

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-09 |
| **Contexte** | Après `make migrate` ou `make migrate-wait` : message d’avertissement indiquant qu’un modèle a des changements non reflétés dans une migration. |
| **Erreur** | `Your models in app(s): 'landing_pages' have changes that are not yet reflected in a migration, and so won't be applied. Run 'manage.py makemigrations' to create new migrations.` |
| **Cause** | Dérive entre l’état du modèle (code Python) et l’état enregistré par les migrations (souvent après des migrations RunPython sans changement de schéma, ou après modification du modèle sans `makemigrations`). |
| **Solution** | (1) **Créer les migrations** : `docker compose exec web python manage.py makemigrations landing_pages` (ou l’app concernée). (2) **Appliquer** : `docker compose exec web python manage.py migrate`. Si Django ne propose rien (`No changes detected`) mais l’avertissement reste : créer une migration de synchronisation (ex. `AlterField` sur le champ concerné avec la définition actuelle du modèle) — ex. `0008_sync_model_state.py` pour `landing_pages`. (3) **Mode équipe** : si bloqué, segmenter pour **Dev Django** (migrations, état des modèles) ou **DevOps** (exécution dans le conteneur) ; documenter dans une segmentation et faire exécuter `makemigrations` + `migrate` par l’agent concerné. |
| **Prévention** | Après toute modification de modèle (champs, choices, Meta) : lancer **`makemigrations`** puis **`migrate`** avant commit. Procédure avant relance : `procedure-avant-migrations-relance.md`. |
| **Lien(s)** | `procedure-avant-migrations-relance.md`, `apps/landing_pages/migrations/0008_sync_model_state.py` (exemple), registre § Dev Django / DevOps |

### PostgreSQL « manque » / Connection refused 5432 — tests ou runserver sur l'hôte

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-07 |
| **Contexte** | Exécution de **pytest** ou **runserver** **sur l'hôte** (WSL) alors que la base tourne dans Docker (`lppp_db`). |
| **Erreur** | `OperationalError: connection to server at "127.0.0.1", port 5432 failed: Connection refused` ou « postgres manque ». |
| **Cause** | Le conteneur **lppp_db** expose PostgreSQL en **5432** dans le réseau Docker ; sur l'**hôte** le port mappé est **5433** (`5433:5432`). Avec `DB_HOST=db` / `DB_PORT=5432`, depuis l'hôte Django tente 127.0.0.1:5432 — rien n'écoute sur 5432. |
| **Solution** | **Sur l'hôte** : dans `.env` mettre **`DB_HOST=localhost`** et **`DB_PORT=5433`**. Lancer `docker compose up -d db redis`, attendre, puis `make test` ou `runserver`. **Dans Docker** : garder `DB_HOST=db`, `DB_PORT=5432`. Alternative : **`make test-docker`** (pytest dans le conteneur, pas besoin de changer .env). |
| **Prévention** | Docker interne = db:5432 ; hôte = localhost:5433. Voir `pret-a-demarrer.md` § Option B, `.env.example`. |
| **Lien(s)** | `pret-a-demarrer.md`, `.env.example`, `infra-devops.md` (§ 3.4), `docker-compose.yml` |

### Landing Maisons-Alfort : page de prospection (missions, CDI, CDD), pas « page municipale »

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-06 |
| **Contexte** | Landing `/p/maisons-alfort/` ; contenu et positionnement de la page. |
| **Erreur** | La landing a été traitée comme une **page municipale** (focus sur l’assistant pour les équipes, peu de structure). L’utilisateur se vend aux élus et services : **missions, CDI, CDD**. L’iframe Conciergerie est une **démo** de ce qu’il peut implanter chez eux, pas le produit principal. |
| **Cause** | Confusion entre « page pour la mairie » (contenu institutionnel) et « landing de prospection pour se vendre à la mairie » (même niveau de qualité et structure que P4S, 0flow, etc.). |
| **Solution** | Maisons-Alfort = template **proposition** avec **structure enrichie** (hero, enjeux, solution, services, mission flash, CTA, coordonnées) et **qualité de texte** au niveau des autres landings. Section « Démo : ce que je peux implanter pour vous » avec l’iframe Conciergerie. Migration `0005_maisons_alfort_landing_proposition_enrichie.py` + section démo dans `proposition.html` + passage de `flowise_embed_url` pour slug `maisons-alfort` dans la vue. |
| **Prévention** | Pour toute landing ciblant une collectivité ou un prospect : **toujours** appliquer la **structure enrichie** et le **niveau de qualité P4S** (contenu statique de qualité, ventes / missions / CDI / CDD). Les démos (chatbot, Loom, etc.) sont des **sections** qui illustrent ce qu’on peut déployer, pas le cœur du message. Voir `strategie-qualite-contenu-landings.md`, `attentes-contenu-et-enrichissement-qualite.md`. |
| **Lien(s)** | `strategie-qualite-contenu-landings.md`, `attentes-contenu-et-enrichissement-qualite.md`, `docs/contacts/mairies/maisons-alfort/` |

### VariableDoesNotExist — clé manquante dans `content` (landing pages)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-07 |
| **Contexte** | Landing publique (ex. `/p/maisons-alfort/`), template `proposition.html` ou `proposition_value.html`, `relance-evenement.html`. |
| **Erreur** | `VariableDoesNotExist: Failed lookup for key [hero_subtitle] in {...}` (ou autre clé `content.*`). Erreur pendant le rendu du template (ex. ligne 581 dans proposition.html). |
| **Cause** | Dans les templates Django, un filtre comme `{{ content.hero_sub_headline\|default:content.hero_subtitle }}` **évalue d’abord** `content.hero_subtitle`. Si la clé n’existe pas dans le dict `content`, Django lève `VariableDoesNotExist` avant d’appliquer le `default`. Une clé absente de `content_json` ou non renseignée par la vue produit la même erreur dès qu’elle est utilisée dans un `{% if %}` ou un `default:variable`. |
| **Solution** | (1) **Vue** : `apps/landing_pages/views.py` — `_content_with_defaults()` renseigne toutes les clés optionnelles et **toujours les deux** clés `hero_sub_headline` et `hero_subtitle` avec la **même** valeur normalisée (`hero_sub_headline or hero_subtitle or ""`), pour les templates `proposition`, `proposition_value`, `relance-evenement`. Ainsi même une ancienne version de template (ex. conteneur non reconstruit) qui référencerait `content.hero_subtitle` ne lève pas d’exception. (2) **Templates** : ne pas utiliser `default:content.une_cle` si `une_cle` peut être absente ; utiliser de préférence `content.hero_sub_headline` avec `|default:''`. |
| **Prévention** | **Gestion des erreurs / Dev Django** : (1) Toute nouvelle clé `content.*` utilisée dans un template landing doit être ajoutée aux `defaults` dans `_content_with_defaults()` (vue). (2) Éviter dans les templates les chaînes du type `{{ content.a\|default:content.b }}` lorsque `b` peut être absent ; privilégier une normalisation côté vue (une seule clé affichée) ou des defaults littéraux `{{ content.a\|default:"" }}`. (3) Consulter ce registre et la vue avant d’ajouter des variables `content.*` dans les templates. |
| **Lien(s)** | `apps/landing_pages/views.py` (§ `_content_with_defaults`), `templates/landing_pages/proposition.html`, `proposition_value.html`, `relance-evenement.html`, `segmentations/2026-02-07-sprint-devops-resolution-erreurs-landing.md` (flux anti-régression) |

### YouTube embed — Erreur 153 (vidéo hero ne s’affiche pas)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-07 |
| **Contexte** | Landing avec fond vidéo YouTube (hero, `content.hero_video_url`), iframe dans `.hero-bg-video`. |
| **Erreur** | Message « Erreur 153 » / « Regarder la vidéo sur YouTube » dans le lecteur intégré ; la vidéo ne se charge pas. |
| **Cause** | Erreur 153 = « Video Player Configuration Error » : la **page** est servie avec `Referrer-Policy: same-origin` (défaut Django depuis 3.1), ce qui supprime le Referer pour les requêtes cross-origin ; l’iframe YouTube ne peut pas s’identifier auprès de YouTube. L’attribut `referrerpolicy` sur l’iframe seul ne suffit pas si l’en-tête HTTP de la page est plus restrictif. |
| **Solution** | (1) **Serveur (obligatoire)** : que la **réponse HTTP** de la page envoie **`Referrer-Policy: strict-origin-when-cross-origin`**. Dans LPPP : **`SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"`** dans `lppp/settings.py` (SecurityMiddleware applique l’en-tête). (2) Sur l’iframe : **`referrerpolicy="strict-origin-when-cross-origin"`**. (3) **URL embed** : utiliser **youtube-nocookie.com** (filtre `youtube_embed_background` dans LPPP). (4) Lien de secours « Regarder la vidéo sur YouTube » (filtre `youtube_watch_url`). |
| **Ne pas reproduire** | **L’agent en charge des erreurs** (et tout agent qui ajoute une vidéo YouTube à une landing) doit **prendre en note** : (1) **Jamais** d’iframe YouTube sans `referrerpolicy="strict-origin-when-cross-origin"`. (2) **Toujours** un lien de secours vers YouTube (filtre `youtube_watch_url`). (3) Utiliser la **procédure dédiée** pour intégrer **n’importe quelle** vidéo YouTube de façon fluide : `integration-video-youtube-landings.md` (checklist, filtres, exemple iframe). |
| **Prévention** | Pour tout nouvel iframe YouTube (embed), inclure `referrerpolicy="strict-origin-when-cross-origin"`. Utiliser les filtres `youtube_embed_background` et `youtube_watch_url` (`landing_filters.py`). **Avant d’ajouter une vidéo YouTube** : consulter `integration-video-youtube-landings.md` pour appliquer la même intégration sans reproduire l’erreur 153. |
| **Lien(s)** | `integration-video-youtube-landings.md` (procédure fluide pour toute vidéo YouTube), `templates/landing_pages/proposition.html` (hero YouTube), `apps/landing_pages/templatetags/landing_filters.py` |

### Blocage vidéo YouTube (fond) + chatbot Flowise — résolution via Claude Code (cloud)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02 |
| **Contexte** | Landing `/p/maisons-alfort/` : vidéo YouTube devant servir de **fond** (autoplay, boucle, sans son) ; chatbot Flowise qui ne s’intégrait pas. Plusieurs itérations avec l’agent Cursor avaient conduit à une **miniature + lien** (pour contourner l’erreur 153) et à un chatbot en **iframe seule**, sans résoudre le cadre vide. |
| **Erreur** | Utilisateur bloqué : vidéo pas en fond automatique ; chatbot cadre vide. |
| **Cause** | (1) **Vidéo** : choix précédent de remplacer l’iframe par une miniature pour éviter l’erreur 153, alors que l’utilisateur voulait **autoplay en fond**. (2) **Chatbot** : variables **FLOWISE_URL** et **FLOWISE_CHATFLOW_ID** absentes du `.env` ; le code utilise des valeurs par défaut mais l’ajout explicite dans `.env` + redémarrage du conteneur web était nécessaire pour que l’embed soit bien fourni. |
| **Solution** | Résolution effectuée par **Claude Code (cloud)** : (1) Vidéo : iframe avec **`src="{{ embed_url }}"`** (chargement direct), **referrerpolicy="strict-origin-when-cross-origin"**, **youtube-nocookie.com**, paramètres autoplay=1&mute=1&loop=1 ; suppression du bouton « Lancer la vidéo » et du script au clic ; lien de fallback « Ouvrir sur YouTube » conservé. (2) Chatbot : ajout dans `.env` de **FLOWISE_URL=http://localhost:3010** et **FLOWISE_CHATFLOW_ID=67206a96-470e-4607-ba8b-5955e97aa116** ; redémarrage du conteneur web. (3) Templates concierge et proposition alignés (iframe hero en `src`, overlay/scanlines limités au hero). |
| **Ne pas reproduire** | **À l’avenir** : (1) Si l’utilisateur demande une **vidéo en fond** (autoplay, boucle, sans son), privilégier l’**iframe avec src=** (et referrer policy + youtube-nocookie) plutôt que de basculer sur miniature seule sans proposer l’option autoplay. (2) En cas de **chatbot qui ne s’affiche pas**, vérifier en premier **.env** (FLOWISE_URL, FLOWISE_CHATFLOW_ID) et **docker compose restart web** avant de changer l’intégration (iframe vs web component). (3) Documenter ici qu’un blocage a été levé par un autre outil (Claude Code) pour éviter que les agents Cursor ne répètent les mêmes choix qui avaient conduit à l’impasse. |
| **Prévention** | Consulter cette entrée et `flowise-chatbot-ecran-vide-diagnostic.md` avant de modifier le hero vidéo ou l’embed chatbot. Exiger **FLOWISE_URL** et **FLOWISE_CHATFLOW_ID** dans la checklist déploiement / démo (voir `.env.example`). |
| **Lien(s)** | `flowise-chatbot-ecran-vide-diagnostic.md`, `integration-video-youtube-landings.md`, `.env.example`, `templates/landing_pages/proposition.html`, `concierge_maisons_alfort.html` |

### Vercel — 404 NOT_FOUND ou PR_END_OF_FILE_ERROR (repo LPPP complet)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-07 |
| **Contexte** | Projet Vercel lié au repo **LPPP_Missions_mairie_m-Alfort** (ou tout repo contenant le **projet Django LPPP entier**). |
| **Erreur** | **404: NOT_FOUND** sur l’URL Vercel ; ou **Échec de la connexion sécurisée / PR_END_OF_FILE_ERROR** (connexion coupée). |
| **Cause** | Le dépôt contient une **app Django** (apps/, manage.py, etc.), pas un site statique ni une app Next.js à la racine. Vercel ne sait pas quoi servir → pas de sortie à la racine → 404. |
| **Solution** | Dans **Vercel** → projet → **Settings** → **General** : définir **Root Directory** = **`deploy/concierge-demo-maisons-alfort`** (démo statique Maisons-Alfort). Laisser **Build Command** et **Output Directory** vides. Puis **Redeploy**. Pour d’autres missions : utiliser le dossier static/standalone correspondant ou suivre `strategie-deploiement-git-vercel.md` (1 repo = 1 contenu déployable). |
| **Prévention** | Pour un repo « missions » contenant tout LPPP : documenter le Root Directory Vercel (ex. `deploy/VERCEL-MISSIONS-MAISONS-ALFORT.md`). Ou, pour une URL dédiée propre : repo avec **uniquement** le contenu déployable (clone → copier `deploy/standalone-*` ou `deploy/static-*` → push). |
| **Lien(s)** | `deploy/VERCEL-MISSIONS-MAISONS-ALFORT.md`, `strategie-deploiement-git-vercel.md` |

### Exemple (template) — ModuleNotFoundError: No module named 'environ'

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | WSL, lancement `make runserver` ou `python manage.py runserver` |
| **Erreur** | `ModuleNotFoundError: No module named 'environ'` |
| **Cause** | Environnement virtuel absent ou dépendances non installées (django-environ dans requirements.txt) |
| **Solution** | `make venv-install` puis `make runserver` |
| **Prévention** | Utiliser `make venv-install` après clône ou changement de branche ; doc `environnement-wsl-linux.md` § 6, Option B |
| **Lien(s)** | `environnement-wsl-linux.md`, `strategie-operationnelle-make.md` § 3.7, `2025-01-30-correction-relance-wsl.md` |

---

### Docker — « The container name "/lppp_xxx" is already in use »

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | WSL ou Linux, `make up` ou `make start` dans le projet LPPP |
| **Erreur** | `Error response from daemon: Conflict. The container name "/lppp_db" is already in use by container "..."` (ou lppp_redis, lppp_web, etc.) |
| **Cause** | Conteneurs LPPP orphelins (créés lors d’une exécution précédente, éventuellement depuis un autre répertoire ou projet Compose). `make down` ne les supprime pas car ils ne sont plus associés au projet Compose actuel. |
| **Solution** | Supprimer **uniquement les conteneurs LPPP** par leur nom, puis relancer : `docker rm -f lppp_db lppp_redis lppp_web lppp_celery lppp_celery_beat lppp_n8n lppp_flowise 2>/dev/null; make up`. **Ne jamais** supprimer ou modifier les conteneurs SquidResearch (django, worker, react, n8n, flowise, postgres, redis, etc.) : SquidResearch a la priorité (prod, écosystème). Décision : `decisions.md` « Priorité SquidResearch ». |
| **Prévention** | Lancer `make down` depuis la racine LPPP avant de quitter ou en cas de changement de branche. En cas de conflit, ne toucher qu’aux conteneurs dont le nom commence par `lppp_`. |
| **Lien(s)** | `infra-devops.md` § 1 (Priorité SquidResearch), `log-commun-lppp-squidresearch.md` |

---

### Flowise — incompatibilités de types entre nœuds / difficulté à raccorder

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Flowise, canvas Chatflow ou flow d'ingestion ; tentative de relier des nœuds entre eux |
| **Erreur** | Connexion refusée entre nœuds, message d'incompatibilité de type, ou flow qui ne s'exécute pas après câblage |
| **Cause** | Flowise impose des types de flux (Document, ChatMessage, etc.) : une sortie ne peut aller que vers une entrée du même type. Câbler « Document » vers « ChatMessage » (ou l'inverse) provoque des erreurs. |
| **Solution** | Pour le RAG Concierge Maisons-Alfort : **ne pas câbler** les nœuds. Utiliser la section **Document Stores** pour l'ingestion (Loader → Splitter → Embedding → Vector Store, sans fils). Sur le **Chatflow**, mettre un seul nœud **Agent** et configurer **Knowledge** via la liste déroulante (sélection du Document Store), pas par un câble. |
| **Prévention** | Suivre la recette `docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md` § « Pourquoi les nœuds ne se raccordent pas ». Règle : Document → Document uniquement ; ChatMessage/string → même type. Vérifier les libellés des prises avant de connecter. |
| **Lien(s)** | `docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md`, `flowise-concierge-ia-maisons-alfort-guide.md` |

---

### LPPP — service web arrêté + « failed to resolve host db » + container name already in use

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-17 |
| **Contexte** | WSL, stack LPPP partiellement arrêtée. `docker compose exec web` → service web non démarré. `python3 manage.py` depuis l'hôte → failed to resolve host 'db'. `docker compose up -d db` → Conflict, container name already in use. |
| **Erreur** | Combinaison : web arrêté ; hôte ne résout pas « db » ; compose refuse de créer car conteneurs existent. |
| **Cause** | Conteneurs LPPP existent mais sont arrêtés ; compose tente de recréer (conflit) ; exécution depuis l'hôte utilise DB_HOST=db (résolu uniquement dans le réseau Docker). |
| **Solution** | **Option A (non destructive)** : `docker start lppp_db lppp_redis && sleep 5 && docker start lppp_web && sleep 8 && docker exec lppp_web python manage.py create_landing_casapy --publish`. Touche uniquement lppp_* (pas SquidResearch). **Option B** : `make clean-containers` puis `make start` (conteneurs supprimés, volumes préservés). |
| **Prévention** | Toujours exécuter les commandes Django dans le conteneur : `docker exec lppp_web python manage.py ...` ou `docker compose exec web python manage.py ...`. |
| **Lien(s)** | `log-commun-lppp-squidresearch.md`, `Makefile`, `pilotage-agents.mdc` |

---

### make migrate / makemigrations — « service "web" is not running »

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | WSL (ou autre), après commit/push ; `make makemigrations` ou `make migrate` |
| **Erreur** | `service "web" is not running` — Makefile:309 (makemigrations) ou Makefile:299 (migrate) Error 1 |
| **Cause** | Les commandes exécutent `docker compose exec web python manage.py ...` ; le conteneur `web` n’existe pas tant que le stack n’est pas démarré. |
| **Solution** | Démarrer le stack : **`make start`** (recommandé : démarre db, redis, web, etc. puis applique migrate automatiquement) ou **`make up`** puis **`make migrate`**. |
| **Prévention** | Avant toute commande `make migrate` / `make makemigrations`, s’assurer que les services tournent (`make ps`). Procédure : `procedure-avant-migrations-relance.md` — l’ordre est : 1) commit+push, 2) **démarrer le stack** si besoin, 3) migrations, 4) relance si nécessaire. |
| **Lien(s)** | `procedure-avant-migrations-relance.md`, `strategie-operationnelle-make.md` |

---

### Docker — « The container name "/lppp_redis" is already in use »

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | `make start` ou `docker compose up -d db redis` ; WSL ou autre |
| **Erreur** | `Error response from daemon: Conflict. The container name "/lppp_redis" is already in use by container "…". You have to remove (or rename) that container to be able to reuse that name.` |
| **Cause** | Un conteneur nommé `lppp_redis` (ou autre `lppp_*`) existe déjà — créé par un ancien `docker compose` ou par un autre répertoire/projet utilisant les mêmes noms. |
| **Solution** | Supprimer les conteneurs LPPP par nom : **`make clean-containers`** puis **`make start`**. (Ne supprime pas les **volumes** : les données db/redis/n8n/flowise restent ; seuls les conteneurs sont retirés.) |
| **Prévention** | Après un `make down` dans un autre répertoire ou un changement de branche, en cas de conflit utiliser `make clean-containers` avant `make start`. |
| **Lien(s)** | `Makefile` (cible `clean-containers`), `strategie-operationnelle-make.md` |

---

### Admin Django — impossible de se connecter / « il n’y a rien »

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-04 |
| **Contexte** | Ouverture de `http://localhost:8010/admin/` (Docker LPPP) : page blanche, timeout, connexion refusée ou aucun formulaire de login. |
| **Erreur** | Rien ne s’affiche, ou « This site can’t be reached », ou page vide. |
| **Cause** | (1) **Stack non démarré** : conflit Docker (`lppp_db` / `lppp_redis` already in use) → `make up` échoue, le conteneur `web` ne tourne pas. (2) **Aucun superutilisateur** : aucun compte admin n’a été créé (ou mot de passe oublié). |
| **Solution** | **(1)** Supprimer les conteneurs LPPP puis relancer : **`make clean-containers`** puis **`make start`**. Attendre la fin (migrate, static). **(2)** Créer un compte admin : **`make createsuperuser`** (dans le terminal, saisir username, email, mot de passe). Puis ouvrir `http://localhost:8010/admin/` et se connecter. |
| **Prévention** | Après un conflit Docker, toujours utiliser `make clean-containers` avant `make start`. À la première installation ou sur une base vide, exécuter `make createsuperuser` avant d’aller sur l’admin. |
| **Lien(s)** | `Makefile` (clean-containers, createsuperuser), `pret-a-demarrer.md`, entrée « Docker — container name already in use » ci-dessus. |

---

### make start — « Django pas encore prêt » en boucle puis interruption

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | `make start` après `make clean-containers` ; conteneurs démarrés mais la boucle d’attente de Django ne se termine pas. |
| **Erreur** | Message répété « Django pas encore prêt, attente 5s... » pendant plusieurs minutes ; pas de message d’erreur visible. |
| **Cause** | `python manage.py check` échoue ou bloque dans le conteneur `web` (sortie masquée par le Makefile). Causes fréquentes : migrations non appliquées, DB injoignable, erreur d’import ou de config Django. |
| **Solution** | (1) **Diagnostiquer** : `docker compose exec web python manage.py check` (voir l’erreur réelle) et `docker compose logs web --tail 80` (logs Gunicorn). (2) **Makefile mis à jour** : `make start` applique maintenant les migrations tôt (après 15 s) puis refait le check ; après 12 échecs (1 min) il affiche la sortie de `check` puis quitte. Relancer `make start` après correction. (3) Si la DB est vide ou corrompue : `make migrate` à la main après avoir vérifié que `web` et `db` tournent. |
| **Prévention** | Utiliser `make start` à jour ; en cas de boucle, ne pas attendre indéfiniment : Ctrl+C puis exécuter les commandes de diagnostic ci‑dessus. |
| **Lien(s)** | `Makefile` (cible `start`), `procedure-avant-migrations-relance.md` |

---

### ModuleNotFoundError: No module named 'markdown' (conteneur web)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | `make start` ou `docker compose logs web` ; conteneur `web` en boucle de redémarrage. |
| **Erreur** | `ModuleNotFoundError: No module named 'markdown'` dans `apps/landing_pages/views.py` (ou autre module). |
| **Cause** | La dépendance est dans `requirements.txt` mais l’**image Docker** du service `web` a été construite avant son ajout (ou jamais reconstruite). |
| **Solution** | **Reconstruire l’image** : `make build` puis `make start`. Ou `docker compose build web` puis `docker compose up -d web`. Le conteneur récupère alors les paquets à jour. |
| **Prévention** | Après ajout ou modification de `requirements.txt`, exécuter `make build` (ou `docker compose build`) avant de relancer les services. |
| **Lien(s)** | `requirements.txt`, `Makefile` (build), `strategie-operationnelle-make.md` |

---

### Landing /p/maisons-alfort/ — Écran blanc

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Page **/p/maisons-alfort/** (ou /maisons-alfort/ après redirection) : écran blanc, rien ne s’affiche ou le contenu n’est pas visible. |
| **Erreur** | Écran blanc (page entière ou zone chat uniquement). |
| **Causes possibles** | (1) **Dev Django** : exception dans la vue, template manquant ou mal nommé, contexte incomplet ; (2) **DevOps** : Django non servi sur l’URL, Flowise non exposé sur 3000, `.env` sans FLOWISE_CHATFLOW_ID / FLOWISE_URL ; (3) **Architecte** : route manquante ou conflit, LandingPage `maisons-alfort` absente en base (migration 0004 non appliquée) ; (4) **Designer** : CSS qui masque le contenu (fond blanc + texte blanc, overflow hidden) ; (5) **Automatizer** : Flowise ne répond pas sur /embed/{id}, chatflow absent ou ID incorrect. |
| **Solution** | **Sprint multi-agents** : suivre `segmentations/2026-01-30-sprint-ecran-blanc-landing-chatbot.md`. **Architecte** : vérifier chaîne route → vue → template, existence de la LandingPage en base. **DevOps** : vérifier que Django répond (curl /p/maisons-alfort/ → 200), Flowise sur 3000, .env FLOWISE_CHATFLOW_ID et FLOWISE_URL. **Dev Django** : s’assurer que flowise_embed_url est passé (ou "" pour placeholder), template toujours visible (hero + intro + zone chat). **Designer** : vérifier styles (contraste, pas de contenu masqué). **Automatizer** : vérifier chatflow déployé et URL /embed/{id} joignable. |
| **Prévention** | Toujours afficher au minimum hero + intro + message « Chat en cours de configuration » si pas d’URL embed ; ne jamais renvoyer une page vide. Voir template `concierge_maisons_alfort.html` et vue `landing_public`. |
| **Lien(s)** | `segmentations/2026-01-30-sprint-ecran-blanc-landing-chatbot.md`, `flowise-concierge-ia-maisons-alfort-guide.md`, `conciergerie-maisons-alfort-architecture-et-onboarding.md` |

---

### Landing /maisons-alfort/ — « Impossible de trouver l'adresse IP du serveur de flowise »

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Page **http://127.0.0.1:8082/maisons-alfort/** (ou /essais/concierge/) : iframe du chatbot Flowise affiche une erreur « Impossible de trouver l'adresse IP du serveur de flowise ». |
| **Erreur** | « Impossible de trouver l'adresse IP du serveur de flowise » (navigateur, dans la zone de l'iframe). |
| **Cause** | L'URL d'embed envoyée au navigateur pointait vers **http://flowise:3000** (nom d'hôte Docker). Le navigateur tourne sur l'hôte et ne peut pas résoudre « flowise » (résolution DNS du réseau Docker). |
| **Solution** | **Correctif code** : `get_flowise_chat_embed_url()` (apps/scraping/flowise_client.py) utilise maintenant une URL joignable par le navigateur : si `DB_HOST` est `localhost` ou `127.0.0.1` (Django sur l'hôte), l'URL par défaut est **http://localhost:3010** (port LPPP). Sinon définir **`FLOWISE_URL=http://localhost:3010`** dans `.env` et redémarrer le runserver. Vérifier que Flowise écoute sur le port 3000 (`docker compose up -d flowise` ou instance locale). |
| **Prévention** | En dev avec runserver sur l'hôte : définir `FLOWISE_URL=http://localhost:3010` si besoin. En Docker full stack LPPP : l'iframe pointe vers http://localhost:3010 (port dédié). |
| **Lien(s)** | `flowise-concierge-ia-maisons-alfort-guide.md`, `segmentations/2026-01-30-sprint-chatbot-landing-flowise.md` |

---

### Landing /p/maisons-alfort/ — iframe du chatbot vide (cadre blanc)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-04 |
| **Contexte** | La **landing** s’affiche correctement (titre, intro) mais le **cadre (iframe) du chatbot** reste blanc, sans interface de chat. |
| **Erreur** | Zone dédiée au chat visible mais vide (rectangle blanc dans l’iframe). |
| **Causes possibles** | (1) **Flowise n’est pas démarré** sur le port **3010** (LPPP). (2) **Mauvais `FLOWISE_CHATFLOW_ID`** : l’ID dans `.env` ne correspond pas au chatflow Conciergerie dans Flowise (récupérer l’ID dans Flowise → chatflow → onglet **Embed**). (3) **URL d’embed non joignable par le navigateur** : si Django tourne sur l’hôte (runserver 127.0.0.1:8082) sans `FLOWISE_URL`, le code utilise `http://localhost:3010` si `DB_HOST=localhost` (port LPPP) ; si `DB_HOST=db`, l’URL devient `http://flowise:3000` et le navigateur ne peut pas la résoudre → iframe vide. (4) Flowise répond mais la page **/embed/{id}** renvoie une page vide (chatflow inexistant ou erreur côté Flowise). |
| **Solution** | **Étape 1** : Sous l’iframe, cliquer sur **« Ouvrir le chat dans un nouvel onglet »** (lien ajouté sur la page). Si le chat **s’affiche** dans l’onglet → problème d’affichage en iframe (CORS / X-Frame-Options à vérifier côté Flowise). Si le nouvel onglet est **vide ou erreur** → **Étape 2** : Vérifier que Flowise tourne (`docker compose ps` → `lppp_flowise` ; `curl -s -o /dev/null -w "%{http_code}" http://localhost:3010` → 200). **Étape 3** : Dans Flowise (http://localhost:3010), ouvrir le chatflow Conciergerie Maisons-Alfort → onglet **Embed** → copier l’**ID** et le mettre dans `.env` : `FLOWISE_CHATFLOW_ID=<id>`. **Étape 4** : Si Django est en runserver sur l’hôte (127.0.0.1:8082), forcer l’URL pour le navigateur : dans `.env` définir `FLOWISE_URL=http://localhost:3010` (LPPP), redémarrer le runserver, recharger la page. |
| **Prévention** | En dev local (runserver sur l’hôte) : avoir `FLOWISE_URL=http://localhost:3010` et `FLOWISE_CHATFLOW_ID` correct dans `.env`, et Flowise démarré sur le port 3010 (LPPP). Voir `flowise-concierge-ia-maisons-alfort-guide.md`, `conciergerie-maisons-alfort-architecture-et-onboarding.md`. |
| **Lien(s)** | **`flowise-chatbot-ecran-vide-diagnostic.md`** (checklist complète écran vide / flux), `flowise-concierge-ia-maisons-alfort-guide.md`, `conciergerie-maisons-alfort-architecture-et-onboarding.md`, entrée « Impossible de trouver l'adresse IP du serveur de flowise » ci-dessus |

---

### Flowise — « No Chatflows Yet » / plus de workflows après reconnexion ou changement de credentials

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Après reconnexion (Flowise demande identifiants) ou après changement de `FLOWISE_USERNAME` / `FLOWISE_PASSWORD` dans `.env`, l’interface Flowise sur localhost:3000 affiche **« No Chatflows Yet »** — plus aucune trace des chatflows créés. Flowise ne permet qu'un seul utilisateur (même email avant/après). |
| **Erreur** | « No Chatflows Yet » ; liste des Chatflows vide. |
| **Cause** | (1) **Deux Flowise** : le port 3000 peut être utilisé par **LPPP** (`lppp_flowise`, volume `flowise_data`) ou par **SquidResearch** (autre conteneur, autre volume). Selon quel stack est démarré, localhost:3000 affiche l’un ou l’autre — les chatflows LPPP ne sont que dans le Flowise LPPP. (2) **Changement de credentials** : en activant ou modifiant `FLOWISE_USERNAME`/`FLOWISE_PASSWORD`, Flowise peut associer les données à un « utilisateur » ; si l’app considère que c’est un nouvel utilisateur, l’espace peut apparaître vide alors que les données sont toujours dans le volume. |
| **Solution** | **Étape 1 — Quel Flowise tourne ?** `docker ps --format "table {{.Names}}\t{{.Ports}}"` et repérer qui expose `3000/tcp`. Si c’est **lppp_flowise** → les données LPPP sont dans le volume `flowise_data` (non supprimé par `docker rm` ni `make down`). Si c’est un autre conteneur (ex. SquidResearch) → tu regardes l’autre instance ; pour retrouver les chatflows LPPP, arrêter l’autre stack et lancer LPPP : `docker compose up -d flowise` depuis la racine LPPP. **Étape 2 — Recréer l’ancien identifiant** : remettre temporairement dans `.env` les **anciennes** valeurs `FLOWISE_USERNAME` et `FLOWISE_PASSWORD` (celles utilisées quand tu avais créé les chatflows), redémarrer Flowise (`docker compose restart flowise`), puis recharger localhost:3010 — les chatflows peuvent réapparaître. **Étape 2 — Recréer le chatflow** : Flowise est single-user ; si les chatflows ont disparu, les recréer avec **`docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md`**, puis mettre le nouvel ID (onglet Embed) dans `.env` : **`FLOWISE_CHATFLOW_ID=<nouvel-id>`**. |
| **Prévention** | Ne pas modifier `FLOWISE_USERNAME`/`FLOWISE_PASSWORD` sans nécessité (risque de réinitialisation). Un seul utilisateur Flowise. Vérifier quel conteneur utilise le port 3000 avant de conclure à une perte de données. Rappel : **`make go`** seul supprime les volumes ; `make down` et `docker rm -f lppp_flowise` ne touchent pas à `flowise_data`. |
| **Lien(s)** | `flowise-concierge-ia-maisons-alfort-guide.md` § Démarrer sans perdre de données, **`sauvegarde-workflows-flowise-n8n.md`** (exporter chatflows dans `docs/flowise-workflows/backups/` pour réinjection), `docker-compose.yml` |

---

### Flowise — 401 Invalid model key or Incorrect local model configuration

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Flowise, chargement d'une page ou exécution d'un chatflow / ingestion |
| **Erreur** | Status 500 — « 401 Invalid model key or Incorrect local model configuration » |
| **Cause** | Problème de configuration du **LLM** ou de l'**embedding** : clé API OpenAI (ou autre) invalide, expirée ou mal renseignée ; ou modèle local (Ollama, etc.) mal configuré (URL, nom du modèle). |
| **Solution** | Vérifier dans Flowise : (1) Credentials / clé API du nœud OpenAI (Chat ou Embeddings) — clé valide et avec les bons droits ; (2) Nom du modèle exact (ex. `gpt-4o-mini`, `text-embedding-3-small`) ; (3) Si modèle local : URL de base (ex. `http://host.docker.internal:11434`) et nom du modèle. Corriger la config puis recharger la page. |
| **Prévention** | Documenter les modèles utilisés dans `data/flowise/comptes-et-llm.md` ; ne pas committer les clés (`.env` / UI Flowise uniquement). |
| **Lien(s)** | `data/flowise/comptes-et-llm.md`, `flowise-faiss-base-path-infra.md` § 5 |

---

### Flowise — faiss.index « No such file or directory » (RAG / Base Path)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Chatflow Conciergerie (ou autre RAG FAISS) : le chat s'affiche mais à l'envoi d'un message, erreur « could not open C:\flowise-data\faiss\.../faiss.index for reading: No such file or directory ». |
| **Erreur** | Error in faiss::FileIOReader::FileIOReader(...): could not open .../faiss.index for reading: No such file or directory |
| **Cause** | Le nœud Faiss utilise un Base Path inadapté : Flowise en Docker (LPPP) avec chemin Windows (C:\...) laissé après réimport ; ou index jamais créé à cet emplacement. |
| **Solution** | **Docker LPPP (port 3010)** : chatflow → nœud Faiss → Base Path to load = **/data/flowise/faiss/maisons-alfort**. Sauvegarder. Si dossier vide côté host (data/flowise/faiss/maisons-alfort/), lancer un upsert (Document Store → Load). **Windows hors Docker** : C:\flowise-data\faiss\conciergerie-maisons-alfort. |
| **Prévention** | À chaque réimport ou changement de stack, vérifier l'adresse tampon (Base Path). Voir flowise-faiss-base-path-infra.md § 5 et automatizer.mdc § Contrôle adresse tampon. |
| **Lien(s)** | flowise-faiss-base-path-infra.md § 5, conciergerie-maisons-alfort-architecture-et-onboarding.md, automatizer.mdc |

---

### Vercel — Root Directory deploy/static-infopro-vercel does not exist

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-20 |
| **Contexte** | Projet lppp-infopro connecté au repo landingPageCreatorForProspection, Root Directory = deploy/static-infopro-vercel. Build échoue. |
| **Erreur** | Build Failed — The specified Root Directory does not exist. |
| **Cause** | Le dossier deploy/static-infopro-vercel n'a pas été commité et poussé. |
| **Solution** | git add deploy/static-infopro-vercel/ puis commit + push. Config Vercel : repo = landingPageCreatorForProspection, Root Directory = deploy/static-infopro-vercel. Voir deploy/PUSH-INFOPRO.md |
| **Lien(s)** | deploy/PUSH-INFOPRO.md |

---

### Vercel 404 / DEPLOYMENT_NOT_FOUND — page ne s’affiche pas

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Déploiement Vercel après push sur GitHub ; ouverture de l’URL du projet (ex. `https://<projet>.vercel.app/` ou `/p4s-archi`) |
| **Erreur** | 404, « 404: NOT_FOUND », « DEPLOYMENT_NOT_FOUND » ou page blanche |
| **Cause** | **Root Directory** Vercel incorrect : Vercel build depuis la racine du dépôt au lieu du dossier qui contient l’app Next.js (ex. `frontend/` en monorepo, ou `./` pour un repo standalone où l’app est à la racine). |
| **Solution** | 1) Vercel Dashboard → projet → **Settings** → **General** → **Root Directory** : **Edit** → saisir `frontend` (monorepo) ou `./` / laisser vide (repo standalone à la racine) → **Save**. 2) **Redeploy** : Deployments → **…** sur le dernier déploiement → **Redeploy** (ou pousser un commit). 3) Attendre build **Ready**, réessayer l’URL. |
| **Prévention** | À la création du projet Vercel, configurer tout de suite le **Root Directory** selon le type de repo (standalone = `./`, monorepo = `frontend`). Voir `strategie-deploiement-git-vercel.md` et `deploiement-vercel-frontend.md`. |
| **Lien(s)** | `deploiement-vercel-frontend.md` § 6, `strategie-deploiement-git-vercel.md` (Pièges à éviter) |

---

### Vercel — 404 NOT_FOUND sur /p/orsys/rapport/ (landing statique ORSYS)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-09 |
| **Contexte** | Landing ORSYS déployée en statique sur Vercel (repo LPPP_orsys) ; clic sur « Consulter le rapport » ou « Voir l’analyse SEO complète » → URL `/p/orsys/rapport/#analyse-seo-complete`. |
| **Erreur** | **404: NOT_FOUND** — la page rapport n’existe pas sur le déploiement statique. |
| **Cause** | L’export statique (`export_landing_static`) n’a pas été lancé avec `--rapport-md`, donc `rapport.html` n’a pas été généré. Le JSON a `rapport_url: "/p/orsys/rapport/"` (URL Django), mais Vercel sert du HTML statique sans Django — aucun fichier ne correspond à ce chemin. |
| **Solution** | 1) Réexporter avec `--rapport-md` : `python manage.py export_landing_static orsys --json docs/contacts/orsys/landing-proposition-aboubakar.json --output deploy/static-orsys-vercel/index.html --rapport-md docs/contacts/orsys/rapport-complet-orsys.md`. 2) Vérifier que `rapport.html` existe dans le dossier. 3) `vercel.json` doit contenir des rewrites : `{ "source": "/p/orsys/rapport/", "destination": "/rapport.html" }`. 4) Copier `rapport.html` dans le repo LPPP_orsys, pousser, redeploy Vercel. |
| **Prévention** | Toujours inclure `--rapport-md` dans l’export pour les landings qui proposent un lien « Consulter le rapport ». Voir `deploy/PUSH-ORSYS.md`, `deploy/static-orsys-vercel/vercel.json`. |
| **Lien(s)** | `deploy/PUSH-ORSYS.md`, `deploy/static-orsys-vercel/vercel.json`, `strategie-deploiement-git-vercel.md` |

---

### Vercel — No Output Directory named "public" after Build

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Déploiement Vercel d’une app Next.js (ex. standalone P4S, frontend) ; build réussit (Route (app), First Load JS) puis échec au final. |
| **Erreur** | `Error: No Output Directory named "public" found after the Build completed. Configure the Output Directory in your Project Settings. Alternatively, configure vercel.json#outputDirectory.` ([Learn More](https://vercel.link/missing-public-directory)) |
| **Cause** | Vercel cherche un répertoire de sortie nommé **public**, alors que Next.js produit **`.next`** (et non `public` — `public` est le dossier d’entrée des assets statiques). Souvent dû à un réglage **Output Directory: public** dans les paramètres du projet Vercel ou à un framework mal détecté. |
| **Solution** | 1) **Dans le repo** : dans le `vercel.json` à la racine de l’app Next.js déployée (ex. `deploy/standalone-p4s/vercel.json` pour P4S), ajouter `"outputDirectory": ".next"` et conserver `"framework": "nextjs"`. 2) **Dans Vercel** : Project → **Settings** → **General** → **Build & Development Settings** → **Output Directory** : laisser **vide** (ou `.next`) et **Framework Preset** = **Next.js** → **Save**. 3) **Redeploy** (push ou Redeploy depuis les Deployments). |
| **Prévention** | Pour tout nouveau projet Vercel lié à une app Next.js : ne pas définir Output Directory sur `public` ; laisser le framework Next.js gérer la sortie, ou fixer `outputDirectory` dans `vercel.json` à `.next`. |
| **Lien(s)** | `deploy/standalone-p4s/vercel.json`, `strategie-deploiement-git-vercel.md`, [Vercel missing public directory](https://vercel.link/missing-public-directory) |

---

### localhost:8000 inaccessible — ERR_CONNECTION_RESET / connexion réinitialisée

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 (enrichi 2025-02-04) |
| **Contexte** | Windows (ou WSL), accès à http://localhost:8010/admin/ (ou /, /essais/) après avoir lancé Docker ou runserver. Navigateur : « Ce site est inaccessible », « La connexion a été réinitialisée », **ERR_CONNECTION_RESET**. |
| **Erreur** | « Ce site est inaccessible », « La connexion a été réinitialisée », **ERR_CONNECTION_RESET** |
| **Cause** | (1) Conteneur `web` non démarré ou en crash (conflit Docker, Django qui plante au démarrage). (2) Sous Windows, le port forward Docker (8000) peut provoquer une connexion réinitialisée. (3) Résolution `localhost` (IPv6 vs IPv4) ou pare-feu. |
| **Solution** | **Diagnostic** : `docker ps` → vérifier que `lppp_web` est « Up ». Si absent ou « Restarting » : `docker compose logs web --tail 50` (erreur Django/Gunicorn ?). Corriger les conflits : `make clean-containers` puis `make start`. **Essai rapide** : en Docker LPPP utiliser **http://127.0.0.1:8010** (Django LPPP = lppp_web). En Option B runserver : 127.0.0.1:8000 ou 8080. **Si toujours ERR_CONNECTION_RESET** : **Option B (runserver local)** : 1) `docker compose up -d db redis` (et `docker compose stop web` pour libérer le port). 2) Dans `.env` : `DB_HOST=localhost`, `REDIS_URL=redis://127.0.0.1:6379/0`, `CELERY_BROKER_URL=redis://127.0.0.1:6379/1`. 3) Venv : `pip install -r requirements.txt`, `python3 manage.py migrate --noinput`, `python3 manage.py runserver 127.0.0.1:8080` (WSL : **python3**). 4) Ouvrir **http://127.0.0.1:8080/admin/** (ou /essais/). |
| **Prévention** | Sous Windows : privilégier Option B pour le dev (runserver sur 8080). Sous WSL : Docker LPPP = **lppp_web sur 8010** (jamais 8000, réservé SquidResearch) ; en cas de reset, tester 127.0.0.1:8010 puis Option B. |
| **Lien(s)** | `pret-a-demarrer.md` § 5.2, `demarrage-projet-equipe-tech.md`, entrée « Admin Django — impossible de se connecter » |

---

### Django inaccessible — problème réseau (sprint Architecte / DevOps / Pentester)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Impossible d’accéder à l’admin Django ni à Django en général ; problème réseau, aucune différence entre admin et reste du site. SquidResearch est prioritaire : on ne touche pas à sa stack. |
| **Erreur** | Site inaccessible (timeout, connexion refusée, reset), admin et pages Django inaccessibles. |
| **Cause** | Plusieurs causes possibles : (1) Conflit de ports si SquidResearch occupe 8000 (ou 3000, 5432) ; (2) Conteneur `lppp_web` non démarré ou en crash ; (3) Sous Windows : port forward Docker 8000 (ERR_CONNECTION_RESET) ; (4) localhost vs 127.0.0.1 (IPv6/IPv4). |
| **Solution** | **Sprint multi-agents** : suivre `segmentations/2026-01-30-sprint-resolution-reseau-django.md`. **Architecte réseau** : consulter le log commun SquidResearch (`log-commun-lppp-squidresearch.md`), identifier conflits de ports, recommander port alternatif LPPP (ex. 8001) si 8000 est pris. **DevOps** : `docker ps` → état `lppp_web` ; `make clean-containers` (conteneurs LPPP uniquement) puis `make start` ; tester http://127.0.0.1:8010 (Django LPPP) ; sinon Option B runserver (voir entrée « localhost:8000 inaccessible »). **Pentester** : vérifier ALLOWED_HOSTS et politique sécurité après toute modification. |
| **Prévention** | Consulter le log commun avant de lancer les deux stacks ; documenter le port Django LPPP si différent de 8000 ; sous Windows privilégier Option B (runserver 8080) si Docker 8000 pose problème. |
| **Lien(s)** | `segmentations/2026-01-30-sprint-resolution-reseau-django.md`, `log-commun-lppp-squidresearch.md`, `infra-devops.md` § 1 et § 3.4, entrée « localhost:8000 inaccessible » ci-dessus |

---

### « LPPP n'a pas son propre Django » — vérifier stack autonome (lppp_web sur 8010)

| Champ | Contenu |
|-------|---------|
| **Contexte** | LPPP doit utiliser **uniquement** sa propre stack : **lppp_web** (Django) sur port **8010**, jamais le port 8000 (SquidResearch). Si la doc ou la config laisse penser le contraire, ou si l'accès se fait encore sur 8000, corriger. |
| **Checklist** | (1) **docker-compose.yml** : service `web` doit avoir `ports: - "8010:8000"` (hôte:conteneur). (2) **README.md**, **pret-a-demarrer.md** : URLs Django = localhost:8010 (Option A Docker). (3) **Makefile** : `services-urls` affiche 8010. (4) Aucune URL dans .env ou le code LPPP ne pointe vers 8000, 5679, 3001 (SquidResearch). (5) Après modification du port : `docker compose up -d --force-recreate web` puis tester http://localhost:8010/. |
| **Prévention** | Toute nouvelle doc ou procédure qui mentionne « Django » pour LPPP en Docker doit indiquer le port **8010** et le conteneur **lppp_web**. Réf. `log-commun-lppp-squidresearch.md` § 5.3, `avis-et-solutions-routage-lppp-reference.md`. |

---

### Modifications Casapy pas visibles — deux pages parallèles (Django vs export statique)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Sur `http://localhost:8010/p/casapy/`, les modifications du template (ex. « Deck 7 slides + one-pager + wave », marqueurs | LPPP) ne s'affichent jamais, même après rafraîchissement et vidage du cache. |
| **Erreur** | Page affichée = titre « Lucas Tymen — Projet Casapy (audit SEO, e-commerce) » sans « \| LPPP », pas de bandeau vert ; code source sans `LPPP proposition.html`. |
| **Cause** | **Deux pages parallèles** : (1) **Page A** = Django dynamique (template + JSON à la volée) sur localhost:8010/p/casapy/ ; (2) **Page B** = export statique figé `deploy/LPPP-Casapy/index.html`. Sur localhost:8010/p/casapy/ seul Django répond. **Cause confirmée** : une requête directe au serveur (`curl -s http://127.0.0.1:8010/p/casapy/`) renvoie bien le titre avec « \| LPPP » et le bandeau « Page servie par Django LPPP ». Si l'utilisateur ne les voit pas, c'est le **cache navigateur** ou un **Service Worker** qui affiche une ancienne réponse. |
| **Solution** | **Cartographie** : lire `cartographie-pages-casapy-paralleles.md`. **Vérifier côté serveur** : `curl -s http://127.0.0.1:8010/p/casapy/` doit contenir « LPPP proposition.html », « \| LPPP » et « Page servie par Django ». Si oui, forcer le client : **fenêtre de navigation privée** (Ctrl+Shift+P) → http://localhost:8010/p/casapy/ ; ou vider les données du site (Stockage) / désactiver le Service Worker pour localhost:8010. Le bandeau vert a été rendu **sticky** (reste visible en haut au scroll) pour confirmer visuellement la Page A. |
| **Prévention** | Ne pas confondre l'URL Django (localhost:8010/p/casapy/) avec l'export statique (file:// ou Vercel). Pour valider les modifs template : navigation privée ou rechargement sans cache après `docker compose restart web`. Procédure détaillée : `procedure-modifications-landing-visible.md` § 5. |
| **Lien(s)** | `cartographie-pages-casapy-paralleles.md`, `procedure-modifications-landing-visible.md`, `deploy/PUSH-CASAPY.md` |

---

### GitLab désynchronisé — push oublié sur un remote

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Après `git push origin main` ; ou vérification des deux remotes (GitHub + GitLab) |
| **Erreur** | GitLab ne contient pas les derniers commits ; ou « on galère entre GitHub, GitLab et Vercel » (miroir incomplet). |
| **Cause** | Push effectué seulement sur `origin` (GitHub), pas sur `gitlab`. Vercel peut être lié à GitHub ; GitLab sert de backup/miroir — s’il n’est pas poussé, le miroir est faux. |
| **Solution** | Après chaque push sur `origin` : `git push gitlab main`. Si le remote `gitlab` n’existe pas : `git remote add gitlab git@gitlab.com:LucasTymen/<repo>.git` puis `git push -u gitlab main`. Utiliser `make push-both` (LPPP) si configuré, ou exécuter les deux pushes à la suite. |
| **Prévention** | Toujours pousser sur **les deux** remotes (origin + gitlab) après un commit. Checklist : `strategie-deploiement-git-vercel.md` (étape 3 : push origin puis push gitlab). Scripts type `push-standalone-p4s.sh` font les deux ; en manuel, ne pas oublier le second push. |
| **Lien(s)** | `git-remotes-github-gitlab.md`, `strategie-deploiement-git-vercel.md`, `pilotage-agents.mdc` (Git — commit + push sur les deux remotes) |

---

### Repo GitHub/GitLab créé avec README — conflit au premier push

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Premier push vers un repo fraîchement créé (GitHub ou GitLab) |
| **Erreur** | `! [rejected] main -> main (non-fast-forward)` ou refus de push car les historiques divergent (repo distant a un commit README, local a un autre premier commit). |
| **Cause** | Le repo a été créé avec « Initialize with README » (ou .gitignore / license), donc il a déjà un commit ; le dépôt local a un autre premier commit → deux historiques différents. |
| **Solution** | Option A : recréer le repo **sans** README, sans .gitignore, sans license, puis refaire `git push -u origin main` (et idem pour GitLab). Option B (si on ne peut pas recréer) : `git pull origin main --allow-unrelated-histories`, résoudre les conflits si besoin, puis `git push origin main`. Préférer Option A pour garder un historique propre. |
| **Prévention** | Toujours créer les repos **Create blank repository** / **Create blank project** **sans** cocher « Add README », « Add .gitignore », « Add license ». Voir `strategie-deploiement-git-vercel.md` (étape 1) et `git-remotes-github-gitlab.md`. |
| **Lien(s)** | `git-remotes-github-gitlab.md` § 6, `strategie-deploiement-git-vercel.md` (Pièges à éviter) |

---

### Vercel — Build Failed : Vulnerable version of Next.js (CVE-2025-66478)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Déploiement Vercel (LPPP_Ackuracy, LPPP_P4S-Architecture) ; build échoue avec message « Vulnerable version of Next.js detected, please update immediately ». |
| **Erreur** | Build Failed ; CVE-2025-66478 (React2Shell) — Next.js 15.0.0 à 16.0.6 affectés. |
| **Cause** | `next@15.1.3` (et versions similaires) dans `package.json` est vulnérable. |
| **Solution** | Mettre à jour Next.js vers une **version corrigée** : pour la branche 15.1.x utiliser **15.1.9** (`"next": "15.1.9"` dans package.json). Mettre à jour dans : `deploy/standalone-ackuracy/package.json`, `deploy/standalone-p4s/package.json`, `frontend/package.json`. Puis **commit + push** sur les repos concernés (ACKURACY, P4S) pour déclencher un nouveau build Vercel. |
| **Prévention** | Vérifier régulièrement [Next.js Security](https://nextjs.org/blog/CVE-2025-66478) et les alertes Vercel ; figer une version patchée (ex. 15.1.9) dans les package.json. |
| **Lien(s)** | [Next.js CVE-2025-66478](https://nextjs.org/blog/CVE-2025-66478), [Vercel CVE-2025-55182](https://vercel.com/changelog/cve-2025-55182) |

---

### Scripts bash push standalone — erreur CRLF ($'\r': command not found)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | WSL ou Git Bash, exécution de `bash deploy/push-standalone-p4s.sh` ou `bash deploy/push-standalone-ackuracy.sh` |
| **Erreur** | `$'\r': command not found`, `set: -: invalid option`, `cd: $'deploy/..\r': No such file or directory`, `fatal: remote error: is not a valid repository name`, `fatal: invalid refspec 'main?'`, `syntax error: unexpected end of file` |
| **Cause** | Fins de ligne **CRLF** (Windows) dans les fichiers `.sh` ; bash interprète le `\r` comme caractère, ce qui casse les commandes et les variables (REPO_DIR, refspec `main`). |
| **Solution** | 1) Convertir les scripts en **LF uniquement** : sous PowerShell `[System.IO.File]::ReadAllText("deploy\push-standalone-p4s.sh") -replace "`r`n", "`n" -replace "`r", "`n"` puis `WriteAllText` ; ou sous WSL `sed -i 's/\r$//' deploy/push-standalone-p4s.sh deploy/push-standalone-ackuracy.sh`. 2) `.gitattributes` avec `deploy/*.sh text eol=lf` pour que Git conserve le LF à l’avenir. |
| **Prévention** | Ne pas éditer les `.sh` avec un éditeur qui force le CRLF ; laisser `.gitattributes` gérer `eol=lf` pour `deploy/*.sh` et `scripts/*.sh`. Après correction, les scripts s’exécutent correctement (push P4S et ACKURACY vers GitHub + GitLab, Vercel rebuild). |
| **Lien(s)** | `deploy/README-standalone.md`, `deploy/push-standalone-p4s.sh`, `scripts/deploy-contabo.sh` |

---

### Deploy Contabo — rsync exclut .env.example (cp: cannot stat '.env.example')

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-07 |
| **Contexte** | Exécution de `make deploy-contabo` ; rsync envoie le projet vers Contabo. |
| **Erreur** | Sur le serveur : `cp: cannot stat '.env.example': No such file or directory`. |
| **Cause** | Rsync `--exclude='.env.*'` exclut tous les fichiers `.env.*`, y compris `.env.example`. |
| **Solution** | Exclusions explicites : `--exclude='.env'`, `--exclude='.env.local'`, `--exclude='.env.production'`. Ne pas exclure .env.example. |
| **Prévention** | Vérifier qu'un pattern d'exclusion rsync ne supprime pas les templates (.env.example). |
| **Lien(s)** | `scripts/deploy-contabo.sh` |

---

### Push GitHub/GitLab — authentification échouée (Windows / agent)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Déploiement P4S (ou autre standalone) : clone + copie + commit OK ; `git push origin main` échoue (PowerShell, Cursor, CI sans credentials). |
| **Erreur** | `Invalid username or token. Password authentication is not supported` (HTTPS) ou `Host key verification failed` (SSH). |
| **Cause** | GitHub n’accepte plus les mots de passe ; le terminal/agent n’a pas de PAT (Personal Access Token) ni de clé SSH configurée. |
| **Solution** | **Étape manuelle** : ouvrir un terminal où vous êtes déjà authentifié (Git Bash, GitHub Desktop, ou PowerShell après `gh auth login` / config SSH), puis `cd deploy/repo-p4s` (ou le repo concerné), `git push -u origin main`, puis `git push gitlab main`. Alternative : exécuter `.\deploy\push-standalone-p4s.ps1` (clone + commit), puis faire le push à la main depuis `deploy/repo-p4s`. |
| **Prévention** | Configurer un PAT (GitHub → Settings → Developer settings → Personal access tokens) pour HTTPS, ou SSH (clés + `ssh-add`), puis utiliser ce terminal pour le push final. |
| **Lien(s)** | `deploy/README-standalone.md`, `deploy/push-standalone-p4s.ps1` |

---

### SSH — Host key verification failed (GitHub / GitLab)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Push/pull vers GitHub ou GitLab en SSH : `git push origin main` ou `git push gitlab main` depuis Cursor, PowerShell, Git Bash ou WSL. |
| **Erreur** | `Host key verification failed. fatal: Could not read from remote repository.` |
| **Cause** | SSH ne reconnaît pas les clés d'hôte de GitHub/GitLab : `known_hosts` vide, mal configuré, ou environnement (PowerShell vs WSL) utilisant un `~/.ssh` différent. La clé privée peut être valide (ex. SquidResearch) mais le host n'est pas dans `known_hosts`. |
| **Solution** | **1)** Ajouter GitHub et GitLab à `known_hosts` : `ssh-keyscan -t ed25519 -t rsa github.com gitlab.com >> ~/.ssh/known_hosts` (exécuter depuis le même environnement que `git` — Git Bash ou WSL). **2)** Charger la clé : `ssh-add ~/.ssh/id_ed25519` (ou ta clé existante). **3)** Tester : `ssh -T git@github.com`, `ssh -T git@gitlab.com`. Doc complète : **`ssh-host-key-verification-github-gitlab.md`**. Fallback HTTPS : `git remote set-url origin https://github.com/...` + PAT. |
| **Prévention** | Exécuter une fois `ssh-keyscan` pour github.com et gitlab.com sur chaque environnement (PowerShell/Git Bash vs WSL). Réutiliser la clé SquidResearch ; s'assurer que l'agent SSH a la clé chargée. |
| **Lien(s)** | `ssh-host-key-verification-github-gitlab.md`, `git-remotes-github-gitlab.md` |

---

### CTA / Gmail sur landing statique — mailto: n’ouvre rien (Windows)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Landing P4S déployée en statique (Vercel) ; clic sur « Me contacter », CTA « Reprendre la conversation » ou lien Gmail. |
| **Erreur** | Rien ne se passe, ou message Windows « Ce fichier ne contient pas d’application associée » (pas de client mail par défaut pour `mailto:`). |
| **Cause** | Lien `mailto:` dépend du client mail configuré sur la machine du visiteur ; sous Windows sans client associé, le lien échoue. CTA et Gmail « en dur » ne déclenchaient aucune action. |
| **Solution** | **Popup (modal) contact** : tous les liens « Me contacter », CTA hero, CTA final et ligne Gmail ouvrent un **popup** (modal CSS `:target`) avec le texte : « Vous pouvez me contacter par Mail à cette adresse : [email] ». L’email est affiché en dur (sélectionnable/copiable). Fermeture par lien « Fermer » ou clic sur l’overlay. Aucun JavaScript ; compatible page statique. Template : `templates/landing_pages/proposition.html` (`.contact-modal`, `#contact-email-modal`). |
| **Prévention** | Sur les landings statiques (export Django → HTML), ne pas compter sur `mailto:` seul : proposer systématiquement le popup avec l’adresse en clair pour que le visiteur puisse copier. Tenir compte de cette contrainte dans tout nouveau template ou export. |
| **Lien(s)** | `deploy/PUSH-POUR-VERSION-COMPLETE.md`, `templates/landing_pages/proposition.html` |

---

### localhost:3010 — Flowise LPPP (pas aux landings Next.js)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Indication d’ouvrir une landing Next.js (ex. Ackuracy) sur http://localhost:3000. |
| **Erreur** | Confusion : le port 3000 est celui de **Flowise**, pas des apps Next.js standalone. |
| **Cause** | Next.js utilise 3000 par défaut ; dans LPPP, 3000 est attribué à Flowise. |
| **Solution** | Landings Next.js en local : **port 3001**. Ex. `cd deploy/standalone-ackuracy && npm run dev` → http://localhost:3001. Le script `dev` est configuré avec `-p 3001` dans `package.json`. Référence ports : `infra-devops.md` § 3.4. |
| **Prévention** | Ne jamais indiquer localhost:3010 pour une landing Next.js (3010 = Flowise LPPP) ; consulter `infra-devops.md` § 3.4 Ports avant de documenter ou proposer une URL de dev. |
| **Lien(s)** | `docs/base-de-connaissances/infra-devops.md` (§ 3.4), `deploy/standalone-ackuracy/README.md` |

---

### Templates / modèles de landing générés — meta description manquante (Lighthouse SEO)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-06 |
| **Contexte** | Génération de **nouveaux templates** ou **modèles** de landing (Django, Next.js, export HTML, conciergerie ou autre). Audit Lighthouse : score SEO dégradé. |
| **Erreur** | « Le document ne contient pas d'attribut meta description » (Lighthouse SEO). |
| **Cause** | Le template généré ou copié n'inclut pas la balise `<meta name="description" content="...">` dans le `<head>`. |
| **Solution** | Ajouter dans le `<head>` : `<meta name="description" content="Texte court (150–160 car.) décrivant la page.">`. Exemple : `templates/landing_pages/concierge_maisons_alfort.html`. |
| **Prévention** | **L'agent en charge des erreurs** (et tout agent qui crée ou génère des templates de landing) doit **prendre en note** : à chaque **nouveau modèle ou template** de page publique, inclure dans le `<head>` : (1) **meta description** (contenu adapté), (2) **viewport**, (3) **title** pertinent. Consulter `segmentations/2026-02-06-lighthouse-landing-maisons-alfort-rapport-seo-perf.md` et appliquer cette checklist avant de livrer un nouveau template. |
| **Lien(s)** | `segmentations/2026-02-06-lighthouse-landing-maisons-alfort-rapport-seo-perf.md`, `templates/landing_pages/concierge_maisons_alfort.html`, `expert-seo-demarche-rapport-wording-copywriting.md` |

---

### Fiche entretien emploi — section « Tests techniques » oubliée

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-02-05 |
| **Contexte** | Génération d'une fiche de préparation d'entretien (Assistant Entretien Emploi) pour une entreprise (ex. 0Flow). |
| **Erreur** | La section **Tests techniques** (programmation, growth, marketing, mix dev/growth) est absente de la fiche générée. L'utilisateur ne sait pas à l'avance si l'entretien sera orienté dev, marketing ou mix ; cette section est indispensable pour se préparer à tous les cas. |
| **Cause** | Le modèle canonique n'a pas été appliqué en entier : la section « 2. PROGRAMMATION – Questions techniques » du modèle (avec sous-parties programmation, growth, marketing, mix) a été omise lors de la génération. |
| **Solution** | Réintégrer la section complète depuis `_modele-canonique_prepa_entretien.html` (accordéon « TESTS TECHNIQUES — Programmation & Growth » et tout son contenu), puis renuméroter les sections suivantes (Questions à poser, Entreprise — Ce que vous devez savoir). |
| **Prévention** | **Toujours générer la fiche à partir du modèle canonique COMPLET** dès la première livraison. Inclure **toutes** les sections : 0 Présentation, 1 Formalités, 2 Q/R stratégiques, **3 Tests techniques** (programmation, growth, marketing, mix), 4 Questions à poser, 5 [Entreprise] — Ce que vous devez savoir. Inclure **tous** les textes, lexique, abréviations (KPI, CPA, CPL, CTA, etc.), questions à poser et tout ce qui peut être utile. Consulter `fiches-entretien-emploi-modele-et-veille.md` et la règle `assistant-entretien-emploi.mdc` ; l'Assistant Entretien Emploi doit s'assurer que le modèle canonique est copié en entier (structure + contenu type) avant d'adapter au cas par cas. |
| **Lien(s)** | `.cursor/rules/assistant-entretien-emploi.mdc`, `fiches-entretien-emploi-modele-et-veille.md`, `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html` |

### Menu burger mobile — liens du drawer non visibles (landing Promovacances)

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Landing Promovacances (index.html, proposition.html) : consultation sur **téléphone**. Le menu burger (waffle) s'affiche, mais les liens du drawer ne sont pas visibles. |
| **Erreur** | Sur mobile, l'icône burger s'affiche correctement ; au clic, le drawer s'ouvre (animation) mais les liens de navigation n'apparaissent pas. |
| **Cause** | Combinaison `transform: translateX(100%)` + `visibility` + `opacity` provoquant des bugs de rendu sur iOS/Safari. Z-index du drawer insuffisant. Possibles problèmes de `color-mix` pour le fond ou la couleur du texte. |
| **Solution** | 1) Remplacer `translateX` par `translate3d(100%, 0, 0)` (+ `-webkit-transform`) pour forcer le rendu GPU. 2) Augmenter le z-index du drawer (ex. 10001). 3) Ajouter `pointer-events: none` quand fermé et `pointer-events: auto` quand ouvert. 4) Fond de repli solide : `rgba(255,255,255,0.98)`. 5) Forcer la couleur des liens : `color: var(--lp-text-on-light, #001327) !important`. 6) `display: flex; align-items: center` sur les liens du drawer. 7) `-webkit-overflow-scrolling: touch` pour le scroll iOS. |
| **Prévention** | Lors de la création ou modification d'un menu burger / drawer mobile : utiliser `translate3d` plutôt que `translateX`, vérifier le z-index (drawer > nav), tester sur émulateur mobile et appareil réel (iOS). |
| **Lien(s)** | `deploy/static-promovacances-vercel/index.html`, `templates/landing_pages/proposition.html` |

### Liens internes target="_blank" — multiplication iframes YouTube → blocage « robot »

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Landing Promovacances (ou autre avec vidéo YouTube en fond) : navigation entre rapport, positionnement marketing, infographie, dashboard audit. |
| **Erreur** | YouTube affiche « Connectez-vous pour confirmer que vous n'êtes pas un robot ». La vidéo de fond ne s'affiche pas (blocage). Surtout observable en local (localhost) ou avec plusieurs onglets ouverts. |
| **Cause** | Liens internes avec `target="_blank"` ouvrent chaque page dans un **nouvel onglet**. Chaque onglet charge une iframe YouTube → multiplication des requêtes et iframes → détection anti-bot de YouTube. |
| **Solution** | Retirer `target="_blank"` des **liens internes** (rapport, positionnement, infographie, dashboard audit) pour qu'ils s'ouvrent dans la **même fenêtre**. Garder `target="_blank"` pour les liens **externes** (LinkedIn, sources, etc.). Fichiers concernés : `deploy/static-promovacances-vercel/index.html`, `templates/landing_pages/proposition.html`, `includes/nav_landing_annexes.html`. |
| **Prévention** | Règle : **liens internes** (même site / même déploiement) = navigation même fenêtre (sans target="_blank") ; **liens externes** = nouvel onglet (target="_blank" rel="noopener noreferrer"). Alternative si blocage persistant : utiliser une vidéo auto-hébergée (MP4/WebM) en fond au lieu de YouTube. |
| **Lien(s)** | `deploy/static-promovacances-vercel/`, `templates/landing_pages/proposition.html`, `includes/nav_landing_annexes.html` |

### Crash / reprise — tâche multi-étapes recommencée du début

| Champ | Contenu |
|-------|---------|
| **Date** | 2026-01-30 |
| **Contexte** | Cursor ou autre IDE : crash en cours de tâche multi-étapes (ex. création landing infopro, duplication Promovacances). La même tâche a été recommencée 4–5 fois du début, perte de temps. |
| **Erreur** | Pas d’erreur technique visible — l’agent ou la session s’interrompt avant la fin ; à la reprise, aucun marqueur de progression, on repart de zéro. |
| **Cause** | Absence de sauvegarde incrémentale et de marqueurs de progression ; tout était en cours, rien de committé ni documenté. |
| **Solution** | 1) **Sauvegarder à chaque étape** : commit git après chaque bloc logique (1–3 fichiers), message explicite. 2) **Marquer la progression** : commentaires timestamp dans le code ou fichier `.progress-<slug>.md` temporaire (ex. `# [2026-01-30 14:32] Étape 1/4 — dossier infopro créé`). 3) **À la reprise** : reprendre au **dernier marqueur** connu (consulter les commits récents, TODO, ou fichier de progression). 4) **Une fois terminé** : retirer les marqueurs temporaires. |
| **Prévention** | Règle **« Sauvegarde incrémentale obligatoire »** dans `pilotage-agents.mdc` : tous les agents sauvegardent systématiquement chaque étape, ajoutent des timestamps en commentaire, les retirent quand la tâche est terminée. L’agent en charge des erreurs vérifie cette règle et documente les reprises. Décision : `decisions.md`. |
| **Lien(s)** | `pilotage-agents.mdc` § « Sauvegarde incrémentale obligatoire », `decisions.md`, `erreurs-et-solutions.md` § « Pour l’agent en charge des erreurs » |

---

*Dernière mise à jour : 2026-01-30 — Sauvegarde incrémentale et reprise après crash. Stratégie fluide : `strategie-deploiement-git-vercel.md`.*
