# Mettre en ligne la landing P4S (la page, pas une app)

Le repo **LPPP_P4S-Architecture** contient **un seul fichier HTML** : la page rendue par Django (`/p/p4s-archi/`), avec **tous les degrés de personnalisation** (hero background, style perso ou thème CSS Vampire, contenu complet). Voir `docs/base-de-connaissances/reconstitution-landing-p4s-personnalisation.md`.

## 1. Régénérer la page (après modification du contenu ou du thème)

À la racine du repo LPPP :

```bash
python manage.py export_landing_static p4s-archi --output deploy/static-p4s-vercel/index.html --rapport-md docs/contacts/p4s-archi/etude-concurrentielle-pestel-swot-porter.md
```

- Sans `--json` si la landing est en base ; avec `--json docs/contacts/p4s-archi/landing-proposition-joel.json` en secours.
- `--rapport-md` génère **rapport.html** (version intermédiaire : société, stratégie, PESTEL/SWOT/Porter) et affiche le lien « Consulter le rapport complet » sur la landing. Sans cette option, le lien rapport est masqué.

Puis copier dans le repo de déploiement :

```powershell
Copy-Item deploy\static-p4s-vercel\index.html deploy\repo-p4s\
Copy-Item deploy\static-p4s-vercel\rapport.html deploy\repo-p4s\
```

## 2. Pousser vers GitHub / GitLab

Depuis un terminal où tu es **connecté à GitHub** :

```bash
cd c:\home\lucas\tools\homelucastoolsLandingsPagesPourProspections\deploy\repo-p4s
git add .
git commit -m "Landing P4S — page statique (export Django)"
git push -u origin main
git push gitlab main
```

(Si le remote `gitlab` n’existe pas : `git remote add gitlab git@gitlab.com:LucasTymen/lppp_p4s-architecture.git` puis `git push -u gitlab main`.)

## 3. Vercel

Dans le projet Vercel **lppp-p4-s-architecture** :  
**Framework Preset** = **Other**, **Build Command** = vide (Override). Pas de build : Vercel sert directement `index.html`.

Après le push, recharger https://lppp-p4-s-architecture.vercel.app/ — tu vois la landing complète (nav, hero, enjeux, solution, services, lien « Consulter le rapport » → rapport.html, stack, mission flash, coordonnées). L’email est affiché en dur (copiable) ; pas de lien mailto.
