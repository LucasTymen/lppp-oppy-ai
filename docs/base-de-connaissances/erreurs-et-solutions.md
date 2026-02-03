# Registre erreurs et solutions LPPP

**Objectif** : Répertorier les erreurs rencontrées et les solutions trouvées pour éviter de les reproduire et guider les agents qui rencontrent des soucis.

**Maintenu par** : Agent qui assiste le Chef de Projet (mise à jour au fur et à mesure des corrections).  
**Consulté par** : Tous les agents — en cas de blocage ou d’erreur, consulter ce registre avant de réinventer ; après une correction, ajouter une entrée.  
**Référence** : `agents-roles-responsabilites.md` (§ Chef de Projet, RACI « Documenter erreurs et solutions »), `pilotage-agents.mdc` (Data-driven et logs).

---

## Comment utiliser ce registre

### Pour un agent qui rencontre une erreur
1. **Consulter ce fichier** : chercher une entrée similaire (contexte, message d’erreur, stack).
2. Si une entrée existe : appliquer la solution et les précautions indiquées.
3. Si aucune entrée : après résolution, **ajouter une entrée** (voir format ci‑dessous) et mettre à jour les logs (`log-projet.md` ou `log-ia.md`).

### Pour l’agent qui assiste le Chef de Projet
- **À chaque correction d’erreur** : ajouter ou compléter une entrée dans ce registre et mettre à jour les logs pour que l’équipe ne reproduise pas l’erreur.
- **Interaction** : le Chef de Projet valide que la doc est à jour ; l’Orchestrateur peut référencer ce doc dans le registre agents/ressources.

---

## Format d’une entrée

Pour chaque erreur documentée, indiquer :

| Champ | Description |
|-------|-------------|
| **Date** | Date de la correction ou de la première occurrence documentée |
| **Contexte** | Où / quand ça se produit (WSL, Docker, commande, page, etc.) |
| **Erreur** | Message d’erreur ou symptôme (copier-coller si pertinent) |
| **Cause** | Cause identifiée (optionnel mais utile) |
| **Solution** | Étapes ou correctif appliqué |
| **Prévention** | Comment éviter que ça se reproduise (doc, procédure, checklist) |
| **Lien(s)** | Vers une doc ou procédure dédiée (ex. `environnement-wsl-linux.md`) |

---

## Entrées

*(Les entrées seront ajoutées au fur et à mesure des corrections.)*

### Exemple (template) — ModuleNotFoundError: No module named 'environ'

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | WSL, lancement `make runserver` ou `python manage.py runserver` |
| **Erreur** | `ModuleNotFoundError: No module named 'environ'` |
| **Cause** | Environnement virtuel absent ou dépendances non installées (django-environ dans requirements.txt) |
| **Solution** | `make venv-install` puis `make runserver` |
| **Prévention** | Utiliser `make venv-install` après clône ou changement de branche ; doc `environnement-wsl-linux.md` § 6, Option B |
| **Lien(s)** | `environnement-wsl-linux.md`, `strategie-operationnelle-make.md` § 3.7, `2025-01-30-correction-relance-wsl.md` |

---

