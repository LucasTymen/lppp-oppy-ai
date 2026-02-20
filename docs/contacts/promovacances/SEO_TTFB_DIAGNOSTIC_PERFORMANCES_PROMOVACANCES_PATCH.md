# Patch à appliquer dans `docs/BASE_CONNAISSANCES/SEO_TTFB_DIAGNOSTIC_PERFORMANCES.md`

1) Insérer la section ci-dessous (Promovacances) juste après le cas d’usage Casapy.  
2) Renommer l’ancienne section `## 4. Références` en `## 5. Références` (et ajuster les sous-niveaux si besoin).  
3) Mettre à jour la ligne **Dernière mise à jour** : `2026-02-19`.

---

## 4. Cas d’usage : Promovacances (exemple réalisé)

**Site** : [Promovacances](https://www.promovacances.com/) (agence de voyage, bons plans vacances).

### 4.1 TTFB
- **Échantillon** : 5 mesures sur la home (`https://www.promovacances.com/`)
- **Médiane** : **~0,10 s** (≈ 100 ms)

**Interprétation (règle projet)** :  
- **TTFB < 500 ms** → si les performances perçues sont mauvaises, prioriser l’analyse **front-end** (JS/CSS/rendu/LCP) plutôt que le serveur.

> Détail des mesures : voir `benchmarks/reports/technology_detector/technology_detector_20260219_164653.json` / `.md`.

### 4.2 Stack et type de serveur (visible)
**Headers (recon)** :
- `Server: fasterize`
- `Via: ...cloudfront.net (CloudFront)`
- `X-Cache: Hit from cloudfront`
- `X-Powered-By`: *(vide)*

**DNS** :
- `CNAME` → `www.promovacances.com.fasterized.com.`

**Conclusion stack** :  
- ✅ Trafic derrière une **stack embarquée** (**Fasterize** + **Amazon CloudFront**).  
- ❌ **Origine non exposée** → techno backend **non déterminable** avec ces seuls signaux.

### 4.3 Conclusion
- TTFB médian ~100 ms : **serveur OK**.
- En cas de lenteur, suspect n°1 : **front-end** (assets, JS, rendu, LCP…).
- Référence : rapports `technology_detector_20260219_164653.*`.

---

> ⚠️ Pense à décaler la section “Références” existante en **§5** si ton fichier était déjà structuré avec “§4 Références”.

