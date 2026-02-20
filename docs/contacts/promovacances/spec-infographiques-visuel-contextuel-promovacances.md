# Promovacances — Infographiques visuelles + contextuelles (spec exécutable)

**Pour** : Infographiste + Rédacteur en chef.  
**Objectif** : étoffer les data avec des phrases courtes et dynamiques, en resituant les contextes, pour que le graphiste puisse créer les illustrations.

Référence : `docs/bonnes-pratiques.md`, `.cursor/rules/redacteur-en-chef.mdc`.  
Modèle : `docs/contacts/casapy/spec-infographiques-visuel-contextuel.md`.

---

## Consignes transverses

| Rôle | Consigne |
|------|----------|
| **Infographiste** | S'inspirer des blocs ci-dessous (jauges TTFB, chaîne priorité, cartes scénarios, plan). Cohérence avec la charte Promovacances (fond clair, Roboto, bleu #3999E5). |
| **Rédacteur en chef** | Chaque bloc visuel est accompagné d'un texte court qui explique le pourquoi et la conséquence. Compréhensible par un humain, non marqué IA. Une phrase sous le visuel suffit. |

---

## A) Blocs à illustrer (data + contexte)

### 1) "Priorités techniques" — TTFB OK, prioriser le front

**Visuel** : 3 barres ou chips (statut vert / orange / rouge) :
- TTFB ~0,10 s → **OK** (serveur réactif)
- LCP 5,2 s → **À améliorer** (contenu principal tardif)
- Perte conversion 18 % → **Impact business**

**Texte contexte (≤35 mots)** :
> Le serveur répond en 0,1 s. Le goulot n’est pas là. C’est le front (images, JS) qui retarde le rendu et pèse sur la conversion.

---

### 2) "Chaîne de priorité" — Images & LCP → JS → Serveur (marginal)

**Visuel** : flowchart 3 boîtes + flèches :
**Images & LCP** → **JS & third-parties** → **Serveur & cache**

**Texte contexte** :
> TTFB déjà bon. Les gains sont sur les images et le JS. Le serveur, on le touche en dernier.

---

### 3) "Manque à gagner" — 3 cartes scénarios

**Visuel** : 3 cards avec inputs (visites, CVR, panier) + ventes perdues + impact mensuel.

| Scénario | Contexte | Impact mensuel |
|----------|----------|----------------|
| 30 k / 1,5 % / 1 200 € | Démo | ~28 k€ |
| 60 k / 2 % / 1 400 € | À recalibrer | — |
| 100 k / 2,5 % / 1 600 € | À recalibrer | — |

**Texte contexte** :
> Ordre de grandeur pour un site tourisme. Les vrais chiffres dépendent de ton trafic et de ton panier. Le dashboard permet de tester plusieurs hypothèses.

---

### 4) "Plan d'action priorisé" — Images → JS → Cache

**Visuel** : timeline ou 3 étapes numérotées :
1. Images & LCP (optimisation, priorité)
2. JS & third-parties (defer, lazy load)
3. Serveur & cache (marginal)

**Texte contexte** :
> Priorité 1 : images et LCP. Priorité 2 : JS. Priorité 3 : serveur, parce qu’il est déjà bon.

---

### 5) "Recovery rings" — répartition du potentiel de gain

**Visuel** : 3 anneaux ou donut :
- 50 % Images & LCP
- 35 % JS & third-parties
- 15 % Serveur & cache

**Texte contexte** :
> Où mettre l’effort en premier. La moitié du gain vient des images et du LCP.

---

### 6) "Waterfall" — requête → TTFB → FCP → LCP → TTI

**Visuel** : barres horizontales (0 s → 8 s) :
- Requête HTML / TTFB : 0,1 s (vert)
- CSS / Fonts : 0,8 s
- JS : 1,2 s
- Images hero : 2,2 s
- LCP : 1,8 s (rouge, conséquence)

**Texte contexte** :
> Le serveur répond vite. Ensuite, CSS, JS et images s’enchaînent. Le LCP arrive tard à cause de ça.

---

## B) Formules (réutilisables)

### CA mensuel
```
CA = Visits × CVR × AOV
```

### Perte de ventes (si perte conversion p)
```
LostOrders = Orders × p
LostRevenue = LostOrders × AOV
```

**Ex. 30 k visites, 1,5 % CVR, panier 1 200 €, perte 18 %** :
- Orders = 450
- LostOrders (18 %) ≈ 81
- LostRevenue ≈ 97 k€/an → ~28 k€/mois

---

## C) Labels JSON (champs existants)

Pour les blocs `type: infographic` dans `landing-proposition-promovacances.json` :
- `ttfb-kpi-bars-promo` → Priorités techniques — TTFB OK, prioriser front
- `flowchart-front-promo` → Chaîne de priorité — Images & LCP → JS → Serveur (marginal)
- `plan-timeline-promo` → Plan d'action priorisé — Images → JS → Cache

---

*Document créé pour que le graphiste ait le contexte suffisant pour illustrer chaque bloc. Données sources : landing-proposition-promovacances.json, audit-dashboard.json, PROMOVACANCES_DIAGNOSTIC_20260219.md.*
