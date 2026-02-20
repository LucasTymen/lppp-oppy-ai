# Procédure : faire apparaître les modifications sur les landing pages

**Pour** : Équipe technique (Dev Django, DevOps).  
**Contexte** : Les modifications apportées aux landing pages (contenu, style, fond hero) ne s'affichent pas tant que le **contenu n'est pas en base** et que le **navigateur ne recharge pas sans cache**. Cette procédure est à appliquer immédiatement.

**Important** : Cette procédure concerne **Django** (URL `/p/<slug>/`, ex. `/p/p4s-archi/`). La landing P4S sur **Vercel** est une **version Next.js** distincte, à l’URL `/p4s-archi` sur le domaine Vercel du projet ; voir `deploiement-vercel-frontend.md` (§ 6 « Où voir la landing P4S sur Vercel »).

---

## 1. Pourquoi les changements ne s'affichent pas

| Cause | Explication |
|-------|-------------|
| **Contenu en base** | La landing affiche le `content_json` **stocké en base** (modèle `LandingPage`). Modifier uniquement le fichier JSON (ex. `landing-proposition-joel.json`) **ne met pas à jour la base**. |
| **Cache navigateur** | Le navigateur peut mettre en cache la page ; un simple F5 peut afficher l’ancienne version. |

---

## 2. Procédure à appliquer (équipe technique)

### A. Après modification du fichier JSON (ex. P4S)

1. **Mettre à jour la base** avec le contenu du fichier :
   ```bash
   python manage.py create_landing_p4s --update
   ```
   Dans Docker :
   ```bash
   docker compose exec web python manage.py create_landing_p4s --update
   ```
2. **Recharger la page** en forçant l’absence de cache : **Ctrl+Shift+R** (Windows/Linux) ou **Cmd+Shift+R** (Mac), ou onglet DevTools → réseau → « Désactiver le cache » puis recharger.

### B. Après modification des templates (HTML/CSS)

- Les templates sont rechargés à chaque requête en **DEBUG**. Si vous utilisez **Gunicorn** (prod ou docker), redémarrer le worker pour prendre en compte les changements :
  ```bash
  docker compose restart web
  ```
- Toujours **recharger sans cache** (Ctrl+Shift+R) pour voir les changements.

### C. Après déploiement : rendre la landing publique

Pour que la landing soit **visible** (plus de 404 sur `/p/p4s-archi/`), elle doit être **publiée** en base (`is_published=True`). Après un déploiement (nouvelle base ou premier déploiement) :

```bash
# En local
python manage.py create_landing_p4s --update --publish

# Avec Docker
make landing-p4s
# ou : docker compose exec web python manage.py create_landing_p4s --update --publish
```

Cela crée ou met à jour la landing P4S et la marque comme **publiée**. À refaire après chaque déploiement si la base a été réinitialisée.

### D. 404 sur toutes les landings (base vide) — réparation

Si **toutes** les pages `/p/<slug>/` (Casapy, FitClem, etc.) renvoient **404 « No LandingPage matches the given query »** : la base ne contient plus les entrées `LandingPage` (volume recréé, prod réinitialisée, etc.). **Aucun bug de code** : une seule logique sert toutes les landings ; la 404 vient de l’absence de ligne en base.

**Réparation (même système pour toutes) :**

1. **Migrations** (recréent Maisons-Alfort, Yuwell) :  
   `docker compose exec web python manage.py migrate --noinput`
2. **Recréer les landings « générateur »** (Casapy, FitClem, Promovacances, P4S) :  
   `make landings-restore`  
   (ou en prod : exécuter les commandes `create_landing_casapy --update --publish`, etc., ou restaurer un backup SQL.)

Après quoi toutes les URLs `/p/casapy/`, `/p/fitclem/`, `/p/promovacances/`, `/p/p4s-archi/`, etc. refonctionnent. Voir `erreurs-et-solutions.md` § « 404 No LandingPage » et § « container name already in use ».

### E. Headers anti-cache (déjà en place)

