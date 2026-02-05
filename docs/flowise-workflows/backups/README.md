# Sauvegardes des chatflows Flowise (LPPP)

**Règle projet** : tout chatflow Flowise créé ou modifié **doit** être exporté en JSON et déposé ici. En cas de perte (credentials, volume, réinitialisation), on réinjecte depuis ce dossier.

Voir la procédure complète : **`docs/base-de-connaissances/sauvegarde-workflows-flowise-n8n.md`**.

---

## Où déposer les exports

- **Un export par chatflow** : `nom-du-chatflow-YYYY-MM-DD.json` (ex. `concierge-maisons-alfort-2026-01-30.json`).
- À chaque **création** ou **modification importante** du chatflow : ré-exporter et ajouter/remplacer le fichier, puis **commit + push**.

---

## Comment exporter depuis Flowise

1. Ouvrir le chatflow dans Flowise (http://localhost:3000).
2. Sur le **canvas** du chatflow : menu (⋯) ou **Export** / **Download** / **Save as JSON** (libellé selon la version Flowise).
3. Enregistrer le fichier dans ce dossier : `docs/flowise-workflows/backups/<nom>-<date>.json`.
4. Mettre à jour ce README si tu ajoutes un nouveau flow (tableau ci‑dessous).

---

## Comment réinjecter (restauration)

1. Dans Flowise : **Chatflows** → **Add New** (créer un chatflow vide).
2. Sur le canvas : **Load** / **Import from file** (depuis le menu du canvas, pas le menu Paramètres global — plus fiable).
3. Choisir le fichier JSON depuis `docs/flowise-workflows/backups/`.
4. Vérifier les credentials (LLM, Embeddings) et la **Knowledge** (Document Store) — les références internes peuvent être à re-sélectionner après import.
5. Sauvegarder, récupérer le nouvel ID (onglet **Embed**) et mettre à jour **`FLOWISE_CHATFLOW_ID`** dans `.env` si besoin.

---

## Fichiers présents (à maintenir)

| Fichier | Chatflow | Date | Notes |
|---------|----------|------|-------|
| `ExportData-conciergerie-maisons-alfort.json` | Concierge Maisons-Alfort | Version actualisée | Un seul ExportData conservé (pas de doublon). Canvas : `../chatflow-conciergerie-maisons-alfort-restore.json`. |

---

*Dossier créé pour éviter la perte des workflows Flowise (règle projet 2026-01-30).*
