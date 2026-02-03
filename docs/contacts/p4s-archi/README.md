# Contact : P4S-archi (p4s-archi.com)

**Premier rapport SEO** et **première landing page** pour ce prospect.

---

## Données SEO (Screaming Frog)

Les exports CSV utilisés pour générer le rapport SEO sont actuellement dans le dossier **Downloads** de l’utilisateur :

| Fichier | Usage |
|---------|--------|
| `SEO_rapport_P4S-archi_rapport_aperçu_problemes.csv` | Problèmes / opportunités (H1, H2, contenu, meta, images, sécurité, codes) |
| `SEO_rapport_P4S-archi_temps_de_réponse_(en_secondes).csv` | Temps de réponse (98,86 % en 0–1 s) |
| `SEO_rapport_P4S-archi_codes_de_réponse_externes,_redirection_(3xx).csv` | Redirections 3xx (ex. reseau-entreprendre.org, LinkedIn, uecc-hexatrust) |
| `SEO_rapport_P4S-archi_codes_de_réponse_externes,_erreur_du_client_(4xx).csv` | Erreurs 4xx (ex. bpifrance.fr 403) |
| `SEO_rapport_P4S-archi_codes_de_réponse_tous.csv` | Tous les codes (200, 302, 403, etc.) |

**Option** : copier ces 5 fichiers dans `docs/contacts/p4s-archi/pieces/` pour les garder avec le dossier contact, ou laisser en Downloads et indiquer le chemin à l’agent Expert SEO.

---

## Livrables prévus

- **Rapport SEO** (synthèse) : `rapport-seo.md` — Expert SEO + analyse sémantique.
- **Étude Growth** (funnel + KPIs) : voir segmentation `2025-01-30-premier-rapport-seo-landing-p4s-archi.md`.
- **Landing** : contenu cas par cas (template relance événement ou autre) — Rédacteur, Designer, Chef de Projet.

## Tri rapport PDF (Optimisation Growth)

- **Tri à garder / à vérifier** : `tri-rapport-optimisation-growth-p4s.md` — analyse du PDF « Rapport — Optimisation Growth pour P4S Architecture » : ce qui est sourcé et à garder vs chiffres / affirmations à vérifier ou écarter (risque d’hallucinations). À consulter avant de réutiliser les chiffres du rapport dans le rapport complet ou le teaser.

## Livrables réalisés

- **Rapport complet P4S** : `rapport-complet-p4s.md` — **source unique**, généré une seule fois, trace pour réutilisation. Document unique (société, produits, concurrence, PESTEL/SWOT/Porter + rapport SEO étude initiale & estimation d’impact, priorisation, verdict prospection). Contient les éléments obligatoires : nombre de problèmes (à quantifier), impact, échantillon 5 prospects (à renseigner). **PDF** : export optionnel depuis ce Markdown (ex. pour envoi au prospect après échange) ; ne pas maintenir deux versions.
- **Rapport teaser (public)** : `rapport-teaser-p4s.md` — extrait affiché sur `/p/p4s-archi/rapport/` pour montrer le sérieux et que tu as des données (synthèse + synthèse exécutive SEO + table estimation d’impact), sans dévoiler tout le rapport. Le rapport complet reste en interne.
- **Étude concurrentielle PESTEL-SWOT-Porter** : `etude-concurrentielle-pestel-swot-porter.md` (société, produits, concurrence, verdict prospection) — alimente le rapport complet.
- **Landing page proposition** : `content-json-proposition.md` et **`landing-proposition-joel.json`** — **source unique** du contenu publié (version validée, anciennement codée en dur dans Next.js). Contenu personnalisé pour Joël Courtois (ton courtois et chaleureux, proposition Growth Engineer). Après édition du JSON : synchroniser vers `deploy/standalone-p4s/src/content/landing.json` et `frontend/src/app/p4s-archi/landing.json` ; pour Django : `python manage.py create_landing_p4s --update`.
- **Brief copywriting + CTA** : `brief-seo-growth-designer-copywriting-cta.md` — mission Expert SEO, Growth, Designer pour étudier le copywriting et les mots-clés des call-to-actions.
- **Brief intégration Rédacteur / Style** : `brief-integration-redaction-style.md` — ce qui doit apparaître (Qui je suis, rapport, prospects, proposition de valeur, Paid Media), procédure `create_landing_p4s --update`, checklist.
- **Page Next.js** : `frontend/src/app/p4s-archi/page.tsx` — landing P4S déployable sur Vercel ; contenu chargé depuis `landing.json` (copie de `landing-proposition-joel.json`). Version 4 blocs (hero, Positionnement, Votre activité & besoins, Me contacter). Voir `deploiement-vercel-frontend.md` et `generation-landing-nextjs-contenu-hero.md`.

**Landing complète (Qui je suis, rapport, services, liens)** : consulter l’URL **Django** `/p/p4s-archi/` (backend LPPP). Après toute modif du JSON, lancer `python manage.py create_landing_p4s --update` pour voir les changements.

---

## Repo landing P4S (déploiement)

**Nom du repo** : **LPPP_P4S-Architecture** (au nom de la société, pour retrouver facilement).

| Plateforme | URL | Remarque |
|------------|-----|----------|
| **GitHub** | `https://github.com/LucasTymen/LPPP_P4S-Architecture` | Repo créé **sans README** (prêt pour premier push). |
| **GitLab** | `https://gitlab.com/LucasTymen/lppp_p4s-architecture` | Repo créé **sans README** (prêt pour premier push). |

**Avis à l’équipe technique (déploiement)** : la **page P4S standalone** (pas de hub) se déploie via le repo **LPPP_P4S-Architecture** et le projet Vercel **lppp-p4-s-architecture** — pas via le repo principal ni le projet « landing-page-creator-for-prospection ». Les repos **LPPP_P4S-Architecture** ont été créés sur GitHub et sur GitLab, **sans README**. Prochaines étapes (voir `procedure-fin-landing-repo-deploiement.md`) : initialiser le dépôt local (ou copier le code de la landing P4S dans un dossier dédié), premier commit, push vers `origin` (GitHub) et vers `gitlab` (GitLab si miroir configuré), configurer le déploiement Vercel sur ce repo, vérifier que le déploiement se fait et que la page fonctionne.

**Vercel (landing P4S standalone)** :
- **Code poussé** : repo **LPPP_P4S-Architecture** (GitHub + GitLab) — app Next.js à la racine du repo, page unique à `/`, pas de hub. Contenu préparé dans `deploy/standalone-p4s/`, push effectué.
- Projet Vercel : **lppp-p4-s-architecture** — [Overview](https://vercel.com/lucas-tymens-projects/lppp-p4-s-architecture). Vercel va builder au push ; **Root Directory** = `./` (app à la racine du repo). URL une fois déployé : `https://lppp-p4-s-architecture.vercel.app` (ou domaine assigné).
- **Console LPPP** : pour traquer cette landing avec les autres, renseigner l’URL Vercel dans l’admin (Landing page `p4s-archi` → champ **URL déployée**). Puis consulter **`/console/`** pour voir toutes les landings et leurs URLs (Django + Vercel).

**Règle** : un contact = un dossier — `docs/base-de-connaissances/organisation-donnees-contacts.md`.
