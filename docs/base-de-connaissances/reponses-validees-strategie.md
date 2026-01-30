# Réponses validées — stratégie LPPP

**Rôle** : Synthèse des réponses validées par l'utilisateur pour déployer la stratégie.  
**Pilote** : Conseiller, Chef de Projet.  
**Référence** : `fonction-premiere-et-segments-prospection.md`, segmentations `2025-01-30-relance-evenements.md`, `2025-01-30-interface-landingsgenerator.md`.

---

## 1. Relance événements (premier livrable)

- **Validation** : Oui, on part maintenant sur la mise en œuvre « Relance événements » (premier livrable = positionnement direct).
- **Priorité du livrable** : Template de landing « relance après événement » + structure `content_json`.
- **Contexte à garder en tête** : Reprise de contact avec des gens avec qui **le feeling est bien passé au salon**. Objectif : une landing **aussi agréable visuellement** qu'une landing commerciale, avec **hero section** et **call-to-action ciblés**. Pas du stock : du cas par cas, orienté « je me replace en produit commercial » à la fin.

---

## 2. Interface essais (Django, mobile-first, dark)

- **Nom de l'app** : **landingsgenerator**.
- **URL** : **/essais/** (racine de l'interface).
- **Premier écran (relance salon)** : Présentation où tu te places comme **produit commercial** à la fin. Cibler à partir de **leur activité**, de ce que tu supposes être **leurs besoins** et **pain points**, et te présenter comme **freelance** ou **alternant** (selon le matching) sérieux à envisager.
- **Thème** : Switch **clair / sombre** (oui). L'agent **Designer** doit **vérifier individuellement** chaque page : tous les fonds en noir pour le mode nuit, passage correct en mode jour. Se méfier des contenus qui supportent mal le switch (comme sur SquidResearch) — tester et corriger au cas par cas.

---

## 3. Données SEO / KPI par prospect

- **Format** : Tu déposeras des **fichiers CSV** (Screaming Frog).
- **Stockage** : **On ne les stocke pas** en base pour l'instant. On produit un **rapport** : bien présenté, clair, lisible, **sexy** à regarder pour que des gens peu techniques aient envie de regarder.
- **Contenu du rapport** : Pas trop enrober. **Prospection sur le manque à gagner** et **estimations de ce que ça leur coûte d'avoir un SEO pourri**.

---

## 4. Priorité globale

- **Priorité #1** : **C = les deux en parallèle** — Relance événements (landing + positionnement direct) **et** Interface essais (landingsgenerator, /essais/, mobile-first, dark + switch).

---

## 5. Segmentations créées

- **Relance événements** : `docs/base-de-connaissances/segmentations/2025-01-30-relance-evenements.md`.
- **Interface landingsgenerator** : `docs/base-de-connaissances/segmentations/2025-01-30-interface-landingsgenerator.md`.

---

*Document rédigé par le Conseiller. Dernière mise à jour : 2025-01-30. Référence : réponses utilisateur validées (relance événements, landingsgenerator, SEO rapport, priorité C).*
