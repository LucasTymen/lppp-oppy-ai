# Rubrique « Chatbot & compétences » — À intégrer dans les supports (élus & services)

**Usage** : section réutilisable pour montrer clairement les compétences, ce qui a été mis en place sur Maisons-Alfort, la démarche et les pistes d’évolution. À placer dans une rubrique dédiée (landing, mail, ou doc joint).

---

## Ce que j’ai mis en place ici

Une **Conciergerie IA** dédiée à la mairie de Maisons-Alfort : un chatbot qui répond aux questions des citoyens **uniquement** à partir de documents officiels (procédures passeport, CNI, pièces à fournir, délais, etc.). Il est intégré sur une landing de démonstration et s’appuie sur un moteur **RAG** (Retrieval-Augmented Generation) : les réponses sont ancrées dans vos textes, pas inventées.

En pratique : l’utilisateur pose une question en langage naturel ; le système retrouve les passages pertinents dans les documents ingérés et formule une réponse factuelle. Si l’information n’est pas dans les sources, le bot ne l’invente pas.

---

## Compétences mobilisées

- **RAG & vectorisation** : ingestion de documents (PDF, texte), découpage, embeddings (OpenAI), stockage vectoriel (FAISS) et requête par similarité.
- **Orchestration** : Flowise (chatflow Conversational Retrieval QA) — chaîne question → recherche documentaire → réponse via LLM (gpt-4o-mini, température 0 pour limiter les hallucinations).
- **Intégration** : chatbot embarqué dans une page web (iframe), paramétrable (couleurs, textes) pour coller à votre charte.
- **Automatisation & interopérabilité** : Python, APIs, scripts pour alimenter ou faire évoluer les bases documentaires et les connecteurs métier.

---

## Démarche

1. **Sources de vérité** : se baser sur vos documents officiels (démarches, FAQ interne, guides) pour que l’IA ne réponde que sur ce qui est validé.
2. **Pas d’hallucination** : modèle configuré pour s’appuyer strictement sur le contexte récupéré ; refus de répondre hors sujet ou inventé.
3. **Itération** : on enrichit les documents (nouveaux thèmes, mises à jour) et on ré-ingère pour faire évoluer le périmètre sans tout refaire.

---

## Évolutions possibles

- **Élargir les thèmes** : autres démarches (état civil, urbanisme, etc.), horaires, contacts, FAQ accueil — à mesure que les documents sont fournis et validés.
- **Déploiement** : passage de la démo à un environnement hébergé (prod) avec contrôle d’accès et suivi des questions posées.
- **Ponts avec vos outils** : connecteurs légers (Python/API) vers vos logiciels métier pour des réponses à jour (ex. délais de rendez-vous, disponibilités).
- **Réutilisation** : même approche pour d’autres services ou d’autres communes (modèle réplicable, base documentaire par site).

---

## Où le voir

- **Landing de démo** : `/p/maisons-alfort/` (contexte projet LPPP).  
- **Documentation technique** : `docs/flowise-workflows/conciergerie-maisons-alfort-architecture-et-onboarding.md`.
