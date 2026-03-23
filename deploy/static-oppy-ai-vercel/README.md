# Landing Oppy-AI (OPPORTUNITY) — page statique

Ce dossier contient **la landing Oppy-AI en fichiers HTML statiques** générés par Django (`manage.py export_landing_static`). Même rendu que Django sur `/p/lppp-oppy-ai/` (thème Oppy cyan, hero CodePen Waves Pins).

**Génération :**
```bash
# À la racine du repo LPPP
python manage.py export_landing_static lppp-oppy-ai --json docs/contacts/lppp-oppy-ai/landing-proposition-lppp-oppy-ai.json --output deploy/static-oppy-ai-vercel/index.html --rapport-md "docs/contacts/lppp-oppy-ai/rapport seo complet.md"
```

**Push vers GitHub (LPPP_OppyAI) :** voir `deploy/PUSH-OPPY-AI.md`.

**Vercel :** Framework = **Other**, Build Command = vide, Output Directory = `.`. La page est servie directement.
