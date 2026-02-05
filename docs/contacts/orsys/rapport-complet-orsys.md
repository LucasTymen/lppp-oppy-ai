# Rapport ORSYS — Contexte 2026 & angle contrat

**À l’attention de** : Aboubakar Timite — ORSYS (Formation IT).  
**Auteur** : Lucas Tymen, Growth Engineer.  
**Date** : Février 2026.

Ce rapport ne propose pas du marketing : une **analyse basée sur la réalité économique de février 2026**. Le marché de la formation est en pleine consolidation (« la grande purge ») ; les entreprises ne financent plus que ce qui est **Business Critical**. J’y pose le cadre (PESTEL, Porter, SWOT, concurrence) et l’**argumentaire contrat** : une machine à **signaux faibles** pour cibler les budgets restructuration et conformité IA Act — là où vos concurrents attendent que le téléphone sonne.

---

## Résumé — Ce qu’il faut retenir

| Élément | Réalité terrain |
|--------|------------------|
| **Marché** | Consolidation (« grande purge »). CPF bridé, subventions OPCO en baisse. Les entreprises ne financent que ce qui est Business Critical. |
| **Angle ORSYS** | Basculement B2C CPF → **B2B Pur** (Plans de développement des compétences). Réduction des coûts d’acquisition vitale. |
| **Opportunité** | **IA Act européen** : former DPO et RSSI à la conformité légale de l’IA. Restructurations et FNE-Formation = budgets captables. |
| **Positionnement** | Données terrain, signaux faibles, automatisation pour **prévoir** qui va licencier ou pivoter et proposer des plans Reclassement. Pas « faire du marketing ». |

