# Sprint — Graphique et éditorial FitClem (Soft Wellness / girly)

**Nom du livrable** : **LPPP-FitClem** — alignement visuel et ton avec fitclem.fr  
**Date** : 2026-01-30  
**Statut** : ✅ Appliqué (2026-01-30)  
**Référence visuelle** : Captures fitclem.fr (assets/ et descriptions détaillées ci-dessous).

**Objectif** : Adapter la landing `/p/fitclem/` (et futures pages multipage) pour ressembler au maximum au style « Soft Wellness » / girly du site FitClem : palette étendue, typographie, formes organiques, ton éditorial.

---

## 1. Synthèse visuelle (d’après les captures fitclem.fr)

### 1.1 Palette de couleurs (affinée)

| Usage | Variable | Hex | Contexte site |
|-------|----------|-----|---------------|
| Primaire CTA / logo | `--fitclem-orange` | `#FF6633` | Boutons « 100 % PLAISIR », « JE TESTE ! », badges |
| Secondaire / douceur | `--fitclem-peach` | `#FFA385` | Fonds doux, accents |
| Fond principal clair | `--fitclem-white` | `#FFFFFF` | Produits, cartes |
| Texte / contraste | `--fitclem-black` | `#1A1A1A` | Lisibilité maximale |
| Fond pastel | `--fitclem-gray-light` | `#F9F9F9` | Blocs secondaires |
| **Nouveau** — Bandeau promo | `--fitclem-magenta` | `#CC3399` / `#D81B60` | Bandeaux top, badges « PRIX TOP Santé » |
| **Nouveau** — Hero lavande | `--fitclem-lavender` | `#B9A9D0` | Fond hero produit (pâte à tartiner) |
| **Nouveau** — Rose pastel | `--fitclem-pastel-pink` | `#FFE4E1` / `#FFB6C1` | Grille tiled, fonds « collations » |
| **Nouveau** — Vert badge | `--fitclem-green` | `#57B894` | Badge « TRANSFORMATIONS » |
| **Nouveau** — Bleu diagnostic | `--fitclem-blue` | `#7EB8DA` | Onglet « Diagnostic » vertical |

### 1.2 Typographie

- **Titres** : Montserrat ou Poppins (Bold), uppercase, letter-spacing
- **Corps** : Inter ou Open Sans
- **Nouveau — titres décoratifs** : Police script ou semi-script (ex. « Nos incontournables ») — option pour sections clés (étude marketing, proposition KPI)
- **Navigation** : uppercase, poids moyen à bold

### 1.3 Formes et composants

- **Boutons CTA** : `border-radius: 50px` (pill), uppercase, fond orange ou magenta
- **Badges circulaires** : cercles parfaits (ex. « 1er Prix Top Santé »)
- **Cartes produit / section** : `border-radius: 20–24px`, ombre légère
- **Onglets catégories** : pill-shaped, fond blanc/gris clair, actif = orange
- **Bandeau promo top** : pleine largeur, fond magenta, texte blanc
- **Pattern fond** : grille/tile légère (pastel pink) optionnelle pour hero ou sections

### 1.4 Imagerie

- **Style** : high-key, luminosité élevée, fonds clairs
- **Mise en page** : images circulaires possibles pour sections (style catégories FitClem)
- **Accents** : feuille verte logo FitClem, éléments organiques (fruits, noisettes, etc.) si pertinents

---

## 2. Tâches graphiques (Designer + Dev Django)

### 2.1 Palette et variables CSS

- [ ] **Étendre** `THEME_CSS_FITCLEM` dans `themes.py` avec les nouvelles variables : `--fitclem-magenta`, `--fitclem-lavender`, `--fitclem-pastel-pink`, `--fitclem-green`, `--fitclem-blue`.
- [ ] **Tester** sur `/p/fitclem/` : fond hero lavande ou pastel pink en option ; bandeau alerte en magenta.

### 2.2 Bandeau promo (optionnel)

- [ ] **Créer** un bandeau type « Candidature Responsable Marketing Digital — Livrable complet » en haut (style bandeau magenta fitclem.fr), fond `--fitclem-magenta`, texte blanc, centré.

### 2.3 Boutons et badges

- [ ] **Vérifier** : tous les CTA en pill (border-radius 50px), uppercase, fond orange ou magenta selon hiérarchie.
- [ ] **Ajouter** si pertinent : badge circulaire type « 1er Prix Top Santé » pour valoriser le rapport SEO (texte adapté : « Manque à gagner 132–324 k€/an »).

