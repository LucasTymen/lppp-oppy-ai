# Rapport complet Infopro Digital — Audit SEO & positionnement marketing

**Date** : 2026-02  
**Sources** : RAPPORT_INFOPRO_DIGITAL_20260220.md, Wappalyzer, étude complète (infopro-digital etude complete), audit SEO (Screaming Frog, PageSpeed), crawl 358 URLs.  
**Usage** : Landing Infopro, page rapport, livrables projet LPPP.

---

## Contexte — Un géant au carrefour de l’info et du business

Infopro Digital n’est pas une agence de com : c’est un **géant technologique et médiatique B2B** qui transforme la donnée technique en décisions business pour les professionnels. Le groupe édite des médias (L’Usine Nouvelle, Le Moniteur, L’Argus), des logiciels, des bases de données, des plateformes de leads et organise des salons professionnels. Le modèle combine **médias + lead generation** : l’info attire, les marketplaces (ExpoPermanent) convertissent.

**Promesse** : « Nous vous aidons à prendre les meilleures décisions professionnelles. »  
**Cible** : décideurs, ingénieurs, acheteurs industriels, assureurs.  
**Positionnement** : passage obligé entre fournisseur et client industriel.

---

## 1. Diagnostic technique — TTFB et stack

### TTFB mesuré (2026-02-20)

| Mesure | TTFB |
|--------|------|
| Médiane (5 prises) | ~0,153 s (~153 ms) |

**Interprétation** : le serveur répond très vite. En cas de perfs décevantes (PageSpeed 68), le bottleneck est côté **front-end** (JS, images, LCP), pas serveur.

### Stack identifiée (Wappalyzer + Technology Detector)

| Catégorie | Technologies |
|-----------|--------------|
| **CMS** | WordPress, Yoast SEO, WP Rocket 3.19.3, Polylang |
| **Infra** | Amazon CloudFront (CDN), Nginx, Amazon Web Services |
| **Front** | Swiper, Preact, LazySizes, jQuery 3.7.1, jQuery Migrate |
| **Data / MarTech** | Piano Analytics, Salesforce Audience Studio, Google Tag Manager, Google AdSense |
| **Conformité** | Didomi (cookies), HSTS |
| **Métadonnées** | Open Graph, HTTP/3 |

Synthèse : stack moderne, CDN CloudFront en première ligne, cache WP Rocket. L’origine WordPress (hébergement) n’est pas identifiable via les headers (via CloudFront).

---

## 2. Audit SEO (crawl 358 URLs)

### PageSpeed Mobile (infopro-digital.com)

| Métrique | Valeur | Statut |
|----------|--------|--------|
| Performance | 68 | Moyen (orange) |
| Accessibilité | 99 | Vert |
| Bonnes pratiques | 96 | Vert |
| SEO | 91 | Vert |

**Blocage principal** : images (alt manquant 88 %, dimensions 62,7 %, 41 images > 100 Ko), layout (CLS), JS.

### Indexabilité et temps de réponse

- **URLs crawlées** : 358  
- **URLs indexables** : 337 (21 non indexables)  
- **URLs répondant en < 1 s** : 97,2 % (349 URLs)  

La majorité des pages répond vite. Les lenteurs semblent plutôt côté front (JS, rendu, images) que serveur.

### Problèmes prioritaires (d’après audit_rapport_aperçu_problemes.csv)

| Priorité | Problème | URLs | % |
|----------|----------|------|---|
| Élevée | 4xx internes | 3 | 0,6 % |
| Élevée | Hreflang liens de retour manquants | 3 | 1,9 % |
| Élevée | URL HTTP | 1 | 0,3 % |
| Élevée | Pagination : URL pas dans balise ancrage | 2 | 1,3 % |
| Élevée | Canonique non indexable | 1 | 0,6 % |
| Élevée | Hreflang : ne pas utiliser version canonique | 1 | 0,7 % |
| Élevée | Hreflang : liens retour non canoniques | 1 | 0,7 % |
| Moyenne | Title doublon | 20 | 12,9 % |
| Moyenne | Title < 30 caractères | 8 | 5,2 % |
| Faible | Meta descriptions manquantes | 108 | 69,7 % |
| Faible | Images sans alt | 118 | 88 % |
| Faible | H2 manquants | 92 | 59,4 % |
| Faible | Images dimensions manquantes | 84 | 62,7 % |
| Faible | Images > 100 Ko | 41 | 30,6 % |
| Faible | Headers sécurité (X-Frame-Options, CSP, X-Content-Type-Options) | 54–97 % des pages |

---

## 3. Positionnement et stratégie marketing

### 3 piliers stratégiques

1. **Inbound de masse (Content Factory)**  
   Autorité des marques (Le Moniteur, L’Usine Nouvelle) et automatisation pour couvrir des milliers de micro-niches (pompes hydrauliques, logiciels paie BTP…). Le contenu automatisé doit rester qualitatif pour maintenir l’autorité.

2. **Long-tail**  
   Priorité aux requêtes ultra-qualifiées plutôt qu’aux mots-clés à gros volume. Défi : piloter la performance de milliers de pages (Search Console, Semrush).

3. **SEO vs GEO**  
   Les bases de données sont un atout pour les moteurs IA (Perplexity, Gemini). Transformer les données en réponses citables.

