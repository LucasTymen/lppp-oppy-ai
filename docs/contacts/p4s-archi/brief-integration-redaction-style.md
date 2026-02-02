# Brief intégration — Rédaction et style (landing P4S)

**Pour** : Rédacteur, Designer (règle editorial.mdc).  
**Objectif** : que la landing P4S affiche tout ce qui a été préparé (Qui je suis, rapport, prospects, proposition de valeur, services dont Paid Media) et que le rendu soit **précis et différenciant**, pas vide.

---

## 1. Ce qui doit apparaître sur la page (Django template `proposition`)

| Élément | Où | Comment |
|--------|-----|--------|
| **Onglet « Qui je suis »** | Section « Ce que j'offre » — **premier onglet** | Contenu dans `content_json.about_me` (liste complète : Paid Media, SEO, Data, Growth, création & optimisation + 4 offres). Si absent → la **base n'a pas été mise à jour** (voir § 3). |
| **Onglet Paid Media** | Section « Ce que j'offre » | Dans `content_json.services` (objet « Paid Media (Google Ads, Meta Ads) »). Idem : visible seulement après mise à jour base. |
| **Lien « Consulter le rapport complet »** | Nav sticky **et** dans la section « Ce que j'offre » (sous le titre) | Liens vers `/p/p4s-archi/rapport/`, `/p/p4s-archi/prospects/`, `/p/p4s-archi/proposition/`. Visibles dans la nav et en ligne sous « Ce que j'offre » (Consulter le rapport complet · Prospects · Proposition de valeur). |
| **Services** | Onglets « Ce que j'offre » | Rapport SEO, Paid Media, Échantillon de prospects, Automatisations et workflows, Autres livrables. Source : `landing-proposition-joel.json` → base après `--update`. |

---

## 2. Rôle Rédacteur / Designer

- **Rédacteur** : s'assurer que le contenu dans `landing-proposition-joel.json` est à jour (about_me, services, intro, pain_points, etc.). Pas de contenu en base = page vide ou ancienne. Référence : `docs/base-de-connaissances/positionnement-freelance-offres.md`, `schema-landing-proposition.md`.
- **Designer** : vérifier que la nav (Enjeux, Solution, Services, Consulter le rapport, Prospects, Proposition de valeur, CTA) est lisible sur mobile (wrap, pas de masquage). Vérifier la lisibilité des liens « Consulter le rapport complet · Prospects · Proposition de valeur » dans la section 03. Style : cohérent avec le thème (couleur primaire pour les liens).

---

## 3. Procédure obligatoire : mettre à jour la base après modification du JSON

**La landing affiche le contenu stocké en base (LandingPage.content_json), pas le fichier JSON directement.**

Après toute modification de `landing-proposition-joel.json` :

```bash
python manage.py create_landing_p4s --update
```

(Dans Docker : `docker compose exec web python manage.py create_landing_p4s --update`.)

Puis recharger la page **sans cache** (Ctrl+Shift+R ou Cmd+Shift+R).

Sans cette étape : pas d'onglet « Qui je suis », pas de Paid Media, pas de texte about_me mis à jour. Voir `content-json-proposition.md` et `procedure-modifications-landing-visible.md`.

---

## 4. URL à consulter

- **Landing Django (source de vérité pour cette structure)** : `/p/p4s-archi/` (backend LPPP).
- **Page Next.js** (`/p4s-archi`) : page simplifiée distincte ; si tu veux la même structure (Qui je suis, rapport, services), il faudra aligner le frontend Next.js sur le contenu Django ou sur le même JSON.

---

## 5. Checklist avant envoi

- [ ] `create_landing_p4s --update` exécuté après dernière modif du JSON.
- [ ] Onglet « Qui je suis » visible (premier onglet de « Ce que j'offre »).
- [ ] Onglet « Paid Media » visible dans les services.
- [ ] Liens « Consulter le rapport complet », « Prospects », « Proposition de valeur » visibles (nav + dans section 03).
- [ ] CTA et email (remplacer VOTRE_EMAIL dans `cta_url`) vérifiés.

---

*Brief créé pour l'équipe rédaction et style. Dernière mise à jour : 2025-01-30.*
