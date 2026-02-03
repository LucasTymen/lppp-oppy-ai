# Procédure : fin de landing — repo au nom de la société et déploiement

**Pour** : Équipe technique (DevOps, Architecte réseau, Dev Django, Designer, Chef de Projet).  
**Objectif** : À la fin de chaque landing page, s’assurer que le dépôt Git est initialisé et poussé vers un **nouveau repo au nom de la société**, puis que le déploiement a bien lieu et que la page fonctionne. **C’est aux agents DevOps et Architecte réseau de se charger de ça et de tout créer et actionner** (repo, git init, commit, push, configuration Vercel, vérification déploiement et page). Chaque membre en charge s’en assure.

**Référence** : `strategie-landings-standalone-vs-hub.md`, `deploiement-vercel-frontend.md`, `agents-roles-responsabilites.md` (RACI, workflow Phase 4–5). **Checklist pré-prod** : pour la qualité, l'intégrité et le fonctionnel avant tout push prod (y compris fin de landing), voir `checklist-pre-prod-integrite.md` (Chef de Projet pilote, Dev Django / DevOps / Pentester par branche).

---

## 1. Règle : une landing terminée = repo dédié + déploiement vérifié

Quand une landing page est **terminée** (contenu et design validés, prête à être envoyée au prospect) :

1. **Repo au nom de la société** : le code de la landing doit être dans un dépôt Git **initialisé** avec un **premier commit** et **poussé sur un nouveau repo nommé après la société** (ex. `landing-p4s-archi`, `p4s-archi-landing`) pour pouvoir s’en rappeler et retrouver facilement le projet.
2. **Déploiement et page OK** : le déploiement (ex. Vercel) doit être configuré et exécuté ; la page doit être **vérifiée** (URL accessible, contenu correct, pas d’erreur).
3. **Contenu et hero** : pour les landings Next.js, le contenu doit venir du JSON du contact (`docs/contacts/<slug>/landing-proposition-*.json` → `src/content/landing.json`) et la hero doit avoir image de fond (JSON ou défaut), **parallax** et **scanlines** actifs par défaut. Voir **`generation-landing-nextjs-contenu-hero.md`** — à appliquer dès la génération de la landing.
4. **DevOps et Architecte réseau** : chargés de **tout créer et actionner** (création/config repo, git init, premier commit, push, configuration Vercel, vérification que le déploiement se fait et que la page fonctionne). Dev Django / Designer fournissent le code ; Chef de Projet valide la checklist.

---

## 2. Étapes obligatoires (checklist)

| # | Étape | Qui est en charge | Vérification |
|---|--------|-------------------|--------------|
| 1 | Créer un **nouveau repo** (GitHub/GitLab) **au nom de la société** (ex. `landing-p4s-archi`) | **DevOps / Architecte réseau** | Repo existant, nom explicite |
| 2 | **Git init** dans le projet/dossier de la landing (si pas déjà un dépôt) | **DevOps / Architecte réseau** (ou Dev Django si défini) | `git status` OK |
| 3 | **Premier commit** (fichiers landing + config minimale : package.json, vercel.json si besoin) | **DevOps / Architecte réseau** / Dev Django | Historique propre |
| 4 | **Push** vers le nouveau repo (branch principale, ex. `main`) | **DevOps / Architecte réseau** | Code présent sur le remote |
| 5 | **Configurer le déploiement** (ex. Vercel lié au repo, Root Directory si monorepo) | **DevOps / Architecte réseau** | Projet Vercel créé / mis à jour |
| 6 | **Vérifier que le déploiement se fait** (build réussi, déploiement actif) | **DevOps / Architecte réseau** | Dashboard Vercel : dernier déploiement « Ready » |
| 7 | **Vérifier que la page fonctionne** (ouvrir l’URL, contenu correct, pas de 404 ni d’erreur) | **DevOps / Architecte réseau** + **Chef de Projet** | Page affichée correctement |
| 8 | **Valider la livraison** (checklist complète, URL enregistrée, doc mise à jour si besoin) | **Chef de Projet** | Livrable validé |

---

## 3. Responsabilités par rôle

