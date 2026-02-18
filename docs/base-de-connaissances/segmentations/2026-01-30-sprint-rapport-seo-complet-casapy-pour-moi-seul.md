# Sprint — Rapport SEO complet Casapy (pour moi seul)

**Date** : 2026-01-30  
**Chef de Projet** : pilote (Accountable)  
**Statut** : 🟡 En cours

**Objectif** : Produire le **rapport SEO complet Casapy** à usage **interne uniquement** (pour moi seul). Version détaillée, exhaustive. Une version résumée pour présentation (intéressante, avec un peu de détail) sera travaillée **plus tard** — hors périmètre de ce sprint.

---

## Périmètre

- **Livrable** : un rapport SEO complet, structuré, qui agrège toutes les analyses et données déjà dans le dossier Casapy. Usage personnel / préparation.
- **Hors périmètre** : la version « à présenter » (résumée, percutante) — à faire dans un second temps.

---

## Sources (dossier `docs/contacts/casapy/`)

| Fichier | Contenu |
|---------|---------|
| `SEO_Casapy_rapport_performances_et_diagnostique.md` | Diagnostic TTFB, infra (o2switch), plan d’action serveur/DB/front, scénarios chiffrés (manque à gagner), formulation pro, questions stratégiques. |
| `stack-technique-et-notes-seo.md` | Stack technique (WordPress, WooCommerce, Elementor, etc.) et note « quelque chose ne va pas ou est manquant ? ». |
| `www.casapy.com-20260218T175921.json` / `.html` | Export crawl (Screaming Frog). |
| `SEO_casapy_rapport_aperçu_problemes.csv` | Synthèse problèmes (canoniques, H1, noindex, titres, meta, images, sécurité, etc.). |
| `SEO_casapy_rapport_indexabilité.csv` | Indexabilité. |
| `SEO_casapy_rapport_temps_de_réponse_(en_secondes).csv` | Temps de réponse. |
| `SEO_casapy_rapport_codes_de_réponse_tous.csv` | Codes de réponse. |
| `SEO_casapy_rapport_versions_canoniques_tous.csv` | Versions canoniques. |
| `SEO_casapy_rapport_hreflang_tous.csv` | Hreflang. |
| `SEO_casapy_rapport_pagination_tous.csv` | Pagination. |
| `SEO_casapy_rapport_url_tous.csv` | URLs. |
| `SEO_casapy_rapport_interne_tous.csv` | Liens internes. |
| `SEO_casapy_rapport_externe_tous.csv` | Liens externes. |

---

## Tâches par rôle

### Expert SEO (Responsible — pilote technique)
- [ ] Structurer le rapport complet (sections : exécutif, stack, crawl/technique, performances/TTFB, indexation/canoniques/H1/titres/meta, liens, sécurité, plan d’action, manque à gagner).
- [ ] Agréger le contenu de `SEO_Casapy_rapport_performances_et_diagnostique.md` et de `stack-technique-et-notes-seo.md` dans le livrable.
- [ ] S’appuyer sur les CSV pour chiffres et listes (problèmes, indexabilité, temps de réponse, etc.) et les intégrer ou résumer dans le rapport.
- [ ] Rédiger ou faire rédiger les parties manquantes (synthèse technique, priorités, recommandations).
- [ ] Livrable cible : `docs/contacts/casapy/rapport-seo-complet-casapy-interne.md` (ou consolidation dans un fichier unique clairement identifié).

### Rédacteur (Consulted)
- [ ] Aider à clarifier et fluidifier les formulations du rapport interne (lisibilité, pas de jargon inutile).
- [ ] Vérifier cohérence des titres et sous-titres.

### Chef de Projet (Accountable)
- [ ] Valider la structure et le périmètre du rapport « pour moi seul ».
- [ ] S’assurer que la version présentation reste hors scope jusqu’à demande explicite.
- [ ] Clôturer le sprint quand le rapport complet interne est livré et validé.

### Data Analyst (optionnel)
- [ ] Si besoin : extraire ou résumer des données des CSV pour les tableaux du rapport (ex. top problèmes, stats indexabilité, temps de réponse).

---

## Livrable

- **Fichier** : `docs/contacts/casapy/rapport-seo-complet-casapy-interne.md`  
  (ou nom explicite équivalent : rapport complet, usage interne uniquement.)

- **Contenu attendu** (à adapter) :
  1. Synthèse / exécutif (2–3 phrases).
  2. Stack technique (référence ou reprise de `stack-technique-et-notes-seo.md`).
  3. Méthodologie (crawl, outils, date).
  4. Audit technique (indexation, canoniques, H1, titres, meta, images, URLs, liens, sécurité) avec renvoi aux CSV et au rapport performances/diagnostique.
  5. Performances (TTFB, LCP, hébergement o2switch, diagnostic serveur).
  6. Plan d’action priorisé (serveur → DB → front-end).
  7. Manque à gagner (scénarios chiffrés, hypothèses, formulation pro).
  8. Annexes / sources (liste des fichiers du dossier Casapy utilisés).

---

## Références

- **Dossier Casapy** : `docs/contacts/casapy/`
- **README Casapy** : `docs/contacts/casapy/README.md`
- **Rapport performances / diagnostique** : `docs/contacts/casapy/SEO_Casapy_rapport_performances_et_diagnostique.md`
- **Stack** : `docs/contacts/casapy/stack-technique-et-notes-seo.md`

---

*Document maintenu par le Chef de Projet. Dernière mise à jour : 2026-01-30.*
