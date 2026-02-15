# Attentes — Contenu et qualité de l'enrichissement

**Objectif** : Référence unique pour ne pas recommencer à zéro. Ce que l’on attend en termes de **contenu** (landings, rédaction) et de **qualité de l’enrichissement** (données prospect, OSINT, livrables). S’appuie sur l’historique du Conseiller, du Chef de Projet, de la stratégie qualité et des erreurs/solutions documentées.

**Pour** : Rédacteur, Conseiller, Chef de Projet, Growth, Pentester, Expert Google Dorks, tous les agents qui produisent ou valident du contenu ou des données enrichies.

---

## 1. Contenu (landings, rédaction)

### 1.1 Barre qualité P4S (toutes les landings)

**Rappel** : une landing ciblant une collectivité (ex. mairie) est une **page de prospection pour se vendre** (missions, CDI, CDD), pas une « page municipale ». Les démos (chatbot, Loom) sont des **sections** qui illustrent ce qu’on peut déployer. Voir `erreurs-et-solutions.md` (entrée « Landing Maisons-Alfort »).

- **Sections complètes** : hero, enjeux, solution, services, offre, coordonnées, CTA — remplies depuis les données, pas de blocs vides ni de placeholders visibles.
- **Pas de squelette** : la page affichée = la page finale ; pas de « Lorem ipsum » ni de « à remplir » pour le visiteur.
- **Un contact = un jeu de données unique** : jamais le même contenu pour deux contacts ; source de vérité = `docs/contacts/<slug>/` et `content_json` dédié à ce contact.
- **Contact utilisable** : CTA et coordonnées fonctionnent (popup contact, email affiché, pas de lien mort).
- **Rapport** : si une étude (PESTEL/SWOT/Porter, SEO) existe pour le contact, `rapport_url` renseigné et lien « Consulter le rapport » visible ; si étude SEO, `seo_resume` pour la section Résumé SEO + ancre `#analyse-seo-complete`.
- **Personnalisation** : hero (image ou thème), style cohérent avec la cible (CSS Vampire ou thème manuel si besoin).

Référence : `strategie-qualite-contenu-landings.md`.

### 1.2 Contenu vivant et humanisation

- **Positionnement** : paragraphe narratif (contexte, angle, « pourquoi je vous contacte ») après le hero ou avant les enjeux.
- **Enjeux** : phrase d’introduction (`enjeux_lead`) au-dessus de la liste des pain points ; pas un mur de listes sans contexte.
- **Rapport / résumé SEO** : `rapport_url`, `seo_resume` (title, manque_annuel, intro, problèmes_cles, lien_analyse) dès qu’une étude existe.
- **Bandeau** : `alert_banner` pour un message d’accroche fort (offre, CTA court) si pertinent.
- **Ton** : phrases variées (courtes et longues), transitions naturelles, « vous » et contexte (prénom, société) ; pas de sur-polissage ni de formules toutes faites.
- **Pas de remplissage** : chaque bloc apporte une info ou une intention claire.

Référence : `brief-contenu-vivant-humanisation-landings.md`.

### 1.3 Éditorial (anti-détection IA, image pratique)

- **Anti-détection IA** : pas de formules de cadrage (« Dans un monde où… »), pas de structure hyper-segmentée partout, pas de vocabulaire corporate excessif, pas d’intensifieurs à faible coût (« crucial », « essentiel »), pas d’emojis ni de symboles non naturels. Texte fluide, crédible, incarné. Voir `bonnes-pratiques.md` § 1.
- **Humanisation** : destinataire réel (prospect, lecteur), contexte métier (nom entreprise, prénom, besoin), formulations naturelles, pas de remplissage.
- **Image pratique** : livrables avant promesses, ancrage technique (stack, format de sortie), éviter les formules vagues ; chiffres et délais crédibles. Voir `bonnes-pratiques.md` § 2 bis.

Référence : `bonnes-pratiques.md`.

### 1.4 Rôle conseiller (informations manquantes)

- **Repérer les manques** : infos importantes manquantes (risque d’être interrogé en entretien ou en livrable) → **demander** à l’utilisateur de les fournir pour intégration.
- **Si indisponibles** : ne pas inventer → **décider avec l’utilisateur** de la stratégie (mentionner le manque, réponse de repli, reporter, etc.).
- **Handoff** : après accord explicite, transmettre au Chef de Projet un brief clair (accord résumé, périmètre, contraintes, risques, ressources). Voir `handoff-conseiller-chef-projet.md`.

