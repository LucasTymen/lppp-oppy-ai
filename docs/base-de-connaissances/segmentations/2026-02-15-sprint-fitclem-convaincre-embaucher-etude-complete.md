# Sprint FitClem — Convaincre d'embaucher : étude complète exposée

**Nom du livrable** : **LPPP-FitClem** — candidature Responsable Marketing Digital.

**Date** : 2026-02-15  
**Statut** : 🟡 En cours  
**Pilote responsable** : **Orchestrateur** — organise chaque agent au moment où il en a besoin, rend des comptes à l'utilisateur.  
**Objectif utilisateur** : **Convaincre FitClem de m'embaucher** en leur donnant **l'étude complète** (pas vendre des services). Les modifications doivent être **visibles sur la page** à chaque étape.

**Règle Git** : En clôture, commit + push sur les deux remotes (origin + gitlab). Réf. `git-remotes-github-gitlab.md`.

---

## 1. Objectif (ce que l'utilisateur veut)

- **Ne pas** : vendre mes services, faire du teasing ou des placeholders.
- **Oui** : **convaincre FitClem de m'embaucher** en leur **donnant l'étude complète** sur la page.
- **Visibilité** : à chaque étape, les modifications doivent **correspondre** à ce qui a été défini et être **visibles** sur http://localhost:8010/p/fitclem/ (ou l’URL de la landing FitClem).

L’**Orchestrateur** est responsable de l’organisation des agents et **rend des comptes** à l’utilisateur (points de contrôle, vérification que tout correspond).

---

## 2. Ce qui a été mis en place pour la visibilité

- **Chargement du contenu depuis le fichier** : pour le slug `fitclem`, la vue `landing_public` charge le contenu depuis `docs/contacts/fitclem/landing-proposition-fitclem.json` si le fichier existe. **Plus besoin de lancer `create_landing_fitclem --update`** pour voir les changements : toute modification du JSON est reflétée sur la page après rechargement.
- **Vérification** : après chaque modification du JSON ou des templates, l’agent concerné (ou l’Orchestrateur) vérifie que la page affiche bien le contenu attendu.

---

## 3. Étude complète = ce qui doit être exposé sur la page

Pour **convaincre d’embaucher**, la page doit exposer **l’étude complète**, pas des résumés ou des liens « voir le rapport ». Contenu à exposer (à partir de `strategie-marketing-fitclem.md`, `strategie-marketing-fitclem-complet.md`, fichier Stratégie Marketing utilisateur) :

| Bloc | Contenu attendu (complet) |
|------|---------------------------|
| **Intro / positionnement** | Contexte candidature + valeur ajoutée (growth, data, ADN marque) — ton « je vous montre comment je travaillerais ». |
| **Enjeux** | Leviers concrets (conversion, SEO, KPI, CRM, compliance) — listés clairement. |
| **Étude marketing** | **PESTEL** (tableau ou paragraphes complets), **SWOT** (forces, faiblesses, opportunités, menaces), **Porter** (5 forces + rôle État), **Concurrentiel** (tableau Trainsweateat, Luce Citron, retailers + différenciation FitClem), **Growth & positionnement** (alignement Ads → Landing, preuve, playbook claims). Pas de simple « synthèse en une ligne ». |
| **Étude SEO** | **Manque à gagner** (132–324 k€/an), **problèmes clés** (performance, 429, H1, alt), **recommandations** et structure prête. Données réelles du rapport / stratégie, pas « à fournir plus tard ». |
| **Proposition KPI** | **6 KPI** (CAC, CVR, AOV, LTV, email revenue share, rétention D30/D60), **plan 0–30 j** et **30–60 j** détaillé, **phrase de synthèse** pour l’entretien. |
| **Chiffres clés / carousel** | Chiffres frappants + graphiques (manque à gagner, timeline 30/60 j) — déjà en place, à garder. |
| **Contact / CTA** | Ton « on en parle ? » / « prêt à en discuter » (convaincre d’embaucher), pas « achetez mes services ». |

---

## 4. Rôles et tâches (Orchestrateur : organiser et rendre des comptes)

### 4.1 Orchestrateur (pilote du sprint)

- [ ] **Lancer** le sprint et diffuser cette segmentation aux agents concernés (Rédacteur, Designer, Dev Django, Chef de Projet).
- [ ] **Ordonnancer** : appeler chaque agent au moment où sa tâche est nécessaire ; vérifier que les livrables sont déposés et que la page reflète les changements.
- [ ] **Points de contrôle** : après chaque étape majeure, vérifier que le contenu affiché sur la page correspond à ce qui a été défini et à la demande utilisateur (étude complète, convaincre d’embaucher).
- [ ] **Rendre des comptes** à l’utilisateur : résumé de ce qui a été fait, ce qui est visible sur la page, et éventuels points restants ou blocages.

### 4.2 Rédacteur

