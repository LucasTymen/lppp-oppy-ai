# Guide équipe — Scraper → n8n → Flowise (Concierge IA Maisons-Alfort)

**Objectif** : faire fonctionner la chaîne complète : scraper Django → n8n → enregistrement du contenu → push vers Flowise → RAG opérationnel.

**Public** : Automatizer, DevOps, Dev Django, toute personne qui configure ou débugge le Concierge IA.

---

## 1. Vue d’ensemble

```
[Déclencher n8n] → [GET /api/concierge/scrape] → [POST save-content] → [POST push-to-flowise] → [Flowise Document Store]
                         (Django web)                  (écrit .txt)           (API Flowise)              (RAG prêt)
```

- **Scraper** : Django extrait le texte des pages maisons-alfort.fr (accueil, état civil, déchets, horaires, travaux).
- **n8n** : workflow en 4 nœuds (déclencher → scrape → save-content → push-to-flowise).
- **Flowise** : Document Store reçoit le fichier, ingestion → vecteurs → chat RAG.

---

## 2. Prérequis

| Élément | Où / Comment |
|--------|----------------|
| Stack LPPP démarré | `make start` ou `make up` (db, redis, web, celery, n8n, flowise) |
| Django OK | `make check` ou `curl -s http://localhost:8000/` → 200 |
| n8n | http://localhost:5678 |
| Flowise | http://localhost:3000 |
| Document Store Flowise | Créé dans Flowise, nom ex. « Maisons-Alfort » (voir `workflow-complet-concierge-maisons-alfort.md`) |
| `.env` | `FLOWISE_URL`, `FLOWISE_DOCUMENT_STORE_ID` (et optionnel `FLOWISE_API_KEY`) pour la commande et l’API push |

---

## 3. Scraper (Django)

### 3.1 Endpoints disponibles

| Méthode | URL | Description |
|---------|-----|-------------|
| GET | `/api/concierge/scrape` | Scrape les URLs par défaut (Maisons-Alfort). Retourne `{ "status": "ok", "pages": [ { "url", "text", "error" } ] }`. |
| POST | `/api/concierge/scrape` | Body `{ "urls": ["https://...", ...] }` (max 20). Même format de réponse. |
| POST | `/api/concierge/save-content` | Body `{ "pages": [...] }` ou `{ "content": "texte brut" }`. Écrit dans `data/flowise/maisons-alfort-contenu.txt` (ou `?filename=autre.txt`). |
| POST | `/api/concierge/push-to-flowise` | Pousse le fichier `data/flowise/maisons-alfort-contenu.txt` (ou `?filename=autre.txt`) vers le Document Store Flowise. |

### 3.2 Tester le scraper à la main

Depuis la machine hôte (Django dans Docker) :

```bash
# Scrape (GET)
curl -s http://localhost:8000/api/concierge/scrape | head -c 500

# Save (il faut d’abord avoir des pages : faire le GET au-dessus et mettre le JSON en body)
# Exemple avec un contenu minimal :
curl -s -X POST http://localhost:8000/api/concierge/save-content \
  -H "Content-Type: application/json" \
  -d '{"content":"Test Maisons-Alfort.\nHoraires : 9h-12h."}'

# Push vers Flowise (après save)
curl -s -X POST http://localhost:8000/api/concierge/push-to-flowise
```

Depuis un autre conteneur du même Docker Compose (ex. n8n), remplacer `localhost` par le **nom du service** : `http://web:8000`.

### 3.3 Commande Django (hors n8n)

Pour alimenter Flowise sans n8n :

```bash
# 1) Scraper et écrire le fichier (en une fois, depuis le host)
docker compose exec web python manage.py scrape_maisons_alfort --output /app/data/flowise/maisons-alfort-contenu.txt
# (si la commande supporte --output ; sinon rediriger la sortie vers data/flowise/maisons-alfort-contenu.txt côté host)

# 2) Pousser vers Flowise
docker compose exec web python manage.py flowise_push_documents --file data/flowise/maisons-alfort-contenu.txt
```

Si `scrape_maisons_alfort` n’écrit pas directement dans `data/flowise/`, écrire le JSON puis un script qui fusionne les `pages[].text` dans un seul `.txt`, ou utiliser les appels API ci-dessus (GET scrape puis POST save-content avec le body renvoyé).

---

## 4. n8n — Faire fonctionner le workflow

### 4.1 Importer le workflow

1. Ouvrir n8n : http://localhost:5678  
2. Menu **Workflows** → **Import from File** (ou glisser-déposer).  
3. Choisir le fichier :  
   `docs/n8n-workflows/concierge-ia-aspiration-maisons-alfort.json`

### 4.2 URLs selon l’environnement

Le workflow utilise par défaut **`http://web:8000`** (conteneurs Docker sur le même réseau).

