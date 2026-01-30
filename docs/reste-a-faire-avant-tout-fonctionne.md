# Ce qui reste à faire avant que tout fonctionne bien

Document de synthèse (Chef de Projet / Orchestrateur). Mis à jour à partir du TODO et des segmentations.

---

## 1. Infra et accès (priorité immédiate)

**Environnement choisi** : **Docker web** (conteneur web, port 8000). Option B (runserver local) reste en dépannage si besoin (voir `pret-a-demarrer.md` § 5).

| Reste à faire | Qui | Référence |
|---------------|-----|-----------|
| **URGENT — Git init + remotes** (GitHub, GitLab) : pas encore fait, signalé comme priorité par l’utilisateur. | DevOps | `2025-01-30-devops-git-init-remotes.md`, `git-remotes-github-gitlab.md` |
| **Vérifier** : admin et /essais/ accessibles (Docker web sur 127.0.0.1:8000 ou runserver 8080 en dépannage), migrations à jour, pas de régression. | DevOps, Dev Django | `lancement-docker-projet.md` |

---

## 2. Montage projet (écrans, routes back, logique métier)

| Reste à faire | Qui | Référence |
|---------------|-----|-----------|
| **Concordance des routes** : tenir à jour `routes-back-lppp.md` à chaque ajout de route. | Dev Django | `routes-back-lppp.md`, `2025-01-30-montage-projet-ecrans-routes-logique.md` |
| **/campaigns/** : définir et implémenter les routes (liste, détail, éventuel CRUD) — actuellement `apps.campaigns.urls` est vide. | Dev Django, Chef de Projet | `montage-projet-ecrans-routes-logique.md` |
| **Écrans /essais/** : premier écran (relance salon) en place ; ajouter les écrans suivants selon specs (wizard, choix template, etc.). | Dev Django, Designer, Chef de Projet | `2025-01-30-interface-landingsgenerator.md` |
| **Designer** : vérifier /essais/ page par page (mode nuit, switch clair/sombre, cas limites). | Designer | `interface-landingsgenerator.md` |
| **Logique métier** : documenter les appels `apps.intelligence` pour les écrans (score_prospect, prospect_completeness, best_landing_for_prospect) ; brancher les vues sur l’intelligence. | Data Analyst, Dev Django | `intelligence-metier-algorithmes.md`, `montage-projet-ecrans-routes-logique.md` |
| **Admin** : s’assurer que modèles (campagnes, prospects, landing pages) sont cohérents avec la logique métier et exposés correctement. | Dev Django | — |

---

## 3. Livrables métier (P4S-archi, première landing)

| Reste à faire | Qui | Référence |
|---------------|-----|-----------|
| **Premier rapport SEO P4S-archi** : à partir des 5 CSV Screaming Frog + analyse sémantique ; livrable `docs/contacts/p4s-archi/rapport-seo.md`. | Expert SEO | `2025-01-30-premier-rapport-seo-landing-p4s-archi.md` |
| **Étude Growth P4S-archi** : KPIs + funnel d’acquisition ; livrable `docs/contacts/p4s-archi/etude-growth-funnel-kpis.md`. | Growth | Idem |
| **Première landing P4S-archi** : template relance événement, content_json, publication ; coordination Rédacteur, Designer, Dev Django. | Chef de Projet, Rédacteur, Designer, Dev Django | Idem |
| **Relance événements** : template landing relance salon + structure content_json (hero, CTA, positionnement freelance/alternant). | Rédacteur, Designer, Dev Django | `2025-01-30-relance-evenements.md` |

---

## 4. Améliorations (après que le cœur fonctionne)

| Reste à faire | Qui | Priorité |
|---------------|-----|----------|
| Moderniser les landing pages (système de templates multiples). | Dev Django, Designer | Haute |
| Implémenter Tailwind CSS (design system). | Designer, Dev Django | Haute |
| Composants réutilisables (hero, CTA, formulaires). | Designer, Dev Django | Haute |
| Analytics et tracking (taux de conversion). | Data Analyst, Dev Django | Moyenne |
| Éditorial anti-détection sur contenus landing (si besoin). | Rédacteur | Moyenne |
| Exposer score / qualité dans l’admin (Prospect, campagnes). | Dev Django, Data Analyst | Basse |

---

## 5. Ordre recommandé « avant que tout fonctionne bien »

1. **URGENT — Git init + remotes** : exécuter la tâche DevOps `2025-01-30-devops-git-init-remotes.md` (GitHub origin + GitLab gitlab). Environnement choisi : **Docker web** (port 8000).
2. **Montage projet** : routes /campaigns/ + écrans /essais/ supplémentaires + branchement logique métier (intelligence) dans les vues.
3. **Livrables P4S-archi** : rapport SEO + étude Growth + première landing (une fois les écrans et routes de base en place).
4. **Design / UX** : vérification Designer sur /essais/, puis Tailwind et composants.

---

## Références

- **TODO** : `docs/TODO.md`
- **Segmentations** : `docs/base-de-connaissances/segmentations/`
- **Routes back** : `docs/base-de-connaissances/routes-back-lppp.md`
- **Prêt à démarrer** : `docs/base-de-connaissances/pret-a-demarrer.md`

---

*Document créé pour synthétiser ce qui reste à faire avant que tout fonctionne bien. À mettre à jour avec le Chef de Projet.*
