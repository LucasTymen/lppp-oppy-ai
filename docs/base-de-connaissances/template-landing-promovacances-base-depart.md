# Template landing Promovacances — base de départ

**Objectif** : Pour gagner du temps, **l’ensemble du projet et des pages** Promovacances sert de **base de départ** pour les futures landings similaires (audit SEO, paid media, dashboard, infographie, positionnement marketing).

---

## 1. Périmètre du modèle

**Dossier contact** : `docs/contacts/promovacances/`  
**Export statique** : `deploy/static-promovacances-vercel/`  
**Push / déploiement** : `deploy/PUSH-PROMOVACANCES.md`

### Pages et fichiers

| Élément | Fichier(s) | Rôle |
|---------|------------|------|
| Proposition | `index.html`, `landing-proposition-promovacances.json` | Hero vidéo, chiffres clés, enjeux, solution, services, CTA |
| Rapport | `rapport.html` | Synthèse rapport, contenu Markdown exporté |
| Infographie | `infographie-promovacances-7-formats.html` | 7 formats, speedo, ring, heatmap |
| Positionnement marketing | `positionnement-marketing.html` | Situation, formules, Google Ads, Meta, bar charts |
| Dashboard audit | `audit-dashboard.json` | Score, timeline, scénarios, bullet, waterfall, recovery |
| Style | `promovacances_style_tokens.css` | Palette, site-bg-fixed, vidéo, overlay |
| Config Vercel | `vercel.json` | Rewrites URLs, 404 |

---

## 2. Structure à réutiliser

- **Nav** : sticky, burger mobile (waffle), liens internes sans `target="_blank"` (éviter blocage YouTube)
- **Layout** : site-bg-fixed, site-bg-video, site-bg-overlay, site-content
- **Pages annexes** : rapport, infographie, positionnement-marketing — navigation même fenêtre
- **Export** : `export_landing_static promovacances` → `deploy/static-promovacances-vercel/`

---

## 3. Exemple : Infopro Digital (lppp-infopro)

Projet créé sur le modèle Promovacances : `docs/contacts/infopro/`, `deploy/static-infopro-vercel/`, commande `create_landing_infopro`, `PUSH-INFOPRO.md`. Voir `docs/contacts/infopro/README.md`.

---

## 4. Procédure pour un nouveau contact

1. **Copier** le dossier `docs/contacts/promovacances/` ou `docs/contacts/infopro/` → `docs/contacts/<slug>/`
2. **Adapter** : JSON, HTML, tokens CSS (couleurs, polices), contenu (chiffres, textes)
3. **Renommer** les fichiers (ex. `infographie-<slug>-7-formats.html`, `infopro_style_tokens.css` → `<slug>_style_tokens.css`)
4. **Créer** la commande `create_landing_<slug>` (copier `create_landing_infopro.py`)
5. **Adapter** `export_landing_static.py` : slug, patterns de copie, URLs
6. **Exporter** : `python manage.py export_landing_static <slug> --json ... --output ... --rapport-md ...`
7. **Déployer** : repo dédié (GitHub/GitLab) + projet Vercel, sur le modèle `PUSH-PROMOVACANCES.md` ou `PUSH-INFOPRO.md`

---

## 5. Fichiers de référence

- **Contact** : `docs/contacts/promovacances/` (tous les fichiers)
- **Export** : `deploy/static-promovacances-vercel/`
- **Template proposition** : `templates/landing_pages/proposition.html` (Django)
- **Commande export** : `apps/landing_pages/management/commands/export_landing_static.py`
- **Push** : `deploy/PUSH-PROMOVACANCES.md`, `deploy/PUSH-INFOPRO.md`

---

*Base de départ établie 2026-01-30. Promovacances = référence complète pour les futures landings audit SEO + paid media.*
