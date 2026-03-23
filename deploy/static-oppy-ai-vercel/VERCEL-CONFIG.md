# Config Vercel — lppp-oppy-ai

Le repo **lppp-oppy-ai** contient le monorepo LPPP (Django + frontend Next.js).  
Sans config : Vercel lance `next build` → erreur « Couldn't find pages or app ».

## Solution : Root Directory (OBLIGATOIRE)

Dans **Vercel** → Projet **lppp-oppy-ai** → **Settings** → **General** :

| Paramètre       | Valeur |
|-----------------|--------|
| **Root Directory** | `deploy/static-oppy-ai-vercel` |
| **Framework Preset** | **Other** |
| **Build Command** | (vide — Override) |
| **Output Directory** | `.` |

**Important** : Root Directory doit pointer sur ce dossier. Sinon Vercel build depuis la racine (frontend Next.js) et échoue.

Le `package.json` ici contient un `vercel-build` no-op au cas où Vercel exécute une commande de build.
