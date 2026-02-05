# Sprint — Finaliser landing ORSYS (design + rédaction)

**Date** : 2026-02  
**Statut** : 🟡 En cours  
**Objectif** : Finaliser la landing ORSYS (Aboubakar) : afficher la **vidéo hero** (YouTube en boucle, muet), le **thème ORSYS** (couleurs/style orsys.fr), le **lien vers le rapport complet** (résumé SEO + analyse), et aligner rédaction/design sur la structure « offensive » déjà en place.

**Règle Git** : En clôture : commit + push sur les deux remotes (`make push-both`). Réf. `git-remotes-github-gitlab.md`.

---

## Problème constaté

- Sur **/p/orsys/** : ni la **vidéo de fond** (hero) ni le **thème repris d’ORSYS** ne s’affichent.
- Parfois **VariableDoesNotExist** si une clé manque dans `content_json` (ex. `positionnement`).
- Souhait : résumé SEO visible sur la page avec **lien cliquable vers le rapport complet** (analyse PESTEL, Porter, SWOT, script).

---

## Cause technique (vidéo + thème)

Le **thème** (couleurs, logo) et la **vidéo hero** sont injectés dans le `content_json` **uniquement** lors de l’exécution de la commande `create_landing_orsys`. Si la landing existe déjà en base sans avoir été mise à jour, le contenu en DB n’a pas `theme`, `theme_css` ni `hero_video_url`.

**Action immédiate (Dev Django / DevOps)** : exécuter en environnement de travail (WSL, à la racine du projet) :

```bash
python3 manage.py create_landing_orsys --update --publish
```

Cela recharge `docs/contacts/orsys/landing-proposition-aboubakar.json` et réinjecte `theme`, `theme_css` et tout le contenu (dont `hero_video_url`). Ensuite recharger **http://127.0.0.1:8082/p/orsys/** (ou l’URL Django utilisée).

---

## Tâches par agent

### Design

- [ ] Vérifier que le thème ORSYS (navy, rose/magenta, teal) s’affiche après `create_landing_orsys --update` (nav, blocs, CTA).
- [ ] Si besoin : tester **CSS Vampire** sur https://www.orsys.fr pour extraire couleurs/dégradés et mettre à jour `create_landing_orsys.py` (THEME_ORSYS / THEME_CSS_ORSYS) ; sinon conserver le thème manuel actuel.
- [ ] Confirmer que la **vidéo YouTube** (hero, boucle, muet) s’affiche correctement en fond du hero.

### Rédaction

- [ ] Vérifier que la section **Résumé SEO** (diagnostic « Fuite de cash ») affiche bien un **lien vers l’analyse complète** (`rapport_url#analyse-seo-complete`) avec le libellé `seo_resume.lien_analyse` (ex. « Voir le diagnostic SEO complet et l’analyse (PESTEL, Porter, SWOT, script) → »).
- [ ] S’assurer que le ton reste **données terrain**, **reprise de contact agréable**, sans approche lourde ni spam (cf. `argumentaire-et-voix-orsys.md`, lettre d’accompagnement).
- [ ] Valider les textes : promesse choc, cas d’usage (Radar levées, Alerte stack, IA Act), Pack Commando 5 jours.

### Dev Django

- [ ] Exécuter `python3 manage.py create_landing_orsys --update --publish` pour injecter theme + theme_css + hero_video_url en base.
- [ ] Vérifier que `_content_with_defaults` dans `views.py` inclut bien `positionnement` (et autres clés optionnelles du template) pour éviter VariableDoesNotExist.
- [ ] Confirmer que le template `proposition.html` utilise bien `content.rapport_url` et `content.seo_resume.lien_analyse` pour le lien « Voir l’analyse complète ».

### Chef de Projet

- [ ] Valider en navigateur : /p/orsys/ affiche thème ORSYS, vidéo hero (boucle, muet), résumé SEO avec lien vers rapport complet.
- [ ] Mettre à jour ce sprint (statut 🟢 Terminé) et `docs/logs/log-projet.md` en fin de sprint.
- [ ] S’assurer que les fiches de mission (brief ORSYS, schema-landing-proposition, strategie-qualite-contenu-landings) restent à jour.

---

## Critères de succès

- [ ] **Vidéo** : fond hero en boucle, muet, visible sur /p/orsys/.
- [ ] **Thème** : couleurs / style ORSYS visibles (nav, blocs, CTA).
- [ ] **Rapport** : bloc « Diagnostic Fuite de cash » avec lien cliquable vers rapport complet (PESTEL, Porter, SWOT, script).
- [ ] Aucune erreur VariableDoesNotExist sur /p/orsys/.

---

## Références

- `docs/contacts/orsys/argumentaire-et-voix-orsys.md`
- `docs/contacts/orsys/landing-proposition-aboubakar.json`
- `apps/landing_pages/management/commands/create_landing_orsys.py`
- `docs/base-de-connaissances/schema-landing-proposition.md` (seo_resume, rapport_url)
- Style ORSYS : https://www.orsys.fr/
