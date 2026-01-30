# Spécialiste workflows N8N et automatisation — info pour l'équipe

**Rôle** : **Automatizer** (workflows N8N, Flowise, MCP, API, automatisation).  
**Objectif** : Donner à chaque membre de l'équipe qui en a besoin les **références et le contexte** pour collaborer avec ce rôle (qui fait quoi, quand le solliciter, quelles ressources).

---

## 1. Qui est l'Automatizer ?

- **Expertise** : N8N, Flowise (LLM et big data), MCP, flux d'API en Python/Django, développement et maintenance des workflows, monitoring, optimisation des tokens, traces de performances pour rapports data-driven.
- **Responsabilités** : Développer, maintenir et actualiser tous les workflows (N8N, Flowise, webhooks Django, tâches Celery, MCP) ; corriger les bugs du monitoring ; optimiser la consommation des tokens ; fournir des traces de performances (latence, débit, taux d'erreur, coût estimé).
- **Règle Cursor** : `.cursor/rules/automatizer.mdc`  
- **Fiche détaillée** : `docs/base-de-connaissances/agents-roles-responsabilites.md` § **Automatizer (rôle 9)**.

---

## 2. Quand le solliciter (par rôle)

| Rôle | Quand solliciter l'Automatizer | Exemples |
|------|--------------------------------|----------|
| **Growth** | Pipelines d'enrichissement (n8n, Flowise), OSINT, intégration des sources avec les workflows ; besoin de nouveaux nœuds ou de modifier un workflow d'enrichissement. | "On ajoute une source Clearbit dans le workflow N8N", "Le batch enrich ne respecte pas le rate limit" |
| **DevOps** | Déploiement des conteneurs n8n/flowise, variables d'environnement (`N8N_*`, `FLOWISE_*`), logs (`make n8n-logs`, `make flowise-logs`), ports (5678, 3000). | "N8N ne démarre pas en prod", "Où mettre les secrets pour Flowise ?" |
| **Dev Django** | API webhook (`/api/enriched/enrich`, `/api/enriched/enrich-one`), contrat des payloads, tâches Celery appelées depuis N8N/Flowise, évolution du backend pour les workflows. | "Le webhook renvoie 400", "N8N doit envoyer un nouveau champ" |
| **Pentester** | Sécurité des flux (isolation API enrich, Flowise, n8n), pas de fuite de données, validation des entrées/sorties des workflows. | "Vérifier que les credentials ne sortent pas des workflows", "Rate limiting côté Django et N8N" |
| **Chef de Projet** | Priorisation des évolutions workflows, specs de flux, validation des livrables (workflows, traces de performances). | "Quel workflow en premier ?", "Rapport de performances des runs d'enrichissement" |
| **Data Analyst** | Traces de performances (latence, débit, taux d'erreur, coût estimé) pour les rapports data-driven et les statistiques. | "Métriques d'enrichissement pour le tableau de bord", "Coût moyen par prospect enrichi" |

---

## 3. Ressources partagées

- **Enrichissement et guide-rails** : `docs/base-de-connaissances/enrichissement-osint-flowise-n8n.md` — API webhook, rate limiting, limites batch, pilotage N8N/Flowise.
- **Routes back (webhooks)** : `docs/base-de-connaissances/routes-back-lppp.md` — `EnrichWebhookView`, `/api/enriched/enrich`, `/api/enriched/enrich-one`.
- **Stratégie opérationnelle Make** : `docs/base-de-connaissances/strategie-operationnelle-make.md` — `make n8n-logs`, `make flowise-logs`, démarrage n8n/flowise.
- **Infra** : `docs/base-de-connaissances/infra-devops.md` — services n8n (5678), flowise (3000), variables `N8N_*`, `FLOWISE_*`.
- **Sécurité des flux** : `docs/base-de-connaissances/politique-credentials-securite-flux.md`, `docs/base-de-connaissances/regles-securite.md`.

---

## 4. En résumé

- **Workflows N8N / Flowise / automatisation** → **Automatizer** est le responsable (développement, maintenance, correctifs, optimisation tokens, traces de performances).
- **Growth, DevOps, Dev Django, Pentester** : le **consulter** pour tout ce qui touche aux workflows, aux webhooks et à l’infra n8n/flowise.
- **Chef de Projet, Data Analyst** : le solliciter pour les specs de flux, la priorisation et les métriques/rapports data-driven.

*Document créé pour informer l’équipe du rôle Automatizer (spécialiste N8N et automatisation). À tenir à jour avec le Chef de Projet et l’Orchestrateur.*