### Flowise — incompatibilités de types entre nœuds / difficulté à raccorder

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Flowise, canvas Chatflow ou flow d'ingestion ; tentative de relier des nœuds entre eux |
| **Erreur** | Connexion refusée entre nœuds, message d'incompatibilité de type, ou flow qui ne s'exécute pas après câblage |
| **Cause** | Flowise impose des types de flux (Document, ChatMessage, etc.) : une sortie ne peut aller que vers une entrée du même type. Câbler « Document » vers « ChatMessage » (ou l'inverse) provoque des erreurs. |
| **Solution** | Pour le RAG Concierge Maisons-Alfort : **ne pas câbler** les nœuds. Utiliser la section **Document Stores** pour l'ingestion (Loader → Splitter → Embedding → Vector Store, sans fils). Sur le **Chatflow**, mettre un seul nœud **Agent** et configurer **Knowledge** via la liste déroulante (sélection du Document Store), pas par un câble. |
| **Prévention** | Suivre la recette `docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md` § « Pourquoi les nœuds ne se raccordent pas ». Règle : Document → Document uniquement ; ChatMessage/string → même type. Vérifier les libellés des prises avant de connecter. |
| **Lien(s)** | `docs/flowise-workflows/workflow-complet-concierge-maisons-alfort.md`, `flowise-concierge-ia-maisons-alfort-guide.md` |

---

### Flowise — 401 Invalid model key or Incorrect local model configuration

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Flowise, chargement d'une page ou exécution d'un chatflow / ingestion |
| **Erreur** | Status 500 — « 401 Invalid model key or Incorrect local model configuration » |
| **Cause** | Problème de configuration du **LLM** ou de l'**embedding** : clé API OpenAI (ou autre) invalide, expirée ou mal renseignée ; ou modèle local (Ollama, etc.) mal configuré (URL, nom du modèle). |
| **Solution** | Vérifier dans Flowise : (1) Credentials / clé API du nœud OpenAI (Chat ou Embeddings) — clé valide et avec les bons droits ; (2) Nom du modèle exact (ex. `gpt-4o-mini`, `text-embedding-3-small`) ; (3) Si modèle local : URL de base (ex. `http://host.docker.internal:11434`) et nom du modèle. Corriger la config puis recharger la page. |
| **Prévention** | Documenter les modèles utilisés dans `data/flowise/comptes-et-llm.md` ; ne pas committer les clés (`.env` / UI Flowise uniquement). |
| **Lien(s)** | `data/flowise/comptes-et-llm.md`, `flowise-faiss-base-path-infra.md` § 5 |

---

### Vercel 404 / DEPLOYMENT_NOT_FOUND — page ne s’affiche pas

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Déploiement Vercel après push sur GitHub ; ouverture de l’URL du projet (ex. `https://<projet>.vercel.app/` ou `/p4s-archi`) |
| **Erreur** | 404, « 404: NOT_FOUND », « DEPLOYMENT_NOT_FOUND » ou page blanche |
| **Cause** | **Root Directory** Vercel incorrect : Vercel build depuis la racine du dépôt au lieu du dossier qui contient l’app Next.js (ex. `frontend/` en monorepo, ou `./` pour un repo standalone où l’app est à la racine). |
| **Solution** | 1) Vercel Dashboard → projet → **Settings** → **General** → **Root Directory** : **Edit** → saisir `frontend` (monorepo) ou `./` / laisser vide (repo standalone à la racine) → **Save**. 2) **Redeploy** : Deployments → **…** sur le dernier déploiement → **Redeploy** (ou pousser un commit). 3) Attendre build **Ready**, réessayer l’URL. |
| **Prévention** | À la création du projet Vercel, configurer tout de suite le **Root Directory** selon le type de repo (standalone = `./`, monorepo = `frontend`). Voir `strategie-deploiement-git-vercel.md` et `deploiement-vercel-frontend.md`. |
| **Lien(s)** | `deploiement-vercel-frontend.md` § 6, `strategie-deploiement-git-vercel.md` (Pièges à éviter) |

---

