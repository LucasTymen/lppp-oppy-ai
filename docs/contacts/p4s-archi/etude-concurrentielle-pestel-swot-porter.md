# P4S Architecture — Société, produits et étude concurrence

**Contact** : P4S-archi (p4s-archi.com)  
**Date** : 2025-01-30  
**Sources** : site p4s-archi.com (pages Produits, Technologie, À propos, Contact), analyse marché cybersécurité industrielle.

---

## 1. La société

**P4S** (P4S Architecture) est une **startup française** spécialisée dans la cybersécurité des réseaux (IT et OT — Opérationnel Industriel). Elle propose une approche **"hardware-centric"** : la technologie **SOFTLESS** remplace les couches logicielles traditionnelles par de la logique câblée sur composants **FPGA**.

### Faits clés (sources site)

- **Siège** : 5 Rue Bellini, 92800 Puteaux, France  
- **Contact** : contact@p4s-archi.com | +33 1 84 20 10 44  
- **Forme juridique** : SAS immatriculée à Évry  
- **Capital** : 100 % français, détenu à plus de 80 % par les fondateurs  
- **R&D et fabrication** : 100 % Made in France (ISEP, EPITA, ENSTA, PMI française)

### Direction (source site « À propos »)

| Nom | Rôle | Contexte |
|-----|------|----------|
| Joël Courtois | CEO | Docteur en IA, ancien DG EPITA |
| Christian Garnier | General Manager | Chercheur et ingénieur |
| Bruno Monsuez | Scientific expert | Ancien directeur de département ENSTA Paris |
| Maxime Apollonio | CTO | Conception et mise en œuvre de réseaux sécurisés |
| Yves Dufayet | Business Manager | Ingénieur et HEC Executive |

---

## 2. Produits et technologie

### Technologie SOFTLESS

- **Principe** : normes Ethernet, processus de cybersécurité et algorithmes en **VHDL** (logique câblée) → implémentation sur **FPGA** → mise en œuvre sur carte électronique.
- **Résultat** : aucun logiciel, aucun OS ; sécurité « secure by design » et « secure by default » (process issu de l’aéronautique).
- **Origine** : plus de 10 ans de recherche.

### Gamme SF-106

| Produit | Description | Spécificités |
|---------|-------------|--------------|
| **SF-106-2 (CipherWall)** | Chiffreur / firewall hautes performances | Protection DoS/DDoS, suppression paquets corrompus, latence &lt; 3 µs, chiffrement AES-256 GCM 16, débit &gt; 18 Gbps |
| **SF-106-8** | Contrôleur réseau cyber 10/100/1000 | 1 pare-feu indépendant par port, latence extrême, versatility |

### Avantages techniques (site)

- Chiffrement **1000× plus rapide** que les solutions logicielles (&lt; 3 µs vs millisecondes)
- **100 % de la bande passante** utilisable (full duplex, par port)
- **Aucune modification** de l’infrastructure existante
- Sobriété énergétique (&lt; 1 W pour SF-106-2, &lt; 10 W pour SF-106-8)
- Paramétrage via réseau ou USB-C (P4S-Console)
- Certification CSPN (ANSSI) en cours

### Secteurs ciblés

- Industrie  
- Médical  
- Gouvernement (grandes administrations)

---

## 3. Analyse PESTEL (macro-environnement)

| Facteur | Impact pour P4S |
|---------|-----------------|
| **Politique** | Soutien français pour la souveraineté numérique et le Made in France. Tensions géopolitiques qui renforcent la demande de protection des infrastructures critiques. |
| **Économique** | Coût élevé de la R&D FPGA, mais marché de la cybersécurité industrielle en forte croissance mondiale. |
| **Social** | Prise de conscience des risques (ransomwares, paralysie). Besoin de solutions simples sans modifier l’existant. |
| **Technologique** | Rupture : passage du logiciel au matériel pur (FPGA) pour limiter les vulnérabilités exploitables à distance. |
| **Environnemental** | Efficacité énergétique des FPGA vs serveurs logiciels, alignée avec la décarbonation. |
| **Légal** | Directives européennes (NIS 2, OSE) imposant des standards de sécurité renforcés aux opérateurs critiques. |