- **DevOps et Architecte réseau** : **chargés de tout créer et actionner** — init repo, premier commit, push, configuration déploiement (ex. Vercel), vérification que le déploiement se fait et que la page répond. S’assurent que le repo est bien nommé après la société et que l’URL de prod est connue. Responsible (R) sur les étapes 1–7 de la checklist.
- **Dev Django / Designer** : fournissent le code de la landing ; consultés (C) pour la structure du projet (fichiers à inclure dans le premier commit). Peuvent vérifier en local que la landing s’affiche avant push.
- **Chef de Projet** : Accountable (A) pour la validation finale ; s’assure que la checklist (étapes 1–8) est accomplie et que DevOps / Architecte réseau ont bien tout créé et actionné ; valide le livrable avant remise au prospect.

---

## 4. Où enregistrer l’URL et le nom du repo

- **URL de la landing** : dans le dossier contact (ex. `docs/contacts/p4s-archi/README.md`) ou dans un registre des landings si existant.
- **Nom du repo** : documenter dans la même fiche contact ou dans `docs/base-de-connaissances/decisions.md` (ex. « Landing P4S : repo `LPPP_P4S-Architecture`, URL https://... »).

---

## 5. Avis à l’équipe technique (repos créés par le Chef de Projet / utilisateur)

Quand le Chef de Projet (ou l’utilisateur) **crée lui-même les repos** (GitHub + GitLab, sans README) pour une landing :

- **Documenter** dans la fiche contact (ex. `docs/contacts/p4s-archi/README.md`) : nom du repo, URLs GitHub et GitLab, et préciser « sans README ».
- **Avis à l’équipe technique** : « Repos [nom] créés sur GitHub et GitLab, sans README. **C’est aux agents DevOps et Architecte réseau de se charger de ça et de tout créer et actionner** : git init (ou copier le code landing), premier commit, push vers origin (GitHub) et gitlab (GitLab), configurer Vercel sur ce repo, vérifier déploiement et page OK. » Voir checklist § 2 (étapes 2–8).
- **Exemple (P4S)** : repo **LPPP_P4S-Architecture** — GitHub `LucasTymen/LPPP_P4S-Architecture`, GitLab `LucasTymen/lppp_p4s-architecture`. Contenu préparé dans `deploy/standalone-p4s/` (app Next.js, page unique à `/`). Push effectué ; Vercel (lppp-p4-s-architecture) build au push. Pour refaire : `make push-standalone-p4s` (WSL/Git Bash) ou voir `deploy/README-standalone.md`. Fiche : `docs/contacts/p4s-archi/README.md` § « Repo landing P4S ».

---

## 6. Stratégie fluide Git + Vercel (réutilisable pour 10+ projets)

Pour appliquer **sans erreur** à chaque nouveau projet : suivre la **checklist unique** dans **`strategie-deploiement-git-vercel.md`** (ordre des étapes, pièges à éviter, push sur les deux remotes, Root Directory Vercel). En cas de blocage (404, push oublié, conflit repo) : **`erreurs-et-solutions.md`**.

---

## 7. Références croisées

- **Génération landing (contenu + hero)** : `generation-landing-nextjs-contenu-hero.md` — contenu depuis JSON contact, hero image/parallax/scanlines par défaut ; à appliquer dès la création de la landing.
- **Stratégie fluide** : `strategie-deploiement-git-vercel.md` — checklist par projet, réutilisable pour 1, 2, … 10+ landings.
- **Erreurs connues** : `erreurs-et-solutions.md` (Vercel 404, push GitLab, conflit README).
- **RACI** : `agents-roles-responsabilites.md` — tâches « Initialiser repo landing par société », « Vérifier déploiement et page OK » (DevOps R, Chef de Projet A).
- **Workflow** : Phase 4 (Validation) et Phase 5 (Déploiement) incluent cette procédure ; Phase 5 étendue avec repo au nom de la société + vérification page.
- **Règles** : `.cursor/rules/devops.mdc`, `.cursor/rules/pilotage-agents.mdc` — étape « fin de landing » rappelée.

---

*Document créé pour que l’équipe s’en rappelle et retrouve facilement chaque landing via un repo au nom de la société, avec déploiement et page vérifiés. Dernière mise à jour : 2025-01-30.*
