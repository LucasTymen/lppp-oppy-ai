# Répertoire de travail Flowise (LPPP)

Tout ce dont tu as besoin pour Flowise (Concierge IA Maisons-Alfort et autres chatflows RAG) est ici.

**Chemin projet** : `data/flowise/`

```
data/flowise/
├── README.md                    ← ce fichier
├── maisons-alfort-contenu.txt   ← contenu à ingérer (RAG Maisons-Alfort)
├── comptes-et-llm.md            ← comptes et LLM à créer / configurer (sans secrets)
└── faiss/                       ← index FAISS (un sous-dossier par RAG) — voir faiss/README.md
    └── maisons-alfort/           ← créé par Flowise ou à la main ; Base Path = /data/flowise/faiss/maisons-alfort
```

## Utilisation

1. **Contenu à ingérer** : après le workflow n8n « Concierge IA – Aspiration Maisons-Alfort », colle les textes dans `maisons-alfort-contenu.txt` (voir le fichier pour le format).
2. **Comptes et LLM** : ouvre `comptes-et-llm.md` pour la liste des comptes (Flowise, OpenAI ou autre) et des modèles (embedding + LLM) à configurer. Les secrets restent dans `.env` ou dans l’UI Flowise, jamais dans ce dépôt.
4. **Guide pas à pas** : `docs/base-de-connaissances/flowise-concierge-ia-maisons-alfort-guide.md`

## Rappel

- Ne pas committer de clés API ni de mots de passe dans ce dossier.
- Les fichiers **`*.txt`** dans `data/flowise/` sont dans le **`.gitignore`** (contenu généré/scrapé) : ils ne sont pas versionnés. À créer ou remplir en local (voir le guide Flowise pour le format de `maisons-alfort-contenu.txt`).
