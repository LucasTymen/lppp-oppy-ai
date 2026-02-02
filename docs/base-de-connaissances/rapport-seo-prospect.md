# Rapport SEO prospect — présentation et contenu

**Rôle** : Stratégie pour les rapports SEO/KPI par prospect (données Screaming Frog).  
**Pilote** : Chef de Projet, Rédacteur / Data Analyst selon livrable.  
**Décision** : on ne stocke pas les données en base ; on produit un **rapport** bien présenté, clair, lisible, sexy pour que des gens peu techniques aient envie de regarder.

---

## 1. Source des données

- **Format** : Fichiers **CSV** (Screaming Frog) déposés par l'utilisateur au fur et à mesure.
- **Usage** : alimenter la production du **rapport** (pas de stockage permanent des CSV en base LPPP pour l'instant, sauf si besoin ultérieur).

---

## 2. Livrable : rapport (pas stockage)

- **On ne stocke pas** les données SEO/KPI en base pour l'instant.
- **On produit un rapport** :
  - **Bien présenté** : clair, lisible, **sexy** à regarder.
  - **Objectif** : que des gens **peu techniques** prennent intérêt à regarder.
  - **Contenu** : pas trop enrober. **Prospection sur le manque à gagner** et **estimations de ce que ça leur coûte d'avoir un SEO pourri**.

---

## 2b. Structure minimale du rapport (à intégrer partout)

Chaque rapport SEO doit contenir **au minimum** :

| Élément | Obligatoire | Description |
|--------|-------------|-------------|
| **Nombre de problèmes** | Oui | Indiquer clairement **combien** de problèmes ont été trouvés (ex. « 12 problèmes identifiés »). |
| **Impact** | Oui | Pour chaque type de problème (ou en synthèse), expliquer **ce qu’ils sous-tendent comme impact** (visibilité, conversion, coût, risque technique, etc.). |
| **Échantillon de 5 prospects** | Si trouvés | Si des **prospects** ont été identifiés (cibles, leads, entreprises pertinentes), en présenter un **échantillon de 5** dans le rapport (nom / entreprise / pertinence ou critère). |

À appliquer à **tous les rapports SEO** et à toute livraison de type « rapport prospect ».

**Rapport complet (fiche + stratégie + SEO)** : pour uniformiser le livrable par entreprise démarchée, utiliser le **template** `template-rapport-complet-prospect.md`. On copie le template dans le dossier contact (`docs/contacts/<slug>/rapport-complet-<slug>.md`), on remplit les sections (société, PESTEL/SWOT/Porter, SEO dont § 3.0 obligatoire). Voir `organisation-donnees-contacts.md` (contenu type d’un dossier contact).

---

## 3. Croisement avec wording + copywriting (Expert SEO)

- Le **rapport SEO** (données Screaming Frog, KPIs, visibilité) est **croisé** avec une **étude wording (wordpricing) + copywriting** pour produire un rapport unifié (pistes SEO + wording + copywriting). Voir `docs/base-de-connaissances/expert-seo-demarche-rapport-wording-copywriting.md`.
- **Pilote** : Expert SEO / AI-GEO. Données fournies par l’utilisateur (rapport SEO, CSV, stats) dans `docs/ressources-utilisateur/` ou via le Conseiller.
- **À discuter** : niveau d’information à transmettre dans le rapport lead magnet (public) et **chiffrage** pour protéger les idées — doc démarche § 4.

---

## 4. Prochaines étapes (à préciser avec Chef de Projet)

- [ ] Définir le format du rapport (PDF généré, page HTML dédiée, intégration dans l'interface landingsgenerator, autre).
- [ ] Définir le flux : dépôt CSV → traitement (script, commande Django, autre) → génération rapport. **Outils** : pandas pour lecture/agrégation CSV (voir `bibliotheques-agents-techniques.md`).
- [ ] Rédacteur / Data Analyst : structure du contenu (manque à gagner, coût SEO pourri) et charte visuelle du rapport.
- [ ] Discussion : niveau d’info à transmettre + chiffrage (protection des idées).

---

*Document rédigé par le Conseiller. Dernière mise à jour : 2025-01-30. Ajout § 3 croisement wording + copywriting (Expert SEO), § 4 à discuter (niveau info + chiffrage). Référence : réponses utilisateur (CSV Screaming Frog, rapport pas stockage, manque à gagner, coût SEO pourri).*
