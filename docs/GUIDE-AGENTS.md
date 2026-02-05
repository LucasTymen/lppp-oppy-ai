# Guide pour les agents LPPP

## 👋 Bienvenue !

Vous êtes un **agent spécialisé** du projet LPPP (Landings Pages Pour Prospections). Ce guide vous explique comment travailler efficacement avec les autres agents.

---

## 🎭 Votre rôle

Vous êtes l'un des 7 agents du projet :

1. **Chef de Projet** : Planification, veille design, validation
2. **Développeur Django** : Backend, modèles, vues, tests
3. **Designer UI/UX** : Templates, composants, responsive
4. **Data Analyst** : Algorithmes, analytics, KPIs
5. **Growth Hacker** : OSINT, automation, n8n/Flowise
6. **DevOps** : Infrastructure, CI/CD, déploiement
7. **Rédacteur** : Contenus, SEO, éditorial

**Votre fiche de rôle complète** : `docs/base-de-connaissances/agents-roles-responsabilites.md`

**Si vous avez un rôle de coordination** (Chef de Projet, Orchestrateur, Conseiller quand vous coordonnez, DevOps pour l’infra) : **consulter systématiquement** le log commun LPPP ↔ SquidResearch avant toute décision ou action touchant Docker, ports, .env ou la coexistence des deux projets → `docs/base-de-connaissances/log-commun-lppp-squidresearch.md`.

---

## 📋 Comment recevoir une tâche

### 1. Le Chef de Projet crée une segmentation

Quand une nouvelle feature est lancée, le Chef de Projet crée un document de segmentation :

**Emplacement** : `docs/base-de-connaissances/segmentations/YYYY-MM-DD-nom-feature.md`

**Contenu** :
- User Story (besoin utilisateur)
- Specs techniques (architecture, données, design)
- **Vos tâches** (section dédiée à votre rôle)
- Dépendances (qui attend qui)
- Critères de validation

### 2. Vous lisez la segmentation

**À lire en priorité** :
1. **User Story** : Comprendre le besoin utilisateur
2. **Votre section** : Liste de vos tâches (checklist)
3. **Dépendances** : Qui doit finir avant vous ? Qui attend votre travail ?
4. **Critères de validation** : Comment savoir que c'est terminé ?

### 3. Vous réalisez vos tâches

- Cochez les tâches au fur et à mesure : `- [ ]` → `- [x]`
- Documentez vos décisions (si importantes)
- Communiquez les bloqueurs au Chef de Projet

### 4. Vous livrez votre travail