---

## 4. Matrice SWOT

| **Forces (Strengths)** | **Faiblesses (Weaknesses)** |
|------------------------|-----------------------------|
| Technologie SOFTLESS unique et disruptive (aucune faille logicielle exploitable à distance) | Jeunesse de l’entreprise (startup) |
| Latence ultra-faible (&lt; 3 µs) adaptée à l’industrie | Cycle de vente long (industriel, étatique) |
| Équipe de direction reconnue (EPITA, ENSTA, HEC) | Notoriété à construire face aux acteurs établis |
| 100 % Made in France (souveraineté) | Certification CSPN en cours (pas encore obtenue) |
| Faible consommation énergétique | |

| **Opportunités (Opportunities)** | **Menaces (Threats)** |
|----------------------------------|------------------------|
| Partenariats avec intégrateurs d’infrastructures critiques (Énergie, Eau, Transport) | Concurrence de solutions logicielles moins chères |
| Expansion internationale via le label de confiance français | Évolution des standards post-quantique |
| Convergence IT/OT nécessitant des ponts sécurisés matériels | Pénurie mondiale de composants (FPGA) |
| NIS 2 et réglementations poussant à la sécurisation | Rivalité avec des acteurs certifiés ANSSI de longue date |

---

## 5. Les 5 Forces de Porter

| Force | Intensité | Commentaire |
|-------|-----------|-------------|
| **Menace des nouveaux entrants** | Faible | Barrière technologique élevée (VHDL/FPGA, 10 ans de R&D). |
| **Pouvoir des fournisseurs** | Moyen | Dépendance aux fabricants de FPGA (Xilinx/Intel), mais la valeur est dans la logique propriétaire. |
| **Pouvoir des clients** | Faible à moyen | Pour les industries critiques, le coût d’une cyberattaque rend l’investissement P4S pertinent. |
| **Menace des produits de substitution** | Moyenne | Firewalls logiciels (Stormshield, etc.) omniprésents, mais ne rivalisent pas en latence ni en immunité logicielle. |
| **Rivalité entre concurrents** | Forte | Présence de Thales, Stormshield et autres pure-players déjà certifiés ANSSI. |

---

## 6. Concurrence — vue d’ensemble

### Grands acteurs institutionnels

- **Thales** : solutions de chiffrement et protection pour secteurs sensibles.

### Spécialistes français cyber-souveraineté

- **Stormshield** : firewalls et protection réseau, certifications ANSSI historiques.  
- **Wallix** : Wallix Bastion, gestion des accès (industriel, gouvernemental).  
- **Tehtris** : détection et réponse (XDR), plus orienté logiciel.

### Géants internationaux

- **Palo Alto Networks**, **CrowdStrike** : solutions majoritairement logicielles et américaines. P4S se positionne comme alternative hardware et souveraine.

### Positionnement P4S vs concurrence

- **Différenciation** : approche 100 % matérielle (SOFTLESS), latence &lt; 3 µs, 100 % bande passante, consommation &lt; 1–10 W.
- **Angle** : « Je protège et j’oublie » — déploiement en quelques heures, sans modification de l’existant.

---

## 7. Verdict pour le projet LPPP (prospection)

P4S est une **cible pertinente** pour un profil « Growth Engineer » ou positionnement similaire :

- Produit technique de pointe (hardware, FPGA, VHDL) adressant des secteurs où la fiabilité est primordiale.
- Besoin de **visibilité et d’évangélisation** : leur défi est moins la technologie que l’acquisition et l’évangélisation.
- **Angle possible** : montrer comment organiser des pipelines de données sécurisés autour de leur stack matérielle, ou automatiser une campagne de sensibilisation ciblée (incidents cybersécurité industrielle récents → directeurs techniques d’entreprises sinistrées).

---

## Références

- **Site P4S** : https://www.p4s-archi.com/ (Produits, Technologie, À propos)
- **Cadre Growth Analyst** : `docs/base-de-connaissances/growth-analyst-concurrentiel-marche-ads.md`
- **Organisation contacts** : `docs/base-de-connaissances/organisation-donnees-contacts.md`
