# Brief design — Landing au niveau de la référence CV / page perso

**Pour** : Designer UI/UX (règle `.cursor/rules/editorial.mdc`, rôle Designer).  
**Contexte** : Les landings proposition (template `proposition.html`) doivent avoir un **effet waouh** et ressembler à la référence ci-dessous, tout en **repreneant le style de la société cible** (CSS Vampire).

---

## 1. Référence visuelle

**URL de référence** :  
https://landingpage-cv-page-perso-byxr27jnz-lucas-tymens-projects.vercel.app/

Objectif : que la landing proposition (Django ou Next.js) atteigne le même niveau de **design moderne, impact visuel et fluidité** que cette page (hero, sections, typo, espacements, animations / micro-interactions).

---

## 2. Ce qu'on récupère chez la cible (CSS Vampire) vs ce qu'on ajoute

- **Chez la cible** : CSS Vampire extrait **uniquement** couleurs (bg, text, primary, secondary), polices, logo. Pas d'image de fond utilisée dans le hero (souvent filtrée). Voir `css-vampire.md`.
- **Thème manuel si extraction insuffisante** : lorsque CSS Vampire ne détecte pas correctement les couleurs d’accent (ex. teal/cyan sur un site sombre), on peut **injecter un thème manuel** (variables CSS + dégradé) dans le JSON ou la commande de création de landing (ex. 0flow : `THEME_0FLAW`, `THEME_CSS_0FLAW`). Étude plus approfondie du site cible : couleurs réelles, dégradés, logos, pour les recréer à la main si besoin.
- **Image de fond hero** : priorité à `hero_background_url` (image fournie par le contact ou extraite manuellement) ; sinon dégradé thème. L’image peut être hébergée en static (ex. `static/landing_pages/images/hero-<slug>.png`) avec parallaxe et overlay.
- **Bandeau (alert banner)** : bandeau optionnel sous la nav (une ligne, fond primary), pour message d’accroche (offre, CTA). Champ `alert_banner` dans le JSON ; style cohérent avec le thème (ex. teal 0Flaw).
- **Le fond du hero (fallback)** : sans image, c’est un **dégradé généré** dans le template à partir des couleurs du thème. Pour retrouver les **effets et couleurs** de la référence (lien ci-dessus), les intégrer dans le template (dégradés, animations, variété de couleurs).

## 3. Contraintes à respecter

- **Style société** : appliquer le thème extrait par **CSS Vampire** (couleurs, polices, logo) pour que le prospect se sente dans son univers.
- **Contenu** : structure Full-Stack Conversion (hero, enjeux, solution, services onglets, stack, mission flash, pourquoi Growth Engineer, CTA). Voir `schema-landing-proposition.md`.
- **Support** : template Django `templates/landing_pages/proposition.html` et/ou page Next.js (frontend) selon la cible (Django = admin + slug, Next = Vercel).

---

## 4. Livrables attendus

1. **Alignement visuel** : proposition de mise en page (ou maquette / spec) qui rapproche la landing de la référence (hero pleine hauteur ou très impactant, nav ancres, sections aérées, typo hiérarchisée, animations ou transitions).
2. **Variables thème** : réutilisation de `--lp-primary`, `--lp-bg`, `--lp-text`, `--lp-font-body`, `--lp-font-heading`, logo et optionnel fond (CSS Vampire).
3. **Mobile-first** : même niveau de soin sur mobile que sur desktop.

---

## 5. Section « Propositions de valeur » (wireframe de référence)

Pour présenter les **prestations / valeur** (services) de façon claire et pratique, s’inspirer du wireframe suivant :

- **Titre de section** : une accroche **orientée bénéfice** (ex. « Des livrables concrets pour votre prospection »), pas uniquement « Prestations ».
- **Grille** : blocs en **grille 2×2** (4 propositions), avec beaucoup d’air entre les blocs.
- **Chaque bloc** :
  - **Sous-titre** (nom du service / de la proposition),
  - **Paragraphe court** (3–5 lignes, concret, pas de vent),
  - **CTA** type « En savoir plus » ou « En discuter » (lien vers contact ou ouverture du modal contact).

Objectif : contenu **digeste**, **pratique**, avec une sortie claire vers l’échange (« Learn more » → contact). Appliqué sur la landing Ackuracy (section Prestations en grille de cartes) ; à répliquer sur les autres templates (Django `proposition.html`, futurs standalones).

Référence visuelle : wireframe « Snap photos and share like never before » (titre + 4 blocs avec sous-titre, texte, bouton Learn more). Image conservée dans le workspace si fournie.

---

## 6. Références projet

- **Schéma contenu** : `schema-landing-proposition.md`
- **CSS Vampire** : `css-vampire.md` (thème société)
- **Responsive (équipe style)** : `design-responsive-landing.md` (breakpoints tablette / desktop / HD)
- **Style perso (fallback)** : `style-perso-fallback.md` (algorithme, chemin référence, diagrammes / funnels)
- **Stack frontend** : `stack-frontend-nextjs-react.md` (effet waouh, Next.js + React, Vercel)
- **Exemple cible** : P4S — `docs/contacts/p4s-archi/landing-proposition-joel.json`
- **Exemple thème manuel + bandeau + hero image** : 0flow — `docs/contacts/0flow/` (thème 0Flaw injecté manuellement, `hero_background_url`, `alert_banner`), `squelette-vs-inversion-complete.md`

---

*Brief créé à la demande utilisateur. Dernière mise à jour : 2025-01-30.*
