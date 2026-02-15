# Brief DevOps + Orchestrateur — Auth PostgreSQL et conteneur web (crash loop)

**Date** : 2026-02-09  
**Statut** : 🟢 Traité (correctif appliqué)  
**Pilotes** : **DevOps** (R), **Orchestrateur** (I — mise à jour registre / erreurs-et-solutions).

---

## Contexte (remontée utilisateur)

Après `make clean-containers` puis `make up`, le conteneur **lppp_web** redémarre en boucle. `make migrate` et `make migrate-wait` échouent : « Container … is restarting ».

**Logs web** : `django.db.utils.OperationalError: password authentication failed for user "Lucas@dmin"`.

---

## Cause identifiée

- Dans le **.env** : `DB_USER=Lucas@dmin` et `DB_PASSWORD=Lucas@dm1n` (credentials personnalisés).
- Le conteneur **lppp_db** (PostgreSQL) est initialisé avec `POSTGRES_USER` / `POSTGRES_PASSWORD` lus depuis le .env. Si le **volume PostgreSQL** a été créé auparavant avec d’autres valeurs (ex. `lpppuser` / `lppppass123`), puis que le .env a été changé en `Lucas@dmin`, la connexion échoue (user ou mot de passe incohérent entre ce que Django envoie et ce que Postgres attend).
- Par ailleurs : **DB_HOST=localhost** et **REDIS_URL=redis://127.0.0.1:6379** dans le .env empêchent le conteneur **web** de joindre les services **db** et **redis** (dans Docker, les hôtes sont **db** et **redis**).

---

## Correctif appliqué (non destructif — protection des données)

- **.env** : **garder les credentials existants** du volume Postgres pour ne pas perdre les données. Si la base a été créée avec `Lucas@dmin` / `Lucas@dm1n`, conserver **`DB_USER=Lucas@dmin`**, **`DB_PASSWORD=Lucas@dm1n`**.
- **Docker** : **`DB_HOST=db`**, **`DB_PORT=5432`** (conteneur web doit joindre le service `db`). **`REDIS_URL=redis://redis:6379/0`**, **`CELERY_BROKER_URL=redis://redis:6379/1`**, **`CELERY_RESULT_BACKEND=redis://redis:6379/2`**.
- **docker-compose** : `POSTGRES_USER` / `POSTGRES_PASSWORD` doivent correspondre au .env pour les **nouveaux** volumes ; pour un volume existant, le .env doit correspondre à l’user déjà créé dans le volume (pas de down -v).
- **N8N / Flowise** : identifiants `Lucas@dmin` / `Lucas@dm1n` laissés en place (auth des apps, pas PostgreSQL).

---

## Actions demandées

### DevOps

- [ ] **Vérifier** qu’après correction du .env, `make up` puis `make migrate-wait` (ou `make migrate`) réussissent.
- [ ] **Protection des données** : si le volume Postgres a été créé avec `Lucas@dmin` : **garder** `DB_USER=Lucas@dmin` et `DB_PASSWORD=Lucas@dm1n` dans le .env (pas de down -v). Réinitialisation (down -v) uniquement sur **demande explicite** de l’utilisateur et **après `make backup`** — voir `protection-donnees-et-sauvegardes.md`.
- [ ] Rappeler dans la doc (ex. `infra-devops.md` ou `pret-a-demarrer.md`) : **DB_USER/DB_PASSWORD doivent correspondre à POSTGRES_USER/POSTGRES_PASSWORD** ; en Docker, **DB_HOST=db**, **Redis/Celery = redis://redis:6379**.

### Orchestrateur

- [ ] **Documenter** l’incident dans `docs/base-de-connaissances/erreurs-et-solutions.md` (entrée « password authentication failed for user … » / DB_USER incohérent).
- [ ] S’assurer que le **registre** et les règles **devops.mdc** / **orchestrateur.mdc** renvoient bien vers `infra-devops.md` et `.env.example` pour les variables DB/Redis.

---

## Références

- `docker-compose.yml` (POSTGRES_USER, POSTGRES_PASSWORD)
- `.env.example` (DB_*, REDIS_URL, CELERY_*)
- `docs/base-de-connaissances/erreurs-et-solutions.md` (entrée « Container … is restarting », à compléter avec cause auth Postgres)
- `docs/base-de-connaissances/infra-devops.md` (§ variables d’env)

*Brief créé après diagnostic du crash loop lppp_web (auth PostgreSQL). Dernière mise à jour : 2026-02-09.*
