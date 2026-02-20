# Sprint — Infographies Casapy ne s'affichent pas

**Date** : 2026-02-19  
**Équipe** : Chef de projet, Ingénieur système, Graphiste, DevOps  
**Objectif** : Corriger l'affichage des infographies (imports, modules, dépendances, routes).

---

## Diagnostic

| Question | Réponse |
|----------|---------|
| **Les infographies sont-elles « importées » ?** | Oui. Les PNG sont des **fichiers statiques** dans `docs/contacts/casapy/` (slide*.png, one-pager, casapy-wave). Ils ne sont pas « importés » en Python : Django les **sert** via une vue dédiée à l’URL `/p/casapy/assets/<fichier>`. |
| **Modules ou dépendances manquants ?** | **Non.** Aucun module Python supplémentaire : `FileResponse` et `Path` sont dans Django et la lib standard. Côté front, uniquement des balises `<img>` (pas de JS/React à installer). |
| **Pourquoi ça ne s’affichait pas ?** | **Ordre des routes Django** : la route générique `p/<slug:slug>/` était déclarée **avant** `p/casapy/assets/<path:filename>`. Selon la résolution des URLs, les requêtes vers les assets pouvaient être prises pour la page landing et renvoyer du HTML au lieu du PNG. |

---

## Corrections appliquées

1. **URLs** (`apps/landing_pages/urls.py`)  
   - Route **`p/casapy/assets/<path:filename>`** déplacée **au-dessus** de **`p/<slug:slug>/`** pour que les requêtes `/p/casapy/assets/slide1-impact-perf-business.png` soient toujours gérées par `serve_casapy_asset` et renvoient le PNG.

2. **Vérifications**  
   - Les 9 PNG sont bien présents dans `docs/contacts/casapy/`.  
   - La vue `serve_casapy_asset` sert depuis ce dossier (path traversal bloqué, Content-Type `image/png`).  
   - Aucune dépendance Python ou front supplémentaire nécessaire.

---

## Checklist équipe (pour que tout se passe bien)

| Rôle | Vérification |
|------|----------------|
| **Ingénieur système** | Après `runserver`, tester : `http://localhost:8010/p/casapy/assets/slide1-impact-perf-business.png` → doit renvoyer l’image. Si 404 : vérifier `BASE_DIR`, que le projet est lancé depuis la racine du repo, et que les PNG sont bien dans `docs/contacts/casapy/`. |
| **Chef de projet** | Landing Casapy doit être **publiée** pour que `/p/casapy/` soit visible : `python manage.py create_landing_casapy --publish` (ou `--update` si déjà créée). Sans ça, la page renvoie 404 (les assets restent accessibles si l’URL est appelée directement). |
| **DevOps / Déploiement** | **Vercel** : les infos sont dans l’export statique. Régénérer : `python manage.py export_landing_static casapy --json docs/contacts/casapy/landing-proposition-casapy.json --output deploy/LPPP-Casapy/index.html` puis push du dossier `deploy/LPPP-Casapy` (voir `deploy/PUSH-CASAPY.md`). Les PNG doivent être à la racine du déploiement avec `index.html`. |

---

## Commandes utiles

```bash
# 1. Créer / publier la landing Casapy (si pas déjà fait)
python manage.py create_landing_casapy --publish

# 2. Régénérer les visuels PNG (si modif script ou spec)
python scripts/generate_visuels_casapy.py --output docs/contacts/casapy

# 3. Lancer Django puis ouvrir http://localhost:8010/p/casapy/
python manage.py runserver 8010

# 4. Tester un asset directement (doit afficher l’image)
# Navigateur : http://localhost:8010/p/casapy/assets/slide1-impact-perf-business.png

# 5. Pour Vercel : régénérer l’export puis push deploy/LPPP-Casapy
python manage.py export_landing_static casapy --json docs/contacts/casapy/landing-proposition-casapy.json --output deploy/LPPP-Casapy/index.html --rapport-md docs/contacts/casapy/rapport-complet-casapy.md
cd deploy/LPPP-Casapy && git add . && git commit -m "fix: infographies + route assets" && git push origin main
```

---

*Sprint exécuté : route assets prioritaire, pas de module manquant, procédure vérifiée.*