### Vercel — No Output Directory named "public" after Build

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Déploiement Vercel d’une app Next.js (ex. standalone P4S, frontend) ; build réussit (Route (app), First Load JS) puis échec au final. |
| **Erreur** | `Error: No Output Directory named "public" found after the Build completed. Configure the Output Directory in your Project Settings. Alternatively, configure vercel.json#outputDirectory.` ([Learn More](https://vercel.link/missing-public-directory)) |
| **Cause** | Vercel cherche un répertoire de sortie nommé **public**, alors que Next.js produit **`.next`** (et non `public` — `public` est le dossier d’entrée des assets statiques). Souvent dû à un réglage **Output Directory: public** dans les paramètres du projet Vercel ou à un framework mal détecté. |
| **Solution** | 1) **Dans le repo** : dans le `vercel.json` à la racine de l’app Next.js déployée (ex. `deploy/standalone-p4s/vercel.json` pour P4S), ajouter `"outputDirectory": ".next"` et conserver `"framework": "nextjs"`. 2) **Dans Vercel** : Project → **Settings** → **General** → **Build & Development Settings** → **Output Directory** : laisser **vide** (ou `.next`) et **Framework Preset** = **Next.js** → **Save**. 3) **Redeploy** (push ou Redeploy depuis les Deployments). |
| **Prévention** | Pour tout nouveau projet Vercel lié à une app Next.js : ne pas définir Output Directory sur `public` ; laisser le framework Next.js gérer la sortie, ou fixer `outputDirectory` dans `vercel.json` à `.next`. |
| **Lien(s)** | `deploy/standalone-p4s/vercel.json`, `strategie-deploiement-git-vercel.md`, [Vercel missing public directory](https://vercel.link/missing-public-directory) |

---

### localhost:8000 inaccessible — ERR_CONNECTION_RESET / connexion réinitialisée

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | Windows, accès à http://localhost:8000/p/p4s-archi/ (ou /admin/, /essais/) après avoir lancé Docker ou runserver |
| **Erreur** | « Ce site est inaccessible », « La connexion a été réinitialisée », **ERR_CONNECTION_RESET** |
| **Cause** | Sous Windows, le port forward Docker vers le conteneur `web` (8000) peut provoquer une connexion réinitialisée ; ou le serveur Django n’est pas démarré. |
| **Solution** | Utiliser l’**Option B (runserver local)** : 1) `docker compose up -d db redis` (garder uniquement db + redis). 2) Dans `.env` : `DB_HOST=localhost`, `REDIS_URL=redis://127.0.0.1:6379/0`, `CELERY_BROKER_URL=redis://127.0.0.1:6379/1`. 3) Venv activé : `pip install -r requirements.txt`, `python manage.py migrate --noinput`, `python manage.py runserver 127.0.0.1:8080`. 4) Ouvrir **http://127.0.0.1:8080/p/p4s-archi/** (landing complète Django). Si le conteneur `web` tourne, le libérer d’abord : `docker compose stop web`. |
| **Prévention** | Sous Windows : privilégier Option B pour le dev (runserver sur 8080). Sous WSL : Docker web sur 8000 fonctionne en général. |
| **Lien(s)** | `pret-a-demarrer.md` § 5.2, `demarrage-projet-equipe-tech.md` |

---

### GitLab désynchronisé — push oublié sur un remote

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Après `git push origin main` ; ou vérification des deux remotes (GitHub + GitLab) |
| **Erreur** | GitLab ne contient pas les derniers commits ; ou « on galère entre GitHub, GitLab et Vercel » (miroir incomplet). |
| **Cause** | Push effectué seulement sur `origin` (GitHub), pas sur `gitlab`. Vercel peut être lié à GitHub ; GitLab sert de backup/miroir — s’il n’est pas poussé, le miroir est faux. |
| **Solution** | Après chaque push sur `origin` : `git push gitlab main`. Si le remote `gitlab` n’existe pas : `git remote add gitlab git@gitlab.com:LucasTymen/<repo>.git` puis `git push -u gitlab main`. Utiliser `make push-both` (LPPP) si configuré, ou exécuter les deux pushes à la suite. |
| **Prévention** | Toujours pousser sur **les deux** remotes (origin + gitlab) après un commit. Checklist : `strategie-deploiement-git-vercel.md` (étape 3 : push origin puis push gitlab). Scripts type `push-standalone-p4s.sh` font les deux ; en manuel, ne pas oublier le second push. |
| **Lien(s)** | `git-remotes-github-gitlab.md`, `strategie-deploiement-git-vercel.md`, `pilotage-agents.mdc` (Git — commit + push sur les deux remotes) |

---

