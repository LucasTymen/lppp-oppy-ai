# Checklist pré-prod — Qualité, intégrité et fonctionnel

**Objectif** : avant chaque **push en prod** (ou fin de landing), s'assurer que la **qualité**, l'**intégrité** et le **fonctionnel** sont couverts. Aucun agent dédié unique : les rôles existants se répartissent les vérifications ; un **pilote** (Chef de Projet) s'assure que la checklist est passée.

**Pilote (Accountable)** : **Chef de Projet** — il ne fait pas toutes les vérifications lui-même mais **s'assure** que chaque branche a été validée par le rôle responsable avant push prod.

**Références** : `definition-of-done.md`, `procedure-fin-landing-repo-deploiement.md`, `regles-securite.md` (§ 9 Checklist avant mise en production), `agents-roles-responsabilites.md` (RACI, Phase 4–5).

---

## 1. Pourquoi pas un seul agent dédié ?

L'ampleur (qualité + intégrité + fonctionnel) peut être couverte par les rôles existants :

- **Dev Django** : tests, pas de régression, migrations, intégrité du code.
- **DevOps** : déploiement reproductible, page accessible, config prod, secrets hors dépôt.
- **Pentester** : sécurité (credentials, flux, rate limiting, checklist `regles-securite.md`).
- **Chef de Projet** : validation livrables, **pilote de la checklist** — s'assure que chaque branche a validé avant push prod.

Un agent unique « QA / Release » serait redondant avec ces responsabilités déjà définies. Le **pilote** (Chef de Projet) assure la **pérennité et l'intégrité** en s'assurant que la checklist est exécutée et que personne ne pousse en prod sans que les trois branches (qualité, intégrité, fonctionnel) soient OK.

---

## 2. Les trois branches (qualité, intégrité, fonctionnel)

| Branche | Contenu | Qui fait (R) | Qui pilote (A) |
|---------|---------|--------------|----------------|
| **Qualité** | Tests passants, pas de régression connue, Definition of Done respectée, doc impactée à jour | Dev Django (tests, code) ; Chef de Projet (validation DoD) | Chef de Projet |
| **Intégrité** | Secrets hors dépôt, config prod OK (DEBUG, ALLOWED_HOSTS, HTTPS), migrations appliquées, checklist sécurité § 9. **DEBUG off en prod** : Chef de Projet, DevOps et Architecte réseau (ingénieur réseau) doivent passer les pages en debug mode off (`DEBUG=False`) avant tout push en prod. | DevOps (config, déploiement) ; Pentester (C pour sécurité) ; Dev Django (migrations) ; Chef de Projet + DevOps + Architecte réseau (vérif. DEBUG off) | Chef de Projet |
| **Fonctionnel** | Page accessible, pas d'erreur (404, 5xx), déploiement réussi (Vercel/Contabo) | DevOps | Chef de Projet |

Le **Chef de Projet** ne réalise pas lui-même chaque case : il **s'assure** que Dev Django a validé qualité, que DevOps a validé intégrité (config, secrets) et fonctionnel (page OK), et que Pentester a été consulté sur la sécurité si besoin. En cas de doute ou de push urgent, c'est lui qui arbitre (bloquer ou accepter le risque).

---

## 3. Checklist opérationnelle (avant push prod)

À utiliser avant chaque **push vers la branche de prod** ou avant chaque **fin de landing** (déploiement Vercel/Contabo).

### 3.1 Qualité (Dev Django + Chef de Projet)

- [ ] **Tests** : `pytest` (ou tests définis) passants ; pas de régression sur les zones modifiées.
- [ ] **Definition of Done** : livrable conforme à `definition-of-done.md` (livrable livré, pas de régression connue, doc impactée à jour).
- [ ] **Validation Chef de Projet** : livrable validé pour mise en prod (conformité specs, UX/content si applicable).

### 3.2 Intégrité (DevOps + Dev Django + Pentester en appui)

- [ ] **Secrets** : aucun secret, token ou clé dans le dépôt ; `.env` non versionné ; variables prod dans Vercel/Contabo/CI.
- [ ] **Config prod** : `DEBUG=False`, `SECRET_KEY` forte, `ALLOWED_HOSTS` explicite, HTTPS activé (voir `regles-securite.md` § 9). **Chef de Projet, DevOps et Architecte réseau (ingénieur réseau)** doivent s'assurer que les pages sont en debug mode off avant push en prod.
- [ ] **Migrations** : migrations Django appliquées en environnement cible si changement de modèles.
- [ ] **Sécurité** : checklist `regles-securite.md` § 9 parcourue ; Pentester consulté (C) pour les flux sensibles (API, webhooks, n8n/Flowise).
- [ ] **Next.js (App Router)** : si le projet utilise **Next.js** avec **App Router**, vérifier que la dépendance **`next`** est sur une **version patchée** conforme au dernier advisory sécurité (RSC / React) — voir **`plan-mise-a-jour-nextjs-securite.md`** ; en cas d’advisory critique, upgrade **avant** prod (DevOps **R**).

### 3.3 Fonctionnel (DevOps)

- [ ] **Déploiement** : build / déploiement réussi (Vercel, Contabo, ou CI).
- [ ] **Page / service** : URL accessible, pas de 404 ni 5xx ; contenu attendu affiché.
- [ ] **Fin de landing** : si landing, procédure `procedure-fin-landing-repo-deploiement.md` accomplie (repo au nom de la société, push, Vercel OK, page vérifiée).

### 3.4 Pilote (Chef de Projet)

- [ ] **Checklist globale** : les trois branches (qualité, intégrité, fonctionnel) ont été validées par les rôles concernés ; aucun push prod sans ce passage.
- [ ] **Arbitrage** : en cas d’exception (hotfix, risque assumé), décision documentée (log, TODO ou décision).

---

## 4. RACI résumé

| Tâche | Chef Projet | Dev Django | DevOps | Pentester |
|-------|-------------|------------|--------|-----------|
| **Piloter la checklist pré-prod (s'assurer que tout est OK avant push prod)** | **A** | R (qualité) | R (intégrité config + fonctionnel) | C (sécurité) |
| **Qualité (tests, DoD, pas de régression)** | A | **R** | I | I |
| **Intégrité (secrets, config prod, migrations, sécurité)** | A | R (migrations) | **R** (config, déploiement) | **C** |
| **Fonctionnel (page OK, déploiement réussi)** | A | I | **R** | I |

---

## 5. Où c'est documenté ailleurs

- **Definition of Done** : `definition-of-done.md` (tâche done = livrable + pas de régression + doc à jour + validation Chef de Projet).
- **Fin de landing** : `procedure-fin-landing-repo-deploiement.md` (repo, push, Vercel, page OK) — cas particulier de la checklist pré-prod pour une landing.
- **Sécurité** : `regles-securite.md` (§ 9 Checklist avant mise en production).
- **Rôles et RACI** : `agents-roles-responsabilites.md` (Chef de Projet pilote checklist pré-prod ; DevOps, Dev Django, Pentester comme ci-dessus).

---

*Document créé pour clarifier qui assure la qualité, l'intégrité et le fonctionnel avant push prod, sans ajouter d'agent dédié. Pilote : Chef de Projet. Dernière mise à jour : 2025-01-30.*
