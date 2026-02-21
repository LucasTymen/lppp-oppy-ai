# Répartition optimale agents — Rapports SEO & marketing (candidatures)

**Date** : 2026-02-20  
**Pilote** : Orchestrateur + Chef de Projet  
**Statut** : 🟡 Référentiel (à activer par contact)  
**Source** : `boite-a-idees.md` (pistes candidatures), `verification-lettre-motivation-funbooker-landing.md`

---

## Objectif

Distribuer les tâches pour **compléter les rapports SEO et marketing** (Infopro, Funbooker, futures candidatures) de façon **efficace** et **réutilisable**, avec maximisation de l’automatisation.

**3 ajouts « très sérieux »** :
1. Tableau opportunités long-tail avec volume estimé  
2. Simulation trafic potentiel (3 scénarios)  
3. 1 cluster détaillé avec mapping Hn / maillage interne  

**Éléments manquants identifiés** :
- **Rapport SEO** : architecture sémantique micro (clusters, requête→page, cannibalisation, gap concurrentiel, impact netlinking)
- **Rapport marketing** : extraction data Ads (impressions, thèmes, segmentation Meta, distribution âge, budget/CPC estimé)

---

## Répartition par agent

| Agent | Tâches | Automatisable | Livrable |
|-------|--------|---------------|----------|
| **Expert SEO** | Cluster mapping, requête→page, cannibalisation, opportunités long-tail chiffrées, simulation trafic par cluster, impact netlinking, 1 cluster détaillé (Hn + maillage) | Partiel (script d’aide) | Section rapport SEO, tableau long-tail, 1 cluster détaillé |
| **Growth** | Extraction data Google Ads (centre transparence), extraction Meta Ad Library (ciblage, distribution âge) | Oui (scraping/API) | Tableaux Ads, bar chart âge |
| **Data Analyst** | Simulations chiffrées (3 scénarios trafic), formules manque à gagner, ordres de grandeur | Oui (template calculs) | Tableau scénarios, formules appliquées |
| **Automatizer** | Workflow extraction Ads (centre transparence, Meta), pipeline cluster analysis (données → Expert SEO) | Oui | Workflows n8n, scripts Python |
| **Dev Django** | Commande `cluster_analysis <slug>`, intégration stack SEO sémantique (spaCy/Gensim), module `apps.seo_semantic` | Oui | Commande, module |
| **Infographiste** | Tableaux long-tail, bar chart âge Meta, scénarios trafic (visuels) | Non (manuel par contact) | HTML/JSON pour positionnement-marketing |
| **Rédacteur** | Synthèse, formulation, labels visuels | Non | Textes rapport |
| **Chef de Projet** | Coordination, validation, priorisation par candidature | — | Segmentation activée |
| **Orchestrateur** | Mise à jour registre, rappels RACI | — | Registre à jour |

---

## Détail par bloc

### 1. Rapport SEO — Architecture sémantique micro

| Tâche | Responsable | Automatisation | Dépendances |
|-------|-------------|----------------|-------------|
| Cluster mapping (topic clusters) | Expert SEO | Script Python (spaCy/Gensim) via Dev Django | CSV crawl, URLs |
| Mapping requête → page existante | Expert SEO | Export Semrush/Ahrefs + script matching | Données KW (optionnel) |
| Cannibalisation potentielle | Expert SEO | Script détection similarité H1/title | Données crawl |
| Gap analysis concurrentielle | Expert SEO + Growth Analyst | Manuel, template | Étude concurrence |
| Opportunités long-tail chiffrées | Expert SEO + Data Analyst | Template Excel/Python | Volumes estimés |
| Simulation trafic par cluster | Data Analyst | Modèle 3 scénarios (bas/moyen/haut) | Données clusters |
| Impact netlinking | Expert SEO | Estimation (formule) | Pas d’outil auto |
| **1 cluster détaillé** (Hn + maillage) | Expert SEO + Infographiste | Structure template | 1 thème prioritaire |

