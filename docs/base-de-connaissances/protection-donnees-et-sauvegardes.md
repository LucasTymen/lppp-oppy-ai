# Protection des données et sauvegardes LPPP

**Objectif** : Garantir que les données (base PostgreSQL, workflows Flowise/n8n, volumes Docker) ne sont jamais perdues par erreur ; tous les agents sont **non destructifs** et les sauvegardes sont documentées et exécutables.

**Référence** : `.cursor/rules/pilotage-agents.mdc` (§ Agents non destructifs — protection des données).

---

## 1. Principes (tous les agents)

- **Ne jamais** proposer ni exécuter une action qui supprime ou réinitialise des données sans **sauvegarde préalable** et **demande explicite** de l’utilisateur.
- **Interdictions** : pas de `docker compose down -v`, pas de recréation de base/volume « pour repartir à zéro », pas de suppression de données ou de workflows sans backup et accord.
- **Correctifs** : privilégier les solutions **sans perte** (aligner .env sur l’existant, créer un utilisateur côté Postgres, etc.) avant toute réinitialisation.

---

## 2. Sauvegarde PostgreSQL (Docker)

- **Commande** : **`make backup`**
- **Effet** : `pg_dump` depuis le conteneur **db** vers `backups/backup_YYYYMMDD_HHMMSS.sql`. Le user et la base utilisés sont ceux du **.env** (`DB_USER`, `DB_NAME`).
- **Fréquence recommandée** : avant toute migration ou relance à risque ; avant changement de credentials ou de volume ; régulièrement en dev (ex. hebdo).
- **Restauration** : `make restore` liste les fichiers ; restauration manuelle :  
  `docker compose exec -i db psql -U <DB_USER> <DB_NAME> < backups/backup_XXX.sql`
- **Nettoyage** : `make backup-clean` supprime les sauvegardes de plus de 7 jours.

**Procédure avant migrations/relance** : l’étape « Sauvegarder l’état » inclut désormais **1a)** `make backup` puis **1b)** commit + push. Voir `procedure-avant-migrations-relance.md` § 2.1.  
**Référence** : `Makefile` (cibles `backup`, `restore`, `backup-clean`), `strategie-operationnelle-make.md`.

---

## 2.1 Sauvegarde automatique (cron / Planificateur de tâches)

- **Script** : **`scripts/backup-auto.sh`** — exécute `make backup` puis `make backup-clean` (ne garde que les 7 derniers jours). À lancer depuis la **racine du projet** ; les conteneurs Docker (**db**) doivent être démarrés.
- **Crontab (WSL / Linux)** : pour une sauvegarde quotidienne à 2 h du matin :
  ```bash
  crontab -e
  # Ajouter (adapter PROJECT_ROOT) :
  0 2 * * * cd /home/lucas/tools/homelucastoolsLandingsPagesPourProspections && bash scripts/backup-auto.sh >> backups/cron-backup.log 2>&1
  ```
  Si le projet est sous Windows (accès depuis WSL) : remplacer le chemin par le chemin WSL vers le projet (ex. `/mnt/c/home/lucas/tools/homelucastoolsLandingsPagesPourProspections`).
- **Windows (Planificateur de tâches)** : créer une tâche qui lance WSL puis le script, ex. :
  `wsl -e bash -c "cd /mnt/c/home/lucas/tools/homelucastoolsLandingsPagesPourProspections && bash scripts/backup-auto.sh"`.
- **Prérequis** : Docker en cours d’exécution et conteneur **lppp_db** démarré au moment de l’exécution. Si la machine est éteinte à l’heure du cron, la sauvegarde ne tourne pas ce jour-là.

---

## 3. Sauvegarde des workflows (Flowise, n8n)

- **Flowise** : tout chatflow créé ou modifié doit être exporté en JSON et déposé dans **`docs/flowise-workflows/backups/`** (nom + date). Réinjection : Load sur le canvas.
- **n8n** : tout workflow créé ou modifié doit être exporté et déposé dans **`docs/n8n-workflows/`**.
- **Procédure détaillée** : **`sauvegarde-workflows-flowise-n8n.md`**.

---

## 4. En cas d’erreur d’auth PostgreSQL (conteneur web)

- **Garder les credentials existants** : si le volume Postgres a été créé avec `Lucas@dmin` / `Lucas@dm1n`, laisser **`DB_USER=Lucas@dmin`**, **`DB_PASSWORD=Lucas@dm1n`** dans le .env. En Docker : **`DB_HOST=db`**, **`REDIS_URL=redis://redis:6379/0`** (et idem Celery).
- **Ne jamais proposer `docker compose down -v`** sans sauvegarde et accord explicite de l’utilisateur.
- **Détail** : `erreurs-et-solutions.md` (§ « password authentication failed for user »), `segmentations/2026-02-09-brief-devops-auth-postgres-conteneur-web.md`.

---

## 5. Récapitulatif

| Données              | Sauvegarde                                      | Pilote / règle                    |
|----------------------|--------------------------------------------------|-----------------------------------|
| Base PostgreSQL      | `make backup` → `backups/backup_*.sql` ; **automatique** : `scripts/backup-auto.sh` (cron / Planificateur) | DevOps ; avant migrations/relance |
| Workflows Flowise    | Export JSON → `docs/flowise-workflows/backups/`  | Automatizer, voir sauvegarde-workflows-flowise-n8n.md |
| Workflows n8n        | Export → `docs/n8n-workflows/`                   | Idem                              |

*Document créé pour formaliser la protection des données et les procédures de sauvegarde (2026-02-09). Sauvegarde automatique (script + cron) ajoutée 2026-01-30.*
