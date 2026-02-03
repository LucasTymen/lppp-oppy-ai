# Conciergerie Maisons-Alfort — État validé et prompts finaux

**Référence** : configuration Flowise **validée et stable** (RAG municipal fonctionnel, propre, non halluciné). Ne pas modifier sans raison.

---

## 1. Câblage validé (à ne plus toucher)

| Nœud | Config | Connexions |
|------|--------|------------|
| **OpenAI Embeddings** | Modèle : `text-embedding-3-small` | Sortie → **Faiss** (Embeddings) |
| **Faiss** | Base path : `/data/flowise/faiss/maisons-alfort` | Embeddings ← OpenAI Embeddings ; Sortie **Faiss Retriever** → Conversational Retrieval QA |
| **ChatOpenAI** | Modèle : `gpt-4o-mini` ; Temperature : `0` | Sortie → **Conversational Retrieval QA** (Chat Model) |
| **Conversational Retrieval QA Chain** | Memory ON ; Return Source Documents ON | Chat Model ← ChatOpenAI ; Vector Store Retriever ← Faiss Retriever |

**Règle d’or Flowise** : **ChatOpenAI = parler**, **OpenAI Embeddings = chercher**. Jamais l’inverse (ChatOpenAI branché comme Embeddings provoque `embedQuery is not a function`). Le chat injecte tout seul `{question}` et `{chat_history}`.

---

## 2. Prompts finaux (copier-coller exact)

**Aucune variable en plus, aucune en moins.**

### Rephrase Prompt (dans Conversational Retrieval QA)

```
Conversation history:
{chat_history}

Question:
{question}
```

### Response Prompt (dans Conversational Retrieval QA)

```
Tu es un agent de conciergerie numérique officiel de la ville de Maisons-Alfort.

Tu réponds uniquement à partir des informations contenues dans le contexte ci-dessous.

Si l'information demandée n'est pas présente dans le contexte, dis clairement que tu ne disposes pas de cette information.

Contexte:
{context}

Question:
{question}
```

---

## 3. Test final (ordre exact)

1. **Save** le canvas.
2. Cliquer sur l’icône **💬** (chat à droite).
3. Poser une question présente dans les docs, ex. : *Quels documents sont nécessaires pour une demande de passeport ?*
4. **Résultat attendu** : réponse correcte, basée uniquement sur le document ; pas d’erreur JS ; pas de réponse hors contexte.

---

## 4. Ce qui bloquait avant (et pourquoi c’est réglé)

- ChatOpenAI branché comme Embeddings → **interdit** (corrigé).
- Prompts non syntaxiquement valides pour Flowise → **corrigé** (variables `{chat_history}`, `{question}`, `{context}` respectées).
- Pas de nœud « Chat Input » à brancher → le chat injecte tout seul les variables.

---

## 5. Suite possible (sans casser l’existant)

- **Ajouter des documents** : upsert d’autres démarches (CNI, mariage, stationnement, écoles…).
- **Guardrail « hors périmètre »** : réponse explicite « Je n’ai pas cette information » si non trouvée (déjà partiellement dans le Response Prompt).
- **Exposer l’agent** : API Flowise, iframe sur site de la mairie (`deploy/concierge-demo-maisons-alfort/index.html`).
- **Versionner les stores** : un dossier FAISS par service / thématique (`/data/flowise/faiss/<projet>`).
- **Logs / audit** : garder les sources retournées (déjà activé : Return Source Documents ON).

---

*Référence : flowise-concierge-ia-maisons-alfort-guide.md, flowise-faiss-base-path-infra.md, workflow-complet-concierge-maisons-alfort.md.*