### 2.4 Sections et cartes

- [ ] **Conserver** bordure gauche pêche + fond gris clair pour `.section`.
- [ ] **Option** : fond pastel pink avec motif grille léger sur hero ou section d’accroche.
- [ ] **Cartes** : border-radius 24px, box-shadow très léger (0 4px 15px rgba(0,0,0,0.05)).

### 2.5 Typographie décorative

- [ ] **Explorer** : police script/semi-script (ex. Pacifico, Dancing Script, ou Great Vibes) pour un ou deux titres de section, si cohérent avec le brief candidature.

### 2.6 Joueur de contenu (content player) — éviter sections plates

- [ ] **Référence** : brief `brief-graphique-fitclem-soft-wellness.md` § 4 — chaque section = texte + visuel (flowchart, dashboard, comparaison, mockup).
- [ ] **Maquettes** : proposer un content player par section (enjeux, solution, étude marketing, SEO, KPI, stack).

### 2.7 Occuper l’espace desktop

- [ ] **Layout** : sections en deux colonnes (texte + visuel) sur desktop ; max-width 1100–1400px au lieu de 720px.
- [ ] **Alternance** : texte gauche / visuel droite, puis visuel gauche / texte droite.
- [ ] **Référence** : brief § 5.

---

## 3. Tâches éditoriales (Rédacteur)

### 3.1 Ton

- **Alignement** : bienveillant, orienté résultat, encouragement (sans promesse miracle).
- **Formulations** : bénéfices concrets, verbes d’action, phrases courtes.
- **Éviter** : jargon technique brut, ton sec ou trop corporate.

### 3.2 Libellés CTA

- [ ] **Remplacer** si génériques : « Voir le livrable complet » → « JE DÉCOUVRE », « Voir l’étude SEO » → « DÉCOUVRIR L’ÉTUDE » (style FitClem : « JE TESTE ! », « 100 % PLAISIR »).
- [ ] **Format** : uppercase, verbe à l’infinitif ou impératif, court.

### 3.3 Titres de sections

- [ ] **Adapter** : titres courts, impact, bénéfice (ex. « Vos enjeux » → « VOS ENJEUX », « Manque à gagner » → « OPPORTUNITÉ SEO »).

### 3.4 Messages de confiance

- [ ] **Intégrer** des éléments de crédibilité : « Manque à gagner 132–324 k€/an », « Étude marketing complète », « Plan 30/60 j actionnable » — sur le modèle des badges « 1er Prix Top Santé » / « VU À LA TV ».

### 3.5 Fichiers à mettre à jour

- [ ] **`landing-proposition-fitclem.json`** : `cta_text`, `alert_banner`, titres dans `seo_resume`, libellés `services`.
- [ ] **Ou** `content-landing-fitclem.md` si contenu multipage séparé.

---

## 4. Ordre de travail

1. **Designer** : mettre à jour `brief-graphique-fitclem-soft-wellness.md` avec la palette étendue et les composants (bandeau, badges).
2. **Dev Django** : étendre `THEME_CSS_FITCLEM` dans `themes.py` + ajuster template proposition si besoin (bandeau promo, badge).
3. **Rédacteur** : réviser libellés CTA et titres dans `landing-proposition-fitclem.json`.
4. **Dev Django** : lancer `create_landing_fitclem --update --publish` pour appliquer les changements.
5. **Chef de Projet** : validation visuelle et éditoriale sur `/p/fitclem/`.

---

## 5. Fichiers concernés

| Fichier | Rôle |
|---------|------|
| `apps/landing_pages/themes.py` | Palette, variables, thème FitClem |
| `docs/contacts/fitclem/landing-proposition-fitclem.json` | Contenu éditorial (CTA, titres) |
| `docs/contacts/fitclem/brief-graphique-fitclem-soft-wellness.md` | Spécifications graphiques |
| `templates/landing_pages/proposition.html` | Structure (bandeau promo si ajouté) |

---

## 6. Critères de succès

- [ ] Palette étendue (magenta, lavande, pastel pink, vert, bleu) disponible et utilisée où pertinent.
- [ ] CTA en style FitClem (uppercase, verbes courts, pill).
- [ ] Ton bienveillant et orienté résultat dans les textes.
- [ ] Visuellement cohérent avec les captures fitclem.fr (formes organiques, couleurs, lisibilité).

---

*Sprint créé pour aligner la landing FitClem sur le style Soft Wellness / girly du site fitclem.fr. Référence : captures fournies (assets/), brief-graphique-fitclem-soft-wellness.md.*
