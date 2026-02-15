# Audit SEO FitClem (fitclem.fr) — Données du crawl

**Date du crawl** : 2026-02-15  
**Outil** : Screaming Frog SEO Spider 23.2 + Lighthouse (export JSON/HTML).  
**Cible** : https://fitclem.fr/

---

## Fichiers déposés

| Fichier | Description |
|---------|-------------|
| `fitclem.fr-20260215T191020.json` | Export **Lighthouse** (performance, accessibilité, bonnes pratiques, SEO) — métriques FCP, LCP, Speed Index, etc. |
| `fitclem.fr-20260215T191020.html` | Rapport **Lighthouse** au format HTML (consultation visuelle). |
| `SEO_FitClem_indexabilité.csv` | **Indexabilité** par segment d’URL (interne : 439 total, 300 indexables, 139 non indexables ; répartition cdn/, collections/, blogs/, products/, pages/, policies/, etc.). |
| `SEO_FitClem_temps_de_réponse_(en_secondes).csv` | **Temps de réponse** : répartition (0–1 s : 96,76 %, 1–2 s : 3,01 %, 2–3 s : 0,23 %). |
| `SEO_FitClem_url_contient_une_espace.csv` | URLs contenant une **espace** (encodage, risque) — ex. `cliniquement prouvé (2).png` (429 Too Many Requests). |
| `SEO_FitClem_images_attribut_alt_manquant.csv` | Images sans **attribut** `alt` (à corriger pour accessibilité et SEO). |
| `SEO_FitClem_images_texte_alt_manquant.csv` | Images avec attribut `alt` **vide** ou texte alt manquant (à renseigner). |
| `SEO_FitClem_h1_manquant.csv` | Pages **sans H1** (collections, pages rewards, à propos, etc.) — à corriger pour SEO et accessibilité. |
| `SEO_FitClem_pagination_l_url_de_pagination_ne_figure_pas_dans_la_balise_d_ancrage.csv` | **Pagination** : URL rel="next"/rel="prev" non présentes dans un lien `<a>` (à corriger pour crawl et PageRank). |
| `SEO_FitClem_codes_de_réponse_internes,_erreur_du_client_(4xx).csv` | **Erreurs 4xx** (84 URL) : 404, 429, etc. — liens à mettre à jour, rediriger ou supprimer. |
| `SEO_FitClem_rapport_aperçu_problemes.csv` | **Aperçu des problèmes** Screaming Frog : liste des types (4xx, H1 manquant, meta description, images, canoniques, sécurité, etc.) avec priorité et description. |
| `SEO_FitClem_interne_tous.csv` | **Toutes les URL internes** crawlées (Adresse, Type, Code HTTP, Title, Meta, H1, H2, indexabilité, temps de réponse, etc.). |

---

## Synthèse rapide (d’après le crawl)

- **500 URL** rencontrées ; **488 crawlées** (97,6 %) ; **432 internes** ; **300 indexables** (68,34 % des internes), **139 non indexables**.
- **7 URL internes** bloquées par robots.txt ; **5 externes** bloquées.
- **Temps de réponse** : majorité 0–1 s (96,76 %), quelques URLs 1–2 s.
- **Problèmes identifiés** : URL avec espace (429) ; images sans alt / alt vide ; **10 pages sans H1** (collections, rewards, à propos…) ; **84 URL en erreur 4xx** ; pagination (rel next/prev hors balise d’ancrage) ; meta descriptions manquantes ou trop longues ; titres trop longs/courts ; éléments HTML non valides dans `<head>` ; en-têtes sécurité (CSP, X-Frame-Options, Referrer-Policy). Voir `SEO_FitClem_rapport_aperçu_problemes.csv` pour la liste complète.

---

**Synthèse business (manque à gagner)** : voir **`../rapport-seo-fitclem-manque-a-gagner.md`** — estimation du coût des erreurs 4xx, de la lenteur et du SEO non capté (132–324 k€/an), argument pour l’entretien et pour la page « Étude SEO » de la landing.

*Ces données alimentent la page « Étude SEO » de la landing FitClem. Référence : `docs/contacts/fitclem/README.md`, sprint `segmentations/2026-02-09-sprint-general-fitclem-landing-multipage.md`.*
