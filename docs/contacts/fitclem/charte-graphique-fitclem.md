# Charte graphique FITCLEM — CSS corporate « Soft Wellness »

**Rôle** : Référence canonique pour le **Designer UI/UX & Front-End** (et tout agent produisant du design) sur les landings et supports FITCLEM.  
**Pilote** : Designer ; validation Chef de Projet.  
**Contexte** : La marque FITCLEM utilise un style **« Soft Wellness »** — douceur (soin/santé) et dynamisme (fitness).  
**Règle** : Pour toute landing ou présentation FITCLEM, **coller à cette charte** (couleurs, typo, formes, ombres).

Référence thématisation générale : `docs/base-de-connaissances/theming-landing-prospect.md`.  
Référence rôle Designer : `docs/base-de-connaissances/agents-roles-responsabilites.md` § Designer.

---

## 1. Palette de couleurs (Hex)

| Usage | Couleur | Hex | Variable CSS suggérée |
|-------|---------|-----|------------------------|
| **Primaire (Action/Énergie)** | Orange corail (logo, CTA principaux) | `#FF6633` | `--fitclem-orange` |
| **Secondaire (Douceur/Bien-être)** | Pêche clair (fonds de sections, éléments secondaires) | `#FFA385` | `--fitclem-peach` |
| **Fond & Pureté** | Blanc (aspect clean, médical/pharmacie) | `#FFFFFF` | `--fitclem-white` |
| **Accent (Luxe/Texte)** | Noir presque pur (typographie, lisibilité max) | `#1A1A1A` | `--fitclem-black` |
| **Fond doux** | Gris très clair | `#F9F9F9` | `--fitclem-gray-light` |

Contraste visé : tons chair/nude + couleurs d’action vives.

---

## 2. Typographie

- **Titres (Headings)** : `Montserrat` ou `Poppins` (Bold). Moderne, géométrique, « Fitness ».
- **Corps de texte** : `Inter` ou `Open Sans`. Très lisible, style startup tech & bien-être.

Polices Google Fonts à charger selon stack (ex. Next.js : `next/font/google` ou link dans le HTML).

---

## 3. Modèle CSS corporate « Fitclem Style »

Variables et règles de base à réutiliser dans les landings et présentations FITCLEM.

```css
:root {
  /* Couleurs de la charte FITCLEM */
  --fitclem-orange: #FF6633;
  --fitclem-peach: #FFA385;
  --fitclem-white: #FFFFFF;
  --fitclem-black: #1A1A1A;
  --fitclem-gray-light: #F9F9F9;
  
  /* Typographie */
  --font-main: 'Inter', sans-serif;
  --font-title: 'Montserrat', sans-serif;
}

body {
  font-family: var(--font-main);
  color: var(--fitclem-black);
  line-height: 1.6;
  background-color: var(--fitclem-white);
}

h1, h2, h3 {
  font-family: var(--font-title);
  font-weight: 700;
  text-transform: uppercase; /* Côté fitness/impact */
  letter-spacing: 1px;
  color: var(--fitclem-black);
}

.btn-primary {
  background-color: var(--fitclem-orange);
  color: white;
  padding: 12px 24px;
  border-radius: 50px; /* Coins très arrondis — wellness */
  text-transform: uppercase;
  font-weight: bold;
  border: none;
  transition: transform 0.2s ease;
  cursor: pointer;
}

.btn-primary:hover {
  transform: scale(1.05);
  background-color: #e55a2d;
}

.section-soft {
  background-color: var(--fitclem-gray-light);
  border-left: 5px solid var(--fitclem-peach);
  padding: 20px;
  margin: 20px 0;
}
```

---

## 4. Éléments iconographiques et formes

- **Bordures** : `border-radius` élevés (20px à 50px). Formes organiques et accueillantes, pas d’angles saillants.
- **Imagerie** : Priorité high-key (haute luminosité), fonds clairs, mise en avant des textures (gummies, poudres, peau).
- **Ombres** : Légères — `box-shadow: 0 4px 15px rgba(0,0,0,0.05);` pour la profondeur sans alourdir.

---

## 5. Utilisation

- **Landing pages FITCLEM** : appliquer cette charte (variables CSS, polices, boutons, sections).
- **Présentations / audits SEO-Marketing** : utiliser ce CSS pour les supports (slides, rapports) afin d’aligner le rendu avec l’univers de la marque.

*Document créé à partir de l’analyse visuelle et des rapports Lighthouse/SEO FITCLEM. Dernière mise à jour : 2026-02-15.*
