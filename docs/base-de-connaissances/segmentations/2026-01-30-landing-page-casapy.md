# Landing page Casapy — Sprint commun

**Date** : 2026-01-30  
**Pilote** : **Orchestrateur** (coordination de toutes les parties).  
**Statut** : 🟡 En cours

**Règle Git** : En clôture, commit + push sur les deux remotes (`make push-both` ou `make commit-push MSG="..."`). Réf. `git-remotes-github-gitlab.md`.

---

## Objectif

Produire une **landing page Casapy** testable (Django `/p/casapy/`), avec :
- **Hero** : vidéo de fond (uniquement hero), overlay + scanlines, parallaxe (réf. FitClem, `assets-mise-en-forme-casapy.md`).
- **Logo** Casapy en header / hero selon maquette.
- **Contenu** : aligné sur le projet (audit SEO, e-commerce, rapport synthétique) ; rédaction pilotée par le Rédacteur, validée par le Chef de Projet.
- **Livrable** : page affichable et testable par l’utilisateur (runserver ou déploiement).

---

## Parties impliquées (RACI)

| Rôle | Responsabilité |
|------|----------------|
| **Orchestrateur** | Pilote ; coordination des livrables ; mise à jour registre / stratégie si besoin. |
| **Chef de Projet** | Scope, priorisation, validation finale. |
| **Rédacteur** | Contenu (hero, intro, enjeux, CTA, coordonnées) ; `landing-proposition-casapy.json` ; bonnes pratiques éditoriales. |
| **Designer** | Intégration logo + vidéo hero, overlay, scanlines, parallaxe ; cohérence visuelle avec `assets-mise-en-forme-casapy.md`. |
| **Développeur Django** | Vue `landing_public` (slug `casapy`), commande `create_landing_casapy`, source JSON depuis `docs/contacts/casapy/`. |
| **Expert SEO** | Titres, meta, structure (H1, liens) ; pas d’invention de données. |
| **Infographiste** (optionnel) | Visuels / chiffres clés si intégrés dans la landing. |
| **DevOps** (optionnel) | Déploiement, URL de test prod si demandé. |

---

## Specs techniques

- **Stack** : Django (app `landing_pages`), template `proposition.html`, contenu depuis `docs/contacts/casapy/landing-proposition-casapy.json`.
- **Assets** : `docs/contacts/casapy/assets-mise-en-forme-casapy.md` — logo URL, vidéo hero URL, comportement (autoplay, muted, loop, overlay, scanlines, parallaxe).
- **Référence** : `deploy/LPPP-FitClem/index.html` et vue FitClem (chargement JSON depuis contact, `hero_video_mp4_url`).
- **URL de test** : `/p/casapy/` (après `python manage.py create_landing_casapy --publish` ou équivalent).

---

## Segmentation des tâches

### 1. Orchestrateur
- [x] Cadrer le sprint et les livrables.
- [ ] S’assurer que toutes les parties ont les infos (registre, assets, brief).
- [ ] En clôture : mise à jour registre / log si nouvelle ressource ou convention.

### 2. Chef de Projet
- [ ] Valider le scope (hero vidéo + logo + contenu minimal pour test).
- [ ] Valider la landing avant livraison à l’utilisateur (test manuel).

### 3. Rédacteur
- [ ] Rédiger / compléter le contenu dans `landing-proposition-casapy.json` (hero_headline, hero_sub_headline, intro, enjeux, CTA, coordonnées).
- [ ] S’appuyer sur `etude-marketing-casapy-clean-room.md`, rapport SEO, `brief-rapport-synthetique-presentation.md` ; pas d’invention.
- [ ] Appliquer `docs/bonnes-pratiques.md` (éditorial anti-détection IA).

### 4. Designer
- [ ] Vérifier l’intégration logo (header/hero) et vidéo hero (overlay, scanlines, parallaxe) selon `assets-mise-en-forme-casapy.md`.
- [ ] Adapter si besoin thème/charte Casapy (couleurs, typo) dans `themes.py` ou via JSON.

### 5. Développeur Django
- [ ] Ajouter le slug `casapy` dans la vue `landing_public` : chargement du JSON depuis `docs/contacts/casapy/landing-proposition-casapy.json` si présent (comme FitClem).
- [ ] S’assurer que `hero_video_mp4_url` (et optionnellement `theme.logo_url`) est disponible pour le template (injection depuis JSON ou depuis assets).
- [ ] Créer la commande `create_landing_casapy` (idempotente, `--update`, `--publish`).
- [ ] Documenter dans le README Casapy comment créer et tester la landing.

### 6. Expert SEO
- [ ] Vérifier `page_title`, meta description, structure H1 / liens dans le contenu fourni.
- [ ] Pas d’invention de chiffres ; renvoyer vers rapport ou « à compléter » si données manquantes.

---

## Livrables

| Livrable | Responsable | Emplacement |
|----------|-------------|-------------|
| Segmentation (ce fichier) | Orchestrateur | `docs/base-de-connaissances/segmentations/2026-01-30-landing-page-casapy.md` |
| Contenu JSON | Rédacteur | `docs/contacts/casapy/landing-proposition-casapy.json` |
| Vue + commande | Dev Django | `apps/landing_pages/views.py`, `management/commands/create_landing_casapy.py` |
| Intégration visuelle | Designer | Template proposition + assets (logo, vidéo) |
| Landing testable | Tous | URL `/p/casapy/` après création en base et `runserver` |

---

## Comment tester

1. Créer la landing : `python manage.py create_landing_casapy --publish`
2. Lancer le serveur : `python manage.py runserver`
3. Ouvrir : `http://127.0.0.1:8000/p/casapy/`
4. Vérifier : hero avec vidéo, overlay, logo, contenu, CTA, lien rapport si présent.

---

*Document piloté par l’Orchestrateur. Dernière mise à jour : 2026-01-30.*
