# Infopro Digital — LPPP (lppp-infopro)

Landing **audit SEO** pour la société Infopro Digital (groupe média B2B).

**Modèle** : dupliqué depuis Promovacances. Voir `docs/base-de-connaissances/template-landing-promovacances-base-depart.md`.

## Créer la landing en base

```bash
make landing-infopro
```

Ou si le stack n'est pas démarré :

```bash
make landing-infopro-full
```

## Export statique (Vercel)

```bash
python manage.py export_landing_static infopro --json docs/contacts/infopro/landing-proposition-infopro.json --output deploy/static-infopro-vercel/index.html --rapport-md docs/contacts/infopro/rapport-complet-infopro.md
```

## Déploiement Vercel (repo général)

| Paramètre | Valeur |
|-----------|--------|
| **Repo** | `landingPageCreatorForProspection` (pas de repo dédié) |
| **Root Directory** | `deploy/static-infopro-vercel` |
| **Vercel** | Projet **lppp-infopro** → https://lppp-infopro.vercel.app |

Procédure : `deploy/PUSH-INFOPRO.md`

## Fichiers

| Fichier | Rôle |
|---------|------|
| `rapport-complet-infopro.md` | Rapport complet (société, stratégie, SEO, marketing) |
| `audit-dashboard.json` | Dashboard (score, timeline, scénarios, bullet, waterfall, recovery) |
| `landing-proposition-infopro.json` | Page proposition |
| `hero-infopro.mp4` | Vidéo fond hero (muted, loop, autoplay) |
| `positionnement-marketing.html` | Page positionnement / étude paid media |
| `infographie-infopro-7-formats.html` | 7 formats infographiques |
| `infopro_style_tokens.css` | Palette, layout site-bg |
