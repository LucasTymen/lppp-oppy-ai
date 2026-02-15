# Contrôle : ce qui bloque le flux + interférences Python / dépendances

**Date** : 2026-02  
**Demande** : Faire contrôler par les équipes concernées ce qui bloque le flux et s’il n’y a pas des interférences entre Python et les dépendances.

**Équipes concernées** : **DevOps** (flux, services, santé), **Dev Django** (Python, dépendances, chaîne vue→template), **Pentester** (CORS / iframe / sécurité flux si besoin).

---

## 1. Périmètre du contrôle

| Qui | Contrôle | Livrable |
|-----|----------|----------|
| **DevOps** | Flux : services (web, flowise, db, redis), ports (8010, 3010), `check_flowise_embed`, IFRAME_ORIGINS/CORS Flowise, logs. | Rapport court « Flux » (OK / blocage identifié) + checklist. |
| **Dev Django** | Python : version, `pip check`, conflits de dépendances, `requirements.txt` vs installé, imports, chaîne landing (vue → contexte → template). | Rapport « Dépendances Python » (OK / conflits) + éventuels correctifs. |
| **Pentester** | Si cadre vide / iframe : CORS, CSP, X-Frame-Options côté Django et Flowise ; pas de secrets dans le HTML. | Note « Sécurité flux » (blocage ou pas). |

---

## 2. Checklist technique (à exécuter)

### 2.1 DevOps — Flux

- [ ] `docker compose ps` → tous les services attendus sont Up (web, flowise, db, redis).
- [ ] `docker compose exec web python manage.py check_flowise_embed` → URL d’embed non vide, pas d’erreur.
- [ ] `docker compose exec web python manage.py check` → aucune erreur Django.
- [ ] Flowise : `IFRAME_ORIGINS` et `CORS_ORIGINS` présents dans l’environnement du conteneur flowise (docker-compose).
- [ ] Depuis l’hôte : `curl -s -o /dev/null -w "%{http_code}" http://localhost:3010/` → 200 ou 302.
- [ ] Logs : `docker compose logs web --tail 30` et `docker compose logs flowise --tail 30` sans erreur critique.

### 2.2 Dev Django — Python et dépendances

- [ ] `pip check` (dans l’environnement du projet ou dans le conteneur web) → aucune incohérence signalée.
- [ ] `pip list` vs `requirements.txt` : versions installées compatibles avec les plages déclarées.
- [ ] Aucun `ImportError` ou conflit de namespace au démarrage (gunicorn, celery) ou lors des tests.
- [ ] Chaîne landing : `landing_public` (slug maisons-alfort) → template `proposition` → contexte `flowise_embed_url`, `content` ; pas de VariableDoesNotExist.

### 2.3 Pentester — Sécurité des flux

- [ ] Aucun secret (FLOWISE_API_KEY, etc.) dans le HTML/JS de la page `/p/maisons-alfort/`.
- [ ] CORS / CSP : pas de blocage côté navigateur pour l’iframe Flowise (ou blocage documenté avec mesure corrective).

---

## 3. Résultats des contrôles (exécution 2026-02)

*Contrôles exécutés dans le conteneur web (et sur l’hôte pour docker compose ps).*

### 3.1 Résultats DevOps (flux)

| Vérification | Résultat |
|--------------|----------|
| `docker compose ps` | Tous les services **Up** : lppp_web (8010:8000), lppp_flowise (3010:3000), lppp_db (5433:5432), lppp_redis (6380:6379), lppp_celery, lppp_celery_beat, lppp_n8n (5681:5678). |
| `python manage.py check` | **Aucune issue** (0 silenced). |
| `python manage.py check_flowise_embed` | **URL d’embed construite** : `http://localhost:3010/embed/67206a96-470e-4607-ba8b-5955e97aa116`. FLOWISE_URL et FLOWISE_CHATFLOW_ID vides en env → valeurs par défaut utilisées. |
| Flowise IFRAME_ORIGINS / CORS | Présents dans `docker-compose.yml` (IFRAME_ORIGINS: "*", CORS_ORIGINS: "*"). Redémarrer Flowise après modification : `docker compose up -d flowise`. |

**Conclusion DevOps** : Aucun blocage flux identifié côté services ni côté construction de l’URL d’embed. Si l’iframe reste vide, vérifier que Flowise a bien été redémarré avec les variables d’environnement (IFRAME_ORIGINS / CORS_ORIGINS) et que le navigateur peut joindre http://localhost:3010.

### 3.2 Résultats Dev Django (Python / dépendances)

| Vérification | Résultat |
|--------------|----------|
| `pip check` | **No broken requirements found.** Aucune incohérence de dépendances. |
| Versions (ex.) | Django 5.2.11 (dans plage requirements >=5.0,<6), gunicorn 22.0.0, celery 5.6.2, psycopg 3.3.2, pandas 2.3.3, pytest 9.0.2 — toutes compatibles avec `requirements.txt`. |
| `pytest apps/` | **28 passed**, 1 warning (option pytest django_settings). Aucun échec, aucun ImportError. |
| Chaîne landing | Vue `landing_public` → template `proposition` (ou concierge selon slug) ; contexte `flowise_embed_url`, `content` avec `_content_with_defaults` — pas de VariableDoesNotExist côté clés hero. |

**Conclusion Dev Django** : Aucune interférence détectée entre Python et les dépendances. Dépendances cohérentes, tests verts.

### 3.3 Résultats Pentester (sécurité flux)

| Vérification | Résultat |
|--------------|----------|
| Secrets dans les templates landing | **Aucun** : pas de FLOWISE_API_KEY, password ni api_key dans les templates (grep sur `templates/landing_pages`). Seuls `flowise_embed_url`, `flowise_api_host`, `flowise_chatflow_id` (nécessaires à l’embed) sont exposés. |

**Conclusion Pentester** : Pas d’exposition de secrets dans le HTML/JS. CORS/iframe : config Flowise (IFRAME_ORIGINS / CORS_ORIGINS) à maintenir pour autoriser l’embed depuis la landing.

---

## 4. Références

- **Diagnostic chatbot** : `flowise-chatbot-ecran-vide-diagnostic.md`
- **Sprint contrôle flux** : `2026-02-06-sprint-controle-flux-chatbot-landing-maisons-alfort.md`
- **Erreurs et solutions** : `erreurs-et-solutions.md`
- **Code** : `apps/landing_pages/views.py`, `apps/scraping/flowise_client.py`, `requirements.txt`, `docker-compose.yml`
