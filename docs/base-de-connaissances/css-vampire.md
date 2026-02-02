# CSS Vampire — reproduction du style du site cible

**Objectif** : visiter le site de la société prospect, extraire polices, couleurs, logo (et éventuellement fond), puis appliquer ce thème à la landing pour que le prospect se sente à l’aise (univers visuel familier).

---

## Ce qu'on récupère « chez eux » (site cible)

Lorsqu'on lance CSS Vampire sur l'URL du prospect (ex. p4s-archi.com), on **extrait uniquement** :

| Élément | Source | Utilisation sur la landing |
|--------|--------|----------------------------|
| **Couleurs** | CSS du site (background, color, border) | `--lp-bg`, `--lp-text`, `--lp-primary`, `--lp-secondary` : fond, textes, boutons, bordures |
| **Polices** | `font-family` dans les feuilles de style | `--lp-font-body`, `--lp-font-heading` (si disponibles) |
| **Logo** | Image dans `.logo`, header, etc. | Affiché en nav et dans le hero |
| **Image de fond** | Première `background-image` du site | Hero **100 %** avec **parallaxe** et **scanlines** + assombrissement 15 %. Si absente ou filtrée (icône UI), dégradé thème. |

Si le site cible est très sobre (fond noir, une couleur d'accent), la landing hérite de ce minimalisme. Les **effets** (animations, dégradés complexes, « waouh ») viennent du **template** et du brief design, pas de l'extraction.

---

## D'où vient le fond du hero (background)

Quand CSS Vampire extrait une **image de fond** (et qu'elle n'est pas filtrée comme icône UI), elle est utilisée dans le **hero à 100 %** avec **parallaxe** (`background-attachment: fixed`), **assombrissement 15 %** (overlay noir) et **effet scanline** (lignes horizontales). Sinon, le hero affiche un **dégradé** généré à partir des couleurs du thème (`--lp-primary`, `--lp-secondary`). Voir `design-brief-landing-reference-cv.md` pour le brief design.

---

## Principe

1. **Visite** : le module récupère la page d’accueil (ou l’URL fournie) du site cible.
2. **Extraction** : parsing du HTML et des feuilles de style (inline + liens) pour extraire :
   - **Polices** : `font-family` (body / heading)
   - **Couleurs** : background, text, primary (boutons/liens), secondary
   - **Logo** : image dans `.logo`, `header img`, ou première image « logo »
   - **Fond** : première `background-image` du site qui ne ressemble pas à une icône UI (checkbox, checkmark, icon, etc.) — souvent absente ; on ne l’utilise **pas** dans le hero de la landing (le hero utilise un dégradé aux couleurs du thème).
3. **Thème** : génération de variables CSS (`--lp-bg`, `--lp-text`, `--lp-primary`, `--lp-font-body`, etc.) et stockage dans `content_json.theme` et `content_json.theme_css`.
4. **Rendu** : le template `proposition.html` injecte `theme_css` et affiche le logo si `theme.logo_url` est présent.

---

## Usage

**Commande Django** : `python manage.py css_vampire <url> [options]`

| Commande | Effet |
|----------|--------|
| `css_vampire https://p4s-archi.com` | Extrait le thème et l’affiche en JSON (sans l’enregistrer). |
| `css_vampire https://p4s-archi.com --slug p4s-archi` | Idem + affiche les variables CSS générées. |
| `css_vampire https://p4s-archi.com --slug p4s-archi --apply` | Enregistre le thème dans la landing `p4s-archi` (`content_json.theme` + `theme_css`). |
| `css_vampire https://... --apply --no-logo` | N’inclut pas le logo (éviter images externes si besoin). |

**Dans Docker** :
```bash
docker compose exec web python manage.py css_vampire https://p4s-archi.com --slug p4s-archi --apply
```

---

## Fichiers

- **Module** : `apps/landing_pages/css_vampire.py` (`vampire(url)`, `theme_to_css_vars(theme)`)
- **Commande** : `apps/landing_pages/management/commands/css_vampire.py`
- **Template** : `templates/landing_pages/proposition.html` (variables CSS + logo si `content.theme`)

---

## Limites

- Extraction basée sur le HTML/CSS récupéré (pas de rendu JavaScript). Les sites en SPA peuvent ne pas exposer tout le CSS.
- Les couleurs sont déduites des propriétés `color`, `background`, `border-color` ; la « primary » est une heuristique (couleur la plus présente en luminance moyenne).
- Le logo est cherché via sélecteurs courants (`.logo`, `header img`) ; selon le site, il peut être manquant ou incorrect.
- L’image de fond extraite est souvent une **icône UI** (checkbox, checkmark, etc.) : on la filtre et on ne l’affiche pas dans le hero. Le hero utilise un **dégradé** aux couleurs primary/secondary du thème.
- Timeout 15 s ; User-Agent navigateur pour limiter les blocages.

---

## Référence

- Schéma landing proposition : `schema-landing-proposition.md` (champs `theme`, `theme_css`).
*Dernière mise à jour : 2025-01-30.*
