# Sprint — Résolution complète environnement réseau (accès Django / admin)

**Date** : 2026-01-30  
**Chef de Projet** : Pilote  
**Statut** : 🟡 En cours

**Contrainte prioritaire** : **SquidResearch est prioritaire.** On ne doit pas endommager sa stack. C’est à LPPP de s’adapter (ports, conteneurs, .env). Réf. `infra-devops.md` § 1, `log-commun-lppp-squidresearch.md`, `decisions.md` (Priorité SquidResearch).

---

## Contexte

- **Problème** : impossible d’accéder à l’admin Django et à Django en général (problème réseau, aucune différence entre admin et reste du site).
- **Objectif** : que l’architecte réseau, le DevOps et le pentester travaillent ensemble pour diagnostiquer et réparer l’environnement, sans toucher à la stack SquidResearch.

---

## Rôles mobilisés et tâches

### 1. Architecte réseau (diagnostic topologie et ports)

**Responsabilité** : Conflits de ports, topologie, recommandation d’adaptation LPPP.

- [ ] **Consulter le log commun** : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md` (pointeur vers le document canonique dans SquidResearch : `docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md`). Vérifier les ports LPPP vs SquidResearch (ex. 8000, 3000, 5432, 5678/5679).
- [ ] **Identifier les conflits** : si SquidResearch occupe le port 8000 (Django), LPPP ne peut pas exposer Django sur 8000 — documenter le port alternatif recommandé pour LPPP (ex. 8001) dans la procédure.
- [ ] **Vérifier la cohérence** : aucun changement côté SquidResearch ; toute adaptation se fait côté LPPP (docker-compose, `.env`, Makefile si besoin).
- [ ] **Livrable** : synthèse « Ports LPPP quand SquidResearch tourne » (ou « LPPP seul ») et mise à jour du pointeur / de la doc si le log commun change d’emplacement.

**Références** : `infra-devops.md` § 3.4, `log-commun-lppp-squidresearch.md`, `erreurs-et-solutions.md` (localhost:8000 inaccessible).

---

### 2. DevOps (diagnostic et réparation opérationnelle)

**Responsabilité** : État des conteneurs, commandes, options de contournement (Option B runserver, port alternatif).

- [ ] **Diagnostic conteneurs** : `docker ps` — vérifier que `lppp_web` est bien « Up ». Si absent ou « Restarting » : `docker compose logs web --tail 50` (erreur Django/Gunicorn ?).
- [ ] **Conflits de conteneurs** : ne supprimer **que** les conteneurs LPPP (`make clean-containers`), jamais ceux de SquidResearch. Puis `make start` (ou `make go` si démarrage à froid).
- [ ] **Test d’accès** : après démarrage, tester **http://127.0.0.1:8000** (et si besoin **http://127.0.0.1:8001** si LPPP est configuré sur 8001 pour éviter le conflit avec SquidResearch). Tester aussi **http://localhost:8000** (IPv6 vs IPv4 peut varier).
- [ ] **Option B (runserver local)** : si Docker web reste inaccessible (ERR_CONNECTION_RESET, Windows, etc.) : 1) `docker compose up -d db redis` et `docker compose stop web` pour libérer le port ; 2) Dans `.env` : `DB_HOST=localhost`, `REDIS_URL=redis://127.0.0.1:6379/0`, `CELERY_BROKER_URL=redis://127.0.0.1:6379/1` ; 3) Venv : `pip install -r requirements.txt`, `python3 manage.py migrate --noinput`, `python3 manage.py runserver 127.0.0.1:8080` (WSL : **python3**) ; 4) Accès **http://127.0.0.1:8080/admin/**.
- [ ] **Port alternatif LPPP (8001)** : si le log commun indique que 8000 est réservé à SquidResearch, configurer LPPP pour exposer le service web sur 8001 (override docker-compose ou fichier d’override documenté), sans modifier SquidResearch.
- [ ] **Livrable** : procédure exécutée et documentée ; mise à jour de `erreurs-et-solutions.md` et de la procédure « Avant migrations / relance » si besoin.

**Références** : `strategie-operationnelle-make.md`, `procedure-avant-migrations-relance.md`, `erreurs-et-solutions.md` (§ localhost:8000 inaccessible, Option B), `pret-a-demarrer.md`.

---

### 3. Pentester (sécurité et isolation)

**Responsabilité** : Vérifier que les correctifs réseau n’exposent pas davantage ni ne violent les règles de sécurité.

- [ ] **ALLOWED_HOSTS** : vérifier que `.env` / `lppp/settings.py` n’utilisent pas `*` ; garder une liste explicite (localhost, 127.0.0.1, web). Si un nouveau port ou host est utilisé (ex. 8001), s’assurer qu’il est couvert sans ouvrir excessivement.
- [ ] **Isolation des flux** : pas de propagation de credentials ; les APIs (admin, concierge, enriched) restent protégées (rate limiting, auth) selon `regles-securite.md` et `politique-credentials-securite-flux.md`.
- [ ] **Aucun impact sur SquidResearch** : ne pas recommander de modification de config, de ports ni de credentials côté SquidResearch.
- [ ] **Livrable** : validation que les changements LPPP (ports, runserver Option B) restent conformes à la politique sécurité ; alerte si une étape du diagnostic expose des données sensibles.

**Références** : `regles-securite.md`, `politique-credentials-securite-flux.md`, `pentester.mdc`.

---

## Ordre d’exécution recommandé

1. **Architecte réseau** : lecture du log commun (SquidResearch) + synthèse ports → livrable « quels ports pour LPPP ».
2. **DevOps** : en parallèle ou après — diagnostic Docker (`docker ps`, `logs web`), puis application de la procédure (clean-containers LPPP uniquement, start, test 127.0.0.1:8000 / 8001) ou Option B runserver.
3. **Pentester** : vérification ALLOWED_HOSTS et politique sécurité après toute modification proposée par DevOps / Architecte.

---

## Critères de succès

- [ ] Cause racine du blocage réseau identifiée (conflit port, conteneur down, Windows/localhost, etc.).
- [ ] Accès à Django (au moins une des options : Docker 8000/8001 ou runserver 8080) et à l’admin fonctionnel.
- [ ] Stack SquidResearch intacte (aucun conteneur ni config SquidResearch modifié).
- [ ] Décisions et procédures documentées dans `erreurs-et-solutions.md`, `decisions.md` et logs si besoin.

---

## Références

- Log commun : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md`
- Infra et ports : `docs/base-de-connaissances/infra-devops.md` § 1, § 3.4
- Erreurs et solutions : `docs/base-de-connaissances/erreurs-et-solutions.md` (§ localhost:8000 inaccessible, Option B)
- Priorité SquidResearch : `docs/base-de-connaissances/decisions.md`, `infra-devops.md` § 1
- Règles : `devops.mdc`, `pentester.mdc`, `orchestrateur.mdc`

---

*Sprint créé pour coordination Architecte réseau, DevOps, Pentester. Dernière mise à jour : 2026-01-30.*
