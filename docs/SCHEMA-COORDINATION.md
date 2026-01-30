# Schéma du système de coordination LPPP

## 🎭 Les 7 agents et leurs interactions

```
                    ┌─────────────────────────────────┐
                    │     CHEF DE PROJET (Vous)       │
                    │  UX/UI Design • Veille • Stratégie│
                    │                                 │
                    │  • Définir features             │
                    │  • Créer segmentations          │
                    │  • Orchestrer agents            │
                    │  • Valider livrables            │
                    └──────────────┬──────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │     SEGMENTATION            │
                    │  (Feature à développer)     │
                    │                             │
                    │  • User Story               │
                    │  • Specs techniques         │
                    │  • Tâches par agent         │
                    │  • Dépendances              │
                    │  • Critères validation      │
                    └──────────────┬──────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐          ┌───────────────┐        ┌───────────────┐
│  DESIGNER     │          │  DÉVELOPPEUR  │        │  RÉDACTEUR    │
│   UI/UX       │          │    DJANGO     │        │               │
│               │          │               │        │               │
│ • Templates   │          │ • Modèles     │        │ • Contenus    │
│ • Composants  │          │ • Vues        │        │ • SEO         │
│ • Responsive  │          │ • Tests       │        │ • Éditorial   │
└───────┬───────┘          └───────┬───────┘        └───────┬───────┘
        │                          │                          │
        │                          ▼                          │
        │                  ┌───────────────┐                  │
        │                  │  INTÉGRATION  │                  │
        │                  │  (Développeur)│                  │
        │                  │               │                  │
        │                  │ • Assembler   │                  │
        │                  │ • Tester      │                  │
        │                  └───────┬───────┘                  │
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐          ┌───────────────┐        ┌───────────────┐
│  DATA         │          │  GROWTH       │        │  DEVOPS       │
│  ANALYST      │          │  HACKER       │        │               │
│               │          │               │        │               │
│ • Algorithmes │          │ • OSINT       │        │ • Docker      │
│ • Analytics   │          │ • n8n/Flowise │        │ • CI/CD       │
│ • KPIs        │          │ • Enrichment  │        │ • Déploiement │
└───────┬───────┘          └───────┬───────┘        └───────┬───────┘
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │      VALIDATION          │
                    │   (Chef de Projet)       │
                    │                          │
                    │  • Vérifier livrables    │
                    │  • Tester UX             │
                    │  • Approuver             │
                    └──────────────┬───────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │      DÉPLOIEMENT         │
                    │       (DevOps)           │
                    │                          │
                    │  Staging → Prod          │
                    └──────────────┬───────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │       ANALYSE            │
                    │  (Data Analyst + Chef)   │
                    │                          │
                    │  • KPIs                  │
                    │  • Optimisations         │
                    │  • Itérations            │
                    └──────────────────────────┘
```

---

## 🔄 Workflow en 6 phases

