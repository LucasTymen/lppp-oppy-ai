# Workflows n8n — exports et documentation

**Objectif** : Stocker les exports JSON des workflows n8n (pour versioning, partage, restauration).

**Référence** : `docs/base-de-connaissances/guide-equipe-scraper-n8n-flowise.md`, `concierge-ia-maisons-alfort-n8n-flowise.md`.

---

## Workflows prévus / en place

| Workflow | Fichier | Description |
|----------|---------|-------------|
| Concierge IA – Aspiration Maisons-Alfort | `concierge-ia-aspiration-maisons-alfort.json` | **Finalisé.** Scrape → save-content → push-to-flowise → Merge (collecte scrape + Flowise) → Rapport run. Sortie : `{ run, scrape: { pageCount, urls, errors }, flowise: { file, numAdded } }`. `http://web:8000` si n8n et Django dans le même Docker. Voir **`docs/base-de-connaissances/guide-equipe-scraper-n8n-flowise.md`**. |

---

## Comment exporter un workflow depuis n8n (obligatoire)

**Règle projet** : tout workflow n8n créé ou modifié **doit** être exporté et déposé ici pour éviter les pertes. Voir **`docs/base-de-connaissances/sauvegarde-workflows-flowise-n8n.md`**.

1. Dans n8n : ouvrir le workflow → menu (⋯) → **Download** ou **Export**.
2. Enregistrer le fichier JSON dans ce dossier avec un nom explicite.
3. Mettre à jour ce README (tableau ci‑dessus) avec le nom du fichier et une courte description.
4. **Commit + push** pour versionner la sauvegarde.

---

*Dossier créé pour le Quick Win Concierge IA. Sauvegarde systématique des workflows (règle 2026-01-30).*
