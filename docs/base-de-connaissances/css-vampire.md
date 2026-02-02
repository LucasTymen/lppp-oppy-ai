# CSS Vampire — reproduction du style du site cible

**Objectif** : visiter le site de la société prospect, extraire polices, couleurs, logo (et éventuellement fond), puis appliquer ce thème à la landing pour que le prospect se sente à l’aise (univers visuel familier).

---

## Principe

1. **Visite** : le module récupère la page d’accueil (ou l’URL fournie) du site cible.
2. **Extraction** : parsing du HTML et des feuilles de style (inline + liens) pour extraire :
   - **Polices** : `font-family` (body / heading)
   - **Couleurs** : background, text, primary (boutons/liens), secondary
   - **Logo** : image dans `.logo`, `header img`, ou première image « logo »
   - **Fond** : première `background-image` si présente (optionnel)
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
- Timeout 15 s ; User-Agent navigateur pour limiter les blocages.

---

## Référence

- Schéma landing proposition : `schema-landing-proposition.md` (champs `theme`, `theme_css`).
*Dernière mise à jour : 2025-01-30.*
