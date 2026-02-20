# Cartographie des deux pages Casapy parallèles (DevOps)

**Rôle** : DevOps / Ingénieur système.  
**Contexte** : L’utilisateur constate que les modifications du template Casapy ne s’affichent jamais sur `http://localhost:8010/p/casapy/` malgré rafraîchissement et vidage du cache. Hypothèse : **deux pages parallèles** (deux sources de vérité) — une dynamique (Django), une figée (export statique). Cette cartographie décrit les deux flux, comment les distinguer et comment éviter la confusion.

**Consignation des erreurs** : si des erreurs sont identifiées pendant une cartographie ou un diagnostic, le **responsable de la consignation des erreurs** (agent qui assiste le Chef de Projet) doit les **répertorier** dans `erreurs-et-solutions.md`. Voir § « Cartographie collaborative » ci-dessous.

---

## 1. Les deux pages parallèles

| Critère | **Page A — Dynamique (Django)** | **Page B — Statique (export)** |
|--------|----------------------------------|---------------------------------|
| **Nom court** | Django Casapy | Export Casapy |
| **Source de vérité** | Template `templates/landing_pages/proposition.html` + JSON `docs/contacts/casapy/landing-proposition-casapy.json` (lus à chaque requête) | Fichier **figé** `deploy/LPPP-Casapy/index.html` (snapshot au moment de l’export) |
| **Génération** | Vue `landing_public` (slug `casapy`) → rendu à la volée | Commande `export_landing_static casapy --json ... --output deploy/LPPP-Casapy/index.html` |
| **URL typique** | `http://localhost:8010/p/casapy/` (Django sur le port 8010) | `file:///.../deploy/LPPP-Casapy/index.html` ou domaine Vercel (ex. `lppp-casapy.vercel.app`) |
| **Qui sert la réponse** | Conteneur **lppp_web** (Gunicorn) ou `python manage.py runserver 8010` sur l’hôte | Aucun serveur LPPP sur 8010 pour cette page ; soit navigateur (file://), soit Vercel (HTTPS) |
| **Titre dans le HTML** | Avec marqueur : `... | LPPP` (si template à jour) | Sans marqueur : `Lucas Tymen — Projet Casapy (audit SEO, e-commerce)` (pas de `| LPPP`) |
| **Code source (début)** | Contient `<!-- LPPP proposition.html -->` et titre avec `| LPPP` | Pas de commentaire LPPP ; titre sans `| LPPP` |
| **Bandeau vert** | Oui (si template à jour) : « Page servie par Django LPPP — template à jour » | Non |
| **Mise à jour** | Toute modification du template ou du JSON est visible après rechargement (et sans cache) | Nécessite de **régénérer l’export** puis (pour Vercel) de pousser le dossier `deploy/LPPP-Casapy` |

---

## 2. Qui répond sur `http://localhost:8010/p/casapy/` ?

- **Uniquement Django** (Page A). Aucun autre service du projet LPPP ne sert le chemin `/p/casapy/` :
  - Pas de nginx dans le dépôt.
  - WhiteNoise sert uniquement `STATIC_ROOT` (`staticfiles/`), pas `deploy/LPPP-Casapy/`.
  - L’export statique (Page B) est un fichier sur disque ; il n’est pas servi par Django à l’URL `/p/casapy/`.

Donc : si l’utilisateur ouvre **http://localhost:8010/p/casapy/** et voit un titre **sans** `| LPPP` et **sans** le bandeau vert, alors soit :

1. **Cache navigateur ou Service Worker** : la réponse HTML reçue est une ancienne version (ex. ancienne réponse Django mise en cache, ou SW qui sert un ancien snapshot).
2. **Django sert bien la Page A** mais le navigateur affiche une version mise en cache (y compris dans l’onglet « Débogueur » / code source).

---

## 3. Flux techniques résumés

### Page A — Dynamique (Django)

```
Navigateur  →  GET http://localhost:8010/p/casapy/
            →  lppp_web (Gunicorn) ou runserver 8010
            →  apps.landing_pages.views.landing_public(slug="casapy")
            →  Chargement JSON : docs/contacts/casapy/landing-proposition-casapy.json
            →  Rendu : templates/landing_pages/proposition.html
            →  Réponse HTML (avec marqueurs | LPPP et bandeau si template à jour)
```

- **Port 8010** : exposé par `docker-compose` (`8010:8000` pour le service `web`) ou par `make runserver` (Django en direct sur 8010).
- **Fichiers lus** : template et JSON depuis le montage volume `.:/app` (Docker) ou depuis le répertoire de travail (runserver).

### Page B — Statique (export)

```
Commande : python manage.py export_landing_static casapy \
  --json docs/contacts/casapy/landing-proposition-casapy.json \
  --output deploy/LPPP-Casapy/index.html \
  --rapport-md docs/contacts/casapy/rapport-complet-casapy.md
```

- **Résultat** : `deploy/LPPP-Casapy/index.html` (HTML figé, pas de `| LPPP` ni bandeau).
- **Utilisation** : push du dossier `deploy/LPPP-Casapy` vers le repo standalone (GitHub/GitLab) puis déploiement Vercel (voir `deploy/PUSH-CASAPY.md`). En local : ouverture en `file://` ou via un serveur statique **hors projet** (ex. `python -m http.server` dans `deploy/LPPP-Casapy` → URL serait `http://localhost:XXXX/` et non `.../p/casapy/`).

---

## 4. Comment distinguer rapidement (checklist DevOps)

| Vérification | Page A (Django) | Page B (statique) |
|--------------|------------------|-------------------|
| Titre onglet | Se termine par **\| LPPP** | Pas de `\| LPPP` |
| En-tête contenu | Bandeau vert « Page servie par Django LPPP — template à jour » | Pas de bandeau |
| Code source (Ctrl+U) | Contient **LPPP proposition.html** | Absent |
| URL | `http://localhost:8010/p/casapy/` (ou 127.0.0.1:8010) | `file://...` ou `https://...vercel.app` |

Si l’utilisateur est sur **localhost:8010/p/casapy/** et ne voit pas les marqueurs → traiter comme **cache/Service Worker** (voir § 5).

---

## 5. Actions recommandées (éviter la confusion)

1. **Vérifier ce qui tourne sur 8010**  
   - `docker ps` → conteneur `lppp_web` (Up).  
   - Ou `make runserver` sur l’hôte (port 8010).  
   - Aucun autre processus (autre projet, serveur statique) ne doit écouter sur 8010.

2. **Contourner le cache pour valider la Page A**  
   - `docker compose restart web` (si Docker).  
   - Fenêtre de **navigation privée** (Ctrl+Shift+P) → ouvrir `http://localhost:8010/p/casapy/`.  
   - Vérifier : titre avec `| LPPP`, bandeau vert, code source avec `LPPP proposition.html`.

3. **Ne pas confondre les URLs**  
   - **Local Django** : `http://localhost:8010/p/casapy/` → toujours la Page A.  
   - **Vercel** : URL du déploiement du repo LPPP-Casapy → Page B (export).  
   - **Fichier local** : `file:///.../deploy/LPPP-Casapy/index.html` → Page B.

4. **Mise à jour du contenu**  
   - Pour voir les changements sur **localhost:8010/p/casapy/** : modifier le template ou le JSON, recharger sans cache (et si besoin redémarrer le conteneur web). Pas besoin de réexporter.  
   - Pour mettre à jour la **page déployée (Vercel)** : régénérer l’export (commande ci-dessus), puis push du dossier `deploy/LPPP-Casapy` (voir `deploy/PUSH-CASAPY.md`).

---

## 6. Fichiers et références

| Élément | Fichier ou ressource |
|--------|----------------------|
| Vue Django (Page A) | `apps/landing_pages/views.py` — `landing_public`, `serve_casapy_asset` |
| URLs | `apps/landing_pages/urls.py` — `p/casapy/assets/<path>`, `p/<slug>/` |
| Template | `templates/landing_pages/proposition.html` (marqueurs Casapy : titre `\| LPPP`, bandeau vert) |
| JSON Casapy | `docs/contacts/casapy/landing-proposition-casapy.json` |
| Export statique (Page B) | `deploy/LPPP-Casapy/index.html` — généré par `export_landing_static` |
| Procédure push / déploiement | `deploy/PUSH-CASAPY.md` |
| Diagnostic « modifs pas visibles » | `procedure-modifications-landing-visible.md` § 5 |
| Ports LPPP | `log-commun-lppp-squidresearch.md` (pointeur), § 5.3 — Django LPPP = 8010 |

---

## 7. Cartographie collaborative

Pour cartographier le projet (ports, flux, services), plusieurs rôles peuvent intervenir en parallèle ; chacun fait des tests et apporte son savoir. Les **erreurs identifiées** sont centralisées par le **responsable de la consignation des erreurs** et répertoriées dans `erreurs-et-solutions.md`.

| Rôle | Contribution |
|------|--------------|
| **Pentester** | Nmap du projet (ports ouverts, services), tests de sécurité, travail en binôme avec DevOps. |
| **DevOps** | Flux (Django, static, déploiement), orchestration (Docker, ports), services et protection prod. |
| **Ingénieur système & réseaux** | Expertise Linux et Python, tests, observabilité, processus et checklist. |

Collaboration : Pentester et DevOps coordonnent les tests (nmap + analyse des flux) ; l’Ingénieur système & réseaux apporte son expertise technique (Linux, Python, réseau). Toute erreur ou anomalie découverte pendant ces opérations doit être **remontée** au responsable de la consignation pour **répertoriation** dans le registre (voir en-tête de ce document).

---

---

## Annexe — Résultat d’une exécution non destructive (cartographie)

*Exécution en lecture seule : aucun changement appliqué.*

| Date | Observation |
|------|-------------|
| 2026-01-30 | **Conteneurs** : lppp_web, lppp_db, lppp_redis, lppp_n8n, lppp_flowise, lppp_celery, lppp_celery_beat — tous Up. |
| 2026-01-30 | **Ports en écoute** (netstat) : 8010 (Django), 5433 (PostgreSQL), 6380 (Redis), 5681 (n8n), 3010 (Flowise). Conforme à `docker-compose.yml`. |
| 2026-01-30 | **HTTP** : `GET http://127.0.0.1:8010/p/casapy/` → **200**. Page A (Django) répond correctement. |

Aucune erreur constatée lors de cette exécution ; rien à consigner dans `erreurs-et-solutions.md`.

---

*Cartographie rédigée par DevOps pour analyser et comprendre les deux pages parallèles Casapy. Dernière mise à jour : 2026-01-30.*
