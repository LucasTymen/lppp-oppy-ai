# Génération landing Next.js — contenu et hero appliqués par défaut

**Objectif** : À chaque nouvelle landing Next.js (standalone), appliquer **automatiquement** :
1. **Contenu** depuis le JSON du contact (`docs/contacts/<slug>/landing-proposition-*.json`).
2. **Hero** : image de fond (depuis le JSON ou image par défaut), **parallax** et **scanlines** actifs par défaut.

**Qualité** : même barre que la landing P4S — contenu complet (pas de squelette), contact utilisable (popup si besoin), contenu **100 % dynamique** (un contact = un JSON unique). Voir `strategie-qualite-contenu-landings.md`.

**Référence technique** : `deploy/standalone-ackuracy/` — template de référence (page qui lit `src/content/landing.json`, hero pleine largeur avec fond, overlay, parallax, scanlines).

**Pilotes** : Designer, Dev Django (appliquer à la génération) ; Chef de Projet (vérifier en fin de landing).

---

## 1. Template de référence pour les nouvelles landings

- **Utiliser** `deploy/standalone-ackuracy/` comme base (et non plus uniquement `standalone-p4s` pour les landings « proposition » avec contenu riche).
- Ce template contient :
  - **Contenu** : chargé depuis `src/content/landing.json` (structure alignée sur `schema-landing-proposition.md` : hero_headline, pain_points, services, about_me, mission_flash, etc.).
  - **Hero** : section pleine largeur avec image de fond, overlay assombri, **parallax** (`background-attachment: fixed` sur desktop), **scanlines** (repeating-linear-gradient), actifs par défaut.
- **Image de fond hero** : prise dans le JSON (`hero_background_url`) si renseignée ; sinon une **image par défaut** peut être utilisée (voir § 4 et `template-hero-aerosection.md`).

---

## 2. Contenu : source unique par contact

- **Source de vérité** : `docs/contacts/<slug>/landing-proposition-<prénom ou contact>.json` (ex. `landing-proposition-alexis.json`, `landing-proposition-joel.json`).
- **À la génération** d’une nouvelle landing standalone :
  1. Copier ce fichier vers `deploy/standalone-<slug>/src/content/landing.json` (ou `src/app/landing.json` selon structure).
  2. La page Next.js doit **importer** ce JSON et afficher toutes les sections (hero, pain points, solution, about_me, services, mission_flash, why_growth_engineer, CTA).
- **Cohérence** : le même schéma `content_json` / landing-proposition est utilisé côté Django (commande `create_landing_*`, admin) et côté Next.js (fichier `landing.json`). Voir `schema-landing-proposition.md`.
cd
- **Parallax** : `background-attachment: fixed` sur la section hero (desktop) ; sur mobile, `scroll` pour éviter les soucis de perf (media query déjà dans le template ACKURACY).
- **Overlay** : dégradé assombrissant pour garder le texte lisible.
- **Scanlines** : calque avec `repeating-linear-gradient` (lignes horizontales légères, opacité ~12 %), appliqué par défaut — pas besoin de l’activer manuellement.
- **Détail** : voir `template-hero-aerosection.md` (comportement, où c’est en place, règles CSS).

---

## 4. Image de fond hero (défaut ou personnalisée)

- **Si** `hero_background_url` est renseigné dans le JSON du contact → utiliser cette URL pour le fond de la hero.
- **Si** vide ou absent : utiliser une **image par défaut** (ex. visuel cyber / aérosection) pour que la hero ne soit pas vide. URL par défaut documentée dans `template-hero-aerosection.md` et/ou `sources.md` (décision projet).
- **Implémentation** : dans le template Next.js, soit le CSS lit une variable (injectée depuis le JSON au build), soit un fichier `landing.json` contient toujours une clé `hero_background_url` (éventuellement la valeur par défaut).

---

## 5. Checklist « génération landing » (Chef de Projet / Dev Django / Designer)

| # | Action | Vérification |
|---|--------|----------------|
| 1 | Partir du template `deploy/standalone-ackuracy/` (contenu depuis JSON + hero complète). | Page affiche bien toutes les sections du JSON. |
| 2 | Copier `docs/contacts/<slug>/landing-proposition-*.json` → `src/content/landing.json` (ou équivalent). | Contenu à l’écran = contenu du contact. |
| 3 | Hero : image de fond (JSON ou défaut), parallax + scanlines actifs. | Pas de hero vide ; effet parallax au scroll ; scanlines visibles. |
| 4 | Adapter `layout.tsx` (title, description) et `package.json` (name) pour la société. | SEO et identité cohérents. |
| 5 | Suivre la procédure fin de landing (repo, push, Vercel) : `procedure-fin-landing-repo-deploiement.md`. | URL déployée et page OK. |

---

## 6. Fichiers à aligner

- **Template** : `deploy/standalone-ackuracy/` (référence).
- **Schéma contenu** : `schema-landing-proposition.md`.
- **Hero** : `template-hero-aerosection.md`.
- **Procédure déploiement** : `procedure-fin-landing-repo-deploiement.md`, `deploy/README-standalone.md`.
- **Stratégie fluide** : `strategie-deploiement-git-vercel.md`.

---

*Document créé pour que le contenu et l’image/parallax/scanlines de la hero soient appliqués automatiquement à chaque génération de landing Next.js. Dernière mise à jour : 2025-01-30.*