### Funnel AAARR (Pirate Metrics) — B2B

| Étape | Objectif | Leviers Infopro |
|-------|----------|-----------------|
| **Acquisition** | Attirer l’audience | SEO de masse, Content Factory, newsletters, SEA & Social Ads (LinkedIn) |
| **Activation** | Première expérience positive | Consommation de contenu, UX/Performance, micro-conversions (newsletter, téléchargement) |
| **Adoption** | Faire revenir | Alertes pro, compte utilisateur, webinars récurrents |
| **Revenu** | Monétiser | Abonnements SaaS/Médias, Lead Gen (ExpoPermanent), publicité & sponsoring |
| **Referral** | Recommandation | Partage LinkedIn, marque employeur, viralité du contenu (baromètres, rapports) |

En B2B, le **Search** reste central ; le paid social complète pour notoriété et leads.

### Google vs Meta

- **Google** : capture de demande, requêtes, intention, mots-clés.  
- **Meta** : génération de demande, créas, test & learn.  
- En B2B, le Search garde une place centrale ; le paid social complète pour notoriété et génération de leads.

---

## 4. PESTEL synthétique

| Dimension | Enjeux clés |
|-----------|-------------|
| **Politique** | Souveraineté numérique, DSA, stabilité réglementaire (BTP, Industrie, Assurance) |
| **Économique** | Passage vers abonnements SaaS et Lead Gen (résilient), arbitrage budgétaire B2B |
| **Social** | Infobésité, besoin de sources certifiées, pénurie de profils hybrides |
| **Technologique** | IA & Content Factory, GEO (SGE, Perplexity), Data & Analytics |
| **Environnemental** | RSE, sobriété numérique, reporting extra-financier |
| **Légal** | RGPD, propriété intellectuelle, Loi AI Act |

---

## 5. SWOT synthétique

**Forces** : Leadership sur marchés de niche, modèle diversifié (SaaS + leads + pub), bases de données propriétaires, expertise tech intégrée.  
**Faiblesses** : Complexité de l’écosystème, inertie structurelle, dépendance au SEO.  
**Opportunités** : GEO, industrialisation par l’IA, expansion internationale, digitalisation B2B.  
**Menaces** : Érosion SEO par l’IA (zero-click), nouveaux entrants agiles, évolution réglementaire.

---

## 6. Concurrents principaux

| Concurrent | Typologie | Force principale |
|------------|-----------|------------------|
| DirectIndustry | Marketplace B2B | Puissance mondiale sur catalogues industriels |
| Kompass | Annuaire | Base de données structurée, data pure |
| Wolters Kluwer | Info pro | Expertise éditoriale (juridique, santé, risque) |
| LinkedIn | Réseau pro | Lead Gen, diffusion de contenus experts |
| Groupe Les Échos | Média | Influence auprès des cadres, Vivatech |
| Europages | Mise en relation B2B | SEO multilingue, sourcing industriel |
| GlobalSpec | Ingénierie | Recherche de composants, très technique |
| Newsweb / BFM Business | News / Veille | Audience chefs d’entreprise |

---

## 7. Formules et ordres de grandeur (Growth / Maths)

### CA mensuel

```
CA = Visites × CVR × AOV
```

### Perte de ventes (si perte de conversion p)

```
LostOrders = Visites × CVR × p  →  LostRevenue = LostOrders × AOV
```

**Exemple** : 30 k visites, 1,5 % CVR, panier 1 200 €, perte 18 % → LostRevenue ≈ ~28 k€/mois.

Ordre de grandeur. Recalibrer avec vos données (trafic, CVR, panier).

### Objectifs SMART (exemples pour poste Content Ops)

| Objectif | Spécifique | Mesurable | Échéance |
|----------|------------|-----------|----------|
| Content Factory | Améliorer workflow contenus IA | +25 % de volume | Fin S1 |
| Qualité SEO | Réduire erreurs techniques | 95 % conformité audits | Bilan 3 mois |
| GEO | Être cité par moteurs IA | 10 mots-clés stratégiques | 12 mois |
| Conversion | Augmenter CTR vers formulaires | +10 % Lead Gen | 6 mois |

---

## 8. Plan d’action priorisé

1. **Images** : alt, width/height, compression (41 images > 100 Ko)  
2. **Meta & structure** : 108 meta descriptions, 92 H2 manquants  
3. **Technique** : 4xx (3 URLs), hreflang, pagination, canoniques  
4. **Sécurité** : X-Frame-Options, CSP, X-Content-Type-Options (54–97 % des pages)

---

## 9. Fichiers du livrable

| Fichier | Rôle |
|---------|------|
| `landing-proposition-infopro.json` | Contenu page proposition |
| `positionnement-marketing.html` | Positionnement / étude paid media |
| `infographie-infopro-7-formats.html` | Infographie 7 formats |
| `audit-dashboard.json` | Données dashboard audit |
| `infopro_style_tokens.css` | Palette, tokens CSS |
| `wappalyzer_infopro-digital-com.csv` | Stack technologique Wappalyzer |

---

*Sources : RAPPORT_INFOPRO_DIGITAL_20260220.md, wappalyzer_infopro-digital-com.csv, Screaming Frog, PageSpeed Insights, étude complète (infopro-digital etude complete), [Google Ads Transparency](https://adstransparency.google.com), Meta Ad Library.*
