# Documentation LPPP

Bienvenue dans la documentation du projet **Landings Pages Pour Prospections** (LPPP).

---

## 📚 Structure de la documentation

```
docs/
├── README.md                          ← Vous êtes ici
├── GUIDE-CHEF-PROJET.md               ← Guide complet pour le chef de projet
├── GUIDE-AGENTS.md                    ← Guide pour les agents spécialisés
├── RECAPITULATIF-SYSTEME-COORDINATION.md ← Récap du système de coordination
├── TODO.md                            ← Tâches prioritaires
├── boite-a-idees.md                   ← Idées en attente
├── bonnes-pratiques.md                ← Éditorial anti-détection IA
│
├── base-de-connaissances/             ← Faits vérifiés, sources, décisions
│   ├── README.md                      ← Règles d'usage de la base
│   ├── registre-agents-ressources.md   ← Registre temps réel (agents, règles, ressources ; orchestrateur)
│   ├── agents-roles-responsabilites.md ← 7 rôles, matrice RACI, workflow
│   ├── decisions.md                   ← Décisions enregistrées
│   ├── sources.md                     ← Références externes
│   ├── intelligence-metier-algorithmes.md ← Scoring, qualité, matching
│   ├── strategie-enrichissement.md    ← Anti-blocage, conteneur Kali
│   ├── enrichissement-osint-flowise-n8n.md ← Pipelines OSINT
│   ├── infra-devops.md                ← Secrets, flux CI/CD
│   ├── regles-securite.md             ← Règles de sécurité (Django, CSRF/XSS, checklist prod)
│   └── segmentations/                 ← Segmentations de features
│       ├── TEMPLATE.md                ← Template réutilisable
│       └── 2025-01-30-systeme-templates-multiples.md ← Exemple concret
│
└── logs/                              ← Historique du projet
    ├── log-projet.md                  ← Actions et décisions
    └── log-ia.md                      ← Logs des interactions IA
```

---

## 🚀 Démarrage rapide

### Environnement WSL / Linux
→ Lire **`docs/base-de-connaissances/environnement-wsl-linux.md`** (environnement préféré, chemins, prérequis)

### Vous êtes **Chef de Projet** ?
→ Lisez **`GUIDE-CHEF-PROJET.md`** (workflow, veille design, checklist)

### Vous êtes un **Agent spécialisé** (Designer, Dev, etc.) ?
→ Lisez **`GUIDE-AGENTS.md`** (comment recevoir et réaliser une tâche)

### Vous voulez comprendre le **système de coordination** ?
→ Lisez **`RECAPITULATIF-SYSTEME-COORDINATION.md`** (rôles, workflow, exemple)

### Vous cherchez les **tâches prioritaires** ?
→ Consultez **`TODO.md`** (liste des tâches à faire)

### Vous avez une **idée de feature** ?
→ Ajoutez-la dans **`boite-a-idees.md`** (brainstorming)

---

## 📖 Documents clés

