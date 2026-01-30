# SEO sémantique — outils gratuits / open-source (Python)

Document de référence pour l’**Expert SEO / AI-GEO** et la coordination avec **DevOps** et **Développeur Django** (architecture, intégration). Stack 100 % gratuite et open-source : keyword-to-topic, topic modelling, clustering sémantique, similarité.

**Pilote fonctionnel** : Expert SEO / AI-GEO.  
**Pilotes technique / infra** : Dev Django (code, intégration dans l’app), DevOps (environnement, Docker, dépendances optionnelles).

---

## 1. Principe

Il ne s’agit pas d’un logiciel SEO prêt à l’emploi mais d’un **stack de bibliothèques Python** à intégrer dans les workflows (scripts, commandes Django, notebooks) :

- **Keyword-to-topic / Topic modelling** : regrouper mots-clés et textes par thèmes.
- **Extraction de thèmes** : identifier les sujets dominants dans un corpus (landing, contenus prospect).
- **Clustering sémantique** : grouper textes ou requêtes par similarité.
- **Analyses de similarité** : rapprocher contenus, mots-clés, intentions.

Ce n’est pas du « SEO out-of-the-box » ; des **notebooks et exemples communautaires** montrent comment faire du topic modelling orienté SEO avec ces libs.

---

## 2. Stack recommandée (Python, open-source)

| Bibliothèque | Rôle | Licence |
|--------------|------|---------|
| **spaCy** | NLP, entités, tokens, lemmatisation, POS | MIT |
| **Gensim** | Topic modelling (LDA, etc.), similarité documentaire | LGPL |
| **NLTK** | Traitement linguistique (tokenize, stopwords, stemmers) | Apache 2.0 |
| **Transformers (Hugging Face)** | Embeddings, modèles sémantiques (sentence-transformers) | Apache 2.0 |

### Utilisation typique

- **spaCy** : prétraitement (tokens, entités, langue), préparation du corpus pour LDA / embeddings.
- **Gensim** : LDA (topic modelling), similarité cosinus entre documents, dictionnaire et corpus.
- **NLTK** : compléments (stopwords multilingues, tokenizers, stemmers) si besoin.
- **Transformers / sentence-transformers** : embeddings pour similarité sémantique (plus lourd en ressources ; optionnel selon l’environnement).

---

## 3. Dépendances projet LPPP

- **Fichier optionnel** : `requirements-seo.txt` à la racine du projet.
- **Intégration** : décidée en accord avec **DevOps** (build Docker, images) et **Dev Django** (emplacement du code : app dédiée, commandes management, ou scripts dans `scripts/` documentés).
- **Installation locale (hors Docker)** : `pip install -r requirements-seo.txt` dans un venv dédié si besoin (pour ne pas alourdir l’env principal avant intégration).
- **Docker** : si le stack SEO sémantique est intégré dans le flux (ex. tâche Celery ou commande Django), DevOps peut inclure `requirements-seo.txt` dans le Dockerfile (multi-stage ou cible dédiée) pour limiter la taille de l’image prod si nécessaire.

---

## 4. Où mettre le code

- **Expert SEO** : définit les cas d’usage (entrées/sorties, métriques), s’appuie sur la doc et les notebooks communautaires pour la méthodologie.
- **Dev Django** : intègre les appels (module dans `apps/`, ex. `apps.seo_semantic` ou sous-module dans une app existante), commandes `manage.py`, ou scripts documentés dans `scripts/` (voir bonnes pratiques projet : pas de scripts one-shot laissés à la racine).
- **DevOps** : valide l’impact sur l’image Docker, le temps de build, les éventuelles variables d’environnement (modèles Hugging Face, cache).

---

## 5. Ressources externes (notebooks, tutos)

- **Topic modelling SEO** : chercher « topic modelling SEO Python », « keyword clustering LDA Gensim », « semantic keyword grouping » (GitHub, Kaggle, Medium).
- **spaCy** : [spacy.io](https://spacy.io) — modèles de langue (`fr_core_news_sm`, `en_core_web_sm`) à télécharger séparément.
- **Gensim** : [radimrehurek.com/gensim](https://radimrehurek.com/gensim) — LDA, LSI, similarité.
- **Hugging Face** : [huggingface.co](https://huggingface.co) — `sentence-transformers` pour embeddings légers (ex. `all-MiniLM-L6-v2`).

---

## 6. Collaboration Expert SEO ↔ DevOps ↔ Dev Django

| Qui | Rôle |
|-----|------|
| **Expert SEO / AI-GEO** | Spécifier les besoins (keyword-to-topic, thèmes, similarité), utiliser le stack dans des notebooks/scripts pour analyses et rapports lead magnet ; s’appuyer sur cette doc. |
| **Dev Django** | Intégrer le code dans l’app (module, commandes, appels depuis vues ou tâches Celery si besoin) ; respecter la structure du projet (apps/, scripts/). |
| **DevOps** | Gérer les dépendances (`requirements-seo.txt`), l’image Docker (optionnel), le cache des modèles (Hugging Face) si pertinent ; documenter dans `infra-devops.md`. |

Pour toute évolution du stack (nouvelles libs, version Python, conteneur dédié) : **accord avec DevOps et Chef de Projet** avant modification des fichiers d’environnement ou du Dockerfile.

---

## 7. Références projet

- **Registre** : `docs/base-de-connaissances/registre-agents-ressources.md` (Expert SEO, DevOps, Dev Django).
- **Rôles et RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md` (tâche « Intégrer / maintenir stack SEO sémantique »).
- **Règle Expert SEO** : `.cursor/rules/expert-seo-ai-geo.mdc`.
- **Infra** : `docs/base-de-connaissances/infra-devops.md` (§ Stack optionnel SEO sémantique).
- **Dépendances optionnelles** : `requirements-seo.txt` (racine du projet).

---

*Document maintenu par l’Expert SEO / AI-GEO en coordination avec DevOps et Dev Django. Dernière mise à jour : 2025-01-30.*
