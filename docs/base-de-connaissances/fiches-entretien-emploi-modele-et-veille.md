# Fiches Entretien Emploi — Modèle canonique, veille et coordination

**Rôle** : Référence pour l’**Assistant Entretien Emploi** et les agents avec lesquels il coordonne.  
**Objectif** : Appliquer toujours le même modèle de fiche, tenir à jour les onglets (rappels, fiches mémoire, questions techniques), coordonner avec Chef de Projet, Architecte, DevOps, Pentester et Rédacteur (agent RH), et éviter tout résidu d’une ancienne société lors d’un changement de cible, et **tenir un rôle conseiller** : repérer les infos importantes manquantes (risque d'être interrogé dessus), demander à l'utilisateur de les fournir ; si indisponibles, décider avec lui de la stratégie à adopter.

---

## 1. Modèle canonique (structure à conserver)

- **Fichier de référence** (dans le projet) : `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html`
- **Origine** : modèle fourni par l’utilisateur (ex. `2511_pitch_Clever-Age_prepa_entretien(1).html`). Ce fichier est la **référence unique** à réutiliser pour chaque nouvelle préparation d’entretien.

### Structure obligatoire

- **HTML5** : `lang="fr"`, titre `Préparation Entretien - [NomEntreprise] - Lucas Tymen`
- **Head** : jQuery (CDN 3.6.0), styles inline ou dans `<style>` :
  - `body` : dégradé violet/bleu (`#667eea` → `#764ba2`), `min-height: 100vh`
  - `.container` : fond blanc, ombre, `max-width: 1400px`
  - **info-box** : rappel rapide (disponibilité, prétentions, localisation, télétravail, type de contrat)
  - **Accordéons** : `.accordion` (sections principales), `.sub-accordion` (sous-sections), `.panel` / `.sub-panel` (contenu)
  - **Encadrés** : `.highlight`, `.success`, `.warning`, `.info`, `.tip`
  - `code`, `ul`, `strong`, `a` : styles cohérents
- **Script** (en fin de body) : jQuery pour `.accordion` / `.sub-accordion` → `slideToggle()` sur `.panel` / `.sub-panel` ; `scroll-behavior: smooth`

### Sections type (à adapter au poste et à l’entreprise)

- **0. VOTRE PRÉSENTATION** : pitch, triple profil, coordonnées
- **1. FORMALITÉS ADMINISTRATIVES** : disponibilité, prétentions, géographie, type de contrat
- **2. Q/R STRATÉGIQUES** (questions techniques spécifiques entreprise / poste)
- **3. TESTS TECHNIQUES — Programmation & Growth** : **obligatoire** — par techno (Python, Django, Java, Spring, Angular, concepts généraux), Growth, Marketing, KPI, frameworks, mix dev/growth (l'entretien peut être orienté pure dev, pure marketing ou mix ; ne jamais omettre). Voir `erreurs-et-solutions.md` § « Fiche entretien — section Tests techniques oubliée ».
- **4. QUESTIONS À POSER** : poste, montée en compétences, télétravail, évolution, synergies
- **5. [NOM ENTREPRISE] – Ce que vous devez savoir** : valeurs, clients, chiffres, implantations, KPI, stratégie commerciale, stacks, évolution carrière, formation, déontologie

**Règle** : générer **d'emblée** la fiche complète avec **toutes** les sections ci-dessus, **tous** les textes, lexique, abréviations et questions utiles. Le contenu de chaque section est **remplacé** pour la société ciblée ; la structure (titres, accordéons, classes CSS) reste celle du modèle.

---

## 2. Veille actualisée — Coordination par onglet

Les **rappels**, **fiches mémoire** et **questions techniques / technologiques** doivent rester à jour. L’Assistant Entretien Emploi s’appuie sur les agents suivants pour maintenir une veille cohérente.

| Onglet / thème | Agent(s) à solliciter | Rôle |
|----------------|------------------------|------|
| **Rappels** (info-box, formalités, disponibilité, prétentions, contrat) | **Chef de Projet** | Aligner avec la stratégie candidature, décisions projet, priorités (CDI / alternance / freelance). |
| **Fiches mémoire** (structure des sections, rubriques type JD2M, organisation des dossiers) | **Chef de Projet**, **Architecte** (structure, infos déjà en base) | Fiches mémoire = structure et bonnes pratiques ; Architecte pour cohérence avec la base de connaissances. |
| **Questions techniques et technologiques** (programmation, tests techniques, stacks, sécu) | **Pentester**, **DevOps** | **Pentester** : veille sur questions de tests techniques, sécurité, bonnes pratiques (anti-hallucination, fiche data). **DevOps** : stacks, CI/CD, infra, conventions techniques. |
| **Questions relationnelles, orientation poste, conventions collectives** | **Rédacteur** (rôle « agent RH ») | Positionnement, discours selon poste/secteur, questions à poser en entretien RH, conventions qui s’appliquent. Voir `agents-roles-responsabilites.md` § Rédacteur. |

- **Chef de Projet** : rappels et fiches mémoire ; validation que les fiches restent alignées avec la stratégie.
- **Architecte** (structure, infos en base) : cohérence des rubriques et des infos déjà documentées.
- **DevOps** : technos, outils, conventions (CI/CD, déploiement, stacks).
- **Pentester** : questions techniques / tests techniques / sécurité ; pas d’invention, s’appuyer sur le dépôt et la doc.
- **Rédacteur (agent RH)** : relations humaines, questions à poser, orientation selon le poste et les conventions.

Références : `registre-agents-ressources.md`, `agents-roles-responsabilites.md`, règles `.cursor/rules/` (devops.mdc, pentester.mdc, editorial.mdc).

---

## 3. Checklist « Nouvelle société » — Éviter fantômes et hallucinations

Lors de la **création ou mise à jour d’une fiche pour une nouvelle société cible** :

1. **Partir du modèle canonique** : copier `_modele-canonique_prepa_entretien.html` (ou la structure équivalente), pas d’une fiche d’une autre entreprise.
2. **Remplacer tout le contenu spécifique** :
   - Titre de page et H1 : nom de la **nouvelle** entreprise.
   - Info-box : rappels **génériques** ou mis à jour (pas de nom d’ancienne société).
   - Section « Ce que vous devez savoir » : **uniquement** données de la société ciblée (valeurs, clients, chiffres, implantations, stacks, etc.).
   - Questions à poser : formulées pour la **nouvelle** entreprise, pas reprise de listes « Clever Age » ou autre.
3. **Recherche globale** dans la fiche : vérifier qu’il ne reste **aucune occurrence** du nom de l’ancienne société, d’anciens clients, d’anciennes adresses ou d’anciennes références.
4. **Pitch / présentation** : adapter les phrases d’accroche et « pourquoi cette entreprise » à la **nouvelle** cible ; supprimer toute mention de l’ancienne.
5. **Résumé et ressources** : dans le dossier entreprise, le `resume-points-cles` et les ressources doivent concerner **uniquement** la société cible.

Si une fiche est créée à partir d’une ancienne fiche (ex. copier une fiche existante puis modifier) : effectuer la checklist ci-dessus **systématiquement** avant de sauvegarder.

---

## 4. Rôle conseiller (informations manquantes)

L'Assistant Entretien Emploi tient un **rôle de conseiller** en plus de la création/mise à jour des fiches :

- **Repérer** les informations importantes **manquantes** (données entreprise, formalités, points techniques, questions probables) sur lesquelles l'utilisateur pourrait être interrogé en entretien.
- **Demander** à l'utilisateur les informations à intégrer (documents, précisions, chiffres, conventions) pour compléter la fiche.
- **Si l'information n'est pas disponible** : ne pas inventer ; **proposer à l'utilisateur de décider ensemble de la stratégie à adopter** (ex. mentionner le manque dans la fiche, préparer une réponse de repli, reporter la recherche). L'utilisateur valide la stratégie.

Cette posture est intégrée à la règle `assistant-entretien-emploi.mdc` et au registre (coordination Orchestrateur).

---

## 5. Enrichissement structure (vue orientée entreprise)

Une **structure complémentaire**, orientée « accroche entreprise » et très alignée avec le discours des sociétés, peut être intégrée dans nos fiches. On conserve **notre** modèle (HTML, accordéons, info-box, ordre général) et on **enrichit** les sections avec les rubriques ci-dessous. À utiliser selon le poste (surtout pertinent pour rôles Growth / business / produit).

### Correspondance avec notre plan

| Notre section | Enrichissement (vue entreprise) | Sous-accordéons suggérés |
|---------------|----------------------------------|---------------------------|
| **0. VOTRE PRÉSENTATION** | Ajouter **Pourquoi moi ? (pitch personnel)** et **Synthèse des compétences** | Pitch d'ouverture, Triple profil, **Pourquoi moi ?** (double compétence, posture « système de croissance durable »), **Synthèse compétences** (Hard Skills, Soft Skills), Coordonnées |
| **1. FORMALITÉS** | Inchangé | Disponibilité, Prétentions, Géographie, Type de contrat |
| **2. PROGRAMMATION / TECHNIQUE** | Ajouter **Questions / Réponses stratégiques** (Technique + Mindset) | Par techno (Python, Django, Java, Spring, Angular…), **Q/R Stratégiques** : Section Technique (outils, data, optimisation), Section Mindset (vision métier, gestion de l'échec, priorisation) |
| **3. QUESTIONS À POSER** | Inchangé, peut croiser « Q/R stratégiques » | Poste, Montée en compétences, Télétravail, Évolution, Synerges |
| **4. [ENTREPRISE] – Ce que vous devez savoir** | **Structurer en « accroche entreprise »** | **I. Présentation de l'entreprise (L'accroche)** : Identité, Produit, Mission, Valeur ajoutée • **II. Leurs missions (vision métier)** : Simplification, Digitalisation, Scalabilité • **III. Marché et opportunités** : Facteur Économique, Technologique, Légal • **IV. Concurrence** : Concurrents directs, indirects, Différenciateur • Valeurs, Chiffres, Implantations, Stacks, Évolution carrière, Formation, Déontologie |

### Rubriques à ajouter (contenu à adapter par entreprise)

- **Mes missions (plan d'action Growth)** — à placer en **section 0** (après « Pourquoi moi ? ») ou en **section 3** selon le poste : Acquisition (Paid, SEO, Content), Data & Tracking (KPI, performance), Expérimentation (A/B testing, conversions).
- **KPI et métriques clés** — à placer en **section 2** (déjà des formules KPI) ou en **section 4** (KPI de l'entreprise) : Acquisition (CPL, CAC), Engagement (taux d'activation), Rétention (fidélité, LTV).

### Règle

- **Garder notre squelette** : info-box, ordre 0 → 1 → 2 → 3 → 4, styles, script.
- **Enrichir** avec les sous-parties ci-dessus quand c’est pertinent pour la société et le poste (sans tout dupliquer si la fiche devient illisible).
- **Anti-hallucination** : remplir uniquement à partir des ressources fournies ou récupérées ; pas d’invention sur l’entreprise.

---

## 6. Types de fiches par famille de poste

En plus de la structure canonique (0 → 5), **adapter les sections et le contenu** selon le type de poste. Deux familles supplémentaires à intégrer quand c’est le cas.

### 6.1 Infogérant informatique (niveau 1 & niveau 2)

Pour un poste **infogérant / support informatique N1 et N2** :

- **Conserver** : info-box, sections 0 (présentation), 1 (formalités), 4 (questions à poser), 5 (entreprise).
- **Section 2** : remplacer / compléter par **Q/R et savoir-faire Infogérant** :
  - **Niveau 1** : prise en charge des demandes (ticketing, première ligne), résolution courante (mot de passe, accès, imprimante, poste), escalade au N2, outils (GLPI, Zendesk, RDS, etc.), procédures et délais SLA.
  - **Niveau 2** : diagnostic avancé, administration (Active Directory, GPO, DNS, DHCP), supervision, déploiement (patches, images), participation à la roadmap infra.
- **Section 3** : **Tests techniques / questions techniques** adaptées : différences N1 vs N2, exemples de tickets, gestion des priorités, relation avec les utilisateurs et les équipes internes, bonnes pratiques (documentation, traçabilité, communication).
- **Lexique** : SLA, ticket, escalade, N1/N2/N3, RDS, AD, GPO, hotline, infogérance, supervision, PRA/PCA.

### 6.2 Consultant SEO

Pour un poste **consultant SEO**, ajouter **obligatoirement** les blocs suivants (en section 2 ou en sous-accordéons dédiés). Ne pas oublier le **rappel des règles de base** et l’**avenir du SEO**.

- **Rappel — SEO technique (règles de base)**  
  Crawlabilité et indexation (robots.txt, sitemap, balisage HTML sémantique, H1 unique, meta title/description), Core Web Vitals (LCP, FID/INP, CLS), structure des URLs, canonical, hreflang, gestion des erreurs (4xx, 5xx), maillage interne, HTTPS, mobile-first. Outils : Search Console, Screaming Frog, Lighthouse.

- **Rappel — SEO sémantique (règles de base)**  
  Intention de recherche (informatif, transactionnel, navigationnel), sujets et entités (topics, clusters), densité et pertinence du contenu, champs sémantiques et synonymes, E-E-A (Experience, Expertise, Authoritativeness), structuration (schémas, FAQ, HowTo). Différence avec le keyword stuffing ; alignement contenu / requêtes / pages.

- **Avenir du SEO — adaptation aux robots et évolution**  
  - **Adapter au robot** : crawlers et indexation (Googlebot, Bingbot), rendu JavaScript, directives et balisage pour les snippets (featured snippets, PAA), signaux E-E-A et YMYL ; pénalités et bonnes pratiques face aux mises à jour (algorithme, spam).  
  - **Avenir du SEO** : recherche vocale, SGE / Search Generative Experience, intégration IA dans les SERP, zero-click, rôle du contenu « expert » et de la marque ; tendances (sémantique, entités, passage du keyword au topic).  

L’Assistant Entretien Emploi doit **toujours inclure** ces trois blocs (SEO technique, SEO sémantique, avenir du SEO) dans toute fiche « Consultant SEO ». S’appuyer sur `rapport-seo-prospect.md`, `seo-semantique-outils-open-source.md` et la base de connaissances pour rester aligné avec le projet (sans inventer).

### 6.3 Pentesting et cybersécurité (notions de base à avancées)

Pour un poste ou un **onglet dédié pentesting / cybersécurité**, inclure les blocs suivants (section 2 ou 3, ou onglet accordéon dédié).

- **Notions de base** : objectifs du pentest (identification des vulnérabilités, rapport d’exploitation, recommandations), différences Red Team / Blue Team / Purple Team, périmètre et autorisation (scope, lettre de mission), méthodologies (OWASP, PTES, NIST), phases (reconnaissance, scanning, exploitation, post-exploitation, reporting).
- **Notions un peu avancées** : vecteurs d’attaque courants (injection, XSS, CSRF, élévation de privilèges), exploitation de services (credentials, services exposés), social engineering, bonnes pratiques de rédaction de rapport (criticité, preuves, reproductibilité).
- **Préceptes cybersécurité** : défense en profondeur, principe du moindre privilège, segmentation, durcissement (hardening), gestion des secrets et des accès, conformité (RGPD, ISO 27001, ANSSI), cycle de vie des vulnérabilités (découverte → correction → vérification).
- **Modes d’action recommandés** : cadrage (scope, règles d’engagement), tests non destructifs en priorité, traçabilité des actions, communication avec le commanditaire, livrables (rapport exécutif, technique, plan de remédiation).
- **Guides en cas d’attaque** : détection et confinement (isoler les systèmes compromis, préserver les preuves), analyse post-incident (forensic, logs), communication de crise, déclaration (CNIL, ANSSI si applicable), retour d’expérience et amélioration des contrôles.

**Lexique** : CVE, CWE, CVSS, OWASP Top 10, PTES, NIST CSF, Red/Blue/Purple Team, scope, PoC, rapport d’exploitation, remédiation.

### 6.4 IoT (Internet of Things)

Pour un poste ou un **onglet touchant à l’IoT**, inclure :

- **Notions de base** : définition (objets connectés, capteurs, actuateurs, passerelles), architectures (capteur → passerelle → cloud, edge), protocoles courants (MQTT, CoAP, HTTP/HTTPS, LoRa, Zigbee, BLE), enjeux (latence, bande passante, énergie, sécurité).
- **Sécurité IoT** : surfaces d’attaque (firmware, interfaces web/API, radio), bonnes pratiques (mise à jour, authentification, chiffrement, durcissement par défaut), standards et cadres (ETSI EN 303 645, NIST IoT, OWASP IoT Top 10).
- **Cas d’usage et tendances** : industrie (IIoT, supervision), bâtiment (smart building), santé (objets médicaux), domotique ; convergence IT/OT, gestion des vulnérabilités et des mises à jour à grande échelle.

**Lexique** : MQTT, CoAP, edge, firmware, OTA (Over-The-Air), IIoT, OT.

---

## 7. Références

- **Espace fiches** : `docs/ressources-utilisateur/fiches-entretien-emploi/` (README, un dossier par entreprise).
- **Modèle canonique** : `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html`
- **Types de poste** : § 6 — **Infogérant N1/N2**, **Consultant SEO** (rappel SEO technique, sémantique, avenir du SEO), **Pentesting / Cybersécurité** (notions base à avancées, préceptes, modes d’action, guides en cas d’attaque), **IoT** (notions, sécurité, cas d’usage). À inclure selon le poste ciblé.
- **Règle Assistant** : `.cursor/rules/assistant-entretien-emploi.mdc`
- **Registre** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Rôles (Rédacteur = agent RH)** : `docs/base-de-connaissances/agents-roles-responsabilites.md` § Rédacteur, § Assistant Entretien Emploi.
- **SEO (contenu)** : `rapport-seo-prospect.md`, `seo-semantique-outils-open-source.md` pour rester aligné avec le projet.
