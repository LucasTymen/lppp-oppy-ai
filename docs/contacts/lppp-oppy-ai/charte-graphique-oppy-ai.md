# Charte graphique OPPY.AI / OPPORTUNITY — CSS corporate « Tech CIM »

**Rôle** : Référence canonique pour le **Designer UI/UX & Front-End** (et tout agent produisant du design) sur les landings et supports LPPP-OppyAI.  
**Pilote** : Designer ; validation Chef de Projet.  
**Contexte** : La marque **Opportunity** (Oppy.ai) est une plateforme CIM (Customer Interaction Management) B2B — agents IA vocaux, RCS, SMS, vidéo, relation client. Style **« Tech CIM »** : fond sombre, accent cyan/turquoise, modernité et fluidité conversationnelle.  
**Règle** : Pour toute landing ou présentation LPPP-OppyAI, **coller à cette charte** (couleurs, typo, formes).

Référence thématisation générale : `docs/base-de-connaissances/theming-landing-prospect.md`.  
Référence rôle Designer : `docs/base-de-connaissances/agents-roles-responsabilites.md` § Designer.  
Source site de référence : [https://www.oppy.ai/](https://www.oppy.ai/).

---

## 1. Palette de couleurs (Hex)

| Usage | Couleur | Hex | Variable CSS suggérée |
|-------|---------|-----|------------------------|
| **Primaire (Accent / CTA)** | Cyan / turquoise (logo, liens, CTA) | `#00C9D4` | `--oppy-cyan` |
| **Secondaire** | Cyan clair (hover, badges) | `#4DD0E1` | `--oppy-cyan-light` |
| **Fond principal** | Noir profond | `#0d0d0d` | `--oppy-bg` |
| **Surface / bloc** | Gris très foncé | `#151515` | `--oppy-surface` |
| **Texte principal** | Gris clair | `#e6e6e6` | `--oppy-text` |
| **Texte atténué** | Gris moyen | `#999` | `--oppy-muted` |
| **Bordure** | Gris translucide | `rgba(0,201,212,0.25)` | `--oppy-border` |

Contraste visé : fond sombre + accent cyan, texte clair pour lisibilité.

---

## 2. Typographie

- **Titres (Headings)** : `Montserrat` (Bold 600–700). Moderne, géométrique, tech.
- **Corps de texte** : `Inter` (400–600). Lisible, neutre, startup B2B.

Polices Google Fonts à charger : `Montserrat`, `Inter` (via `fonts.googleapis.com`).

---

## 3. Modèle CSS corporate « Oppy Style »

Variables et règles de base à réutiliser dans les landings LPPP-OppyAI.

```css
:root {
  --oppy-cyan: #00C9D4;
  --oppy-cyan-light: #4DD0E1;
  --oppy-bg: #0d0d0d;
  --oppy-surface: #151515;
  --oppy-text: #e6e6e6;
  --oppy-muted: #999;
  --oppy-border: rgba(0,201,212,0.25);
  
  --lp-font-body: 'Inter', system-ui, sans-serif;
  --lp-font-heading: 'Montserrat', system-ui, sans-serif;
}

body {
  font-family: var(--lp-font-body);
  color: var(--oppy-text);
  background-color: var(--oppy-bg);
  line-height: 1.6;
}

h1, h2, h3 {
  font-family: var(--lp-font-heading);
  font-weight: 700;
  color: var(--oppy-text);
}

.cta {
  background-color: var(--oppy-cyan);
  color: #0d0d0d;
  border-radius: 8px;
  font-weight: 600;
  transition: background-color 0.2s ease, transform 0.2s ease;
}
.cta:hover {
  background-color: var(--oppy-cyan-light);
  transform: scale(1.02);
}
```

---

## 4. Hero particules (alignement)

Le hero de la landing LPPP-OppyAI utilise un canvas de particules animées. Les teintes doivent rester dans la gamme cyan/turquoise :

- **Hue** : 175–210 (HSL)
- **Saturation** : ~72 %
- **Luminosité** : ~62 %

Cela correspond à `--oppy-cyan` et variantes pour l’effet visuel cohérent avec la charte.

---

## 5. Logo

- **URL** : `https://www.oppyai.fr/wp-content/themes/kadence-child/images/logo_opportunity.png`
- Utilisation : navbar, hero (optionnel si fond sombre avec particules).

---

## 6. Éléments et formes

- **Bordures** : `border-radius` modérés (8px à 16px). Style tech, pas trop organique.
- **Ombres** : discrètes — `box-shadow: 0 2px 12px rgba(0,0,0,0.3);` pour les cartes.
- **Sections** : fond `--oppy-surface` ou dégradés légers vers `--oppy-bg`.

---

*Document créé d’après l’analyse du site oppy.ai et les besoins de la landing LPPP-OppyAI. Dernière mise à jour : 2026-01-30.*
