# Landing ACKURACY (Next.js)

Contenu depuis `src/content/landing.json` (aligné sur `docs/contacts/ackuracy/landing-proposition-alexis.json`). Qualité P4S : nav sticky, sections numérotées, popup contact, Stack, Coordonnées.

**En local** : `npm run dev` → **http://localhost:3001** (port 3000 réservé à Flowise, voir `docs/base-de-connaissances/infra-devops.md` § 3.4 Ports).

**Pour voir les changements sur Vercel** : la version déployée est celle du repo GitHub (LPPP_Ackuracy). Il faut **copier ce dossier** vers le repo puis **push** :

- **PowerShell** : voir `deploy/README-standalone.md` § ACKURACY (Copy-Item, git add, commit, push).
- **Bash** : `bash deploy/push-standalone-ackuracy.sh` (puis push à la main si besoin d’auth).

Sans ce push, l’URL Vercel affiche l’ancienne version.
