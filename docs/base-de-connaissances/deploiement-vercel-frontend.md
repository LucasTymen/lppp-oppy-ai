# Déploiement du frontend Next.js sur Vercel

**Rôle** : Procédure pour déployer le frontend (landing pages) sur Vercel.  
**Référence** : `stack-frontend-nextjs-react.md`, `infra-devops.md`.

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
   - `vercel.json` (racine) — `rootDirectory: "frontend"` pour le monorepo

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

## 5. Variable d'environnement CTA

Pour que le bouton « Reprendre la conversation » envoie l'email vers toi :

1. Vercel Dashboard → Project → **Settings** → **Environment Variables**
2. Ajouter : `NEXT_PUBLIC_CONTACT_EMAIL` = `ton@email.com`
3. Redéployer (ou attendre le prochain déploiement)

Sans cette variable, le CTA ouvre le client mail avec le sujet pré-rempli (l'utilisateur doit saisir son adresse).

---

## 7. Déploiement automatique

Une fois le projet lié à GitHub, **chaque push sur la branche principale** déclenche un déploiement automatique.

---

*Document créé pour le déploiement de la page P4S. Dernière mise à jour : 2025-01-30.*
