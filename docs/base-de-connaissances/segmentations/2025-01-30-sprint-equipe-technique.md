# Sprint 2025-01-30 — Toute l'équipe technique mobilisée

**Date** : 2025-01-30  
**Statut** : 🟢 En cours  
**Objectif** : S'assurer que **chaque rôle technique** a au moins une tâche explicite sur ce sprint (stack, montage projet, interface /essais/, livrables P4S-archi).

**Référence** : ce document est la **matrice d'assignation** du sprint ; les détails techniques restent dans les segmentations liées. Le **Chef de Projet** met à jour les statuts et `reste-a-faire-avant-tout-fonctionne.md` à chaque avancement notable.

---

## 1. Périmètre du sprint

| Bloc | Segmentations | Priorité |
|------|----------------|----------|
| **Stack et accès** | `2025-01-30-lancement-docker-projet.md` | Haute |
| **Montage projet (écrans, routes, logique)** | `2025-01-30-montage-projet-ecrans-routes-logique.md` | Haute |
| **Interface /essais/** | `2025-01-30-interface-landingsgenerator.md` | Haute |
| **Relance événements** | `2025-01-30-relance-evenements.md` | Haute |
| **Livrables P4S-archi** | `2025-01-30-premier-rapport-seo-landing-p4s-archi.md` | Haute |

---

## 2. Assignation par rôle — toute l'équipe technique

Chaque agent technique doit travailler sur au moins une tâche listée ci-dessous. Les livrables et critères de fin sont dans les segmentations détaillées.

| Rôle | Tâches ce sprint | Segmentation(s) | Statut |
|------|------------------|-----------------|--------|
| **Chef de Projet** | Valider specs écrans et routes ; répartir les tâches ; maintenir TODO, segmentations et `reste-a-faire-avant-tout-fonctionne.md` ; valider livrables avant intégration. | Montage, Interface, toutes | À faire |
| **Orchestrateur** | Mettre à jour le registre et les segmentations ; s'assurer que chaque pilote a les bonnes références (registre, `routes-back-lppp.md`, `intelligence-metier-algorithmes.md`) ; pointer ce sprint dans le registre. | Montage, Registre | À faire |
| **Dev Django** | Backend : vues, URLs, static ; admin et /essais/ fonctionnels ; routes /campaigns/ (liste + détail) ; tenir à jour `routes-back-lppp.md` ; connecter les vues à `apps.intelligence` ; cohérence modèles admin. | Lancement, Montage, Interface | En cours / À faire |
| **DevOps** | Stack Docker (build, up) ou Option B runserver si ERR_EMPTY_RESPONSE ; `.env`, ports ; vérifier static/WSGI ; **collaborer avec Automatizer** pour conteneurs n8n/flowise et logs (voir `info-automatizer-pour-equipe.md`) ; pas de régression admin/essais ; déploiement cohérent. | Lancement, Montage, Interface | À faire |
| **Pentester** (sécurité) | Une fois le stack lancé : isolation des flux (API enrich, Flowise, n8n), pas de fuite de données ; **collaborer avec Automatizer** pour la sécurité des workflows (voir `info-automatizer-pour-equipe.md`) ; appliquer `regles-securite.md`, `politique-credentials-securite-flux.md`. | Lancement | À faire |
| **Designer** | Interface /essais/ : vérification page par page (mode nuit, switch clair/sombre, fonds noirs, cas limites type SquidResearch) ; mobile-first, safe-area. | Interface | À faire |
| **Data Analyst** | Documenter les appels `apps.intelligence` pour les écrans (`score_prospect`, `prospect_completeness`, `best_landing_for_prospect`) ; fournir les points d'entrée à Dev Django ; brancher les nodes sur l'intelligence. | Montage | À faire |
| **Growth** | Vérifier pipelines enrichissement (n8n, Flowise) et tâches Celery en cohérence avec le stack ; **collaborer avec Automatizer** pour workflows N8N/Flowise (voir `info-automatizer-pour-equipe.md`) ; **déléguer au Growth Analyst** (études concurrentielles, SWOT, marché, Ads, nouveaux marchés — voir `growth-analyst-concurrentiel-marche-ads.md`) ; documenter stratégie d'enrichissement si besoin ; préparation étude Growth P4S-archi (KPIs, funnel). | Montage (flux), P4S-archi | À faire |
| **Automatizer** (workflows N8N, Flowise, automatisation) | Développer et maintenir les workflows (N8N, Flowise, webhooks, Celery) ; monitoring, optimisation tokens, traces de performances ; collaborer avec Growth, DevOps, Dev Django, Pentester (voir `info-automatizer-pour-equipe.md`). | Lancement (flux), Montage | À faire |
| **Rédacteur** | Contenu premier écran /essais/ (présentation relance salon, positionnement freelance/alternant, ciblage activité/pain points) ; structure `content_json` relance événement (hero, CTA) ; bonnes pratiques `bonnes-pratiques.md`. | Interface, Relance événements | À faire |
| **Expert SEO** | Préparer ou produire le premier rapport SEO P4S-archi (5 CSV Screaming Frog + analyse sémantique) ; livrable `docs/contacts/p4s-archi/rapport-seo.md` ; coordination avec Rédacteur/Designer pour intégration. | P4S-archi | À faire |

---

## 3. Ordre et parallélisation

1. **En parallèle** : DevOps (stack) + Dev Django (backend/URLs) + Chef de Projet (validation specs).
2. **Ensuite** : Pentester (sécurité flux), Data Analyst (doc intelligence + points d'entrée), Designer (vérif /essais/), Rédacteur (contenus).
3. **En parallèle** : Growth (enrichissement + prépa étude P4S), Expert SEO (rapport P4S-archi).
4. **Orchestrateur** : mise à jour registre et références en continu.

---

## 4. Références

- **Registre** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Routes back** : `docs/base-de-connaissances/routes-back-lppp.md`
- **Reste à faire** : `docs/reste-a-faire-avant-tout-fonctionne.md`
- **TODO** : `docs/TODO.md`
- **Rôles et RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md`

---

*Document créé pour mobiliser toute l'équipe technique sur ce sprint. À mettre à jour par le Chef de Projet et l'Orchestrateur.*
