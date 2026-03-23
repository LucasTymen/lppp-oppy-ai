# Base CV / savoir-faire pour prospection et justification

**Rôle** : outil de référence pour analyser et prospecter une entreprise en proposant le savoir-faire de Lucas Tymen. Les agents **doivent avoir accès** à ce fichier et **peuvent piocher dedans** dès qu’il faut justifier ou parler de son savoir-faire (argumentaire, email d’approche, LM, entretien, etc.).

**Fichier** : `docs/ressources-utilisateur/cv_base_datas_pour_candidatures.json`

---

## 1. Usage

- **Prospection** : analyser une cible (entreprise, offre) et proposer un savoir-faire pertinent à partir des expériences, compétences, preuves business et arguments réutilisables contenus dans le JSON.
- **Justification** : quand un agent rédige un message de candidature, une lettre de motivation, un email d’approche, une fiche entretien ou tout contenu qui présente le profil, il **peut et doit** s’appuyer sur ce fichier pour rester factuel et cohérent (pas d’invention d’outils, de durées ou de chiffres non présents ou non dérivables du fichier).
- **Landings** : ce fichier **n’est pas utilisé par défaut** dans la génération des landing pages. Les landings continuent d’être alimentées par les JSON de contact (`docs/contacts/<slug>/landing-proposition-*.json`). En revanche, si un agent doit rédiger un bloc « À propos » ou un argumentaire sur le profil pour une landing de prospection, il peut piocher dans `cv_base_datas_pour_candidatures.json`.

---

## 2. Contenu type du JSON (pour les agents)

Le fichier contient notamment :

- **meta** : positionnement global, objectif, stratégie par secteur (IT support vs growth/SEO/data/dev).
- **experiences** : expériences détaillées (SquidResearch, Parazar, Avtis, Engage Paris, LPPP, projets collectifs, APSI, Freelance) avec réalisations, stack, preuves (benchmarks, délivrabilité, leads, etc.).
- **stages_et_projets_collectifs** : stages et projets de formation (Farniente, Pet Sitter, L’Accroche, Chewie n’B).
- **preuves_business_contextualisees** : indicateurs par projet (parc, tickets, matching, délivrabilité, leads, throughput, cache, Next.js/Vercel, OSINT, Tor/anti-détection).
- **competences_detaillees** : par domaine (IT support, backend/fullstack, automation/data, SEO/growth, design, Microsoft 365, etc.) avec niveaux et outils.
- **arguments_reutilisables** : arguments par type de cible (it_pme, backend_engineer, growth_systems) avec contexte et valeur.
- **narratifs_candidature** : accroches par profil (it_support_pme, it_ops_hybride, accroche_backend, accroche_growth, CTA landing Infopro).
- **mots_cles_ats** : mots-clés par secteur pour ATS et recruteurs.
- **assets_strategiques** : ex. landing Infopro (URL, description, usage).
- **personas_specialises** : détection secteur et titres CV par persona (it_support_pme, backend_django, growth_ops, seo_technique, etc.).

---

## 3. Règles pour les agents

- **Accès** : tout agent qui rédige ou adapte un CV, une LM, un email de candidature ou un argumentaire de prospection **doit pouvoir consulter** `docs/ressources-utilisateur/cv_base_datas_pour_candidatures.json`.
- **Piocher, pas inventer** : utiliser uniquement les données de ce fichier (ou dérivables de celui-ci) pour justifier le savoir-faire. Ne pas inventer d’outils, de durées ou de chiffres absents du fichier.
- **Landings** : ne pas brancher ce fichier comme source par défaut des landings ; l’utiliser uniquement quand le besoin est de **justifier ou présenter le savoir-faire** dans un contenu (texte « À propos », email d’approche lié à une landing, etc.).

---

## 4. Mise à jour

Le fichier est maintenu par l’utilisateur (source : Downloads, puis copie dans le dépôt). Pour mettre à jour la version dans le projet, copier le fichier depuis `Downloads\cv_base_datas_pour_candidatures.json` vers `docs/ressources-utilisateur/cv_base_datas_pour_candidatures.json`.

---

*Référence : registre `registre-agents-ressources.md` § Base savoir-faire / prospection ; ressources utilisateur `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md`.*
