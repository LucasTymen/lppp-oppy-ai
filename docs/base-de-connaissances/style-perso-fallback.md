# Style perso (fallback) — algorithme et référence projet

**Objectif** : Pour les sociétés dont on ne peut pas récupérer l'identité visuelle (CSS Vampire impossible ou échec) ou dont le thème extrait est jugé trop moche, appliquer le **style de la landing page personnelle** (CV / page perso) et réutiliser graphiques et infographiques pour diagrammes et funnels personnalisés.

---

## 1. Algorithme de fallback

Le template **proposition** utilise le style perso quand **au moins une** des conditions suivantes est vraie :

| Condition | Description |
|----------|-------------|
| **Pas de thème** | `content.theme` absent ou vide (CSS Vampire jamais lancé ou erreur). |
| **Explicite** | `content.use_perso_style === true` ou `content.theme.use_fallback === true` (choix manuel en admin / content_json). |
| **Thème "moche"** | Thème sans identité visuelle : pas de `logo_url`, pas de `background_image_url`, et pas de couleur `primary` dans `theme.colors`. |

Implémentation : `apps/landing_pages/views.py` → `_use_perso_style(lp)`.

---

## 2. Chemin de référence (projet landing perso)

**Projet** : landing CV / page perso (graphiques, infographiques, style, animations).

| Contexte | Chemin à utiliser |
|----------|-------------------|
| **Linux / WSL** | `/home/lucas/lucasTymenGraphx/landingpageCvPagePerso` |
| **Windows (accès WSL)** | `\\wsl$\Ubuntu\home\lucas\lucasTymenGraphx\landingpageCvPagePerso` ou `\\wsl.localhost\Ubuntu\home\lucas\lucasTymenGraphx\landingpageCvPagePerso` |

**Config LPPP** : variable d'environnement `LANDING_PERSO_REF_PATH` (défaut : `/home/lucas/lucasTymenGraphx/landingpageCvPagePerso`). Voir `lppp/settings.py` et `.env.example`.

Dans un script, un lien symbolique ou une doc, utiliser **toujours** le chemin absolu Linux ci-dessus pour cohérence.

---

## 3. Ce qu'on réutilise depuis le projet perso

- **Style** : couleurs (indigo/violet), polices (Inter), dégradés hero, animations (fadeInUp, slideInLeft, glow-pulse). Copié dans `templates/landing_pages/includes/perso_style.html`.
- **Graphiques / infographiques** : diagrammes personnalisés, funnels adaptés. À **copier** depuis le projet perso (dossier public/assets ou équivalent) vers LPPP (ex. `static/landing_pages/diagrams/`, `static/landing_pages/funnels/`) ou à héberger et référencer par URL dans `content_json`.
- **Usage** : pas systématique ; les blocs diagramme/funnel dans le template sont **optionnels** et s'affichent quand `content.diagram_url` ou `content.funnel_image_url` est renseigné. Voir § 5.

---

## 4. Schéma content_json (champs liés au fallback)

| Clé | Type | Description |
|-----|------|-------------|
| `use_perso_style` | bool | Si `true`, force le style perso (prioritaire sur le thème). |
| `theme.use_fallback` | bool | Si `true`, même effet que `use_perso_style` pour le thème. |
| `diagram_url` | string | URL d'une image ou asset de diagramme personnalisé (optionnel). |
| `funnel_image_url` | string | URL d'une image de funnel adapté (optionnel). |

Quand le fallback est actif, le template n'injecte pas `theme_css` (CSS Vampire) mais le bloc `perso_style.html` et la classe `lp-perso-style` sur `<body>`.

---

## 5. Template : diagrammes et funnels

Dans `templates/landing_pages/proposition.html` :

- Une section **« En un coup d'œil »** (id `diagramme-funnel`) est rendue **si** `content.diagram_url` ou `content.funnel_image_url` est défini.
- Les images sont affichées dans une carte avec bordures arrondies ; pas d’usage systématique, mais les blocs restent dans le template pour réutilisation (diagrammes / funnels copiés depuis le projet perso ou générés).

Pour alimenter : copier les assets depuis `LANDING_PERSO_REF_PATH` vers les statics LPPP et mettre les URLs dans `content_json`, ou renseigner des URLs externes.

---

## 6. Fichiers concernés

- **Config** : `lppp/settings.py` (`LANDING_PERSO_REF_PATH`), `.env.example`
- **Logique** : `apps/landing_pages/views.py` (`_use_perso_style`, contexte `use_perso_style`, `perso_ref_path`)
- **Style** : `templates/landing_pages/includes/perso_style.html` (variables CSS + animations)
- **Template** : `templates/landing_pages/proposition.html` (classe body, include perso, section diagramme/funnel)
- **Schéma** : `schema-landing-proposition.md` (à faire évoluer avec `diagram_url`, `funnel_image_url`, `use_perso_style`, `theme.use_fallback`)

---

*Dernière mise à jour : 2025-01-30.*
