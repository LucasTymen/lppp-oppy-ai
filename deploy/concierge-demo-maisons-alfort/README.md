# Démo Concierge IA — Maisons-Alfort

Page démo de l’assistant virtuel (RAG) pour la Ville de Maisons-Alfort. Couleurs bleu/blanc et zone de chat (iframe Flowise).

## Utilisation

1. **Sans Flowise** : ouvrir `index.html` dans un navigateur — un texte d’instructions s’affiche à la place du chat.
2. **Avec Flowise** : une fois le Chatflow RAG configuré dans Flowise, récupérer l’URL du chat (embed). Dans `index.html`, remplacer le bloc placeholder par :
   ```html
   <iframe src="VOTRE_URL_FLOWISE" title="Chat assistant Maisons-Alfort"></iframe>
   ```
   Ou définir la variable `FLOWISE_CHAT_URL` (injection au build si déploiement statique).

## Déploiement

- **Local** : ouvrir `index.html` directement.
- **Vercel / Netlify** : déployer le contenu de ce dossier (site statique). Optionnel : variable d’environnement `FLOWISE_CHAT_URL` pour l’URL du chat.

## Référence

Plan technique et segmentation : `docs/base-de-connaissances/concierge-ia-maisons-alfort-n8n-flowise.md`, `docs/base-de-connaissances/segmentations/2025-01-30-quick-win-concierge-ia-maisons-alfort.md`.
