# Deck 7 slides + 1 one-pager — Spec exécutable (consultant-grade)

**Date** : 2026-01-30  
**Principe** : 1 idée/slide | ≤35 mots/slide | visuel recommandé + **So what** au même endroit (bas droite) | Wave = slide à part (pas bonus décoratif)

---

## Règles de design

- **So what** : toujours au **même endroit** (bas droite) sur toutes les slides.
- **Chiffres** : indiquer « Hypothèse / à valider » à côté de chaque chiffre non issu de GA4.
- **Wave** : slide dédiée (slide 7) — illustre **TTFB/LCP** (axe Y : plus bas = mieux) *ou* **CVR/CA** (axe Y : plus haut = mieux) selon choix ; par défaut **TTFB/LCP** pour alignement diagnostic.

### Contraste et couleurs (fond sombre)

- **Fond sombre** → **texte blanc** pour tous les textes (lisibilité).
- **Mise en valeur** (chiffres clés, So what, accents) → **couleurs claires** : jaune, orangé, ou **bleu turquoise** (pas de texte sombre sur fond sombre).

---

## Slide 1 — Problème : performance serveur

| Élément | Contenu |
|--------|---------|
| **Titre** | Le frein #1 est serveur, pas le front |
| **Texte (≤35 mots)** | Hébergement mutualisé → TTFB ~3,7s → LCP ~32s. Résultat : pages perçues "cassées/lentes", friction, perte de confiance et d'intention d'achat. |
| **Visuel** | Chaîne cause→effet (icônes) |
| **So what** | -30% conv ≈ **54k€/mois** (hypothèse à valider GA4) |

---

## Slide 2 — Pourquoi : preuve par diagnostic (TTFB)

| Élément | Contenu |
|--------|---------|
| **Titre** | Le goulot = temps de réponse serveur |
| **Texte** | TTFB bon <0,5s / critique >2s. Casapy est en zone rouge : la page attend le serveur avant de pouvoir afficher (LCP). |
| **Visuel** | Waterfall simplifié (TTFB rouge dominant) |
| **So what** | Priorité = backend/DB/hosting |

---

## Slide 3 — Cause racine : mutualisé inadapté à WooCommerce

| Élément | Contenu |
|--------|---------|
| **Titre** | Mutualisé = performance instable sur WooCommerce |
| **Texte** | Ressources partagées (CPU/PHP-FPM/DB) + WooCommerce/Elementor = latence variable, pics, lenteur structurelle. |
| **Visuel** | "Immeuble vs maison" (mutualisé vs VPS/stack) |
| **So what** | Stabiliser = améliorer UX + conversion |

---

## Slide 4 — Plan : 1-2-3 (serveur → DB → front)

| Élément | Contenu |
|--------|---------|
| **Titre** | Plan d'action priorisé |
| **Texte** | 1. Serveur : migration ou cache (Redis/OPcache). 2. DB : nettoyage transients/sessions + index. 3. Front : LCP image + defer JS + optimisation Elementor. |
| **Visuel** | 3 blocs numérotés |
| **So what** | Gains rapides + base saine pour CRO/SEO |

---

## Slide 5 — Ce que ça coûte : scénarios (cartes)

| Élément | Contenu |
|--------|---------|
| **Titre** | Manque à gagner (ordre de grandeur) |
| **Texte** | 3 scénarios montrent l'impact potentiel d'une perte de conversion à -30%. À recalibrer avec trafic réel + CVR + AOV (GA4). |
| **Visuel** | 3 cards (27k / 54k / 180k) |
| **So what** | La perf est un sujet **business**, pas technique |

---

## Slide 6 — Marketing : clean room (faits vs hypothèses)

| Élément | Contenu |
|--------|---------|
| **Titre** | Audit marketing : ce qui est prouvé vs à valider |
| **Texte** | FACT : pas de traces Meta/Google (à date des bibliothèques). HYPOTHESIS : persona, USP, funnel, canaux. Next : collecter 5 preuves site + tracking. |
| **Visuel** | Split "FACT / HYPOTHESIS" |
| **So what** | Décisions basées sur données, pas intuitions |

---

## Slide 7 — Ce que ça débloque : progression + cycles (Wave)

| Élément | Contenu |
|--------|---------|
| **Titre** | Après fix : baseline meilleure + volatilité plus faible |
| **Texte** | Les cycles (saisonnalité, stock, créas) restent, mais une infra saine augmente le niveau moyen et réduit les "creux". |
| **Visuel** | Sinusoïde + tendance, amplitude réduite après J0 (marqueur vertical "Fix (J0)" si possible) |
| **So what** | Amélioration durable : CVR, SEO (CWV), ROAS |

**Wave — choix d’axe** :
- **Option A (recommandée)** : **TTFB/LCP** — axe Y = temps (plus bas = mieux) ; avant fix = courbe haute, après fix = courbe plus basse + moins volatile.
- **Option B** : **CVR/CA** — axe Y = conversion ou CA (plus haut = mieux) ; après fix = niveau moyen plus haut + creux moins profonds.

---

# One-pager — Dashboard exécutif

| Bloc | Position | Contenu |
|------|----------|---------|
| **1 — Symptôme** | Top-left | TTFB ~3,7s ; LCP ~32s → zone rouge |
| **2 — Cause** | Top-right | Mutualisé + WooCommerce/Elementor → latence/variabilité |
| **3 — Impact** | Middle (gros chiffre) | Scénario conservateur : **~54k€/mois** (à valider GA4) |
| **4 — Plan 30 jours** | Bottom-left | Serveur/cache → DB → Front (3 étapes) |
| **5 — Marketing clean room** | Bottom-right | FACT/HYPOTHESIS + "5 preuves à fournir" + KPIs à installer (GA4/GTM) |

---

## Icônes cohérentes (suggestion)

- Serveur / hosting : serveur, datacenter, cloud
- DB : base de données, cylindre
- UX / front : écran, curseur, page
- Panier / conversion : panier, caddie, flèche
- SEO / CWV : graphique, jauge, Core Web Vitals
- Rouge = problème | Orange = moyen | Vert = objectif

---

## Rôles

| Rôle | Mission |
|------|---------|
| **Infographiste** | Illustrer les 7 slides + one-pager avec la même approche que précédemment (fond transparent, consultant-grade, visuels recommandés ci-dessus). |
| **Rédacteur en chef** | Texte explicatif très court et synthétique pour recontextualiser ; éviter la sensation "je ne comprends pas" pour quelqu'un pas du métier. |

---

*Spec prête à exécuter. Réf. brief-visuels-enjeux-casapy-slides.md, notes-infographie-necessaires.md. Segmentation : segmentations/2026-01-30-casapy-deck-7-slides-infographiste-redacteur.md.*
