# Yuwell — Portfolio / étude graphique (landing LPPP)

**Type** : landing page portfolio (étude graphique), hors prospection classique.  
**Objectif** : servir de portfolio pour une candidature graphiste chez Yuwell (Jiangsu Yuyue Medical Equipment).  
**Source** : `portfolio Yuwell_1.pdf` (étude ChatGPT : contexte marque, charte, système couleur par gamme produit).  
**URL** : `/yuwell/` (redirige vers `/yuwell/presentation/`). Cinq pages dédiées, nav commune.

---

## 1. Contexte projet

- **Yuwell** : entreprise chinoise d’équipements médicaux (respiratoire, diagnostic, mobilité, clinique/urgence, soins à domicile).
- **Usage** : portfolio multi-pages présentant une étude de charte couleur structurante et déclinée par gamme produit, pour démontrer une approche design system / industriel, pas « artiste ».
- **Public** : recruteur / responsable marque ou produit Yuwell.
- **Positionnement** : fonction, lisibilité, système, contrainte — pas de signature artistique ni d’effets gratuits.

---

## 2. Structure multi-pages (5 pages)

| Page | URL | Contenu (résumé) |
|------|-----|------------------|
| **Présentation** | `/yuwell/presentation/` | Accueil : hero vidéo, bienvenue, cartes liens vers les 4 autres pages |
| **Study case** | `/yuwell/study-case/` | Contexte, objectifs, principes design, déclinaison par gamme, palettes, règles, bénéfices |
| **Study case 2** | `/yuwell/study-case-2/` | Second cas d’étude (à compléter : ex. fiche produit, notice, design system) |
| **Charte graphique** | `/yuwell/charte-graphique/` | Palette corporate + palettes par gamme (HEX, RGB, Pantone), règles d’usage |
| **À propos** | `/yuwell/a-propos/` | Parcours, approche design, contact (à compléter) |

Nav sticky commune sur toutes les pages (Présentation, Study case, Study case 2, Charte graphique, À propos). Base de style : `yuwell_base.html` ; chaque page étend la base et remplit les blocs `yuwell_hero` et `yuwell_content`.

**Typo** : rapprochement yuwell-eu.com (clean, pur, **ultra fines / thin**) — police **Work Sans** (Google Fonts, validée Designer) : corps 300, hero-sub 200, titres 600/700. Brief : `docs/base-de-connaissances/design-brief-typo-portfolio-yuwell.md`.

**Observation site yuwell-eu.com** : les changements de rubrique s’appuient sur **plusieurs familles de polices** (repérées : MiSans-Thin, Oswald, et d’autres selon les sections — jusqu’à l’ordre de **7 typo** distinctes). Notre proposition inverse le parti pris : **une seule famille (Work Sans)** avec **hiérarchie par poids** (100–700), pour un design system plus cohérent et maintenable.

**Couleurs (charte proposée)** : corporate et gammes sont définies dans `THEME_CSS_YUWELL` (`apps/landing_pages/themes.py`) : variables `--lp-*` (corporate) et `--yuwell-respiratoire`, `--yuwell-diagnostic`, `--yuwell-soins-domicile`, `--yuwell-mobilite`, `--yuwell-urgence-alerte`, etc. Utilisées dans les templates (ex. page Charte graphique, mock-cards). Notre proposition conserve l’épuré tout en ajoutant la **structure couleur par gamme** (identification familles produit, lisibilité catalogue).

---

## 3. Palettes de référence (PDF)

### 3.1 Corporate

| Usage | Nom | HEX | RGB | Pantone |
|-------|-----|-----|-----|---------|
| Marque principale | Yuwell Red | #E60012 | 230, 0, 18 | PANTONE 186 C |
| Neutre principal | Pure White | #FFFFFF | 255, 255, 255 | PANTONE White |
| Neutre secondaire | Cool Gray | #F5F5F5 | 245, 245, 245 | PANTONE Cool Gray 1 C |
| Texte principal | Dark Charcoal | #333333 | 51, 51, 51 | PANTONE 426 C |

### 3.2 Par gamme (extrait)

- **Respiratoire** : Cyan médical #00C2D1 (3125 C), Bleu moyen #0078A8 (7699 C), Bleu grisé #90C2D3 (544 C).
- **Diagnostic** : Vert stable #57B894 (7496 C), Vert moyen #3F8D68 (3292 C), Vert désaturé #AACFBF (565 C).
- **Soins à domicile** : Teal doux #4DA6A1 (7718 C), Teal clair #8FC7C4 (3245 C), Gris bleuté #BECFD1 (656 C).
- **Mobilité** : Cool Slate #7A7A7A (Cool Gray 9 C), Orange attention #E08E3C (7584 C).
- **Clinique / urgence** : Rouge sécurisé #C5281C (186 C désaturé) — usage strict alerte, jamais fond.

---

## 4. Rôles équipe (structure et contenu)

