# Démarrer le projet — équipe technique

**Rôle** : Checklist et diagnostic pour que le projet redémarre et que les rendus des landing pages soient visibles.  
**Pilotes** : DevOps, Dev Django.  
**Référence** : `pret-a-demarrer.md`, `infra-devops.md`, Makefile.

---

## 1. Objectif

- Faire **redémarrer le projet** (Docker ou Option B).
- Permettre d’**utiliser le projet naturellement** et de **voir les rendus des landing pages**.

---

## 2. Checklist démarrage

### Option A — Docker (stack complet)

| Étape | Commande / action | Vérification |
|-------|-------------------|---------------|
| 1 | Fichier `.env` présent à la racine (copie de `.env.example`, SECRET_KEY et mots de passe renseignés) | `ls -la .env` ou vérifier dans l’explorateur |
| 2 | `make start` ou `make go` (WSL/Linux/Git Bash) | Les conteneurs db, redis, web, celery démarrent |
| 3 | `make createsuperuser` (si premier lancement) | Compte admin créé |
| 4 | Ouvrir http://localhost:8000/admin/ | Connexion admin OK |
| 5 | Ouvrir http://localhost:8000/essais/ | Interface essais s’affiche |
| 6 | Ouvrir http://localhost:8000/landings/ ou URL des campagnes/landings | Liste des landings (si routes en place) |

**Arrêt** : `make down`.

### Option B — Dev local (PostgreSQL + Redis en Docker, Django en local)

| Étape | Commande / action | Vérification |
|-------|-------------------|---------------|
| 1 | `docker compose up -d db redis` | Ports 5432 et 6379 exposés |
| 2 | `.env` avec `DB_HOST=localhost`, `REDIS_URL=redis://127.0.0.1:6379/0`, etc. | Voir `pret-a-demarrer.md` § Option B |
| 3 | Venv activé, `pip install -r requirements.txt`, `python3 manage.py migrate`, `python3 manage.py createsuperuser` | Migrations OK |
| 4 | `make runserver` ou `python3 manage.py runserver 127.0.0.1:8080` (WSL : **python3**) | http://127.0.0.1:8080/admin/ et /essais/ accessibles |

### Voir les rendus des landing pages

- **Django (templates)** : admin → Landing pages ; ou URL dédiée (ex. `/p/<slug>/` si implémentée).
- **Next.js (frontend)** : en local `cd frontend && npm run dev` → http://localhost:3000/ et http://localhost:3000/p4s-archi. En prod : Vercel (URL déployée).

---

## 3. Causes fréquentes de blocage

| Problème | Piste de résolution |
|----------|---------------------|
| **Docker : ERR_EMPTY_RESPONSE ou port 8000 inaccessible** | Sous Windows : utiliser **Option B** (runserver 127.0.0.1:8080) ou WSL pour lancer Docker. Voir `pret-a-demarrer.md` § 5. |
| **Django / admin inaccessible (problème réseau)** | **Option B (WSL)** : à la racine du projet (répertoire d’origine ou chemin actuel), lancer **`bash scripts/runserver-wsl.sh`** (port 8080) ou **`bash scripts/runserver-wsl.sh 8082`** si 8080 est occupé. S’assurer que `db` et `redis` tournent (`docker start lppp_db lppp_redis`). Puis ouvrir **http://127.0.0.1:8080/admin/** (ou le port choisi). Sinon : sprint `segmentations/2026-01-30-sprint-resolution-reseau-django.md`. |
| **Migrations en erreur** | `make migrate` ou `docker exec web python manage.py migrate --noinput`. Vérifier DB_HOST et credentials dans `.env`. |
| **Module not found / ImportError** | Vérifier PYTHONPATH, venv activé, ou rebuild image Docker (`make build` puis `make up`). |
| **PostgreSQL pas prêt** | L’entrypoint attend la DB ; si timeout, augmenter les sleep dans `go` ou vérifier santé : `docker compose ps`, `docker compose logs db`. |
| **.env manquant ou vide** | Copier `.env.example` vers `.env`, renseigner SECRET_KEY, DB_PASSWORD, etc. |

---

## 4. Commandes utiles

```bash
# Docker
make start      # Démarrage (docker-up-seq + attente Django + migrate)
make go        # Démarrage à froid complet (build + up + migrate + collectstatic)
make down      # Tout arrêter
make logs-web  # Logs du service web
make health-check  # Santé des services

# Option B (local)
docker compose up -d db redis
source .venv/bin/activate   # ou .venv\Scripts\Activate.ps1 (Windows)
python manage.py migrate --noinput
make runserver
```

---

## 5. Rendu des landings : deux chemins

| Chemin | Usage | URL type |
|--------|--------|----------|
| **Django (templates)** | Admin, liste/détail campagnes, page landing par slug si vue en place | http://localhost:8000/admin/ ; http://localhost:8000/p/\<slug\>/ |
| **Next.js (frontend)** | Pages déployées sur Vercel ; en local `npm run dev` dans `frontend/` | http://localhost:3000/p4s-archi ; https://\<projet\>.vercel.app/p4s-archi |

L’équipe peut **unifier progressivement** sur Next.js pour les rendus publics tout en gardant Django pour l’admin et l’API.

---

## 6. Suite : classer les landings par secteur et catégorie

Pour une utilisation « naturelle » et des rendus faciles à parcourir, voir la proposition dans `classification-landings-secteur-categorie.md` (secteurs, catégories, filtres liste).

---

*Document créé pour l’équipe technique. Dernière mise à jour : 2025-01-30.*
