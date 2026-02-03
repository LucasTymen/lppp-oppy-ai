# Rapport complet ACKURACY — Société, stratégie et SEO

**Contact** : Alexis Clavier (Sales Representative) — ackuracy.com  
**Date** : 2025-01-30  
**Objectif** : Document de travail unique regroupant la fiche société, l’analyse concurrence / PESTEL / SWOT / Porter et le rapport SEO pour la prospection et la proposition de valeur (Growth Engineer, SEO, funnel).

---

## Synthèse

ACKURACY est une société de **cybersécurité offensive** (pentest, red team) qui simule des attaques réelles pour aider les entreprises à renforcer leurs défenses. Positionnement international (New York), slogan « Where protection meets precision ». Ce rapport compile : (1) la fiche société et produits, (2) l’analyse stratégique (PESTEL, SWOT, Porter) et concurrence, (3) le **rapport SEO** (diagnostic technique Screaming Frog, opportunités, estimation d’impact et priorisation). Il sert de base pour les propositions (landing, lead magnet, angle Growth Engineer).

---

## 1. Société, produits et concurrence

*Détail complet dans* : [`etude-concurrentielle-pestel-swot-porter.md`](./etude-concurrentielle-pestel-swot-porter.md)

### 1.1 La société

- **Bureau** : 90 Washington St #17m, New York, NY 10006, USA  
- **Contact commercial** : Alexis Clavier (Sales Representative) — alexis@ackuracy.com | +33 6 15 66 56 67  
- **Événement source** : Cyber Show Paris  
- **Segment** : Cyber / Red Team  

### 1.2 Produits et technologie

- **Offres** : Penetration testing (web, internal, external), Red team services, Crisis management, Infrastructure audit, Threat Intelligence, GRC, Training & awareness, Strategic Advisory.  
- **Niveaux** : Level One (Essential), Level Two (Advanced), Level Three (Custom), Level Ultimate (Red Team).  
- **Secteurs** : Insurance, Transportation, Telecommunications, IoT, Finance media, Market research.

### 1.3 Concurrence (vue d’ensemble)

- **Grands cabinets** : Orange Cyberdefense, Thales.  
- **Pure-players** : Synacktiv, Vaadata, I-Tracing, SYSDREAM (Hub One).  
- **Plateformes** : Bug bounty (HackerOne, Intigriti) ; outils de scan automatisés.  
- **Différenciation ACKURACY** : approche « boutique » offensive, offre graduée Essential → Red Team ; positionnement international.

---

## 2. Analyse stratégique (PESTEL, SWOT, Porter)

*Détail complet dans* : [`etude-concurrentielle-pestel-swot-porter.md`](./etude-concurrentielle-pestel-swot-porter.md)

### 2.1 PESTEL (résumé)

| Facteur | Impact pour ACKURACY |
|--------|----------------------|
| **Politique** | Tensions géopolitiques renforcent la demande en pentest et red team. |
| **Économique** | Budgets cyber en hausse ; coût assurance/fuite pousse à l’audit. |
| **Légal** | NIS 2, DORA, GDPR : obligations d’audit régulier ; marché en expansion. |

### 2.2 SWOT (résumé)

| **Forces** | **Faiblesses** |
|------------|----------------|
| Expertise offensive reconnue | Prospection probablement manuelle |
| Offre structurée par niveaux | Visibilité limitée vs grands cabinets |
| Site bilingue EN/FR | H1 manquants, 35 images sans alt (SEO) |

| **Opportunités** | **Menaces** |
|------------------|-------------|
| Industrialiser la détection de leads (NIS 2, RSSI) | Automatisation du pentest (IA, scans low-cost) |
| Automatiser nurturing et prospection | Rivalité avec cabinets certifiés ANSSI |

### 2.3 Porter (résumé)

- **Pouvoir des clients** : Fort (comparaison de devis).  
- **Rivalité** : Forte (Orange, Thales, Synacktiv, Vaadata, etc.).  
- **Substitution** : Moyenne (bug bounty, scans automatisés).

---

## 3. Rapport SEO — Étude initiale & estimation d’impact

**Périmètre** : SEO technique (crawl Screaming Frog).  
**Sources** : site ackuracy.com ; **9 exports CSV Screaming Frog** (voir [README.md](./README.md) de ce dossier). Aucun chiffre inventé.

### 3.0 Éléments obligatoires du rapport

| Élément | Contenu |
|---------|---------|
| **Nombre de problèmes identifiés** | **21 types de problèmes** (rapport aperçu problèmes). Principaux : 4 pages sans version canonique ; 2 pages sans H1 (/terms, /privacy) ; 2 pages avec H1 multiple (/, /fr) ; 35 images sans attribut alt ; meta description trop longue (1 page) ; titles dupliqués (2 pages) ; 4 pages sans en-têtes Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Referrer-Policy ; liens `target="_blank"` sans `rel="noopener"` (4 pages). |
| **Impact** | Perte de crawl budget, dilution du PageRank (canoniques manquantes), mauvaise structuration des pages (H1 manquants/multiples), moindre accessibilité (alt manquants), risque sécurité (en-têtes manquants). |
| **Échantillon de 5 prospects** | **À renseigner** lors de la prospection (cibles, leads, entreprises pertinentes). Pour ce rapport initial : pas de données disponibles. |

