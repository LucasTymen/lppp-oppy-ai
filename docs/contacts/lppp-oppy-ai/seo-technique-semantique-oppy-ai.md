# SEO technique & sémantique — OPPORTUNITY (Oppy.ai)

Document de travail LPPP pour la suite du livrable après la partie **marketing / stratégie**.  
**À compléter avec des mesures réelles** : crawl (Screaming Frog, Sitebulb, etc.), Google Search Console, PageSpeed / CrUX, logs serveur si accès.

---

## 1. Périmètre

| Élément | Note |
|--------|------|
| **Cible** | Site public **oppy.ai** (et éventuellement sous-domaines / micro-sites à lister après inventaire). |
| **Objectif** | Visibilité organique B2B (décideurs IT, marketing, relation client, digital) + **cohérence sémantique** avec le positionnement CIM / IA conversationnelle / grands comptes. |
| **Non-objectif** | Ne pas confondre ce document avec le **dashboard stratégique** (funnel, maturité stack) : le JSON `audit-dashboard.json` actuel reste orienté étude GAM ; un **second fichier** ou une évolution pourrait accueillir les métriques SEO terrain plus tard. |

---

## 2. SEO technique — grille de contrôle

Cocher / compléter après audit. *Aucun chiffre inventé ici.*

### 2.1 Crawl & indexation

- [ ] **Robots.txt** : autorisation crawl, pas de blocage involontaire des pages stratégiques.
- [ ] **Sitemap XML** : à jour, URLs canoniques, priorité / fréquence cohérentes.
- [ ] **Indexation** : couverture GSC (erreurs, exclusions, soft 404).
- [ ] **Canoniques** : auto-références, pas de doubles indexations (www / non-www, trailing slash, paramètres).
- [ ] **Pagination / facettes** (si e-commerce ou listing) : rel next/prev ou noindex ciblé selon stratégie.
- [ ] **Hreflang** (si multilingue réel) : réciprocité et codes ISO corrects.

### 2.2 Rendu & contenu machine

- [ ] **JavaScript** : contenu critique visible pour Google (test inspection d’URL, comparaison HTML brut vs rendu).
- [ ] **Status HTTP** : 4xx/5xx sur pages importantes, chaînes de redirections.
- [ ] **Maillage interne** : profondeur clics, pages orphelines, ancres variées (éviter sur-optimisation exact match).

### 2.3 On-page

- [ ] **Balises title** : uniques, intention + marque, longueur raisonnable.
- [ ] **Meta description** : incitation au clic, alignée sur l’intention (pas bourrage de mots-clés).
- [ ] **Hiérarchie H1–Hn** : un H1 par URL (règle courante), enchaînement logique.
- [ ] **Images** : attributs `alt` pertinents, formats modernes (WebP/AVIF si stack le permet), dimensions explicites si utile au CLS.

### 2.4 Données structurées

- [ ] **Organization** / **WebSite** (logo, sameAs réseaux).
- [ ] **SoftwareApplication** ou **Product** si pages produit SaaS adaptées.
- [ ] **FAQ** uniquement si contenu réellement en FAQ (éviter le spam de schema).
- [ ] Validation **Rich Results Test** / Schema.org.

### 2.5 Performance & CWV

- [ ] **LCP, INP, CLS** (field + lab) sur templates clés : home, page produit / solution, blog pilier.
- [ ] **TTFB** : distinguer réseau CDN vs origine.
- [ ] **Third-parties** : impact des tags (Analytics, chat, AB test).

### 2.6 Sécurité & confiance (SEO indirect)

- [ ] HTTPS partout, pas de mixed content.
- [ ] Headers de sécurité (CSP, X-Frame, etc.) — alignement avec équipe technique.

---

## 3. SEO sémantique — intentions & clusters

Aligné sur l’étude projet (CIM, grands comptes, canaux, conformité). **À valider par recherche de mots-clés** (GSC, Keyword Planner, outils tiers) et analyse SERP.

### 3.1 Piliers thématiques (exemples de clusters)

| Pilier | Sous-thèmes (à décliner en pages / hubs) |
|--------|----------------------------------------|
| **CIM / orchestration** | Parcours client, omnicanal, timing des messages, cas d’usage sectoriels. |
| **Canaux** | SMS professionnel, RCS, email transactionnel, WhatsApp Business (si dans l’offre), voicebot, vidéo personnalisée. |
| **IA conversationnelle** | Agents vocaux, NLU, personnalisation, automatisation sans déshumaniser. |
| **Conformité & confiance** | RGPD, délivrabilité, réputation expéditeur, Ecovadis / RSE (angle éditorial, pas sur-optimisation). |
| **Secteurs** | Banque, assurance, télécom, retail — **pages dédiées ou études de cas** si contenu disponible. |

### 3.2 Types d’intention

- **Informationnelle** : « qu’est-ce que le RCS », « CIM définition », comparatifs éducatifs.
- **Commerciale** : « solution SMS entreprise », « plateforme interaction client ».
- **Transactionnelle** : démo, contact, essai — **pages money** à prioriser en maillage et suivi conversions.

### 3.3 Cannibalisation

- Lister les URL qui se disputent la même intention ; plan de **consolidation** ou différenciation title/H1.

### 3.4 Contenu & E-E-A-T (B2B)

- Signaux d’expertise : auteurs identifiés, sources, mises à jour, études chiffrées lorsque publiable.
- Liens externes vers références sectorielles (régulateur, standards) si pertinent.

---

## 4. Livrables SEO suggérés (prochaines itérations)

1. **Rapport crawl** : export + synthèse (top erreurs, opportunités quick wins).
2. **Carte sémantique** : tableur ou mindmap (pilier → page cible → requêtes seed).
3. **Plan éditorial 90 j** : aligné sur la roadmap GAM (contenus qui nourrissent inbound + sales enablement).
4. **Fiche par template** : meta type, schema type, CTA, KPI (position, clics, impressions).

---

## 5. Lien avec les fichiers LPPP

| Fichier | Rôle |
|---------|------|
| `landing-proposition-lppp-oppy-ai.json` | Champ `seo_technique_semantique` : résumé affiché sur la landing. |
| `etude-oppy-ai-source.md` | Contexte business ; croiser avec les mots du marché pour la sémantique. |
| Futur `audit-seo-oppy-ai.json` (optionnel) | Si vous dupliquez le modèle Infopro pour des **chiffres PageSpeed / crawl** réels sur oppy.ai. |

*Dernière mise à jour : document préparé pour la phase SEO ; chiffres et cases à cocher à remplir après mesures.*
