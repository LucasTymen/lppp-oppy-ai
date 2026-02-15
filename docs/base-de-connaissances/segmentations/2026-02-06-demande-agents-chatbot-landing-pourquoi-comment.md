# Demande à tous les agents — Chatbot sur la landing : pourquoi ça ne marche pas, comment en finir

**Date** : 2026-02-06  
**Contexte** : La landing **/p/maisons-alfort/** affiche bien la page (titre, intro, message de dépannage) mais **le chatbot ne s’affiche pas** dans la zone prévue. Flowise fonctionne en interne (test direct sur localhost:3010). L’objectif est d’**utiliser le chatbot complètement dans la landing page**.

---

## Demande explicite à chaque agent

Chaque rôle concerné est invité à répondre (dans ce document, dans le sprint, ou dans `erreurs-et-solutions.md`) à **deux questions** :

1. **Pourquoi ça ne marche pas ?**  
   Selon votre périmètre (infra, intégration, sécurité, front, flux), quelle(s) cause(s) possible(s) voyez-vous ? Qu’avez-vous déjà vérifié ou constaté ?

2. **Comment en finir et réussir à utiliser le chatbot complètement dans la landing ?**  
   Quelles actions concrètes proposez-vous (vous ou votre rôle) pour que le widget/chat s’affiche et réponde sur `/p/maisons-alfort/` ?

---

## Rôles concernés et où répondre

| Agent | Pourquoi ça ne marche pas (hypothèses / constats) | Comment en finir (actions proposées) | Où documenter la réponse |
|-------|---------------------------------------------------|-------------------------------------|---------------------------|
| **DevOps** | Ports, .env, Flowise down, API prediction injoignable ? | Vérifs, correctifs infra, santé des services | Sprint § DevOps ou `flowise-chatbot-ecran-vide-diagnostic.md` |
| **Architecte** | Chaîne route/vue/template cassée, variables d’embed absentes, mauvais ID ? | Corriger la chaîne, lister les points de défaillance | Sprint § Architecte |
| **Ingénieur système** | Réseau (localhost:3010 joignable depuis le navigateur ?), processus, conteneurs ? | Checklist réseau/processus, contrôle des flux | Sprint § Ingénieur système |
| **Pentester** | CORS, CSP, X-Frame-Options bloquent le script ou l’iframe ? Secrets exposés ? | Ajuster config (sans casser la sécu), fiche sécurité flux | Sprint § Pentester |
| **Dev Django** | Contexte (flowise_api_host, flowise_chatflow_id) bien passés ? Template injecte bien le script ? | Corriger vue/template si besoin | Ce doc ou sprint |
| **Automatizer** | Flowise embed (script vs iframe), API Flowise, chatflow ID, version flowise-embed ? | Choisir la bonne méthode d’embed, tester l’API | Ce doc ou `flowise-chatbot-ecran-vide-diagnostic.md` |
| **Designer** | Zone chat masquée (CSS), conteneur trop petit, script qui ne monte pas ? | Ajuster styles, conteneur, visibilité | Ce doc ou sprint |
| **Chef de Projet** | Synthèse des réponses, priorisation, validation | Coordonner les réponses et le plan d’action | Sprint, `log-projet.md` |

---

## Comment répondre

- **Option 1** : Ajouter sous cette section (ou dans le sprint) un paragraphe **« Réponse [Rôle] »** avec vos constats et propositions.
- **Option 2** : Compléter le paragraphe « Diagnostic [Rôle] » déjà prévu dans le sprint `2026-02-06-sprint-controle-flux-chatbot-landing-maisons-alfort.md`.
- **Option 3** : Ouvrir une entrée dans `erreurs-et-solutions.md` (ex. « Chatbot ne s’affiche pas sur la landing — cause et solution ») et y indiquer la cause identifiée et les actions.

Une fois toutes les réponses recueillies, le **Chef de Projet** (ou l’agent qui pilote) synthétise la **cause racine** et le **plan d’action** pour en finir et avoir le chatbot pleinement utilisable sur la landing.

---

## Références

- **Sprint contrôle des flux** : `2026-02-06-sprint-controle-flux-chatbot-landing-maisons-alfort.md`
- **Diagnostic pas à pas** : `flowise-chatbot-ecran-vide-diagnostic.md`
- **Résumé problème / setup / config** : `chatbot-conciergerie-resume-probleme-setup-config.md`
- **Registre erreurs** : `erreurs-et-solutions.md`
- **Rôles** : `agents-roles-responsabilites.md`, `registre-agents-ressources.md`
