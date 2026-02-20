# Promovacances — PPP (candidature)

Landing **rapport complet** pour la société Promovacances (tourisme / vacances).

**Modèle de référence** : ce projet sert de **base de départ** pour les futures landings similaires. Voir `docs/base-de-connaissances/template-landing-promovacances-base-depart.md`.

## Créer la landing en base (une seule fois)

1. **Racine projet** : se placer dans le répertoire LPPP (celui qui contient `Makefile`, `manage.py`, `docker-compose.yml`).
2. **Stack Docker** : si les services ne tournent pas, lancer le stack puis créer la landing :

   ```bash
   make landing-promovacances-full
   ```
   (Enchaîne `make start` puis `make landing-promovacances`.)

   Si le stack est déjà démarré :

   ```bash
   make landing-promovacances
   ```

Procédure coordonnée (Chef de Projet, DevOps, Architecte, Ingénieur Sys) :  
`docs/base-de-connaissances/segmentations/2026-02-19-landing-promovacances-creation-coordonnee.md`

## Repo landing (LPPP_promovacances)

| Plateforme | URL |
|------------|-----|
| **GitHub** | `https://github.com/LucasTymen/LPPP_promovacances` (principal) |
| **GitLab** | `https://gitlab.com/LucasTymen/lppp_promovacances` (miroir) |
| **Vercel** | Projet **lppp-promovacances** (tiret) lié au repo GitHub. 1 repo = 1 projet. |

**Push** : `deploy/push-promovacances.ps1` ou voir `deploy/PUSH-PROMOVACANCES.md`. Ne jamais pousser `node_modules` (déjà dans `.gitignore` racine).

## URLs

| URL | Rôle |
|-----|------|
| `/p/promovacances/` | Page proposition (hero, intro, CTA vers dashboard). |
| `/p/promovacances/audit-dashboard/` | Dashboard audit SEO (score, timeline, compteur perte, bullet, waterfall, recovery). |

## Dashboard audit SEO

- **Données** : `audit-dashboard.json` (structure identique au modèle Casapy, contenu adapté tourisme).

Les chiffres du JSON (TTFB, LCP, score, scénarios, pertes estimées, recovery rings) sont des **valeurs de démonstration**. Remplacer par les données réelles de l’audit une fois les mesures effectuées.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `audit-dashboard.json` | Contenu du dashboard (titres, score, timeline, scénarios, bullet, waterfall, recovery). |
| `landing-proposition-promovacances.json` | Contenu de la page proposition (hero, intro, CTA, lien dashboard). |
| `spec-infographiques-visuel-contextuel-promovacances.md` | Spec pour graphiste : data + contexte court pour chaque bloc (jauges, chaîne priorité, scénarios, plan). |
| `promovacances-marketing-study-en.md` | Marketing study (EN) : SEO perf + paid media (Google Ads, Meta), version étude. |
| `positionnement-marketing.html` | Onglet « Positionnement marketing » : résumé situation + étude paid media (Google, Meta). |
| `analyse-marketing-paid-media.md` | Synthèse paid media (FR). |
| `README.md` | Ce fichier. |

Voir `docs/base-de-connaissances/audit-dashboard-modele-seo.md` pour la structure complète du JSON et la marche à suivre.
