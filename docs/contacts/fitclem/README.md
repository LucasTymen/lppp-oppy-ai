# LPPP-FitClem — Candidature Responsable Marketing Digital

**Nom projet / livrable** : **LPPP-FitClem** (FitClem = marque cible).

**Contexte** : Candidature pour un poste de **Responsable Marketing Digital** chez FITCLEM (marque fitness & bien-être, fondatrice Clémentine Sarlat / Fitclem). Poste basé Paris (75), présentiel. Fourchette 40–54 k€.

**Livrable** : Landing page commerciale **multipage** (candidature) avec :
- Étude marketing (growth, positionnement, PESTEL, SWOT, Porter, concurrentiel)
- Étude SEO (structure prête, données à fournir plus tard)
- Étude iconographique et graphique
- Proposition d’amélioration des KPI
- CTAs sur chaque page

**Source recherche** : `strategie-marketing-fitclem.md` (synthèse) et **`strategie-marketing-fitclem-complet.md`** (intégralité partie 1 + partie 2 : Ads Meta, framework audit, compliance, plan 30/60 j, CRM/email, réécriture CTA, etc.). Le fichier utilisateur **Stratégie Marketing** (échanges Gemini/GPT, ex. Downloads) constitue la source détaillée pour le sprint éditorial (PESTEL, SWOT, Porter, concurrentiel, growth, KPI, message house, A/B tests).

**Audit SEO** : les données brutes sont dans **`audit-seo/`** (JSON/HTML Lighthouse, CSV). La **synthèse business** (manque à gagner, estimation 132–324 k€/an, argument entretien) est dans **`rapport-seo-fitclem-manque-a-gagner.md`** — à utiliser pour la page « Étude SEO » de la landing et l’argumentaire candidature. **Structure diapo** (slides pour présentation ou dossier) : **`diapo-audit-seo-fitclem-structure.md`**.

**Sprint structure (référence)** : `docs/base-de-connaissances/segmentations/2026-02-09-sprint-general-fitclem-landing-multipage.md`  
**Sprint prioritaire (Orchestrateur pilote, rend des comptes)** : `docs/base-de-connaissances/segmentations/2026-02-15-sprint-fitclem-convaincre-embaucher-etude-complete.md` — objectif : convaincre d'embaucher, étude complète exposée, visibilité depuis le fichier JSON (pas de --update).  
**Sprint éditorial / webdesign / infographique** : `docs/base-de-connaissances/segmentations/2026-02-15-sprint-fitclem-editorial-webdesign-infographique.md` — remplir, illustrer, animer le contenu (Rédacteur, Designer, Infographiste, sous Chef de Projet).  
**Sprint « générer la page complète »** : `docs/base-de-connaissances/segmentations/2026-01-30-sprint-general-fitclem-generer-page-complete.md` (contenu réel partout, étude SEO alimentée, infographie InfographicCraft).  
**Sprint graphique et éditorial** : `docs/base-de-connaissances/segmentations/2026-01-30-sprint-fitclem-graphique-editorial.md` — alignement visuel et ton avec fitclem.fr (Soft Wellness / girly).

**Charte graphique (Designer)** : `charte-graphique-fitclem.md` — palette, typo, CSS corporate « Soft Wellness » ; à respecter pour toute landing ou support FITCLEM.

**Contenu landing** : `landing-proposition-fitclem.json` a été enrichi (sprint 2026-02-15) à partir de la stratégie marketing : intro, enjeux (5 pain points), solution (PESTEL/SWOT/Porter/concurrentiel, growth, plan 30/60 j), services détaillés (étude marketing, étude SEO, proposition KPI), mission flash et why_growth_engineer « prêts entretien ». **Pour voir les modifications sur http://localhost:8010/p/fitclem/** : exécuter depuis la racine du projet (WSL ou environnement Django) : **`python3 manage.py create_landing_fitclem --update`** — cela met à jour le `content_json` en base ; sans cette commande, la page affiche l’ancien contenu.

**Carousel chiffres clés** : `key_figures_carousel` (5 KPI + 2 slides graphiques : barre 132–324 k€/an, timeline 30/60 j). Infographie standalone : `infographie-chiffres-cles-fitclem.html`.

**Vidéo hero (fond)** : l’URL est dans `landing-proposition-fitclem.json` (`hero_video_url`). Intégration fluide comme conciergerie Maisons-Alfort (iframe youtube-nocookie, autoplay muet, boucle, `referrerpolicy`, lien « Ouvrir sur YouTube »). Si la landing existe déjà en base, exécuter `python3 manage.py create_landing_fitclem --update` pour appliquer la vidéo.
