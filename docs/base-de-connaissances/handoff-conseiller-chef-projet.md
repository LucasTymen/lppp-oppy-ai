# Handoff Conseiller → Chef de Projet

**Rôle** : Après **accord explicite** de l’utilisateur sur la stratégie, le **Conseiller** transmet au **Chef de Projet** les éléments nécessaires pour créer la segmentation et répartir les tâches. Ce document définit le **contenu minimal du brief** (handoff).

**Référence** : workflow de coordination — Phase 0 (Conseiller) → Phase 1 (Chef de Projet). Voir `.cursor/rules/coordination-agents.mdc`.

---

## 1. Checklist du brief (Conseiller → Chef de Projet)

Le Conseiller transmet au Chef de Projet (dans la segmentation à créer, en en-tête, ou dans un message structuré) :

| Élément | Description |
|--------|-------------|
| **Accord résumé** | En 3 à 5 lignes : ce sur quoi l’utilisateur a explicitement accordé (feature, périmètre, contraintes principales). |
| **Périmètre** | Features / livrables **inclus** ; éventuellement **exclus** (hors scope pour cette itération). |
| **Contraintes connues** | Techniques, délais, dépendances externes, ressources utilisateur à disposition. |
| **Risques identifiés** | Risques ou points d’attention mentionnés pendant l’échange (technique, organisationnel, données). |
| **Ressources utilisateur** | Si des données ou documents ont été déposés dans `docs/ressources-utilisateur/` ou `docs/contacts/`, les référencer (REGISTRE-RESSOURCES.md, chemin des fichiers). |

Le Chef de Projet s’en sert pour rédiger la segmentation (`YYYY-MM-DD-nom-feature.md`), mettre à jour le TODO et assigner les tâches selon la RACI.

---

## 2. Où mettre le brief

- **Option A** : En début de la segmentation créée par le Chef de Projet (section « Contexte / Handoff Conseiller »).
- **Option B** : Dans un fichier dédié par feature (ex. `docs/base-de-connaissances/segmentations/YYYY-MM-DD-nom-feature-brief.md`) référencé par la segmentation.
- **Recommandation** : **Option A** — une section « Contexte / Handoff » en tête de la segmentation, remplie par le Chef de Projet à partir des éléments fournis par le Conseiller.

---

## Références

- **Coordination** : `.cursor/rules/coordination-agents.mdc`
- **Conseiller** : `.cursor/rules/conseiller.mdc`
- **Template segmentation** : `docs/base-de-connaissances/segmentations/TEMPLATE.md`

---

*Document créé à l’issue de la réunion agile organisation équipe (2025-01-30).*
