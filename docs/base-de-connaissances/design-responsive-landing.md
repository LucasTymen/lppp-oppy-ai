# Design responsive — Landing proposition

**Pour** : Équipe style / Designer.  
**Contexte** : Le template `proposition.html` applique des déclinaisons responsives pour **mobile** (base), **tablette**, **desktop** et **HD**. Ce document décrit les breakpoints et conventions pour aligner les futurs styles.

---

## 1. Breakpoints

| Cible | Variable CSS | Valeur | Usage |
|-------|--------------|--------|--------|
| **Mobile** | — | &lt; 768px | Base : nav compacte, hero centré, sections 720px max. |
| **Tablette** | `--lp-bp-tablet` | 768px | Nav + logo agrandis, hero typo renforcée, sections 720px. |
| **Desktop** | `--lp-bp-desktop` | 1024px | Plus d’air (padding, gaps), sections 800px, bordures/typo renforcées. |
| **HD** | `--lp-bp-hd` | 1440px | Corps de texte légèrement agrandi, sections 880px, hero plus grand. |

Les variables sont définies dans `:root` du template ; les media queries utilisent les valeurs en dur (768px, 1024px, 1440px) car `var()` dans une condition `@media` n’est pas supporté partout.

---

## 2. Éléments concernés par les déclinaisons

- **Nav** : padding, taille du logo (36px → 42 → 48 → 52), liens et CTA.
- **Hero** : padding vertical/horizontal, taille H1 et sous-titre, logo hero (64 → 80 → 88 → 96), CTA.
- **Icebreaker** : padding, max-width, taille de police.
- **Sections** : padding, max-width (720 → 800 → 880), titres H2, numéros, bordures.
- **Cartes / onglets services / stack / Mission Flash / citation** : padding, tailles de police.
- **CTA final** : padding bloc et bouton.

---

## 3. Où modifier (équipe style)

- **Template** : `templates/landing_pages/proposition.html`  
  - Variables : bloc `:root` (lignes ~14–22).  
  - Media queries : fin du `<style>`, blocs `@media (min-width: 768px)`, `1024px`, `1440px`.
- **Cohérence** : toute nouvelle règle qui touche nav, hero, sections ou CTA devrait avoir une déclinaison par breakpoint si l’effet visuel le justifie (taille, espacement).

---

## 4. Références

- Brief design : `design-brief-landing-reference-cv.md`
- Schéma contenu : `schema-landing-proposition.md`
- Thème société : `css-vampire.md`

*Dernière mise à jour : 2025-01-30.*
