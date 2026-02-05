# 0Flow (zéro-flow) — Samson Fedida

**Société** : 0Flow — Workflow Automation & Productivité (cybersécurité / automation).  
**Contact** : Samson Fedida — samson.fedida@0flaw.fr  
**Landing** : proposition personnalisée pour l'entretien (PoC automation, pas un CV).

---

## Fichiers

| Fichier | Usage |
|---------|--------|
| `landing-proposition-samson.json` | Contenu complet de la landing (hero, 0Flow Solution, enjeux, services = Insight Cards, stack, mission flash, coordonnées). À synchroniser en base via `python3 manage.py create_landing_0flow --update`. |
| `etude-concurrentielle-pestel-swot-porter.md` | SWOT, PESTEL, Porter, concurrence — pour le rapport d'audit et la préparation entretien. |
| **`style-voix-et-design-0flaw.md`** | **Brief Rédacteur & Designer** : voix et ton 0Flaw (vocabulaire, CTA, à éviter) + procédure **CSS Vampire** sur https://0flaw.fr/ pour appliquer le thème visuel à la landing 0flow. |
| `etude-seo-0flaw-manque-a-gagner.md` | **Étude SEO** : problèmes identifiés (4xx, H1, non-indexables, Referrer-Policy, titres dupliqués, canoniques), hypothèses B2B cyber, **manque à gagner ~2 500 €/mois (~30 000 €/an)**, plan d’action priorisé et export tâches dev/rédacteurs. |
| **`squelette-vs-inversion-complete.md`** | **Squelette vs inversion complète** : différence page générique vs page prête à envoyer (thème 0Flaw, logo, Loom, rapport) + checklist. |
| `rapport-complet-0flow.md` | **Page rapport** : présentation (qui je suis, contexte 0Flow), résumé SEO (chiffres, priorités), puis analyse SEO complète (ancre `#analyse-seo-complete`). Servie sur `/p/0flow/rapport/`. |

---

## Squelette vs inversion complète

| | **Squelette** | **Inversion complète** |
|---|----------------|-------------------------|
| Contenu | JSON rempli, sections OK | Idem |
| Thème | Style perso (inter/indigo) — générique | **CSS Vampire 0flaw.fr** → couleurs, polices, **logo 0Flaw** |
| Hero | Dégradé générique | Dégradé ou fond issu du thème 0Flaw |
| Démo / Rapport | Souvent vides | `loom_embed_url` + `rapport_url` renseignés |
| **Résultat** | Page correcte mais impersonnelle | **Page finale, prête à envoyer** |

**Pour inverser** : 1) `create_landing_0flow --update` 2) `css_vampire https://0flaw.fr/ --slug 0flow --apply` 3) optionnel : Loom + `rapport_url` puis re-`--update`. Détail : **`squelette-vs-inversion-complete.md`**.

---

## Landing page

- **Slug** : `0flow`
- **URL** : `/p/0flow/`
- **Rapport (présentation + SEO)** : `/p/0flow/rapport/` — page pour te présenter avec résumé SEO et lien vers l’analyse complète (ancre `#analyse-seo-complete`).
- **Template** : `proposition`
- **CTA** : « Télécharger mon rapport d'audit d'automatisation » ; section **Résumé SEO** sur la landing avec lien « Voir l'analyse SEO complète » vers le rapport.
- **Hero (fond)** : `hero_background_url` = `/static/landing_pages/images/hero-0flow.png` (image cyberpunk/tech en fond, parallaxe + overlay). Fichier source : `apps/landing_pages/static/landing_pages/images/hero-0flow.png`.
- **Démo Loom** : renseigner `loom_embed_url` dans le JSON (ex. `https://www.loom.com/embed/xxx`) puis `create_landing_0flow --update` pour afficher la section « Démo 60 sec ».

---

## Style voix + design (Rédacteur / Designer)

- **Voix** : s’aligner sur le style 0Flaw (professionnel, direct, vocabulaire cyber/automation, CTA type « Réserver une démo »). Voir **`style-voix-et-design-0flaw.md`**.
- **Design** : thème **manuel** 0Flaw (navy, teal, dégradé hero, bandeau) injecté par `create_landing_0flow` — pas besoin de CSS Vampire pour 0flow.

## Checklist entretien

- [ ] Vidéo Loom 60–90 sec finalisée (scraper → données enrichies → CRM ou équivalent).
- [ ] `loom_embed_url` mis à jour dans `landing-proposition-samson.json` puis `create_landing_0flow --update`.
- [ ] **CSS Vampire** exécuté sur https://0flaw.fr/ pour le thème 0flow (voir `style-voix-et-design-0flaw.md`).
- [ ] QR code pointant vers `/p/0flow/` (ou URL de prod).
- [ ] Rapport d'audit (ce document ou une version PDF) lié via `rapport_url` si souhaité.

---

## Repo et déploiement (LPPP_0flow)

- **GitHub** : [LucasTymen/LPPP_0flow](https://github.com/LucasTymen/LPPP_0flow) — repo dédié à la landing 0Flow (page statique pour Vercel).
- **GitLab** : [LucasTymen/LPPP_0flow](https://gitlab.com/LucasTymen/LPPP_0flow) — `git@gitlab.com:LucasTymen/LPPP_0flow.git` (miroir, push sur les deux).
- **Vercel** : projet lié au repo GitHub LPPP_0flow ; Root Directory = `./`, pas de build (page statique).
- **Procédure push** : voir **`deploy/PUSH-LPPP-0FLOW.md`** (régénérer l’export, clone/copie, push origin + gitlab, config Vercel).
- **URL de prod** : à renseigner après premier déploiement (ex. `https://lppp-0flow.vercel.app`).
