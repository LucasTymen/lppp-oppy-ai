# LPPP — Projet Casapy

**Nom projet** : **LPPP-Casapy** (Casapy = cible / marque).

**Contexte** : Nouveau projet LPPP démarré le 2026-01-30. Objectif et livrables à préciser avec l’utilisateur (landing, prospection, rapport, autre).

**Segmentation de lancement** : `docs/base-de-connaissances/segmentations/2026-01-30-projet-casapy-lppp.md`

**Rapport SEO (en cours)** :
- **Sprint commun** : `docs/base-de-connaissances/segmentations/2026-01-30-sprint-rapport-seo-complet-casapy-pour-moi-seul.md` — objectif = **rapport complet pour moi seul** (usage interne, détaillé). La version résumée pour présentation sera travaillée **plus tard**.
- Stack technique et notes : `stack-technique-et-notes-seo.md`.
- Éléments du rapport (sources) : `SEO_Casapy_rapport_performances_et_diagnostique.md`, exports crawl (JSON/HTML), CSV (aperçu problèmes, indexabilité, temps de réponse, canoniques, hreflang, pagination, url, interne, externe, codes de réponse).
- **Livrable sprint** : `rapport-seo-complet-casapy-interne.md` (rapport agrégé, complet, interne uniquement).
- **Étude marketing (clean room)** : `etude-marketing-casapy-clean-room.md` — structure anti-hallucination (faits vs hypothèses), champs à compléter, checklist validation. **Constat factuel** : aucune trace de publicité Meta ou Google. 5 éléments factuels à fournir pour version finale béton.
- **Rapport synthétique (présentation)** : pour responsable placement, patron / responsable alternance, référents. **Rédacteur** responsable ; **Expert SEO** référent technique ; **Infographiste** + **chargé chiffres** (Data Analyst / Growth) pour illustrations parlantes et à propos. Brief : `brief-rapport-synthetique-presentation.md` ; sprint : `segmentations/2026-01-30-rapport-synthetique-casapy-presentation.md`. Livrable : `rapport-synthetique-casapy-presentation.md` + visuels dans ce dossier.
- **Visuels slide-ready (4 slides + one-pager)** : générés par `scripts/generate_visuels_casapy.py` (NumPy, Matplotlib). Brief : `brief-visuels-enjeux-casapy-slides.md`. Fichiers : `slide1-impact-perf-business.png`, `slide2-waterfall-ttfb.png`, `slide3-hebergement-comparatif.png`, `slide4-matrice-seo-timeline.png`, `one-pager-dashboard-casapy.png`.

**Dashboard audit performance (template récupérable)** :
- **Template Django** : `templates/landing_pages/casapy_audit_dashboard.html` — dashboard complet (7 blocs : speedometer, timeline utilisateur, compteur pertes, bullet chart, matrice Impact×Effort, waterfall, recovery rings). Code Claude intégré ; le **Chef de Projet** peut récupérer ce fichier et le réinjecter (autre projet, iframe, export statique) sans difficulté.
- **URL** : `http://localhost:8010/p/casapy/audit-dashboard/` (vue `casapy_audit_dashboard`).
- **Utilisation** : liens vers le dashboard à **plusieurs endroits** — (1) **Landing Casapy** (`/p/casapy/`) : nav « Dashboard audit » + CTA sous le bandeau vert ; (2) **Rapport Casapy** (`/p/casapy/rapport/`) : bouton « Voir le dashboard audit performance » + lien dans la nav annexes ; (3) **Nav annexes** (rapport, prospects, proposition) : lien « Dashboard audit » pour le slug casapy.
- **Récupération / réinjection** : copier le contenu du template (HTML/CSS/JS inline) ; ou inclure en iframe depuis cette URL ; ou exporter la réponse HTML en fichier statique pour déploiement hors Django.

**Infographies (InfographicCraft)** :
- `infographie-audit-seo-casapy.html` — TTFB, funnel impact, KPI, plan d'action (effect waouh)
- `infographie-funnel-positionnement-casapy.html` — AARRR, chaîne blocage, positionnement concurrence
- `infographie-casapy-7-formats.html` — 7 formats (speedometer, timeline, lost revenue meter, bullet, heatmap, waterfall, ring) en un seul HTML autonome.

**Landing page** :
- **Segmentation** : `docs/base-de-connaissances/segmentations/2026-01-30-landing-page-casapy.md` (Orchestrateur pilote, toutes parties).
- **Contenu** : `landing-proposition-casapy.json` (hero, intro, enjeux, infographies, CTA, rapport ; logo + vidéo hero depuis `assets-mise-en-forme-casapy.md`).
- **Création en base** : `docker exec lppp_web python manage.py create_landing_casapy --publish`
- **Test Django** : `http://localhost:8010/p/casapy/` — les infographies sont servies via `/p/casapy/assets/<fichier>.png` (vue dédiée).
- **Export statique** : `deploy/LPPP-Casapy/` (index.html, rapport.html, 9 PNG) — procédure push : `deploy/PUSH-CASAPY.md`. Affichage universel (Firefox, Chrome, Safari, mobile) : CSS dans `proposition.html` (infographic-image-wrap, infographic-img, services-segment-infographic).

**À compléter** :
- Objectif principal (ex. : landing candidature, landing commerciale, audit SEO, prospection ciblée)
- Cible (secteur, interlocuteurs, message)
- Livrables attendus (pages, études, déploiement)
- Sources / brief (textes, charte, données à déposer dans ce dossier ou dans `docs/ressources-utilisateur/`)

*Document maintenu par le Chef de Projet / Conseiller. Dernière mise à jour : 2026-01-30.*
