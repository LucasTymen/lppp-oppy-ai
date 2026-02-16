# Sprint éditorial, webdesign et infographique — FitClem (contenu rempli, illustré, animé)

**Nom du livrable** : **LPPP-FitClem** — contenu complet (sortir du squelette).

**Date** : 2026-02-15  
**Statut** : 🟡 En cours  
**Pilote** : **Chef de Projet** (supervision scrum, validation livrables).  
**Rôles** : Rédacteur (éditorial), Designer (webdesign, charte FitClem), Infographiste (dataviz, chiffres clés).

**Règle Git** : En clôture de livraison, **commit + push sur les deux remotes** (origin + gitlab). Réf. `git-remotes-github-gitlab.md`.

---

## 1. Objectif

Remplir, illustrer et animer le contenu de la landing FitClem : aujourd’hui **squelette** (phrases courtes, listes génériques). Le livrable doit refléter l’étude réelle (stratégie marketing, PESTEL, SWOT, Porter, concurrentiel, growth, KPI, plan 30/60 j) et offrir une expérience **éditoriale et visuelle** au niveau candidature Responsable Marketing Digital.

**Source de contenu** :  
- `docs/contacts/fitclem/strategie-marketing-fitclem.md` (synthèse)  
- `docs/contacts/fitclem/strategie-marketing-fitclem-complet.md` (détails)  
- Fichier utilisateur **Stratégie Marketing** (Downloads) — échanges Gemini/GPT : ADN, PESTEL, SWOT, Porter, concurrentiel, Ads Meta, copywriting, graphique/icono, KPI, plan 30/60 j, message house, A/B tests.

---

## 2. Périmètre du sprint

| Domaine | Remplir | Illustrer | Animer |
|--------|---------|------------|--------|
| **Éditorial** | Textes complets (intro, enjeux, solution, services, SEO, mission, about) à partir de la stratégie | — | Formulations percutantes, bullets actionnables |
| **Webdesign** | Cohérence charte FitClem (couleurs, typo, CTA) | Hiérarchie, sections, icônes, blocs “preuve” / “routine” | Micro-interactions, lisibilité, scan mode |
| **Infographique** | Chiffres clés (KPI, manque à gagner SEO, plan 30/60 j) | Infographie(s) HTML type Pictochart (PESTEL, SWOT, ou KPI) | Option : petite animation ou reveal au scroll |

---

## 3. Rôles et tâches (sous supervision Chef de Projet)

### 3.1 Chef de Projet

- [ ] **Superviser le scrum** : prioriser remplir → illustrer → animer ; valider les livrables par rôle.
- [ ] **Valider** que le contenu reflète la stratégie (pas de contenu inventé) ; valider charte FitClem (réf. `charte-graphique-fitclem.md`).
- [ ] **Clôture** : mise à jour `log-projet.md`, `TODO.md` ; commit + push si livraison complète.

### 3.2 Rédacteur

- [x] **Remplir** tous les champs de la landing à partir des sources (fait 2026-02-15 : contenu intégré dans `landing-proposition-fitclem.json`). (stratégie, stratégie-complet, fichier Stratégie Marketing) :
  - **Intro / icebreaker** : candidature + valeur ajoutée (growth, data, ADN communautaire).
  - **Enjeux (pain_points)** : 3–5 leviers concrets (conversion, SEO, UX, CRO, CRM, compliance).
  - **Solution** : synthèse méthodo (PESTEL, SWOT, Porter, concurrentiel) + proposition valeur (alignement Ads → Landing, playbook claims, plan 30/60 j).
  - **Services (3 onglets)** :  
    - **Étude marketing** : PESTEL, SWOT, Porter, étude concurrentielle, growth & positionnement (texte riche, pas une ligne).  
    - **Étude SEO** : structure prête, manque à gagner 132–324 k€/an, axes techniques (H1, alt, perfs), lien rapport.  
    - **Proposition KPI** : 6 KPI (CAC, CVR, AOV, LTV, email revenue share, rétention D30/D60), plan 0–30 j et 30–60 j, phrase de synthèse entretien.
  - **Résumé SEO** : manque à gagner, problèmes clés, lien analyse.
  - **Mission flash / Why growth engineer** : phrases “prêtes entretien” (synthèse stratégie).
  - **About me** : profil Growth Engineer, livrable opérationnel.
