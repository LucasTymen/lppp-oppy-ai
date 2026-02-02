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
- **Le fond du hero** : ce n'est **pas** une image du site cible ; c'est un **dégradé généré** dans le template à partir de ces couleurs. Pour retrouver les **effets et couleurs** de la référence (lien ci-dessus), il faut les intégrer dans le template (dégradés, animations, variété de couleurs).

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

## 5. Références projet

- **Schéma contenu** : `schema-landing-proposition.md`
- **CSS Vampire** : `css-vampire.md` (thème société)
- **Responsive (équipe style)** : `design-responsive-landing.md` (breakpoints tablette / desktop / HD)
- **Style perso (fallback)** : `style-perso-fallback.md` (algorithme, chemin référence, diagrammes / funnels)
- **Stack frontend** : `stack-frontend-nextjs-react.md` (effet waouh, Next.js + React, Vercel)
- **Exemple cible** : P4S — `docs/contacts/p4s-archi/landing-proposition-joel.json`

---

*Brief créé à la demande utilisateur. Dernière mise à jour : 2025-01-30.*
