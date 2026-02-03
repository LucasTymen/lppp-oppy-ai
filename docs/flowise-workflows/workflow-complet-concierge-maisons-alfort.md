# Workflow complet et fonctionnel — Concierge IA Maisons-Alfort (Flowise)

Recette reproductible en **click & drop** dans l’UI Flowise. À suivre dans l’ordre pour obtenir un RAG opérationnel (Document Store + Chatflow).

---

## Pourquoi les nœuds ne se raccordent pas (et comment l'éviter)

Flowise impose des **types de flux** entre nœuds (Document, ChatMessage, etc.). Si tu branches une sortie « Document » sur une entrée « ChatMessage » (ou l'inverse), la connexion est refusée ou le flow ne tourne pas — d'où les **incompatibilités** quand on câble tout à la main sur le canvas.

**Règle pour ce RAG (Concierge Maisons-Alfort) : ne pas tout câbler sur un seul canvas.**

1. **Document Store (ingestion)**  
   Se configure **dans la section Document Stores**, pas en reliant des nœuds sur le canvas. Tu choisis successivement : Loader → Text Splitter → Embedding → Vector Store, puis tu lances **Upsert**. Aucun câble à tirer : l'interface enchaîne les étapes pour toi.

2. **Chatflow (réponse)**  
   Sur le **canvas Chatflow**, tu mets **un seul nœud type Agent** (ou Conversational Retrieval). Tu ne branches pas de « Document » ou de « Loader » ici. Tu configures l'Agent avec :
   - **Model/LLM** : OpenAI ou Ollama (dans les paramètres du nœud)
   - **Knowledge** : tu **sélectionnes** le Document Store « Maisons-Alfort » dans une **liste déroulante** (pas un câble)
   - **System Message** : le prompt en texte

Résultat : **aucune connexion physique entre nœuds** pour ce use case — tout passe par des **sélections** (Document Store, Knowledge). Si ta version affiche des prises sur l'Agent, laisse-les **déconnectées** et remplis uniquement les champs.

**Si plus tard tu construis un flow avec plusieurs nœuds câblés** : une sortie **Document** ne va que vers une entrée **Document** ; une sortie **ChatMessage** / **string** ne va que vers une entrée du même type. Vérifier les libellés des prises avant de tirer un câble.

**Règle d’or** : **ChatOpenAI = parler**, **OpenAI Embeddings = chercher**. Jamais brancher ChatOpenAI comme Embeddings (sinon erreur `embedQuery is not a function`). Voir `conciergerie-maisons-alfort-etat-valide-prompts.md` pour la config validée et les prompts finaux.

---

## Prérequis

- Flowise démarré (`make up` ou `make start`), accès à **http://localhost:3000**
- Fichier **`data/flowise/maisons-alfort-contenu.txt`** rempli (sortie n8n ou scraper)
- Comptes / clés : **OpenAI** (embedding + LLM) ou **Ollama** local — voir `data/flowise/comptes-et-llm.md`

---

## Partie 1 — Document Store « Maisons-Alfort »

| # | Action | Détail |
|---|--------|--------|
| 1 | Ouvrir Flowise | http://localhost:3000 |
| 2 | Aller dans **Document Stores** | Menu / sidebar |
| 3 | **Créer** un Document Store | Nom : `Maisons-Alfort` → Enregistrer |
| 4 | **Ouvrir** ce store | Cliquer sur « Maisons-Alfort » |
| 5 | **Add Document Loader** | Choisir **Text File** (ou **Plain Text**) |
| 6 | Configurer le loader | Prêt pour upload de `.txt` ; optionnel : metadata `source: maisons-alfort` |
| 7 | **Text Splitter** | **Recursive Character Text Splitter** — Chunk Size **1000**, Overlap **150** |
| 8 | **Embedding** | **OpenAI Embeddings** (ou Ollama) — renseigner la clé API si demandé ; modèle ex. `text-embedding-3-small` |
| 9 | **Vector Store** | **In-Memory Vector Store** (démo) ou Upstash/Pinecone (persistant) |
| 10 | **Upsert / Process** | Uploader **`data/flowise/maisons-alfort-contenu.txt`** → lancer l’ingestion → attendre la fin (nombre de chunks affiché) |
| 11 | (Optionnel) **Retrieval Query** | Tester une question (ex. « Quels documents pour un passeport ? ») pour vérifier que des chunks remontent |

---

## Partie 2 — Chatflow RAG (canvas)

| # | Action | Détail |
|---|--------|--------|
| 12 | Aller dans **Chatflows** (ou **Build** / **Canvas**) | Créer un nouveau chatflow |
| 13 | Nommer le chatflow | ex. **Assistant Maisons-Alfort** (icône disquette) |
| 14 | **Ajouter un nœud Agent** | Bouton **+** → chercher **Agent** (ou **Conversational Retrieval** selon la version) |
| 15 | Configurer le **modèle (LLM)** | Dans l’Agent : **OpenAI Chat** (ou Ollama) — modèle ex. `gpt-4o-mini` ; renseigner la clé API |
| 16 | **Ajouter la Knowledge** | Dans la config de l’Agent : **Knowledge** / **Document Store** → sélectionner **Maisons-Alfort** (créé à l’étape 3) |
| 17 | Description de la Knowledge | Ex. *« Contenu officiel du site de la Ville de Maisons-Alfort : horaires, démarches (état civil, déchets, travaux), informations pratiques. »* (ou **Auto-generate** si proposé) |
| 18 | **System Prompt** (System Message) | Coller : *« Tu es l'assistant virtuel officiel de la ville de Maisons-Alfort. Tu réponds de manière courtoise, précise et uniquement en te basant sur les informations fournies dans la base de connaissances. Si tu ne trouves pas l'information, dis que tu ne peux pas répondre et invite l'utilisateur à contacter la mairie. »* |
| 19 | **Sauvegarder** | Icône disquette |
| 20 | **Tester** | Dans l’onglet chat du flow : poser « Quels documents pour un passeport ? », « Quand passent les encombrants ? » → vérifier que les réponses s’appuient sur le contenu |

---

## Partie 3 — Récupérer l’URL du chat

| # | Action | Détail |
|---|--------|--------|
| 21 | Onglet **Embed** (ou **Share** / **API**) | Sur l’écran du Chatflow |
| 22 | Copier l’**URL d’iframe** (ou API) | Ex. `http://localhost:3000/embed/xxx` |
| 23 | Page démo | Remplacer dans `deploy/concierge-demo-maisons-alfort/index.html` le `src` de l’iframe par cette URL |

---

## Résumé visuel (ordre des nœuds)

**Document Store (ingestion)**  
`Text File (upload)` → `Recursive Character Text Splitter` → `OpenAI Embeddings` → `In-Memory Vector Store` → **Upsert**

**Chatflow (réponse)**  
`Agent` ← lié à **Knowledge** = Document Store « Maisons-Alfort » + **System Prompt** ci‑dessus ; LLM = OpenAI (ou Ollama).

---

*Une fois le flow construit, tu peux l’**exporter en JSON** (Load Chatflow / Export selon ta version) et déposer le fichier dans `docs/flowise-workflows/` pour le partager ou le réimporter.*
