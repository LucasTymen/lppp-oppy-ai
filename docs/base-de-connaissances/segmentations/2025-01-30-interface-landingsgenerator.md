# Interface landingsgenerator (/essais/) — mobile-first, dark + switch

**Date** : 2025-01-30  
**Chef de Projet** : Agent Chef de Projet  
**Statut** : 🟡 En cours (stratégie validée, développement à lancer)  
**Référence** : `reponses-validees-strategie.md`

---

## 📋 User Story

> En tant qu'utilisateur LPPP, je veux une interface Django (mobile-first, mode nuit par défaut + switch clair/sombre) pour mes essais et ma prospection, avec un premier écran « relance salon » : présentation où je me place comme produit commercial (freelance/alternant selon matching), en partant de l'activité et des pain points du prospect.

**Contexte** :
- **App** : **landingsgenerator**.
- **URL** : **/essais/** (racine).
- **Premier écran (relance salon)** : Présentation ; cibler activité, besoins supposés, pain points ; se présenter comme **freelance** ou **alternant** (selon matching) sérieux à envisager — **produit commercial** à la fin.
- **Thème** : Mode nuit par défaut + **switch clair/sombre**. Le **Designer** doit vérifier **individuellement** chaque page : fonds noirs en mode nuit, passage correct en mode jour. Se méfier des contenus qui supportent mal le switch (comme sur SquidResearch).

**Critères d'acceptation** :
- [x] App Django `apps.landingsgenerator`, URL `/essais/`.
- [x] Base template mobile-first (viewport, touch targets ≥ 44px), dark par défaut + switch clair/sombre : `templates/landingsgenerator/base.html`.
- [x] Premier écran : présentation relance salon : `templates/landingsgenerator/index.html` (objectif, lien admin).
- [ ] Designer : vérification page par page (fonds noir mode nuit, switch propre ; gérer cas type SquidResearch).

---

## 🔧 Specs techniques

### Architecture
- **Nouvelle app** : `apps.landingsgenerator` (ou nom de module cohérent).
- **URLs** : `lppp/urls.py` → `path("essais/", include("apps.landingsgenerator.urls"))`.
- **Templates** : `templates/landingsgenerator/` (ou `templates/essais/`) — base.html (mobile-first, CSS variables dark/light, switch).
- **Static** : CSS interface (variables, media prefers-color-scheme ou [data-theme], safe-area).

### Design
- Mobile-first ; mode nuit par défaut ; switch clair/sombre ; Designer vérifie chaque page (fonds, contraste, cas limites type SquidResearch).

---

## 👥 Segmentation des tâches (résumé)

| Agent | Rôle | Tâches clés |
|-------|------|-------------|
| **Chef de Projet** | Spécifier et valider | Specs, validation livrables. |
| **Dev Django** | App + vues | Créer app landingsgenerator, URLs /essais/, vues premier écran (présentation relance salon). |
| **Designer** | Base template + thème | Base template mobile-first, dark + switch ; vérifier chaque page (fonds noir, switch propre ; cas SquidResearch). |
| **Rédacteur** | Contenu premier écran | Textes présentation, positionnement freelance/alternant, ciblage activité/pain points. |
| **DevOps** | Déploiement | Vérifier inclusion app, static, déploiement. |

---

## 🔄 Dépendances

- Auth : protéger l'interface (LoginRequiredMixin ou équivalent) pour accès contrôlé.
- Référence SquidResearch : attention aux contenus qui supportent mal le switch clair/sombre — tester et documenter les pièges.

---

*Segmentation créée par le Conseiller. À détailler par le Chef de Projet (estimation heures, ordre d'exécution).*
