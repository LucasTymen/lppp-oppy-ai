# Quick Win — Concierge IA Maisons-Alfort (n8n + Flowise)

**Date** : 2025-01-30  
**Statut** : 🟡 En cours  
**Objectif** : Réaliser la **maquette** du « Concierge IA » (agent de réponse administrative) pour la mairie de Maisons-Alfort avec n8n et Flowise, en moins de 2 h d’impact, pour une démo immédiate auprès d’un élu.

**Plan technique détaillé** : `docs/base-de-connaissances/concierge-ia-maisons-alfort-n8n-flowise.md` — à suivre pour l’exécution.

**Règle Git** : En clôture, commit + push sur les deux remotes (`make push-both` ou équivalent). Réf. `git-remotes-github-gitlab.md`.

---

## 📋 Contexte

- **Quick Win** : Le « Concierge IA » est le plus rapide à mettre en place et le plus parlant pour un élu (barre de recherche → réponse type agent municipal, 24h/24, basée uniquement sur le site de la ville).
- **Stack** : Aspiration des pages clés de maisons-alfort.fr → RAG (Flowise) → Chat avec system prompt « assistant officiel Maisons-Alfort » → Page démo personnalisée (logo, couleurs bleu/blanc).
- **Équipe** : Automatizer (n8n + Flowise), DevOps (infra, exposition démo), Dev Django (optionnel scraping), Pentester (sécurité flux), Chef de Projet (validation).

---

## 👥 Segmentation — intervenir directement sur la maquette

Les tâches ci-dessous sont à réaliser **directement** sur la maquette (workflow n8n, Chatflow Flowise, page démo). Chaque rôle s’appuie sur le plan technique (`concierge-ia-maisons-alfort-n8n-flowise.md`).

---

### 1. Automatizer (n8n + Flowise) — pilote maquette

**Responsabilité** : Workflow n8n d’aspiration + configuration RAG Flowise + intégration chat dans la démo.

- [ ] Créer dans n8n le workflow **« Concierge IA – Aspiration Maisons-Alfort »** :
  - Trigger (manuel ou schedule).
  - Nœuds HTTP Request vers 4–6 pages clés (Horaires, État Civil, Déchets, Travaux, etc. sur maisons-alfort.fr).
  - Extraction du texte (HTML Extract ou équivalent).
  - Sortie : textes prêts pour Flowise (fichier, API ou copier-coller selon option choisie).
- [ ] Dans Flowise : créer un **Chatflow** RAG avec :
  - Document Loader (texte/JSON selon sortie n8n).
  - Text Splitter + Vector Store + LLM.
  - System Prompt : *« Tu es l'assistant virtuel officiel de la ville de Maisons-Alfort. Tu réponds de manière courtoise, précise et uniquement en te basant sur les informations fournies. »*
- [ ] Ingérer les textes aspirés dans la base vectorielle Flowise (upload manuel pour la première démo si plus rapide).
- [ ] Récupérer l’URL du chat Flowise (embed ou API) pour la page démo.
- [ ] Documenter le workflow (export JSON dans `docs/n8n-workflows/` si le dossier existe, ou dans le plan technique) et les URLs cibles.

**Livrables** : Workflow n8n fonctionnel, Chatflow Flowise opérationnel, URL chat pour embed.

**Références** : `info-automatizer-pour-equipe.md`, `enrichissement-osint-flowise-n8n.md`, `concierge-ia-maisons-alfort-n8n-flowise.md`.

---

### 2. DevOps (infra, exposition démo)

**Responsabilité** : Services n8n et Flowise disponibles ; exposition de la démo si besoin.

- [ ] Vérifier que n8n (5678) et Flowise (3000) sont démarrés (`make up` ou `make services-urls`).
- [ ] Si démo en ligne demandée : exposer Flowise (reverse proxy, tunnel ngrok, ou URL Contabo) en HTTPS pour que l’iframe fonctionne.
- [ ] S’assurer que la page démo (statique ou Next.js) est servie et pointe vers la bonne URL Flowise.

**Livrables** : Accès n8n + Flowise confirmés ; URL démo si mise en ligne.

