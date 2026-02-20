# Rapport d'analyse détaillé : Infopro Digital

**Cible** : [Infopro Digital](https://www.infopro-digital.com/fr/)  
**Secteur** : Média B2B — information, data, technologies pour les entreprises  
**Date** : 2026-02-20  
**Méthodologie** : Technology Detector (Pentester + DevOps), mesure TTFB, stack technique documentée

---

## 1. Vue d'ensemble

Infopro Digital est le **leader B2B en information, data et technologies** pour les entreprises. Le groupe édite des logiciels, bases de données, plateformes de leads, organise des salons professionnels et couvre plusieurs secteurs (Construction, Automobile, Risques & Assurances, Industrie, Distribution).

**Positionnement** : connecter les communautés professionnelles via l'information et les technologies.

---

## 2. Stack technique (inventaire)

### 2.1 Front-end

| Catégorie | Technologies |
|-----------|--------------|
| **Librairies JS** | Swiper, Preact, LazySizes, jQuery 3.7.1, jQuery Migrate 3.4.1 |
| **Performance** | LazySizes (lazy loading images), Preact (bundle léger) |
| **UI** | Swiper (carrousels) |

### 2.2 Back-end / CMS

| Catégorie | Technologies |
|-----------|--------------|
| **CMS** | WordPress |
| **Blog** | WordPress |
| **Langage** | PHP |
| **Base de données** | MySQL |
| **Plugins WordPress** | Yoast SEO, WP Rocket 3.19.3, Polylang |

### 2.3 Infrastruture / DevOps

| Catégorie | Technologies |
|-----------|--------------|
| **Serveur web** | Nginx |
| **Proxy inversé** | Nginx |
| **CDN** | Amazon CloudFront |
| **PaaS** | Amazon Web Services (AWS) |
| **Cache** | WP Rocket 3.19.3 (cache page, minification) |
| **Protocole** | HTTP/3 |

### 2.4 Data / Analytics / MarTech

| Catégorie | Technologies |
|-----------|--------------|
| **Analytics** | Piano Analytics |
| **Personalisation** | Piano |
| **Segmentation** | Salesforce Audience Studio |
| **Plateforme données clients** | Salesforce Audience Studio |
| **Gestionnaire de balises** | Google Tag Manager |
| **Régie publicitaire** | Google AdSense |

### 2.5 SEO / Traduction / Sécurité

| Catégorie | Technologies |
|-----------|--------------|
| **SEO** | Yoast SEO |
| **Traduction** | Polylang (multilingue FR/EN) |
| **Conformité cookies** | Didomi |
| **Sécurité** | HSTS |
| **Métadonnées** | Open Graph |

---

## 3. Benchmark Technology Detector (2026-02-20)

### 3.1 Configuration

- **URL** : https://www.infopro-digital.com/fr/
- **Domaine** : infopro-digital.com
- **Technologies connues en entrée** : WordPress, Nginx, CloudFront, Yoast SEO, WP Rocket, Piano Analytics, Polylang
- **Script** : `scripts/benchmark/run_technology_detector_benchmark.sh`

### 3.2 Résultats Pentester (headers, DNS)

| Indice | Valeur |
|--------|--------|
| **Server** | nginx |
| **X-Powered-By** | _(vide)_ |
| **X-Host** | _(vide)_ |
| **Via** | 1.1 458e178928cba27987d8f2cdf2fced38.cloudfront.net (CloudFront) |
| **X-Cache** | Miss from cloudfront |

**DNS**

| Type | Valeurs |
|------|---------|
| **A** | 81.92.95.55, 81.92.94.54, 152.89.172.56 |
| **AAAA** | 2a01:c8:101::55, 2a09:35c0:102::56, 2a01:c8:100::54 |
| **CNAME** | d298e8qyc37j0i.cloudfront.net. |
| **Reverse DNS (PTR)** | cdn.perf1.com. |

### 3.3 Hypothèse hébergement (DevOps)

- **Type** : indéterminé
- **Confiance** : low
- **Sources** : Server (nginx générique)

**Interprétation** :  
Les headers n'exposent pas d'indice fort (X-Powered-By masqué, pas de marque Kinsta/WP Engine). Le CNAME pointe vers **CloudFront** (CDN AWS). Le PTR `cdn.perf1.com` suggère une couche supplémentaire (Perf1, CDN/accélération français). L’origine (hébergement WordPress réel : mutualisé, VPS ou cloud) n’est pas identifiable via les seuls headers et DNS.

---

## 4. Mesure TTFB (Time To First Byte)

### 4.1 Protocole

- 5 mesures sur la homepage `https://www.infopro-digital.com/fr/`
- Commande : `curl -w '%{time_starttransfer}\n' -o /dev/null -s -m 30`
- Date : 2026-02-20

### 4.2 Résultats

| # | TTFB (s) |
|---|----------|
| 1 | 0,148 |
| 2 | 0,148 |
| 3 | 0,153 |
| 4 | 0,167 |
| 5 | 0,185 |

**Médiane** : ~0,153 s (~153 ms)

### 4.3 Interprétation (règle SEO_TTFB)

| TTFB | Interprétation | Coupable probable |
|------|----------------|-------------------|
| **TTFB > 1 s** | Serveur lent | Problème serveur |
| **TTFB < 500 ms** | Serveur rapide | Problème front-end |

→ **TTFB ≈ 150 ms** : le serveur / CDN répond très vite. En cas de perfs décevantes (Core Web Vitals), le **bottleneck serait côté front-end** (JS, CSS, rendu, LCP, CLS) plutôt que serveur.

---

## 5. Synthèse infrastructure

```
[Client] → [CloudFront CDN] → [Origin ?]
                ↑
         CNAME : d298e8qyc37j0i.cloudfront.net
         Via: cloudfront.net
         PTR (IP) : cdn.perf1.com
```

- **CDN** : CloudFront (AWS) en première ligne
- **Cache** : X-Cache « Miss from cloudfront » lors du benchmark — pas de hit au moment de la mesure
- **Serveur exposé** : nginx (proxy ou origin)
- **Hébergement WordPress** : non identifiable (headers masqués, CDN devant)

---

## 6. Points forts identifiés

1. **Stack moderne** : CloudFront, HTTP/3, HSTS, WP Rocket
2. **TTFB excellent** : ~150 ms, indiquant une bonne couche CDN/cache
3. **SEO structuré** : Yoast SEO, Open Graph
4. **Écosystème data** : Piano Analytics, Salesforce Audience Studio, GTM
5. **Multilingue** : Polylang (FR/EN)
6. **Conformité** : Didomi pour les cookies

---

## 7. Pistes d’optimisation (si besoin)

- **Core Web Vitals** : avec un TTFB faible, toute latence ressentie viendrait du front (JS, CSS, LCP). Piste : audit LazySizes, Swiper, jQuery.
- **Cache CDN** : lors du benchmark, X-Cache = Miss ; vérifier la couverture des pages stratégiques en Hit pour les visiteurs récurrents.
- **JS** : jQuery + jQuery Migrate + Preact — possibilité de rationaliser (Preact peut remplacer jQuery pour certaines parties).

---

## 8. Références

| Document | Chemin |
|----------|--------|
| Cas d'école Technology Detector | `docs/BASE_CONNAISSANCES/CAS_ECOLE_TECHNOLOGY_DETECTOR_BENCHMARK.md` |
| TTFB et diagnostic SEO | `docs/BASE_CONNAISSANCES/SEO_TTFB_DIAGNOSTIC_PERFORMANCES.md` |
| Rapport benchmark JSON | `benchmarks/reports/technology_detector/technology_detector_20260220_134922.json` |
| Rapport benchmark MD | `benchmarks/reports/technology_detector/technology_detector_20260220_134922.md` |
