# Comptes et LLM pour Flowise (Concierge IA Maisons-Alfort)

Liste de ce qu’il faut **créer ou configurer** (aucun secret ne doit être écrit ici ; tout reste dans `.env` ou dans l’interface Flowise).

**Identifiants (accès UI)** : les agents qui en ont besoin (Automatizer, DevOps, Dev Django) utilisent les variables **`FLOWISE_USERNAME`** et **`FLOWISE_PASSWORD`** dans le fichier **`.env`** à la racine du projet (fichier non versionné). Ne jamais copier ou coller d'identifiants dans un fichier du dépôt ou un doc committé. Voir `flowise-push-documents-informatique.md` § Identifiants et anti-leak.

---

## 1. Compte Flowise (accès UI)

| Quoi | Où le configurer | Note |
|------|------------------|------|
| **Utilisateur / mot de passe Flowise** | Fichier `.env` à la racine du projet | `FLOWISE_USERNAME` et `FLOWISE_PASSWORD`. Si vides, l’UI Flowise peut être en accès libre (déconseillé en production). |

À faire : remplir dans `.env` (copié depuis `.env.example`) puis redémarrer les conteneurs (`make down` puis `make up`).

---

## 2. Embedding (vecteurs pour la RAG)

Tu as besoin d’**un modèle d’embedding** pour que Flowise indexe le contenu du Document Store.

| Option | Ce qu’il te faut | Où le renseigner |
|--------|-------------------|------------------|
| **OpenAI Embeddings** | Clé API OpenAI | Dans Flowise : nœud **Embeddings** → OpenAI → champ **API Key** (ou Credentials Flowise). |
| **Ollama** (local) | Ollama installé + modèle ex. `nomic-embed-text` | Dans Flowise : nœud Embeddings → Ollama → URL de base (ex. `http://host.docker.internal:11434` si Ollama sur ta machine). |

Recommandation démo rapide : **OpenAI** avec `text-embedding-3-small` (ou `text-embedding-ada-002`) si tu as une clé.

---

## 3. LLM (modèle de chat)

Tu as besoin d’**un LLM** pour l’agent du Chatflow (réponses au visiteur).

| Option | Ce qu’il te faut | Où le renseigner |
|--------|-------------------|------------------|
| **OpenAI Chat** | Même clé API OpenAI | Dans Flowise : nœud **Agent** → Model → OpenAI → **API Key**. Modèle suggéré : `gpt-4o-mini` ou `gpt-3.5-turbo`. |
| **Ollama** (local) | Ollama installé + modèle ex. `llama3.2` ou `mistral` | Dans Flowise : nœud Agent → Model → Ollama → URL de base. |

Recommandation démo : **OpenAI** `gpt-4o-mini` (bon compromis coût/qualité).

---

## 4. Récap « ce que je dois avoir »

- [ ] **.env** : `FLOWISE_USERNAME` et `FLOWISE_PASSWORD` (optionnel pour dev local).
- [ ] **Clé API OpenAI** (ou compte Ollama local) pour **embedding**.
- [ ] **Même clé OpenAI** (ou Ollama) pour le **LLM** du Chatflow.
- [ ] Fichier **maisons-alfort-contenu.txt** rempli (sortie n8n) et uploadé dans le Document Store Flowise.

Une seule clé OpenAI suffit pour embedding + chat ; tu la renseignes dans les deux nœuds (Embeddings et Agent) dans l’interface Flowise.
