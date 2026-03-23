# Sprint : Enrichissement page d'accueil Infopro — illustrations et explications

**Date** : 2026-02-21  
**Statut** : 🟢 En cours (étape 1–3 livrées)  
**Pilote** : Chef de Projet  

---

## Contexte

La page d'accueil lppp-infopro est jugée **trop vide** et manque d'**illustrations** et d'**explications**. Il faut l'enrichir en utilisant **graphiques et infographies** pour illustrer les sections : Chiffres clés, Enjeux, Solution, Services.

**Anti-crash** : appliquer les mesures systématiques — commit après chaque bloc logique, mise à jour logs, fichier `.progress-enrichissement-accueil-infopro.md`.

---

## RACI

| Rôle | Responsabilité |
|------|----------------|
| **Rédacteur en chef** | Textes, légendes, formulations (bonnes pratiques éditoriales) |
| **Expert Marketing** | Angle commercial, enjeux business, manque à gagner, CTA |
| **Infographiste** | Visuels (TTFB, funnel, flowchart, recovery rings), intégration infographie 7 formats |
| **Expert Math** | Chiffres, formules, graphiques (bar chart, timeline), cohérence data |

---

## Livrables par section

### 1. Chiffres clés
- [ ] **Expert Math** : vérifier cohérence des chiffres (TTFB 0,15 s, 68/100, 97 %, 337/358)
- [ ] **Infographiste** : mini-graphiques ou icônes pour chaque KPI (speedo, barres)
- [ ] **Rédacteur** : légendes courtes et explicatives sous chaque chiffre

### 2. Enjeux (Vos enjeux)
- [ ] **Template** : ajouter bloc `enjeux-visuals` pour Infopro (comme Promovacances) : TTFB comparison, funnel impact, flowchart priorité
- [ ] **Expert Marketing** : formuler « Ce que ça coûte » et « Ce qu'on débloque » en langage business
- [ ] **Rédacteur** : réécrire pain_points avec explications claires (pourquoi 68 bloque, impact images)

### 3. Section Infographies audit (actuellement absente pour Infopro)
- [ ] **Template** : ajouter condition `landing_page.slug == 'infopro'` pour afficher iframe dashboard + lien infographie 7 formats
- [ ] **Infographiste** : s'assurer que infographie-infopro-7-formats.html et audit-dashboard.json sont bien intégrés

### 4. Solution
- [ ] **Rédacteur** : enrichir solution_workflow et solution_piliers avec explications étape par étape
- [ ] **Infographiste** : schéma plan d'action 3 étapes (Images → Meta → Technique) si pas déjà présent

### 5. Services (Ce que j'offre)
- [ ] **Expert Marketing** : renforcer angle valeur (qu'est-ce que ça apporte concrètement ?)
- [ ] **Rédacteur** : éviter répétitions, clarifier différences entre Dashboard, Diagnostic, Plan d'action

---

## Données Infopro (audit-dashboard.json)

- TTFB : ~0,15 s (serveur OK)
- PageSpeed Mobile perf : 68/100
- URLs &lt; 1 s : 97,2 %
- Indexabilité : 337/358
- Priorités : images (45 %), meta (35 %), technique (20 %)
- Manque à gagner : 132–324 k€/an (fourchette)

---

## Fichiers impactés

| Fichier | Modification |
|---------|--------------|
| `templates/landing_pages/proposition.html` | Ajouter `elif slug == 'infopro'` pour enjeux-visuals + section infographies-audit |
| `docs/contacts/infopro/landing-proposition-infopro.json` | Enrichir pain_points, solution_workflow, services_segments |
| `docs/contacts/infopro/` | Fichiers infographie existants (infographie-infopro-7-formats.html, audit-dashboard.json) |

---

## Anti-crash

- Commit après chaque modification (1–3 fichiers)
- Mise à jour `docs/logs/log-projet.md`
- Fichier `.progress-enrichissement-accueil-infopro.md` (supprimer à la fin)
- Reprise au dernier marqueur en cas d'interruption
