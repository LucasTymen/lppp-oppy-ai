# Notes nécessaires pour l'infographie Casapy

**Objectif** : n’utiliser que les ressources nécessaires pour l’infographie / les visuels Casapy. Éviter de charger tout le projet.

---

## Ressources indispensables (infographie)

| Fichier | Usage |
|---------|-------|
| `landing-proposition-casapy.json` | Contenu (enjeux, segments infographiques, `visual`, `src` des images). |
| `brief-visuels-enjeux-casapy-slides.md` | Brief pour les slides (messages, layout, chiffres). |
| `spec-deck-casapy-7-slides.md` | Spec exécutable 7 slides + one-pager (contenu, visuel, So what, Wave, icônes). |
| `segmentations/2026-01-30-casapy-deck-7-slides-infographiste-redacteur.md` | Segmentation Infographiste + Rédacteur pour ce deck. |
| `slide1-impact-perf-business.png` | Chaîne cause → effet (So what 54k€). |
| `slide2-waterfall-ttfb.png` | Waterfall TTFB (goulot serveur). |
| `slide3-hebergement-comparatif.png` | Mutualisé vs stack adaptée. |
| `slide4-plan-priorise.png` | Plan 1-2-3 serveur → DB → front. |
| `slide5-scenarios-cout.png` | 3 cartes 27k / 54k / 180k. |
| `slide6-fact-hypothesis.png` | FACT vs HYPOTHESIS marketing. |
| `slide4-matrice-seo-timeline.png` | Matrice SEO + timeline 30/60/90. |
| `one-pager-dashboard-casapy.png` | Dashboard exécutif (5 blocs). |
| `casapy-wave-progression.png` | Wave TTFB avant/après fix (J0). |
| `scripts/generate_visuels_casapy.py` | Régénération des visuels (Matplotlib). |

---

## Optionnels (contexte)

| Fichier | Usage |
|---------|-------|
| `rapport-complet-casapy.md` | Rapport complet (optionnel pour export). |
| `SEO_Casapy_rapport_performances_et_diagnostique.md` | Données techniques source. |
| `infographie-audit-seo-casapy.html` | Infographie SEO (référence). |
| `infographie-funnel-positionnement-casapy.html` | Infographie funnel (référence). |

---

## À ne pas charger / générer

- **node_modules** : jamais à la racine ; uniquement dans `deploy/standalone-*` si besoin.
- **Tous les nodes** : ne pas tout générer — uniquement ce qui est demandé.
- Fichiers volumineux ou crawl non nécessaires (ex. `www.casapy.com-*.json` si pas utilisé).

---

*Réf. `regle-jamais-generer-tous-les-nodes.md`, `brief-visuels-enjeux-casapy-slides.md`.*
