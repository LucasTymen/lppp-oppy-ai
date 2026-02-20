# Workflows Flowise (LPPP)

Ce dossier contient les **workflows Flowise** (chatflows RAG, Concierge IA, etc.) sous forme de **recettes reproductibles** et de **sauvegardes JSON** versionnées (dossier **`backups/`**).

- **Résumé équipe (architecture + onboarding)** : **`conciergerie-maisons-alfort-architecture-et-onboarding.md`** — ce qui est en place, chemin FAISS, schéma Mermaid, checklist développeur. Partager tel quel.
- **À utiliser en priorité — workflow complet** : `workflow-complet-concierge-maisons-alfort.md` — à suivre pas à pas dans l’UI Flowise (click & drop) pour obtenir un workflow complet et fonctionnel.
- **État validé + prompts finaux** : `conciergerie-maisons-alfort-etat-valide-prompts.md` — câblage stable, prompts copier-coller, test final, suite possible.
- **Sauvegardes (règle projet)** : **`backups/`** — tout chatflow créé ou modifié doit être exporté en JSON et déposé ici. Réinjection via **Load** sur le canvas. Voir `backups/README.md` et **`docs/base-de-connaissances/sauvegarde-workflows-flowise-n8n.md`**.
- **Template** : `chatflow-concierge-maisons-alfort-template.json` (exemple). Flowise permet d’exporter / importer un chatflow en JSON (bouton **Load Chatflow** ou **Import** selon la version). Si tu as déjà construit le flow, exporte-le et dépose le fichier ici pour le partager. Le format exact dépend de la version Flowise.

Voir aussi : `docs/base-de-connaissances/flowise-concierge-ia-maisons-alfort-guide.md`, `data/flowise/README.md`.
