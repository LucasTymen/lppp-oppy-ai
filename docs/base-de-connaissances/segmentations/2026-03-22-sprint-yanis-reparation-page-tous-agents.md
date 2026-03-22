# Sprint — Réparation et mise en fonction de la page (tous les agents)

**Date** : 2026-03-22  
**Statut** : 🟢 Terminé  
**Pilote** : **Yanis** (Orchestrateur)  
**Objectif** : Orchestrer **tous les agents** pour **réparer** et **mettre en fonction** la page (landing LPPP-OppyAI et/ou système de landings).

---

## 1. Contexte

L’utilisateur signale des difficultés d’accès à la page (erreur SSL, redirections). Un correctif **SECURE_SSL_REDIRECT=False** a été appliqué en local pour permettre l’accès HTTP. Ce sprint vise à :

- **Diagnostiquer** tout dysfonctionnement restant
- **Réparer** infra, templates, contenu, visuels
- **Valider** que la page fonctionne correctement (local + éventuellement prod)
- **Documenter** les correctifs dans `erreurs-et-solutions.md`

**URLs cibles** :
- Local : http://localhost:8010/ — http://localhost:8010/p/lppp-oppy-ai/ — http://localhost:8010/p/lppp-oppy-ai/proposition/

---

## 2. Agents mobilisés et tâches

### Yanis (Orchestrateur) — Pilote

- [ ] Valider le périmètre du sprint (page(s) à réparer)
- [ ] S’assurer que **tous les rôles** sont mobilisés selon leurs compétences
- [ ] Vérifier qu’aucune tâche n’est en doublon
- [ ] Mettre à jour le **registre** pour pointer vers ce sprint
- [ ] En fin de sprint : valider que la checklist « réparation » est complète

---

### Chef de Projet

- [ ] Prioriser les actions (P0 infra → P1 page visible → P2 contenu/visuel)
- [ ] Consulter `erreurs-et-solutions.md` et `checklist-pre-prod-integrite.md`
- [ ] Valider les livrables des agents
- [ ] Mettre à jour `log-projet.md`, `log-ia.md` en fin de sprint

---

### DevOps

- [ ] **Infra** : `docker compose ps` — db, redis, web Up ; port 8010 accessible
- [ ] **HTTP** : vérifier que `SECURE_SSL_REDIRECT=False` est bien dans `.env` (local)
- [ ] **Test connexion** : `curl -sI http://127.0.0.1:8010/p/lppp-oppy-ai/` → 200 (pas 301 vers HTTPS)
- [ ] En cas d’échec : consulter `segmentations/2026-01-30-sprint-page-instable-promovacances-devops-archi.md`
- [ ] Documenter tout correctif dans `erreurs-et-solutions.md`

---

### Dev Django / Frontend

- [ ] Vérifier que les vues `landing_public`, `landing_proposition_value` chargent correctement
- [ ] Pas de `VariableDoesNotExist` ni 500 sur `/p/lppp-oppy-ai/` et `/p/lppp-oppy-ai/proposition/`
- [ ] Valider que le JSON `landing-proposition-lppp-oppy-ai.json` est lu et injecté
- [ ] Lancer les tests : `make test-docker` ou `pytest apps/landing_pages/`

---

### Designer UI/UX

- [ ] Vérifier le rendu : hero, sections, nav, CTA
- [ ] **Contraste** : appliquer `contraste-textes-landing.md` (fond clair → texte sombre, etc.)
- [ ] **Responsive** : mobile, tablette, desktop
- [ ] Nav sticky si applicable (`position: sticky; top: 0`)

---

### Rédacteur

- [ ] Vérifier que le contenu (JSON, templates) est complet et sans placeholder « Infopro » ou générique
- [ ] Appliquer `docs/bonnes-pratiques.md` (éditorial, humanisation)

---

### Expert SEO

- [ ] Vérifier meta, titres, structure des sections SEO (si section `seo_technique_semantique` présente)
- [ ] Pas de contenu dupliqué ou vide

---

### Pentester (Consultation)

- [ ] S’assurer que les correctifs (ex. SECURE_SSL_REDIRECT en local) ne dégradent pas la sécurité
- [ ] En prod : SECURE_SSL_REDIRECT doit rester True ; le correctif local ne doit pas être poussé en prod

---

### Automatizer (si pertinent)

- [ ] Si la page embarque Flowise, n8n ou chatbot : vérifier les flux et l’embed

---

### Infographiste (si pertinent)

- [ ] Si des infographies ou visuels sont cassés : corriger chemins, dimensions, affichage

---

## 3. Ordre d’exécution recommandé

1. **DevOps** : diagnostic infra + HTTP (priorité immédiate)
2. **Dev Django** : vues, JSON, tests
3. **Designer** : rendu, contraste, responsive
4. **Rédacteur** : contenu
5. **Expert SEO** : meta, structure
6. **Chef de Projet** : validation, logs
7. **Yanis (Orchestrateur)** : clôture, registre

---

## 4. Critères de succès

- [x] La page http://localhost:8010/p/lppp-oppy-ai/ charge sans erreur (200)
- [x] La page http://localhost:8010/p/lppp-oppy-ai/proposition/ charge sans erreur (200)
- [ ] Pas de redirection HTTP → HTTPS en local
- [ ] Pas d’erreur 500, VariableDoesNotExist, ni contenu cassé
- [ ] Tests pytest passent
- [x] Correctifs documentés (fallback landing_proposition_value + _content_with_defaults)
- [ ] `log-projet.md` et `log-ia.md` mis à jour

---

## 5. Références

- `erreurs-et-solutions.md` — entrées SSL/redirection, page instable
- `pret-a-demarrer.md` — Option A (Docker 8010), Option B (runserver)
- `segmentations/2026-01-30-sprint-page-instable-promovacances-devops-archi.md` — checklist diagnostic
- `segmentations/2026-02-07-sprint-refonctionnement-landing-optimisation-hierarchisation.md` — modèle sprint multi-agents
- `registre-agents-ressources.md` — rôles et ressources

---

## 6. Correctifs appliqués (2026-03-22)

| Problème | Solution |
|----------|----------|
| **404 sur /proposition/** (landing hors base) | `landing_proposition_value` : fallback via `_fallback_landing_from_contact` quand `LandingPage` absent, comme `landing_rapport`. |
| **500 VariableDoesNotExist (positionnement)** | Appliquer `_content_with_defaults(ctx["content"], "proposition_value")` pour les deux branches (fallback et DB). |
| **SSL_ERROR_RX_RECORD_TOO_LONG** (précédent) | `.env` : `SECURE_SSL_REDIRECT=False` pour dev local. |

---

*Document piloté par Yanis (Orchestrateur). Dernière mise à jour : 2026-03-22.*
