# Rapport complet [NOM_SOCIÉTÉ] — Société, stratégie et SEO

**Contact** : [slug-contact] ([domaine-site.com])  
**Date** : [AAAA-MM-JJ]  
**Objectif** : Document de travail unique regroupant la fiche société, l’analyse concurrence / PESTEL / SWOT / Porter et le rapport SEO pour la prospection et la proposition de valeur (Growth Engineer, SEO, funnel).

---

## Public cible et angle rédactionnel

**Public** : décideur / homme d'affaires (DG, directeur, responsable).  
**Règle** : il veut savoir **ce qui s'applique à sa société** — diagnostic concret, opportunités, plan d'action, chiffres. **Pas de théorie** : privilégier le concret (problèmes identifiés sur son site, impact business, priorités, estimation d'impact). Chaque section doit répondre à « Qu'est-ce que ça change pour nous ? ».

---

## Guide de remplissage

| Étape | Où | Action |
|-------|-----|--------|
| 1 | En-tête | Remplacer `[NOM_SOCIÉTÉ]`, `[slug-contact]`, `[domaine-site.com]`, `[AAAA-MM-JJ]`. |
| 2 | Synthèse | 1 paragraphe : qui est l’entreprise, secteur, produit phare, ce que contient le rapport. |
| 3 | § 1 | Société (siège, contact, forme juridique, direction), Produits (nom, description, atouts), Concurrence (acteurs + différenciation). |
| 4 | § 2 | PESTEL : 1 ligne par facteur. SWOT : 3–5 points par case. Porter : intensité + commentaire par force. |
| 5 | § 3.0 | **Obligatoire** : nombre de problèmes SEO (crawl), impact, échantillon 5 prospects si disponible. |
| 6 | § 3.1–3.7 | Adapter au diagnostic réel (technique, sémantique, opportunités, estimation, priorisation, conclusion). |
| 7 | § 4 | Verdict : pertinence cible, angle d’approche pour le projet LPPP. |
| 8 | Références | Lien site, lien étude détaillée (`etude-concurrentielle-pestel-swot-porter.md` dans le dossier contact). |

**Usage** : copier ce fichier dans `docs/contacts/<slug_contact>/rapport-complet-[slug].md` (ex. `rapport-complet-p4s-archi.md`) et remplir les sections. L’étude détaillée concurrence peut rester dans un fichier séparé `etude-concurrentielle-pestel-swot-porter.md` au même endroit.

**Data-driven, pas de vanity** : s’appuyer sur des **données sourcées** (site cible, crawl Screaming Frog, exports CSV) ; **ne pas inventer** de chiffres (CA, part de marché, classements) ; **éviter les métriques de vanity** (ex. « meilleur du marché », « leader » sans source). Indiquer la source pour chaque donnée (ex. « D’après l’export X », « Source : site Y, page Z »). Les fourchettes d’estimation (trafic, leads) sont des ordres de grandeur à affiner avec GSC / crawl — pas des promesses.

---

## Synthèse

[Un paragraphe : nom de l’entreprise, secteur, âge / taille si pertinent, produit ou service phare, positionnement. Puis : ce que compile ce rapport (fiche société, stratégie, SEO) et à quoi il sert (prospection, landing, angle Growth Engineer).]

---

## 1. Société, produits et concurrence

*Détail complet dans* : [`etude-concurrentielle-pestel-swot-porter.md`](./etude-concurrentielle-pestel-swot-porter.md) *(à créer dans le dossier contact si besoin).*

### 1.1 La société

- **Siège** : [Adresse] — Contact : [email] | [téléphone]  
- **Forme** : [SAS, SA, etc.] ([RCS]). Capital [X % français / détenu par…]. [R&D / fabrication : localisation si pertinent.]  
- **Direction** : [Nom] ([rôle]), [Nom] ([rôle]), …

### 1.2 Produits et technologie

- **[Nom technologie ou offre]** : [Principe en 1–2 phrases]. [Résultat : bénéfice client.]  
- **Gamme / Produits phares** :  
  - **[Produit A]** : [description courte, spécificités].  
  - **[Produit B]** : [description courte].  
- **Atouts** : [liste courte : performance, différenciation, certification, etc.]

### 1.3 Concurrence (vue d’ensemble)

- **Institutionnels / grands acteurs** : [Noms + positionnement].  
- **Spécialistes (marché / pays)** : [Noms + positionnement].  
- **Internationaux** : [Noms] — [comment la cible se positionne face à eux].  
- **Différenciation [NOM_SOCIÉTÉ]** : [3–5 points clés : technique, message, souveraineté, etc.]

---

## 2. Analyse stratégique (PESTEL, SWOT, Porter)

### 2.1 PESTEL (macro-environnement)

| Facteur | Impact pour [NOM_SOCIÉTÉ] |
|--------|----------------------------|
| **Politique** | [1–2 phrases] |
| **Économique** | [1–2 phrases] |
| **Social** | [1–2 phrases] |
| **Technologique** | [1–2 phrases] |
| **Environnemental** | [1–2 phrases] |
| **Légal** | [1–2 phrases] |

### 2.2 Matrice SWOT

| **Forces (S)** | **Faiblesses (W)** |
|----------------|---------------------|
| [Point 1] | [Point 1] |
| [Point 2] | [Point 2] |
| [Point 3] | [Point 3] |
| … | … |

| **Opportunités (O)** | **Menaces (T)** |
|----------------------|------------------|
| [Point 1] | [Point 1] |
| [Point 2] | [Point 2] |
| … | … |

### 2.3 Les 5 Forces de Porter

| Force | Intensité | Commentaire |
|-------|-----------|-------------|
| **Menace des nouveaux entrants** | [Faible / Moyenne / Forte] | [1 phrase] |
| **Pouvoir des fournisseurs** | [Faible / Moyen / Fort] | [1 phrase] |
| **Pouvoir des clients** | [Faible / Moyen / Fort] | [1 phrase] |
| **Menace des produits de substitution** | [Faible / Moyenne / Forte] | [1 phrase] |
| **Rivalité entre concurrents** | [Faible / Moyenne / Forte] | [1 phrase] |

---

## 3. Rapport SEO — Étude initiale & estimation d’impact

**Périmètre** : SEO technique, SEO sémantique, potentiel business.

### 3.0 Éléments obligatoires du rapport (nombre de problèmes, impact, prospects)

| Élément | Contenu |
|---------|---------|
| **Nombre de problèmes identifiés** | [Chiffrer après crawl Screaming Frog : nb URLs 4xx, 3xx, pages lentes, etc. Sinon : « À quantifier — exécuter un crawl complet et mettre à jour. »] |
| **Impact** | [Synthèse : perte de crawl budget, Core Web Vitals, compréhension sémantique, positionnement. Ou renvoyer aux § 3.2 et 3.3.] |
| **Échantillon de 5 prospects** | [Si cibles/leads identifiés : nom, entreprise, pertinence. Sinon : « À renseigner après campagne ou enrichissement. »] |

---

### 3.1 Synthèse exécutive SEO

[2–4 phrases : potentiel de visibilité, freins techniques et sémantiques, état actuel (compréhension moteurs, positionnement, visibilité hors marque). Puis : ce qu’une correction permettrait (indexation, trafic qualifié, canal durable).]

---

### 3.2 Diagnostic SEO technique

#### 3.2.1 Codes de réponse HTTP

[Constats : 4xx, 3xx, chaînes de redirection. **Impact SEO** : crawl budget, PageRank, indexation.]

#### 3.2.2 Temps de réponse et performance

[Constats : seuils dépassés, pages lentes. **Impact SEO** : Core Web Vitals, crawl, mobile.]

#### 3.2.3 Architecture du site

[Constats : profondeur, orphelines, hiérarchie. **Impact SEO** : compréhension contenus, pages prioritaires.]

---

### 3.3 Diagnostic SEO sémantique

#### 3.3.1 Problème central : clarté sémantique

[Le site répond-il à « Sur quels sujets ce site est-il légitime ? » Intentions de recherche, vocabulaire, pages piliers.]

#### 3.3.2 Pages services et intentions de recherche

[Pages ciblant des requêtes précises ? Signaux sémantiques (lexique métier, cas d’usage) ? Conséquence sur le positionnement.]

#### 3.3.3 Autorité thématique

[Contenus experts, démonstrations, réponses structurées. Impact : crédibilité, longue traîne, moteurs IA.]

---

### 3.4 Opportunités SEO identifiées

| Opportunité | Description | Impact estimé |
|-------------|-------------|----------------|
| **Pages services orientées intention** | [service + problème, solution + métier] | [ex. +50 à +150 visites / mois / page en B2B] |
| **Pages piliers sémantiques** | [1 pilier par thème, maillage] | [compréhension Google, autorité] |
| **Optimisation GEO (moteurs IA)** | [contenus structurés, FAQ] | [visibilité indirecte, leads] |

---

### 3.5 Estimation d’impact global

**Scénario conservateur (6 à 9 mois)**

| Indicateur | Situation actuelle | Après optimisation |
|------------|--------------------|--------------------|
| Trafic SEO mensuel | [X–Y] | [estimation] |
| Requêtes positionnées | [X] | [estimation] |
| Leads SEO mensuels | [X] | [estimation] |
| Dépendance Ads | [Élevée / Moyenne / Faible] | [Réduite] |

*Hypothèses : [correction technique, contenus ciblés, suivi GSC].*

---

### 3.6 Priorisation des actions

| Phase | Période | Actions |
|-------|---------|---------|
| **Phase 1 – Fondations** | 0–30 jours | [4xx/3xx, temps de réponse, audit sémantique, pages stratégiques] |
| **Phase 2 – Activation** | 30–60 jours | [Pages services, piliers, maillage, balises] |
| **Phase 3 – Accélération** | 60–90 jours | [Contenus experts, GEO, ajustements] |

---

### 3.7 Conclusion SEO

[2–4 phrases : SEO pas exploité comme levier aujourd’hui ; blocages ; ce que la mise en œuvre permettrait ; potentiel réaliste.]

---

## 4. Verdict pour le projet LPPP (prospection)

[NOM_SOCIÉTÉ] est une **cible [pertinente / à qualifier / secondaire]** pour un profil « Growth Engineer » ou positionnement similaire :

- [Point 1 : produit, secteur, fiabilité.]
- [Point 2 : défi principal — techno vs acquisition / notoriété.]
- **Angle possible** : [Proposition de valeur concrète : pipelines, funnel, SEO, campagne ciblée, etc.]

---

## Références

- **Site** : [URL du site cible]
- **Étude détaillée** : [`etude-concurrentielle-pestel-swot-porter.md`](./etude-concurrentielle-pestel-swot-porter.md)
- **Structure rapport SEO** : `docs/base-de-connaissances/rapport-seo-prospect.md`
