# Reconstitution de la landing P4S — tous les degrés de personnalisation

**Objectif** : Ne plus déployer un squelette. La page exportée doit être **la même** que celle servie par Django (`/p/p4s-archi/`), avec **tous** les degrés de personnalisation prévus dans le projet.

---

## 1. Degrés de personnalisation (ce qui est pris en compte)

| Degré | Source | Effet |
|-------|--------|--------|
| **Hero background** | `content_json.hero_background_url` (ou `theme.background_image_url` si CSS Vampire) | Image de fond hero 100 %, parallaxe, overlay 15 %, scanlines. |
| **Thème CSS Vampire** | `content_json.theme` + `content_json.theme_css` (après `css_vampire <url> --slug p4s-archi --apply`) | Couleurs, polices, logo du site cible (p4s-archi.com) injectés dans la landing. |
| **Style perso (fallback)** | `use_perso_style` (déterminé par la vue / l’export) | Si pas de thème ou thème « moche » : Inter, couleurs indigo (#6366f1, #818cf8), animations (fadeInUp, glow-pulse). Voir `templates/landing_pages/includes/perso_style.html`. |
| **Contenu** | `content_json` (depuis `landing-proposition-joel.json` ou base) | Toutes les sections : 01 Enjeux, 02 Solution, 03 Ce que j’offre (onglets), 04 Stack, 05 Mission Flash, Why Growth Engineer, 07 Coordonnées, CTA. |

La **vue** `landing_public` et la **commande** `export_landing_static` utilisent la **même logique** : `_use_perso_style(lp)` pour décider style perso vs thème, et `perso_ref_path` pour les assets optionnels.

---

## 2. Commande d’export (ne plus forcer un squelette)

```bash
python manage.py export_landing_static p4s-archi --output deploy/static-p4s-vercel/index.html
```

- **Avec landing en base** : utilise `content_json` (et donc `theme` / `theme_css` si présents) et `_use_perso_style(lp)`.
- **Sans landing en base** (option `--json`) : charge le JSON fourni, crée un objet minimal pour le template, et applique quand même `_use_perso_style` (souvent `True` → style perso).

La page générée contient **tout** : structure complète, contenu, hero avec background, style perso ou thème, animations.

---

## 3. Pour pousser la personnalisation au maximum (thème site cible)

1. Mettre à jour la landing en base :  
   `python manage.py create_landing_p4s --update`
2. (Optionnel) Extraire le thème du site cible :  
   `python manage.py css_vampire https://p4s-archi.com --slug p4s-archi --apply`
3. Exporter la page (sans `--json`, pour prendre la base) :  
   `python manage.py export_landing_static p4s-archi --output deploy/static-p4s-vercel/index.html`
4. Copier vers le repo de déploiement et pousser :  
   voir `deploy/PUSH-POUR-VERSION-COMPLETE.md`.

---

## 4. Fichiers concernés

- **Vue** : `apps/landing_pages/views.py` (`_use_perso_style`, `landing_public`).
- **Export** : `apps/landing_pages/management/commands/export_landing_static.py` (même contexte que la vue : `use_perso_style`, `perso_ref_path`).
- **Template** : `templates/landing_pages/proposition.html` (hero, theme_css, perso_style).
- **Style perso** : `templates/landing_pages/includes/perso_style.html`.
- **Schéma** : `schema-landing-proposition.md` (champs `theme`, `theme_css`, `use_perso_style`, `hero_background_url`).

---

*Créé pour reconstituer la landing P4S avec tous les degrés de personnalisation après perte du déploiement. Dernière mise à jour : 2025-01-30.*
