# Montage du projet — écrans, concordance des routes back, logique métier

**Sprint** : voir `2025-01-30-sprint-equipe-technique.md` (toute l'équipe technique mobilisée).  
**Date** : 2025-01-30  
**Statut** : 🟢 À lancer (environnement et admin opérationnels)  
**Objectif** : Mettre en place toutes les fonctionnalités en coordonnant les **orchestrateurs**, l’agent **logique métier / algorithmes**, le **Dev Django** et le **DevOps** : écrans, concordance des routes dans le back, branchement de la logique métier.

---

## Pilotes et rôles

| Pilote | Rôle | Tâches clés |
|--------|------|-------------|
| **Orchestrateur** | Registre, stratégie, alignement | Mettre à jour le registre et les segmentations ; s’assurer que Chef de Projet, Dev Django, DevOps, Data Analyst ont les bonnes références (registre, `routes-back-lppp.md`, `intelligence-metier-algorithmes.md`). |
| **Chef de Projet** | Coordination, priorités | Valider les specs écrans et routes ; répartir les tâches ; maintenir TODO et cette segmentation. |
| **Data Analyst** (logique métier / algorithmes) | Scoring, qualité, matching | Brancher `apps.intelligence` sur les écrans et les données ; documenter dans `intelligence-metier-algorithmes.md` ; fournir les points d’entrée pour Dev Django. |
| **Dev Django** | Écrans, vues, URLs | Implémenter les écrans (landingsgenerator, landing_pages, campaigns) ; assurer la **concordance des routes** (voir `routes-back-lppp.md`) ; connecter les vues à la logique métier. |
| **DevOps** | Infra, cohérence back | Vérifier que static, WSGI servent correctement les routes ; pas de régression sur admin/essais ; déploiement cohérent. |

---

## 1. Concordance des routes (back)

Référence détaillée : **`docs/base-de-connaissances/routes-back-lppp.md`**.

Résumé actuel : `/admin/`, `/` (liste landings), `/p/<slug>/` (page publique), `/essais/` (index relance salon), `/campaigns/` (à définir), `/api/enriched/...` (webhooks enrichissement).

**Tâche Dev Django** : tenir à jour `routes-back-lppp.md` à chaque ajout de route ; implémenter les vues et URLs manquantes pour les écrans validés.

---

## 2. Écrans à mettre en place (priorité)

- [ ] **/essais/** : index relance salon en place ; ajouter les écrans suivants selon specs Chef de Projet.
- [ ] **/campaigns/** : définir et implémenter les routes (liste, détail, CRUD si besoin).
- [ ] **Landing pages** : `/` et `/p/<slug>/` en place ; enrichir si besoin (scoring/matching).
- [ ] **Admin** : cohérence modèles (campagnes, prospects, landing pages) avec la logique métier.

---

## 3. Logique métier et algorithmes

Référence : **`docs/base-de-connaissances/intelligence-metier-algorithmes.md`**.

**Data Analyst** : Exposer les points d’entrée utilisés par les écrans (`score_prospect()`, `prospect_completeness()`, `best_landing_for_prospect()`). Documenter seuils et formules. Brancher les nodes sur l’intelligence.

**Dev Django** : Utiliser `apps.intelligence` dans les vues (scores, matching, qualité). Ne pas dupliquer la logique.

---

## 4. Ordre d’exécution suggéré

1. Orchestrateur / Chef de Projet : valider cette segmentation, mettre à jour registre et TODO.
2. Dev Django + DevOps : finaliser la doc concordance des routes (`routes-back-lppp.md`).
3. Data Analyst : documenter les appels intelligence pour les écrans.
4. Dev Django : implémenter écrans et routes manquants (/campaigns/, écrans /essais/ supplémentaires).
5. DevOps : vérifier static, déploiement, pas de régression.

---

## Références

- **Registre** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Routes back** : `docs/base-de-connaissances/routes-back-lppp.md`
- **Logique métier** : `docs/base-de-connaissances/intelligence-metier-algorithmes.md`
- **Interface /essais/** : `docs/base-de-connaissances/segmentations/2025-01-30-interface-landingsgenerator.md`

---

*Segmentation créée pour le montage du projet. Dernière mise à jour : 2025-01-30.*
