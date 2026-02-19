# Brief visuels — Enjeux Casapy (4 slides + one-pager)

**Date** : 2026-02-18  
**Cible** : Graphiste, Webdesigner — visuels « slide-ready » pour présentation non-tech.  
**Règle** : 1 visuel = 1 message ; tout chiffré, relié à l’impact business.

---

## Visuels pré-générés (Matplotlib)

Les visuels suivants ont été générés par `scripts/generate_visuels_casapy.py` :

| Fichier | Description |
|---------|-------------|
| `slide1-impact-perf-business.png` | Chaîne cause → effet + impact 54 k€ |
| `slide2-waterfall-ttfb.png` | Waterfall TTFB vs Front (goulot serveur) |
| `slide3-hebergement-comparatif.png` | Mutualisé vs Stack adaptée (2 colonnes) |
| `slide4-matrice-seo-timeline.png` | Matrice Urgence/Impact + timeline 30/60/90 |
| `one-pager-dashboard-casapy.png` | Dashboard exécutif (4 blocs) |

---

## 1) Slide « Impact perf → Impact business »

**Message** : Serveur lent → TTFB 3,7 s → LCP 32 s → UX dégradée → -30 % conversion → **54 k€/mois**.

**Layout** (horizontal) :  
Serveur/Hosting → TTFB 3,7 s (rouge) → LCP 32 s (rouge) → UX dégradée (orange) → Perte conv. -30 % (orange) → **≈ 54 k€/mois** (gros chiffre).

**Mini-calc** : 10 k visites × 2 % × 900 € = 180 k€ CA/mois | 180 k€ × 30 % = **54 k€ impact**.

---

## 2) Slide « Diagnostic technique » (TTFB vs Front)

**Message** : Le goulot est le TTFB (serveur) — le front ne peut pas compenser.

**Waterfall** : DNS (court) → TTFB (très long, rouge) → Téléchargement (moyen) → Render/LCP (long, orange).

**Jauges** : TTFB 3,7 s / objectif < 0,8 s | LCP 32 s / objectif < 2,5 s.

---

## 3) Slide « Pourquoi l’hébergement bloque »

**Layout** : 2 colonnes — **Mutualisé (aujourd’hui)** vs **Recommandation (VPS/Cloud)**.

| Mutualisé | Reco |
|-----------|------|
| Ressources partagées | CPU/RAM dédiés |
| PHP-FPM partagé | Cache (Redis, full page) |
| MySQL partagé | DB optimisée |
| Pics = perf instable | Monitoring, auto-scaling |
| **Risque élevé** | **Perf stable** |

---

## 4) Slide « SEO & Growth : état → plan »

**Matrice 2×2** (Urgence vs Impact) :
- **Quick wins / High impact** : Canonicals, hreflang, structure URLs, clusters sémantiques.
- **Structurant / High impact** : Architecture SEO, pages piliers, données structurées.
- **Quick wins / Lower** : Titles/meta, internal linking.
- **À clarifier** : Acquisition payante (Meta/Google : aucune trace).

**Timeline** : 0–30 j (perf serveur + tracking) | 30–60 j (clusters + CRO) | 60–90 j (scale contenus + campagnes tests).

---

## Bonus — One-pager

4 blocs : (1) Core Web Vitals (jauges) | (2) Impact 54 k€ | (3) Causes racines (hosting, WooCommerce, DB) | (4) Roadmap 3 étapes.

---

## Style graphique

- **Rouge** = problème | **Orange** = moyen | **Vert** = objectif.
- Chiffres clés en gros : **3,7 s / 32 s / -30 % / 54 k€**.
- 1 graphique + 1 phrase par slide.

### Contraste (fond sombre)

- **Fond sombre** → **texte blanc** pour tous les textes.
- **Mise en valeur** (chiffres, So what, accents) → **couleurs claires** : jaune, orangé, ou bleu turquoise.

---

*Brief maintenu par Rédacteur / Designer. Référence : landing-proposition-casapy.json, rapport-complet-casapy.md.*
