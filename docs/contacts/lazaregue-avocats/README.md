# LAZARÈGUE AVOCATS — Sarah Hinderer

**Société** : LAZARÈGUE AVOCATS — Droit cyber / RGPD / conformité.  
**Contact** : Sarah Hinderer.  
**Stratégie** : Le choix « Niche / Argent » — appui technique via scripts, structuration de données ; proposition « Mission d’appui technique » pour un dossier complexe.

---

## Fichiers

| Fichier | Usage |
|---------|--------|
| `landing-proposition-sarah.json` | Contenu de la landing (hero, enjeux, services, rapport_url, alert_banner, seo_resume). Synchroniser en base : `python manage.py create_landing_lazaregue --update`. |
| `rapport-complet-lazaregue-avocats.md` | Page rapport (présentation + résumé + ancre `#analyse-seo-complete`). Contenu à compléter avec l’étude personnalisée fournie plus tard. Servi sur `/p/lazaregue-avocats/rapport/`. |
| `squelette-vs-inversion-complete.md` | Checklist squelette → inversion complète (thème, hero, rapport, démo). |

---

## Landing page

- **Slug** : `lazaregue-avocats`
- **URL** : `/p/lazaregue-avocats/`
- **Rapport** : `/p/lazaregue-avocats/rapport/`
- **Template** : `proposition`
- **CTA** : « Reprendre la conversation » ; bandeau : « Mission d'appui technique — données structurées sans tout faire à la main ».

---

## Checklist inversion complète

1. `create_landing_lazaregue --update` (et `--publish` si besoin).
2. **Thème** : `css_vampire <URL site cabinet>` --slug lazaregue-avocats --apply` (ou thème manuel si extraction insuffisante).
3. Remplir `rapport-complet-lazaregue-avocats.md` avec l’étude personnalisée (à fournir plus tard) ; mettre à jour `seo_resume` dans le JSON si chiffres clés.
4. Optionnel : `loom_embed_url`, `hero_background_url`.
5. Vérifier rendu sur `/p/lazaregue-avocats/`.

*Dernière mise à jour : 2025-01-30.*