| Rôle | Responsabilité |
|------|----------------|
| **Chef de projet** | Valider la structure et le positionnement (portfolio vs prospection) ; s’assurer que la doc et les décisions sont à jour. |
| **Designer** | Visuel de la landing (grille, typo, couleurs) ; cohérence avec l’étude (sobre, médical, lisible) ; hiérarchie, responsive, accessibilité. |
| **Dev Django** | Route `/yuwell/`, vue, template, données palettes (contexte ou JSON). |
| **Rédacteur** | Textes des sections (contexte, objectifs, principes) à partir du PDF ; ton professionnel, pas créatif ; Study case 2 et À propos. |
| **Expert SEO** | Titres de page, meta description, H1/H2 pour les 5 pages ; mots-clés pertinents (Yuwell, étude graphique, charte couleur). |

**Remplissage du contenu** : voir la segmentation **`docs/base-de-connaissances/segmentations/2026-02-08-remplissage-contenu-portfolio-yuwell.md`** — tâches détaillées pour Rédacteur, Designer, Expert SEO et Chef de Projet.

Référence : `docs/base-de-connaissances/decisions.md` (entrée landing Yuwell), `docs/base-de-connaissances/routes-back-lppp.md` (route `yuwell/`).

---

## 5. Fichiers concernés

- **Vues** : `apps/landing_pages/views.py` — `yuwell_portfolio` (redir.), `yuwell_presentation`, `yuwell_study_case`, `yuwell_study_case_2`, `yuwell_charte_graphique`, `yuwell_a_propos` ; helper `_yuwell_common_context(active_nav)`.
- **URLs** : `apps/landing_pages/urls.py` — `yuwell/`, `yuwell/presentation/`, `yuwell/study-case/`, `yuwell/study-case-2/`, `yuwell/charte-graphique/`, `yuwell/a-propos/`.
- **Templates** : `yuwell_base.html` (nav + style) ; `yuwell_presentation.html`, `yuwell_study_case.html`, `yuwell_study_case_2.html`, `yuwell_charte_graphique.html`, `yuwell_a_propos.html`.
- **Données palettes** : dans la vue (YUWELL_PALETTE_CORPORATE, YUWELL_PALETTE_GAMMES).

---

## 6. Usages d’icônes (fil de fer / ultra thin)

**Recommandation** : décliner les icônes en style **fil de fer** (outline, trait fin / ultra thin) pour rester aligné avec la typo Work Sans et l’esprit épuré du portfolio.

**Ressources gratuites secteur médical / produit** (à vérifier en ligne pour versions et licences actuelles) :

| Ressource | Style | Licence | Lien / remarque |
|-----------|--------|---------|------------------|
| **Health Icons** | Outline (stroke 2px), Filled | CC0 (pas d’attribution) | [healthicons.org](https://healthicons.org/) — 1 700+ icônes santé (devices, diagnostics, medications, people, symbols, etc.) ; SVG/PNG ; Figma, React. |
| **Lineicons** | Line / outline, plusieurs variantes | MIT | [lineicons.com](https://lineicons.com/icons/category/health-medical) — 575 icônes Health & Medical ; SVG, PNG ; gratuit en tier « essential ». |
| **Unicons (IconScout)** | Line, Thin line | Gratuit (vérifier conditions) | [iconscout.com/unicons](https://iconscout.com/unicons/free-line-icons/medical) — variantes line et thin line médical. |
| **Lucide** | Outline fin (héritier Feather) | ISC | [lucide.dev](https://lucide.dev/) — 1 000+ icônes dont médical (ex. briefcase-medical) ; style minimaliste trait fin ; React, Vue, SVG. |
| **Icons8** (style Wired/Outline) | Cute Outline / Wired | Gratuit avec attribution ou licence | [icons8.com](https://icons8.com/icons/set/healthcare--style-wired) — health/healthcare en outline ; vérifier licence pour usage commercial sans watermark. |

**Référence détaillée** : `docs/base-de-connaissances/icones-fil-de-fer-medical-product.md`.

---

## 7. Référence site officiel (inspiration composition / style)

- **Analyse composition, style et templates** yuwell-eu.com : `docs/ressources-utilisateur/etudes/yuwell-eu-com-analyse-composition-style.md`.
- **Page produit** : [yuwell-eu.com — Product (categoryId=51)](https://www.yuwell-eu.com/#/product?categoryId=51&switchover=1).
- **Sprint alignement** (Chef de Projet → Webdesigner, Rédacteur, Dev) : `docs/base-de-connaissances/segmentations/2026-02-09-sprint-alignement-portfolio-yuwell-esprit-yuwell-eu.md`.

---

*Document créé pour structurer la landing portfolio Yuwell et aligner l’équipe. Source : portfolio Yuwell_1.pdf. Dernière mise à jour : 2026-01-30. Structure 5 pages : 2026-02-08. § 6 Icônes : 2026-01-30.*
