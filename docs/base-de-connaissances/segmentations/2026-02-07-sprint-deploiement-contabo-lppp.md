# Sprint — Déploiement LPPP sur Contabo (Orchestrateur, Architecte, DevOps)

**Date** : 2026-02-07  
**Statut** : 🟡 En cours  
**Objectif** : Déployer LPPP sur le serveur Contabo et lancer tous les services, **sous supervision de l'Orchestrateur, de l'Architecte et du DevOps**, sans endommager SquidResearch.

**Règle absolue** : Aucun secret (clés privées, mots de passe, credentials) ne doit être créé ni stocké dans le dépôt. Les vrais secrets restent sur la machine locale (`~/.ssh/contabo_key`), dans les secrets CI/CD, ou sur le serveur.

**Log commun** : Consulter `docs/base-de-connaissances/log-commun-lppp-squidresearch.md` avant toute action. **SquidResearch a la priorité** ; LPPP s'adapte. Réf. `deploiement-contabo-lppp-securite.md`.

---

## Contexte

- **Serveur Contabo** : déploiement LPPP à côté de SquidResearch.
- **Documentation source** : SquidResearch (dépôt externe) — adresses, clé SSH, chemins. Les agents LPPP s'appuient sur ce sprint sans dupliquer les secrets.
- **Isolation** : LPPP dans un répertoire séparé (ex. `/var/www/lppp`), SquidResearch inchangé dans `/var/www/squidresearch`.

---

## Informations Contabo (documentées dans SquidResearch — pas de secret dans LPPP)

| Élément | Valeur | Source |
|---------|--------|--------|
| **IP / host** | 173.249.4.106 | SquidResearch |
| **Utilisateur SSH** | root | SquidResearch |
| **Commande connexion** | `ssh -i ~/.ssh/contabo_key root@173.249.4.106` | SquidResearch |
| **Clé SSH** | `~/.ssh/contabo_key` (côté machine locale) | Non dans le dépôt — machine utilisateur ou secrets CI |
| **SquidResearch (serveur)** | `/var/www/squidresearch` | Ne pas écraser |
| **LPPP (serveur)** | `/var/www/lppp` (ou équivalent) | À créer / utiliser |

**Credentials** (n8n, Flowise, DB, etc.) : **pas dans le repo**. Sur le serveur, dans `.env` ou `.env.production` du dépôt concerné. Exemple côté SquidResearch : `grep -E '^N8N_BASIC_AUTH_|^FLOWISE_' .env.production` (après `cd` dans le bon dépôt).

---

## Supervision — Rôles

| Rôle | Responsabilité |
|------|----------------|
| **Orchestrateur** | Coordination de l'équipe, mise à jour du registre, alignement des procédures, s'assurer que DevOps/Architecte/Chef de projet sont alignés. |
| **Architecte** | Schéma d'isolation (réseau, répertoires, reverse proxy), règles de routage pour que LPPP et SquidResearch ne se chevauchent pas. |
| **DevOps** | Exécution du déploiement : SSH, clone, .env, docker-compose, ports, commandes. Isolation des stacks, vérification de la santé. |
| **Chef de Projet** | Validation du plan, checklist pré-déploiement, mise à jour des logs et de la base de connaissances. |
| **Pentester** | Revue sécurité (vulnérabilités, durcissement, recommandations) — voir `deploiement-contabo-lppp-securite.md`. |

**Aucun déploiement LPPP sur Contabo en prod sans** : validation DevOps (isolation, ports), validation Architecte (schéma), validation Chef de projet (plan), audit Pentester (recommandations appliquées).

---

## Tâches par agent

### Orchestrateur
- [ ] Vérifier que le **registre** (`registre-agents-ressources.md`) référence ce sprint et les docs déploiement.
- [ ] S'assurer que **Architecte** et **DevOps** ont les mêmes prérequis (chemins, ports, priorité SquidResearch).
- [ ] Coordonner avec le **Chef de Projet** pour la validation finale et la mise à jour des logs.

### Architecte
- [ ] Valider le **schéma d'isolation** : LPPP dans `/var/www/lppp`, SquidResearch dans `/var/www/squidresearch` ; aucun chevauchement.
- [ ] Documenter les **règles de routage** (reverse proxy, domaines/sous-domaines) pour LPPP vs SquidResearch — si applicable.
- [ ] Confirmer les **ports LPPP** : 8010 (Django), 5433 (PostgreSQL LPPP), 6380 (Redis LPPP), 3010 (Flowise LPPP), 5681 (n8n LPPP) — pas de conflit avec SquidResearch. Réf. `log-commun-lppp-squidresearch.md`.

