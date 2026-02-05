# ORSYS — Squelette vs inversion complète

**Objectif** : Passer d’une landing « structure » à une page prête à envoyer à Aboubakar Timite.

Référence : `docs/base-de-connaissances/strategie-qualite-contenu-landings.md`, `docs/contacts/0flow/squelette-vs-inversion-complete.md`.

---

## 1. Squelette (état actuel)

| Élément | État |
|--------|------|
| **Contenu** | JSON rempli (hero, enjeux, services, rapport_url, alert_banner, seo_resume). |
| **Rapport** | `rapport-complet-orsys.md` présent mais contenu à compléter (étude personnalisée à venir). |
| **Thème** | Style perso par défaut tant que CSS Vampire (ou thème manuel) non appliqué. |
| **Hero** | Dégradé générique sauf si `hero_background_url` ou thème fourni. |

---

## 2. Inversion complète

| Élément | À faire |
|--------|---------|
| **Contenu** | Déjà en place ; compléter `seo_resume` et rapport quand l’étude est fournie. |
| **Thème** | `css_vampire https://www.orsys.fr/ --slug orsys --apply` ou thème manuel si besoin. |
| **Rapport** | Remplir `rapport-complet-orsys.md` (analyse complète, chiffres) ; ancre `#analyse-seo-complete` déjà en place. |
| **Optionnel** | `loom_embed_url`, `hero_background_url`. |

---

## 3. Checklist

| # | Action | Commande / Fichier |
|---|--------|---------------------|
| 1 | Mettre le contenu en base | `python manage.py create_landing_orsys --update` |
| 2 | Appliquer le thème (site ORSYS) | `python manage.py css_vampire https://www.orsys.fr/ --slug orsys --apply` |
| 3 | Compléter le rapport | Éditer `rapport-complet-orsys.md` ; mettre à jour `seo_resume` dans le JSON si besoin |
| 4 | Vérifier | `/p/orsys/` et `/p/orsys/rapport/` |

*Dernière mise à jour : 2025-01-30.*
