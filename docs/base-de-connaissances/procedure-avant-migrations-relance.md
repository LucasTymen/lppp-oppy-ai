# Procédure avant migrations et relance

**Objectif** : sécuriser l’état du dépôt avant d’appliquer des migrations ou de relancer le système, pour pouvoir revenir en arrière si besoin.

**Pilotes** : DevOps (relance, infra), Dev Django (migrations), Architecte (cohérence).  
**Référence** : `strategie-operationnelle-make.md`, `checklist-pre-prod-integrite.md`, `Makefile`.

---

## 1. Ordre recommandé

| Étape | Action | Qui | Commande / détail |
|-------|--------|-----|--------------------|
| **1** | **Sauvegarder l’état** | DevOps / Chef de Projet | **1a)** `make backup` (dump PostgreSQL → `backups/backup_*.sql`). **1b)** Commit + push (origin + gitlab) pour ne pas perdre l’état actuel. Voir § 2.1. |
| **2** | **Migrations** (si changement de modèles) | Dev Django | `make makemigrations` puis `make migrate` (ou exécuter dans le conteneur `web`). |
| **3** | **Relancer le système** | DevOps | `make relance` (sans rebuild) ou `make start` (démarrage + migrate automatique). |

---

## 2. Détail des étapes

### 2.1 Sauvegarde (base de données + dépôt) avant toute migration ou relance risquée

À faire **depuis la racine du projet** (conteneurs **db** et **web** démarrés).

**1. Sauvegarde de la base PostgreSQL**

```bash
make backup
```

→ Crée `backups/backup_YYYYMMDD_HHMMSS.sql`. Nettoyage : `make backup-clean` (garde 7 jours). Voir `protection-donnees-et-sauvegardes.md`.

**2. Commit et push (état du code)**

```bash
cd /chemin/vers/homelucastoolsLandingsPagesPourProspections   # ou ton chemin projet

git status
git add .
git commit -m "chore: état avant migrations / relance — sauvegarde"
make push-both
```

Si `make push-both` n’est pas utilisé :  
`git push origin main && git push gitlab main`

**Pourquoi** : en cas d’échec des migrations ou de la relance, on peut revenir à ce commit (ou comparer l’état).

### 2.2 Migrations (uniquement si les modèles Django ont changé)

**Prérequis** : le stack Docker doit être démarré (au moins `db` et `web`). Sinon : `make start` ou `make up` avant d’exécuter les commandes ci‑dessous. Si tu vois *« service "web" is not running »* → lancer d’abord `make start`.

- **Créer les migrations** (après modification de `models.py`) :  
  `make makemigrations`  
  (ou `docker compose exec web python manage.py makemigrations`)
- **Appliquer les migrations** :  
  `make migrate`  
  (ou `docker compose exec web python manage.py migrate --noinput`)

Si aucun fichier de modèle n’a été modifié, **pas besoin** de `makemigrations` ; `make migrate` applique simplement les migrations déjà présentes dans `*/migrations/*.py`.

### 2.3 Relance du système

- **Redémarrer sans rebuild** (containers déjà construits) :  
  `make relance`
- **Démarrer tout** (avec attente Django + migrate automatique) :  
  `make start`
- **Démarrage à froid** (tout recréer, **attention : `make go` supprime les volumes**) :  
  `make go` — à réserver aux cas « tout reprendre à zéro ».

Après relance : `make health-check` et `make services-urls` pour vérifier que les services répondent.

---

## 3. Rôle de l’équipe

| Rôle | Responsabilité |
|------|----------------|
| **Architecte** | S’assurer que la procédure (commit → migrations → relance) est respectée et documentée ; pas de migration en prod sans état versionné. |
| **DevOps** | Exécuter commit/push et relance ; vérifier santé des services après relance. |
| **Dev Django** | Créer et appliquer les migrations ; vérifier qu’aucune migration en attente ne casse le schéma. |
| **Chef de Projet** | Valider qu’on ne relance pas sans sauvegarde (commit/push) quand c’est une opération à risque. |

---

## 4. Références

- **Make** : `make help`, `Makefile` (racine) ; **backup BDD** : `make backup`, `make backup-clean`, `make restore` — voir `protection-donnees-et-sauvegardes.md`
- **Stratégie opérationnelle** : `strategie-operationnelle-make.md`
- **Checklist pré-prod** : `checklist-pre-prod-integrite.md` (migrations, intégrité)
- **Git (deux remotes)** : `git-remotes-github-gitlab.md`, `make push-both`

---

*Document créé pour aligner l’équipe technique (Architecte, DevOps, Dev Django) sur la séquence : sauvegarde → migrations → relance. Dernière mise à jour : 2025-02-03.*
