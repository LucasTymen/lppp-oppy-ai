# Brief InfographicCraft — Comment solliciter l’agent Infographiste

**Agent** : InfographicCraft (règle `.cursor/rules/infographiste-dataviz.mdc`).  
**Rôle** : Assister le **Chef de Projet** et le **Rédacteur** pour rendre les pages plus dynamiques en résumant les **chiffres clés** par des infographies (un seul fichier HTML autonome, style Pictochart, print-friendly).

---

## Quand le solliciter

- Vous avez un rapport, une étude ou une page avec beaucoup de chiffres et vous voulez une **version infographique** pour la rendre plus lisible et percutante.
- Vous préparez une **landing candidature** ou un **dossier** et souhaitez une infographie (ex. audit SEO, manque à gagner, KPI).
- Vous voulez un **résumé visuel** (TL;DR, KPI cards, timeline, actions) à intégrer ou à exporter en PDF.

---

## Format du brief (variables)

Transmettez à l’agent (dans la demande ou en remplissant les variables) :

| Variable | Exemple | Obligatoire |
|----------|---------|-------------|
| **THEME** | Audit SEO fitclem.fr — Manque à gagner | Oui |
| **AUDIENCE** | Recruteur FitClem / Responsable marketing | Recommandé |
| **TON** | Professionnel, factuel, percutant | Optionnel |
| **SECTIONS** | Contexte, pertes directes, chiffrage, actions prioritaires, argument candidature | Recommandé |
| **DATA** | Chiffres exacts (132–324 k€/an, 84 URL 4xx, Speed Index 10,6 s, etc.) ou renvoi vers un fichier (`rapport-seo-fitclem-manque-a-gagner.md`) | Si vide → « À compléter » |
| **CONSTRAINTS** | Couleurs marque, max 1 page A4 à l’impression, pas de timeline | Optionnel |

---

## Exemple de demande

*« Génère une infographie avec le brief suivant :*  
*THEME : Audit SEO FitClem — manque à gagner et leviers.*  
*AUDIENCE : Recruteur (candidature Responsable Marketing Digital).*  
*TON : Pro, factuel.*  
*SECTIONS : entonnoir percé, 3 pertes (4xx, lenteur, SEO), tableau synthèse k€/an, 3 actions prioritaires, argument candidature.*  
*DATA : voir `docs/contacts/fitclem/rapport-seo-fitclem-manque-a-gagner.md` (chiffres 11–27 k€/mois, 132–324 k€/an, 84 URL 4xx, Speed Index 10,6 s).*  
*CONSTRAINTS : 1 couleur primaire + accent, print-friendly. »*

---

## Sortie attendue de l’agent

1. **Plan court** (6–10 lignes) : structure + composants choisis (header, TL;DR, KPI cards, etc.).
2. **Fichier** `infographie.html` complet (HTML + CSS + JS dans le même fichier), à déposer dans `docs/contacts/<slug>/` ou emplacement indiqué.

---

## Références

- Règle : `.cursor/rules/infographiste-dataviz.mdc`
- Registre : `docs/base-de-connaissances/registre-agents-ressources.md` § Infographiste / Data Viz