---

### 3.1 Synthèse exécutive SEO

L’analyse SEO technique met en évidence un **potentiel de visibilité organique** partiellement limité par des problèmes structurels.

**Points positifs** :
- **100 % des pages** ont un temps de réponse en 0–1 seconde (excellent).
- Toutes les pages sont **indexables** (code 200, pas de meta robots bloquant).
- Site bilingue EN/FR avec contenu différencié.

**Points à corriger** :
- Absence de **versions canoniques** sur les 4 pages → risque de duplication et dilution du PageRank.
- Pages **/terms** et **/privacy** sans H1 → signal de structure faible.
- Pages **/** et **/fr** avec **plusieurs H1** → confusion pour les moteurs.
- **35 images** sans attribut alt → accessibilité et SEO image dégradés.
- **En-têtes de sécurité** manquants (CSP, X-Frame-Options, etc.) → moindre résilience face aux attaques XSS et clickjacking.

Une correction progressive permettrait une meilleure indexation, une structuration claire et une base solide pour le trafic organique qualifié.

---

### 3.2 Diagnostic SEO technique (données CSV Screaming Frog)

#### 3.2.1 Périmètre du crawl

| Métrique | Valeur | Source |
|----------|--------|--------|
| URLs crawlées | 4 | CSV rapport_interne_tous |
| Pages indexables | 4 | CSV indexabilité |
| Temps de réponse 0–1 s | 100 % | CSV temps_de_réponse |

**Pages** : https://www.ackuracy.com/ (homepage), /terms, /fr, /privacy.

#### 3.2.2 Problèmes identifiés (extrait rapport aperçu problèmes)

| Priorité | Problème | Nb URL | Impact |
|----------|----------|--------|--------|
| Moyenne | Versions canoniques manquantes | 4 | Imprévisibilité du classement, dilution PageRank |
| Moyenne | H1 manquant | 2 (/terms, /privacy) | Signal de structure faible, difficulté à classer |
| Moyenne | H1 multiple | 2 (/, /fr) | Confusion structure document |
| Moyenne | Title doublon | 2 | Difficile de distinguer les pages |
| Moyenne | Meta description manquante | 2 | Opportunité CTR perdue |
| Faible | 35 images sans texte alt | 35 | Accessibilité, SEO image |
| Faible | En-têtes sécurité manquants | 4 | XSS, clickjacking |
| Faible | Liens target="_blank" sans rel="noopener" | 4 | Sécurité, performance (anciens navigateurs) |

#### 3.2.3 Estimation d’impact (ordre de grandeur)

- **Canoniques** : correction prioritaire → évite la dilution du PageRank et améliore la cohérence d’indexation.  
- **H1** : correction prioritaire → renforce le signal de pertinence pour les requêtes cibles.  
- **Images alt** : correction progressive → améliore l’accessibilité et le potentiel SEO image.  
- **En-têtes sécurité** : recommandé → améliore la confiance et la résilience du site.

---

### 3.3 Priorisation recommandée

| Priorité | Action | Effort estimé |
|----------|--------|---------------|
| 1 | Ajouter balises canoniques sur les 4 pages | Faible |
| 2 | Corriger H1 : un seul par page ; ajouter H1 sur /terms et /privacy | Moyen |
| 3 | Rendre les titles uniques et descriptifs | Faible |
| 4 | Ajouter meta descriptions sur les 2 pages sans | Faible |
| 5 | Ajouter attributs alt sur les 35 images | Moyen |
| 6 | Configurer en-têtes sécurité (CSP, X-Frame-Options, etc.) | Moyen (DevOps) |
| 7 | Ajouter rel="noopener" sur liens target="_blank" | Faible |

---

## 4. Verdict pour le projet LPPP (prospection)

ACKURACY est une **cible pertinente** pour un profil « Growth Engineer » :

- **Problème commercial** : Alexis (Sales) a besoin de leads RSSI qualifiés ; la prospection manuelle sur LinkedIn est chronophage.  
- **Angle possible** : proposer un **pipeline de détection d’opportunités** (OSINT, enrichissement, gouvernance RACI) pour alimenter le CRM avec des leads qualifiés.  
- **Positionnement** : « Je ne vous vends pas du code, je vous vends une machine à détecter les signaux d’achat (recrutement RSSI, NIS 2, changements d’infra). »  
- **Rapport SEO** : le diagnostic technique peut servir de **lead magnet** pour ouvrir la conversation (rapport teaser, synthèse exécutive).

---

## Références

- **Étude détaillée** : [`etude-concurrentielle-pestel-swot-porter.md`](./etude-concurrentielle-pestel-swot-porter.md)
- **Fiche contact** : [`fiche-contact.json`](./fiche-contact.json)
- **Site ACKURACY** : https://www.ackuracy.com/
- **Rapports SEO** : CSV Screaming Frog (voir `README.md` pour la liste des fichiers)
- **Organisation contacts** : `docs/base-de-connaissances/organisation-donnees-contacts.md`