```
PHASE 1 : PLANIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌─────────────────────────────────────────────────────────────────┐
│  Chef de Projet                                                 │
│  ────────────────                                               │
│  1. Analyser le besoin (problème, valeur, KPIs)                 │
│  2. Faire de la veille (tendances web design 2026)              │
│  3. Créer la segmentation (User Story, Specs, Tâches)           │
│  4. Mettre à jour TODO.md                                       │
│  5. Informer les agents concernés                               │
└─────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼

PHASE 2 : DÉVELOPPEMENT (PARALLÈLE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Designer    │  │ Développeur  │  │  Rédacteur   │  │ Data Analyst │
│  ──────────  │  │ ───────────  │  │  ──────────  │  │ ────────────│
│  Templates   │  │  Modèles     │  │  Contenus    │  │  Algorithmes │
│  Composants  │  │  Vues        │  │  SEO         │  │  Analytics   │
│  Responsive  │  │  Tests       │  │  Éditorial   │  │  KPIs        │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │                 │
       └─────────────────┴─────────────────┴─────────────────┘
                                   │
                                   ▼

PHASE 3 : INTÉGRATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌─────────────────────────────────────────────────────────────────┐
│  Développeur Django                                             │
│  ───────────────────                                            │
│  1. Intégrer les templates du Designer                          │
│  2. Brancher les contenus du Rédacteur                          │
│  3. Intégrer les données enrichies (Growth)                     │
│  4. Afficher les scores (Data Analyst)                          │
│  5. Exécuter les tests unitaires (pytest)                       │
└─────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼

PHASE 4 : VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌─────────────────────────────────────────────────────────────────┐
│  Chef de Projet                                                 │
│  ────────────────                                               │
│  1. Vérifier les livrables (fonctionnel, performance, qualité)  │
│  2. Tester l'UX (mobile, desktop, accessibilité)                │
│  3. Valider les contenus (orthographe, SEO, ton)                │
│  4. Approuver pour déploiement OU demander corrections          │
└─────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼

PHASE 5 : DÉPLOIEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌─────────────────────────────────────────────────────────────────┐
│  DevOps                                                         │
│  ───────                                                        │
│  1. Déployer sur staging (Vercel/Contabo)                       │
│  2. Chef de Projet valide sur staging                           │
│  3. Déployer en production                                      │
│  4. Monitorer les logs et performances                          │
└─────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼

PHASE 6 : ANALYSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌─────────────────────────────────────────────────────────────────┐
│  Data Analyst + Chef de Projet                                 │
│  ───────────────────────────────                                │
│  1. Collecter les KPIs (taux de conversion, temps de chargement)│
│  2. Analyser les résultats (ce qui marche, ce qui ne marche pas)│
│  3. Identifier les optimisations (A/B testing, améliorations)   │
│  4. Planifier les itérations suivantes (nouvelles features)     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Matrice RACI (Responsible, Accountable, Consulted, Informed)

```
Tâche                          │ Chef │ Dev  │ Designer │ Data │ Growth │ DevOps │ Rédacteur
                               │Projet│Django│          │Analyst│        │        │
───────────────────────────────┼──────┼──────┼──────────┼──────┼────────┼────────┼──────────
Définir features prioritaires  │  R   │  C   │    C     │  C   │   C    │   I    │    I
Créer modèles Django           │  I   │  R   │    I     │  C   │   I    │   I    │    I
Designer templates landing     │  A   │  I   │    R     │  I   │   I    │   I    │    C
Développer algorithmes scoring │  A   │  C   │    I     │  R   │   C    │   I    │    I
Configurer pipelines OSINT     │  A   │  C   │    I     │  C   │   R    │   C    │    I
Déployer sur Vercel/Contabo    │  A   │  C   │    I     │  I   │   I    │   R    │    I
Rédiger contenus landing       │  A   │  I   │    C     │  I   │   I    │   I    │    R
Intégrer Tailwind CSS          │  I   │  C   │    R     │  I   │   I    │   I    │    I
Créer tâches Celery enrich.    │  I   │  R   │    I     │  I   │   C    │   I    │    I
Analyser taux de conversion    │  A   │  I   │    I     │  R   │   C    │   I    │    C
Configurer CI/CD GitHub        │  A   │  C   │    I     │  I   │   I    │   R    │    I
Documenter base connaissance   │  R   │  C   │    C     │  C   │   C    │   C    │    C

Légende :
  R = Responsible (réalise la tâche)
  A = Accountable (valide et arbitre)
  C = Consulted (consulté, donne son avis)
  I = Informed (informé du résultat)
