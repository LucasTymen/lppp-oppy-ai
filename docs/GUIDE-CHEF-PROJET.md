# Guide du Chef de Projet LPPP

## 🎯 Votre rôle

Vous êtes le **chef de projet** avec expertise en **UX/UI design** et **veille web**. Votre mission :

1. **Définir la vision produit** (features prioritaires, roadmap)
2. **Analyser les tendances** (web design, UX, conversion)
3. **Orchestrer les agents** (répartir les tâches, valider les livrables)
4. **Maintenir la documentation** (TODO, logs, base de connaissances)
5. **Garantir la qualité** (UX, performance, éditorial)

---

## 📚 Documents clés à connaître

### Documentation projet
- **`README.md`** : Vue d'ensemble du projet (stack, démarrage rapide)
- **`docs/TODO.md`** : Liste des tâches (à mettre à jour régulièrement)
- **`docs/boite-a-idees.md`** : Idées en attente (brainstorming)
- **`docs/bonnes-pratiques.md`** : Éditorial anti-détection IA, humanisation

### Base de connaissances (`docs/base-de-connaissances/`)
- **`registre-agents-ressources.md`** : **Registre temps réel** — tous les agents, règles Cursor, ressources à votre disposition (maintenu par l’orchestrateur ; à consulter en priorité pour savoir quels agents et quelles capacités utiliser)
- **`log-commun-lppp-squidresearch.md`** : **À consulter systématiquement** (en tant que Chef de Projet / coordination) — pointeur vers le log commun LPPP ↔ SquidResearch (adresses, ports, .env, coexistence, état Docker). Document canonique dans le dépôt SquidResearch ; éviter conflits de ports et mélange des stacks.
- **`agents-roles-responsabilites.md`** : 7 rôles d'agents, matrice RACI
- **`decisions.md`** : Décisions enregistrées (architecture, stack, process)
- **`sources.md`** : Références externes (SquidResearch, docs Django, etc.)
- **`segmentations/`** : Segmentations de features (template à réutiliser)
- **`strategie-operationnelle-make.md`** : Stratégie opérationnelle Make — catalogue des commandes `make`, workflows (lancement, migrations, mise à jour, contrôle modules), répartition DevOps / Dev Django / Chef Projet. `make help` pour l'aide. **Validation avant prod** : `make validate`, `make release-checklist`

### Logs (`docs/logs/`)
- **`log-projet.md`** : Historique des actions et décisions
- **`log-ia.md`** : Logs des interactions avec les agents IA

### Registre erreurs et solutions
- **`docs/base-de-connaissances/erreurs-et-solutions.md`** : Répertoire des erreurs rencontrées et des solutions trouvées — à consulter en cas de blocage ; à mettre à jour après chaque correction (vous ou l’agent qui vous assiste). Les autres agents peuvent y contribuer en ajoutant une entrée après résolution.

### Règles agents (`.cursor/rules/`)
- **`pilotage-agents.mdc`** : Anti-hallucination, data-driven, éditorial
- **`coordination-agents.mdc`** : Workflow de segmentation, RACI
- **`orchestrateur.mdc`** : Mise à jour du registre agents/ressources, stratégie, interactions pilotes (vous et DevOps y êtes référencés)
- **`editorial.mdc`** : Bonnes pratiques éditoriales (à appliquer aux contenus)
- **`devops.mdc`** : Orchestration, protection prod, secrets

---

## 🔄 Workflow de coordination des agents

### 1. Planification (vous)

Quand une nouvelle feature est demandée :

1. **Analyser le besoin** :
   - Quel problème résout-elle ?
   - Quelle valeur apporte-elle ?
   - Quels sont les KPIs de succès ?

