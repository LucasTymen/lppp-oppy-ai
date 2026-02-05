# ORSYS — Aboubakar Timite

**Société** : ORSYS — Formation IT (grosse machine, besoin permanent de remplir les sessions).  
**Contact** : Aboubakar Timite (profil opérationnel).  
**Stratégie** : Le choix « Volume » — scraping offres d’emploi pour détecter les besoins formation, leads sur un plateau.

---

## Fichiers

| Fichier | Usage |
|---------|--------|
| `landing-proposition-aboubakar.json` | Contenu de la landing (angle **données terrain**, signaux faibles, restructuration, conformité IA Act). Synchroniser en base : `python manage.py create_landing_orsys --update`. |
| `rapport-complet-orsys.md` | Page rapport : **Diagnostic SEO** (crawl fév. 2026, données des CSV), PESTEL, Porter, SWOT, concurrence, **script contrat**. Servi sur `/p/orsys/rapport/`. |
| **`argumentaire-et-voix-orsys.md`** | **Brief Rédaction & Design** : message central, vocabulaire à privilégier/éviter, contexte 2026. Inclut les **éléments à remonter dans la lettre** qui accompagne le rapport. |
| **`lettre-accompagnement-rapport-orsys.md`** | **Modèle mail/lettre** pour proposer le rapport à Aboubakar : éléments importants à faire remonter, ton (données terrain), phrase du script. À adapter par la rédaction. |
| `squelette-vs-inversion-complete.md` | Checklist squelette → inversion complète (thème, hero, rapport, démo). |

---

## Landing page

- **Slug** : `orsys`
- **URL** : `/p/orsys/`
- **Rapport** : `/p/orsys/rapport/`
- **Template** : `proposition`
- **Thème** : injecté par `create_landing_orsys` (bleu navy #223B86, rose #E91E63, teal #00A9BE — ref. orsys.fr).
- **Hero** : fond vidéo YouTube en boucle, muet (`hero_video_url`), ou image si désactivé.
- **Onglet « Conseils & Stratégie »** : premier onglet « Ce que j'offre » = pitch machine de guerre / signaux faibles (marketing).
- **CTA** : « Reprendre la conversation » ; bandeau : « Signaux faibles & budgets restructuration / conformité IA Act ». Ton : **données terrain** en lettre ; marketing dans l’onglet conseils (voir `argumentaire-et-voix-orsys.md`).

---

## Checklist inversion complète

1. `create_landing_orsys --update` (et `--publish` si besoin).
2. **Thème** : `css_vampire https://www.orsys.fr/ --slug orsys --apply` (ou thème manuel si extraction insuffisante).
3. Remplir `rapport-complet-orsys.md` avec l’étude personnalisée (à fournir plus tard) ; mettre à jour `seo_resume` dans le JSON si chiffres clés.
4. Optionnel : `loom_embed_url`, `hero_background_url`.
5. Vérifier rendu sur `/p/orsys/`.

*Dernière mise à jour : 2025-01-30.*
