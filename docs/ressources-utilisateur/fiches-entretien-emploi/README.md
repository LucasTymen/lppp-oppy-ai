# Fiches Entretien Emploi — Espace de l’assistant copilote

**Rôle** : espace de travail de l’**Assistant Entretien Emploi** (règle `.cursor/rules/assistant-entretien-emploi.mdc`).  
L’agent y crée et met à jour les **fiches Résumé** (HTML avec accordéons) pour la préparation des entretiens d’embauche.

## Modèle canonique

- **Fichier de référence** : `_modele-canonique_prepa_entretien.html` (à la racine de ce dossier).
- À **chaque nouvelle préparation** : utiliser ce modèle (structure + styles + script), puis **remplacer tout le contenu** par les données de la société ciblée. Vérifier qu'il ne reste **aucun résidu** de l'ancienne société (checklist dans la base de connaissances).
- **Doc complète** : `docs/base-de-connaissances/fiches-entretien-emploi-modele-et-veille.md` (modèle, veille, coordination agents, checklist « nouvelle société »).

## Organisation

- **Un dossier par entreprise** (nom de l’entreprise, éventuellement `Nom_Marche` si pertinent).
- Dans chaque dossier :
  - **fiche HTML** : fiche de préparation entretien (structure = modèle canonique, contenu = société ciblée).
  - **ressources** : notes, extraits, documents utilisés pour construire la fiche.
  - **résumé** : fichier texte ou Markdown des points clés à réviser.
  - **versions** : copies datées des fiches avant mise à jour (ou sous-dossier `versions/`).

## Exemples de référence

- **Structure HTML** : modèle canonique (titre, info-box, accordéons `.accordion` / `.sub-accordion`, `.panel` / `.sub-panel`, classes `.highlight`, `.success`, `.warning`, `.info`, `.tip`).
- **Rubriques** : présentation entreprise, missions, KPIs, questions techniques (Python, Django, Java, Spring, Angular, Growth…), questions à poser, questions relationnelles (Rédacteur = agent RH).

## Règles

- Ne pas supprimer une fiche sans en garder une copie datée.
- Toute mise à jour → nouvelle version datée ou copie de l’ancienne avant écrasement.
- **Changement de société** : repartir du modèle canonique ou appliquer la checklist « nouvelle société » (doc base de connaissances) pour éviter fantômes et hallucinations.
