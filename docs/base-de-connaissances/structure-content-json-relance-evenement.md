# Structure content_json — template relance-evenement

**Rôle** : Schéma réutilisable pour le template `relance-evenement.html` (landing relance salon).  
**Pilote** : Rédacteur (contenu cas par cas), Chef de Projet (validation).  
**Référence** : `docs/base-de-connaissances/segmentations/2025-01-30-relance-evenements.md`.

---

## 1. Champs utilisés par le template

Le template `templates/landing_pages/relance-evenement.html` utilise les clés suivantes dans `content_json` (contenu **cas par cas** pour chaque prospect) :

| Clé | Type | Usage |
|-----|------|--------|
| `hero_title` | string | Titre principal (hero). Fallback : `landing_page.title`. |
| `hero_subtitle` | string | Sous-titre hero. Fallback : "Pour {prospect_company} — {prospect_name}". |
| `cta_text` | string | Libellé du bouton CTA. |
| `cta_url` | string | Lien du CTA (mailto:, tel:, ou URL). |
| `positionnement` | string | Bloc « Positionnement » (freelance / alternant selon matching). |
| `activite_pain_points` | string | Bloc « Votre activité & besoins » (ciblage activité, pain points). |
| `produit_commercial` | string | Bloc « Me contacter » (se présenter comme produit commercial à la fin). |

---

## 2. Exemple (à adapter cas par cas)

```json
{
  "hero_title": "On s’est croisés au salon — suite à notre échange",
  "hero_subtitle": "Pour [Société] — [Prénom]",
  "cta_text": "Prendre rendez-vous",
  "cta_url": "mailto:contact@exemple.com?subject=Relance salon",
  "positionnement": "Freelance en acquisition B2B & SEO, ou alternant selon votre besoin.",
  "activite_pain_points": "En partant de votre activité et de ce que je suppose être vos besoins et pain points…",
  "produit_commercial": "Je me présente comme un freelance (ou alternant) sérieux à envisager — prêt à en discuter."
}
```

---

## 3. Règle

- **Même structure** (mêmes champs) pour toutes les landing « relance-evenement ».
- **Contenu cas par cas** pour chaque prospect — sinon ça sonne faux. Le Rédacteur s’appuie sur les CV et segments (`docs/ressources-utilisateur/REGISTRE-RESSOURCES.md`, `fonction-premiere-et-segments-prospection.md`).

---

*Document créé par le Conseiller. Dernière mise à jour : 2025-01-30.*
