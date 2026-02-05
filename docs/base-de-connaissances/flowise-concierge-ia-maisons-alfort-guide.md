# Flowise — Guide pas à pas Concierge IA Maisons-Alfort

**Objectif** : Créer dans Flowise un Chatflow RAG (Document Loader texte, Text Splitter, Vector Store, LLM), avec le system prompt « assistant officiel Maisons-Alfort », ingérer les textes venant de n8n, puis récupérer l’URL du chat pour la page démo.

**Références** : [Flowise RAG](https://docs.flowiseai.com/tutorials/rag), [Document Stores](https://docs.flowiseai.com/using-flowise/document-stores), [Document Loaders](https://docs.flowiseai.com/integrations/langchain/document-loaders) (Text File, Plain Text).

---

## Démarrer sans perdre de données (`make up`)

**Tu ne perds rien** en faisant `make up` (ou `make start`) :

- **Landing pages et code** : tout est dans ton dépôt (fichiers sur le disque). Docker monte le projet en lecture/écriture (`.:/app`) : les conteneurs utilisent tes fichiers, ils ne les effacent pas.
- **Base PostgreSQL** (landings en base, utilisateurs, etc.) : stockée dans un volume nommé `postgres_data`. `make up` et `make down` **ne suppriment pas** les volumes.
- **n8n** (workflows) et **Flowise** (chatflows, vecteurs) : idem, volumes `n8n_data` et `flowise_data` conservés.

La **seule** commande qui supprime les volumes (et donc réinitialise la base, n8n, Flowise) est **`make go`** (démarrage à froid complet). À utiliser seulement pour repartir de zéro. En résumé : **`make up` = démarrer ; `make down` = arrêter ; les données restent.**

---

## Vue d’ensemble

1. **Document Store** : créer une base de documents « Maisons-Alfort », y ajouter un loader **Text File**, un **Text Splitter**, un **Embedding** et un **Vector Store**, puis **Upsert** (ingestion).
2. **Chatflow** : créer un flux avec un nœud **Agent**, une **Knowledge (Document Store)** pointant vers ce Document Store, et un **System Prompt**.
3. **Ingestion des textes** : les textes sortis de n8n sont mis dans un ou plusieurs fichiers `.txt`, uploadés dans le Document Store (ou via API).
4. **URL du chat** : utiliser l’onglet **Embed** ou **API** du Chatflow pour récupérer l’URL à mettre dans la page démo.

**Interface de test dans LPPP** : une fois le chatflow créé, configurer `FLOWISE_CHATFLOW_ID` (ID visible dans Flowise → Embed) dans `.env`, puis ouvrir **`/essais/concierge/`** (authentification admin requise) pour tester le chatbot dans l’interface Django. Voir `docs/base-de-connaissances/routes-back-lppp.md` et `.env.example`.

**Landing publique équipes municipales** : la page **`/maisons-alfort/`** affiche le même chatbot en mode public (sans connexion). Pour qu’il s’affiche au lieu du message « Chat en cours de configuration », il faut **obligatoirement** dans ton `.env` :
- **`FLOWISE_CHATFLOW_ID`** = l’ID du chatflow (dans Flowise : ouvre ton Chatflow → onglet **Embed** → l’URL est du type `http://.../embed/XXXX` → **XXXX** est l’ID à copier).
- **`FLOWISE_URL`** = `http://localhost:3000` si Flowise tourne en local (pour que l’iframe charge le chat depuis le navigateur).

Puis **redémarrer le runserver** (ou le conteneur web) pour que Django relise le `.env`. Sous WSL : `python3 manage.py runserver 127.0.0.1:8082` ou `bash scripts/runserver-wsl.sh 8082` (pas `python`, utiliser **python3**).

### Exemple d’ID et d’appels API (Flowise Embed / Prediction)

Une fois le chatflow créé, Flowise affiche dans l’onglet **Embed** un script et une URL de prédiction. Le **même ID** sert pour l’iframe (`/embed/{id}`) et pour l’API (`/api/v1/prediction/{id}`). Exemple (à remplacer par ton propre ID si différent) :

- **ID chatflow** : `c95b70d6-c7b7-49a8-920f-de00615b0176`
- **Host** : `http://localhost:3000`

**Embed (script dans une page HTML)** :

```html
<script type="module">
    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
    Chatbot.init({
        chatflowid: "c95b70d6-c7b7-49a8-920f-de00615b0176",
        apiHost: "http://localhost:3000",
    })
</script>
```

**API de prédiction** (même chatflowId) :

- **curl** :  
  `curl http://localhost:3000/api/v1/prediction/c95b70d6-c7b7-49a8-920f-de00615b0176 -X POST -d '{"question": "Hey, how are you?"}' -H "Content-Type: application/json"`

- **Python** :  
  `POST http://localhost:3000/api/v1/prediction/{chatflowId}` avec body `{"question": "..."}` (ex. avec `requests.post(API_URL, json={"question": "..."})`).

- **JavaScript (fetch)** :  
  `POST` sur la même URL avec `body: JSON.stringify({ question: "..." })`.

Dans LPPP, l’iframe utilise l’URL **`{FLOWISE_URL}/embed/{FLOWISE_CHATFLOW_ID}`** construite par `get_flowise_chat_embed_url()` ; il suffit de définir `FLOWISE_CHATFLOW_ID` (et `FLOWISE_URL`) dans `.env`.

**Workflow complet en une seule recette (click & drop)** : **`docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md`** — checklist reproductible étape par étape.

---

## Étape 1 — Préparer les textes pour Flowise (depuis n8n)

Après avoir exécuté le workflow n8n « Concierge IA – Aspiration Maisons-Alfort », tu obtiens des items avec `url` et `text`.

**Option A — Un seul fichier .txt (recommandé pour démarrer)**  
Crée un fichier `maisons-alfort-contenu.txt` qui contient tout le texte à ingérer, par exemple une section par page avec un titre :

```
=== Page: Accueil (https://www.maisons-alfort.fr/) ===
[colle ici le champ "text" du premier item]

=== Page: État civil ===
[colle le "text" du 2e item]

=== Page: Déchets ===
[colle le "text" du 3e item]

...
```

Tu peux copier-coller les sorties du nœud « Pages pour Flowise » dans n8n (affichage JSON des items), extraire chaque `text` et les concaténer dans ce fichier.

**Option B — Export automatique depuis n8n**  
Si tu ajoutes un nœud « Write Binary File » ou que tu exportes le JSON depuis n8n, tu peux générer le `.txt` avec un petit script local. Exemple Python (à lancer en local après avoir récupéré le JSON) :

```python
# Exemple : tu as un fichier pages.json avec {"pages": [{"url": "...", "text": "..."}, ...]}
import json
with open("pages.json") as f:
    data = json.load(f)
with open("maisons-alfort-contenu.txt", "w", encoding="utf-8") as out:
    for p in data.get("pages", []):
        out.write(f"\n\n=== {p.get('url', '')} ===\n\n")
        out.write(p.get("text", ""))
```

Ensuite, uploade `data/flowise/maisons-alfort-contenu.txt` dans Flowise (étape 2). Voir aussi `data/flowise/README.md` et `data/flowise/comptes-et-llm.md` (comptes + LLM à configurer).

---

## Étape 2 — Document Store dans Flowise

1. Ouvre Flowise : **http://localhost:3000** (ou l’URL de ton instance).
2. Va dans **Document Stores** (menu ou onglet dédié).
3. **Créer un Document Store** :
   - Nom : `Maisons-Alfort` (ou « Assistant Ville Maisons-Alfort »).
   - Enregistrer.

4. **Ouvrir ce Document Store** et configurer le pipeline d’indexation :

   **2.1 Document Loader**  
   - Clique sur **Add Document Loader** (ou équivalent).
   - Choisis **Text File** (ou **Plain Text** si disponible et adapté).
   - Configure :
     - **Upload** : tu uploaderas le fichier `maisons-alfort-contenu.txt` (ou plusieurs .txt).
     - Optionnel : **Metadata** (ex. `source: maisons-alfort`) pour filtrer plus tard.
   - Valide.

   **2.2 Text Splitter**  
   - Choisis **Recursive Character Text Splitter**.
   - Paramètres suggérés :
     - **Chunk Size** : 800–1200 (caractères).
     - **Chunk Overlap** : 100–150.
   - Cela découpe le texte en blocs pour la recherche sémantique.

   **2.3 Embedding**  
   - Clique sur **Select Embeddings**.
   - Choisis un modèle d’embedding (ex. **OpenAI Embeddings** si tu as une clé API, ou **Ollama** / autre selon ton installation).
   - Si OpenAI : modèle type `text-embedding-ada-002` (ou `text-embedding-3-small`). Renseigne ta clé dans les credentials si demandé.

   **2.4 Vector Store**  
   - Clique sur **Select Vector Store**.
   - Pour une démo rapide : **In-Memory Vector Store** (pas de base externe).
   - Pour garder les données après redémarrage : **Upstash**, **Pinecone** ou autre (à configurer avec tes identifiants).
   - Option **Top K** : 4 par défaut (nombre de chunks récupérés par question).

   **2.5 Record Manager (optionnel)**  
   - Tu peux ignorer pour la première démo ; utile si tu veux mettre à jour / supprimer des documents plus tard.

5. **Upsert (ingestion)**  
   - Dans le Document Store, déclenche l’**upload** du fichier `maisons-alfort-contenu.txt` (bouton d’upload ou « Process » / « Upsert » selon l’UI).
   - Attends la fin du traitement (nombre de chunks créés affiché).
   - Optionnel : utilise **Retrieval Query** pour tester une question (ex. « Quels documents pour un passeport ? ») et vérifier que des chunks pertinents remontent.

---

## Étape 3 — Chatflow RAG (Agent + Knowledge + System Prompt)

1. Dans Flowise, va dans **Chatflows** (ou **Flows** selon la version).
2. **Créer un nouveau Chatflow** (nom ex. « Assistant Maisons-Alfort »).

3. **Ajouter un nœud Agent**  
   - Glisse-dépose un nœud **Agent** (ou **Chatflow** avec Agent).
   - Configure le **modèle** (LLM) : OpenAI, Ollama, etc. Renseigne les credentials si besoin.

4. **Ajouter la Knowledge (Document Store)**  
   - Dans la config de l’Agent, cherche **Knowledge** / **Document Store** / **Add Knowledge**.
   - Sélectionne le **Document Store** « Maisons-Alfort » que tu viens de créer et d’upserter.
   - Définir **ce que contient la base** (description pour le LLM) : ex.  
     *« Contenu officiel du site de la Ville de Maisons-Alfort : horaires, démarches (état civil, déchets, travaux), informations pratiques pour les habitants. »*  
   - Tu peux utiliser le bouton **Auto-generate** si Flowise le propose pour générer cette description.

5. **System Prompt**  
   - Dans l’Agent, champ **System Message** (ou **System Prompt**) :
   ```
   Tu es l'assistant virtuel officiel de la ville de Maisons-Alfort. Tu réponds de manière courtoise, précise et uniquement en te basant sur les informations fournies dans la base de connaissances. Si tu ne trouves pas l'information, dis que tu ne peux pas répondre et invite l'utilisateur à contacter la mairie.
   ```
   - Enregistre.

6. **Tester le Chatflow**  
   - Dans l’interface du Chatflow, pose des questions (ex. « Quels documents pour un passeport ? », « Quand passent les encombrants ? »).
   - Vérifie que les réponses s’appuient bien sur le contenu du site (sans inventer).

---

## Étape 4 — Récupérer l’URL du chat (embed ou API)

1. Dans l’écran du Chatflow, ouvre l’onglet **Embed** (ou **Share** / **API**).
2. Tu obtiens soit :
   - une **URL d’iframe** (ex. `http://localhost:3000/embed/xxx`) à mettre dans la page démo,
   - soit une **URL d’API** (ex. `http://localhost:3000/api/v1/prediction/xxx`) pour appels programmatiques.
3. **Pour la page démo** (`deploy/concierge-demo-maisons-alfort/index.html`) :  
   - Remplace le bloc placeholder par une balise iframe dont le `src` est l’URL d’embed fournie par Flowise.  
   - Exemple :  
     `<iframe src="http://localhost:3000/embed/VOTRE_ID" title="Chat assistant Maisons-Alfort"></iframe>`  
   - Si Flowise est exposé en production, utilise l’URL HTTPS correspondante.

4. **Optionnel — Chatflow ID pour API**  
   - L’ID du Chatflow est souvent visible dans l’URL (ex. `.../chatflow/abc-123`) ou dans la section API.  
   - Prédiction : `POST http://localhost:3000/api/v1/prediction/{chatflowId}` avec body `{"question": "..."}` (voir [API Reference](https://docs.flowiseai.com/api-reference)).

---

## Résumé des choix importants

| Élément | Suggestion pour la démo |
|--------|--------------------------|
| Document Loader | **Text File** (fichier .txt contenant les textes scrapés) |
| Text Splitter | **Recursive Character Text Splitter** (chunk 800–1200, overlap 100–150) |
| Embedding | OpenAI ou Ollama selon ta config |
| Vector Store | **In-Memory** pour tester ; Upstash/Pinecone pour persistant |
| System Prompt | « Tu es l'assistant virtuel officiel de la ville de Maisons-Alfort… » |
| Ingestion | Un fichier .txt unique avec toutes les pages concaténées (ou un .txt par page si tu préfères) |

---

## Dépannage rapide

- **« Impossible de trouver l'adresse IP du serveur de flowise »** (iframe sur /maisons-alfort/) : l'URL d'embed doit être résolue par le **navigateur** ; le nom `flowise` n'existe que dans le réseau Docker. Avec runserver sur l'hôte (DB_HOST=localhost), le code utilise désormais `http://localhost:3000` par défaut. Sinon définir **FLOWISE_URL=http://localhost:3000** dans `.env`. S'assurer que Flowise écoute sur 3000 (`docker compose up -d flowise`). Voir `erreurs-et-solutions.md` § Landing /maisons-alfort/.
- **Aucun chunk après Upsert** : vérifier que le fichier .txt est bien uploadé et que le Text Splitter a une taille de chunk raisonnable (pas trop grande).
- **Le modèle ne répond pas** : vérifier les credentials du LLM (clé API, URL Ollama, etc.).
- **Réponses hors-sujet** : renforcer le System Prompt (« uniquement sur les informations fournies ») et vérifier que la Knowledge pointe vers le bon Document Store et qu’il est bien upserté.
- **Embed ne s’affiche pas** : si la page démo est en HTTPS et Flowise en HTTP, l’iframe peut être bloquée ; exposer Flowise en HTTPS ou tester en local (page et Flowise en localhost).

---

*Guide créé pour assister à la mise en place du Concierge IA Maisons-Alfort dans Flowise. Plan technique global : `concierge-ia-maisons-alfort-n8n-flowise.md`.*
