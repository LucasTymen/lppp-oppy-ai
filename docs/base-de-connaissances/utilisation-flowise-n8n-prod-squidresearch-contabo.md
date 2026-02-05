# Utilisation de Flowise et n8n hébergés sur la prod Squid Research (Contabo)

> **État actuel (2026-01-30)** : **option mise en pause.** On reste en **local** pour l’intégration du chatbot dans les landings. Ce document reste la référence si on souhaite repasser sur la prod plus tard.

**Objectif** : permettre à LPPP d’utiliser Flowise et n8n déjà déployés et opérationnels sur la production Squid Research (Contabo), **sans jamais remettre en cause l’intégrité** de cette prod.

**Références** : `log-commun-lppp-squidresearch.md`, `infra-devops.md`, décision « Priorité SquidResearch » dans `decisions.md`.

---

## 1. Principe : LPPP = client uniquement

- **Flowise et n8n sur Contabo** restent **sous la responsabilité de Squid Research** (config, credentials, chatflows, workflows, volumes).
- **LPPP** les **consomme** comme des services externes :
  - **Flowise** : URL d’embed du chatflow (ex. Conciergerie Maisons-Alfort) pour les landings (iframe, `flowise_client.get_flowise_chat_embed_url()`).
  - **n8n** : URLs de webhooks pour déclencher des workflows (scraper, enrichissement, etc.).
- Aucun déploiement LPPP **sur** Contabo qui pourrait écraser ou concurrencer les conteneurs/volumes Squid Research. Aucune modification de la config ou des credentials **sur** la prod Squid Research depuis LPPP.

---

## 2. Configuration côté LPPP

Renseigner dans le **`.env` de LPPP** (jamais committé) les URLs de la prod :

| Variable | Usage | Exemple (à adapter selon l’infra Squid Research) |
|----------|--------|---------------------------------------------------|
| **FLOWISE_URL** | Base Flowise (embed, API push si utilisé). | `https://flowise.<domaine-prod>` ou URL interne si LPPP et prod partagent le même réseau. |
| **FLOWISE_CHATFLOW_ID** | ID du chatflow à afficher en embed (ex. Conciergerie). | Même ID que celui déployé sur prod (récupéré dans Flowise → Embed). |
| **N8N_WEBHOOK_URL** | Base n8n pour les webhooks (workflows). | `https://n8n.<domaine-prod>/` ou chemin complet du webhook. |

- Les **valeurs réelles** (domaine, chemins) dépendent de l’infra Squid Research / Contabo. Les documenter si besoin dans le **log commun** (côté Squid Research) ou dans un fichier local non versionné.
- Si la prod exige une **API key** ou un **token** pour Flowise, utiliser `FLOWISE_API_KEY` dans `.env` (déjà prévu dans `flowise_client` pour le push de documents).

---

## 3. Règles pour ne jamais compromettre l’intégrité

| Règle | Description |
|-------|--------------|
| **Pas de déploiement LPPP sur Contabo** | Ne pas lancer le `docker-compose` LPPP sur le serveur Contabo de Squid Research, ni y déployer des conteneurs LPPP (Flowise/n8n LPPP) qui entreraient en conflit avec les services existants. |
| **Pas de modification de la prod depuis LPPP** | Les changements de chatflows, de workflows, de credentials ou de volumes Flowise/n8n sur prod sont faits **depuis l’équipe / l’infra Squid Research**, pas par des scripts ou commandes LPPP ciblant cette prod. |
| **LPPP ne fait qu’appeler des URLs** | LPPP se contente de construire l’URL d’embed (Flowise) et d’appeler les webhooks n8n. Aucune action « d’administration » sur les instances prod (reset, réinit, suppression de données). |
| **Conciergerie Maisons-Alfort** | La config Conciergerie (chatflow, FAISS, credentials) est **validée et stable** ; « plus de reset ». Si le chatflow tourne sur prod Squid Research, LPPP pointe simplement `FLOWISE_URL` + `FLOWISE_CHATFLOW_ID` vers cette instance. Voir `conciergerie-maisons-alfort-architecture-et-onboarding.md`. |
| **Secrets** | Les URLs prod et tokens éventuels restent dans le `.env` LPPP (ou variables d’environnement du déploiement LPPP), jamais dans le dépôt. |

---

## 4. Cas d’usage

- **Landings « élus » (ex. Conciergerie Maisons-Alfort)** : la page LPPP (`/p/maisons-alfort/`) affiche l’iframe du chat Flowise. Si Flowise est sur Contabo, `FLOWISE_URL` pointe vers l’URL publique (ou interne) de cette instance ; le navigateur charge l’embed depuis cette URL.
- **Workflows n8n (scraper, enrichissement)** : les workflows n8n sur Contabo exposent des webhooks ; LPPP ou des jobs externes appellent ces URLs. `N8N_WEBHOOK_URL` (ou URLs complètes par workflow) pointe vers la prod.

---

## 5. Qui fait quoi

| Rôle | Responsabilité |
|------|----------------|
| **DevOps** | Vérifier que les variables d’env (FLOWISE_URL, N8N_WEBHOOK_URL, etc.) sont cohérentes avec l’infra Squid Research / Contabo ; ne pas modifier la prod Squid Research depuis LPPP. Consulter le log commun avant toute décision sur ports/coexistence. |
| **Automatizer** | Workflows et chatflows restent maintenus **sur** l’instance concernée (locale LPPP ou prod Squid Research). Si prod utilisée : pas de push de config depuis LPPP vers prod sans accord ; sauvegardes des workflows dans le dépôt LPPP (voir `sauvegarde-workflows-flowise-n8n.md`) pour versioning, la prod étant gérée côté Squid Research. |
| **Chef de Projet** | Valider le choix « utiliser la prod Squid Research » et s’assurer que les règles d’intégrité sont respectées. |

---

## 6. Résumé

- **Oui**, LPPP peut utiliser Flowise et n8n hébergés sur la prod Squid Research (Contabo), en les traitant comme des **services externes** : renseigner `FLOWISE_URL`, `FLOWISE_CHATFLOW_ID`, `N8N_WEBHOOK_URL` (ou équivalent) dans le `.env` LPPP.
- **Intégrité préservée** : LPPP ne déploie rien sur Contabo, ne modifie pas les conteneurs ni la config prod ; il se contente d’appeler les URLs d’embed et de webhook.

*Document rédigé pour alignement équipe (2026-01-30).*
