# Étude d’impact et de risques — Routage des conteneurs LPPP

**Date** : 2026-02-05  
**Contexte** : Sprint urgent de revue des routages des conteneurs, en cohérence avec le **log commun** et la **recommandation de l’équipe SquidResearch**.  
**Pointeur log commun** : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md`. Document canonique (recommandation détaillée) : dans le dépôt SquidResearch, `docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md`.

---

## 1. État actuel des routages LPPP (synthèse)

D’après `docker-compose.yml`, `infra-devops.md` et `erreurs-et-solutions.md` :

| Service    | Conteneur   | Port hôte → conteneur | Remarque                          |
|-----------|-------------|------------------------|-----------------------------------|
| PostgreSQL| lppp_db     | 5433:5432              | Port LPPP dédié (SquidResearch 5432). Stack autonome § 5.3 log commun. |
| Redis     | lppp_redis  | 6380:6379              | Port LPPP dédié (SquidResearch 6379). |
| Django    | lppp_web    | 8010:8000              | Port LPPP dédié (SquidResearch 8000). |
| n8n       | lppp_n8n    | 5681:5678              | Port LPPP dédié (SquidResearch 5679). |
| Flowise   | lppp_flowise| 3010:3000              | Port LPPP dédié (SquidResearch 3000/3001). |
| Celery    | lppp_celery | —                      | Pas d’exposition de port.         |
| Celery beat | lppp_celery_beat | —                | Idem.                            |

**Résolution interne Docker** : les services communiquent par noms (db, redis, web, flowise, n8n). Le **navigateur** (hôte) doit joindre des adresses **localhost** ou **127.0.0.1** avec les ports **exposés** (8000, 3000, 5678, etc.).

**Règle de priorité** : SquidResearch a la priorité ; en cas de conflit, **c’est LPPP qui change** (ports alternatifs, ex. Django 8001, Flowise 3002 — à valider avec le log commun).

---

## 2. Source de la recommandation SquidResearch

La **recommandation précise** (routage, ports recommandés pour LPPP, coexistence, hermeticité) figure dans le **document canonique** maintenu par l’équipe SquidResearch :

- **WSL** : `/home/lucas/tools/squidResearch/docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md`
- **Windows** : `\\wsl.localhost\Ubuntu-22.04\home\lucas\tools\squidResearch\docs\infrastructure\LOG_COMMUN_LPPP_SQUIDRESEARCH.md`

Cette étude ne remplace pas la lecture de ce document. Elle en complète la mise en œuvre côté LPPP (impact, risques, points d’attention).

---

## 3. Impact pour LPPP d’un changement de routage

Tout changement de **ports exposés** ou de **routage** implique :

| Zone d’impact | Fichiers / éléments concernés | Action typique |
|--------------|-------------------------------|----------------|
| **Docker**   | `docker-compose.yml`, éventuel `docker-compose.override.yml` ou `docker-compose.windows.yml` | Modifier le mapping `ports:` (ex. 8001:8000 pour web). |
| **Makefile** | `services-urls`, `health-check`, aide `make help` | Mettre à jour les URLs affichées (port Django, Flowise, n8n). |
| **Documentation** | `infra-devops.md` § 3.4, `pret-a-demarrer.md`, `strategie-operationnelle-make.md`, `flowise-concierge-ia-maisons-alfort-guide.md` | Remplacer les anciens ports par les nouveaux partout. |
| **.env / .env.example** | Variables `FLOWISE_URL`, `N8N_WEBHOOK_URL` (si ports changent) | Ex. `FLOWISE_URL=http://localhost:3002` si Flowise passe sur 3002. |
| **Django**   | `lppp/settings.py` (ALLOWED_HOSTS), `apps/scraping/flowise_client.py` (URL d’embed) | ALLOWED_HOSTS : ajouter tout nouveau host/port si besoin ; flowise_client utilise FLOWISE_URL. |
| **Procédures** | `erreurs-et-solutions.md`, sprints (résolution réseau, chatbot, lancement) | Mettre à jour les exemples d’URL (127.0.0.1:8001, localhost:3002, etc.). |
| **Option B (runserver)** | `pret-a-demarrer.md`, Option B | Si Django en Docker passe sur 8001, garder 8080 pour runserver ; pas de conflit. |

