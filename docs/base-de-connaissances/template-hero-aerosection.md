# Template Hero (Aérosection) — réutilisable pour toutes les landings et rapports

**Objectif** : Appliquer rapidement le même hero (image fond 100 %, parallaxe, scanlines optionnelles) à toutes les landings et aux rapports qui ont une section hero.

---

## 1. Comportement

- **Image de fond** : `hero_background_url` (prioritaire) ou `theme.background_image_url` (CSS Vampire).
- **Affichage** : image à **100 %** de la section hero (`background-size: cover`, `background-position: center`).
- **Parallaxe** : `background-attachment: fixed`.
- **Overlay** : assombrissement 15 % (`rgba(0,0,0,0.15)`).
- **Scanlines** : lignes horizontales légères (opacité 12 %) — texture discrète, pas de forme dominante.
- **Sans image** : fond uni (couleur thème), **pas de dégradé en V** ni forme blanche.

---

## 2. Où c’est en place

- **Template Django** : `templates/landing_pages/proposition.html` (section `.hero.has-bg-image`).
- **Contenu** : `content_json.hero_background_url` ou `content_json.theme.background_image_url`.
- **Schéma** : `schema-landing-proposition.md` (champ `hero_background_url`).
- **Landings Next.js standalone** : `deploy/standalone-ackuracy/` — référence. Hero pleine largeur avec `.hero-ackuracy__bg` (image), overlay, **parallax** et **scanlines actifs par défaut**. Contenu depuis `src/content/landing.json` ; image depuis `hero_background_url` du JSON ou image par défaut (voir § 4 et `generation-landing-nextjs-contenu-hero.md`).

---

## 3. Appliquer aux autres landings / rapports

1. **Landing** : dans le `content_json` de la landing, renseigner `hero_background_url` (URL de l’image). Mettre à jour en base via la commande dédiée (ex. `create_landing_p4s --update`) ou en admin.
2. **Autre template** (ex. relance-evenement, page rapport) : réutiliser les mêmes classes et règles CSS :
   - Section hero avec classe `hero has-bg-image` si une image est fournie.
   - Style inline `background-image: url('…')` ou variable selon le moteur de template.
   - Mêmes règles : `.hero.has-bg-image { background-size: cover; background-position: center; background-attachment: fixed; }`, `::before` overlay 15 %, `::after` scanlines (repeating-linear-gradient, opacité 12 %).
3. **Rapports** (HTML ou générés) : inclure un bloc hero avec les mêmes contraintes (image 100 %, parallaxe, overlay + scanlines optionnelles) si le rapport a une « aérosection » en tête.

---

## 4. Image par défaut (landings Next.js)

- Si `hero_background_url` est vide dans le JSON du contact, utiliser une **image par défaut** pour que la hero ne soit pas vide.
- **URL par défaut** (visuel cyber / aérosection, utilisée pour ACKURACY) :  
  `https://cdn.prod.website-files.com/6797c4b65039d9b51b032ae0/688c8ec596bba036056db3a1_DefaultCorrected.png`
- Documentée dans `sources.md` ou ici ; à appliquer à chaque nouvelle landing Next.js si le contact ne fournit pas d’image (voir `generation-landing-nextjs-contenu-hero.md`).

---

## 5. Fichiers à aligner

- `templates/landing_pages/proposition.html` (référence Django)
- `deploy/standalone-ackuracy/` (référence Next.js : hero + parallax + scanlines par défaut)
- `docs/base-de-connaissances/schema-landing-proposition.md`
- `docs/base-de-connaissances/generation-landing-nextjs-contenu-hero.md` (procédure génération)
- Tout nouveau template de landing ou de rapport avec hero : reprendre ce pattern.

---

*Créé pour réutilisation sur les autres rapports et landing pages. Dernière mise à jour : 2025-01-30.*
