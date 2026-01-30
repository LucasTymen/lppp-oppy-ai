# Intelligence métier et algorithmes LPPP

Document de référence pour le **matching**, le **scoring**, le **filtrage** et la **qualité des données**, afin d’adapter les contenus rédigés (landing pages) et les stratégies de prospection. Les algorithmes sont centralisés dans l’app `apps.intelligence` et réutilisables partout (campaigns, landing_pages, scraping).

**Spec canonique des formules** : pour les **formules mathématiques et algorithmes explicites** (score prospect, complétude, matching, normalisation), voir **`formules-et-algorithmes-reference.md`**. Ce document décrit où brancher les algorithmes et la stratégie d’implantation ; le Data Analyst et le Dev Django s’inspirent du doc de référence pour implémenter sans réinventer.

---

## 1. Sources des algorithmes

| Source | Contenu | Usage LPPP |
|--------|--------|------------|
| **SquidResearch** | `apps/campaigns/nodes/data_nodes.py` : `_safe_eval_expression` (évaluation d’expressions mathématiques sécurisées), noeud ENRICHED. Référence idFinder (tests) si module présent. | Scoring configurable (formules type `score = min(100, email_score + company_score)`), pipelines d’enrichissement. |
| **LPPP** | `apps.intelligence` : scoring, qualité données, matching. | Partout où il faut noter, filtrer ou faire correspondre prospects / landing / contenus. |

SquidResearch est une référence externe (chemin documenté dans `sources.md`). Aucun credential ; code utile copié ou adapté dans LPPP.

---

## 2. Où brancher les algorithmes

| Zone | Besoin | Module / point d’entrée |
|------|--------|--------------------------|
| **Campagnes / prospects** | Score de qualité prospect, tri, filtrage par seuil. | `intelligence.scoring.score_prospect()`, `intelligence.quality.prospect_completeness()` |
| **Nodes (pipelines)** | Enrichissement, calcul de score dans le payload. | `campaigns.nodes.data_nodes` utilise `intelligence.scoring` et `intelligence.quality` |
| **Landing pages** | Adapter le contenu au prospect (nom, entreprise, score). Choisir template ou variante. | `intelligence.matching.best_landing_for_prospect()`, champs `content_json` alimentés selon qualité |
| **Scraping / ENRICHED** | Qualité des données enrichies, déduplication, normalisation. | `intelligence.quality.normalize_company_name()`, `intelligence.matching` |
| **Admin / rapports** | Listes filtrées, colonnes score, alertes qualité. | Filtres Django basés sur champs calculés ou méthodes `intelligence.*` |

---

## 3. Scoring

- **Formules configurables** : expressions mathématiques sécurisées (`safe_eval`) avec variables (ex. `email_score`, `company_score`, `has_contact`). Plage typique 0–100.
- **Score prospect** : combinaison de complétude (email, contact, company, enriched_data) et optionnellement règles métier (secteur, taille, etc.).
- **Score et contenu** : seuils pour décider quelle variante de texte ou quel niveau de personnalisation afficher (ex. si score &gt; 80 → message très personnalisé, sinon → message générique).

---

## 4. Qualité des données

- **Complétude prospect** : définition et sortie de `prospect_completeness` → **`formules-et-algorithmes-reference.md`** (§ 3). Champs obligatoires / optionnels par entité (Prospect, LandingPage).
- **Normalisation** : email (regex), nom entreprise (NFD, suppression accents), nom contact (trim, collapse espaces) → **`formules-et-algorithmes-reference.md`** (§ 4).
- **Cohérence** : pas de doublons critères choisis (ex. campaign + email).
- **Enriched_data** : structure attendue documentée ; champs manquants ou invalides dégradent le score ou déclenchent des alertes.

Les résultats de qualité alimentent le scoring et les stratégies d’affichage (contenus rédigés).

---

## 5. Matching

- **Prospect ↔ Landing page** : une landing peut être liée à un prospect (FK). Le matching peut proposer la « meilleure » landing pour un prospect (déjà liée, ou par campagne/template/score).
- **Normalisation** : noms d’entreprise et de contact pour comparaison, déduplication et recherche (lower, strip, suppression d’accents optionnelle).
- **Filtrage** : exclusion ou priorisation par score, statut campagne, qualité email, etc.

---

## 6. Stratégie d’implantation

1. **Centraliser** dans `apps.intelligence` : pas de logique de scoring/qualité/matching dupliquée dans les autres apps.
2. **Réutiliser** les mêmes fonctions depuis les nodes, les vues, les tâches Celery et l’admin.
3. **Configurer** les seuils et formules (django.conf ou modèles) pour adapter sans toucher au code.
4. **Documenter** toute nouvelle règle ou formule dans **`formules-et-algorithmes-reference.md`** (spec canonique), puis dans ce fichier si impact sur les points d’entrée ; et dans `decisions.md` si décision de conception.

---

## Références

- **Formules et algorithmes (spec canonique)** : `formules-et-algorithmes-reference.md`
- **Décisions** : `decisions.md`

*Dernière mise à jour : 2025-01-30. Référence : SquidResearch `data_nodes.py` (safe_eval, ENRICHED), structure LPPP.*
