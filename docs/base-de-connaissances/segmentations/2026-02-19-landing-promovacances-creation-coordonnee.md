# Segmentation — Création landing Promovacances (action coordonnée)

**Date** : 2026-02-19  
**Contexte** : LPPP — PPP Promovacances (rapport audit SEO). La landing n’apparaît pas tant que l’entrée en base n’est pas créée ; la commande doit être exécutée **dans le conteneur Docker** (host DB = `db`).  
**Rôles** : Chef de Projet (cadrage), DevOps (stack + exécution), Architecte (structure), Ingénieur Sys (exécution).

---

## 1. Où on se trouve (racine projet LPPP)

La **racine du projet LPPP** est le répertoire qui contient :

- `Makefile`
- `manage.py`
- `docker-compose.yml`
- `apps/`, `docs/`, `lppp/`, `templates/`

**Sous WSL** : le chemin peut être un bind mount du type  
`/mnt/wsl/docker-desktop-bind-mounts/Ubuntu-22.04/<hash>/`  
ou un clone classique (`~/tools/homelucastoolsLandingsPagesPourProspections`).  
**Sous Windows** : `c:\home\lucas\tools\homelucastoolsLandingsPagesPourProspections`.

**À faire** : ouvrir un terminal et `cd` dans ce répertoire. Vérifier avec `ls Makefile manage.py docker-compose.yml` (ou `dir` sous Windows).

---

## 2. Problèmes rencontrés

- `python3 manage.py create_landing_promovacances --publish` → **failed to resolve host 'db'**  
  → La config Django pointe vers le service Docker `db` ; en dehors du réseau Docker, ce hostname n’existe pas.

- `make landing-promovacances` → **service "web" is not running**  
  → Le stack Docker (db, redis, web, …) n’est pas démarré.

---

## 3. Séquence coordonnée (tout lancer depuis la racine)

| Étape | Qui | Action | Commande |
|-------|-----|--------|----------|
| 1 | DevOps / Ingénieur Sys | (Optionnel) Nettoyer conteneurs orphelins | `make clean-containers` |
| 2 | DevOps | Démarrer le stack (db, redis, web, …) | `make start` |
| 3 | — | Attendre la fin (Django prêt, URLs affichées) | — |
| 4 | DevOps / Ingénieur Sys | Créer la landing Promovacances en base | `make landing-promovacances` |

**En une seule commande** (tout enchaîner) :

```bash
make clean-containers && make landing-promovacances-full
```

(En cas de conflit « container name already in use » ; sinon `make landing-promovacances-full` seul.) Cette cible Make enchaîne `make start` puis `make landing-promovacances`. À utiliser quand le stack n’est pas encore démarré.

---

## 4. Vérifications après création

- **Liste des landings** : http://localhost:8010/ (ou l’URL affichée par `make services-urls`) → Promovacances doit apparaître.
- **Admin Django** : http://localhost:8010/admin/landing_pages/landingpage/ → une entrée « Lucas Tymen — PPP Promovacances (rapport audit SEO) », slug `promovacances`.
- **Page proposition** : http://localhost:8010/p/promovacances/
- **Dashboard audit** : http://localhost:8010/p/promovacances/audit-dashboard/

---

## 5. Références

- **Stratégie Make** : `docs/base-de-connaissances/strategie-operationnelle-make.md`  
- **Log commun LPPP / SquidResearch** : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md` (pointeur)  
- **Promovacances** : `docs/contacts/promovacances/README.md`  
- **Registre agents** : `docs/base-de-connaissances/registre-agents-ressources.md`
