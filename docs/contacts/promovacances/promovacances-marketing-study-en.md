# Promovacances — Marketing Study (English)

**Version** : Study / Internal.  
**Purpose** : consolidated view for SEO performance + paid media analysis. Data from public sources (Google Ads Transparency, Meta Ad Library, probing, PageSpeed).

---

## 1. SEO & Performance — Summary

**Site** : promovacances.com (travel, vacation packages, reservations)

### 1.1 TTFB (Time To First Byte)
- **Median** : ~0.10 s (5 measures on homepage)
- **Stack** : Fasterize (optimization/cache) → CloudFront (CDN) → client
- **Takeaway** : Server is fast. If users feel the site is slow, the main suspect is the front-end (JS, images, LCP), not the server.

### 1.2 LCP (Largest Contentful Paint)
- **Value** : ~5.2 s (to confirm with field measurements)
- **Context** : Hero image or main banner. In travel, visuals drive conversion. Optimizing image size, format, and priority is the main lever.

### 1.3 Conversion Loss
- **Estimated** : 18 % (delta CVR)
- **Scenario (demo)** : 30k visits, 1.5 % CVR, €1,200 AOV → ~€28k/month potential recovery

### 1.4 Action Plan (priority order)
1. **Images & LCP** — optimization, loading priority
2. **JS & third-parties** — defer, lazy load
3. **Server & cache** — marginal (TTFB already good)

---

## 2. Technical Stack (visible signals)

| Layer | Observation |
|-------|-------------|
| CDN | CloudFront (Via header, X-Cache) |
| Optimization | Fasterize (Server header, CNAME) |
| Backend | Not exposed (no X-Powered-By or similar) |

DNS: `www.promovacances.com.fasterized.com` → CloudFront.

---

## 3. Scenarios (revenue impact)

| Visits | CVR | AOV | Context | Monthly impact (order of magnitude) |
|--------|-----|-----|---------|-------------------------------------|
| 30k | 1.5 % | €1,200 | Demo | ~€28k |
| 60k | 2 % | €1,400 | To calibrate | — |
| 100k | 2.5 % | €1,600 | To calibrate | — |

Formula: LostRevenue ≈ Visits × CVR × loss% × AOV. Calibrate with GA4 data.

---

## 4. Paid Media

### 4.1 Sources
- **Google Ads Transparency** : adstransparency.google.com
- **Meta Ad Library** : search "Promovacances" or domain promovacances.com

### 4.2 Google Ads — Facts
- **Advertiser** : Karavel SAS (promovacances.com)
- **Volume** : ~3,000 ads (France region)
- **Format** : text, theme "Travel & tourism"

| Theme | Impressions | Period | Last run |
|-------|-------------|--------|----------|
| Sardinia | 800k–900k | Apr 2023 → Nov 2025 | Feb 2026 |
| All inclusive | 100k–125k | Nov 2024 → Nov 2025 | Feb 2026 |

PPC is structured. Themes rotate over long periods. Volume suggests templated / feed-driven campaigns.

### 4.3 Meta (Facebook / Instagram) — Facts
- **Declared targeting** : France, 18–65+, all genders (broad / algo-driven)
- **Content** : destinations, clubs, all-inclusive, promos

| Ad | Coverage (est.) | Note |
|----|-----------------|------|
| "Des séjours faciles, fiables…" | ~129k | — |
| UAE -30% (video 0:15) | — | ~57 % reach in 65+ |
| Club Framissima Greece | ~5.7k | Active 6h at capture |

**Age breakdown (Framissima Greece)** :
- 45–54 : ~21 %
- 55–64 : ~26 %
- 65+ : ~23 %
- 45+ total : ~70 %

**Gender** : ~66 % women

### 4.4 Hypotheses (unverifiable without account access)
1. **Broad ≠ random** : with broad targeting, algo optimizes delivery for objective (clicks, LPV, purchase).
2. **45+ / 65+ over-representation** : may come from creative (5★ club, peace of mind, beach) rather than explicit age targeting.
3. **65+ and “false clicks”** : possible risk depending on placements/device. Validate via LPV/CVR/CPA by age and placement, not blanket exclusions.
4. **Segment by creative, not audience** : keep broad for learning, differentiate messaging (Ibiza/Goa vs serenity vs family) rather than tight age targeting.
5. **Google Ads** = demand capture (queries, intent). **Meta** = demand generation (offers, creatives, test & learn).

### 4.5 Next steps for paid
- **Google** : keywords, ad variations, positions, competition (paid research tools).
- **Meta** : creative analysis (promo vs brand), rotation, landing coherence (conversion path), LPV/click and CVR/CPA by age if available.
- **Campaign objective** : clicks vs conversions — changes the diagnosis; not visible in Ad Library.

---

## 5. References

- Google Ads Transparency : https://adstransparency.google.com
- Meta Ad Library : search "Promovacances" or promovacances.com
- Technical diagnostic : `PROMOVACANCES_DIAGNOSTIC_20260219.md`
- Paid media analysis (FR) : `analyse-marketing-paid-media.md`
- Spec infographics : `spec-infographiques-visuel-contextuel-promovacances.md`

---

*Internal study. Data from public sources and probing (Feb 2026). Recalibrate with internal data for production use.*