### DevOps (Responsable — R du déploiement)
- [ ] **Prérequis** : clé SSH `~/.ssh/contabo_key` présente en local (ou dans secrets CI). Ne pas créer de fichier contenant la clé.
- [ ] **Orchestration** : depuis WSL, à la racine du projet : `make deploy-contabo` (ou `bash scripts/deploy-contabo.sh`). Le script fait : rsync du projet vers le serveur, puis SSH pour build + up + migrate.
- [ ] **Connexion** : `ssh -i ~/.ssh/contabo_key root@173.249.4.106`.
- [ ] **Sur le serveur** : créer `/var/www/lppp` (ou équivalent) si absent ; ne pas toucher à `/var/www/squidresearch`.
- [ ] **Clone** : cloner le dépôt LPPP (GitHub ou GitLab) dans `/var/www/lppp`. Ex. : `git clone git@github.com:LucasTymen/landingPageCreatorForProspection.git .` (depuis `/var/www/lppp`).
- [ ] **.env** : copier `.env.example` vers `.env`, renseigner les variables (SECRET_KEY, DB_PASSWORD, FLOWISE_*, etc.) — **sur le serveur uniquement**, jamais dans le dépôt.
- [ ] **Build & up** : `docker compose build` puis `docker compose up -d` (ou équivalent make).
- [ ] **Migrations** : `docker compose exec web python manage.py migrate`.
- [ ] **Superuser** : `docker compose exec web python manage.py createsuperuser` (première fois).
- [ ] **Santé** : vérifier que les services répondent (Django, admin, essais, Flowise, n8n).
- [ ] **Documenter** toute erreur et solution dans `erreurs-et-solutions.md`.

### Chef de Projet
- [ ] Valider le **plan de déploiement** (Architecte + DevOps alignés).
- [ ] Vérifier la **checklist pré-prod** : `regles-securite.md` § 9 — DEBUG=False, SECRET_KEY forte, ALLOWED_HOSTS, HTTPS si exposé.
- [ ] Après déploiement réussi : mettre à jour `log-projet.md`, ce sprint (statut 🟢), et `decisions.md` si besoin.

### Pentester
- [ ] Revue **vulnérabilités** (config Django, API, flux Flowise/n8n, exposition des services) — réf. `regles-securite.md`, `pentester.mdc`.
- [ ] Recommandations appliquées avant ou juste après mise en prod.

---

## Procédure déploiement (DevOps — résumé)

**Depuis la machine locale** (WSL / bash) :

```bash
# 1. Connexion SSH (clé déjà dans ~/.ssh/contabo_key)
ssh -i ~/.ssh/contabo_key root@173.249.4.106

# 2. Sur le serveur
mkdir -p /var/www/lppp
cd /var/www/lppp
git clone git@github.com:LucasTymen/landingPageCreatorForProspection.git .

# 3. .env (sur le serveur — ne jamais committer)
cp .env.example .env
# Éditer .env : SECRET_KEY, DB_PASSWORD, FLOWISE_URL, FLOWISE_CHATFLOW_ID, etc.

# 4. Build et lancement
docker compose build
docker compose up -d

# 5. Migrations
docker compose exec web python manage.py migrate

# 6. Superuser (première fois)
docker compose exec web python manage.py createsuperuser

# 7. Vérification
docker compose ps
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8010/
```

**Si la clé `~/.ssh/contabo_key` n'existe pas en local** : la recréer ou la récupérer depuis un coffre / backup, puis ajouter la clé publique dans `~/.ssh/authorized_keys` sur 173.249.4.106. Les agents ne peuvent pas fournir le contenu de la clé privée ni les mots de passe.

---

## Critères de succès

- [ ] **LPPP déployé** dans `/var/www/lppp` (ou équivalent) sans toucher à SquidResearch.
- [ ] **Stack LPPP** : db, redis, web, celery, celery-beat, n8n, flowise — tous Up.
- [ ] **Django** répond (port 8010 ou celui configuré).
- [ ] **Admin** accessible ; **essais** accessible ; **landing Maisons-Alfort** accessible.
- [ ] **Checklist pré-prod** respectée (DEBUG=False, ALLOWED_HOSTS, etc.).
- [ ] **Logs** et base de connaissances à jour.

---

## Références

- **Déploiement Contabo LPPP** : `deploiement-contabo-lppp-securite.md`
- **Infra** : `infra-devops.md` (§ 3.2 Contabo)
- **Log commun** : `log-commun-lppp-squidresearch.md`
- **Sécurité** : `regles-securite.md`, `pentester.mdc`
- **Source Contabo** : dépôt SquidResearch (documentation connexion, chemins, credentials)
