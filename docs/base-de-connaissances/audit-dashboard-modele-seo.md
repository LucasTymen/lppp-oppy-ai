# Dashboard audit SEO — Modèle réutilisable

**Objectif** : réutiliser la même structure de dashboard (navbar sticky, speedometer, timeline, compteur perte, bullet chart, heatmap, waterfall, recovery rings) pour **plusieurs projets SEO**. On garde la structure et les données type ; **seul le contenu à afficher change** (titres, chiffres, scénarios, libellés).

**Chef de Projet** : ce document décrit comment dupliquer le modèle pour 2 autres projets (ou plus).

---

## Solution pratique : 1 template + 1 JSON par projet

- **Un seul template** : `templates/landing_pages/seo_audit_dashboard.html` (structure identique, données injectées).
- **Un fichier JSON par projet** : `docs/contacts/<slug>/audit-dashboard.json`. Tu remplaces uniquement le contenu de ce fichier (titres, score, TTFB, LCP, scénarios, libellés, etc.).
- **Une seule URL** : `/p/<slug>/audit-dashboard/` — dès qu’un fichier `audit-dashboard.json` existe pour le slug, le dashboard s’affiche avec ces données.

**Pour un 2e ou 3e projet** :
1. Créer le dossier contact : `docs/contacts/<nouveau_slug>/`.
2. Copier `docs/contacts/casapy/audit-dashboard.json` vers `docs/contacts/<nouveau_slug>/audit-dashboard.json`.
3. Remplacer dans ce JSON : `title_page`, `label_tag`, `title`, `title_accent`, `header_meta`, `status_label`, `score`, `speedo_note`, sections, `timeline_markers`, `scenarios`, `bullet_metrics`, `waterfall_resources`, `recovery_rings`. Tu peux me donner le contenu et je l’intègre, ou éditer le JSON toi-même.
4. Aucun changement de code : la vue charge le JSON pour ce slug et rend le même template.

**Référence** : le JSON Casapy est le modèle : `docs/contacts/casapy/audit-dashboard.json`. Sa structure définit les champs attendus (voir ci‑dessous).

---

## Structure du JSON (champs à remplacer)

| Bloc | Champs principaux |
|------|-------------------|
| **En-tête** | `title_page`, `label_tag`, `title`, `title_accent`, `header_meta`, `status_label` |
| **Score** | `score`, `speedo_note`, `speedo_note_strong`, `section1_sub` |
| **Sections** | `section2_sub`, `section3_sub`, `loss_monthly_label`, `loss_annual_label` |
| **Timeline** | `timeline_max_t`, `timeline_markers` (t, label, event, desc, color) |
| **Scénarios perte** | `scenarios` (visits, cvr, aov, label) |
| **Bullet chart** | `bullet_metrics` (name, unit, current, target, industry, max, bad, warn, ok, color) |
| **Waterfall** | `waterfall_max_t`, `waterfall_resources` (label, start, dur, color, tag) |
| **Recovery rings** | `recovery_rings` (pct, label, color, sub) |

La **matrice Impact × Effort** (heatmap) reste pour l’instant en dur dans le template (quick wins, stratégique, si temps, éviter). Si tu veux la rendre configurable plus tard, on pourra ajouter un bloc `matrix` dans le JSON.

---

## Navbar sticky

La barre d’en-tête du dashboard est en **sticky-top** : elle reste visible en haut au scroll. C’est déjà en place dans le template.

---

## Fichiers concernés

| Fichier | Rôle |
|---------|------|
| `templates/landing_pages/casapy_audit_dashboard.html` | Copie de référence (données en dur) ; la version en production pour Casapy est servie par le template générique + JSON. |
| `templates/landing_pages/seo_audit_dashboard.html` | Template générique utilisé pour tous les projets (données injectées depuis `audit-dashboard.json`). |
| `docs/contacts/<slug>/audit-dashboard.json` | Données du dashboard pour ce projet. |
| `apps/landing_pages/views.py` | Vue `seo_audit_dashboard(request, slug)` qui charge le JSON et rend le template. |
| `apps/landing_pages/urls.py` | Route `p/<slug:slug>/audit-dashboard/`. |

---

*Modèle défini pour réutilisation sur 2 autres projets SEO. Dernière mise à jour : 2026-01-30.*
