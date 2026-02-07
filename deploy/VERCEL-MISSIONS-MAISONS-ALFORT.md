# Vercel — repo LPPP_Missions_mairie_m-Alfort

Ce dépôt contient **tout le projet LPPP** (Django). Vercel ne déploie pas une app Django telle quelle : il faut lui indiquer **quel dossier statique** servir.

## Configuration requise sur Vercel

1. **Vercel** → ton projet **LPPP_Missions_mairie_m-Alfort** → **Settings** → **General**.
2. **Root Directory** : renseigner **`deploy/concierge-demo-maisons-alfort`** (puis *Save*).
3. **Build Command** : laisser vide (site statique, pas de build).
4. **Output Directory** : laisser vide (Vercel sert le contenu du Root Directory).
5. **Redeploy** : **Deployments** → sur le dernier déploiement, **⋯** → **Redeploy**.

Après le redeploy, l’URL (ex. `https://lppp-missions-mairie-m-alfort.vercel.app`) doit afficher la page démo **Assistant Ville de Maisons-Alfort** (`index.html`).

## En cas d’erreur de connexion (PR_END_OF_FILE_ERROR)

Peut survenir si le déploiement était en échec ou instable. Après avoir configuré le Root Directory et redeployé, réessayer. Si le problème persiste : vérifier l’onglet **Deployments** (build vert) et l’onglet **Functions / Logs** sur Vercel.

## Référence

- Démo : `deploy/concierge-demo-maisons-alfort/`
- Stratégie déploiement : `docs/base-de-connaissances/strategie-deploiement-git-vercel.md`