**Effort estimé** : 1 à 2 h (modifs + relecture doc + tests) si les changements restent limités aux ports exposés et à la doc. Plus si refonte des noms de services ou du réseau Docker interne.

---

## 4. Étude de risques (matrice simplifiée)

| Risque | Gravité | Probabilité | Mitigation |
|--------|---------|-------------|------------|
| **Conflit de ports** (LPPP et SquidResearch sur 8000, 3000, 5432) | Élevée | Élevée si les deux stacks tournent | Suivre la recommandation SquidResearch ; attribuer à LPPP des ports distincts (ex. 8001, 3002) et documenter. |
| **Régression accès** (Django, admin, n8n, Flowise inaccessibles après changement) | Élevée | Moyenne | Tests systématiques après modification (`make start`, curl sur chaque service) ; Option B runserver documentée en secours. |
| **Doc obsolète** (anciens ports encore indiqués dans guides ou erreurs-et-solutions) | Moyenne | Élevée | Checklist de mise à jour (infra-devops, pret-a-demarrer, strategie-operationnelle-make, flowise-concierge, erreurs-et-solutions, sprints). |
| **ALLOWED_HOSTS trop permissif** (ou oubli d’un nouveau host/port) | Moyenne | Faible | Pentester valide ; garder liste explicite (localhost, 127.0.0.1, web, éventuellement nouveau port). |
| **URLs d’embed / webhooks** (Flowise, n8n) incorrectes après changement de port | Élevée | Moyenne | Vérifier FLOWISE_URL, N8N_WEBHOOK_URL, et flowise_client.py ; tester la page /maisons-alfort/ et les workflows n8n. |
| **Modification involontaire de SquidResearch** | Critique | À éviter (règle stricte) | Ne toucher qu’aux fichiers et conteneurs **LPPP** ; pas d’édition du docker-compose ou .env SquidResearch. |

---

## 5. Points d’attention (avis)

- **Conflits 8000 et 3000** : Ce sont les plus probables (Django et Flowise souvent sur les mêmes ports que SquidResearch). La recommandation SquidResearch doit trancher : soit « LPPP seul sur 8000/3000 », soit « LPPP sur 8001/3002 (ou autres) quand SquidResearch tourne ». Documenter clairement les deux scénarios (LPPP seul vs coexistence).
- **Port 5432 (PostgreSQL)** : Si les deux stacks exposent 5432, un seul pourra écouter sur l’hôte. Souvent on n’expose pas la DB SquidResearch sur l’hôte, ou on utilise des ports différents (ex. LPPP 5432, SquidResearch 5433). À confirmer dans le log commun.
- **Port 5678 (n8n)** : LPPP 5678, SquidResearch 5679 d’après le résumé du pointeur → pas de conflit. Vérifier dans le canonique que rien ne change.
- **Flowise et données** : Changer le port de Flowise (ex. 3002) n’efface pas les volumes ; en revanche, **quel conteneur** (lppp_flowise vs SquidResearch) utilise le port 3000 doit rester clair pour éviter de se connecter au mauvais Flowise (voir erreurs-et-solutions § « No Chatflows Yet »).
- **Option B (runserver)** : Elle reste valide (db + redis + éventuellement flowise en Docker, Django en local sur 8080). Les procédures Option B ne doivent pas supposer que Django Docker est sur 8000 si on bascule LPPP sur 8001.
- **Cohérence globale** : Une fois les ports LPPP fixés, une **seule** source de vérité (idéalement infra-devops.md § 3.4 + log commun) et une relecture de toute la doc qui cite des URLs (guides, erreurs-et-solutions, sprints) limitent les incohérences et la confusion.

---

## 6. Synthèse et prochaines étapes

- **Recommandation** : Elle doit être **lue dans le document canonique SquidResearch** (chemin § 2). Cette étude en prépare l’application côté LPPP (impact, risques, points d’attention).
- **Sprint** : Le sprint urgent `segmentations/2026-02-05-sprint-urgent-routage-conteneurs.md` mobilise toute l’équipe : Architecte et DevOps lisent le log commun, appliquent la recommandation, mettent à jour la doc et les procédures.
- **Validation** : Chef de Projet valide le plan et les critères de succès ; Pentester valide la sécurité ; DevOps et Dev Django vérifient les URLs et ALLOWED_HOSTS.

*Document rédigé pour le sprint urgent routage conteneurs. Dernière mise à jour : 2026-02-05.*
