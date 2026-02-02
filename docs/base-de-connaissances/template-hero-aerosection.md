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

---

## 3. Appliquer aux autres landings / rapports

1. **Landing** : dans le `content_json` de la landing, renseigner `hero_background_url` (URL de l’image). Mettre à jour en base via la commande dédiée (ex. `create_landing_p4s --update`) ou en admin.
2. **Autre template** (ex. relance-evenement, page rapport) : réutiliser les mêmes classes et règles CSS :
   - Section hero avec classe `hero has-bg-image` si une image est fournie.
   - Style inline `background-image: url('…')` ou variable selon le moteur de template.
   - Mêmes règles : `.hero.has-bg-image { background-size: cover; background-position: center; background-attachment: fixed; }`, `::before` overlay 15 %, `::after` scanlines (repeating-linear-gradient, opacité 12 %).
3. **Rapports** (HTML ou générés) : inclure un bloc hero avec les mêmes contraintes (image 100 %, parallaxe, overlay + scanlines optionnelles) si le rapport a une « aérosection » en tête.

---

## 4. Fichiers à aligner

- `templates/landing_pages/proposition.html` (référence)
- `docs/base-de-connaissances/schema-landing-proposition.md`
- Tout nouveau template de landing ou de rapport avec hero : reprendre ce pattern.

---

*Créé pour réutilisation sur les autres rapports et landing pages. Dernière mise à jour : 2025-01-30.*
