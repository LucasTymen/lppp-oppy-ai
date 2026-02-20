# Sprint — Illustrations Infopro (Math + Graphiste)

**État** : Carte perceptuelle 2D ajoutée (2026-01-30). Radar remplacé par diagramme positionnement concurrentiel.

**Date** : 2026-01-30  
**Pilote** : Chef Marketing & Growth  
**Statut** : 🟡 En cours  
**Contact** : Infopro Digital — `docs/contacts/infopro/`

**Principe** : **Illustrer les textes sans les remplacer**. Les visuels viennent en complément, pas en substitution.

---

## 📐 Types d’illustrations utilisés dans la profession (référence)

### Graphiques de données (Math / Data Analyst)
- **Bar chart horizontal** : comparaisons (concurrents, priorités SEO, poids par catégorie)
- **Bar chart vertical** : répartition, volumes
- **Bullet chart** : valeur actuelle vs cible vs référence (ex. PageSpeed 68 vs 90)
- **Donut / pie** : part de marché, répartition %
- **Funnel visuel** : AAARR avec largeurs décroissantes (acquisition → referral)
- **Waterfall** : cumul, décomposition (déjà présent dans infographie)
- **Heatmap 2×2** : Impact × Effort (déjà présent)
- **Gauge / tachymètre** : score unique (déjà présent)

### Schémas conceptuels (Graphiste)
- **Funnel AAARR** : 5 étages en cascade (visuel, pas juste liste)
- **Matrice SWOT** : 4 quadrants (Forces / Faiblesses | Opportunités / Menaces)
- **PESTEL** : 6 blocs (hexagone ou grille) avec icônes
- **Google vs Meta** : schéma comparatif (2 blocs, flux) — partiel existant
- **Flux / flow** : Acquisition → Activation → Adoption → Revenu → Referral
- **Icônes** : par pilier (Content Factory, Long-tail, GEO)
- **Formule illustrée** : CA = V × CVR × AOV (schéma avec flèches, ex. bloc diagramme)

### Illustrations figuratives (Graphiste ou génération)
- **Métaphore visuelle** : géant B2B au carrefour info/business (carrefour, pont, hub)
- **Personnage / scène** : décideur, ingénieur, acheteur (optionnel, si besoin storytelling)

---

## 🎯 Répartition des tâches

### Math (Expert Maths / chargé chiffres)
**Responsabilité** : graphiques de données, calculs visuels, formules illustrées.

| Priorité | Visuel à produire | Données | Fichier cible |
|----------|-------------------|---------|---------------|
| P1 | **Bar chart** — Problèmes SEO par priorité (Élevée / Moyenne / Faible) | 7 élevés, 2 moyennes, 6 faibles (URLs ou %) | rapport.html, positionnement-marketing |
| P1 | **Donut** — Répartition URLs (337 indexables / 21 non indexables) | 337 vs 21 | rapport.html |
| P2 | **Formule CA illustrée** — schéma bloc : Visites → CVR → AOV → CA | Labels + exemple 30k × 1,5% × 1200€ | positionnement-marketing |
| P2 | **Bullet chart** — Objectifs SMART (actuel vs cible) | +25% Content, 95% SEO, 10 GEO, +10% CTR | positionnement-marketing |
| P3 | **Bar chart** — Perte 28 k€/mois (LostRevenue) vs CA potentiel | 28 k€ / mois | rapport, positionnement |

**Livrables** : SVG ou HTML/CSS intégré dans les pages. Pas de lib externe lourde si possible (CSS + SVG inline).

**⚠️ S’il ne sait pas faire** : préciser quels visuels (ex. donut SVG animé, bullet chart responsive) → question posée à l’utilisateur pour génération par Claude.

---

### Graphiste (Infographiste / Designer)
**Responsabilité** : schémas conceptuels, icônes, funnel visuel, PESTEL, SWOT.

| Priorité | Visuel à produire | Contenu | Fichier cible |
|----------|-------------------|---------|---------------|
| P1 | **Funnel AAARR** — 5 étages en cascade (bords arrondis, couleurs dashboard) | A → Ac → Ad → R → Ref avec labels | positionnement-marketing, rapport |
| P1 | **Matrice SWOT** — 4 quadrants avec bullets courts | Forces, Faiblesses, Opportunités, Menaces | rapport.html, positionnement-marketing |
| P2 | **PESTEL** — 6 blocs (hexagone ou grille 2×3) | P, E, S, T, E, L avec icônes | rapport.html, positionnement-marketing |
| P2 | **Piliers stratégiques** — 3 icônes (Content Factory, Long-tail, GEO) | Icônes + court label | positionnement-marketing |
| P3 | **Google vs Meta** — schéma comparatif enrichi | 2 blocs (Capture vs Génération demande) | Déjà partiel : améliorer si besoin |

**Livrables** : SVG (prioritaire) ou PNG fond transparent. Palette : tokens Infopro (`infopro_style_tokens.css`).

**⚠️ S’il ne sait pas faire** : préciser quels visuels (ex. hexagone PESTEL, funnel SVG) → question posée à l’utilisateur pour génération par Claude.

---

## ❓ Questions à poser à l’utilisateur (génération par Claude)

Si **Math** ou **Graphiste** ne peut pas produire un visuel, formuler une **demande précise** pour génération par Claude, par exemple :

1. **« Donut SVG** — 337 (indexables) vs 21 (non indexables), fond sombre Infopro, couleurs vert/rouge. »
2. **« Funnel AAARR SVG** — 5 étages (Acquisition → Referral), largeurs décroissantes, style dashboard sombre. »
3. **« Matrice SWOT SVG** — 4 quadrants, texte court par case, bordure fine, fond `#0e0e1a`. »
4. **« Hexagone PESTEL** — 6 blocs, icônes minimalistes, labels P / E / S / T / E / L. »
5. **« Bar chart horizontal** — Problèmes SEO (Élevée 7, Moyenne 2, Faible 6), couleurs par priorité. »

Format attendu : description texte claire + contraintes (taille, palette, format SVG/PNG).

---

## 📁 Fichiers impactés

| Fichier | Modifications |
|---------|---------------|
| `docs/contacts/infopro/rapport-complet-infopro.md` | Référence aux visuels (placeholders) |
| `docs/contacts/infopro/positionnement-marketing.html` | Intégration visuels (img ou inline SVG) |
| `deploy/static-infopro-vercel/rapport.html` | Idem (via export) |
| `docs/contacts/infopro/infographie-infopro-7-formats.html` | Optionnel : renvoi vers rapport/positionnement |

---

## ✅ Critères d’acceptation

- [ ] Les textes restent inchangés ; les visuels les accompagnent.
- [ ] Palette et style cohérents avec le dashboard Infopro (fond sombre, accents rouge/orange/vert).
- [ ] Responsive : visuels lisibles sur mobile.
- [ ] Accessibilité : `aria-label` ou texte alternatif pour chaque visuel.
- [ ] Pas de régression : export statique OK.

---

*Pilote : Chef Marketing & Growth. Réf. : rapport-complet-infopro.md, positionnement-marketing.html, infographie-infopro-7-formats.html.*