**Références** : `infra-devops.md`, `strategie-operationnelle-make.md`, `concierge-ia-maisons-alfort-n8n-flowise.md`.

---

### 3. Dev Django (optionnel — aspiration centralisée)

**Responsabilité** : Endpoint ou commande de scraping si on choisit de centraliser l’aspiration côté LPPP.

- [ ] (Optionnel) Créer une commande Django `scrape_maisons_alfort` ou un endpoint `GET /api/concierge/scrape-maisons-alfort` qui :
  - Utilise BeautifulSoup (déjà dans `requirements.txt`) pour extraire le texte des pages clés de maisons-alfort.fr.
  - Retourne un JSON `{ "pages": [ { "url": "...", "text": "..." } ] }`.
- [ ] Documenter l’endpoint dans `routes-back-lppp.md` si créé.
- [ ] n8n pourra alors appeler cet endpoint au lieu de faire les HTTP Request directement.

**Livrables** : Endpoint ou commande (si décidé) + ligne dans la doc routes.

**Références** : `concierge-ia-maisons-alfort-n8n-flowise.md` § Étape 1 Option B, `routes-back-lppp.md`.

---

### 4. Pentester (cyber, sécurité des flux)

**Responsabilité** : Vérification rapide que credentials et flux sont sûrs ; recommandation rate limit sur le chat public.

- [ ] Vérifier qu’aucun credential n’est exposé dans le workflow n8n (variables d’environnement, pas de clés en dur).
- [ ] S’assurer que l’API enrich et les webhooks LPPP ne sont pas impactés par ce nouveau flux (isolation).
- [ ] Recommander un rate limit ou une modération sur le chat Flowise si exposé publiquement (éviter abus).

**Livrables** : Avis sécurité + recommandations (ex. rate limit côté reverse proxy ou Flowise).

**Références** : `politique-credentials-securite-flux.md`, `regles-securite.md`, `concierge-ia-maisons-alfort-n8n-flowise.md`.

---

### 5. Chef de Projet (validation, pitch)

**Responsabilité** : Validation de la maquette et mise à jour des docs.

- [ ] Valider que la démo « 2 minutes » est prête (aspiration → RAG → chat → page personnalisée).
- [ ] Mettre à jour `docs/logs/log-projet.md` avec la livraison Quick Win Concierge IA.
- [ ] Mettre à jour `docs/TODO.md` ou `docs/boite-a-idees.md` si des évolutions sont identifiées (ex. mise à jour auto hebdo, déploiement démo sur Vercel).

**Livrables** : Checklist démo validée, logs et TODO à jour.

**Références** : `concierge-ia-maisons-alfort-n8n-flowise.md` § Checklist « Démo prête », pitch 30 s dans le plan technique.

---

## 📁 Fichiers créés / modifiés

| Fichier | Rôle |
|---------|------|
| `docs/base-de-connaissances/concierge-ia-maisons-alfort-n8n-flowise.md` | Plan technique (déjà créé) — référence pour tous |
| `docs/base-de-connaissances/segmentations/2025-01-30-quick-win-concierge-ia-maisons-alfort.md` | Cette segmentation |
| `docs/n8n-workflows/` (optionnel) | Export du workflow n8n « Concierge IA – Aspiration Maisons-Alfort » |
| `docs/base-de-connaissances/routes-back-lppp.md` | +1 endpoint si Dev Django crée `/api/concierge/scrape-maisons-alfort` |

---

## ✅ Checklist globale « Démo prête »

- [ ] Workflow n8n « Aspiration Maisons-Alfort » créé et testé.
- [ ] Chatflow Flowise configuré (RAG + system prompt Maisons-Alfort).
- [ ] Documents ingérés dans Flowise.
- [ ] Page démo avec iframe/widget + couleurs/logo Maisons-Alfort.
- [ ] Avis Pentester pris en compte.
- [ ] URL de démo accessible pour le pitch élu.

---

*Segmentation créée pour que l’équipe (Automatizer, DevOps, Dev Django, Pentester, Chef de Projet) intervienne directement sur la maquette du Concierge IA Maisons-Alfort. Plan technique : `concierge-ia-maisons-alfort-n8n-flowise.md`.*
