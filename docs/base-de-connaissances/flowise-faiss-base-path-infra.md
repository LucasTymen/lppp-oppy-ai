# Flowise — Base Path FAISS (infra et persistance)

**Contexte** : RAG avec Vector Store **FAISS** dans Flowise. FAISS exige un champ **« Base Path to load »** : le dossier physique où sont écrits et relus les fichiers d’index (`index.faiss`, metadata, etc.). Ce chemin doit être **persistant**, **accessible en lecture/écriture** par le conteneur Flowise, et **idéalement isolé par RAG / projet**.

---

## 1. Où stocker les index FAISS ?

**Recommandation LPPP** : **un dossier par RAG sous `data/flowise/faiss/<projet>`**, monté dans le conteneur Flowise.

| Côté host (projet) | Côté conteneur Flowise (à renseigner dans l’UI) |
|--------------------|--------------------------------------------------|
| `data/flowise/faiss/maisons-alfort/` | **`/data/flowise/faiss/maisons-alfort`** |
| `data/flowise/faiss/<autre-projet>/` | **`/data/flowise/faiss/<autre-projet>`** |

**Pourquoi ce choix :**

- Le volume **`./data/flowise`** est déjà monté dans Flowise en **`/data/flowise`** (`docker-compose.yml`). Tout ce qui est sous `data/flowise/faiss/` sur le host est donc visible en **`/data/flowise/faiss/`** dans le conteneur.
- **Persistant** : `data/flowise` est sur le disque du host ; `make down` / `make up` ne suppriment pas ces dossiers (seul `make go` supprime les volumes nommés, pas le bind mount `./data/flowise`).
- **Un dossier par RAG** : isolation claire (Maisons-Alfort, autre client, autre agent). Pas de mélange d’index.
- **Pas de volume Docker dédié supplémentaire** : on réutilise le montage existant. Si tu préfères un volume nommé plus tard (ex. `flowise_faiss_data`), tu peux le monter en `/data/flowise/faiss` et garder la même logique de sous-dossiers par projet.

**À faire dans Flowise** : dans la config du nœud **Vector Store FAISS**, champ **« Base Path to load »**, renseigner :

- Pour le RAG Maisons-Alfort : **`/data/flowise/faiss/maisons-alfort`**
- Pour un autre RAG : **`/data/flowise/faiss/<nom-projet>`**

Flowise créera le dossier au premier upsert si besoin (avec les droits du process). Tu peux aussi créer à l’avance côté host, ex. `data/flowise/faiss/maisons-alfort`.

---

## 2. Un dossier par client / par agent ?

**Oui.** Un sous-dossier par RAG (par « projet » ou par agent) :

- `data/flowise/faiss/maisons-alfort/` → Concierge IA Maisons-Alfort  
- `data/flowise/faiss/autre-ville/` → autre RAG  
- `data/flowise/faiss/autre-agent/` → autre use case  

Chaque Document Store / flow qui utilise FAISS pointe vers son propre Base Path. Évite les mélanges d’index et les conflits d’écriture.

---

## 3. Versionner ou écraser les index ?

**Ne pas versionner** les fichiers d’index (binaires, souvent lourds). Ils sont dans le **`.gitignore`** (`data/flowise/faiss/*/`).

**À l’exécution** : on **écrase / met à jour** l’index à chaque ingestion (upsert). C’est le comportement normal de Flowise/FAISS : un nouvel upsert recrée ou met à jour l’index dans le même Base Path. Pas besoin de versioning manuel des index (sauf besoin métier très spécifique de garder des snapshots).

---

## 4. Récap

| Question | Réponse |
|----------|--------|
| Où stocker les index FAISS ? | **`/data/flowise/faiss/<projet>`** dans le conteneur (= `data/flowise/faiss/<projet>/` sur le host). |
| Volume Docker dédié ? | Optionnel. Le bind mount `./data/flowise` suffit ; possible d’ajouter plus tard un volume nommé pour `faiss` si besoin. |
| Un dossier par client / agent ? | **Oui** — un sous-dossier par RAG. |
| Versionner ou écraser ? | **Ne pas versionner** (gitignore). **Écraser / mettre à jour** à chaque upsert (comportement par défaut). |

Dès que le **Base Path** est renseigné dans Flowise (ex. `/data/flowise/faiss/maisons-alfort`), tu peux lancer l’ingestion et finaliser le RAG.

---

## 5. Erreur 401 « Invalid model key » (hors FAISS)

Si Flowise affiche **« 401 Invalid model key or Incorrect local model configuration »** au chargement d’une page, le souci vient en général du **LLM ou de l’embedding** (clé API OpenAI invalide, modèle inexistant, ou mauvaise config d’un modèle local). Ce n’est pas lié au Base Path FAISS. Vérifier :

- Clé API OpenAI (ou autre fournisseur) valide et renseignée au bon endroit dans Flowise.
- Nom du modèle exact (ex. `gpt-4o-mini`, `text-embedding-3-small`).
- Si modèle local (Ollama, etc.) : URL et nom du modèle cohérents.

Voir aussi `docs/base-de-connaissances/erreurs-et-solutions.md` (entrée Flowise 401).
