# Concierge IA Maisons-Alfort — Plan technique n8n + Flowise (Quick Win)

**Objectif** : Mettre en place rapidement un **« Concierge IA »** (agent de réponse administrative) pour la mairie de Maisons-Alfort : une barre de recherche où le citoyen pose une question complexe, l’IA répond en s’appuyant **uniquement** sur les données du site maisons-alfort.fr (RAG). Démo en **moins de 2 h** pour un impact visuel immédiat auprès d’un élu.

**Pilotes** : **Automatizer** (n8n + Flowise), **DevOps** (infra, exposition démo), **Dev Django** (optionnel : endpoint scraping), **Pentester** (sécurité flux / rate limit).  
**Référence équipe** : `info-automatizer-pour-equipe.md`, `enrichissement-osint-flowise-n8n.md`, `infra-devops.md`.

---

## 1. Pourquoi ce Quick Win

| Critère | Réponse |
|--------|---------|
| **Vitesse** | Pas de scraper complexe : on nourrit une IA (RAG) avec les textes des pages clés du site. |
| **Impact visuel** | Très parlant pour un élu : question → réponse précise type « agent municipal ». |
| **Maintenance** | Une fois le pipeline en place, il peut se mettre à jour en relançant l’aspiration (n8n schedule ou manuel). |

**Pitch 30 s** (pour la prospection) : *« Le site de la ville contient une mine d’infos, mais il est parfois complexe de trouver une réponse rapide (ex. documents pour passeport, horaires encombrants). J’ai développé un prototype d’assistant intelligent qui répond 24h/24 en se basant exclusivement sur vos sources officielles — moins d’appels répétitifs à l’accueil, meilleur service aux Alfortais. Je vous ai préparé une démo personnalisée de 2 minutes. »*

---

## 2. Architecture cible (n8n + Flowise)

```
[Trigger n8n: manuel ou schedule]
        ↓
[Étape 1 — Aspiration] n8n : HTTP Request vers pages clés maisons-alfort.fr
   OU  n8n appelle un endpoint Django (si on crée /api/concierge/scrape-maisons-alfort)
        ↓
[Étape 2 — Texte] Extraction du texte (n8n "HTML Extract" / "Set" ou script Python)
        ↓
[Étape 3 — RAG] Envoi des textes vers Flowise :
   - Soit : Flowise « Document Loader » + base vectorielle déjà configurée, n8n envoie les chunks/textes via API Flowise
   - Soit : Fichiers déposés dans un volume partagé que Flowise ingère (schedule ou manuel)
        ↓
[Étape 4 — Chat] Flowise Chatflow avec System Prompt :
   "Tu es l'assistant virtuel officiel de la ville de Maisons-Alfort. Tu réponds de manière courtoise, précise et uniquement en te basant sur les informations fournies."
        ↓
[Étape 5 — Démo] Interface : iframe ou widget Flowise (URL du chatflow) + personnalisation (logo, couleurs bleu/blanc Maisons-Alfort)
```

- **n8n** (port 5678) : orchestration aspiration + optionnel envoi des données vers Flowise.
- **Flowise** (port 3000) : RAG (documents + vecteurs + LLM) + chat API / embed.
- **Démo** : une page HTML statique ou une route Next.js qui embarque le chat Flowise et applique les couleurs/logo.

---

## 3. Plan d’action par étape (maquette exécutable)

### Étape 1 — Aspiration des données (≈ 15 min)

**Option A (recommandée pour aller vite)** : dans n8n, workflow avec :
- **Trigger** : Manuel (bouton « Test workflow ») ou Schedule (ex. 1×/semaine).
- **Nœuds HTTP Request** : une requête par URL cible (ex. 4–6 pages : Horaires, État Civil, Déchets, Travaux, Accueil, Contact). URLs de base : `https://www.maisons-alfort.fr/...` (à lister après vérification du sitemap ou de la structure du site).
- **Nœud HTML Extract** (ou « Extract from HTML ») : extraire le corps de texte de chaque page (sélecteur type `body` ou `.content` selon le site). Sortie : un champ `text` ou `content` par page.

**Option B** : Dev Django ajoute une commande ou un endpoint (ex. `GET /api/concierge/scrape-maisons-alfort`) qui utilise BeautifulSoup (déjà dans `requirements.txt`) pour scraper les mêmes pages et retourne un JSON `{ "pages": [ { "url": "...", "text": "..." } ] }`. n8n appelle cet endpoint (HTTP Request) puis traite le JSON. Utile si le site est anti-bot ou si on veut centraliser la logique.

**Responsable** : **Automatizer** (n8n Option A), **Dev Django** (Option B si décidé).

---

### Étape 2 — Configuration de l’IA / RAG (≈ 30 min)

**Dans Flowise** (interface sur port 3000) :
1. Créer un **Chatflow** (ou « Flow » selon la version) avec :
   - **Document Loader** : type « Text » ou « PDF » selon ce qu’on envoie (si n8n envoie du texte brut, utiliser un loader « Text » ou « JSON » si Flowise le propose).
   - **Text Splitter** : découper les textes en chunks (ex. 500–1000 caractères, overlap 100).
   - **Vector Store** : (ex. in-memory pour la démo, ou Redis/Pinecone si déjà en place).
   - **LLM** : modèle disponible (OpenAI, Ollama, etc. selon config Flowise).
