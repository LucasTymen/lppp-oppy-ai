# Bonnes pratiques LPPP

Approche inspirée SquidResearch : **éditorial anti-détection IA** et **humanisation** pour tout contenu rédigé (landing pages, docs, messages). Les agents et le chef de projet appliquent ces règles.

---
## 1 a. Éditorial anti-détection IA

Tu es un correcteur éditorial expert dans la détection et la neutralisation des marqueurs de texte générés par intelligence artificielle.

Ton rôle est de réécrire ou corriger des articles rédigés pour les réseaux sociaux en adoptant un ton humain, nuancé, fluide, sans structure artificielle, ni marqueurs typiques de génération LLM.

Pour chaque texte fourni, corrige-le pour qu’il évite tous les signaux suivants :

Formules de cadrage en introduction (ex. : "Dans un monde où…")

Structure hyper-segmentée (titres, sous-titres, listes, pas de listes à puces sauf si vraiment pertinentes).

Vocabulaire corporate anglo-saxon excessif (ex. : "scalable", "mindset", "impact", etc.) – mais tu peux garder les termes pertinents au growth

Antithèses binaires simplistes (ex. : "Soit tu évolues, soit tu échoues.")

Intensifieurs à faible coût ("crucial", "essentiel", etc.)

Répétitions rhétoriques ou idées dites 3 fois différemment

Marqueurs artificiels de transition ("Et pourtant…", "Mais ce n’est pas tout…")

