# Rapport complet Casapy — Audit SEO & Étude marketing

**Date** : 2026-01-30  
**Source** : `SEO_Casapy_rapport_performances_et_diagnostique.md`, `etude-marketing-casapy-clean-room.md`.  
**Usage** : Landing Casapy, page rapport, livrables projet LPPP.

---

## Contexte

Casapy est un e-commerce (canapés convertibles, ameublement) sur stack **WordPress / WooCommerce / Elementor**, hébergé sur **o2switch PowerBoost v3** (mutualisé). Ce rapport regroupe le diagnostic technique SEO, l’estimation du manque à gagner et l’analyse marketing en clean room (faits vs hypothèses).

---

## 1. Diagnostic technique — TTFB

### TTFB mesuré (médiane sur 5 prises)

| Page         | TTFB    |
|--------------|---------|
| Homepage     | ~3,77 s |
| Page produit | ~3,63 s |

**Référence SEO :**
- Bon : &lt; 500 ms  
- Problème : &gt; 1 s  
- Critique : &gt; 2 s  
- Casapy : **~3,7 s**

### Lecture stratégique

Le problème principal est **serveur/backend**, pas prioritairement JS/CSS.

Le LCP à 32 s devient logique :
1. 3,7 s pour commencer à répondre
2. Elementor + WooCommerce chargent
3. Scripts multiples
4. Images lourdes
5. Requêtes SQL

→ Effondrement mobile.

### Hébergement identifié

- **Stack** : o2switch PowerBoost v3 (mutualisé)
- **Reverse DNS** : odns.fr

Pour WooCommerce + Elementor, un mutualisé reste insuffisant : ressources partagées, CPU limité, PHP-FPM partagé, base MySQL partagée.

---

## 2. Impact business et manque à gagner

Avec un TTFB de 3,7 s :
- Perte SEO (Core Web Vitals)
- Baisse du crawl efficiency
- Augmentation du taux de rebond
- **Perte de conversion mobile massive**
- CPC Ads plus chers

**Perte de conversion estimée : 25 à 50 %** — hypothèse conservatrice : **30 % de conversions perdues**.

### Scénarios chiffrés (hypothèses réalistes)

Panier moyen secteur canapés : 600 € (bas) | 900 € (moyen) | 1 200 € (haut).

#### Cas 1 — 5 000 visiteurs / mois

| Conversion | Perte 30 % | Perte mensuelle (600 €) | Perte mensuelle (900 €) | Perte mensuelle (1 200 €) |
|------------|------------|-------------------------|-------------------------|---------------------------|
| 2 %        | 30 ventes  | 18 000 €                | 27 000 €                | 36 000 €                  |
| 5 %        | 75 ventes  | 45 000 €                | 67 500 €                | 90 000 €                  |

#### Cas 2 — 10 000 visiteurs / mois

| Conversion | Perte 30 % | Perte mensuelle (600 €) | Perte mensuelle (900 €) | Perte mensuelle (1 200 €) |
|------------|------------|-------------------------|-------------------------|---------------------------|
| 2 %        | 60 ventes  | 36 000 €                | 54 000 €                | 72 000 €                  |
| 5 %        | 150 ventes | 90 000 €                | 135 000 €               | 180 000 €                 |

**Lecture conservatrice** : 10 000 visiteurs, 2 % conversion, panier 900 € → **~54 000 € / mois** potentiellement impactés.

Un hébergement mutualisé à 30 €/mois qui provoque 30 000 € de perte mensuelle → **ROI d’une migration serveur quasi immédiat**.

---

## 3. Plan d’action (ordre prioritaire)

### Étape 1 — Serveur (priorité absolue)

- **Option A** : Redis object cache, page cache WooCommerce intelligent, OPcache, PHP 8.2
- **Option B** : Migration vers VPS ou hébergement WooCommerce optimisé (recommandé)

### Étape 2 — Base de données

- Nettoyage sessions WooCommerce
- Révision index MySQL
- Nettoyage transients
- Suppression révisions massives

### Étape 3 — Front-end (après serveur)

- Optimisation LCP image
- Défer JS Elementor
- Supprimer jQuery Migrate si possible
- Audit Bootstrap 3

---

## 4. Étude marketing (clean room)

**Constat factuel** : aucune trace de publicité Meta ou Google (Meta Ads Library, Google Ads Transparency).

### Marché et positionnement

- Secteur ameublement en ligne : concurrentiel (acteurs omnicanaux, marketplaces, pure players).
- USP, persona et concurrents : à extraire du site et à valider (voir `etude-marketing-casapy-clean-room.md`).

### Funnel AARRR (retail)

- **Acquisition** : SEO (pages catégories, filtres crawlables, contenus, maillage) ; SEA/Shopping (actuellement non actif ou non visible) ; social (organique, UGC).
- **Activation** : checklist fiche produit (photos HD, dimensions, avis, réassurance livraison/retours).
- **Rétention** : post-achat, email, reco, inspiration.

### SWOT

- Forces, faiblesses, opportunités, menaces à remplir avec preuves (voir doc clean room).

---

## 5. Proposition de valeur — Ce que ce livrable apporte

- **Diagnostic technique** : TTFB, LCP, hébergement, plan d’action priorisé.
- **Estimation chiffrée** : scénarios manque à gagner (conservateurs).
- **Étude marketing clean room** : faits vs hypothèses, champs à compléter.

---

*Document maintenu par Rédacteur / Expert SEO. Dernière mise à jour : 2026-01-30.*