```

---

## 🎯 Exemple : Feature "Système de templates multiples"

```
┌─────────────────────────────────────────────────────────────────┐
│  FEATURE : Système de templates multiples                      │
│  ────────────────────────────────────────────────────────────   │
│  User Story : Choisir parmi 3 templates (modern, minimal,      │
│               corporate) pour adapter le design à la cible      │
│                                                                 │
│  Durée : 3-4 jours (avec parallélisation)                       │
│  KPIs : Taux de conversion +20%, temps <2s, accessibilité >90  │
└─────────────────────────────────────────────────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐          ┌───────────────┐        ┌───────────────┐
│  DESIGNER     │          │  DÉVELOPPEUR  │        │  RÉDACTEUR    │
│   (10h)       │          │    (4h)       │        │    (3h)       │
│               │          │               │        │               │
│ • Setup       │          │ • Modifier    │        │ • Rédiger     │
│   Tailwind    │          │   modèle      │        │   contenus    │
│ • Créer       │          │ • Créer vues  │        │   (3 types)   │
│   modern.html │          │ • Admin       │        │ • SEO         │
│ • Créer       │          │ • Tests       │        │ • Variables   │
│   minimal.html│          │ • Migration   │        │   JSON        │
│ • Créer       │          │               │        │               │
│   corporate   │          │               │        │               │
│ • Documenter  │          │               │        │               │
└───────┬───────┘          └───────┬───────┘        └───────┬───────┘
        │                          │                          │
        │                          ▼                          │
        │                  ┌───────────────┐                  │
        │                  │  INTÉGRATION  │                  │
        │                  │  (Développeur)│                  │
        │                  │     (1h)      │                  │
        │                  │               │                  │
        │                  │ • Intégrer    │                  │
        │                  │   templates   │                  │
        │                  │ • Brancher    │                  │
        │                  │   contenus    │                  │
        │                  │ • Tester      │                  │
        │                  └───────┬───────┘                  │
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐          ┌───────────────┐        ┌───────────────┐
│  DATA         │          │  GROWTH       │        │  DEVOPS       │
│  ANALYST      │          │  HACKER       │        │    (2h)       │
│   (2h)        │          │   (1h)        │        │               │
│               │          │               │        │ • Vérifier    │
│ • Définir     │          │ • Documenter  │        │   build       │
│   événements  │          │   workflow    │        │ • Déployer    │
│   tracking    │          │   n8n         │        │   staging     │
│ • Préparer    │          │ • Créer       │        │ • Lighthouse  │
│   dashboard   │          │   workflow    │        │ • Déployer    │
│ • Documenter  │          │   test        │        │   prod        │
│   KPIs        │          │               │        │               │
└───────┬───────┘          └───────┬───────┘        └───────┬───────┘
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │      VALIDATION          │
                    │   (Chef de Projet)       │
                    │        (2h)              │
                    │                          │
                    │  • Vérifier livrables    │
                    │  • Tester UX mobile/desk │
                    │  • Approuver             │
                    └──────────────────────────┘

TOTAL : 25h (22h développement + 3h planification)
DURÉE : 3-4 jours (avec parallélisation optimale)
```

---

## 📁 Structure des documents

```
docs/
├── GUIDE-CHEF-PROJET.md          ← Workflow, veille, checklist, FAQ
├── GUIDE-AGENTS.md               ← Comment recevoir et réaliser une tâche
├── RECAPITULATIF-SYSTEME-COORDINATION.md ← Récap complet du système
├── SCHEMA-COORDINATION.md        ← Vous êtes ici (diagrammes ASCII)
├── TODO.md                       ← Tâches prioritaires
├── boite-a-idees.md              ← Idées en attente
├── bonnes-pratiques.md           ← Éditorial anti-détection IA
│
├── base-de-connaissances/
│   ├── agents-roles-responsabilites.md ← 7 rôles, matrice RACI
│   ├── decisions.md              ← Décisions enregistrées
│   ├── sources.md                ← Références externes
│   └── segmentations/
│       ├── TEMPLATE.md           ← Template réutilisable
│       └── 2025-01-30-systeme-templates-multiples.md ← Exemple
│
└── logs/
    ├── log-projet.md             ← Historique actions/décisions
    └── log-ia.md                 ← Logs interactions IA
```

---

## 🚀 Démarrage rapide

### Vous êtes Chef de Projet ?
```
1. Lire GUIDE-CHEF-PROJET.md
2. Consulter TODO.md (tâches prioritaires)
3. Créer une segmentation (copier TEMPLATE.md)
4. Informer les agents concernés
5. Suivre l'avancement
6. Valider les livrables
7. Mettre à jour la documentation
```

### Vous êtes un Agent ?
```
1. Lire GUIDE-AGENTS.md
2. Consulter la segmentation (vos tâches)
3. Réaliser vos tâches (cocher au fur et à mesure)
4. Livrer votre travail (checklist validation)
5. Informer le Chef de Projet
```

---

*Document créé le 2025-01-30. Maintenu par le Chef de Projet.*
