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

### D. Headers anti-cache (déjà en place)

- La vue `landing_public` envoie désormais les en-têtes **Cache-Control**, **Pragma** et **Expires** pour limiter la mise en cache du navigateur. Après déploiement, les rechargements devraient afficher la dernière version sans avoir à vider le cache manuellement à chaque fois.

---

## 3. Récapitulatif à communiquer

- **Modification du contenu (texte, hero_background_url, etc.)** → Éditer le JSON **puis** lancer `create_landing_p4s --update` (ou la commande équivalente pour la landing concernée).
- **Modification du template ou du style** → Redémarrer le serveur web si besoin, puis recharger la page **sans cache** (Ctrl+Shift+R).
- **Headers** : Les réponses de la vue landing publique sont envoyées avec des en-têtes anti-cache pour que les modifications soient visibles immédiatement après mise à jour de la base.

---

## 4. Fichiers concernés

- **Vue** : `apps/landing_pages/views.py` (headers Cache-Control sur `landing_public`)
- **Commande P4S** : `apps/landing_pages/management/commands/create_landing_p4s.py` (option `--update`)
- **JSON P4S** : `docs/contacts/p4s-archi/landing-proposition-joel.json`

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
