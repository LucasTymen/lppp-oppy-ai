# Casapy — Intégration infographies : validation (Ingénieur système + Chef de projet)

**Date** : 2026-02-19  
**Contexte** : Appliquer et valider la chaîne complète (localhost, export statique, Vercel) pour un affichage limpide et universel (Firefox, Chrome, Safari, mobile, Apple).

---

## Checklist Ingénieur système

| Point | Statut | Détail |
|-------|--------|--------|
| **Serving assets localhost** | OK | Route `/p/casapy/assets/<filename>` ; vue `serve_casapy_asset` sert les PNG depuis `docs/contacts/casapy/` ; Content-Type `image/png` ; pas de path traversal. |
| **Template : URL des images** | OK | Si `content.casapy_assets_url` présent (Django) → URL absolue vers assets ; sinon (export statique) → `seg.src` relatif. |
| **Export statique** | OK | `export_landing_static casapy --json ... --output deploy/LPPP-Casapy/index.html` recopie tous les PNG (slide*.png, one-pager, casapy-wave, infographie*.html). |
| **Dossier deploy/LPPP-Casapy** | OK | 9 PNG + index.html + rapport.html + vercel.json ; prêt pour push vers GitHub/GitLab puis déploiement Vercel. |
| **Pas de débordement horizontal** | OK | `main#top` overflow-x: hidden ; images `max-width: 100%` ; conteneurs `width: 100%`, `min-width: 0`. |

---

## Checklist Chef de projet

| Point | Statut | Détail |
|-------|--------|--------|
| **Scope** | OK | Infographies 7 slides + one-pager + wave ; contraste fond sombre (texte blanc, accents jaune/orangé/turquoise) ; So what bas droite. |
| **Affichage universel** | OK | CSS : `display: block`, `object-fit: contain`, `decoding="async"` ; media query mobile ; `.services-segment-infographic` et `.services-segments` sans overflow qui coupe. |
| **Procédure déploiement** | OK | `deploy/PUSH-CASAPY.md` : étape 1 = régénérer l’export ; étape 3 = push `deploy/LPPP-Casapy` (origin + gitlab). Localhost = Django sert les assets sous `/p/casapy/assets/`. |
| **Documentation** | OK | README Casapy, notes-infographie-necessaires.md, spec-deck-casapy-7-slides.md à jour. |

---

## Commande à lancer après modif (rappels)

```bash
# 1. Régénérer les visuels (si modif script ou spec)
python scripts/generate_visuels_casapy.py --output docs/contacts/casapy

# 2. Régénérer l’export statique (si modif template, JSON ou visuels)
python manage.py export_landing_static casapy --json docs/contacts/casapy/landing-proposition-casapy.json --output deploy/LPPP-Casapy/index.html --rapport-md docs/contacts/casapy/rapport-complet-casapy.md

# 3. Pour voir sur Vercel : push deploy/LPPP-Casapy (voir PUSH-CASAPY.md)
```

---

*Validation conjointe Graphiste (CSS, intégration) + Ingénieur système (serving, export, deploy) + Chef de projet (scope, doc).*
