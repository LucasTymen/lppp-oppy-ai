# Landing P4S — page statique (la page, pas une app)

Ce dossier contient **la landing P4S en un seul fichier HTML** générée par Django (`manage.py export_landing_static`). C’est exactement la page servie par Django sur `/p/p4s-archi/`.

**Pour mettre à jour la page :**
1. À la racine du repo LPPP :  
   `python manage.py export_landing_static p4s-archi --output deploy/static-p4s-vercel/index.html`
2. Copier le contenu de ce dossier dans le repo **LPPP_P4S-Architecture** (en remplacement de tout le contenu actuel : supprimer l’app Next.js, mettre uniquement `index.html` + `vercel.json`).
3. Commit + push vers GitHub (et GitLab). Vercel déploiera la page statique.

**Sur Vercel :** Framework Preset = **Other**, Build Command = vide, Output Directory = `.` (ou laisser par défaut). Aucun build : Vercel sert directement `index.html`.
