# Avis à l’équipe — Rangement projet, landing pages et ressources

**Date** : 2026-01-30  
**Porteur** : Chef de Projet (demande utilisateur)  
**Statut** : À appliquer par toute l’équipe

---

## Message

**On devrait ranger le projet, les landing pages et les ressources.**

Tous les agents sont invités à appliquer les règles existantes (bonnes pratiques § 5 et 6, organisation contacts, ressources utilisateur) et à contribuer au rangement dans leur périmètre. Le Chef de Projet pilote et valide ; l’Orchestrateur rappelle la stratégie si besoin.

---

## Références (à respecter)

| Doc | Contenu |
|-----|--------|
| `docs/bonnes-pratiques.md` § 5 et § 6 | Rien à la racine sauf prévu ; pas de temporaire ; où mettre les fichiers (apps/, docs/, lppp/, docker/, templates/) ; un fichier = un rôle clair. |
| `docs/base-de-connaissances/organisation-donnees-contacts.md` | Un contact = un dossier `docs/contacts/<slug>/` ; contenu type (content_json, notes, rapport, pieces/). |
| `docs/contacts/REGISTRE-CONTACTS.md` | Liste des dossiers contacts ; à mettre à jour à chaque nouveau dossier. |
| `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md` | Index des ressources (textes, images, ébauches, études, autres) ; structure des dossiers. |
| `docs/base-de-connaissances/segmentations/2026-01-30-rangement-projet-landings-ressources.md` | Tâches par rôle pour le rangement (checklist opérationnelle). |

---

## Checklist de rangement (synthèse)

- **Racine projet** : aucun fichier ni dossier en plus de ceux prévus (README, Makefile, manage.py, docker-compose, requirements, .env.example, .gitignore + apps/, lppp/, docs/, docker/, templates/, .cursor/). Supprimer scripts one-shot, copies de debug, fichiers temporaires.
- **Landing pages** : contenus par contact dans `docs/contacts/<slug>/` (landing-proposition-*.json, rapports) ; déploiements dans `deploy/<projet>/` avec README ou doc dédiée ; cohérence avec `REGISTRE-CONTACTS.md` et console landings (admin / vues).
- **Ressources** : tout ce qui vient de l’utilisateur dans `docs/ressources-utilisateur/` (textes/, images/, ebauches/, etudes/, autres/) avec entrée dans `REGISTRE-RESSOURCES.md` ; fiches entretien dans `fiches-entretien-emploi/` par entreprise.
- **Documentation** : docs dans `docs/` (base-de-connaissances, logs, contacts, segmentations) ; pas de .md orphelins à la racine.
- **Code** : métier dans `apps/<app>/` ; config dans `lppp/`, `docker/` ; scripts pérennes dans `scripts/` documenté ou commandes Django / Makefile.

Chaque agent nettoie derrière lui en fin de session et ne laisse rien d’inutile.

---

## Suivi

- **TODO** : tâche « Rangement projet, landings et ressources (avis équipe) » dans `docs/TODO.md`.
- **Segmentation** : `segmentations/2026-01-30-rangement-projet-landings-ressources.md` pour répartition des tâches par rôle.

---

*Document maintenu par le Chef de Projet. Dernière mise à jour : 2026-01-30.*
