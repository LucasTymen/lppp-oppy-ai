# Sauvegarde des workflows Flowise et n8n — règle projet

**Objectif** : éviter que les workflows (chatflows Flowise, workflows n8n) ne se volatilisent ou soient effacés. **Tout workflow créé ou modifié doit être exporté et versionné dans le dépôt** pour pouvoir être réinjecté en cas de problème.

**Contexte** : pertes répétées de chatflows Flowise (réinitialisation après changement de credentials, volume vide, etc.) et risque identique pour n8n. Décision utilisateur : sauvegarder systématiquement et permettre une réinjection facile.

**Pilotes** : **Automatizer** (Responsible — export et dépôt), **Chef de Projet** (vérification que la règle est appliquée), **tous les agents** qui créent ou modifient un workflow (doivent exporter et sauvegarder).

---

## 1. Règle

- **Flowise** : tout **chatflow** (ex. Concierge Maisons-Alfort, futurs RAG) → export JSON déposé dans **`docs/flowise-workflows/backups/`** avec nom explicite et date (ex. `concierge-maisons-alfort-2026-01-30.json`). À faire **dès la création** et **à chaque modification importante**.
- **n8n** : tout **workflow** → export JSON déposé dans **`docs/n8n-workflows/`** (déjà en place), nom explicite, et mise à jour du README du dossier. À faire dès la création et à chaque modification importante.
- **Commit + push** : les fichiers d’export font partie du dépôt ; après dépôt, faire **commit et push** (sur les deux remotes si applicable) pour que toute l’équipe et les environnements disposent des sauvegardes.

---

## 2. Où sauvegarder

| Type | Dossier | Nom de fichier type |
|------|---------|----------------------|
| **Flowise — chatflow** | `docs/flowise-workflows/backups/` | `nom-du-chatflow-YYYY-MM-DD.json` |
| **n8n — workflow** | `docs/n8n-workflows/` | `nom-workflow.json` (voir README du dossier) |

---

## 3. Comment exporter

### Flowise (chatflow)

1. Ouvrir le chatflow dans l’UI Flowise (http://localhost:3000).
2. Sur le **canvas** du chatflow : menu (⋯) ou **Export** / **Download** / **Save as JSON**.
3. Enregistrer dans `docs/flowise-workflows/backups/<nom>-<date>.json`.
4. Optionnel : mettre à jour le tableau dans `docs/flowise-workflows/backups/README.md`.

**Réinjection** : créer un nouveau chatflow vide → sur le canvas **Load** / **Import from file** → sélectionner le JSON. Vérifier ensuite les credentials (LLM, Embeddings) et la Knowledge (Document Store). Récupérer le nouvel ID (onglet Embed) et mettre à jour `FLOWISE_CHATFLOW_ID` dans `.env` si besoin.

### n8n (workflow)

1. Dans n8n : ouvrir le workflow → menu (⋯) → **Download** ou **Export**.
2. Enregistrer dans `docs/n8n-workflows/` avec un nom explicite.
3. Mettre à jour `docs/n8n-workflows/README.md` (tableau des workflows).

**Réinjection** : dans n8n, **Import from file** (ou glisser-déposer le JSON) puis sauvegarder.

---

## 4. Qui fait quoi (RACI)

| Rôle | Responsabilité |
|------|----------------|
| **Automatizer** | Créer/modifier les workflows Flowise et n8n ; **exporter et déposer** les JSON dans les dossiers ci‑dessus ; mettre à jour les README si besoin. |
| **Dev Django** | Si un workflow touche à des endpoints Django : s’assurer que le workflow exporté est bien sauvegardé (ou rappeler à l’Automatizer). |
| **DevOps** | Rappel dans les procédures de déploiement / relance : les workflows sont dans le dépôt ; en cas de perte de volume, réinjecter depuis `docs/flowise-workflows/backups/` et `docs/n8n-workflows/`. |
| **Chef de Projet** | Vérifier que la règle est appliquée (à chaque livrable ou sprint contenant un workflow : présence des exports dans le dépôt). |

**Tout agent** qui crée ou modifie un workflow Flowise ou n8n doit appliquer cette règle (exporter + déposer + commit).

---

## 5. Références

- **Flowise backups** : `docs/flowise-workflows/backups/README.md`
- **n8n workflows** : `docs/n8n-workflows/README.md`
- **Recette Concierge Maisons-Alfort** : `docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md` (inclut l’étape de sauvegarde)
- **Erreur « No Chatflows Yet »** : `erreurs-et-solutions.md` § Flowise — No Chatflows Yet ; réinjection via backups

---

*Document créé pour formaliser la règle de sauvegarde des workflows (2026-01-30).*
