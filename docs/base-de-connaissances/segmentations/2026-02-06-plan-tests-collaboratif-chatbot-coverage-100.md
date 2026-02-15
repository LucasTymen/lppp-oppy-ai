# Plan de tests collaboratif — Chatbot landing (coverage 100 %, tests pas à pas)

**Date** : 2026-02-06  
**Objectif** : Corriger les causes et symptômes identifiés, tester pas à pas, viser **100 % de couverture** sur la feature chatbot. Chaque agent réalise les tests qu’il maîtrise ; tous collaborent : chacun peut **contrôler**, **suggérer** aux autres les tests, les résultats attendus et les solutions.

**Commande pour lancer tous les tests + coverage** : `make test-cov-docker` (ou `make test-cov-docker-build` si l’image n’a pas pytest). Rapport HTML : `htmlcov/index.html` après exécution.

**Sous Windows** : exécuter les commandes make depuis **WSL** (dans le répertoire du projet, ex. `cd /mnt/c/home/lucas/tools/homelucastoolsLandingsPagesPourProspections` puis `make test-cov-docker-build` si besoin de rebuild l’image avec pytest).

---

## 1. Répartition des tests par agent (qui maîtrise quoi)

| Agent | Fichiers / domaine | Tests à maîtriser | Résultats attendus |
|-------|--------------------|-------------------|---------------------|
| **Dev Django** | `flowise_client.py`, vues landing, template | `test_flowise_client.py`, `test_views_concierge.py` (landing_pages), `test_views_concierge.py` (landingsgenerator) | Tous passent ; coverage `apps/scraping/flowise_client.py` et `apps/landing_pages/views.py` (branches concierge) à 100 % |
| **DevOps** | Commande diagnostic, env, santé | `test_check_flowise_embed_command.py` | Commande affiche URL / avertissement ; `--ping` ne fait pas crasher |
| **Architecte** | Chaîne route → vue → template, contexte | Tests d’intégration vue + contexte (`flowise_embed_url`, `flowise_api_host`, `flowise_chatflow_id`) | Contexte complet pour template concierge ; pas de 404 sur `/p/maisons-alfort/` |
| **Pentester** | Sécurité : pas de secrets dans le HTML | `test_concierge_template_does_not_expose_secrets_in_html` | Aucun `sk-`, `FLOWISE_API_KEY` dans le HTML rendu |
| **Automatizer** | Client Flowise, config embed, push | `test_flowise_client.py` (get_flowise_config, get_flowise_chat_embed_url, get_flowise_chat_embed_config, push_file_to_flowise) | URL embed correcte (port 3010), config (base_url, chatflow_id) parsée ; push mock OK / erreur selon cas |

Chaque agent peut **suggérer** à un autre un test manquant ou un résultat à vérifier (ex. : « Pentester suggère à Dev Django : ajouter un test que le template ne contient pas de token » → déjà couvert par `test_concierge_template_does_not_expose_secrets_in_html`).

---

## 2. Suite de tests (pas à pas) — ordre recommandé

1. **Client Flowise (scraping)**  
   - `apps/scraping/tests/test_flowise_client.py`  
   - Couvre : `get_flowise_config`, `get_flowise_chat_embed_url`, `get_flowise_chat_embed_config`, `push_file_to_flowise`.  
   - **Résultat attendu** : tous les tests passent ; pas d’appel réseau réel (mocks).

2. **Commande diagnostic (scraping)**  
   - `apps/scraping/tests/test_check_flowise_embed_command.py`  
   - Couvre : `check_flowise_embed` (sortie diagnostic, warning si chatflow vide, `--ping` sans crash).  
   - **Résultat attendu** : tous les tests passent.

3. **Vues landing Conciergerie (landing_pages)**  
   - `apps/landing_pages/tests/test_views_concierge.py`  
   - Couvre : `concierge_maisons_alfort_public`, `landing_public` avec template concierge, contexte (embed_url, api_host, chatflow_id), placeholder si URL vide, script embed si config complète, pas de secrets dans le HTML.  
   - **Résultat attendu** : tous les tests passent ; coverage sur les branches concierge des vues.

4. **Vue Concierge (landingsgenerator)**  
   - `apps/landingsgenerator/tests/test_views_concierge.py`  
   - Couvre : `/essais/concierge/` (anonyme → redirect login, staff → 200 + flowise_embed_url).  
   - **Résultat attendu** : tous les tests passent.

5. **Coverage global**  
   - Lancer `make test-cov-docker` et ouvrir `htmlcov/index.html`.  
   - **Objectif** : 100 % sur les modules concernés par la feature chatbot (`flowise_client.py`, vues et branches concierge, commande `check_flowise_embed`).  
   - Chaque agent peut **suggérer** d’ajouter un test si une branche ou un fichier reste non couvert.

---

## 3. Contrôle et suggestions entre agents

- **DevOps** peut demander à **Dev Django** : « Les tests de la commande `check_flowise_embed` couvrent-ils le cas où Flowise ne répond pas (--ping) ? » → oui (test `test_command_ping_does_not_crash`).  
- **Pentester** peut demander : « Le HTML rendu contient-il des secrets ? » → test dédié `test_concierge_template_does_not_expose_secrets_in_html`.  
- **Architecte** peut demander : « La vue `landing_public` passe-t-elle bien `flowise_api_host` et `flowise_chatflow_id` au template ? » → oui (test `test_landing_maisons_alfort_injects_flowise_embed_url` étendu + tests dédiés).  
- **Automatizer** peut suggérer : « Tester que `get_flowise_chat_embed_config()` renvoie ("", "") si l’URL d’embed est vide » → couvert par `TestGetFlowiseChatEmbedConfig`.  

Chaque agent documente ses suggestions ou constats dans ce document (section 5 ci-dessous) ou dans le sprint `2026-02-06-sprint-controle-flux-chatbot-landing-maisons-alfort.md`.

---

## 4. Corrections déjà appliquées (tests ajoutés / modifiés)

- **flowise_client** : tests pour `get_flowise_chat_embed_config()` (retour vide, parsing base_url + chatflow_id, strip query string).  
- **landing_pages/views** : tests pour contexte `flowise_api_host` et `flowise_chatflow_id`, rendu script embed (Chatbot.init), et **pas de secrets dans le HTML** (Pentester).  
- **Vue concierge** : test adapté (iframe ou Chatbot.init + 3010) selon la branche du template.

---

## 5. Suggestions et résultats à obtenir (à compléter par les agents)

*Chaque agent peut ajouter ici une ligne ou un paragraphe : test suggéré, résultat attendu, ou solution proposée.*

| Agent | Suggestion / test à ajouter | Résultat attendu | Statut |
|-------|------------------------------|------------------|--------|
| *(exemple)* | *Pentester : pas de sk- dans le HTML* | *assert "sk-" not in html* | ✅ Ajouté |
| | | | |
| | | | |

---

## 6. Références

- **Sprint contrôle des flux** : `2026-02-06-sprint-controle-flux-chatbot-landing-maisons-alfort.md`
- **Stratégie chatbot** : `2026-01-30-strategie-chatbot-ecran-vide-et-flux.md`
- **Rapport benchmark coverage** : `2026-01-30-rapport-benchmark-coverage-flux-robots.md`
- **Makefile** : `make test-cov-docker`, `make test-cov-docker-build`
- **Rôles** : `agents-roles-responsabilites.md`, `registre-agents-ressources.md`
