# Spec deck Casapy — 7 slides + 1 one-pager (approche consultant-grade)

**Date** : 2026-02-19  
**Approche** : Problème → Pourquoi → Ce que ça coûte → Ce qu'on fait → Ce que ça débloque  
**Principe** : 1 slide = 1 idée | max 35 mots | badges Rouge/Orange/Vert | encadré « So what » (impact business)

---

## Slide 0 — Ce que j'offre (optionnel)

- 3 cartes : Audit technique perf (TTFB/LCP) | Audit SEO technique & sémantique | Audit Growth (AARRR + tracking + reco)
- CTA : « Consulter le rapport complet → »

---

## Slide 1 — Impact perf → Impact business

**Headline** : Le frein #1 est serveur : il dégrade l'UX et la conversion.

**Chaîne** : Hébergement mutualisé → TTFB ~3,7 s → LCP 32 s → Friction UX → -25 à -50 % conversion

**So what** : Scénario conservateur -30 % = ~54 k€/mois (10k visites / 2 % / 900 €)

---

## Slide 2 — Diagnostic : TTFB vs Front

**Headline** : Le goulot n'est pas d'abord le front : c'est la réponse serveur.

**Waterfall** : DNS court (vert) | TTFB très long (rouge) | Download moyen | Render/LCP long (orange)

**Contexte** : TTFB bon < 0,5 s / critique > 2 s → Casapy en zone rouge. LCP élevé en découle.

---

## Slide 3 — Mutualisé vs stack adaptée

**Headline** : WooCommerce + Elementor = besoin de ressources stables.

**Gauche** : Mutualisé (CPU/RAM partagés, perf variable) | ❌ risque élevé  
**Droite** : Stack adaptée (VPS, Redis, DB optimisée) | ✅ perf stable  
**Métaphore** : Immeuble vs maison

---

## Slide 4 — Priorités + plan d'action

**Headline** : Plan en 3 étapes : serveur, puis DB, puis front.

**Table criticité** : TTFB (critique) | LCP mobile (bloquant) | Hébergement (inadapté) | Perte conv (business)

**Roadmap** : 1. Serveur (VPS/Redis) | 2. DB (transients, index) | 3. Front (LCP, defer JS)

**So what** : Amélioration UX + baisse abandon + SEO (CWV) + ROAS meilleur

---

## Slide 5 — Manque à gagner (3 cartes)

Carte 1 : 5k / 2 % / 900 € → **27 k€/mois**  
Carte 2 : 10k / 2 % / 900 € → **54 k€/mois**  
Carte 3 : 10k / 5 % / 1200 € → **180 k€/mois**

*Scénarios pour cadrer l'ordre de grandeur — à recalibrer avec GA4 + taux conversion réel.*

---

## Slide 6 — Marketing clean room (FACT vs HYPOTHESIS)

**Headline** : On sépare faits et hypothèses.

**FACT** : Aucune trace pub Meta/Google | Marché concurrentiel  
**HYPOTHESIS** : Persona, positionnement, concurrents, funnel AARRR

**Next inputs** : USP, page livraison, PDP, catégories, avis

---

## One-pager — Dashboard exécutif

**Gauche** : Jauges TTFB/LCP | Impact 54 k€/mois | Cause racine mutualisé  
**Droite** : Roadmap serveur → DB → front | Marketing clean room | KPIs à suivre

---

## Graphique sinusoïde — Progression avant/après fix

**Modèle** : y(t) = (b + mt) + A·sin(2πt/T + φ) avec amplitude qui baisse après J30 (fix)

**Usage** : Avant fix = volatilité haute (mutualisé) | Après fix = baseline meilleure + volatilité réduite

**Fichier** : casapy-wave-progression.png (Matplotlib)

---

*Spec pour Graphiste + Rédacteur. Réf. brief-visuels-enjeux-casapy-slides.md.*
