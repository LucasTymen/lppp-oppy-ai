# Bibliothèques spécialisées — besoins des agents techniques

**Rôle** : Tour des outils dont ont besoin les agents techniques pour traiter les données, rendre les rapports plus visuels et scraper, **sans overkill**.  
**Pilote** : Chef de Projet, DevOps (intégration des deps).  
**Référence** : `requirements.txt`, `requirements-seo.txt`, `agents-roles-responsabilites.md`.

---

## 1. État des lieux (déjà en place)

| Besoin | Bibliothèque actuelle | Utilisé par |
|--------|------------------------|-------------|
| Requêtes HTTP | `requests` | Growth, scraping, APIs |
| Scraping HTML | `beautifulsoup4`, `lxml` | Growth, Pentester, pipelines enrichissement |
| SEO sémantique (NLP, topic modelling) | `requirements-seo.txt` : spaCy, Gensim, NLTK, transformers, sentence-transformers | Expert SEO (optionnel) |
| Backend / BDD | Django, psycopg, redis, celery | Dev Django, Data Analyst, tous |

**Manquant** (documenté ou utile) :
- **Traitement CSV / données structurées** : rapport SEO (Screaming Frog), imports, agrégations — pas de lib dédiée dans `requirements.txt`.
- **Calcul / tableaux** : Data Analyst (fiche rôle : pandas, numpy, PostgreSQL analytics) — pandas/numpy non installés.
- **Rendu visuel des données** : rapport SEO « sexy », KPIs, funnel — pas de lib de viz dans le projet (éviter d’ajouter trop de dépendances).

---

## 2. Besoins par agent technique

### Data Analyst / Data Engineer

- **Actuel** : `apps/intelligence/` (scoring, quality, matching) — stdlib uniquement (ast, operator, re).
- **Utile** : **pandas** (CSV, agrégations, analytics, exports), **numpy** (calculs, stats si extension des algorithmes). Déjà cité dans la fiche rôle.
- **Viz** : pas obligatoire en lib Python ; rapports via templates HTML / tableaux générés depuis pandas.

### Expert SEO / AI-GEO

- **Actuel** : `requirements-seo.txt` (spaCy, Gensim, NLTK, transformers) pour l’analyse sémantique.
- **Utile** : **pandas** pour lire et croiser les CSV Screaming Frog, agréger les métriques, préparer les données du rapport (manque à gagner, coût SEO pourri).
- **Viz** : rapport « sexy » = HTML/CSS (templates Django) + tableaux/chiffres clés issus de pandas ; pas de matplotlib/plotly en première phase (éviter overkill).

### Growth Hacker / OSINT

- **Actuel** : `requests`, `beautifulsoup4`, `lxml` — suffisant pour le scraping documenté.
- **Utile** : **pandas** pour études funnel/KPIs (agrégations, séries temporelles si besoin), cohérence avec Data Analyst et Expert SEO.
- **Scraping** : rien à ajouter (Beautiful Soup couvre le besoin).

### Dev Django

- **Actuel** : Django, apps, pas de traitement CSV dans le code actuel.
- **Utile** : **pandas** (et éventuellement numpy) si intégration de commandes management ou de vues pour rapport SEO (lecture CSV → génération rapport).

### Pentester (spécialisation Growth)

- **Actuel** : même stack que Growth (scraping, enriched).
- **Utile** : aucune lib supplémentaire identifiée.

---

## 3. Proposition consolidée (sans overkill)

### À ajouter dans `requirements.txt`

| Bibliothèque | Rôle | Utilisateurs |
|--------------|------|--------------|
| **pandas** | CSV, tableaux, agrégations, préparation données (rapport SEO, analytics, KPIs) | Data Analyst, Expert SEO, Growth, Dev Django |
| **numpy** | Calculs, stats (optionnel mais léger et souvent utilisé avec pandas) | Data Analyst, Expert SEO (analyses avancées) |

**Versions** : pandas>=2.0,<3 ; numpy>=1.24,<3 (compatibles Django 5, Python 3.10+).

### Non ajouté (pour l’instant)

- **Visualisation** (matplotlib, seaborn, plotly) : rapports « visuels » via **templates HTML + données préparées avec pandas** (tableaux, cartes, chiffres clés). Si besoin de graphiques plus tard, ajouter une seule lib (ex. plotly pour rapports interactifs) après validation.
- **Autres libs scraping** (Scrapy, etc.) : Beautiful Soup + lxml suffisent pour le périmètre actuel.
- **Scikit-learn / autres ML** : pas de besoin identifié ; stack SEO sémantique (requirements-seo.txt) couvre NLP/topic modelling.

### Déjà en place, à conserver

- **Scraping** : `requests`, `beautifulsoup4`, `lxml`.
- **SEO sémantique** : `requirements-seo.txt` (spaCy, Gensim, NLTK, transformers) — optionnel, installé à part ou intégré au Docker selon accord DevOps.

---

## 4. Résumé

- **Ajout minimal** : **pandas** + **numpy** dans `requirements.txt` pour couvrir traitement CSV, analytics, rapport SEO et études Growth/Data Analyst.
- **Visuel** : rendu des données via HTML/templates (Django) et exports pandas (CSV, HTML), sans lib de chart pour l’instant.
- **Scraping** : aucun ajout, Beautiful Soup + lxml conservés.

---

## 5. Références

- **Rôles** : `agents-roles-responsabilites.md` (§ Data Analyst, Expert SEO, Growth).
- **Rapport SEO** : `rapport-seo-prospect.md`, `segmentations/2025-01-30-premier-rapport-seo-landing-p4s-archi.md`.
- **SEO sémantique** : `seo-semantique-outils-open-source.md`, `requirements-seo.txt`.
- **Infra** : `infra-devops.md` (impact Docker, build).

---

*Document créé par le Conseiller après tour des agents techniques. Dernière mise à jour : 2025-01-30.*
