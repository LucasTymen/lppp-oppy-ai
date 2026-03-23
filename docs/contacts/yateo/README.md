# YATEO — LPPP (landing growth B2B)

**Société** : YATEO — consacrée au **growth B2B**.  
**Objectif** : nouvelle landing page pour prospecter YATEO en mettant en avant le savoir-faire acquisition, automatisation, SEO et data.

## Contexte

- Secteur : growth B2B (acquisition, leads, funnel, data).
- Angle à définir : audit SEO, automatisation prospection, pipeline leads, reporting, etc. — à préciser selon l’offre / le besoin YATEO.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `landing-proposition-yateo.json` | Contenu de la page proposition (hero, intro, enjeux, CTA, coordonnées). |
| `README.md` | Ce fichier. |

## Accès à la landing

La page est servie **en fallback** depuis le JSON (pas de landing en base ni de thème dédié pour l’instant) : **http://localhost:8010/p/yateo/**

## Export statique (quand la landing est prête)

```bash
python3 manage.py export_landing_static yateo --json docs/contacts/yateo/landing-proposition-yateo.json --output deploy/static-yateo-vercel/index.html
```

## Références

- Template de départ : `docs/base-de-connaissances/template-landing-promovacances-base-depart.md`
- Savoir-faire (arguments, preuves) : `docs/ressources-utilisateur/cv_base_datas_pour_candidatures.json` — piocher pour justifier le profil growth B2B.
