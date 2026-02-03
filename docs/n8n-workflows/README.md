# Workflows n8n — exports et documentation

**Objectif** : Stocker les exports JSON des workflows n8n (pour versioning, partage, restauration).

**Référence** : `docs/base-de-connaissances/guide-equipe-scraper-n8n-flowise.md`, `concierge-ia-maisons-alfort-n8n-flowise.md`.

---

## Workflows prévus / en place

| Workflow | Fichier | Description |
|----------|---------|-------------|
| Concierge IA – Aspiration Maisons-Alfort | `concierge-ia-aspiration-maisons-alfort.json` | **Complet.** Scrape (Django) → save-content → push-to-flowise. Utiliser `http://web:8000` si n8n et Django sont dans le même Docker. Voir **`docs/base-de-connaissances/guide-equipe-scraper-n8n-flowise.md`** pour faire fonctionner la chaîne. |

---

## Comment exporter un workflow depuis n8n

1. Dans n8n : ouvrir le workflow → menu (⋯) → **Download** ou **Export**.
2. Enregistrer le fichier JSON dans ce dossier avec un nom explicite.
3. Mettre à jour ce README avec le nom du fichier et une courte description.

---

*Dossier créé pour le Quick Win Concierge IA et les futurs workflows n8n documentés.*