2. **Faire de la veille** (si besoin) :
   - Tendances web design : [Awwwards](https://www.awwwards.com/), [Dribbble](https://dribbble.com/)
   - Composants UI : [TailwindUI](https://tailwindui.com/), [shadcn/ui](https://ui.shadcn.com/)
   - Best practices UX : [Nielsen Norman Group](https://www.nngroup.com/), [Baymard Institute](https://baymard.com/)

3. **Créer la segmentation** :
   - Copier le template : `docs/base-de-connaissances/segmentations/TEMPLATE.md`
   - Renommer : `YYYY-MM-DD-nom-feature.md`
   - Remplir toutes les sections (User Story, Specs, Tâches par agent)
   - Définir les dépendances (parallèle ou séquentiel)

4. **Mettre à jour le TODO** :
   - Ajouter les nouvelles tâches dans `docs/TODO.md`
   - Marquer les priorités (Haute, Moyenne, Basse)

5. **Informer les agents** :
   - Partager la segmentation avec les agents concernés
   - Préciser les deadlines et dépendances

### 2. Développement (agents)

Les agents travaillent en parallèle selon la segmentation :

- **Designer** → Templates HTML/CSS
- **Développeur Django** → Backend et logique métier
- **Rédacteur** → Contenus et SEO
- **Data Analyst** → Algorithmes et analytics
- **Growth Hacker** → Automation et OSINT
- **DevOps** → Infrastructure et déploiement

**Votre rôle** : Être disponible pour répondre aux questions, débloquer les agents

### 3. Validation (vous)

Quand les agents ont terminé :

1. **Vérifier les livrables** :
   - Fonctionnel : Les features marchent comme prévu ?
   - Performance : Temps de chargement, accessibilité ?
   - Qualité : Tests passent, pas de linter errors ?
   - Éditorial : Contenus appliquent les bonnes pratiques ?

2. **Tester l'UX** :
   - Mobile (vrais devices, pas juste DevTools)
   - Desktop (différents navigateurs)
   - Accessibilité (lecteur d'écran, navigation clavier)

3. **Approuver ou demander des corrections** :
   - Si OK → Passer à la phase de déploiement
   - Si KO → Lister les corrections nécessaires, renvoyer aux agents

### 4. Déploiement (DevOps)

1. **Staging** : DevOps déploie sur environnement de test
2. **Validation staging** : Vous testez sur l'URL de staging
3. **Production** : DevOps déploie en production (après votre validation)

### 5. Analyse (Data Analyst + vous)

1. **Collecter les données** : Data Analyst extrait les KPIs
2. **Analyser les résultats** : Taux de conversion, temps de chargement, etc.
3. **Identifier les optimisations** : Qu'est-ce qui peut être amélioré ?
4. **Planifier les itérations suivantes** : Nouvelles features, corrections

### 6. Documentation (vous)

Après chaque feature terminée :

1. **Mettre à jour le TODO** : Marquer "Fait" les tâches terminées
2. **Mettre à jour les logs** : Ajouter une entrée dans `docs/logs/log-projet.md`
3. **Enregistrer les décisions** : Ajouter dans `docs/base-de-connaissances/decisions.md`
4. **Archiver la segmentation** : Marquer le statut 🟢 Terminé

---

## 🎨 Veille web design (sources recommandées)

### Inspiration design
- **[Awwwards](https://www.awwwards.com/)** : Sites primés (tendances 2026)
- **[Dribbble](https://dribbble.com/tags/landing-page)** : Designs landing pages
- **[Behance](https://www.behance.net/)** : Projets web design
- **[Land-book](https://land-book.com/)** : Galerie de landing pages
- **[Lapa Ninja](https://www.lapa.ninja/)** : Landing pages classées par catégorie

### Composants UI
- **[TailwindUI](https://tailwindui.com/)** : Composants Tailwind CSS (payant)
- **[shadcn/ui](https://ui.shadcn.com/)** : Composants React + Tailwind (gratuit)
- **[Flowbite](https://flowbite.com/)** : Composants Tailwind (gratuit)
- **[DaisyUI](https://daisyui.com/)** : Composants Tailwind (gratuit)

### UX Best Practices
- **[Nielsen Norman Group](https://www.nngroup.com/)** : Recherche UX (articles, études)
- **[Baymard Institute](https://baymard.com/)** : UX e-commerce (études)
- **[UX Collective](https://uxdesign.cc/)** : Articles UX (Medium)
- **[Smashing Magazine](https://www.smashingmagazine.com/)** : Articles web design/UX

### Performance & Accessibilité
- **[Lighthouse](https://developers.google.com/web/tools/lighthouse)** : Audit performance/accessibilité
- **[WebPageTest](https://www.webpagetest.org/)** : Test de performance
- **[WAVE](https://wave.webaim.org/)** : Test d'accessibilité
- **[A11y Project](https://www.a11yproject.com/)** : Ressources accessibilité

### Tendances & Actualités
- **[Product Hunt](https://www.producthunt.com/)** : Nouveaux produits tech
- **[Hacker News](https://news.ycombinator.com/)** : Actualités tech
- **[Designer News](https://www.designernews.co/)** : Actualités design
- **[CSS-Tricks](https://css-tricks.com/)** : Tutoriels CSS/JS

---

## 📋 Checklist : Lancer une nouvelle feature

- [ ] 1. Analyser le besoin (problème, valeur, KPIs)
- [ ] 2. Faire de la veille (si besoin)
- [ ] 3. Créer la segmentation (copier `TEMPLATE.md`, remplir)
- [ ] 4. Mettre à jour `docs/TODO.md` (ajouter les tâches)
- [ ] 5. Informer les agents concernés (partager la segmentation)
- [ ] 6. Suivre l'avancement (tableau dans la segmentation)
- [ ] 7. Valider les livrables (fonctionnel, performance, qualité, éditorial)
- [ ] 8. Tester l'UX (mobile, desktop, accessibilité)
- [ ] 9. Approuver le déploiement (staging → prod)
- [ ] 10. Analyser les résultats (KPIs, optimisations)
- [ ] 11. Mettre à jour la documentation (TODO, logs, décisions)

---

## 🛠️ Outils à votre disposition

### Agents disponibles
1. **Chef de Projet** (vous) : Planification, veille, validation
2. **Développeur Django** : Backend, modèles, vues, tests
3. **Designer UI/UX** : Templates, composants, responsive
4. **Data Analyst** : Algorithmes, analytics, KPIs
5. **Growth Hacker** : OSINT, automation, n8n/Flowise
6. **DevOps** : Infrastructure, CI/CD, déploiement
7. **Rédacteur** : Contenus, SEO, éditorial

### Matrice RACI
Voir `docs/base-de-connaissances/agents-roles-responsabilites.md` pour savoir qui fait quoi.

### Template de segmentation
`docs/base-de-connaissances/segmentations/TEMPLATE.md` (à copier pour chaque feature)

---

## 💡 Conseils pour réussir

### 1. Toujours data-driven
- Ne jamais affirmer sans source (règle anti-hallucination)
- Documenter les décisions dans `decisions.md`
- S'appuyer sur les données du projet (modèles, templates, docs)

### 2. Paralléliser au maximum
- Identifier les tâches indépendantes (Designer + Développeur + Rédacteur en parallèle)
- Définir clairement les dépendances (qui attend qui)
- Optimiser le temps de développement (3-4 jours au lieu de 2 semaines)

### 3. Valider avant de déployer
- Tester sur vrais devices (pas juste DevTools)
- Vérifier l'accessibilité (WCAG 2.1)
- Mesurer les performances (Lighthouse)
- Relire les contenus (orthographe, ton)

### 4. Documenter, documenter, documenter
- Mettre à jour le TODO après chaque session
- Enregistrer les décisions importantes
- Maintenir les logs à jour
- Créer des segmentations détaillées

### 5. Communiquer clairement
- Rédiger des specs techniques précises (pas d'ambiguïté)
- Définir des critères de validation mesurables
- Être disponible pour débloquer les agents
- Donner du feedback constructif

---

## 🚀 Exemple concret : Feature "Système de templates multiples"

Voir `docs/base-de-connaissances/segmentations/2025-01-30-systeme-templates-multiples.md` pour un exemple complet de segmentation.

**Résumé** :
- **User Story** : Choisir parmi 3 templates (modern, minimal, corporate)
- **Agents impliqués** : Designer (10h), Développeur (4h), Rédacteur (3h), Data Analyst (2h), Growth (1h), DevOps (2h)
- **Durée totale** : 3-4 jours (avec parallélisation)
- **KPIs** : Taux de conversion +20%, temps de chargement <2s, accessibilité >90

---

## 📞 Questions fréquentes

### Q : Comment savoir si une tâche doit être parallèle ou séquentielle ?
**R** : Posez-vous la question : "Cette tâche dépend-elle du résultat d'une autre ?" Si non → parallèle. Si oui → séquentielle.

### Q : Que faire si un agent est bloqué ?
**R** : Identifier le bloqueur, débloquer rapidement (prendre une décision, fournir une info manquante), documenter la décision.

### Q : Comment prioriser les features ?
**R** : Matrice Effort/Impact. Priorité haute = Impact élevé + Effort faible. Priorité basse = Impact faible + Effort élevé.

### Q : Faut-il créer une segmentation pour chaque feature ?
**R** : Oui pour les features complexes (>3 tâches, plusieurs agents). Non pour les tâches simples (correction de bug, ajout d'un champ).

### Q : Comment mesurer le succès d'une feature ?
**R** : Définir des KPIs mesurables dans la segmentation (taux de conversion, temps de chargement, score accessibilité). Analyser les données après déploiement.

---

## 🎓 Ressources pour aller plus loin

### Méthodologies agiles
- **Scrum** : [Scrum Guide](https://scrumguides.org/)
- **Kanban** : [Kanban Guide](https://www.atlassian.com/agile/kanban)
- **Lean UX** : [Lean UX Book](https://www.jeffgothelf.com/lean-ux-book/)

### Gestion de projet web
- **Shape Up** (Basecamp) : [Shape Up Guide](https://basecamp.com/shapeup)
- **Design Sprint** (Google) : [Design Sprint Kit](https://designsprintkit.withgoogle.com/)

### UX/UI Design
- **Don't Make Me Think** (Steve Krug) : Livre UX classique
- **The Design of Everyday Things** (Don Norman) : Principes de design
- **Refactoring UI** (Adam Wathan) : Design pour développeurs

---

*Document maintenu par le Chef de Projet. Dernière mise à jour : 2025-01-30.*
