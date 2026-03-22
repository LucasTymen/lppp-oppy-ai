# Fiches Entretien Emploi — Espace de l’assistant copilote

**Rôle** : espace de travail de l’**Assistant Entretien Emploi** (règle `.cursor/rules/assistant-entretien-emploi.mdc`).  
L’agent y crée et met à jour les **fiches Résumé** (HTML avec accordéons) pour la préparation des entretiens d’embauche.

## Modèle canonique (structure de référence)

- **Fichier de référence** : `_modele-canonique_prepa_entretien.html` (à la racine de ce dossier). Ce modèle est la **structure de référence** fournie par l’utilisateur.
- **Règle** : **même organisation, même structure, même nombre d’onglets** que le modèle donné. Le **contenu** seul change et s’adapte dynamiquement (boîte, poste).
- **Cinq familles de contenu à reprendre** : (1) questions qu’on est censé me poser, (2) questions que je peux poser à l’entreprise, (3) pistes de réflexion / pitch personnel, (4) conditions d’embauche, (5) questions à poser relatives aux RH. Toutes doivent être présentes ; détail : `fiches-entretien-emploi-modele-et-veille.md` § 1 « Contenu à reprendre ».
- À **chaque nouvelle préparation** : reprendre cette structure (sections + sous-accordéons), puis **adapter le contenu** (présentation, formalités, entreprise, etc.) à la société ciblée. Vérifier qu'il ne reste **aucun résidu** de l'ancienne société (checklist dans la base de connaissances).
- **Doc complète** : `docs/base-de-connaissances/fiches-entretien-emploi-modele-et-veille.md` (règle centrale § 1, modèle, veille, coordination agents, checklist « nouvelle société »).

## Organisation

- **Règle projet** : un projet = un dossier à part (voir `docs/base-de-connaissances/organisation-projets-et-nouveaux-dossiers.md`).
- **Un dossier par entreprise** (slug unique : nom de l’entreprise, éventuellement `Nom_Marche` si pertinent).
- Dans chaque dossier :
  - **fiche HTML** : fiche de préparation entretien (structure = modèle canonique, contenu = société ciblée).
  - **ressources** : notes, extraits, documents utilisés pour construire la fiche.
  - **résumé** : fichier texte ou Markdown des points clés à réviser.
  - **versions** : copies datées des fiches avant mise à jour (ou sous-dossier `versions/`).

## Types de poste (sections à adapter)

- **Général** : structure canonique 0 → 5 (présentation, formalités, Q/R stratégiques, tests techniques, questions à poser, entreprise).
- **Infogérant N1/N2 / Maintenance N2** : ticketing, escalade, AD, GPO, DNS, DHCP, supervision, déploiement. Détail : doc § 6.1.
- **Consultant SEO** : rappel SEO technique, sémantique, avenir du SEO. Détail : doc § 6.2.
- **Pentesting / Cybersécurité** : notions base à avancées, préceptes, guides en cas d’attaque. Détail : doc § 6.3.
- **IoT** : architectures, protocoles, sécurité, cas d’usage. Détail : doc § 6.4.
- **Ruby / Ruby on Rails** : langage Ruby, Rails (MVC, ActiveRecord, migrations, sécurité). Détail : doc § 6.5.
- **DevOps (initiation)** : Git, GitLab CI/CD, GitHub Actions, Docker, WordPress. Détail : doc § 6.6.
- **CSS** : sélecteurs, layout (Flexbox, Grid), responsive, variables. Détail : doc § 6.7.
- **SQL** : DDL, DML, jointures, agrégations, index, transactions. Détail : doc § 6.8.
- **PostgreSQL** : JSONB, admin, performance, intégration. Détail : doc § 6.9.

**Règle** : le contenu existant (Python, Django, Java, etc.) est **repris tel quel** ; on **enrichit** en ajoutant ces modules au **même format** que le modèle (cours et révisions, notions principales par module). Ne pas supprimer sans adapter.

## Exemples de référence

- **Structure HTML** : modèle canonique (titre, info-box, accordéons `.accordion` / `.sub-accordion`, `.panel` / `.sub-panel`, classes `.highlight`, `.success`, `.warning`, `.info`, `.tip`).
- **Rubriques** : présentation entreprise, missions, KPIs, questions techniques (Python, Django, Java, Spring, Angular, Growth…), questions à poser, questions relationnelles (Rédacteur = agent RH).

## Règles

- Ne pas supprimer une fiche sans en garder une copie datée.
- Toute mise à jour → nouvelle version datée ou copie de l’ancienne avant écrasement.
- **Changement de société** : repartir du modèle canonique ou appliquer la checklist « nouvelle société » (doc base de connaissances) pour éviter fantômes et hallucinations.
