# Étude SEO 0Flaw — Problèmes et manque à gagner

**Contexte** : Société de cybersécurité et de formation (B2B). Analyse pour la prospection 0flow (Samson Fedida).  
**Usage** : Argumentaire landing, rapport d'audit, plan d'action dev/rédacteurs.

---

## 1. Échantillon des problèmes SEO identifiés

| Catégorie | Volume | Détail / Exemple |
|-----------|--------|-------------------|
| **Codes 4xx** | 1 page | Lien cassé vers une ressource e-mail protection (404). |
| **Balises H1 manquantes** | 3 pages | Pages importantes sans H1 → mauvaise hiérarchisation du contenu. |
| **Pages non indexables** | 23 pages | Marquées « Non indexable » → absence des résultats de recherche. |
| **Problèmes divers** | 24 occurrences | Performances, balises manquantes, duplications. |
| **Referrer-Policy manquante** | 155 pages | En-tête Referrer-Policy non configuré → signal sécurité faible. |
| **Temps de réponse** | Plusieurs pages | Réponse en plusieurs secondes → risque rebond et dégradation Core Web Vitals. |
| **Titres de page en doublon** | Plusieurs pages | Même `<title>` sur plusieurs URLs → dilution SEO et confusion. |
| **URLs sans canonique** | Plusieurs pages | Absence de balise canonique → risque contenu dupliqué. |

---

## 2. Hypothèses pour l’estimation (cybersécurité / formation B2B)

| Paramètre | Valeur | Commentaire |
|-----------|--------|-------------|
| **Taux de conversion moyen** | ~2,2 % | Moyenne B2B services techniques (démo, devis, inscription formation). |
| **Valeur moyenne par conversion** | ~250 € | Prudent ; formations et audits cyber peuvent monter bien plus. |
| **CTR organique (top 10)** | ~2 % par page | Si indexée mais mal optimisée. |
| **Visites perdues** | Par type de problème | Estimées à partir de ~100 impressions/jour/page non exploitée × CTR. |

---

## 3. Estimation du manque à gagner SEO

| Problème | Pages concernées (est.) | Visites perdues / mois | Conversions perdues / mois | Manque à gagner / mois |
|----------|------------------------|------------------------|----------------------------|-------------------------|
| Pages non indexables | 23 | ~230 | ~5 | ~1 250 € |
| H1 manquant (mauvais CTR) | 3 | ~60 | ~1 | ~250 € |
| Titres dupliqués | 5 | ~100 | ~2 | ~500 € |
| Liens cassés (4xx) | 1 | ~10 | <1 | ~50 € |
| Absence de canonical | 6 | ~90 | ~2 | ~500 € |
| **Total mensuel estimé** | — | — | — | **~2 500 €** |
| **Total annuel** | — | — | — | **~30 000 €** |

*Source : performances moyennes SEO organique (2 % CTR, hypothèses B2B cybersécurité).*

---

## 4. Priorisation des actions

**Ordre recommandé** (impact business + faisabilité) :

1. **Indexabilité** — Débloquer les 23 pages non indexables (meta robots, blocages, sitemap). Impact maximal sur le trafic et les conversions.
2. **Sécurité et confiance** — Mettre en place Referrer-Policy sur l’ensemble des pages (155). Signal fort pour le secteur cybersécurité.
3. **Contenu et structure** — Corriger les H1 manquants (3) et les titres dupliqués ; ajouter les canoniques sur les URLs concernées.
4. **Technique** — Corriger le lien 4xx (e-mail protection) ; réduire les temps de réponse (performance).
5. **Problèmes divers** — Traiter les 24 occurrences (balises, duplications) selon audit détaillé page par page.

---

## 5. Export tâches SEO (développeurs / rédacteurs)

### 5.1 Bloc développeurs

| Priorité | Tâche | Détail |
|----------|--------|--------|
| P0 | Rendre indexables les pages bloquées | Identifier cause (noindex, robots.txt, autre) pour les 23 pages ; corriger. |
| P0 | Ajouter Referrer-Policy | En-tête HTTP sur l’ensemble du site (ex. `Referrer-Policy: strict-origin-when-cross-origin` ou politique adaptée). |
| P1 | Corriger le lien 4xx | Ressource e-mail protection → corriger ou supprimer le lien. |
| P1 | Canoniques | Ajouter `<link rel="canonical">` sur les pages sans canonique (liste à extraire du crawl). |
| P2 | H1 | Définir un H1 unique et pertinent sur les 3 pages concernées. |
| P2 | Titres uniques | Attribuer un `<title>` unique par page (liste des doublons à fournir). |
| P2 | Performance | Analyser et réduire le temps de réponse des pages lentes (cible < 2 s). |

### 5.2 Bloc rédacteurs / contenu

| Priorité | Tâche | Détail |
|----------|--------|--------|
| P1 | Titres et H1 | Proposer des titres et H1 différenciés et orientés SEO pour les pages à doublons / sans H1. |
| P2 | Contenu | Vérifier que les pages désormais indexables ont un contenu suffisant et non dupliqué. |

---

## 6. Suite possible

- **Plan d’action détaillé page par page** : à générer à partir d’un export Screaming Frog (URLs, statut, type de problème).
- **Rapport complet prospect** : intégrer ce document dans `rapport-complet-0flow.md` (section SEO) si créé. Voir `docs/base-de-connaissances/template-rapport-complet-prospect.md`.
- **Landing 0flow** : utiliser le chiffre **~30 000 € / an** et les problèmes prioritaires comme arguments dans la proposition (Insight Cards, CTA rapport d’audit).

---

*Document créé à partir de l’étude SEO fournie. Hypothèses : B2B cybersécurité et formation. Dernière mise à jour : 2026-01-30.*
