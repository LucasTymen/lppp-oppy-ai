# Template Positionnement marketing — page dédiée

**Objectif** : Réutiliser la structure et le contenu de la page « Positionnement marketing » Promovacances comme **modèle canonique** pour les futures pages similaires (étude paid media, Google Ads, Meta, formule CA, etc.).

**Contexte** : Fait partie du **modèle global Promovacances** — l’ensemble du projet (`docs/contacts/promovacances/` + `deploy/static-promovacances-vercel/`) sert de **base de départ** pour gagner du temps. Voir `template-landing-promovacances-base-depart.md`.

---

## 1. Modèle canonique

**Fichier de référence** : `docs/contacts/promovacances/positionnement-marketing.html`

Cette page complète et enrichie devient le **nouveau modèle** pour les pages de positionnement / étude marketing :
- Structure (nav, site-bg-fixed, vidéo fond, site-content, cards)
- Sections : Situation, Formules et ordres de grandeur, Google Ads, Meta, Bar chart âge, Sources
- Formules mathématiques (blocs `.formula-block`), diagrammes de flux (`.flow-diagram`), graphiques (`.bar-chart`)
- Palette et tokens CSS (`promovacances_style_tokens.css` adaptables par contact)

---

## 2. Contenu type

| Section | Contenu |
|---------|---------|
| **Situation** | Contexte entreprise, stack technique, paid media (canaux, volume) |
| **Formules** | CA = Visites × CVR × AOV ; perte de ventes ; ordre de grandeur |
| **Google Ads** | Thèmes, impressions, périodes (sources transparence Google) |
| **Meta** | Annonceur, régions, types d’annonces (Meta Ad Library) |
| **Graphiques** | Bar chart répartition âge, flow diagrams |
| **Sources** | Liens vers Google Ads Transparency, Meta Ad Library |

---

## 3. Appliquer aux autres landings

1. **Copier** la structure de `docs/contacts/promovacances/positionnement-marketing.html`.
2. **Remplacer** le contenu par les données du contact (prospect).
3. **Adapter** les tokens CSS (couleurs, polices) selon la charte du contact.
4. **Garder** : nav sticky, site-bg (vidéo/overlay), layout cards, formules, tableaux, bar charts.
5. **Checklist intégrité nav** (Chef de Projet / Architecte supervisent, Graphiste exécute) : `body { padding-top: 0 }` (jamais 60px), nav collée en haut ; `.site-content-inner` ou `main` avec `padding-top` pour le contenu sous la nav. Voir `erreurs-et-solutions.md` § « Barre de navigation décalée ».
5. Pour FitClem, futures landings Growth : s’inspirer de ce modèle pour la page « Étude marketing ».

---

## 4. Fichiers à aligner

- **Modèle** : `docs/contacts/promovacances/positionnement-marketing.html`
- **Export statique** : `deploy/static-promovacances-vercel/positionnement-marketing.html`
- **Style tokens** : `docs/contacts/promovacances/promovacances_style_tokens.css`
- **Doc étude marketing** : `etude-marketing-page-onglet-dedie.md`

---

*Modèle établi 2026-01-30. La page Promovacances enrichie (chiffres, formules, infographies) devient la référence pour les futures pages positionnement marketing.*