- La vue `landing_public` envoie les en-têtes **Cache-Control**, **Pragma** et **Expires** pour limiter la mise en cache du navigateur. Après déploiement, les rechargements devraient afficher la dernière version sans avoir à vider le cache manuellement à chaque fois.

### F. Système unifié (moteur de landings)

- **Une seule logique** dans `landing_public` : pour tout slug, le contenu est chargé depuis **`docs/contacts/<slug>/landing-proposition-<slug>.json`** si le fichier existe, sinon depuis **`content_json`** en base. Aucune branche `if slug == "x"` pour le chargement du contenu.
- **Options par slug** (assets, dashboard audit) restent injectées après coup (ex. Casapy : `casapy_assets_url` ; tout slug avec `audit-dashboard.json` : `audit_dashboard_url`). Aucune branche ne peut « casser » les autres landings.

---

## 3. Récapitulatif à communiquer

- **Modification du contenu (texte, hero_background_url, etc.)** → Éditer le JSON **puis** lancer `create_landing_p4s --update` (ou la commande équivalente pour la landing concernée).
- **Modification du template ou du style** → Redémarrer le serveur web si besoin, puis recharger la page **sans cache** (Ctrl+Shift+R).
- **Headers** : Les réponses de la vue landing publique sont envoyées avec des en-têtes anti-cache pour que les modifications soient visibles immédiatement après mise à jour de la base.

---

## 4. Fichiers concernés

- **Vue** : `apps/landing_pages/views.py` — logique unifiée (fichier `landing-proposition-<slug>.json` ou `content_json`), headers anti-cache, options par slug (assets, audit_dashboard_url).
- **Commandes** : `create_landing_casapy`, `create_landing_fitclem`, `create_landing_promovacances`, `create_landing_p4s` (option `--update --publish`).
- **Restauration globale** : `make landings-restore` (après base vide).
- **JSON par contact** : `docs/contacts/<slug>/landing-proposition-<slug>.json` (ex. casapy, fitclem, promovacances) ; P4S : `landing-proposition-joel.json` dans p4s-archi (convention différente, contenu en base après `create_landing_p4s`).

---

## 5. Diagnostic : les modifs ne s'affichent jamais (Casapy / template)

Si après rafraîchissement et vidage du cache les changements n'apparaissent toujours pas (ex. `/p/casapy/`) :

- **Vérifier que Django sert la page** : titre de l'onglet Casapy doit se terminer par **| LPPP** ; un bandeau vert « Page servie par Django LPPP — template à jour » (sticky en haut au scroll) doit apparaître ; code source (Ctrl+U) doit contenir **LPPP proposition.html**. Sinon, la page ne vient pas de ce Django.
- **Vérification côté serveur** (si le navigateur ne montre pas les marqueurs) : `curl -s http://127.0.0.1:8010/p/casapy/` — si la sortie contient « | LPPP » et « Page servie par Django », le serveur est à jour et le blocage est **côté client** (cache ou Service Worker).
- **Contourner le cache navigateur** : 1) `docker compose restart web`. 2) Ouvrir une **fenêtre de navigation privée** (Ctrl+Shift+P) et aller sur http://localhost:8010/p/casapy/ — si le bandeau vert et « | LPPP » apparaissent, le blocage venait du cache ou d'un Service Worker. 3) Effacer les données du site pour localhost:8010 (Firefox : Outils > Gestionnaire d'applications > Stockage ; Chrome : Application > Stockage) ; ou désactiver tout Service Worker enregistré pour ce site.
- **Si le marqueur apparaît** : la page est bien servie par Django ; si un bloc manque, vérifier le JSON et les conditions du template.
- **Cartographie des deux pages Casapy** : voir `cartographie-pages-casapy-paralleles.md` (Page A = Django dynamique sur localhost:8010, Page B = export statique deploy/LPPP-Casapy pour Vercel/file://).

---

*Procédure créée à la demande utilisateur. À appliquer par l’équipe technique immédiatement. Dernière mise à jour : 2026-01-30.*
