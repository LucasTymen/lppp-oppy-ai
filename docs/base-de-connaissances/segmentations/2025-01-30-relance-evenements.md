# Relance événements — landing + positionnement direct

**Date** : 2025-01-30  
**Chef de Projet** : Agent Chef de Projet  
**Statut** : 🟡 En cours (stratégie validée, développement à lancer)  
**Référence** : `fonction-premiere-et-segments-prospection.md`, `reponses-validees-strategie.md`

---

## 📋 User Story

> En tant qu'utilisateur LPPP, je veux une landing « relance après événement » (salon) avec hero section et CTA ciblés, pour reprendre contact avec des gens avec qui le feeling est bien passé au salon et me positionner comme freelance ou alternant sérieux à envisager.

**Contexte** :
- Reprise de contact avec des contacts salon (feeling bien passé).
- Objectif : landing **aussi agréable visuellement** qu'une landing commerciale : **hero section** + **call-to-action ciblés**.
- Cibler à partir de **leur activité**, **besoins supposés**, **pain points** ; se présenter comme **produit commercial** à la fin (freelance ou alternant selon matching).

**Critères d'acceptation** :
- [x] Template de landing « relance après événement » (hero + CTA) : `templates/landing_pages/relance-evenement.html`.
- [x] Structure `content_json` définie et documentée : `docs/base-de-connaissances/structure-content-json-relance-evenement.md`.
- [ ] Contenu cas par cas pour chaque prospect (Rédacteur — sinon ça sonne faux).
- [ ] Visuel à affiner (Designer — thème prospect, niveau landing commerciale).

---

## 🔧 Specs techniques

### Architecture
- **Composants impactés** : `apps/landing_pages/` (models, views, templates), `templates/landing_pages/` (nouveau template type « relance-evenement » ou intégré au système de templates).
- **Structure `content_json`** : champs type hero (titre, sous-titre, visuel), CTA (texte, lien), bloc positionnement (freelance / alternant selon matching), personnalisation prospect (activité, pain points).

### Design
- Hero section + CTA ciblés ; thème prospect ou fallback SquidResearch (voir `theming-landing-prospect.md`).
- Responsive, mobile-first.

---

## 👥 Segmentation des tâches (résumé)

| Agent | Rôle | Tâches clés |
|-------|------|-------------|
| **Chef de Projet** | Spécifier et valider | Specs, wireframes légers, validation livrables. |
| **Designer** | Template + visuel | Template landing relance-événement (hero, CTA), thème prospect / fallback. |
| **Rédacteur** | Contenu cas par cas | Textes par prospect (activité, pain points, positionnement freelance/alternant), s'appuyer sur CV et segments. |
| **Dev Django** | Backend + intégration | Modèle/vues si besoin, sélection template, injection `content_json`. |
| **DevOps** | Déploiement | Vérifier déploiement templates/static. |

---

## 🔄 Dépendances

- Données prospect (activité, besoins, pain points) : fournies au fur et à mesure.
- CV et segments : `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md`, `fonction-premiere-et-segments-prospection.md`.

---

*Segmentation créée par le Conseiller. À détailler par le Chef de Projet (estimation heures, ordre d'exécution).*
