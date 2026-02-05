# LAZARÈGUE AVOCATS — Squelette vs inversion complète

**Objectif** : Passer d’une landing « structure » à une page prête à envoyer à Sarah Hinderer.

Référence : `docs/base-de-connaissances/strategie-qualite-contenu-landings.md`, `docs/contacts/0flow/squelette-vs-inversion-complete.md`.

---

## 1. Squelette (état actuel)

| Élément | État |
|--------|------|
| **Contenu** | JSON rempli (hero, enjeux, services, rapport_url, alert_banner, seo_resume). |
| **Rapport** | `rapport-complet-lazaregue-avocats.md` présent mais contenu à compléter (étude personnalisée à venir). |
| **Thème** | Style perso par défaut tant que CSS Vampire (ou thème manuel) non appliqué. |
| **Hero** | Dégradé générique sauf si `hero_background_url` ou thème fourni. |

---

## 2. Inversion complète

| Élément | À faire |
|--------|---------|
| **Contenu** | Déjà en place ; compléter `seo_resume` et rapport quand l’étude est fournie. |
| **Thème** | `css_vampire <URL site cabinet> --slug lazaregue-avocats --apply` ou thème manuel si besoin. |
| **Rapport** | Remplir `rapport-complet-lazaregue-avocats.md` (analyse complète, gains, plan d’action) ; ancre `#analyse-seo-complete` déjà en place. |
| **Optionnel** | `loom_embed_url`, `hero_background_url`. |

---

## 3. Checklist

| # | Action | Commande / Fichier |
|---|--------|---------------------|
| 1 | Mettre le contenu en base | `python manage.py create_landing_lazaregue --update` |
| 2 | Appliquer le thème (site cabinet) | `python manage.py css_vampire <URL> --slug lazaregue-avocats --apply` |
| 3 | Compléter le rapport | Éditer `rapport-complet-lazaregue-avocats.md` ; mettre à jour `seo_resume` dans le JSON si besoin |
| 4 | Vérifier | `/p/lazaregue-avocats/` et `/p/lazaregue-avocats/rapport/` |

*Dernière mise à jour : 2025-01-30.*