Référence : `fiches-entretien-emploi-modele-et-veille.md` § 4, `conseiller.mdc`, `assistant-entretien-emploi.mdc`.

---

## 2. Qualité de l'enrichissement (données prospect, OSINT)

### 2.1 Règles métier

- **Une tâche = un outil** : ne pas regrouper plusieurs sources en une seule exécution (risque de blocage Google/LinkedIn). Privilégier le flux décomposé (`enrich_prospect_decomposed`) pour les contacts complexes.
- **Guide-rails** : validation des entrées, rate limiting, max batch 50 ; pas de propagation de données sensibles sans contrôle.
- **Fiche data complète** : `Prospect.enriched_data` rempli (company, contact), qualité et score via `apps.intelligence` ; livrable = prospects avec fiche enrichie complète (badges complets).
- **Pas d’hallucination** : s’appuyer uniquement sur les sources et APIs présentes dans le dépôt ; ne pas inventer d’API, de syntaxe ou de variable. Si une info n’existe pas, indiquer « à vérifier » ou proposer de l’ajouter après validation.

Référence : `strategie-enrichissement.md`, `enrichissement-osint-flowise-n8n.md`, `pentester.mdc`, `expert-google-dorks-linkedin.mdc`.

### 2.2 Sécurité et flux

- **Credentials** : jamais divulgués ni committés ; pas de log de mots de passe ou de tokens.
- **Isolation des flux** : rate limiting sur les API d’enrichissement ; validation des webhooks N8N/Flowise ; pas d’exécution de code arbitraire ni de log de données personnelles.

Référence : `regles-securite.md`, `politique-credentials-securite-flux.md`, `pentester.mdc`.

### 2.3 En cas d’erreur ou de blocage

- **Consulter** `erreurs-et-solutions.md` avant de réinventer ; après une correction, ajouter une entrée (contexte, erreur, cause, solution, prévention).
- **Logs** : mettre à jour `log-projet.md` ou `log-ia.md` après résolution pour que l’équipe ne reproduise pas l’erreur.

Référence : `erreurs-et-solutions.md`, `agents-roles-responsabilites.md` (Chef de Projet, documenter erreurs).

---

## 3. Checklist rapide (avant livraison / avant enrichissement)

| Domaine | Points à vérifier |
|---------|-------------------|
| **Contenu landing** | Un contact = un JSON dédié ; sections complètes ; pas de squelette ; CTA/coordonnées OK ; rapport_url / seo_resume si étude existe ; ton vivant, éditorial OK. |
| **Conseiller** | Accord explicite obtenu ; brief (handoff) transmis au Chef de Projet ; manques identifiés et traités avec l’utilisateur (pas d’invention). |
| **Enrichissement** | Une source à la fois si contact complexe ; guide-rails respectés ; fiche data complète ; pas d’invention de sources ou d’API. |
| **Sécurité** | Aucun secret dans le code ni le dépôt ; erreurs documentées dans erreurs-et-solutions si nouveau cas. |

---

## 4. Fichiers sources (pour ne pas recommencer)

| Document | Usage |
|----------|--------|
| `strategie-qualite-contenu-landings.md` | Qualité P4S, contenu dynamique, checklist livraison. |
| `brief-contenu-vivant-humanisation-landings.md` | Contenu vivant, champs à combler, ton, mission Rédacteur/Designer. |
| `bonnes-pratiques.md` | Éditorial anti-détection IA, humanisation, image pratique. |
| `handoff-conseiller-chef-projet.md` | Brief Conseiller → Chef de Projet, périmètre, contraintes. |
| `fiches-entretien-emploi-modele-et-veille.md` § 4 | Rôle conseiller (manques, ne pas inventer, stratégie avec l’utilisateur). |
| `strategie-enrichissement.md` | Une tâche = un outil, flux décomposé, fusion + intelligence. |
| `enrichissement-osint-flowise-n8n.md` | API webhook, guide-rails, N8N/Flowise. |
| `erreurs-et-solutions.md` | Consulter avant de corriger ; ajouter une entrée après résolution. |
| `regles-securite.md` | Secrets, Django prod, CSRF/XSS, rate limiting, checklist prod. |

---

*Document créé pour centraliser les attentes contenu et enrichissement (historique Conseiller, stratégie qualité, brief, erreurs). À utiliser pour ne pas recommencer et aligner tous les agents. Dernière mise à jour : 2026-02-06.*
