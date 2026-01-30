# Stratégie d’enrichissement LPPP

Document de référence pour l’enrichissement des prospects (OSINT, contournement blocages Google/LinkedIn). Aligné avec les règles du projet (anti-hallucination, data-driven).

---

## 1. Conteneur quali Linux (Kali)

- **Le conteneur Kali Linux** (`kalilinux` dans `docker-compose.yml`, profil `full`) est le **conteneur quali** (quality Linux) sur lequel repose une grande partie de la stratégie d’enrichissement.
- Il fournit l’environnement et les outils (OSINT, réseau, etc.) utilisés pour les tâches d’enrichissement. **Ne pas l’oublier** : les pipelines et la doc doivent y faire référence.
- Démarrage : `docker compose --profile full up -d` pour lancer **enriched** et **kalilinux**.
- Référence : `docker-compose.yml` (services `enriched`, `kalilinux`), `docker/Dockerfile.enriched`.

---

## 2. Anti-blocage Google / LinkedIn (leçon SquidResearch)

- En production, la stratégie SquidResearch **a échoué** lorsque tous les outils étaient utilisés ensemble (blocage systématique par Google ou LinkedIn).
- Elle **fonctionnait bien** lorsque les outils étaient utilisés **indépendamment**, élément par élément.
- **Principe retenu pour LPPP** : **conserver ce fonctionnement** — chaque tâche est décomposée et lance **une instance d’un seul outil** à la fois. Les données sont ensuite **restaurées / fusionnées** avec la collaboration de l’**agent chargé de l’intelligence métier** (`apps.intelligence`).

---

## 3. Flux décomposé (une tâche = un outil)

1. **Décomposition** : pour un prospect donné, au lieu d’un seul job qui appelle toutes les sources d’un coup, on lance **une tâche Celery par source** (une tâche = un outil / une source OSINT).
2. **Exécution** : chaque tâche (`enrich_prospect_single_source`) appelle **une seule source**, écrit le résultat partiel (ex. Redis), puis se termine.
3. **Restoration / fusion** : une tâche dédiée (`enrich_prospect_merge_and_save`) agrège les résultats partiels, appelle l’**intelligence métier** (qualité, scoring dans `apps.intelligence`), puis enregistre `enriched_data` sur le modèle `Prospect`.
4. **Orchestration** : on peut lancer d’un coup le flux décomposé via `enrich_prospect_decomposed(prospect_id, source_names)` qui enchaîne les tâches une par une puis déclenche le merge.

Cela limite les patterns « bot » détectés par Google/LinkedIn et évite les blocages en prod.

---

## 4. Rôle de l’agent intelligence métier

- **`apps.intelligence`** : qualité (`prospect_completeness`), scoring (`score_prospect`), normalisation.
- **Collaboration** : les résultats bruts des sources OSINT (une par tâche) sont fusionnés ; la **fusion et le calcul qualité/score** sont faits dans la tâche de merge, qui s’appuie sur `apps.intelligence.quality` et `apps.intelligence.scoring`.
- Les agents (DevOps, métier) doivent s’assurer que le flux décomposé et l’intelligence métier restent alignés (même schéma de données, même contrat `enriched_data`).

---

## 5. Récapitulatif

| Élément | Rôle |
|--------|------|
| **Conteneur Kali (quali)** | Environnement et outils d’enrichissement ; central à la stratégie. |
| **Une tâche = un outil** | Éviter les blocages Google/LinkedIn ; exécution élément par élément. |
| **Résultats partiels** | Stockage temporaire (ex. Redis) par prospect et par source. |
| **Tâche merge + intelligence** | Fusion des partiels, qualité, score, sauvegarde sur `Prospect`. |
| **`apps.intelligence`** | Qualité et scoring ; collaboration avec le flux d’enrichissement. |

---

*Dernière mise à jour : 2025-01-30. Source : retour d’expérience SquidResearch en prod, docker-compose LPPP, apps.scraping.enriched, apps.intelligence.*
