# Definition of Done — LPPP

**Rôle** : Règle partagée pour considérer qu’une **tâche** ou une **étude** est « terminée » (done).  
**Consommé par** : Chef de Projet (validation), tous les agents (livrables).

---

## 1. Tâche technique (code, config, déploiement)

Une tâche technique est **done** quand :

- Le **livrable** est livré (code, config, migration, template, etc.) dans le dépôt ou à l’emplacement prévu.
- **Pas de régression connue** : les fonctionnalités existantes concernées n’ont pas été cassées (tests passants si applicable).
- La **documentation impactée** est à jour : `routes-back-lppp.md`, segmentations, registre, etc., si la tâche les concerne.
- Le **Chef de Projet** a validé (ou la segmentation précise que la validation est implicite pour cette tâche).

---

## 2. Étude ou rapport (Growth, Growth Analyst, Expert SEO, Data Analyst)

Une étude ou un rapport est **done** quand :

- Le **livrable** est déposé au bon endroit (ex. `docs/contacts/<slug>/etude-growth-funnel-kpis.md`, `rapport-seo.md`).
- Le format respecte le cadre défini (ex. `growth-etude-funnel-kpis.md`, `growth-analyst-concurrentiel-marche-ads.md`).
- Le **Chef de Projet** (ou le rôle Accountable selon la RACI) a validé ou pris connaissance pour intégration.

---

## 3. Segmentation / feature

Une **segmentation** (feature) est **done** quand :

- Toutes les tâches listées dans la segmentation sont **done** selon les critères ci-dessus.
- Les **critères de validation** de la segmentation sont remplis (voir TEMPLATE et chaque segmentation).
- Le **Chef de Projet** a validé la feature et mis à jour les logs / TODO / reste-a-faire.

---

## Références

- **Template segmentation** : `docs/base-de-connaissances/segmentations/TEMPLATE.md` (critères de validation).
- **Coordination** : `.cursor/rules/coordination-agents.mdc`.
- **RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md`.
- **Checklist pré-prod** : `docs/base-de-connaissances/checklist-pre-prod-integrite.md` (qualité, intégrité, fonctionnel avant push prod ; Chef de Projet pilote).

---

*Document créé à l’issue de la réunion agile organisation équipe (2025-01-30). À référencer dans le TEMPLATE et la coordination.*
