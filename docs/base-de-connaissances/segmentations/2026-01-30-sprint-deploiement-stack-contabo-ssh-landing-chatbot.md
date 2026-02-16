# Sprint — Déploiement stack complète Contabo (SSH, isolation, landing municipale + chatbot)

**Date** : 2026-01-30  
**Statut** : 🟡 En cours  
**Piloté par** : **Orchestrateur** — coordination des agents impactés et décisionnaires.

**Objectif** : Déployer la stack LPPP complète sur le serveur Contabo, activer les clés SSH, s’assurer que tout est en place et fonctionne, **sans aucun impact sur la stack SquidResearch déjà en place**. Raccorder la landing page municipale (Maisons-Alfort) et l’agent d’automatisation (chatbot) pour vérifier le bon fonctionnement.

---

## ⛔ Règle absolue — Comportement protecteur et non destructif

**Tous les agents concernés doivent agir de façon protectrice et non destructrice.**

| Principe | Application |
|----------|-------------|
| **Ne pas casser ce qui fonctionne** | Aucune modification des conteneurs, ports, volumes, .env ou répertoires de **SquidResearch**. En cas de doute : ne pas toucher, demander au Chef de Projet ou à l’Orchestrateur. |
| **Priorité SquidResearch** | SquidResearch a la priorité. LPPP s’adapte (ports dédiés, répertoire séparé). Réf. `log-commun-lppp-squidresearch.md`, `deploiement-contabo-lppp-securite.md`. |
| **Isolation stricte** | Stack LPPP = conteneurs `lppp_*` uniquement. Aucun partage de conteneurs, volumes ni `.env` avec SquidResearch. |
| **Validation avant action destructive** | Aucun `docker compose down -v`, suppression de volume ou modification des credentials SquidResearch sans accord explicite et sauvegarde. |

**Consulter systématiquement** avant toute action infra : `log-commun-lppp-squidresearch.md` (pointeur vers le log canonique SquidResearch), `deploiement-contabo-lppp-securite.md`, `avis-et-solutions-routage-lppp-reference.md`.

---

## Contexte

- **Serveur** : Contabo (IP documentée dans SquidResearch). LPPP déployé dans `/var/www/lppp`, SquidResearch dans `/var/www/squidresearch` — **ne pas modifier SquidResearch**.
- **Clés SSH** : À activer/vérifier sur le serveur ; clé locale `~/.ssh/contabo_key` (hors dépôt). Aucun secret dans le dépôt LPPP.
- **Landing municipale** : `/p/maisons-alfort/` — template proposition + iframe/embed chatbot Conciergerie.
- **Chatbot** : Flowise (port 3010 LPPP), chatflow Conciergerie Maisons-Alfort ; n8n si applicable. Raccordement à la landing pour vérifier l’end-to-end.

---

## Rôles et responsabilités (Orchestrateur pilote)

| Rôle | Responsabilité | Comportement attendu |
|------|----------------|----------------------|
| **Orchestrateur** | Coordonner les agents, mettre à jour le registre, s’assurer que les décisions sont protectrices. Briefing des agents impactés et décisionnaires. | Ne pas imposer d’action qui touche à SquidResearch. Valider les plans avec Chef de Projet avant exécution. |
| **DevOps** | Déploiement, SSH, Docker LPPP, .env LPPP, santé des services. | Uniquement conteneurs/ports LPPP. Vérifier les ports avant tout `up`. Ne jamais arrêter/modifier les conteneurs SquidResearch. |
| **Architecte** | Schéma d’isolation, routage, vérification des chevauchements. | Documenter que LPPP et SquidResearch sont bien séparés ; alerter si un changement risquerait un conflit. |
| **Chef de Projet** | Validation du plan, checklist, mise à jour des logs et de la base de connaissances. | Refuser toute tâche qui impacterait SquidResearch. Clôturer le sprint avec logs à jour. |
| **Pentester** | Revue sécurité (vulnérabilités, durcissement) sur LPPP uniquement. | Tests non destructifs ; pas de modification de prod sans accord. |
| **Automatizer** | Flowise, n8n — configuration chatbot, embed, santé des flux. | Vérifier que les flux (landing → Flowise) fonctionnent sans toucher aux instances SquidResearch. |

---

## Tâches par agent (ordonnancées par l’Orchestrateur)

### Orchestrateur
- [ ] Mettre à jour le **registre** (`registre-agents-ressources.md`) : référencer ce sprint et les docs déploiement / log commun.
- [ ] **Briefing** : s’assurer que DevOps, Architecte, Chef de Projet ont bien la règle « protecteur, non destructif » et la priorité SquidResearch.
- [ ] Coordonner l’ordre des actions : SSH → isolation vérifiée → déploiement LPPP → raccordement landing + chatbot → vérifications.
- [ ] En cas de conflit ou de doute sur une action : escalade au Chef de Projet, pas d’action destructive.

### Architecte
- [ ] **Vérifier l’absence de chevauchement** : confirmer que les ports LPPP (8010, 5433, 6380, 3010, 5681) et le répertoire `/var/www/lppp` ne recoupent pas SquidResearch (8000, 5432, 6379, 5679, 3000/3001, `/var/www/squidresearch`). Documenter dans ce sprint ou dans `deploiement-contabo-lppp-securite.md`.
- [ ] **Règles de routage** : si reverse proxy (Nginx) est utilisé, valider que les blocs LPPP pointent uniquement vers les ports LPPP et ne modifient pas les blocs SquidResearch.

