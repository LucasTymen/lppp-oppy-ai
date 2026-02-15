# Registre des ressources utilisateur LPPP

**Rôle** : index central pour retrouver rapidement toutes les données et ressources que tu transmets au Conseiller (textes, images, ébauches, textes d’études, etc.).  
**Maintenu par** : Conseiller (à chaque enregistrement d’une nouvelle ressource).  
**Consommé par** : toi, le Conseiller, et tous les agents qui ont besoin de s’appuyer sur tes données.

---

## Comment retrouver une ressource

- **Par type** : textes → `textes/` ; images → `images/` ; ébauches → `ebauches/` ; études → `etudes/` ; autre → `autres/`.
- **Par le registre** : tableau ci‑dessous (date, type, titre, fichier, usage/contexte).

---

## Tableau des ressources

| Date       | Type    | Titre / description courte | Fichier | Usage / contexte |
|------------|---------|-----------------------------|---------|------------------|
| 2025-01-30 | autres | CV full — Marketing & Growth, Acquisition B2B, SEO, Paid Media (Lucas Tymen) | Réf. Downloads : CV-full_MarketingEtGrowth…_2026-01-27_Lucas_Tymen.pdf | Agent RH / Rédacteur : adapter discours (Marketing & Growth, B2B, SEO, Paid Media). Voir fonction-premiere-et-segments-prospection.md. |
| 2025-01-30 | autres | LM Teeptrak (Lucas Tymen) | Réf. Downloads : LM TEEPTRAK_Lucas Tymen.pdf | Lead magnet / positionnement Teeptrak. Rédacteur : angles et discours. |
| 2025-01-30 | autres | CV Assistant Webmarketing — SEO, SEA, Data (Lucas Tymen) | Réf. Downloads : CV_Assistant Webmarketing…_2026-01-28_Lucas_Tymen.pdf | Agent RH / Rédacteur : adapter discours (Assistant Webmarketing, SEO, SEA, Data). |
| 2025-01-30 | autres | CV Growth Engineer — Acquisition, Automation & Data, Alternance TEEPTRAK | Réf. Downloads : CV_Growth Engineer…_2026-01-27_Lucas_Tymen.pdf | Agent RH / Rédacteur : adapter discours (Growth Engineer, alternance Teeptrak). |
| 2025-01-30 | etudes | 5 — Cabinets avocats, secteurs ART et Juridique | Réf. Downloads : 5_cabinets avocats_secteurs ART et Juridique | Segment prospection : cabinets avocats, art, juridique. Voir fonction-premiere-et-segments-prospection.md. |
| 2025-01-30 | etudes | Prospection boîtes sans tech | Réf. Downloads : prospection boites sans tech | Segment prospection : boîtes sans tech. |
| 2025-01-30 | etudes | 2 — Relance après événement + liste prospects | Réf. Downloads : 2_exemple de relance apres evennement… | Segment prospection : relance post-événement. |
| 2025-01-30 | etudes | 3 — Prospection boîtes low tech + leads | Réf. Downloads : 3_prospection de boites low tech_plus_leads | Segment prospection : low tech + leads. |
| 2025-01-30 | etudes | 4 — Concept low tech, idées | Réf. Downloads : 4_concept pour la low tech_beaucoup d'idées | Segment prospection : concept et idées low tech. |
| 2026-01-30 | textes | Prospection commando — sociétés low-tech / sous-digitalisées (Créteil + 15 km) | `textes/2026-01-30_prospection-commando-lowtech.json` | Base de ciblage : meta (stratégie, zone_focus, exclusions), opportuniteEmbauche (MISSION_THEN_CDI, alternance Rocket School), entreprises_ciblees (nom, ville, segment, mode_ciblage_principal, besoin, priorite), plan_action_proof_of_value. Exploitable en script Python/Node (filtrer par priorité/segment) ; voir `textes/README-prospection-lowtech.md`. |
| 2026-01-30 | etudes | Yuwell — portfolio / étude graphique (structure + palettes) | `etudes/yuwell-portfolio-etude-graphique.md` + PDF source `portfolio Yuwell_1.pdf` (Downloads) | Landing portfolio design graphique : système couleur par gamme produit ; structure, objectifs, palettes HEX/RGB/Pantone ; URL `/yuwell/`. |

**Note** : les chemins « Réf. Downloads » pointent vers tes Downloads. Pour versionner dans le dépôt : copier les fichiers dans `etudes/` ou `autres/` avec un nom explicite, puis mettre à jour la colonne « Fichier ».

*À compléter par le Conseiller à chaque enregistrement d’une ressource transmise par l’utilisateur.*

---

## Structure des dossiers

- **textes/** : contenus, notes, documents rédigés.
- **images/** : visuels, captures, schémas, références.
- **ebauches/** : brouillons, wireframes texte, maquettes préliminaires.
- **etudes/** : textes d’études, recherches ou documents qui ont servi à élaborer un système ou un outil.
- **autres/** : tout autre format (PDF, etc.) ou ressource qui ne va pas dans les catégories ci‑dessus.

Fichiers nommés de façon explicite (ex. `YYYY-MM-DD_nom-court.ext` ou `nom-descriptif.ext`) pour faciliter la recherche.

---

*Document maintenu par le Conseiller. Référence : `.cursor/rules/conseiller.mdc`.*
