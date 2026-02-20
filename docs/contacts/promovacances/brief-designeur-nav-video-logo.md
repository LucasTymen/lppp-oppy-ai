# Brief Designer — Landing Promovacances (nav, vidéo, logo)

**Demandé par** : Utilisateur  
**Rôle responsable** : Designer UI/UX  
**Fichiers concernés** : `apps/landing_pages/themes.py` (THEME_PROMOVACANCES), `templates/landing_pages/proposition.html` (si overrides nécessaires)  
**Références** : `docs/base-de-connaissances/contraste-textes-landing.md`, `theming-landing-prospect.md`, `registre-agents-ressources.md` § Designer

---

## Contexte

La landing Promovacances (`/p/promovacances/`) doit aligner son rendu sur la page d’accueil officielle : navbar fixe, vidéo hero en pleine largeur avec parallaxe, logo officiel.

---

## 1. Logo officiel

- **Remplacer** l’URL actuelle du logo dans `apps/landing_pages/themes.py` (THEME_PROMOVACANCES) par :
- **URL** : `https://upload.wikimedia.org/wikipedia/commons/8/8d/Promovacances.svg`
- S’assurer que le logo s’affiche correctement dans la navbar et la hero (nav-logo, hero-logo si applicable).

---

## 2. Navbar fixe en haut

- La navbar doit être **position: fixed ; top: 0** et rester visible au scroll.
- Vérifier que :
  - `.nav` a bien `position: fixed` (et non sticky) pour Promovacances ;
  - le contenu principal a un `padding-top` suffisant pour ne pas passer sous la navbar ;
- Si le thème Promovacances écrase le style de base, ajouter des overrides avec `!important` ou une spécificité plus forte.

---

## 3. Vidéo hero : pleine largeur (100 %) et parallaxe

- **Pleine largeur** : la vidéo doit occuper 100 % de la largeur/hauteur du hero (pas de bandes noires).
  - `.hero-bg-video` : `width: 100vw`, `height: 100vh` (ou équivalent) ;
  - iframe/vidéo : `object-fit: cover`, `min-width: 100%`, `min-height: 100%`, `left: 50%`, `top: 50%`, `transform: translate(-50%, -50%)` ;
  - éviter tout ratio 16:9 figé qui crée des bandes noires.
- **Parallaxe** : la vidéo doit rester fixe au scroll (position: fixed sur le conteneur vidéo).
  - `.hero.has-bg-video .hero-bg-video` : `position: fixed` (comme sur FitClem) ;
  - `.hero` : `width: 100vw`, `overflow: hidden`, `margin-left: calc(50% - 50vw)` si nécessaire pour éviter le scroll horizontal.

---

## 4. Vérifications finales

- Navbar fixe, logo visible, vidéo en 100 % sans cadre noir, effet parallaxe au scroll.
- Contraste et accessibilité : `docs/base-de-connaissances/contraste-textes-landing.md`.
