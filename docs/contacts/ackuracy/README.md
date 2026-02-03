# Contact : ACKURACY (ackuracy.com)

**Événement source** : Cyber Show Paris  
**Contact clé** : Alexis Clavier (Sales Representative)  
**Segment** : Cyber / Red Team  

---

## Données SEO (Screaming Frog)

Les exports CSV utilisés pour générer le rapport SEO sont dans le dossier **Downloads** de l’utilisateur :

| Fichier | Usage |
|---------|-------|
| `SEO_ackuracy_rapport_interne_tous.csv` | Toutes les URLs crawlées (4 pages : /, /terms, /fr, /privacy) |
| `SEO_ackuracy_rapport_rapport_aperçu_problemes.csv` | Problèmes / opportunités (H1, H2, meta, images, sécurité, etc.) |
| `SEO_ackuracy_rapport_indexabilité.csv` | Statut indexable / non indexable |
| `SEO_ackuracy_rapport_temps_de_réponse_(en_secondes).csv` | Temps de réponse (100 % en 0–1 s) |
| `SEO_ackuracy_rapport_h1_manquant.csv` | Pages sans H1 (/terms, /privacy) |
| `SEO_ackuracy_rapport_h1_multiple.csv` | Pages avec plusieurs H1 (/, /fr) |
| `SEO_ackuracy_rapport_images_texte_alt_manquant.csv` | 35 images sans attribut alt |
| `SEO_ackuracy_rapport_versions_canoniques_manquant.csv` | 4 pages sans balise canonique |
| `SEO_ackuracy_rapport_sécurité_liens_avec_attribut_crossorigin_non_sécurisés.csv` | Liens target="_blank" sans rel="noopener" |

**Option** : copier ces fichiers dans `docs/contacts/ackuracy/pieces/` pour les garder avec le dossier contact, ou laisser en Downloads et indiquer le chemin à l’agent Expert SEO.

---

## Livrables prévus

- **Rapport complet** : `rapport-complet-ackuracy.md` — fiche société + PESTEL/SWOT/Porter + rapport SEO.
- **Étude concurrentielle** : `etude-concurrentielle-pestel-swot-porter.md` — société, produits, concurrence.
- **Landing** : contenu cas par cas (template relance événement ou autre) — Rédacteur, Designer, Chef de Projet.

---

## Livrables réalisés

- **Fiche contact** : `fiche-contact.json` — données contact Cyber Show Paris.
- **Étude PESTEL/SWOT/Porter** : `etude-concurrentielle-pestel-swot-porter.md`.
- **Rapport complet** : `rapport-complet-ackuracy.md` — document unique (société + stratégie + SEO).
- **Landing proposition** : `landing-proposition-alexis.json` — contenu pour Alexis Clavier.
- **Page Next.js** : `frontend/src/app/ackuracy/page.tsx` — landing ACKURACY avec charte Red/Blue/Purple.
- **Package standalone** : `deploy/standalone-ackuracy/` — app Next.js à la racine, `vercel.json` avec `"framework": "nextjs"` (évite l’erreur « No Output Directory public »).

---

## Repo landing ACKURACY (déploiement)

**Repos créés (vides, sans README)** :

| Plateforme | URL | Remarque |
|------------|-----|----------|
| **GitHub** | https://github.com/LucasTymen/LPPP_Ackuracy | Project ID: 78192791 |
| **GitLab** | https://gitlab.com/LucasTymen/lppp_ackuracy | |

**Push depuis la racine du projet LPPP** (ne pas faire `git init` à la racine) :

```bash
# 1. Depuis la racine du projet LPPP
cd "c:\home\lucas\tools\homelucastoolsLandingsPagesPourProspections"

# 2. Supprimer l’éventuel clone précédent
rm -rf deploy/repo-ackuracy

# 3. Cloner le repo GitHub (vide) dans deploy/repo-ackuracy
git clone https://github.com/LucasTymen/LPPP_Ackuracy.git deploy/repo-ackuracy

# 4. Copier le contenu du standalone dans le clone (sans écraser .git du clone)
# WSL / Git Bash :
#   cp -r deploy/standalone-ackuracy/. deploy/repo-ackuracy/
# PowerShell (depuis la racine du projet) :
#   Copy-Item deploy\standalone-ackuracy\* deploy\repo-ackuracy\ -Recurse -Force
#   Copy-Item deploy\standalone-ackuracy\.gitignore deploy\repo-ackuracy\ -Force

# 5. Aller DANS le clone (c’est lui qui sera poussé)
cd deploy/repo-ackuracy

# 6. Commit et push
git add .
git status
git commit -m "Landing ACKURACY standalone — page unique, charte Red/Blue/Purple"
git push -u origin main

# 7. Ajouter GitLab et pousser
git remote add gitlab git@gitlab.com:LucasTymen/lppp_ackuracy.git
git push -u gitlab main
```

**Vercel** : après le push, sur [vercel.com/new](https://vercel.com/new) → Import **LPPP_Ackuracy** (GitHub). **Root Directory** : laisser vide ou `./`. Déployer puis vérifier l’URL (ex. `https://lppp-ackuracy.vercel.app`).

---

## Note sur les données Gemini

Les informations fournies par Gemini sur ACKURACY (conversation Ackuracy) ont été **vérifiées et croisées** avec les données du site (ackuracy.com) et les rapports SEO Screaming Frog. Données non vérifiables (effectifs, CA, part de marché) non reportées. Les noms de personnes (ex. Alexis Clavier) proviennent de la fiche contact fournie par l’utilisateur.

---

**Règle** : un contact = un dossier — `docs/base-de-connaissances/organisation-donnees-contacts.md`.