- **Si n8n tourne dans le même Docker Compose que Django** : garder `http://web:8000` pour les 3 nœuds HTTP (scrape, save-content, push-to-flowise).
- **Si n8n tourne en local (hors Docker)** et Django dans Docker : remplacer par `http://localhost:8000` dans chaque nœud HTTP.

### 4.3 Enchaînement des nœuds

1. **Déclencher** — Déclenchement manuel (ou remplacer par cron/webhook plus tard).  
2. **Scrape Maisons-Alfort (Django)** — GET `http://web:8000/api/concierge/scrape`. Sortie : 1 item avec `status`, `pages`.  
3. **Préparer body save-content** — Code : prend `$input.first().json`, retourne `[{ json: { pages: body.pages } }]` pour le nœud suivant.  
4. **Save content (Django)** — POST `http://web:8000/api/concierge/save-content` avec body JSON `{ "pages": [...] }`. Écrit `data/flowise/maisons-alfort-contenu.txt` sur le serveur.  
5. **Push to Flowise (Django)** — POST `http://web:8000/api/concierge/push-to-flowise`. Appelle l’API Flowise (Document Store upsert) avec ce fichier.

### 4.4 Erreurs fréquentes n8n

| Symptôme | Cause probable | Action |
|----------|----------------|--------|
| « connect ECONNREFUSED » sur web:8000 | n8n hors Docker ou mauvais réseau | Utiliser `http://localhost:8000` si n8n est sur le host ; sinon vérifier que `web` et `n8n` sont bien sur le même réseau Docker. |
| 400 sur save-content | Body non envoyé ou mal formaté | Vérifier que le nœud Code envoie bien `{ pages: [...] }` et que le nœud HTTP est en POST, Content-Type JSON, body = `$json`. |
| 502 sur push-to-flowise | Flowise injoignable ou FLOWISE_DOCUMENT_STORE_ID manquant | Vérifier `.env` (FLOWISE_URL, FLOWISE_DOCUMENT_STORE_ID). Depuis le conteneur `web`, Flowise est à `http://flowise:3000`. |

---

## 5. Flowise — Côté équipe

- **Document Store** : doit exister (nom ex. « Maisons-Alfort »), avec Text Splitter + Embeddings + Vector Store configurés. Voir `docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md`.  
- **Variables d’environnement (conteneur `web`)** :  
  - `FLOWISE_URL` : `http://flowise:3000` (depuis le conteneur) ou `http://localhost:3000` (depuis le host).  
  - `FLOWISE_DOCUMENT_STORE_ID` : UUID du Document Store (récupéré dans l’UI Flowise).  
- Après un **push réussi**, lancer l’**ingestion / Process** dans Flowise (Document Store → Upsert ou Process) si ton setup le requiert, ou vérifier que l’API upsert a bien ajouté les chunks.  
- Ensuite, le **Chatflow** qui utilise ce Document Store en « Knowledge » peut répondre aux questions sur Maisons-Alfort.

---

## 6. Checklist « tout faire fonctionner »

1. [ ] `make start` (ou `make up`) — tous les services up.  
2. [ ] `curl -s http://localhost:8000/api/concierge/scrape` → `{"status":"ok","pages":[...]}`.  
3. [ ] `.env` contient `FLOWISE_URL` et `FLOWISE_DOCUMENT_STORE_ID` (et `FLOWISE_API_KEY` si besoin).  
4. [ ] Dans Flowise : Document Store « Maisons-Alfort » créé et configuré (loader, splitter, embeddings, vector store).  
5. [ ] n8n : workflow importé, URLs = `http://web:8000` (ou `localhost:8000` si n8n hors Docker).  
6. [ ] Exécuter le workflow n8n (bouton « Test workflow » ou « Execute Workflow »).  
7. [ ] Vérifier : aucun nœud en erreur ; dernier nœud « Push to Flowise » retourne 200 et un JSON avec `status: ok`.  
8. [ ] Dans Flowise : lancer l’ingestion si nécessaire, puis tester le chat (Chatflow avec Knowledge = Maisons-Alfort).

---

## 7. Références

- **Routes back** : `docs/base-de-connaissances/routes-back-lppp.md`  
- **Flowise (workflow complet, prompts)** : `docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md`, `conciergerie-maisons-alfort-etat-valide-prompts.md`  
- **Push documents** : `docs/base-de-connaissances/flowise-push-documents-informatique.md`  
- **Export workflow n8n** : `docs/n8n-workflows/concierge-ia-aspiration-maisons-alfort.json`, `docs/n8n-workflows/README.md`

---

*Document créé pour que l’équipe puisse faire fonctionner le scraper, n8n et Flowise de bout en bout. Dernière mise à jour : 2026-01-30.*