👉 **Détail** : [Diagnostic SEO](#diagnostic-seo), [PESTEL, Porter, SWOT, concurrence, script](#analyse-seo-complete) ci-dessous.

---

<h2 id="analyse-seo-complete">Analyse complète</h2>

Analyse basée sur la réalité économique de février 2026. **Diagnostic SEO** : données d’un crawl du site orsys.fr (février 2026).

---

<h3 id="diagnostic-seo">0. Diagnostic SEO — Données terrain (crawl février 2026)</h3>

| Indicateur | Valeur | Commentaire |
|------------|--------|-------------|
| **URLs crawlées** | 485 | Périmètre analysé. |
| **Indexables** | 288 (59,4 %) | Pages considérées comme indexables. |
| **Non indexables** | 197 (40,6 %) | Dont **189** dans le segment `formations/` (pages canonisées vers les fiches .html). |
| **Erreurs 4xx** | 3 | Ressources images (.avif) en 404. |
| **Contenu doublon exact** | 2 | `orsys-lemag` et `orsys-lemag/` (même contenu, risque de dilution). |
| **H1 manquant** | 2 | Pages orsys-lemag (sans slash et avec slash). |
| **Canoniques manquantes** | 208 | Pas de balise canonique → risque d’imprévisibilité d’indexation. |
| **Pages canonisées** | 189 | URL pointe vers une autre (ex. `/formations/python` → `formations-developpement-logiciel.html`). |
| **Version canonique non indexable** | 5 | La cible de la canonique est elle-même non indexable. |
| **Hreflang : liens de retour manquants** | 1 | orsys-lemag (FR/EN/NL/ES) — réciprocité à corriger. |

**Temps de réponse (en secondes)** :

| Tranche | Nombre d’URLs | % |
|---------|----------------|---|
| 0 – 1 s | 97 | 20,0 % |
| 1 – 2 s | 331 | 68,3 % |
| 2 – 3 s | 52 | 10,7 % |
| 3 – 5 s | 3 | 0,6 % |
| 10+ s | 2 | 0,4 % |

**Problèmes prioritaires (aperçu)** : 126 pages avec H1 multiple ; 9 titres de page dupliqués ; 13 méta-descriptions dupliquées ; 84 titres > 60 caractères (troncature SERP) ; 475 URLs sans en-tête HSTS / X-Content-Type-Options / Referrer-Policy (sécurité et signal).

---

### 1. PESTEL : La « Grande Purge » de la formation

| Facteur | Analyse de situation (Réalité 2026) | Impact pour ORSYS |
|---------|-------------------------------------|-------------------|
| **Politique** | Fin du « Quoi qu’il en coûte » : le gouvernement a durci le reste à charge CPF (100 € minimum) et réduit les subventions aux OPCO de 15 % en 2025. | ORSYS doit basculer du « B2C via CPF » vers le **B2B Pur** (Plan de développement des compétences). |
| **Économique** | Récession RH : les licenciements dans la tech (Mass Layoffs) réduisent le nombre de stagiaires. Les budgets formation sont les premiers coupés dans les PME/ETI. | Besoin vital d’outils d’automatisation pour réduire les coûts d’acquisition client. |
| **Social** | Défiance vs Apprentissage : l’accès aux contrats pro est devenu un parcours du combattant. Les étudiants galèrent à trouver des alternances. | ORSYS doit prouver un « taux d’employabilité » réel, pas juste délivrer des certificats. |
| **Technologique** | Obsolescence éclair : une formation « Prompt Engineering » de 2024 est déjà périmée. L’IA générative automatise 40 % des tâches des dévs juniors. | Nécessité de vendre de la **Formation de pointe** (IA Ops, LLM Fine-tuning) plutôt que du « Bureautique / Python base ». |
| **Environnemental** | Bilan Carbone : les entreprises privilégient le distanciel pour le score RSE. | Digitalisation forcée du catalogue. |
| **Légal** | L’AI Act européen : nouvelles obligations de conformité pour les entreprises utilisant l’IA. | **ÉNORME OPPORTUNITÉ** : former les DPO et RSSI à la conformité légale de l’IA. |

---

### 2. PORTER : Le rapport de force s’inverse

1. **Menace des substituts (MAXIMALE)** — Les entreprises créent leurs propres « Académies internes » via des LLM nourris de leur propre documentation. Pourquoi payer ORSYS ?
2. **Pouvoir des clients (ÉLEVÉ)** — Les acheteurs formation (DRH) exigent des remises de 20–30 % car ils savent que l’offre est saturée.
3. **Concurrence sectorielle (CONSOLIDATION)** — Les petits meurent. Seuls les « Gros » (Cegos, Orsys, Global Knowledge) restent, mais se battent à mort sur les prix.
4. **Nouveaux entrants** — Des experts indépendants sur LinkedIn vendent des « Bootcamps » intensifs plus agiles qu’une grosse structure.

---

### 3. SWOT Stratégique (angle de tir)

| | |
|---|---|
| **FORCES** | Catalogue certifiant (répond aux critères légaux que l’IA ne peut pas fournir seule). |
| **FAIBLESSES** | Structure de coûts lourde. Inertie à mettre à jour les programmes face à l’IA. |
| **OPPORTUNITÉS** | Utiliser un profil **Growth** pour **prévoir** quels secteurs vont licencier ou pivoter et proposer des plans de « Reclassement » (financés par l’État / Région via FNE-Formation, etc.). |
| **MENACES** | La gratuité des connaissances. L’IA qui devient un « formateur » personnel intégré aux outils (Microsoft Copilot). |

---

### 4. Analyse concurrentielle : où se placer ?

| Concurrent | Stratégie actuelle | Faille à exploiter |
|------------|-------------------|--------------------|
| **Cegos** | Management / Soft Skills. | Moins crédibles sur l’automatisation technique pure. |
| **Global Knowledge** | Certifications Cloud / Infra. | Très rigides, liés aux calendriers des éditeurs. |
| **OpenClassrooms** | 100 % Online / Mentorat. | Souvent perçu comme « trop scolaire » pour des experts seniors. |

---

### 5. Argumentaire « Contrat » — Le script

À utiliser en entretien ou en relance. Ne pas vendre « du marketing » ; vendre de la **donnée terrain** et une machine à signaux faibles.

> **« Aboubakar, je sais que le marché de la formation est tendu, que le CPF est bridé et que les entreprises gèlent leurs recrutements. C’est précisément pour ça que je suis là.**
>
> **Mon script ne cherche pas “qui recrute”, il cherche “qui lève des fonds” ou “qui change de stack technique”.**
>
> **On va utiliser l’automatisation pour aller chercher les budgets de restructuration et de conformité IA Act. Je vous apporte une machine de guerre pour détecter les signaux faibles là où vos concurrents attendent que le téléphone sonne. »**

---

### 6. Suite possible

- Formaliser les **3 types de signaux faibles** que le script peut détecter pour ORSYS (à intégrer dans la landing ou un one-pager).
- Affiner la mise en forme (callouts, synthèses) selon vos retours.

---

Si ce cadre vous parle, échangeons — sans engagement.

**Lucas Tymen** — [lucas.tymen@gmail.com](mailto:lucas.tymen@gmail.com) — [LinkedIn](https://www.linkedin.com/in/lucas-tymen-310255123/)

*Rapport basé sur la réalité économique de février 2026. Dernière mise à jour : 2026-02.*