2. **System Prompt** : *« Tu es l'assistant virtuel officiel de la ville de Maisons-Alfort. Tu réponds de manière courtoise, précise et uniquement en te basant sur les informations fournies. »*
3. Récupérer l’**URL du chat** (embed ou API) fournie par Flowise pour l’intégrer à la page démo.

**Alimentation des documents** :
- **Option 1** : Dans Flowise, upload manuel des textes (copier-coller depuis n8n ou export JSON) pour la première démo.
- **Option 2** : n8n envoie les textes à l’API Flowise (si disponible) pour ingérer dans la base vectorielle. Vérifier la doc Flowise (endpoints d’ingestion de documents).
- **Option 3** : n8n écrit les textes dans un fichier (volume partagé) et Flowise lit ce fichier (schedule ou manuel).

**Responsable** : **Automatizer** (config Flowise + choix option ingestion).

---

### Étape 3 — Personnalisation démo (≈ 15 min)

- **Page démo** : une seule page (HTML statique ou Next.js) contenant :
  - Titre type « Assistant Ville de Maisons-Alfort »
  - iframe ou widget du chat Flowise (URL du chatflow).
  - Couleurs bleu/blanc et logo Maisons-Alfort (assets fournis ou liens vers le site officiel).
- **Hébergement** : même serveur que Flowise (ex. Contabo) ou page statique sur Vercel avec iframe pointant vers l’URL Flowise (nécessite que Flowise soit exposée en HTTPS pour la démo, ou tunnel ngrok en dev).

**Responsable** : **Designer** (maquette couleurs/logo) ou **Automatizer** (intégration iframe + CSS). **DevOps** : exposition de Flowise (URL publique ou tunnel) si démo en ligne.

---

## 4. Rôles et tâches (qui fait quoi)

| Rôle | Tâches concrètes | Livrable |
|------|-------------------|----------|
| **Automatizer** | Créer le workflow n8n « Concierge IA – Aspiration Maisons-Alfort » (trigger + HTTP Request × N pages + extraction texte). Configurer le Chatflow Flowise (RAG + system prompt). Documenter les URLs cibles et le flux dans ce doc ou dans `docs/n8n-workflows/`. | Workflow n8n importable + Chatflow Flowise opérationnel + doc courte |
| **DevOps** | S’assurer que n8n (5678) et Flowise (3000) sont démarrés (`make up` ou `make services-urls`). Si démo en ligne : exposer Flowise (reverse proxy, tunnel ou URL) et éventuellement la page démo. | Services accessibles + URL démo si demandé |
| **Dev Django** | (Optionnel) Commande ou endpoint `/api/concierge/scrape-maisons-alfort` qui retourne les textes scrapés (BeautifulSoup). À appeler depuis n8n si on choisit Option B. | Endpoint ou commande + 1 ligne dans `routes-back-lppp.md` |
| **Pentester** | Vérifier qu’aucun credential n’est exposé dans le workflow n8n ; rate limit ou modération sur le chat public si exposé (éviter abus). | Avis sécurité + recommandations (ex. rate limit côté Flowise ou reverse proxy) |
| **Chef de Projet** | Valider la maquette (démo 2 min), mettre à jour la segmentation et le log projet. | Checklist validée + mise à jour docs |

---

## 5. URLs et références techniques

- **n8n** : `http://localhost:5678` (local) ; voir `strategie-operationnelle-make.md` (`make n8n-logs`, `make flowise-logs`).
- **Flowise** : `http://localhost:3000` ; doc officielle Flowise pour RAG et Chatflow.
- **Site cible** : `https://www.maisons-alfort.fr/` — lister les pages à aspirer (sitemap ou navigation : Horaires, État Civil, Déchets, Travaux, etc.).
- **LPPP** : `enrichissement-osint-flowise-n8n.md` (guide-rails API, rate limit) ; `info-automatizer-pour-equipe.md` (collaboration Automatizer).

---

## 6. Checklist « Démo prête »

- [ ] Workflow n8n « Aspiration Maisons-Alfort » créé et testé (au moins 4 pages).
- [ ] Chatflow Flowise configuré (RAG + system prompt Maisons-Alfort).
- [ ] Documents (textes des pages) ingérés dans Flowise.
- [ ] Page démo avec iframe/widget + couleurs/logo Maisons-Alfort.
- [ ] Avis Pentester (credentials, rate limit) pris en compte.
- [ ] URL de démo accessible (local ou exposée) pour le pitch élu.

---

*Document créé pour que l’équipe (Automatizer, DevOps, Dev Django, Pentester) intervienne directement sur la maquette du Concierge IA Maisons-Alfort. À utiliser avec la segmentation `segmentations/2025-01-30-quick-win-concierge-ia-maisons-alfort.md`. Dernière mise à jour : 2025-01-30.*
