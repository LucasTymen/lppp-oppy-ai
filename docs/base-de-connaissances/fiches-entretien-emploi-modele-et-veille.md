# Fiches Entretien Emploi — Modèle canonique, veille et coordination

**Rôle** : Référence pour l’**Assistant Entretien Emploi** et les agents avec lesquels il coordonne.  
**Objectif** : Appliquer toujours le même modèle de fiche, tenir à jour les onglets (rappels, fiches mémoire, questions techniques), coordonner avec Chef de Projet, Architecte, DevOps, Pentester et Rédacteur (agent RH), et éviter tout résidu d’une ancienne société lors d’un changement de cible, et **tenir un rôle conseiller** : repérer les infos importantes manquantes (risque d'être interrogé dessus), demander à l'utilisateur de les fournir ; si indisponibles, décider avec lui de la stratégie à adopter.

---

## 1. Modèle canonique (structure de référence)

- **Fichier de référence** (dans le projet) : `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html`
- **Origine** : modèle fourni par l’utilisateur (ex. fiche Clever Age). Ce fichier est la **structure de référence** à réutiliser pour chaque nouvelle préparation d’entretien.

### Règle centrale : même organisation, même structure, même nombre d’onglets — contenu dynamique

Le **modèle que l’utilisateur a donné** définit la **structure de référence**. Pour toute fiche (nouvelle société, nouveau poste) :

- **Structure = fixe** : on conserve **la même organisation**, **la même structure**, **le même nombre d’onglets** (sections principales et sous-accordéons) que dans le modèle de référence. Aucune section ni onglet ne doit être supprimé ou ajouté de façon incohérente — la grille des onglets reste identique.
- **Contenu = dynamique** : le **contenu** à l’intérieur de chaque onglet **change et s’adapte** (nom d’entreprise, pitch, formalités, questions à poser, bloc entreprise, données spécifiques à la boîte et au poste). Seul le texte (et les données) est remplacé ou adapté ; pas la structure ni le nombre d’onglets.

En résumé : **même organisation, même structure, même nombre d’onglets** que le modèle donné ; **contenu adapté** dynamiquement selon la boîte et le poste.

### Contenu à reprendre dans toute fiche (les cinq familles)

Toute fiche doit **reprendre** les éléments suivants. Ils correspondent aux onglets / sections du modèle de référence ; seul le détail du texte s’adapte (boîte, poste).

| Famille de contenu | Description | Où dans la fiche (exemples) |
|--------------------|-------------|-----------------------------|
| **1. Questions qu’on est censé me poser** | Les questions que le recruteur / l’entreprise peut me poser (techniques, métier, comportementales). | Section Programmation / Tests techniques (Q/R par techno), Q/R stratégiques, éventuellement bloc « questions courantes en entretien ». |
| **2. Les questions que je peux être amenée à poser** | Les questions que moi, candidat, je pose à l’entreprise (poste, projets, équipe, évolution). | Section « Questions à poser » (à l’entreprise). |
| **3. Pistes de réflexion via mon pitch personnel** | Mon pitch, mon positionnement, les angles de réflexion personnels — peut rester stable d’une fiche à l’autre ou s’adapter légèrement. | Section 0 (Présentation), pitch d’ouverture, triple profil, « pourquoi moi », stratégie d’entretien. |
| **4. Conditions d’embauche** | Disponibilité, prétentions, géographie, type de contrat, télétravail. | Info-box + Section 1 (Formalités administratives). |
| **5. Questions à poser relatives aux RH** | Questions spécifiquement RH à poser (package, formation, congés, télétravail, évolution, culture). | Section « Questions à poser » (sous-partie RH) ou Formalités selon le modèle. |

**Règle** : ces cinq familles sont **toujours présentes** dans la structure. On ne supprime aucun de ces blocs ; on **reprend** la même organisation (questions qu’on me pose, questions que je pose, pitch / pistes de réflexion, conditions d’embauche, questions RH) et on adapte le **contenu** (texte, noms, chiffres) selon la boîte et le poste. Le pitch personnel et les pistes de réflexion **ne changent pas forcément** d’une fiche à l’autre ; les conditions d’embauche et les questions à poser (dont RH) s’adaptent au contexte.

### Structure obligatoire

- **Sections à la racine** : les sections 0 à 6 (Présentation, Formalités, Programmation, Questions à poser, [Entreprise], Checklist, Lexique) sont des **blocs au même niveau** ; le panel de la section 2 doit être fermé avant la section 3. **Tous les accordéons fermés par défaut** (pas de `active` ni `display: block` sur les panels). Détail : `fiches-entretien-emploi-template-html.md`.
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
- **3. TESTS TECHNIQUES — Programmation & Growth** : **obligatoire**. Voir règle ci-dessous (§ Tests techniques : reprise et enrichissement).
- **4. QUESTIONS À POSER** : poste, montée en compétences, télétravail, évolution, synergies
- **5. [NOM ENTREPRISE] – Ce que vous devez savoir** : valeurs, clients, chiffres, implantations, KPI, stratégie commerciale, stacks, évolution carrière, formation, déontologie

**Règle** : générer **d'emblée** la fiche complète avec **toutes** les sections ci-dessus, **tous** les textes, lexique, abréviations et questions utiles. Le contenu **à adapter** (présentation, formalités, questions à poser, bloc entreprise, etc.) est **adapté** pour la société et le poste ciblés — **jamais supprimé sans l’adapter**. La section Tests techniques est **reprise telle quelle** (contenu existant du modèle) et **enrichie** avec les modules listés en § 6 ; la structure (titres, accordéons, classes CSS) reste celle du modèle.

#### Tests techniques : reprise et enrichissement

- **Contenu existant** : les blocs déjà présents dans le modèle canonique (Python, Django, Java, Spring, Angular, concepts généraux, Growth, Marketing, KPI, etc.) sont **repris tels quels** — on ne les supprime pas.
- **Enrichissement** : on **ajoute** les modules suivants, au **même format** que le modèle existant. Comme sur le modèle existant, ce sont des **fichiers de cours et de révisions** comprenant les **notions principales** de chacun de ces modules : chaque module = un sous-accordéon avec des Q/R ou notions (Définition, Exemple, Cas d’usage, etc.), comme pour Python ou Django.
- **Modules à ajouter** : **IoT** (§ 6.4), **CSS** (§ 6.7), **Cybersécurité** (§ 6.3), **Maintenance informatique N2** (§ 6.1), **DevOps** (§ 6.6 : Git, GitLab CI/CD, GitHub Actions, Docker, WordPress), **SQL** (§ 6.8), **PostgreSQL** (§ 6.9). Ruby/Rails (§ 6.5) optionnel selon besoin.
- **Excellence et variété** : ces modules sont inclus pour couvrir les questions possibles, même si le poste n’est pas directement lié. Voir `erreurs-et-solutions.md` § « Fiche entretien — section Tests techniques oubliée ».

### Fixe vs à adapter (par boîte et poste)

| Élément | Statut | Action |
|--------|--------|--------|
| **Structure (organisation, nombre d’onglets, sections)** | **Fixe** | **Identique au modèle donné** : même organisation, même structure, même nombre d’onglets (sections + sous-accordéons). Ne pas supprimer ni réorganiser les onglets. |
| **Structure HTML/CSS/JS** (accordéons, panels, classes, style) | **Fixe** | Toujours identique au modèle de référence ; ne pas modifier. |
| **Section Tests techniques (Programmation & Growth)** | **Fixe + enrichi** | **Repris tels quels** : Python, Django, Java, Spring, Angular, concepts, Growth, etc. (format cours/révisions, notions principales). **Enrichi** par ajout des modules § 6 (IoT, CSS, cybersécurité, Maintenance N2, DevOps, SQL, PostgreSQL) au **même format** (sous-accordéon, Q/R avec Définition, Exemple, Cas d’usage). Ne pas supprimer le contenu existant. |
| **Section 2 — Culture générale / concepts transverses** | **Fixe** | Conserver, actualiser si besoin. |
| **Info-box** (dispo, prétentions, lieu, télétravail, contrat) | **À adapter** | Ajuster selon stratégie candidature (Chef de Projet). |
| **Section 0 — Présentation** (pitch, triple profil, coordonnées) | **À adapter** | Pitch et « pourquoi cette entreprise » selon la **boîte** et le **poste**. |
| **Section 1 — Formalités** | **À adapter** | Détails selon offre et contexte (type de contrat, géo, etc.). |
| **Section 3 — Questions à poser** | **À adapter** | Formuler pour la **boîte** ciblée (nom, projets, équipe, etc.). |
| **Section 4 — [NOM ENTREPRISE]** | **À adapter** | Uniquement données de la **boîte** (valeurs, clients, chiffres, stacks, etc.). |
| **Section 5 — Checklist finale** | **À adapter** | Points spécifiques au poste / à l’entretien si besoin. |
| **Section 6 — Lexique** | **À adapter** | Compléter selon technos du **poste** / de la boîte. |

**En résumé** : tout le reste (présentation, formalités, questions à poser, fiche entreprise, checklist, lexique) est **à adapter selon la boîte et le poste**. Le template HTML est unique : `_modele-canonique_prepa_entretien.html`.

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

## 6. Types de fiches par famille de poste — Enrichissement de la section Tests techniques

**Règle importante** : le contenu existant des fiches (toutes les sections, dont la section Programmation / Tests techniques avec Python, Django, Java, Spring, Angular, etc.) n’est **jamais supprimé** : il est **adapté** (présentation, formalités, entreprise, questions à poser selon la boîte et le poste). La section **Tests techniques** est **reprise telle quelle** (même structure, mêmes Q/R par techno) et **enrichie** en **ajoutant** les modules ci-dessous.

Comme sur le **modèle existant** (`_modele-canonique_prepa_entretien.html`), les blocs techniques sont des **fichiers de cours et de révisions** comprenant les **notions principales** de chaque module : chaque module = sous-accordéon avec questions/réponses au format **Définition**, **Exemple**, **Cas d’usage** (ou équivalent), comme pour Python ou Django dans le modèle.

En plus de la structure canonique (0 → 5), **adapter les sections et le contenu** selon le type de poste. Les paragraphes ci-dessous décrivent le **contenu à ajouter** (enrichissement) pour chaque module.

### 6.1 Infogérant informatique (niveau 1 & niveau 2)

Pour un poste **infogérant / support informatique N1 et N2** (à inclure aussi dès que des questions de **maintenance informatique N2** sont susceptibles d’être posées, même si le poste n’est pas directement infogérance) :

- **Conserver** : info-box, sections 0 (présentation), 1 (formalités), 4 (questions à poser), 5 (entreprise).
- **Section 2** : remplacer / compléter par **Q/R et savoir-faire Infogérant** :
  - **Niveau 1** : prise en charge des demandes (ticketing, première ligne), résolution courante (mot de passe, accès, imprimante, poste), escalade au N2, outils (GLPI, Zendesk, RDS, etc.), procédures et délais SLA.
  - **Niveau 2** : diagnostic avancé, administration (Active Directory, GPO, DNS, DHCP), supervision, déploiement (patches, images), participation à la roadmap infra.
- **Section 3 — Questions techniques maintenance N2** (toujours les avoir, variété d’excellence) :
  - **Ticketing et escalade** : cycle de vie d’un ticket, critères d’escalade N1 → N2 → N3, prioritisation (P1/P2/P3), délais SLA, outils (GLPI, ServiceNow, Jira Service Desk).
  - **Active Directory / annuaire** : GPO (stratégies de groupe), OU (unités d’organisation), gestion des comptes et des droits, réplication, sauvegarde AD.
  - **Réseau (niveau N2)** : DNS (enregistrements A, CNAME, MX), DHCP (réservation, scope), dépannage connectivité, VLAN, pare-feu basique.
  - **Supervision et déploiement** : outils de supervision (Nagios, Zabbix, PRTG), déploiement de patches (WSUS, SCCM), images système, PRA/PCA.
  - **Bonnes pratiques** : documentation, traçabilité des interventions, communication avec les utilisateurs et les équipes internes, gestion des priorités.
- **Lexique** : SLA, ticket, escalade, N1/N2/N3, RDS, AD, GPO, OU, DNS, DHCP, hotline, infogérance, supervision, PRA/PCA, WSUS, SCCM.

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

### 6.5 Ruby et Ruby on Rails

Pour des **questions techniques Ruby / Ruby on Rails** (à inclure dans la variété des technos, même si le poste n’est pas centré Rails) :

- **Ruby (langage)** : typage dynamique, objets et classes, blocs et yield, modules et mixins, symboles vs strings, itérateurs (each, map, select), gestion des erreurs (begin/rescue), gems et Bundler.
- **Ruby on Rails** : MVC (modèles, vues, contrôleurs), convention over configuration, migrations, ActiveRecord (associations, validations, requêtes), routes et ressources REST, vues (ERB, partials), asset pipeline, Webpacker, sécurité (CSRF, injection), déploiement (Capistrano, Puma, Nginx).
- **Questions courantes** : différence Ruby vs Rails, Rack, middleware, tests (RSpec, Minitest), différence avec Django/Flask ou autres frameworks.

**Lexique** : MVC, ORM, migration, REST, ERB, gem, Bundler, RSpec, Capistrano.

### 6.6 DevOps (initiation — Git, GitLab CI/CD, GitHub Actions, Docker, WordPress)

Pour des **questions sur des pratiques DevOps** (initiation ; à inclure en format **cours et révisions**, notions principales) :

- **Git (GitHub, GitLab)** : branches, merge vs rebase, conflits, workflow (feature branch, main/develop), pull request / merge request, tags, .gitignore, bonnes pratiques de commit.
- **GitLab CI/CD** : fichier `.gitlab-ci.yml`, stages (build, test, deploy), jobs, variables, pipelines, runners, cache.
- **GitHub Actions** : workflows (`.github/workflows/`), triggers (push, pull_request), jobs et steps, secrets, actions réutilisables, matrix strategy.
- **Docker** : images et conteneurs, Dockerfile (FROM, RUN, COPY, CMD, EXPOSE), docker-compose (multi-conteneurs, services, volumes, networks), bonnes pratiques (image légère, non-root, .dockerignore).
- **WordPress** : architecture (PHP, MySQL, thèmes, plugins), sécurité (mises à jour, rôles, sauvegardes), performance (cache, CDN), déploiement et hébergement.

**Lexique** : CI/CD, pipeline, Dockerfile, image, conteneur, volume, merge request, staging, runner, workflow.

### 6.7 CSS (questions techniques)

Pour des **questions techniques CSS** (à inclure dans la variété des technos front) :

- **Sélecteurs et spécificité** : classes, id, combinateurs, pseudo-classes (:hover, :nth-child), spécificité et !important, cascade et héritage.
- **Layout** : Flexbox (flex-direction, justify-content, align-items), Grid (grid-template, areas), position (relative, absolute, fixed, sticky), display (block, inline, flex, grid).
- **Responsive** : media queries, unités (rem, em, vw/vh), mobile-first vs desktop-first, breakpoints.
- **Moderne** : variables CSS (custom properties), transitions et animations, préprocesseurs (Sass) si pertinent.

**Lexique** : Flexbox, Grid, media query, spécificité, rem/em.

### 6.8 SQL (notions principales — cours et révisions)

Pour des **questions techniques SQL** (format **cours et révisions**, notions principales, comme les autres modules) :

- **Bases** : DDL (CREATE, ALTER, DROP), DML (SELECT, INSERT, UPDATE, DELETE), DCL (GRANT, REVOKE), schéma, tables, clés primaires et étrangères.
- **Requêtes** : SELECT avec WHERE, ORDER BY, LIMIT, DISTINCT ; agrégations (COUNT, SUM, AVG, MIN, MAX) et GROUP BY, HAVING ; jointures (INNER, LEFT, RIGHT, FULL, CROSS).
- **Notions avancées** : sous-requêtes, EXISTS, IN ; vues (VIEW) ; index (création, impact sur les perfs) ; transactions (BEGIN, COMMIT, ROLLBACK) et ACID.
- **Optimisation** : lecture de plans d’exécution (EXPLAIN), index appropriés, évitement des full table scans.

**Lexique** : DDL, DML, jointure, index, transaction, ACID, vue.

### 6.9 PostgreSQL (notions principales — cours et révisions)

Pour des **questions techniques PostgreSQL** (format **cours et révisions**, notions principales) :

- **Spécificités** : type JSON/JSONB, types array, extensions (pg_trgm, PostGIS si pertinent), séquences, SERIAL.
- **Administration** : connexion (psql), utilisateurs et rôles (CREATE ROLE, GRANT), sauvegarde (pg_dump, pg_restore), maintenance (VACUUM, ANALYZE).
- **Performance** : EXPLAIN (ANALYZE, BUFFERS), index (B-tree, GIN, GiST), connexions (pooling : PgBouncer), paramètres (shared_buffers, work_mem).
- **Intégration** : utilisation avec Django (ORM, migrations), avec Python (psycopg2), avec des outils (DBeaver, pgAdmin).

**Lexique** : JSONB, VACUUM, EXPLAIN, psql, pg_dump, pool de connexions.

---

## 7. Références

- **Organisation projets** : `organisation-projets-et-nouveaux-dossiers.md` — un projet = un dossier à part ; nouvelle fiche entretien → `docs/ressources-utilisateur/fiches-entretien-emploi/<slug_entreprise>/` ; templates/modèles dans les emplacements partagés.
- **Espace fiches** : `docs/ressources-utilisateur/fiches-entretien-emploi/` (README, un dossier par entreprise).
- **Modèle canonique** : `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html`
- **Template HTML (structure à appliquer)** : `fiches-entretien-emploi-template-html.md` (sections à la racine, accordéons fermés par défaut).
- **Types de poste / modules d’enrichissement** : § 6 — **Infogérant N1/N2** (§ 6.1), **Consultant SEO** (§ 6.2), **Pentesting / Cybersécurité** (§ 6.3), **IoT** (§ 6.4), **Ruby / Ruby on Rails** (§ 6.5), **DevOps** (§ 6.6 : Git, GitLab CI/CD, GitHub Actions, Docker, WordPress), **CSS** (§ 6.7), **SQL** (§ 6.8), **PostgreSQL** (§ 6.9). Tous au format **cours et révisions** (notions principales, comme le modèle existant). Ne pas supprimer le contenu existant ; **reprendre tels quels** et **enrichir**.
- **Règle Assistant** : `.cursor/rules/assistant-entretien-emploi.mdc`
- **Registre** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Rôles (Rédacteur = agent RH)** : `docs/base-de-connaissances/agents-roles-responsabilites.md` § Rédacteur, § Assistant Entretien Emploi.
- **SEO (contenu)** : `rapport-seo-prospect.md`, `seo-semantique-outils-open-source.md` pour rester aligné avec le projet.
