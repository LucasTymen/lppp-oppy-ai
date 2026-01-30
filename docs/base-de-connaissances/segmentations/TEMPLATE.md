# [NOM DE LA FEATURE]

**Date** : YYYY-MM-DD  
**Chef de Projet** : [Nom]  
**Statut** : 🟡 En cours / 🟢 Terminé / 🔴 Bloqué

---

## 📋 User Story

> En tant que [type d'utilisateur], je veux [action] afin de [bénéfice].

**Contexte** :
- Pourquoi cette feature est importante
- Quel problème elle résout
- Quelle valeur elle apporte

**Critères d'acceptation** :
- [ ] Critère 1
- [ ] Critère 2
- [ ] Critère 3

---

## 🎯 Objectifs et KPIs

**Objectif principal** : [ex: Augmenter le taux de conversion de 15%]

**KPIs mesurables** :
- Métrique 1 : [ex: Temps de chargement < 2s]
- Métrique 2 : [ex: Taux de conversion > 5%]
- Métrique 3 : [ex: Score accessibilité > 90]

---

## 🔧 Specs techniques

### Architecture
- Composants impactés : [ex: `apps/landing_pages/models.py`, `templates/`]
- Nouvelles dépendances : [ex: Tailwind CSS, Alpine.js]
- Modifications de base de données : [ex: Nouvelle colonne `template_key`]

### Données
- Champs `content_json` nécessaires : [ex: `hero_title`, `cta_text`, `testimonials`]
- Sources de données : [ex: OSINT, saisie manuelle, API externe]

### Design
- Templates concernés : [ex: `modern.html`, `minimal.html`]
- Composants réutilisables : [ex: Hero, CTA, Formulaire]
- Responsive : [ex: Mobile-first, breakpoints Tailwind]

---

## 👥 Segmentation des tâches

### 1. Chef de Projet (Xh)
**Responsabilité** : Planification et validation

- [ ] Tâche 1 : [ex: Analyser les tendances web design 2026]
- [ ] Tâche 2 : [ex: Créer les wireframes (Figma)]
- [ ] Tâche 3 : [ex: Rédiger les specs techniques]
- [ ] Tâche 4 : [ex: Valider les livrables des agents]
- [ ] Tâche 5 : [ex: Mettre à jour TODO.md et logs]

**Livrables** :
- Wireframes (Figma ou papier)
- Specs techniques (ce document)
- Validation finale (checklist)

---

### 2. Développeur Django (Xh)
**Responsabilité** : Backend et logique métier

- [ ] Tâche 1 : [ex: Modifier le modèle `LandingPage` (ajouter `template_key`)]
- [ ] Tâche 2 : [ex: Créer la logique de sélection de template dans `views.py`]
- [ ] Tâche 3 : [ex: Ajouter le champ dans l'admin Django]
- [ ] Tâche 4 : [ex: Écrire les tests unitaires (pytest)]
- [ ] Tâche 5 : [ex: Créer la migration de base de données]

**Livrables** :
- Code Python (models, views, admin)
- Tests unitaires (couverture > 80%)
- Migration de base de données

**Dépendances** :
- Attend les specs du Chef de Projet
- Collabore avec le Designer (intégration templates)

---

### 3. Designer UI/UX (Xh)
**Responsabilité** : Templates et expérience utilisateur

- [ ] Tâche 1 : [ex: Créer `templates/landing_pages/modern.html`]
- [ ] Tâche 2 : [ex: Implémenter Tailwind CSS (via CDN ou build)]
- [ ] Tâche 3 : [ex: Développer les composants réutilisables (hero, CTA)]
- [ ] Tâche 4 : [ex: Assurer le responsive (mobile-first)]
- [ ] Tâche 5 : [ex: Tester l'accessibilité (WCAG 2.1)]

**Livrables** :
- Templates HTML/CSS
- Documentation des composants
- Tests d'accessibilité (rapport)

**Dépendances** :
- Reçoit les wireframes du Chef de Projet
- Fournit les templates au Développeur Django

---

### 4. Data Analyst (Xh)
**Responsabilité** : Algorithmes et analytics

- [ ] Tâche 1 : [ex: Créer un dashboard pour comparer les performances par template]
- [ ] Tâche 2 : [ex: Définir les KPIs (taux de conversion par template)]
- [ ] Tâche 3 : [ex: Implémenter le tracking des événements (clics CTA)]

**Livrables** :
- Dashboard analytics (Jupyter ou Django admin)
- Documentation des KPIs

**Dépendances** :
- Attend le déploiement pour collecter les données

---

### 5. Growth Hacker (Xh)
**Responsabilité** : Enrichissement et automation

- [ ] Tâche 1 : [ex: Configurer les workflows n8n pour générer les contenus]
- [ ] Tâche 2 : [ex: Créer les chatbots Flowise pour qualifier les prospects]

**Livrables** :
- Workflows n8n (export JSON)
- Chatbots Flowise (configuration)

**Dépendances** :
- Collabore avec le Rédacteur (contenus)

---

### 6. DevOps (Xh)
**Responsabilité** : Infrastructure et déploiement

- [ ] Tâche 1 : [ex: Vérifier que les templates sont inclus dans le build Docker]
- [ ] Tâche 2 : [ex: Déployer sur staging (Vercel/Contabo)]
- [ ] Tâche 3 : [ex: Tester les performances (temps de chargement)]
- [ ] Tâche 4 : [ex: Déployer en production]

**Livrables** :
- URL de staging
- Rapport de performances (Lighthouse)
- URL de production

**Dépendances** :
- Attend la validation du Chef de Projet

---

### 7. Rédacteur (Xh)
**Responsabilité** : Contenus et SEO

- [ ] Tâche 1 : [ex: Rédiger les contenus pour chaque template (exemples)]
- [ ] Tâche 2 : [ex: Créer des `content_json` types pour chaque template]
- [ ] Tâche 3 : [ex: Optimiser pour le SEO (mots-clés, meta descriptions)]
- [ ] Tâche 4 : [ex: Valider l'orthographe et la grammaire]

**Livrables** :
- Contenus rédigés (JSON)
- Documentation des variables dynamiques
- Checklist SEO

**Dépendances** :
- Reçoit les briefs du Chef de Projet
- Collabore avec le Designer (contenu ↔ design)

---

## 🔄 Dépendances et ordre d'exécution

### Phase 1 : Planification (séquentiel)
1. **Chef de Projet** → Wireframes et specs (bloquant pour les autres)

### Phase 2 : Développement (parallèle)
2. **Designer** → Templates HTML/CSS
3. **Développeur Django** → Modèles et vues
4. **Rédacteur** → Contenus

### Phase 3 : Intégration (séquentiel)
5. **Développeur Django** → Intégrer les templates et contenus

### Phase 4 : Validation (séquentiel)
6. **Chef de Projet** → Valider les livrables
7. **Data Analyst** → Préparer le dashboard analytics

### Phase 5 : Déploiement (séquentiel)
8. **DevOps** → Déployer sur staging
9. **Chef de Projet** → Valider sur staging
10. **DevOps** → Déployer en production

**Durée totale estimée** : [ex: 3-5 jours] (avec parallélisation)

---

## ✅ Critères de validation

### Fonctionnel
- [ ] Les 3 templates s'affichent correctement
- [ ] Le champ de sélection fonctionne dans l'admin Django
- [ ] Les contenus dynamiques sont bien injectés
- [ ] Le responsive fonctionne (mobile, tablette, desktop)

### Performance
- [ ] Temps de chargement < 2s (Lighthouse)
- [ ] Score accessibilité > 90 (WCAG 2.1)
- [ ] Pas d'erreurs console JavaScript

### Qualité
- [ ] Tests unitaires passent (couverture > 80%)
- [ ] Pas de linter errors (flake8, black)
- [ ] Documentation à jour (README, base de connaissances)

### Éditorial
- [ ] Contenus appliquent les bonnes pratiques (`docs/bonnes-pratiques.md`)
- [ ] Orthographe et grammaire validées
- [ ] SEO optimisé (mots-clés, meta descriptions)

---

## 📊 Suivi de l'avancement

| Agent | Statut | Avancement | Bloqueurs |
|-------|--------|------------|-----------|
| Chef de Projet | 🟡 En cours | 50% | — |
| Développeur Django | ⚪ Pas démarré | 0% | Attend specs |
| Designer | ⚪ Pas démarré | 0% | Attend wireframes |
| Data Analyst | ⚪ Pas démarré | 0% | Attend déploiement |
| Growth Hacker | ⚪ Pas démarré | 0% | — |
| DevOps | ⚪ Pas démarré | 0% | Attend validation |
| Rédacteur | ⚪ Pas démarré | 0% | Attend briefs |

**Légende** :
- ⚪ Pas démarré
- 🟡 En cours
- 🟢 Terminé
- 🔴 Bloqué

---

## 📝 Notes et décisions

### Décisions prises
- [Date] : Décision 1 (ex: Utiliser Tailwind CSS via CDN pour simplifier le build)
- [Date] : Décision 2 (ex: Créer 3 templates initialement, ajouter d'autres plus tard)

### Risques identifiés
- Risque 1 : [ex: Tailwind CSS peut alourdir le temps de chargement → mitigation : purge CSS]
- Risque 2 : [ex: Responsive complexe sur certains templates → mitigation : mobile-first]

### Questions en suspens
- Question 1 : [ex: Faut-il permettre la personnalisation des couleurs par landing ?]
- Question 2 : [ex: Doit-on créer un preview mode avant publication ?]

---

## 🔗 Références

- **User Story** : [Lien vers issue GitHub ou document]
- **Wireframes** : [Lien vers Figma]
- **Documentation technique** : `docs/base-de-connaissances/`
- **Matrice RACI** : `docs/base-de-connaissances/agents-roles-responsabilites.md`

---

*Document maintenu par le Chef de Projet. Dernière mise à jour : [Date].*
