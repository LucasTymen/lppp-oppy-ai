# Fonction première du projet LPPP et segments de prospection

**Rôle** : Vision produit, segments et pistes pour les landing pages et la prospection.  
**Pilote** : Chef de Projet, Conseiller ; consommation par Designer, Rédacteur, Growth, tous les agents.  
**Décision** : discuter de la faisabilité avant de développer pour avoir quelque chose de vraiment exploitable qui fonctionne bien.

---

## 1. Fonction première du projet

Le projet LPPP a pour **fonction première** de créer des **landing pages adaptées** à la fois à :

1. **Tes besoins de positionnement** : te placer, te présenter, offrir des prestations et des compétences (skills) ciblées.
2. **Tes angles de prospection** : collecte de data, lead magnets, relances, campagnes par secteur ou type de cible.

Tu as exploré **plusieurs pistes et secteurs**. Certaines approches sont **similaires** (réutilisables), d’autres demandent peut‑être des **adaptations personnalisées au coup par coup**. Le Conseiller et le Chef de Projet trient, segmentent et organisent les informations pour que toute l’équipe (Designer, Rédacteur, Growth, Dev) s’appuie sur la même vision.

**Avant de commencer à coder** : on discute de la **faisabilité** pour avoir quelque chose de vraiment exploitable et qui fonctionne bien.

---

## 2. Segments et pistes identifiés

D’après les ressources transmises, les **segments / approches** à prendre en compte sont :

| Segment / piste | Description courte | Ressource / référence |
|-----------------|--------------------|------------------------|
| **Cabinets avocats — secteurs ART et Juridique** | Prospection ciblée cabinets avocats, secteurs art et juridique. | Dossier « 5_cabinets avocats_secteurs ART et Juridique » (ressources utilisateur). |
| **Boîtes sans tech** | Prospection de boîtes sans tech. | Dossier « prospection boites sans tech » (ressources utilisateur). |
| **Relance après événement** | Exemple de relance après événement + liste de prospects. | Dossier « 2_exemple de relance apres evennement (et liste des prospects) » (ressources utilisateur). **Priorité 1.** |
| **Boîtes low tech + leads** | Prospection low tech avec leads. | Dossier « 3_prospection de boites low tech_plus_leads » (ressources utilisateur). |
| **Concept low tech — idées** | Concept et idées pour la low tech. | Dossier « 4_concept pour la low tech_beaucoup d'idées » (ressources utilisateur). |

**Priorisation** : **1. Relance événements** en premier.

---

## 3. CV et adaptation du discours (agent RH / Rédacteur)

Tu mets à disposition **plusieurs CV** pour que **l’agent chargé des RH** (ou le **Rédacteur / Content Strategist**) puisse **adapter le discours et le dialogue** à chaque contexte (poste, secteur, type de prospect).

**CV référencés** (voir `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md`) :

- **CV full — Marketing & Growth, Acquisition B2B, SEO, Paid Media** (2026-01-27).
- **LM Teeptrak** (lead magnet / positionnement Teeptrak).
- **CV Assistant Webmarketing — SEO, SEA, Data** (2026-01-28).
- **CV Growth Engineer — Acquisition, Automation & Data (Alternance TEEPTRAK)** (2026-01-27).

**Usage** : le **Rédacteur** (voir `agents-roles-responsabilites.md` § Rédacteur) — ou un futur agent RH dédié — s’appuie sur ces CV pour adapter les contenus des landing pages, les relances et les messages (ton, compétences mises en avant, angles par secteur). Les CV sont enregistrés dans les ressources utilisateur ; à copier dans `docs/ressources-utilisateur/etudes/` ou `autres/` si tu veux les versionner dans le dépôt.

---

## 4. Organisation des informations pour l’équipe

- **Registre des ressources** : `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md` — toutes les ressources (CV, dossiers secteurs, études) y sont listées avec type, titre, usage.
- **Ce document** : fonction première + segments + lien vers CV/RH.
- **Réponses validées** : `docs/base-de-connaissances/reponses-validees-strategie.md` (relance événements, landingsgenerator, SEO rapport, priorité C).
- **Segmentations** : `docs/base-de-connaissances/segmentations/2025-01-30-relance-evenements.md`, `2025-01-30-interface-landingsgenerator.md`.
- **Rapport SEO prospect** : `docs/base-de-connaissances/rapport-seo-prospect.md` (rapport pas stockage, CSV Screaming Frog, manque à gagner, coût SEO pourri).
- **TODO** : `docs/TODO.md`.

Le **Conseiller** et le **Chef de Projet** mettent à jour ce document et le registre quand de nouveaux segments ou ressources arrivent.

---

## 5. Orientations faisabilité (décisions utilisateur)

Les points suivants ont été actés avec toi :

- **Priorisation** : **1. Relance événements** en premier.
- **Structure JSON vs contenu** : Les structures de JSON (ex. `content_json`) peuvent être à peu près les mêmes (mêmes champs, même schéma). En pratique : **contenu cas par cas systématique** pour chaque prospect — sinon ça sonne faux. Schéma réutilisable, contenus rédigés/saisis pour chaque prospect.
- **Données par prospect (SEO, KPI)** : Chaque prospect doit avoir un rapport SEO et une étude des KPI. Tu fournis les éléments au fur et à mesure. Pas d'automatisation complète pour l'instant sauf si une solution est identifiée (APIs SEO, exports analytics, Lighthouse, etc.) ; on pourra intégrer des briques progressivement.
- **Délais et phasage** : Contrainte temps. **Phase 1** : **positionnement direct** uniquement (une version par prospect). **Phase 2 (ultérieure)** : altérations pour **A/B testing**.

---

## 6. Prochaines étapes (faisabilité)

- [x] **Discuter faisabilité** avec toi (§ 5). “positionnement” vs “lead magnet” vs “relance événement”).
- [x] **Trier similaire vs personnalisé** (acté : même schéma JSON, contenu cas par cas) : quelles approches partagent le même template / discours, lesquelles nécessitent une config ou un contenu spécifique.
- [ ] **Relance événements (priorité 1)** : mise en œuvre — premier livrable positionnement direct.
- [ ] **Rédacteur** : s'appuyer sur CV et dossiers secteurs pour le discours cas par cas (ce doc + REGISTRE-RESSOURCES).
- [ ] Réception des éléments SEO / KPI au fur et à mesure ; intégration (manuel puis semi-auto/auto si solution trouvée).

---

*Document rédigé par le Conseiller. Dernière mise à jour : 2025-01-30. Référence : décision utilisateur (fonction première, segments, CV pour RH/rédacteur, orientations faisabilité : relance événements priorité 1, JSON même structure / contenu cas par cas, données SEO/KPI au fur et à mesure, positionnement direct puis A/B plus tard).*
