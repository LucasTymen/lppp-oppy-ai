# Rapport Lighthouse — Landing /p/maisons-alfort/ (Conciergerie IA)

**Date** : 2026-02-06  
**URL** : http://localhost:8010/p/maisons-alfort/  
**Contexte** : Partagé pour l’**Expert SEO**, le **DevOps** et le **Chef de projet** — scores non brillants, actions à prioriser.

---

## 1. Scores (Lighthouse 13.0.1, mobile, 4G lente)

| Catégorie        | Score | Statut   |
|------------------|-------|----------|
| **Performances** | 41    | À traiter |
| **Accessibilité**| 100   | OK       |
| **Bonnes pratiques** | 90 | OK    |
| **SEO**          | 41    | À traiter |

---

## 2. Métriques Performances (détail)

| Métrique | Valeur  | Cible / remarque |
|----------|---------|-------------------|
| First Contentful Paint (FCP) | 29,8 s | Très élevé |
| Largest Contentful Paint (LCP) | 30,1 s | Très élevé |
| Total Blocking Time (TBT) | 0 ms | OK |
| Cumulative Layout Shift (CLS) | 0,281 | À améliorer (< 0,1) |
| Speed Index (SI) | 29,8 s | Très élevé |

**Diagnostic Lighthouse (Performances)** :
- Réduire les ressources **JavaScript inutilisées** (économies estimées ~2 942 Kio).
- Réduire les ressources **CSS inutilisées** (~32 Kio).
- Éviter d’énormes charges utiles réseau : **taille totale ~5 638 Kio**.
- Réduire le temps d’exécution JavaScript (~1,5 s) et le travail du thread principal (~2,9 s).
- **8 tâches longues** sur le thread principal.

**Contexte technique** : La page inclut une **iframe Flowise** (chatbot) chargée depuis `localhost:3010`. Le bundle React/JS de Flowise pèse lourd et participe fortement au FCP/LCP et au poids total. Les améliorations côté LPPP (meta, structure) n’allègent pas le contenu de l’iframe.

---

## 3. SEO — problèmes relevés

- **Le document ne contient pas d’attribut `meta description`** → corrigé dans le template `concierge_maisons_alfort.html` (meta description ajoutée).
- **Rédigez votre code HTML de sorte à autoriser les robots d’exploration à analyser le contenu** → vérifier qu’aucune balise ou directive ne bloque l’indexation (ex. `noindex` non voulu, contenu critique accessible au HTML).

Autres points à vérifier manuellement (hors scope Lighthouse automatique) : structure des titres (H1/H2), URLs canoniques, données structurées si pertinent.

---

## 4. Répartition des actions (RACI)

| Rôle | Actions recommandées |
|------|----------------------|
| **Expert SEO** | Vérifier après déploiement que la **meta description** est bien prise en compte ; valider la crawlabilité et la structure du contenu (titres, texte visible). Consulter `docs/base-de-connaissances/expert-seo-demarche-rapport-wording-copywriting.md` et bonnes pratiques SEO du projet. |
| **DevOps** | **Performances** : analyser la part due à l’iframe Flowise vs au reste de la page ; envisager **chargement différé (lazy)** de l’iframe (ex. `loading="lazy"` ou chargement au scroll / après FCP) pour améliorer FCP/LCP de la page hôte ; durées de cache, compression. Si Flowise est servi derrière le même domaine en prod, évaluer options (inline critical CSS, defer scripts côté landing). |
| **Chef de projet** | Prioriser les correctifs (SEO déjà partiellement traité ; perf = choix entre lazy iframe, acceptation du coût Flowise, ou optimisation côté Flowise). Valider la cible de scores pour la landing (ex. SEO > 80, Perf selon contrainte métier). |

---

## 5. Correctif déjà appliqué (2026-02-06)

- **Template** `templates/landing_pages/concierge_maisons_alfort.html` : ajout de la balise **`<meta name="description" content="...">`** pour corriger l’audit SEO « meta description manquante ». Re-lancer Lighthouse après déploiement pour mesurer l’impact sur le score SEO.

---

## 6. Références

- **Rapport SEO prospect** : `docs/base-de-connaissances/rapport-seo-prospect.md`
- **Expert SEO / bonnes pratiques** : `docs/base-de-connaissances/expert-seo-demarche-rapport-wording-copywriting.md`, `docs/bonnes-pratiques.md`
- **Stratégie qualité** : `docs/base-de-connaissances/strategie-qualite-contenu-landings.md`
- **Landing Conciergerie** : `docs/base-de-connaissances/chatbot-conciergerie-resume-probleme-setup-config.md`
