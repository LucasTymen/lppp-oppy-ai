# Console landings — Automatiser et traquer les landing pages générées

**Objectif** : pouvoir **consulter dans une console** toutes les landing pages générées, avec leurs URLs (Django + Vercel standalone), et poser les bases pour **automatiser** la génération et le **traçage** des déploiements.

**Pilotes** : Chef de Projet (vision), DevOps (déploiement, URL), Dev Django (console, modèle).  
**Dernière mise à jour** : 2025-01-30.

---

## 1. Ce qui est en place

### 1.1 Console (consultation)

- **URL** : **`/console/`** (après connexion au site LPPP).
- **Contenu** : tableau de toutes les landing pages avec :
  - Société / titre, slug, secteur, catégorie ;
  - Statut (publiée / brouillon, déployée si `deploy_url` renseigné) ;
  - **URL Django** : lien vers la landing sur le backend (ex. `https://<ton-domaine>/p/<slug>/`) ;
  - **URL déployée** : lien vers la version Vercel standalone si renseigné ;
  - Date de création.
- **Filtres** : par secteur et par catégorie.
- **Accès** : utilisateurs connectés ; les non-staff ne voient que leurs propres landings.

### 1.2 Traçage (URL déployée)

- **Modèle** : `LandingPage` a un champ **`deploy_url`** (URL, optionnel).
- **Usage** : quand une landing est déployée en standalone sur Vercel (1 repo = 1 projet Vercel), renseigner l’URL du projet (ex. `https://lppp-p4-s-architecture.vercel.app`) dans l’admin ou via l’API.
- **Effet** : la console affiche alors « déployée » et le lien vers la version live ; tu peux consulter en un coup d’œil toutes les landings et leurs deux URLs (Django + Vercel).

### 1.3 Où renseigner l’URL déployée

- **Admin Django** : `Landing page` → éditer une landing → champ **URL déployée** (`deploy_url`). À remplir après chaque déploiement Vercel réussi (voir `strategie-deploiement-git-vercel.md`).
- **Procédure** : après avoir poussé le code et configuré Vercel pour un repo standalone, noter l’URL du projet (ex. `https://lppp-<slug>.vercel.app`) et la mettre dans la fiche landing correspondante (même slug) dans l’admin.

---

## 2. Étape suivante : automatisation (à développer)

Pour **automatiser** la génération et le traçage :

1. **Création de landings**  
   - Depuis l’admin (déjà possible).  
   - **À prévoir** : commande Django ou API (ex. `POST /api/landings/` ou `create_landing_from_prospect`) pour créer une landing à partir d’un prospect / d’un template ; déclenchement possible depuis n8n ou un script après enrichissement.

2. **Traçage après déploiement**  
   - Aujourd’hui : renseignement manuel de `deploy_url` dans l’admin.  
   - **À prévoir** (optionnel) : script ou webhook post-déploiement Vercel qui met à jour `deploy_url` (via API Django ou mise à jour directe en base) pour que la console soit à jour sans saisie manuelle.

3. **Console**  
   - Déjà en place : `/console/` liste toutes les landings avec URLs Django et déployées.  
   - Évolutions possibles : export CSV, colonne « Dernière mise à jour déploiement », lien direct « Copier URL » pour envoi au prospect.

---

## 3. Récapitulatif

| Élément | Statut | Détail |
|--------|--------|--------|
| **Console** | ✅ En place | `/console/` — tableau landings + URL Django + URL déployée, filtres secteur/catégorie. |
| **Champ deploy_url** | ✅ En place | Sur `LandingPage` ; renseigné à la main dans l’admin après déploiement Vercel. |
| **Traçage manuel** | ✅ En place | Remplir `deploy_url` après chaque déploiement standalone (voir procédure Git + Vercel). |
| **Automatisation création** | À prévoir | API ou commande pour créer une landing depuis prospect/template ; déclenchement n8n/script. |
| **Automatisation traçage** | À prévoir | Webhook ou script post-déploiement Vercel pour mettre à jour `deploy_url`. |

---

## 4. Références

- **Vue console** : `apps/landing_pages/views.py` (`console_landings`), template `templates/landing_pages/console.html`.
- **Modèle** : `apps/landing_pages/models.py` (`LandingPage.deploy_url`).
- **Admin** : `apps/landing_pages/admin.py` (liste avec `deploy_url`).
- **Déploiement** : `strategie-deploiement-git-vercel.md`, `procedure-fin-landing-repo-deploiement.md`.

---

*Document créé pour l’étape suivante : automatiser et traquer les landings, consulter dans la console. Dernière mise à jour : 2025-01-30.*
