# Promovacances — Avis Expert SEO et équipe technique

**Contexte** : remplacer le contenu template de la landing Promovacances par les **données réelles** issues du probing et de la doc (diagnostic TTFB, stack, rapports).

**Sources** : `PROMOVACANCES_DIAGNOSTIC_20260219.md`, `PROMOVACANCES_TTFB_DIAGNOSTIC_SECTION.md`, rapports SEO (Screaming Frog, PageSpeed, etc.) dans `docs/contacts/promovacances/`.

---

## 1. Avis Expert SEO

### Cohérence données / message

- Le **template actuel** indique un TTFB Homepage **2,1 s** (« à améliorer ») et positionne le **serveur & cache** comme principal levier (55 % du recovery). Les chiffres du **diagnostic réel** montrent un **TTFB médian ~0,10 s (100 ms)** et une stack **Fasterize + CloudFront** : le serveur est **déjà réactif**.
- **Risque** : si on laisse les chiffres démo en production, la landing devient **contradictoire** avec les faits et peut nuire à la crédibilité en entretien (le prospect ou le recruteur peut vérifier).
- **Recommandation** : **remplacer** les valeurs template par les données réelles :
  - **TTFB** : **~0,10 s** (100 ms), avec la conclusion « serveur OK ».
  - **Stack** : Fasterize + CloudFront, origine non exposée (backend non déterminable).
  - **Narrative** : « En cas de lenteur perçue, suspect n°1 = **front-end** (LCP, JS, images) », pas le serveur. Ajuster les **recovery rings** : priorité aux leviers **images & LCP** et **JS & third-parties**, serveur en levier marginal.
- **Quantification** : les scénarios « manque à gagner » restent **à recalibrer avec les données client** (trafic, CVR, panier). On peut garder un exemple chiffré (ex. 28 k€/mois) comme **ordre de grandeur** en précisant « à ajuster avec vos données GA4 / Search Console ».

### SEO / crédibilité

- Une landing qui affiche des **métriques alignées sur un vrai audit** renforce le positionnement « audit SEO / perf » et évite toute ambiguïté sur l’origine des chiffres (probing réel vs démo).

---

## 2. Avis équipe technique (Dev Django / DevOps)

### Données à injecter

- **Landing** : `docs/contacts/promovacances/landing-proposition-promovacances.json` — champs à mettre à jour avec les valeurs du diagnostic (TTFB, stack, conclusion). Pas d’invention : uniquement les valeurs documentées dans `PROMOVACANCES_DIAGNOSTIC_20260219.md` et `PROMOVACANCES_TTFB_DIAGNOSTIC_SECTION.md`.
- **Dashboard** : `docs/contacts/promovacances/audit-dashboard.json` — même logique : TTFB réel (**0,1 s**), timeline et waterfall cohérentes, recovery rings rééquilibrés (front > serveur). Structure JSON inchangée (compatibilité template `seo_audit_dashboard.html`).

### Procédure

1. Mise à jour des deux JSON avec les données réelles.
2. Rechargement en base : `make landing-promovacances` ou `python manage.py create_landing_promovacances --update --publish` pour que la landing reflète le nouveau `content_json`.
3. Aucun changement de code (vues, templates) : seul le **contenu** des JSON est modifié.

### Références

- Vue landing : `apps/landing_pages/views.py` (chargement `landing-proposition-<slug>.json` ou `content_json`).
- Vue dashboard : `seo_audit_dashboard(request, slug)` charge `docs/contacts/<slug>/audit-dashboard.json`.
- Modèle dashboard : `docs/base-de-connaissances/audit-dashboard-modele-seo.md`, `docs/contacts/casapy/audit-dashboard.json`.

---

## 3. Synthèse

| Élément | Template (avant) | Données réelles (après) |
|--------|-------------------|--------------------------|
| TTFB Homepage | 2,1 s (à améliorer) | **~0,10 s** (100 ms) — serveur OK |
| Principal levier | Serveur & cache (55 %) | **Front** : images & LCP, JS & third-parties |
| Stack visible | — | Fasterize + CloudFront, origine non exposée |
| Scénarios manque à gagner | Démo 28 k€/mois | Conserver ordre de grandeur + « à recalibrer avec vos données » |

**Action** : appliquer les mises à jour ci-dessous dans `landing-proposition-promovacances.json` et `audit-dashboard.json`, puis exécuter `create_landing_promovacances --update --publish`.