- [x] **Relecture objectif** : tout texte doit viser à **convaincre d’embaucher** (pas vendre des services). Adapter intro, icebreaker, CTA, mission flash en conséquence.
- [x] **Étude complète dans le contenu** : alimenter `landing-proposition-fitclem.json` (ou les templates si structure multipage) avec **l’étude complète** :
  - **Étude marketing** : texte complet PESTEL, SWOT, Porter, concurrentiel, growth (d’après stratégie marketing). Les onglets / sections doivent contenir le fond, pas une seule phrase.
  - **Étude SEO** : manque à gagner, problèmes, axes, recommandations (données du rapport et de la stratégie). Pas de placeholder « données à fournir ».
  - **Proposition KPI** : 6 KPI détaillés, plan 0–30 j et 30–60 j en texte actionnable, phrase de synthèse.
- [x] **Livrable** : contenu intégré dans le JSON (ou fichier de contenu) ; vérification que la page affiche bien l’étude complète après rechargement.

### 4.3 Designer

- [ ] **Charte FitClem** : appliquer `docs/contacts/fitclem/charte-graphique-fitclem.md` pour cohérence visuelle.
- [ ] **Responsive** : mobile-first, tous devices (règle explicite projet). Vérifier que la page s’affiche correctement sur mobile, tablette, desktop.
- [ ] **Hiérarchie** : sections « étude complète » lisibles (titres, sous-titres, blocs bien séparés) pour que FitClem puisse parcourir l’étude sans confusion.

### 4.4 Dev Django

- [ ] **Visibilité** : la vue charge déjà le contenu FitClem depuis le fichier JSON (slug `fitclem`). Vérifier que la route `/p/fitclem/` affiche bien le template avec le contenu du fichier.
- [ ] **Template** : si le contenu « étude complète » nécessite de nouvelles sections ou champs (ex. blocs PESTEL, SWOT détaillés), ajouter les blocs dans le template et s’assurer que le JSON peut les alimenter (ou étendre le JSON avec les clés nécessaires).

### 4.5 Chef de Projet

- [ ] **Validation** : vérifier que le livrable final correspond à « convaincre d’embaucher » et « étude complète exposée ».
- [ ] **Logs** : mise à jour de `docs/logs/log-projet.md` (et `log-ia.md` si pertinent) en fin de sprint.

---

## 5. Critères de succès (vérification à chaque étape)

- [ ] **Objectif** : la page vise clairement à **convaincre FitClem de m’embaucher** (ton et CTA), pas à vendre des services.
- [ ] **Étude complète** : PESTEL, SWOT, Porter, concurrentiel, growth, SEO (manque à gagner, problèmes, reco), KPI et plan 30/60 j sont **exposés en entier** sur la page (ou sur les pages dédiées si multipage), sans placeholder « à venir ».
- [ ] **Visibilité** : les modifications sont **visibles** sur http://localhost:8010/p/fitclem/ (contenu chargé depuis le fichier JSON).
- [ ] **Orchestrateur** : a organisé les agents, vérifié les livrables et **rendu des comptes** à l’utilisateur.

---

## 6. Fichiers et références

| Ressource | Emplacement |
|-----------|-------------|
| Contenu (source de vérité) | `docs/contacts/fitclem/landing-proposition-fitclem.json` |
| Stratégie (synthèse) | `docs/contacts/fitclem/strategie-marketing-fitclem.md` |
| Stratégie (complet) | `docs/contacts/fitclem/strategie-marketing-fitclem-complet.md` |
| Charte graphique | `docs/contacts/fitclem/charte-graphique-fitclem.md` |
| Vue (chargement FitClem) | `apps/landing_pages/views.py` (landing_public, slug fitclem) |
| Template landing | `templates/landing_pages/proposition.html` |
| Registre / Orchestrateur | `docs/base-de-connaissances/registre-agents-ressources.md`, `.cursor/rules/orchestrateur.mdc` |
| Suite à améliorer (vidéo, charte, ton) | `docs/contacts/fitclem/suite-a-ameliorer-fitclem.md` |

---

## 7. Ordre de travail suggéré (Orchestrateur)

1. **Vérifier la visibilité** : confirmer que la vue charge bien le JSON pour `fitclem` et que l’utilisateur peut voir le contenu actuel sur la page.
2. **Rédacteur** : compléter le JSON (et/ou contenu) avec **l’étude complète** (PESTEL, SWOT, Porter, concurrentiel, SEO, KPI, plan 30/60 j) ; adapter le ton « convaincre d’embaucher ». Point de contrôle : recharger la page et vérifier que tout s’affiche.
3. **Designer** : appliquer la charte FitClem, vérifier responsive. Point de contrôle : affichage correct sur plusieurs largeurs.
4. **Dev Django** : si besoin, étendre le template pour afficher les nouveaux blocs (étude détaillée). Point de contrôle : aucune régression, page cohérente.
5. **Chef de Projet** : validation finale ; **Orchestrateur** : rendre compte à l’utilisateur (résumé livré, critères de succès, suite éventuelle).

---

*Sprint créé pour aligner le livrable FitClem sur l’objectif « convaincre d’embaucher » et « étude complète », avec l’Orchestrateur comme pilote responsable devant rendre des comptes. Dernière mise à jour : 2026-02-15.*
