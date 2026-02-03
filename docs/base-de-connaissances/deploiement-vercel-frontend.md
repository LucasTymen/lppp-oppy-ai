# Déploiement du frontend Next.js sur Vercel

**Rôle** : Procédure pour déployer le frontend (landing pages) sur Vercel.  
**Référence** : `stack-frontend-nextjs-react.md`, `infra-devops.md`.

**Stratégie fluide (Git + Vercel, 10+ projets)** : pour une checklist unique sans erreur, voir **`strategie-deploiement-git-vercel.md`**. En cas de 404 ou de galère déploiement : **`erreurs-et-solutions.md`**.

---

## 1. Prérequis

- Dépôt LPPP sur **GitHub** (remote `origin`)
- Compte **Vercel** ([vercel.com/lucas-tymens-projects](https://vercel.com/lucas-tymens-projects))
- Frontend Next.js dans `frontend/` à la racine du dépôt

---

## 2. Node.js

Vercel utilise **Node 20** par défaut (ou via `engines` dans `package.json`). Le frontend requiert Node >= 20.9.0 pour Next.js 16. En local, si tu as Node 18 : utilise `nvm use 20` ou installe Node 20.

---

## 3. Créer la page sur GitHub

1. **Pousser le code** sur GitHub :
   ```bash
   git add .
   git status   # vérifier les fichiers
   git commit -m "feat: frontend Next.js + page P4S-archi"
   git push origin main
   ```

2. Le frontend contient :
   - `frontend/` — app Next.js
   - `frontend/src/app/p4s-archi/page.tsx` — page P4S
   - **Root Directory** : à configurer dans **Vercel Dashboard** → Project Settings → Build and Deployment → **Root Directory** = `frontend` (le schéma Vercel n’accepte plus `rootDirectory` dans `vercel.json`).

---

## 3. Déployer sur Vercel

### Option A : Import depuis le dashboard Vercel

1. Aller sur [vercel.com/new](https://vercel.com/new)
2. **Import Git Repository** : sélectionner le dépôt LPPP (GitHub)
3. **Configure Project** :
   - **Root Directory** : `frontend` (obligatoire pour le monorepo)
   - **Framework Preset** : Next.js (auto-détecté)
   - **Build Command** : `npm run build` (par défaut)
   - **Output Directory** : `.next` (par défaut)
4. **Environment Variables** (optionnel) :
   - `NEXT_PUBLIC_CONTACT_EMAIL` = ton adresse email (pour que le CTA mailto pointe vers toi)
5. Cliquer sur **Deploy**

### Option B : CLI Vercel

```bash
cd frontend
npx vercel
# ou, si déjà configuré :
npx vercel --prod
```

Pour le monorepo, configurer le **Root Directory** dans le projet Vercel (Dashboard → Project Settings → General → Root Directory = `frontend`).

---

## 5. URLs après déploiement

- **Page d'accueil** : `https://<projet>.vercel.app/`
- **Page P4S** : `https://<projet>.vercel.app/p4s-archi`

---

## 6. Où voir la landing P4S sur Vercel (pour les types techniques)

Le **dashboard Vercel** affiche la liste des **projets**, pas des routes. La landing P4S n’apparaît pas comme une entrée séparée : elle est une **route** du projet.

| Ce que tu vois sur Vercel | Ce que c’est |
|---------------------------|---------------|
| **Projet** « landing-page-creator-for-prospection » | C’est le frontend Next.js (monorepo, `rootDirectory: "frontend"`). |
| **URL du projet** (ex. `landing-page-creator-for-prospectio.vercel.app`) | Accueil Next.js. Depuis là : lien « Page P4S-archi » ou URL directe `/p4s-archi`. |
| **Page P4S** | `https://<projet>.vercel.app/p4s-archi` — à ouvrir dans le navigateur, pas listée dans le dashboard. |

**Si la page P4S ne s’affiche pas ou renvoie 404 (y compris « 404: NOT_FOUND » / `DEPLOYMENT_NOT_FOUND`) :**

C’est en général parce que Vercel build depuis la **racine du dépôt** au lieu de `frontend/`. Il n’y a pas d’app Next.js à la racine → pas de déploiement valide → 404.

**À faire (priorité 1) :**

1. **Vercel** → projet **landing-page-creator-for-prospection** → **Settings** → **General**.
2. **Root Directory** : cliquer **Edit**, saisir `frontend` (sans slash final), **Save**.
3. **Redeploy** : onglet **Deployments** → **…** sur le dernier déploiement → **Redeploy** (ou pousser un commit sur la branche liée).
4. Attendre la fin du build, puis réessayer : `https://landing-page-creator-for-prospectio.vercel.app/p4s-archi`.

**Si ça persiste :**

- **Build** : vérifier que le dernier déploiement est **Ready** (pas Failed). Si Failed, ouvrir les logs pour voir l’erreur (souvent Node, dépendances ou chemin).
- **Route** : la page est définie par `frontend/src/app/p4s-archi/page.tsx` ; Next.js expose automatiquement `/p4s-archi` une fois le build fait depuis `frontend/`.

**Landings standalone (un projet, pas de hub)** : la page d'accueil `/` est neutralisée (aucun lien vers les landings). Chaque prospect n'arrive que par lien direct (ex. `...vercel.app/p4s-archi`). Pas de lien « Accueil » sur les landings. Voir `strategie-landings-standalone-vs-hub.md`.

**Important — quelle page tu veux déployer** :
- **Page P4S standalone (pas de hub)** : repo **LPPP_P4S-Architecture**, projet Vercel **lppp-p4-s-architecture**. C’est ce dépôt et ce projet qu’il faut pousser et déployer pour la landing P4S dédiée. Ne pas utiliser le projet « landing-page-creator-for-prospection » pour la page P4S si tu veux du standalone.
- **Repo principal LPPP** (landingPageCreatorForProspection) : lié au projet Vercel « landing-page-creator-for-prospection » ; les push sur ce repo déclenchent ce projet (ancien setup). Pour éviter le hub, privilégier un repo + projet Vercel par prospect (ex. LPPP_P4S-Architecture → lppp-p4-s-architecture).

**Deux déploiements distincts :**

- **Django (backend LPPP)** : `/p/p4s-archi/` — hébergement propre (ex. Contabo), pas sur Vercel. Rendu complet (Qui je suis, rapport, services). Voir `procedure-modifications-landing-visible.md` pour `make landing-p4s`.
- **Vercel (frontend Next.js)** : `/p4s-archi` — version simplifiée, déployée automatiquement à chaque push sur la branche liée.

---

## 7. Variable d'environnement CTA

Pour que le bouton « Reprendre la conversation » envoie l'email vers toi :

1. Vercel Dashboard → Project → **Settings** → **Environment Variables**
2. Ajouter : `NEXT_PUBLIC_CONTACT_EMAIL` = `ton@email.com`
3. Redéployer (ou attendre le prochain déploiement)

Sans cette variable, le CTA ouvre le client mail avec le sujet pré-rempli (l'utilisateur doit saisir son adresse).

---

## 8. Déploiement automatique

Une fois le projet lié à GitHub, **chaque push sur la branche principale** déclenche un déploiement automatique.

---

*Document créé pour le déploiement de la page P4S. Dernière mise à jour : 2025-01-30.*
