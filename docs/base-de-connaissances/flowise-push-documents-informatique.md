# Flowise — Pousser les documents (brief Informaticien / Dev)

**Objectif** : permettre aux agents (Informaticien, Dev, Automatizer) de **pousser les documents** depuis le répertoire de travail `data/flowise/` vers Flowise (Document Store), en respectant l’arborescence, pour que l’utilisateur n’ait pas à importer manuellement dans l’interface quand c’est impossible ou peu pratique (Flowise dans son propre conteneur).

**Références** : [Flowise Document Store API](https://docs.flowiseai.com/api-reference/document-store), [Upsertion](https://docs.flowiseai.com/using-flowise/upsertion), `flowise-concierge-ia-maisons-alfort-guide.md`, `data/flowise/README.md`.

---

## Identifiants et anti-leak (agents Automatizer, DevOps, Dev Django)

- **Connexion UI Flowise** : `FLOWISE_USERNAME` et `FLOWISE_PASSWORD` dans **`.env`** uniquement (fichier non versionné). Les agents qui automatisent ou documentent l’accès à Flowise s’appuient sur ces variables ; ils ne doivent **jamais** écrire ni coller d’identifiants (login, mot de passe, clé API) dans un fichier du dépôt, un document committé, un ticket ou un message.
- **API (push documents)** : `FLOWISE_URL`, `FLOWISE_DOCUMENT_STORE_ID`, et optionnellement `FLOWISE_API_KEY` dans `.env`. Même règle : pas de valeur sensible dans le code ou la doc versionnée.
- En cas de doute : `docs/base-de-connaissances/politique-credentials-securite-flux.md` et `regles-securite.md`.

---

## 1. Arborescence à respecter

Tout le contenu destiné à Flowise doit être dans le répertoire de travail suivant (côté **projet / host**) :

```
data/flowise/
├── README.md
├── maisons-alfort-contenu.txt   ← contenu RAG Maisons-Alfort (à remplir depuis n8n ou scraper)
├── comptes-et-llm.md
└── (autres .txt si besoin, par thème ou par source)
```

- **Côté host** : les agents (scripts, n8n, commandes Django) écrivent ou déposent les fichiers dans `data/flowise/`.
- **Côté Flowise (conteneur)** : ce même dossier est monté en **`/data/flowise`** (voir `docker-compose.yml`). Flowise peut donc lire les fichiers à cet endroit si un loader est configuré pour un chemin, ou les documents sont poussés via **API** depuis le host (recommandé).

---

## 2. Pousser les documents vers Flowise (API)

Deux options pour alimenter le **Document Store** Flowise sans passer par l’upload manuel dans l’UI.

### Option A — Commande Django (recommandé)

Une commande management pousse les fichiers de `data/flowise/` vers le Document Store configuré :

```bash
# Depuis le host (ou dans le conteneur web)
python manage.py flowise_push_documents

# Ou en ciblant un fichier
python manage.py flowise_push_documents --file data/flowise/maisons-alfort-contenu.txt
```

**Prérequis** : dans `.env` (ou variables d’environnement) :

- `FLOWISE_URL` : URL de Flowise (ex. `http://localhost:3000` depuis le host, `http://flowise:3000` depuis un conteneur Docker).
- `FLOWISE_DOCUMENT_STORE_ID` : l’**UUID du Document Store** (ex. « Maisons-Alfort »). On le récupère dans l’interface Flowise : Document Stores → ouvrir le store → l’ID est dans l’URL ou dans les paramètres.
- `FLOWISE_API_KEY` (optionnel) : si Flowise est configuré avec un secret pour l’API, renseigner le token ici.

La commande envoie chaque fichier `.txt` (ou le fichier indiqué) en **POST** vers l’API Flowise Document Store Upsert.

### Option B — API Flowise directement (scripts, n8n)

Pour un script externe ou un workflow n8n :

1. **Lister les Document Stores** (pour obtenir l’ID) :  
   `GET {FLOWISE_URL}/api/v1/document-store/store`  
   (avec header `Authorization: Bearer {FLOWISE_API_KEY}` si configuré).

2. **Upsert d’un fichier** :  
   `POST {FLOWISE_URL}/api/v1/document-store/upsert/{documentStoreId}`  
   - Body : **multipart/form-data** avec le fichier (clé souvent `file` ou `files`).  
   - Exemple cURL depuis le host :
     ```bash
     curl -X POST "http://localhost:3000/api/v1/document-store/upsert/VOTRE_STORE_ID" \
       -H "Authorization: Bearer VOTRE_CLE_SI_BESOIN" \
       -F "file=@data/flowise/maisons-alfort-contenu.txt"
     ```

3. **Alternative — Vector Upsert (Chatflow)** : si le RAG est configuré via un **Chatflow** avec nœud d’upsert (méthode « Chatflow Upsert »), on peut utiliser :  
   `POST {FLOWISE_URL}/api/v1/vector/upsert/{chatflowId}`  
   avec le fichier en `multipart/form-data` (clé `files`).  
   Voir [Flowise Upsertion](https://docs.flowiseai.com/using-flowise/upsertion) et [Vector Upsert API](https://docs.flowiseai.com/api-reference/vector-upsert).

---

## 3. Rôle des agents

| Rôle | Tâche |
|------|--------|
| **Dev / Informaticien** | Mettre en place et maintenir la commande `flowise_push_documents`, les variables d’environnement (`.env.example` + doc), et éventuellement un nœud n8n qui appelle l’API Flowise ou l’endpoint Django après le scraper. |
| **Automatizer** | Intégrer dans les workflows n8n : après aspiration (ex. Concierge Maisons-Alfort), écrire les textes dans `data/flowise/maisons-alfort-contenu.txt` (ou plusieurs .txt), puis déclencher la push (appel à l’API Django ou à Flowise). |
| **DevOps** | S’assurer que le volume `data/flowise` est bien monté dans le conteneur Flowise (`docker-compose.yml`) et que les URLs (FLOWISE_URL depuis web/host) sont correctes. |

---

## 4. Résumé

- **Arborescence** : tout le contenu à ingérer dans Flowise est dans **`data/flowise/`** (host) et monté en **`/data/flowise`** dans le conteneur Flowise.
- **Push** : les agents poussent les documents via la **commande Django** `flowise_push_documents` ou via l’**API Flowise** (Document Store upsert ou Vector upsert selon la config).
- **Aucun secret** dans ce document : FLOWISE_URL, FLOWISE_DOCUMENT_STORE_ID et FLOWISE_API_KEY restent dans `.env` / configuration déploiement.