### Pour le Chef de Projet
| Document | Description |
|----------|-------------|
| **`GUIDE-CHEF-PROJET.md`** | Guide complet : rôle, workflow, veille design, checklist, FAQ |
| **`base-de-connaissances/registre-agents-ressources.md`** | **Registre temps réel** : tous les agents, règles Cursor, ressources à disposition (maintenu par l'orchestrateur) |
| **`TODO.md`** | Liste des tâches prioritaires (à mettre à jour régulièrement) |
| **`boite-a-idees.md`** | Idées en attente (non encore planifiées) |
| **`base-de-connaissances/agents-roles-responsabilites.md`** | 7 rôles d'agents, matrice RACI, workflow de coordination |
| **`base-de-connaissances/segmentations/TEMPLATE.md`** | Template pour segmenter une feature |

### Pour les Agents
| Document | Description |
|----------|-------------|
| **`GUIDE-AGENTS.md`** | Guide pour recevoir et réaliser une tâche |
| **`base-de-connaissances/registre-agents-ressources.md`** | Registre temps réel : agents, règles, ressources à disposition |
| **`bonnes-pratiques.md`** | Éditorial anti-détection IA, humanisation (Rédacteur) |
| **`base-de-connaissances/agents-roles-responsabilites.md`** | Votre fiche de rôle, matrice RACI |
| **`base-de-connaissances/segmentations/`** | Vos tâches par feature |

### Pour tous
| Document | Description |
|----------|-------------|
| **`RECAPITULATIF-SYSTEME-COORDINATION.md`** | Récap du système : rôles, workflow, exemple concret |
| **`base-de-connaissances/decisions.md`** | Décisions enregistrées (architecture, stack, process) |
| **`base-de-connaissances/sources.md`** | Références externes (SquidResearch, docs, etc.) |
| **`base-de-connaissances/regles-securite.md`** | Règles de sécurité (secrets, Django prod, CSRF/XSS, checklist prod) |
| **`logs/log-projet.md`** | Historique des actions et décisions |

---

## 🎭 Les 7 rôles d'agents

| Rôle | Expertise | Responsabilités |
|------|-----------|-----------------|
| **1. Chef de Projet** | UX/UI design, veille web, stratégie | Définir features, orchestrer agents, valider |
| **2. Développeur Django** | Django, Python, PostgreSQL, Celery | Backend, modèles, vues, tests |
| **3. Designer UI/UX** | HTML/CSS/JS, Tailwind, design systems | Templates, composants, responsive |
| **4. Data Analyst** | Algorithmes, scoring, analytics | Scoring, qualité données, KPIs |
| **5. Growth Hacker** | Scraping, OSINT, automation | OSINT, n8n/Flowise, enrichissement |
| **6. DevOps** | Docker, CI/CD, déploiement | Infrastructure, staging/prod |
| **7. Rédacteur** | Copywriting, SEO, éditorial | Contenus, bonnes pratiques, SEO |

**Détails complets** : `base-de-connaissances/agents-roles-responsabilites.md`

---

## 🔄 Workflow de coordination (résumé)

```
1. PLANIFICATION (Chef Projet)
   → Analyser besoin, créer segmentation, mettre à jour TODO

2. DÉVELOPPEMENT (Agents en parallèle)
   → Designer, Développeur, Rédacteur, Data Analyst, Growth travaillent

3. INTÉGRATION (Développeur)
   → Assembler les pièces, exécuter les tests

4. VALIDATION (Chef Projet)
   → Vérifier livrables, tester UX, approuver

5. DÉPLOIEMENT (DevOps)
   → Staging → Validation → Production

6. ANALYSE (Data Analyst + Chef Projet)
   → Collecter KPIs, analyser résultats, planifier itérations
```

**Détails complets** : `GUIDE-CHEF-PROJET.md` ou `RECAPITULATIF-SYSTEME-COORDINATION.md`

---

## 📋 Règles importantes

### 1. Anti-hallucination
- Ne jamais inventer de fichiers, d'API, de variables qui n'existent pas
- Vérifier dans le code avant d'affirmer un fait
- Si une info n'est pas trouvée : indiquer "à vérifier"

### 2. Data-driven
- S'appuyer sur les données du projet (modèles, templates, docs)
- Documenter les décisions dans `base-de-connaissances/decisions.md`
- Mettre à jour les logs après chaque session

### 3. Éditorial (pour contenus)
- Appliquer les bonnes pratiques dans `bonnes-pratiques.md`
- Humanisation : pas de "révolutionnaire", "cutting-edge"
- Variété syntaxique : phrases courtes et longues

### 4. Sécurité
- Rien de sensible committé (secrets, mots de passe, tokens) ; respecter le `.gitignore`
- Appliquer les règles dans `base-de-connaissances/regles-securite.md` (Django prod, CSRF/XSS, checklist prod)

**Détails** : `.cursor/rules/pilotage-agents.mdc`

---

## 🎯 Exemple concret : Feature "Système de templates multiples"

**Segmentation** : `base-de-connaissances/segmentations/2025-01-30-systeme-templates-multiples.md`

**Résumé** :
- **User Story** : Choisir parmi 3 templates (modern, minimal, corporate)
- **Agents impliqués** : Designer (10h), Développeur (4h), Rédacteur (3h), Data Analyst (2h), Growth (1h), DevOps (2h)
- **Durée** : 3-4 jours (avec parallélisation)
- **KPIs** : Taux de conversion +20%, temps de chargement <2s, accessibilité >90

**Voir la segmentation complète** pour les détails (specs, tâches, dépendances, validation).

---

## 🛠️ Outils et ressources

### Documentation technique
- **Racine du projet** : `../README.md` (stack, démarrage rapide)
- **Base de connaissances** : `base-de-connaissances/` (décisions, sources, algorithmes)
- **Règles agents** : `../.cursor/rules/` (pilotage, coordination, éditorial, devops)

### Veille web design (Chef de Projet)
- **Awwwards** : https://www.awwwards.com/
- **Dribbble** : https://dribbble.com/tags/landing-page
- **TailwindUI** : https://tailwindui.com/
- **Nielsen Norman Group** : https://www.nngroup.com/

### Code de référence
- **SquidResearch** : `/home/lucas/tools/squidResearch` (monorepo, templates, algorithmes)
- **Django docs** : https://docs.djangoproject.com/
- **Celery docs** : https://docs.celeryproject.org/

---

## 📞 Besoin d'aide ?

### Je suis Chef de Projet
→ Consultez **`GUIDE-CHEF-PROJET.md`** (workflow, veille, checklist, FAQ)

### Je suis un Agent spécialisé
→ Consultez **`GUIDE-AGENTS.md`** (comment recevoir et réaliser une tâche)

### Je cherche une décision passée
→ Consultez **`base-de-connaissances/decisions.md`**

### Je cherche une référence externe
→ Consultez **`base-de-connaissances/sources.md`**

### Je veux voir l'historique du projet
→ Consultez **`logs/log-projet.md`**

### Je veux créer une segmentation
→ Copiez **`base-de-connaissances/segmentations/TEMPLATE.md`**
→ Voir exemple : **`2025-01-30-systeme-templates-multiples.md`**

---

## ✅ Checklist : Maintenir la documentation

### Après chaque feature terminée
- [ ] Mettre à jour `TODO.md` (marquer "Fait")
- [ ] Mettre à jour `logs/log-projet.md` (ajouter une entrée)
- [ ] Enregistrer les décisions dans `base-de-connaissances/decisions.md`
- [ ] Archiver la segmentation (marquer 🟢 Terminé)

### Après chaque décision importante
- [ ] Ajouter dans `base-de-connaissances/decisions.md`
- [ ] Mettre à jour `logs/log-projet.md`

### Après chaque nouvelle idée
- [ ] Ajouter dans `boite-a-idees.md`
- [ ] Trier et prioriser avec le Chef de Projet
- [ ] Déplacer vers `TODO.md` quand l'idée devient une tâche

---

## 🎉 Résumé

Cette documentation vous permet de :

✅ **Comprendre les rôles** (7 agents, matrice RACI)  
✅ **Segmenter les features** (template réutilisable)  
✅ **Coordonner les agents** (workflow en 6 phases)  
✅ **Valider la qualité** (critères fonctionnel, performance, éditorial)  
✅ **Documenter systématiquement** (TODO, logs, décisions)  
✅ **Faire de la veille** (sources design, UX, performance)  

**Prochaine action recommandée** : Lire votre guide (Chef de Projet ou Agent) et consulter la segmentation de la prochaine feature.

---

*Document créé le 2025-01-30. Maintenu par le Chef de Projet.*
