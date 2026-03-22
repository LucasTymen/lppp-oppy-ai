# LPPP-OppyAI — OPPORTUNITY (Oppy.ai)

**Slug URL** : `lppp-oppy-ai` → `/p/lppp-oppy-ai/`

**Contenu** : étude stratégique **Growth & Acquisition** + **trame SEO technique & sémantique** pour **oppy.ai** (JSON + markdown détaillé ; métriques crawl / GSC / PageSpeed à remplir après mesures). Gabarit Django : `proposition.html`.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `etude-oppy-ai-source.md` | Source documentaire (copie de travail de l’étude). |
| `seo-technique-semantique-oppy-ai.md` | Trame SEO (grilles, piliers) — à compléter. |
| `SEO Semantique.md` | Audit sémantique oppy.ai (marque, H1, métadonnées, E-E-A-T, clusters). |
| `SEO Technique.md` | Écosystème URLs (oppy.ai, oppycx, allmysms, API, RCS), références. |
| `rapport seo complet.md` | Audit consolidé : TTFB, cache, fragmentation, pertes, plan P0/P1/P2. |
| `landing-proposition-lppp-oppy-ai.json` | Contenu landing (`seo_technique_semantique`, `expertise_stack`, etc.). |
| `audit-dashboard.json` | Dashboard `/p/lppp-oppy-ai/audit-dashboard/` (lecture **stratégique** GAM ; audit SEO terrain = option futur JSON type Infopro). |
| `infographie-lppp-oppy-ai-7-formats.html` | Synthèse visuelle / sections exportables (SWOT, funnel, concurrents). |
| `positionnement-marketing.html` | Positionnement B2B grands comptes & différenciation CIM. |

## Django / admin

- **Fallback** : si aucune `LandingPage` en base, chargement du JSON `landing-proposition-lppp-oppy-ai.json`.
- **Admin** : créer une entrée avec `slug=lppp-oppy-ai`, `template_key=proposition`.

## Déploiement statique (optionnel)

Voir la doc déploiement du projet pour exporter une version statique si besoin.