- Vérifiez les critères de validation
- Informez le Chef de Projet (ou l'agent suivant)
- Mettez à jour le tableau de suivi dans la segmentation

---

## 🔄 Workflow général

```
1. PLANIFICATION (Chef Projet)
   ↓
   Crée la segmentation
   ↓

2. DÉVELOPPEMENT (Vous + autres agents)
   ↓
   Vous travaillez en parallèle
   ↓

3. INTÉGRATION (Développeur Django)
   ↓
   Assemble les pièces
   ↓

4. VALIDATION (Chef Projet)
   ↓
   Vérifie la qualité
   ↓

5. DÉPLOIEMENT (DevOps)
   ↓
   Met en production
   ↓

6. ANALYSE (Data Analyst + Chef Projet)
   ↓
   Mesure les résultats
```

---

## 📊 Matrice RACI : Qui fait quoi ?

**R** = Responsible (vous réalisez la tâche)  
**A** = Accountable (vous validez et arbitrez)  
**C** = Consulted (on vous consulte pour avis)  
**I** = Informed (on vous informe du résultat)

**Voir la matrice complète** : `docs/base-de-connaissances/agents-roles-responsabilites.md`

**Exemple** : Si vous êtes **Designer** et la tâche est "Designer templates landing", vous êtes **R** (Responsible). Le Chef de Projet est **A** (Accountable, il valide votre travail).

---

## 🛠️ Outils et ressources

### Documentation projet
- **`README.md`** : Vue d'ensemble (stack, démarrage rapide)
- **`docs/TODO.md`** : Tâches prioritaires
- **`docs/bonnes-pratiques.md`** : Éditorial anti-détection IA
- **`docs/base-de-connaissances/strategie-operationnelle-make.md`** : Stratégie opérationnelle — toutes les commandes `make` (lancement, migrations, tests, lint, logs, etc.). `make help` pour l'aide. **DevOps** : up, down, build, restart, logs. **Dev Django** : migrate, makemigrations, test, lint, shell., humanisation, **rangement et maintenance** (§ 5)

### Base de connaissances
- **`docs/base-de-connaissances/registre-agents-ressources.md`** : **Registre temps réel** — tous les agents, règles Cursor, ressources à votre disposition (à consulter pour connaître les capacités disponibles et les autres agents)
- **`docs/base-de-connaissances/agents-roles-responsabilites.md`** : Votre fiche de rôle
- **`docs/base-de-connaissances/decisions.md`** : Décisions enregistrées
- **`docs/base-de-connaissances/sources.md`** : Références externes

### Segmentations
- **`docs/base-de-connaissances/segmentations/`** : Vos tâches par feature

### Règles agents
- **`.cursor/rules/pilotage-agents.mdc`** : Anti-hallucination, data-driven
- **`.cursor/rules/coordination-agents.mdc`** : Workflow de segmentation
- **`.cursor/rules/orchestrateur.mdc`** : Registre agents/ressources (qui met à jour les ressources à disposition)
- **`.cursor/rules/editorial.mdc`** : Bonnes pratiques éditoriales (Rédacteur)
- **`.cursor/rules/devops.mdc`** : Orchestration, protection prod (DevOps)

---

## 📝 Règles importantes

### 1. Anti-hallucination
- **Ne jamais inventer** de fichiers, d'API, de variables qui n'existent pas
- **Vérifier dans le code** avant d'affirmer un fait
- **Si une info n'est pas trouvée** : indiquer "à vérifier"

### 2. Data-driven
- **S'appuyer sur les données du projet** : modèles, templates, docs
- **Documenter les décisions** dans `docs/base-de-connaissances/decisions.md`
- **Mettre à jour les logs** (fait par le Chef de Projet)

### 3. Éditorial (pour Rédacteur)
- **Appliquer les bonnes pratiques** dans `docs/bonnes-pratiques.md`
- **Humanisation** : pas de "révolutionnaire", "cutting-edge"
- **Variété syntaxique** : phrases courtes et longues

### 4. Communication
- **Consulter les agents concernés** (voir matrice RACI)
- **Documenter les bloqueurs** (informer le Chef de Projet)
- **Être disponible** pour répondre aux questions

---

## 🎯 Exemple : Vous êtes Designer

### Tâche reçue
Feature : "Système de templates multiples"  
Segmentation : `docs/base-de-connaissances/segmentations/2025-01-30-systeme-templates-multiples.md`

### Votre section (extrait)

```markdown
### 3. Designer UI/UX (10h)

- [ ] Setup Tailwind CSS (1h)
- [ ] Créer template modern.html (3h)
- [ ] Créer template minimal.html (3h)
- [ ] Créer template corporate.html (2h)
- [ ] Documenter les composants (1h)

**Livrables** :
- 3 templates HTML/CSS
- Documentation des composants
- Tests manuels (screenshots)

**Dépendances** :
- ✅ Wireframes du Chef de Projet (terminés)
- ⏳ Code Django du Développeur (parallèle, pas bloquant)
```

### Votre workflow

1. **Lire la segmentation complète** (User Story, Specs design)
2. **Commencer par le setup Tailwind CSS** (1h)
3. **Créer les 3 templates** (8h, en parallèle du Développeur)
4. **Documenter les composants** (1h)
5. **Tester sur mobile/desktop** (screenshots)
6. **Cocher les tâches** dans la segmentation
7. **Informer le Chef de Projet** (livrables prêts)

### Critères de validation

- [ ] Les 3 templates s'affichent correctement
- [ ] Responsive fonctionne (mobile, tablette, desktop)
- [ ] Score accessibilité > 90 (WCAG 2.1)
- [ ] Documentation des composants créée

---

## 🚨 Que faire si vous êtes bloqué ?

### Bloqueur technique
**Exemple** : Vous ne savez pas comment implémenter une fonctionnalité

**Action** :
1. Vérifier la documentation (`README.md`, `docs/base-de-connaissances/`)
2. Chercher dans le code existant (exemples similaires)
3. Consulter l'agent concerné (voir matrice RACI)
4. Informer le Chef de Projet (il débloquera)

### Bloqueur de dépendance
**Exemple** : Vous attendez le travail d'un autre agent

**Action** :
1. Vérifier le tableau de suivi (statut de l'autre agent)
2. Travailler sur une autre tâche (si possible)
3. Informer le Chef de Projet (il relancera l'autre agent)

### Bloqueur de specs
**Exemple** : Les specs ne sont pas claires

**Action** :
1. Lister vos questions précises
2. Consulter le Chef de Projet (il clarifiera)
3. Documenter la décision (si importante)

---

## ✅ Checklist : Avant de livrer votre travail

### Fonctionnel
- [ ] Toutes mes tâches sont cochées
- [ ] Mon code/design fonctionne comme prévu
- [ ] J'ai testé sur les environnements cibles (mobile, desktop, etc.)

### Qualité
- [ ] Pas de linter errors (si applicable)
- [ ] Tests unitaires passent (si applicable)
- [ ] Documentation à jour (si nécessaire)

### Communication
- [ ] J'ai coché mes tâches dans la segmentation
- [ ] J'ai informé le Chef de Projet (ou l'agent suivant)
- [ ] J'ai documenté les décisions importantes (si applicable)

---

## 📚 Ressources par rôle

### Développeur Django
- **Django docs** : https://docs.djangoproject.com/
- **Celery docs** : https://docs.celeryproject.org/
- **Pytest docs** : https://docs.pytest.org/
- **Code de référence** : SquidResearch (`/home/lucas/tools/squidResearch`)

### Designer UI/UX
- **Tailwind CSS** : https://tailwindcss.com/
- **TailwindUI** : https://tailwindui.com/
- **Awwwards** : https://www.awwwards.com/
- **Dribbble** : https://dribbble.com/tags/landing-page

### Data Analyst
- **PostgreSQL docs** : https://www.postgresql.org/docs/
- **pandas docs** : https://pandas.pydata.org/docs/
- **Code de référence** : `apps/intelligence/` (scoring, quality, matching)

### Growth Hacker
- **n8n docs** : https://docs.n8n.io/
- **Flowise docs** : https://docs.flowiseai.com/
- **Code de référence** : `apps/scraping/enriched/`

### DevOps
- **Docker docs** : https://docs.docker.com/
- **Vercel docs** : https://vercel.com/docs
- **GitHub Actions** : https://docs.github.com/en/actions
- **Code de référence** : `docker-compose.yml`, `Makefile`

### Rédacteur
- **Bonnes pratiques** : `docs/bonnes-pratiques.md`
- **LanguageTool** : https://languagetool.org/
- **Code de référence** : `templates/landing_pages/`, `content_json`

---

## 💡 Conseils pour réussir

### 1. Lire la segmentation en entier
Ne vous contentez pas de votre section. Comprendre le contexte global vous aide à prendre de meilleures décisions.

### 2. Communiquer tôt et souvent
Si vous avez un doute, une question, un bloqueur → informez le Chef de Projet immédiatement.

### 3. Documenter vos décisions
Si vous prenez une décision importante (choix technique, compromis) → documentez-la dans la segmentation ou `decisions.md`.

### 4. Tester votre travail
Avant de livrer, vérifiez que tout fonctionne. Utilisez la checklist de validation.

### 5. Respecter les dépendances
Si un autre agent attend votre travail, priorisez cette tâche. La parallélisation est clé pour la rapidité.

---

## 🎉 Résumé

En tant qu'agent LPPP, vous devez :

✅ **Lire la segmentation** (User Story, vos tâches, dépendances)  
✅ **Réaliser vos tâches** (cocher au fur et à mesure)  
✅ **Respecter les règles** (anti-hallucination, data-driven, éditorial)  
✅ **Communiquer** (bloqueurs, questions, livrables)  
✅ **Valider votre travail** (checklist avant livraison)  
✅ **Documenter** (décisions importantes)  

**En cas de doute** : Consultez le Chef de Projet ou la documentation (`docs/base-de-connaissances/`)

---

*Document créé le 2025-01-30. Maintenu par le Chef de Projet.*