Métadiscours excessif (parler de ce qu'on va dire, ou de ce qu’on vient de dire)

Supprime aussi tous les éléments typiques des IA :

Pas d’emojis

Pas de symboles ou caractères spéciaux non naturels (backticks, //, etc.)

Pas de double espace

➤ Objectif final : produire un texte fluide, crédible, incarné, qui pourrait naturellement être écrit par un analyste ou un professionnel humain.

---

## 1 b. Éditorial anti-détection IA

Objectif : les textes ne doivent pas sonner « générés par IA » (détecteurs, lecteurs).

- **Varier les structures** : éviter les listes à puces parfaites partout ; mélanger phrases courtes et longues, paragraphes d’une ou plusieurs phrases.
- **Éviter les formules toutes faites** : « En conclusion », « Il est important de noter que », « En résumé », « Nous sommes ravis de… », « À l’heure où… ».
- **Ton direct** : privilégier « on », « vous », formulations concrètes plutôt que formelles et vagues.
- **Imperfections contrôlées** : une virgule de trop ou un « du coup » de temps en temps, si ça reste lisible. Pas de sur-polissage.
- **Pas de sur-qualification** : éviter « solution innovante », « accompagnement sur-mesure », « expertise unique » sans donnée précise.
- **Ancrage concret** : chiffre, exemple, cas d’usage plutôt que généralités.

---

## 2. Humanisation

- **Un destinataire réel** : écrire pour une personne (prospect, lecteur), pas pour un moteur ou un algorithme.
- **Contexte métier** : nom d’entreprise, prénom, besoin identifié quand c’est disponible (landing pages personnalisées).
- **Formulations naturelles** : tournures qu’un humain utiliserait à l’oral ou dans un mail (sans en faire trop).
- **Pas de remplissage** : chaque bloc de contenu doit apporter une info ou une intention claire.

---

## 2 bis. Image pratique — éviter le vent

**Objectif** : se positionner de façon **pratique et concrète**, pas théorique ; éviter de vendre du rêve ou de « brasser du vent ».

- **Livrables avant promesses** : privilégier « je livre un script qui fait X », « livrable : CSV ou intégration CRM », « 50 leads qualifiés » plutôt que « je transforme votre expertise en avantage commercial » sans précision.
- **Ancrage technique** : nommer la stack (Python, Scrapy, Make, etc.) et le format de sortie (CSV, API, rapport) quand c'est pertinent.
- **Éviter les formules vagues** : « infrastructure qui tourne 24/7 », « logique Red/Blue/Purple appliquée à la croissance » sans explication courte ; préférer « un script que vous lancez quand vous voulez » ou une phrase qui décrit le résultat concret.
- **Chiffres et délais** : si on cite un gain (ex. heures gagnées, nombre de leads), rester crédible ; sinon formuler en « gain de temps sur la prospection » plutôt qu'un chiffre non mesuré.
- **Différenciation factuelle** : « code propriétaire que vous gardez » vs « rapports PDF » = OK ; ajouter un élément concret (ex. « livrable = repo ou script livré ») renforce l'image pratique.

**Pilotes** : Rédacteur (contenus par contact), Chef de Projet (validation). Référence positionnement : `positionnement-freelance-offres.md` (ne pas survendre).

---

## 3. Data-driven et anti-hallucination

- **Aucune affirmation sans source** : chiffres, fonctionnalités, stack → document ou base de connaissances (`docs/base-de-connaissances/`).
- **En cas de doute** : chercher dans le code, le README ou les docs avant d’écrire ; si pas trouvé, indiquer « à vérifier » ou ne pas affirmer.
- **Pas d’invention** : pas de noms de fichiers, d’API ou de variables qui n’existent pas dans le dépôt.
- **Mise à jour des logs** : le chef de projet / agent pilote met à jour `docs/logs/log-projet.md` et `docs/logs/log-ia.md` après les sessions.

---

## 4. Pilotage des agents

- **Règles centralisées** : `.cursor/rules/` contient les règles (anti-hallucination, data-driven, éditorial) ; tous les agents les respectent.
- **Base de connaissances** : faits et décisions dans `docs/base-de-connaissances/` ; s’y référer avant de rédiger ou coder.
- **TODO et idées** : `docs/TODO.md` (tâches), `docs/boite-a-idees.md` (idées) ; les maintenir à jour.

---

## 5. Rangement, organisation et maintenance

Chaque agent nettoie derrière lui et ne crée rien d'inutile. Organisation propre et lisible.

### Nettoyage après action

- **Rien à la racine** : ne pas créer de fichiers ou dossiers à la racine du projet sauf ceux déjà prévus (README.md, Makefile, manage.py, docker-compose.yml, requirements.txt, .env.example, .gitignore, dossiers `apps/`, `lppp/`, `docs/`, `docker/`, `templates/`, `.cursor/`).
- **Supprimer le temporaire** : tout fichier créé pour un test ou une manip ponctuelle doit être supprimé en fin de session (scripts one-shot, copies de backup inutiles, fichiers de debug).
- **Pas de scripts temporaires** : interdiction de laisser des scripts « pour voir », `test_*.py` à la racine, `script.py`, `run.sh` ou équivalents sans vocation pérenne. Si un script est utile, l'intégrer au bon endroit (ex. commande Django, tâche dans `Makefile`, script dans `scripts/` s'il existe et est documenté).

### Où mettre les fichiers

- **Code métier** : `apps/<app>/` (modèles, vues, tâches Celery, nodes).
- **Configuration projet** : `lppp/`, `docker/`, racine pour les fichiers listés ci-dessus uniquement.
- **Documentation** : `docs/` (base-de-connaissances, logs, guides). Pas de nouveaux `.md` à la racine.
- **Scripts réutilisables** : uniquement s'ils sont nécessaires, dans un dossier dédié (ex. `scripts/`) documenté dans la base de connaissances ou le README ; sinon privilégier le Makefile ou les commandes Django.

### Règles de maintenance

- **Ne pas écrire pour écrire** : tout script ou document doit répondre à un besoin explicite (tâche, décision, référence, erreur documentée). L'Orchestrateur (coordinateur) et le Chef de Projet (responsable rédaction) veillent en temps réel à ce qu'aucun agent ne produise de contenu inutile. Voir `.cursor/rules/pilotage-agents.mdc` § Ne pas écrire pour écrire.
- **Un fichier = un rôle clair** : pas de doublons, pas de fichiers « au cas où ».
- **Nommage explicite** : noms de fichiers et dossiers qui décrivent leur contenu.
- **Cohérence** : respecter la structure existante (apps/, docs/, etc.) ; en cas de doute, vérifier dans `docs/base-de-connaissances/` ou demander.

---

*Dernière mise à jour : 2025-01-30. Source : contexte projet LPPP + référence SquidResearch (README).*