### Repo GitHub/GitLab créé avec README — conflit au premier push

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Premier push vers un repo fraîchement créé (GitHub ou GitLab) |
| **Erreur** | `! [rejected] main -> main (non-fast-forward)` ou refus de push car les historiques divergent (repo distant a un commit README, local a un autre premier commit). |
| **Cause** | Le repo a été créé avec « Initialize with README » (ou .gitignore / license), donc il a déjà un commit ; le dépôt local a un autre premier commit → deux historiques différents. |
| **Solution** | Option A : recréer le repo **sans** README, sans .gitignore, sans license, puis refaire `git push -u origin main` (et idem pour GitLab). Option B (si on ne peut pas recréer) : `git pull origin main --allow-unrelated-histories`, résoudre les conflits si besoin, puis `git push origin main`. Préférer Option A pour garder un historique propre. |
| **Prévention** | Toujours créer les repos **Create blank repository** / **Create blank project** **sans** cocher « Add README », « Add .gitignore », « Add license ». Voir `strategie-deploiement-git-vercel.md` (étape 1) et `git-remotes-github-gitlab.md`. |
| **Lien(s)** | `git-remotes-github-gitlab.md` § 6, `strategie-deploiement-git-vercel.md` (Pièges à éviter) |

---

### Vercel — Build Failed : Vulnerable version of Next.js (CVE-2025-66478)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-02 |
| **Contexte** | Déploiement Vercel (LPPP_Ackuracy, LPPP_P4S-Architecture) ; build échoue avec message « Vulnerable version of Next.js detected, please update immediately ». |
| **Erreur** | Build Failed ; CVE-2025-66478 (React2Shell) — Next.js 15.0.0 à 16.0.6 affectés. |
| **Cause** | `next@15.1.3` (et versions similaires) dans `package.json` est vulnérable. |
| **Solution** | Mettre à jour Next.js vers une **version corrigée** : pour la branche 15.1.x utiliser **15.1.9** (`"next": "15.1.9"` dans package.json). Mettre à jour dans : `deploy/standalone-ackuracy/package.json`, `deploy/standalone-p4s/package.json`, `frontend/package.json`. Puis **commit + push** sur les repos concernés (ACKURACY, P4S) pour déclencher un nouveau build Vercel. |
| **Prévention** | Vérifier régulièrement [Next.js Security](https://nextjs.org/blog/CVE-2025-66478) et les alertes Vercel ; figer une version patchée (ex. 15.1.9) dans les package.json. |
| **Lien(s)** | [Next.js CVE-2025-66478](https://nextjs.org/blog/CVE-2025-66478), [Vercel CVE-2025-55182](https://vercel.com/changelog/cve-2025-55182) |

---

### Scripts bash push standalone — erreur CRLF ($'\r': command not found)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-02-03 |
| **Contexte** | WSL ou Git Bash, exécution de `bash deploy/push-standalone-p4s.sh` ou `bash deploy/push-standalone-ackuracy.sh` |
| **Erreur** | `$'\r': command not found`, `set: -: invalid option`, `cd: $'deploy/..\r': No such file or directory`, `fatal: remote error: is not a valid repository name`, `fatal: invalid refspec 'main?'`, `syntax error: unexpected end of file` |
| **Cause** | Fins de ligne **CRLF** (Windows) dans les fichiers `.sh` ; bash interprète le `\r` comme caractère, ce qui casse les commandes et les variables (REPO_DIR, refspec `main`). |
| **Solution** | 1) Convertir les scripts en **LF uniquement** : sous PowerShell `[System.IO.File]::ReadAllText("deploy\push-standalone-p4s.sh") -replace "`r`n", "`n" -replace "`r", "`n"` puis `WriteAllText` ; ou sous WSL `sed -i 's/\r$//' deploy/push-standalone-p4s.sh deploy/push-standalone-ackuracy.sh`. 2) `.gitattributes` avec `deploy/*.sh text eol=lf` pour que Git conserve le LF à l’avenir. |
| **Prévention** | Ne pas éditer les `.sh` avec un éditeur qui force le CRLF ; laisser `.gitattributes` gérer `eol=lf` pour `deploy/*.sh`. Après correction, les scripts s’exécutent correctement (push P4S et ACKURACY vers GitHub + GitLab, Vercel rebuild). |
| **Lien(s)** | `deploy/README-standalone.md`, `deploy/push-standalone-p4s.sh`, `deploy/push-standalone-ackuracy.sh` |

---

---

### Push GitHub/GitLab — authentification échouée (Windows / agent)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Déploiement P4S (ou autre standalone) : clone + copie + commit OK ; `git push origin main` échoue (PowerShell, Cursor, CI sans credentials). |
| **Erreur** | `Invalid username or token. Password authentication is not supported` (HTTPS) ou `Host key verification failed` (SSH). |
| **Cause** | GitHub n’accepte plus les mots de passe ; le terminal/agent n’a pas de PAT (Personal Access Token) ni de clé SSH configurée. |
| **Solution** | **Étape manuelle** : ouvrir un terminal où vous êtes déjà authentifié (Git Bash, GitHub Desktop, ou PowerShell après `gh auth login` / config SSH), puis `cd deploy/repo-p4s` (ou le repo concerné), `git push -u origin main`, puis `git push gitlab main`. Alternative : exécuter `.\deploy\push-standalone-p4s.ps1` (clone + commit), puis faire le push à la main depuis `deploy/repo-p4s`. |
| **Prévention** | Configurer un PAT (GitHub → Settings → Developer settings → Personal access tokens) pour HTTPS, ou SSH (clés + `ssh-add`), puis utiliser ce terminal pour le push final. |
| **Lien(s)** | `deploy/README-standalone.md`, `deploy/push-standalone-p4s.ps1` |

---

### CTA / Gmail sur landing statique — mailto: n’ouvre rien (Windows)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Landing P4S déployée en statique (Vercel) ; clic sur « Me contacter », CTA « Reprendre la conversation » ou lien Gmail. |
| **Erreur** | Rien ne se passe, ou message Windows « Ce fichier ne contient pas d’application associée » (pas de client mail par défaut pour `mailto:`). |
| **Cause** | Lien `mailto:` dépend du client mail configuré sur la machine du visiteur ; sous Windows sans client associé, le lien échoue. CTA et Gmail « en dur » ne déclenchaient aucune action. |
| **Solution** | **Popup (modal) contact** : tous les liens « Me contacter », CTA hero, CTA final et ligne Gmail ouvrent un **popup** (modal CSS `:target`) avec le texte : « Vous pouvez me contacter par Mail à cette adresse : [email] ». L’email est affiché en dur (sélectionnable/copiable). Fermeture par lien « Fermer » ou clic sur l’overlay. Aucun JavaScript ; compatible page statique. Template : `templates/landing_pages/proposition.html` (`.contact-modal`, `#contact-email-modal`). |
| **Prévention** | Sur les landings statiques (export Django → HTML), ne pas compter sur `mailto:` seul : proposer systématiquement le popup avec l’adresse en clair pour que le visiteur puisse copier. Tenir compte de cette contrainte dans tout nouveau template ou export. |
| **Lien(s)** | `deploy/PUSH-POUR-VERSION-COMPLETE.md`, `templates/landing_pages/proposition.html` |

---

### localhost:3000 — réservé à Flowise (pas aux landings Next.js)

| Champ | Contenu |
|-------|---------|
| **Date** | 2025-01-30 |
| **Contexte** | Indication d’ouvrir une landing Next.js (ex. Ackuracy) sur http://localhost:3000. |
| **Erreur** | Confusion : le port 3000 est celui de **Flowise**, pas des apps Next.js standalone. |
| **Cause** | Next.js utilise 3000 par défaut ; dans LPPP, 3000 est attribué à Flowise. |
| **Solution** | Landings Next.js en local : **port 3001**. Ex. `cd deploy/standalone-ackuracy && npm run dev` → http://localhost:3001. Le script `dev` est configuré avec `-p 3001` dans `package.json`. Référence ports : `infra-devops.md` § 3.4. |
| **Prévention** | Ne jamais indiquer localhost:3000 pour une landing ; consulter `infra-devops.md` § 3.4 Ports avant de documenter ou proposer une URL de dev. |
| **Lien(s)** | `docs/base-de-connaissances/infra-devops.md` (§ 3.4), `deploy/standalone-ackuracy/README.md` |

---

*Dernière mise à jour : 2025-01-30 — Port 3000 = Flowise, landings Next.js = 3001. Précédent : CTA/Gmail popup contact. Stratégie fluide : `strategie-deploiement-git-vercel.md`.*