**Pilote** : Expert SEO. **Support technique** : Dev Django (commandes, module).

---

### 2. Rapport marketing — Extraction data Ads

| Tâche | Responsable | Automatisation | Source |
|-------|-------------|----------------|--------|
| Google Ads : impressions, thèmes | Growth | Scraping centre transparence OU saisie manuelle | adstransparency.google.com |
| Meta : ciblage, distribution âge | Growth | Scraping Meta Ad Library OU saisie | Meta Ad Library |
| Bar chart répartition âge | Infographiste | Template HTML réutilisable | Données Growth |
| Budget/CPC estimé | Growth + Data Analyst | Formule ordre de grandeur | Données publiques |
| Tableau scénarios manque à gagner | Data Analyst | Template 3 lignes (30k, 60k, 100k visites) | Formule CA = V × CVR × AOV |

**Pilote** : Growth. **Support** : Automatizer (workflow n8n si extraction automatisée).

---

### 3. Ordre d’exécution recommandé

```
Phase 0 — Préparation (Chef de Projet)
├── Choisir le contact (ex. Infopro, Funbooker)
├── Vérifier données disponibles (crawl CSV, Ads transparency)
└── Activer cette segmentation pour le contact

Phase 1 — Données (parallèle)
├── Growth → Extraction Ads (Google + Meta)
├── Expert SEO → Réception crawl + préparation clusters
└── Data Analyst → Template scénarios (formules)

Phase 2 — SEO sémantique (séquentiel)
├── Expert SEO → Clusters, long-tail, 1 cluster détaillé
├── Dev Django → Commande cluster_analysis (si intégré)
└── Infographiste → Visuels clusters / long-tail

Phase 3 — Marketing (parallèle à Phase 2 si données dispo)
├── Growth → Livraison données Ads
├── Infographiste → Bar chart âge, tableaux
└── Rédacteur → Synthèse, légendes

Phase 4 — Intégration & validation
├── Chef de Projet → Intégration rapport + positionnement-marketing
├── Rédacteur → Relecture, cohérence
└── DevOps → Export, push, déploiement
```

---

## Automatisation cible

| Élément | Agent | Outil / Flux | Gain |
|---------|-------|--------------|------|
| Extraction Google Ads | Automatizer + Growth | Workflow n8n (centre transparence) ou script Python | ~30 min → 5 min |
| Extraction Meta Ads | Automatizer + Growth | Workflow n8n ou Puppeteer/Playwright | ~45 min → 10 min |
| Cluster analysis | Dev Django + Expert SEO | Commande `manage.py cluster_analysis infopro` | Répétable |
| Scénarios trafic | Data Analyst | Template Python/Excel (entrées : visites, CVR, AOV) | Réutilisable |
| Bar chart âge | Infographiste | Template HTML (data-* attributes) | Copier-coller données |

---

## Checklist par nouvelle candidature

- [ ] **Chef de Projet** : Activer segmentation, vérifier dossier contact
- [ ] **Growth** : Extraire données Ads (Google + Meta) ou documenter absence
- [ ] **Expert SEO** : 1 cluster détaillé + tableau long-tail (même partiel)
- [ ] **Data Analyst** : Tableau 3 scénarios manque à gagner
- [ ] **Infographiste** : Bar chart âge (si Meta dispo), visuels clusters
- [ ] **Rédacteur** : Synthèse, cohérence lettre ↔ landing
- [ ] **DevOps** : Export, push, vérification déploiement

---

## Références

- `docs/boite-a-idees.md` — Pistes candidatures (accompli vs sous-exploité)
- `docs/base-de-connaissances/verification-lettre-motivation-funbooker-landing.md`
- `docs/base-de-connaissances/seo-semantique-outils-open-source.md`
- `docs/base-de-connaissances/template-positionnement-marketing.md`
- `docs/base-de-connaissances/registre-agents-ressources.md`

---

*Document créé pour optimiser la répartition et l’efficacité par candidature. À activer par contact (Infopro, Funbooker, etc.).*