### DevOps (exécution déploiement)
- [ ] **Clés SSH** : vérifier que la clé `~/.ssh/contabo_key` est en place en local ; que l’accès SSH au serveur fonctionne (`ssh -i ~/.ssh/contabo_key root@<IP>`). Sur le serveur : s’assurer que les clés/authorized_keys sont correctes pour les accès requis. **Ne pas écraser** les clés existantes utilisées par SquidResearch.
- [ ] **Déploiement LPPP** : exécuter depuis la racine LPPP `make deploy-contabo` (ou `bash scripts/deploy-contabo.sh`). Le script fait rsync vers `/var/www/lppp` et lance build/up/migrate **dans ce répertoire uniquement**.
- [ ] **Vérification Docker** : avant `docker compose up`, confirmer que le `docker-compose.yml` utilisé est celui de LPPP (conteneurs `lppp_*`). Après `up`, vérifier avec `docker ps` qu’aucun conteneur SquidResearch n’a été arrêté ou modifié.
- [ ] **.env** : sur le serveur, dans `/var/www/lppp` uniquement, créer/éditer `.env` depuis `.env.example`. Ne jamais toucher au `.env` de SquidResearch.
- [ ] **Santé** : Django (8010), Flowise (3010), n8n (5681) répondent ; migrations appliquées ; superuser créé si première fois.

### Automatizer (Flowise / n8n — chatbot)
- [ ] **Raccordement landing + chatbot** : vérifier que la landing municipale (`/p/maisons-alfort/`) reçoit bien l’URL d’embed Flowise et que le chatbot s’affiche (ou documenter la cause si vide). Réf. `flowise-chatbot-ecran-vide-diagnostic.md`, `flowise-concierge-ia-maisons-alfort-guide.md`.
- [ ] **Variables** : `FLOWISE_URL`, `FLOWISE_CHATFLOW_ID` dans le `.env` LPPP (serveur) ; pas d’exposition de secrets côté client.
- [ ] **Test de bout en bout** : page landing accessible → zone chat visible et répondant. Documenter le résultat dans ce sprint ou dans la base de connaissances.

### Chef de Projet
- [ ] Valider le **plan de déploiement** (Architecte + DevOps alignés, pas d’impact SquidResearch).
- [ ] **Checklist pré-prod** : `regles-securite.md` § 9 (DEBUG=False, SECRET_KEY, ALLOWED_HOSTS, etc.) appliquée à LPPP uniquement.
- [ ] Après déploiement réussi : mise à jour de `log-projet.md`, statut de ce sprint, et `decisions.md` si une décision est prise.

### Pentester
- [ ] Revue **sécurité LPPP** (config Django, API, flux Flowise/n8n) — réf. `regles-securite.md`, `pentester.mdc`. **Tests non destructifs** ; pas de modification de la prod SquidResearch.

---

## Ordre d’exécution recommandé

1. **Orchestrateur** : briefing + mise à jour registre ; rappel règle protectrice.
2. **Architecte** : validation schéma d’isolation (ports, répertoires) — **bloquant** pour le déploiement.
3. **DevOps** : vérification SSH → déploiement LPPP (script) → santé des services.
4. **Automatizer** : raccordement landing municipale + chatbot ; test end-to-end.
5. **Chef de Projet** : validation finale, mise à jour des logs.
6. **Pentester** : revue sécurité (en parallèle ou après mise en place).

---

## Critères de succès

- [ ] **Clés SSH** : accès serveur opérationnel sans impact sur les accès existants (ex. SquidResearch).
- [ ] **Stack LPPP** déployée dans `/var/www/lppp` ; tous les services LPPP (web, db, redis, flowise, n8n, etc.) sont Up.
- [ ] **Aucun impact sur SquidResearch** : conteneurs, ports et répertoires SquidResearch inchangés et fonctionnels.
- [ ] **Landing municipale** (`/p/maisons-alfort/`) accessible et **chatbot** raccordé (embed visible et fonctionnel ou cause documentée).
- [ ] **Documentation** : logs et base de connaissances à jour ; erreurs éventuelles consignées dans `erreurs-et-solutions.md`.

---

## Références

- **Log commun LPPP ↔ SquidResearch** : `log-commun-lppp-squidresearch.md`
- **Déploiement Contabo LPPP** : `deploiement-contabo-lppp-securite.md`
- **Sprint déploiement Contabo (précédent)** : `2026-02-07-sprint-deploiement-contabo-lppp.md`
- **Chatbot / landing Maisons-Alfort** : `flowise-concierge-ia-maisons-alfort-guide.md`, `flowise-chatbot-ecran-vide-diagnostic.md`, `2026-02-06-sprint-controle-flux-chatbot-landing-maisons-alfort.md`
- **Script déploiement** : `scripts/deploy-contabo.sh` ; cible Makefile : `make deploy-contabo`
- **Avis et solutions routage** : `avis-et-solutions-routage-lppp-reference.md`

---

*Document piloté par l’Orchestrateur. Tous les agents concernés agissent de façon protectrice et non destructrice. Dernière mise à jour : 2026-01-30.*
