# Casapy — Deck 7 slides + one-pager : illustration + recontextualisation

**Date** : 2026-01-30  
**Demandeur** : utilisateur  
**Statut** : 🟢 À exécuter

---

## Contexte

Suite aux infographies déjà livrées (même approche, fond transparent), l’utilisateur souhaite **illustrer** les parties du deck selon la spec consultant-grade (7 slides + 1 one-pager) et **recontextualiser** avec un texte court et synthétique pour qu’un lecteur non du métier comprenne sans sensation de flou.

- **Spec exécutable** : `docs/contacts/casapy/spec-deck-casapy-7-slides.md` (contenu exact ≤35 mots/slide, visuel recommandé, So what au même endroit, Wave en slide à part).
- **Wave** : par défaut **TTFB/LCP** (axe Y = plus bas = mieux) ; option CVR/CA (plus haut = mieux) documentée dans la spec.

---

## Rôles et missions

| Rôle | Mission | Livrable / critère |
|------|---------|---------------------|
| **Infographiste** | Illustrer les **7 slides + one-pager** avec la **même approche que précédemment** (fond transparent, consultant-grade, style cohérent). Suivre la spec : type de visuel par slide (chaîne cause→effet, waterfall, immeuble vs maison, 3 blocs, 3 cards, split FACT/HYPOTHESIS, sinusoïde Wave). So what au même endroit (bas droite). Icônes cohérentes (serveur, DB, UX, panier, SEO). | Visuels 7 slides + one-pager (PNG/SVG fond transparent) ; Wave avec marqueur « Fix (J0) » si possible. |
| **Rédacteur en chef** | **Texte explicatif très court et synthétique** pour recontextualiser chaque bloc/slide ; éviter la sensation « je ne comprends pas » pour quelqu’un pas du métier. Rester aligné sur le wording de la spec (≤35 mots/slide) tout en clarifiant les notions (TTFB, LCP, mutualisé, etc.) si besoin en légende ou encart. | Textes courts par slide/one-pager ; pas de jargon sans explication minimale. |

---

## Fichiers de référence

- `docs/contacts/casapy/spec-deck-casapy-7-slides.md` — spec exécutable (contenu, visuels, So what, one-pager, icônes, choix Wave).
- `docs/contacts/casapy/brief-visuels-enjeux-casapy-slides.md` — brief visuels (alignement messages).
- `docs/contacts/casapy/notes-infographie-necessaires.md` — ressources indispensables pour l’infographie.
- `scripts/generate_visuels_casapy.py` — régénération Matplotlib (option transparent).

---

## Conseils cabinet (spec)

1. **« Hypothèse / à valider »** à côté de chaque chiffre non issu de GA4.
2. **So what au même endroit** (bas droite) sur toutes les slides.

---

*Segmentation créée suite à demande utilisateur. Infographiste + Rédacteur en chef en charge ; Chef de Projet valide les livrables.*
