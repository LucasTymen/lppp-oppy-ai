# Contenu landing page P4S — Proposition personnelle (Joël Courtois)

**Contexte** : Suite à un échange positif avec Joël Courtois (CEO, docteur en IA, ancien DG EPITA). Proposition de ce que tu peux faire pour P4S. Ton : courtois, chaleureux, personnel.

**Template utilisé** : `proposition.html` (structure content_json).

> **Si tu ne vois pas** l'onglet « Qui je suis », ni Paid Media, ni les liens « Consulter le rapport » : le contenu affiché vient de la **base de données**. Exécuter `python manage.py create_landing_p4s --update` puis recharger sans cache. Voir aussi `brief-integration-redaction-style.md`.

---

## Appliquer les modifications en base

**Après toute modification de `landing-proposition-joel.json`**, lancer la commande pour mettre à jour la base :

```bash
python manage.py create_landing_p4s --update
```

(Dans Docker : `docker compose exec web python manage.py create_landing_p4s --update`.)

Sans cette étape, les changements dans le fichier JSON **ne s'affichent pas** sur la landing (le contenu affiché vient de la base). Voir `docs/base-de-connaissances/procedure-modifications-landing-visible.md`.

---

## content_json

Schéma template **proposition** : `docs/base-de-connaissances/schema-landing-proposition.md`.  
Fichier source : `landing-proposition-joel.json`.

- **page_title** : titre de la page (pas la phrase d’accroche).
- **intro** : phrase d’accroche comme texte d’intro.
- **icebreaker** : contexte de prospection (où et comment vous vous êtes rencontrés, ce qui a accroché). Ex. P4S : rencontre au Cyber Security Show à Champerret, discussion tech / IoT, écoute et contact chaleureux de Joël, pertinence des produits.
- **about_me** : texte de l'onglet « Qui je suis » (premier onglet de « Ce que j'offre »). Tu peux reprendre le bloc de présentation de ta landing page CV (référence `design-brief-landing-reference-cv.md`) : copier-coller le paragraphe « à propos » ici. Les retours à la ligne sont conservés.
- **about_me_title** : libellé de l'onglet (défaut : « Qui je suis »).

---

## À faire avant envoi

Remplace **VOTRE_EMAIL** dans `cta_url` par ton adresse mail réelle. Quand Joël clique sur « Reprendre la conversation », le mail part vers toi.

---

## Notes pour personnalisation

- **Prénom** : "Joël" dans le titre pour garder le ton personnel.
- **Référence à l’étude** : mentionnée dans le bloc final pour montrer le travail préparatoire sans être lourd.
- **Pas d’emphase corporate** : formulation directe, "je", "vous", comme dans un mail.
- **Angle concret** : veille incidents cyber + ciblage décideurs + automatisation — aligné avec le verdict de l’étude P4S.