- [ ] **Ton** : professionnel, candidature RMD ; pas de promesses vagues ; données et recommandations actionnables.
- [ ] **Livrable** : contenu intégré dans `docs/contacts/fitclem/landing-proposition-fitclem.json` (ou fichier `content-landing-fitclem.md` pour reprise par Dev).

### 3.3 Designer (webdesign)

- [ ] **Charte FitClem** : appliquer strictement `docs/contacts/fitclem/charte-graphique-fitclem.md` (palette, typo, boutons, sections douces, border-radius, ombres).
- [ ] **Illustrer** : renforcer la hiérarchie (H1 bénéfice, H2 mécanisme, bullets, preuve, CTA) ; proposer emplacements pour icônes ou pictos (enjeux, services, KPI) ; section “preuve” / “plan 30/60 j” lisible (scan mode).
- [ ] **Animer** : micro-interactions (hover CTA, reveal léger au scroll si déjà en place), lisibilité mobile.
- [ ] **Livrable** : ajustements CSS/variables sur le template ou la page FitClem ; instructions claires pour intégration (réf. theming-landing-prospect.md § charte FITCLEM).

### 3.4 Infographiste (InfographicCraft)

- [ ] **Brief** : thème = candidature FitClem ; audience = recruteur / Clémentine Sarlat ; données = PESTEL, SWOT, ou 6 KPI + plan 30/60 j (selon priorité Chef de Projet).
- [ ] **Livrable** : une infographie HTML autonome (style Pictochart, charte FitClem) — ex. `docs/contacts/fitclem/infographie-fitclem-kpi.html` ou `infographie-fitclem-swot.html` — à intégrer ou lier depuis la landing (section “En un coup d’œil” ou onglet KPI).
- [ ] **Règle** : pas d’invention de chiffres ; données = stratégie + rapport SEO (manque à gagner, problèmes clés). Réf. `.cursor/rules/infographiste-dataviz.mdc`, `brief-infographiccraft.md`.

---

## 4. Critères de succès

- [ ] **Contenu** : plus de squelette ; chaque section (intro, enjeux, solution, services, SEO, mission, about) est **remplie** avec le fond de la stratégie (PESTEL, SWOT, Porter, concurrentiel, growth, KPI, plan 30/60 j).
- [ ] **Design** : charte FitClem appliquée (couleurs, typo, CTA) ; hiérarchie et lisibilité améliorées.
- [ ] **Illustration** : au moins un support infographique (KPI ou SWOT/PESTEL) livré et référencé ; emplacements “preuve” / chiffres clés identifiés.
- [ ] **Chef de Projet** : validation finale avant clôture ; pas de contenu inventé (anti-hallucination).

---

## 5. Fichiers et références

| Ressource | Emplacement |
|-----------|-------------|
| Contenu landing (cible) | `docs/contacts/fitclem/landing-proposition-fitclem.json` |
| Stratégie (synthèse) | `docs/contacts/fitclem/strategie-marketing-fitclem.md` |
| Stratégie (complet) | `docs/contacts/fitclem/strategie-marketing-fitclem-complet.md` |
| Charte graphique | `docs/contacts/fitclem/charte-graphique-fitclem.md` |
| Template landing | `templates/landing_pages/proposition.html` |
| Règles éditorial / design | `docs/bonnes-pratiques.md`, `theming-landing-prospect.md` |
| Infographiste | `brief-infographiccraft.md`, `registre-agents-ressources.md` § Infographiste |

---

## 6. Ordre de travail suggéré

1. **Chef de Projet** : valider périmètre (sections à remplir, priorité infographie : KPI vs SWOT vs PESTEL).
2. **Rédacteur** : remplir tout le contenu (JSON ou fichier markdown) à partir des 3 sources stratégie.
3. **Designer** : appliquer charte FitClem + hiérarchie + emplacements illustrés ; **Infographiste** : produire 1 infographie (KPI ou SWOT).
4. **Dev Django** (si besoin) : intégrer champs supplémentaires ou lien vers infographie dans le template.
5. **Chef de Projet** : validation finale ; clôture sprint (logs, commit, push).

---

*Sprint créé pour remplir, illustrer et animer le contenu FitClem sous supervision Chef de Projet. Dernière mise à jour : 2026-02-15.*
