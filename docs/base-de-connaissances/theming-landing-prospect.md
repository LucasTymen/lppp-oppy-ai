# Thématisation des landing pages : style de la société contactée

**Rôle** : Stratégie design pour les landing pages LPPP — thème prospect + fallback.  
**Pilote design** : Designer UI/UX & Front-End (voir `agents-roles-responsabilites.md`).  
**Décision** : les landing pages créées reprennent le thème de la société contactée ; si le rendu est trop moche, utiliser la charte graphique SquidResearch (sur instruction utilisateur).

---

## 1. Objectif

- **Priorité** : les landing pages reflètent le **style de la société que l’on contacte** (prospect) : couleurs, polices, thème général pour rester cohérent avec leur identité et augmenter la pertinence perçue.
- **Fallback** : si le thème prospect est jugé trop moche ou inutilisable, utiliser la **charte graphique SquidResearch** (qualité « bogoss »). L’utilisateur indiquera quand basculer sur ce fallback.
- **Idéal** : reprendre leur **style CSS, polices et couleurs** (et thème d’une façon générale) pour appliquer à nos templates de landing.

---

## 2. Responsable et coordination

- **Designer UI/UX & Front-End** : en charge de la mise en œuvre (templates, design system, variables CSS, intégration des couleurs/polices prospect).
- **Chef de Projet** : valide la stratégie et les livrables ; peut fournir wireframes ou priorités.
- **Conseiller** : a documenté la stratégie ; coordination avec le Designer pour les choix techniques (extraction du thème prospect, structure des données, fallback).

Référence rôle Designer : `docs/base-de-connaissances/agents-roles-responsabilites.md` § Designer.  
Référence SquidResearch : `docs/base-de-connaissances/sources.md` (chemin dépôt, charte graphique pour fallback).

---

## 3. SquidResearch — charte graphique (fallback)

- **Quand** : sur instruction de l’utilisateur (« utilise la charte SquidResearch », « c’est trop moche passe en bogoss SquidResearch », etc.).
- **Où** : dépôt SquidResearch (hors workspace LPPP) :
  - **WSL/Linux** : `/home/lucas/tools/squidResearch`
  - **Windows (WSL)** : `\\wsl.localhost\Ubuntu-22.04\home\lucas\tools\squidResearch`
  - **Depuis $HOME** : `tools/squidResearch`
- **Quoi** : reprendre les **polices, couleurs et thème** (CSS, design system) de SquidResearch pour l’appliquer aux landing pages LPPP lorsque le thème prospect n’est pas utilisé.
- Le Designer s’appuie sur les fichiers CSS / design system du dépôt SquidResearch pour définir la charte « bogoss » à réutiliser dans les templates LPPP.

---

## 4. Chartes prospect documentées

### FITCLEM

- Pour les **landings et supports FITCLEM**, le Designer **doit s’appuyer sur la charte graphique canonique** : `docs/contacts/fitclem/charte-graphique-fitclem.md`.
- Cette charte définit palette (orange corail, pêche, blanc, noir), typographie (Montserrat/Poppins, Inter/Open Sans), variables CSS « Fitclem Style », boutons, sections douces, border-radius élevés et ombres légères. **Coller à cette charte** pour toute production design FITCLEM.

### Oppy.ai (LPPP-OppyAI)

- Pour les **landings et supports LPPP-OppyAI**, le Designer **doit s'appuyer sur la charte** : `docs/contacts/lppp-oppy-ai/charte-graphique-oppy-ai.md` — style « Tech CIM » (fond sombre, accent cyan/turquoise, polices Montserrat/Inter).

---

## 5. Thème prospect — approche cible (général)

- **Idéal** : réutiliser le **style CSS, polices et couleurs** (et thème général) du site de la société contactée.
- **Données possibles** : URL du site prospect, couleurs extraites (manuel ou outil), polices identifiées, éventuellement extraits de données enrichies (si champ dédié existe côté enrichissement).
- **Implémentation** : à préciser avec le Designer (variables CSS par landing, champs `content_json` ou modèle pour couleurs/polices, sélection template + thème). Le système de templates multiples (`docs/base-de-connaissances/segmentations/2025-01-30-systeme-templates-multiples.md`) peut être étendu pour injecter le thème prospect dans chaque template (modern, minimal, corporate).
- **Fallback** : si thème prospect absent ou jugé trop moche → appliquer la charte SquidResearch (voir § 3).

---

## 6. Lien avec le système de templates multiples

- La segmentation **« Système de templates multiples »** (`docs/base-de-connaissances/segmentations/2025-01-30-systeme-templates-multiples.md`) définit les templates de base (modern, minimal, corporate).
- La **thématisation prospect** (ce document) s’applique **en plus** : chaque template peut recevoir les couleurs, polices et thème soit du prospect, soit de la charte SquidResearch (fallback).
- Le Designer intègre cette règle dans les maquettes et le code : structure permettant d’injecter un jeu de variables (couleurs, polices) selon la source (prospect vs SquidResearch).

---

## 7. Switch clair/sombre (interface landingsgenerator)

- L'interface **landingsgenerator** (/essais/) a un **switch clair/sombre**. Le **Designer** doit **vérifier individuellement** chaque page : tous les **fonds en noir** pour le mode nuit, **passage correct** en mode jour.
- **Se méfier** des contenus qui supportent mal le switch (comme sur SquidResearch) — tester et corriger au cas par cas. Référence : `reponses-validees-strategie.md`, segmentation `2025-01-30-interface-landingsgenerator.md`.

---

## 8. Prochaines étapes (Designer / Chef de Projet)

- [ ] Designer : prendre connaissance de ce document, de la segmentation « templates multiples » et de la segmentation « interface landingsgenerator » (switch clair/sombre, vérification page par page).
- [ ] Designer : identifier dans SquidResearch les fichiers de la charte graphique (CSS, polices, couleurs) pour le fallback.
- [ ] Designer + Chef de Projet : définir comment stocker et injecter le thème prospect (champs modèle, `content_json`, ou service dédié) et comment déclencher le fallback SquidResearch (choix manuel en admin, règle métier, etc.).
- [ ] Intégrer la thématisation dans les specs des templates (modern, minimal, corporate) et dans les livrables.

---

*Document rédigé par le Conseiller. Dernière mise à jour : 2026-02-15 (ajout § 4 charte FITCLEM). Référence : décision utilisateur (thème prospect + fallback charte SquidResearch) ; coordination Designer.*
