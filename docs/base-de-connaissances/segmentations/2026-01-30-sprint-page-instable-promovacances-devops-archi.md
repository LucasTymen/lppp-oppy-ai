# Sprint : Page instable (Promovacances) — DevOps, Architecte, Ingénieur Système & Réseau

**Date** : 2026-01-30  
**Statut** : 🟡 À traiter  
**Pilotes** : **DevOps**, **Architecte réseau**, **Ingénieur Système et Réseau**  
**RACI** : DevOps R (diagnostic infra, déploiement, Vercel) ; Architecte R (flux, routage, ports) ; Ingénieur Sys R (connexion, résolution, stabilité)

---

## 1. Contexte

L’utilisateur signale que **la page est instable**. Deux environnements possibles :

| Environnement | URL | Stack |
|---------------|-----|-------|
| **Local (Django)** | http://localhost:8010/p/promovacances/ | Docker LPPP (lppp_web, db, redis), port 8010 |
| **Prod (Vercel)** | URL du projet LPPP_promovacances sur Vercel | Export statique HTML, GitHub LPPP_promovacances |

Références : `docs/contacts/promovacances/README.md`, `deploy/PUSH-PROMOVACANCES.md`, `infra-devops.md` (§ 3.4), `erreurs-et-solutions.md`.

---

## 2. Diagnostic — checklist par environnement

### A. Local (Django 8010)

| # | Vérification | Commande / action | Responsable |
|---|--------------|-------------------|-------------|
| 1 | Conteneurs LPPP démarrés | `docker compose ps` — db, redis, web Up | DevOps |
| 2 | Port 8010 exposé | `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8010/` → 200 | Ingénieur Sys |
| 3 | Pas de conflit de ports | `netstat -an \| grep 8010` (ou équivalent) ; aucun autre processus sur 8010 | Architecte |
| 4 | Conteneurs orphelins | Si `container name already in use` : `make clean-containers` puis `make start` | DevOps |
| 5 | Web en crash loop | `docker compose logs web --tail 100` — corriger erreur (Import, DB, .env) | DevOps |
| 6 | ERR_CONNECTION_REFUSED / RESET | Si Docker web inaccessible (Windows) : Option B runserver sur 8080 (voir `pret-a-demarrer.md` § 5) | Ingénieur Sys |
| 7 | Landing en base | `make landings-restore` si 404 « No LandingPage » | DevOps |

Référence : `erreurs-et-solutions.md` (Docker, 404, auth Postgres).

### B. Prod (Vercel — landing statique Promovacances)

| # | Vérification | Commande / action | Responsable |
|---|--------------|-------------------|-------------|
| 1 | Build Vercel OK | Dashboard Vercel → projet LPPP_promovacances → dernier déploiement « Ready » | DevOps |
| 2 | URL principale 200 | `curl -s -o /dev/null -w "%{http_code}" <URL_VERCEL>` | Ingénieur Sys |
| 3 | Rewrites rapport | `/p/promovacances/rapport/` → `/rapport.html` (voir `vercel.json`) | Architecte |
| 4 | CLS / layout shift | Lighthouse ou DevTools → Layout Shift ; images sans dimensions → ajouter width/height | Architecte / DevOps |
| 5 | LCP / lenteur | Optimiser images, précharger hero ; vérifier ressources bloquantes | Architecte |
| 6 | Cache / contenu obsolète | Headers Cache-Control ; recharger sans cache (Ctrl+Shift+R) | DevOps |
| 7 | Liens cassés | Vérifier nav (index, rapport, infographie, positionnement-marketing) | Ingénieur Sys |

---

## 3. Actions correctives prioritaires

### Local

1. **Conteneurs orphelins** : `make clean-containers && make start`
2. **Base vide (404)** : `make landings-restore`
3. **Web crash loop** : corriger selon logs (`docker compose logs web`), puis `make start`
4. **Windows / WSL** : si ERR_CONNECTION_REFUSED ou RESET sur 8010, appliquer Option B (runserver 8080) — `pret-a-demarrer.md` § 5

### Vercel

1. **404 rapport** : vérifier `vercel.json` rewrites ; s’assurer que `rapport.html` est bien dans le repo et déployé
2. **Layout instable (CLS)** : ajouter `width` et `height` sur images hero/principales ; navbar sticky (`position: sticky; top: 0; z-index: 100`)
3. **Performance** : réduire taille images, précharger LCP

---

## 4. Livrables attendus

- [ ] Diagnostic : identification de la cause (local vs Vercel, symptôme précis)
- [ ] Correction appliquée et vérifiée
- [ ] Mise à jour de `erreurs-et-solutions.md` si nouvelle erreur identifiée
- [ ] Mise à jour de `log-projet.md` ou `log-ia.md` selon les règles projet

---

## 5. Références

- `docs/base-de-connaissances/erreurs-et-solutions.md` — erreurs connues (Docker, 404, Postgres, etc.)
- `docs/base-de-connaissances/pret-a-demarrer.md` — Option A (Docker 8010), Option B (runserver 8080)
- `docs/base-de-connaissances/procedure-modifications-landing-visible.md` — cache, base, templates
- `docs/base-de-connaissances/procedure-fin-landing-repo-deploiement.md` — vérification page OK
- `.cursor/rules/devops.mdc` — orchestration, flux, secrets
