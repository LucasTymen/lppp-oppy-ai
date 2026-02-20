# Promovacances — Probing & diagnostic (Tech / Réseaux / DevOps / Pentest)

**Site** : https://www.promovacances.com/  
**Date** : 2026-02-19  
**Objectif** : synthèse rapide “stack visible”, exposition de l’origine, et lecture perf côté serveur (TTFB).

---

## 1) Résumé exécutable (TL;DR)
- Le trafic passe par une **stack embarquée** : **Fasterize (optimisation/cache)** → **Amazon CloudFront (CDN)** → client.
- L’**origine n’est pas exposée** (pas de headers backend / techno serveur applicatif).
- **TTFB médian ~0,10 s** (5 mesures sur la home) : côté serveur, c’est **bon**. Si la perf utilisateur est mauvaise, le **suspect n°1 est le front** (JS/CSS/rendu/LCP).

---

## 2) Technology detector (recon)
**Rapports source** :  
- `benchmarks/reports/technology_detector/technology_detector_20260219_164653.json`  
- `benchmarks/reports/technology_detector/technology_detector_20260219_164653.md`

### 2.1 Headers
| Header | Valeur |
|---|---|
| `Server` | `fasterize` |
| `X-Powered-By` | *(vide)* |
| `Via` | `1.1 ddd858d5f65a619c7f96bffdd59c00a6.cloudfront.net (CloudFront)` |
| `X-Cache` | `Hit from cloudfront` |

### 2.2 DNS
| Type | Valeur |
|---|---|
| A | `195.149.66.20` |
| AAAA | *(—)* |
| CNAME | `www.promovacances.com.fasterized.com.` |
| Reverse DNS (PTR) | *(vide sur l’IP CloudFront / non exploitable)* |

---

## 3) Type de serveur : “embarquée” ou non ?
✅ **Oui : stack embarquée (CDN + optimisation)**
- **Fasterize** en couche d’optimisation/cache devant l’origine.
- **CloudFront** en frontal (présence dans `Via` + `X-Cache`).

**Chaîne typique** : Origine (serveur applicatif) → Fasterize → CloudFront → client.

ℹ️ **Origine non qualifiable** avec ces seuls signaux : mutualisé / VPS / dédié / cloud **indéterminable** tant que l’origine ne fuit pas de headers ou d’artefacts.

**Confiance** :
- **Forte** sur “Fasterize + CloudFront” (CNAME + headers).
- **Faible** sur la techno backend (aucun header utile exposé).

---

## 4) TTFB (Time To First Byte)
**Mesures** : 5 mesures sur `https://www.promovacances.com/`  
**Médiane** : **~0,10 s** (≈ 100 ms)

**Interprétation projet** :
- **TTFB < 500 ms** → si la perf est “lamentable”, le coupable probable est le **front-end** (JS, CSS, rendu, LCP), plus que le serveur.

---

## 5) Recommandations (techniques & SEO perf)
1. **Ne pas accuser le backend** tant que les métriques terrain (RUM) confirment : avec un TTFB médian ~100 ms, les gains côté serveur seront souvent marginaux vs LCP/INP.
2. Prioriser :
   - **LCP** : taille/ordre de chargement des ressources critiques, preloading, compression, cache.
   - **JS** : bundle splitting, déferrement, réduction du main thread, pruning.
   - **Images** : formats modernes, dimensions, lazy-load, poids.
3. Pour identifier l’origine : collecter (si possible) cookies/headers sur endpoints non cachés, traces d’erreurs, et fingerprinting passif (sans attaque).

---

## 6) Annexes
- Les détails (preuves brutes) sont dans les rapports `technology_detector_20260219_164653.*`.
