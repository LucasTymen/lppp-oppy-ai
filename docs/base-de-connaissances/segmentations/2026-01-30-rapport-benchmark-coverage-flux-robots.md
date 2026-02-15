# Rapport benchmark — Coverage, flux et actions des robots (feature chatbot)

**Date** : 2026-01-30  
**Objectif** : Mesure data-driven des résultats de la feature chatbot (landing agents municipaux), de l’intégration et des flux ; preuves que le mécanisme fonctionne et premières métriques.

**Public** : Chef de Projet, Architecte, Automatizer, Pentester, Assistant. Tous les agents exécutent les tests de couverture et contribuent à ce rapport.

---

## 1. Métriques à collecter

### 1.1 Couverture de code (coverage)

| Métrique | Description | Cible | Comment mesurer |
|----------|-------------|--------|------------------|
| **Couverture globale apps/** | % de lignes exécutées par les tests (pytest-cov) | Viser 100 % sur les modules de la feature | `make test-cov` → rapport terminal + `htmlcov/index.html` |
| **Couverture flowise_client** | get_flowise_config, get_flowise_chat_embed_url, push_file_to_flowise | 100 % | Rapport coverage sur `apps/scraping/flowise_client.py` |
| **Couverture vues concierge** | concierge_maisons_alfort_public, landing_public (template_key concierge), ConciergeChatView | 100 % | Rapport coverage sur `apps/landing_pages/views.py`, `apps/landingsgenerator/views.py` |
| **Nombre de tests** | Total de tests passants | Augmenter à chaque livrable | `pytest apps/ -v` → count |

**Commande** : depuis la racine du projet (après `pip install -r requirements-test.txt`) :

```bash
make test-cov
# Puis ouvrir htmlcov/index.html pour le détail par fichier.
```

---

### 1.2 Flux (n8n, Flowise)

| Métrique | Description | Preuve / mesure |
|----------|-------------|------------------|
| **Nombre de workflows n8n exécutés** | Exécutions du workflow Conciergerie (aspiration Maisons-Alfort, push vers Flowise) | n8n → Historique des runs ; ou log dédié si mis en place |
| **Nombre de chatflows Flowise actifs** | Chatflows déployés et répondant (ex. Conciergerie Maisons-Alfort) | Flowise → liste des chatflows ; test manuel ou API /api/v1/prediction/{id} |
| **Nombre de requêtes embed servies** | Pages vues avec iframe chatbot (landing /p/maisons-alfort/, /essais/concierge/) | Logs Django (requêtes GET) ou analytics si ajouté ; ou comptage manuel pendant la phase de test |
| **Nombre de prédictions Flowise** | Appels à l’API de prédiction (questions posées dans le chat) | Flowise logs ou métriques si exposées ; ou test manuel (N questions = N prédictions) |

**Stratégie non destructive** : ne pas réinitialiser les runs n8n ni les chatflows ; noter les compteurs avant/après une session de test pour dériver les delta.

---

### 1.3 Actions des robots (preuves de fonctionnement)

| Action | Description | Preuve |
|--------|-------------|--------|
| **Django sert l’URL d’embed** | La vue fournit `flowise_embed_url` au template | Test unitaire (contexte) + test manuel : page contient l’iframe avec la bonne URL |
| **Flowise répond sur /embed/{id}** | L’iframe charge le chat et l’utilisateur peut envoyer un message | Test manuel : ouvrir `http://localhost:3010/embed/{FLOWISE_CHATFLOW_ID}` → chat visible et répond |
| **Landing affiche le chatbot** | /p/maisons-alfort/ affiche l’iframe et le chat répond | Test manuel + test automatisé (contenu HTML contient flowise_embed_url) |
| **Push de documents vers Flowise** | Commande ou API pousse un fichier au Document Store | Test unitaire (mock) + test d’intégration optionnel (fichier test → Flowise) |

---

## 2. Template du rapport (à remplir par l’équipe)

### 2.1 Session du __________ (date)

**Environnement** : Docker LPPP / local (préciser). Branche Git : __________

#### Coverage

| Fichier / module | Couverture % | Lignes non couvertes (optionnel) |
|------------------|--------------|-----------------------------------|
| apps/scraping/flowise_client.py | ___ % | |
| apps/landing_pages/views.py (concierge + landing_public) | ___ % | |
| apps/landingsgenerator/views.py | ___ % | |
| **Total apps/ (ou sous-ensemble feature)** | ___ % | |

**Nombre de tests** : ___ passants, ___ échoués, ___ skip.

**Objectif 100 %** : [ ] Atteint sur les modules feature / [ ] En cours (lister les écarts).

#### Flux

| Métrique | Valeur (avant session) | Valeur (après session) | Delta |
|----------|------------------------|------------------------|-------|
| Runs n8n (workflow Conciergerie) | | | |
| Requêtes GET /p/maisons-alfort/ (ou /essais/concierge/) | (optionnel) | | |
| Prédictions Flowise (optionnel) | | | |

#### Actions des robots (checklist)

- [ ] Django sert `flowise_embed_url` dans le contexte (test automatisé OK).
- [ ] Page /p/maisons-alfort/ affiche l’iframe et le chat (test manuel OK).
- [ ] Flowise répond sur /embed/{id} (test manuel OK).
- [ ] Push document vers Flowise (test unitaire ou intégration OK).

#### Incidents / remarques

_(Libre)_

---

## 3. Commandes de référence

```bash
# Installer les deps de test (une fois)
pip install -r requirements-test.txt

# Lancer les tests avec couverture
make test-cov

# Rapport HTML détaillé
make coverage-report
# Puis ouvrir htmlcov/index.html

# Tests + coverage dans Docker (DB dispo → tous les tests)
make test-cov-docker

# Tests dans Docker (sans coverage si pytest-cov non installé dans l’image)
make test-docker
```

---

## 4. Rôles et responsabilités

| Rôle | Contribution au benchmark |
|------|---------------------------|
| **Tous les agents** | Exécuter `make test-cov-docker` (PostgreSQL dans le conteneur ; pas de SQLite). Remonter les résultats (coverage %, échecs), ne pas casser les tests existants. |
| **Architecte** | Vérifier que les métriques (coverage, flux) reflètent bien la chaîne d’intégration (Django → Flowise → embed) ; proposer des seuils ou objectifs. |
| **Automatizer** | Fournir les chiffres ou méthodes pour « nombre de flux n8n », « prédictions Flowise » si disponibles ; documenter comment les relever sans impact destructif. |
| **Pentester** | Valider que les tests et le rapport n’exposent pas de données sensibles ; confirmer que les preuves (logs, métriques) sont conformes à la sécurité. |
| **Assistant / Chef de Projet** | Remplir le template du rapport (§ 2) après chaque session significative ; mettre à jour ce document avec les premiers métriques et objectifs 100 % coverage sur la feature. |

---

## 5. Références

- **Feature chatbot** : `segmentations/2026-01-30-feature-chatbot-landing-agents-municipaux.md`
- **Tests** : `apps/scraping/tests/test_flowise_client.py`, `apps/landing_pages/tests/test_views_concierge.py`, `apps/landingsgenerator/tests/test_views_concierge.py`
- **Configuration tests** : `pytest.ini`, `.coveragerc`, `requirements-test.txt`
- **Makefile** : `make test-cov`, `make test-cov-docker`, `make coverage-report`

---

*Document créé pour le benchmark data-driven de la feature chatbot. Dernière mise à jour : 2026-01-30.*
