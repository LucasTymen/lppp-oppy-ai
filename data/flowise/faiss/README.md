# Index FAISS (Flowise)

Les index du Vector Store FAISS sont stockés ici : **un sous-dossier par RAG**.

- **Côté host** : `data/flowise/faiss/<projet>/` (ex. `maisons-alfort`)
- **Dans Flowise (Base Path)** : `/data/flowise/faiss/<projet>`

Exemple pour le Concierge Maisons-Alfort : créer le dossier `maisons-alfort` (ou le laisser créer par Flowise au premier upsert), puis dans Flowise, Vector Store FAISS → **Base Path to load** = **`/data/flowise/faiss/maisons-alfort`**.

Les contenus de ces sous-dossiers (fichiers d’index) ne sont pas versionnés (`.gitignore`). Voir `docs/base-de-connaissances/flowise-faiss-base-path-infra.md`.
