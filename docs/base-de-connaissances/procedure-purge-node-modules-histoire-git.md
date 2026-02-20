# Procédure — Purge de node_modules de l’historique Git

**Pilote** : DevOps.  
**Contexte** : node_modules a été committé ; GitLab refuse le push (blob > 100 MiB). Il faut retirer `node_modules/` de tout l’historique.  
**Référence** : `regle-jamais-committer-node-modules.md`, `segmentations/2026-01-30-sprint-nettoyage-reparation-git-node-modules.md`.

---

## Prérequis

- **Sauvegarde** : tout travail en cours committé ou sauvegardé. La réécriture d’historique modifie les commits et les hash.
- **Environnement** : WSL ou Git Bash (Python 3 pour git-filter-repo si utilisé).
- **Dépôt** : à la racine du projet LPPP (`landingPageCreatorForProspection`), pas dans deploy/LPPP-Casapy.

---

## Option A — git filter-repo (recommandé)

1. **Installer git-filter-repo** (si besoin) :
   ```bash
   pip3 install git-filter-repo
   ```
   Ou voir : https://github.com/newren/git-filter-repo

2. **Cloner en miroir** (pour ne pas casser le clone actuel) :
   ```bash
   cd /home/lucas/tools   # ou chemin parent
   git clone --mirror file:///home/lucas/tools/homelucastoolsLandingsPagesPourProspections LPPP-clean.git
   cd LPPP-clean.git
   ```

3. **Supprimer node_modules de tout l’historique** :
   ```bash
   git filter-repo --path node_modules --invert-paths --force
   ```

4. **Remplacer l’origin par le dépôt nettoyé** (depuis le clone de travail) :
   ```bash
   cd homelucastoolsLandingsPagesPourProspections
   git remote remove origin
   git remote add origin file:///home/lucas/tools/LPPP-clean.git
   git fetch origin
   git reset --hard origin/main
   git remote set-url origin https://github.com/LucasTymen/landingPageCreatorForProspection.git
   # ou git@github.com:...
   git push origin main --force
   git push gitlab main --force
   ```

5. **Nettoyer le miroir** si plus besoin : `rm -rf LPPP-clean.git`.

---

## Option B — BFG Repo-Cleaner

1. Télécharger BFG : https://rtyley.github.io/bfg-repo-cleaner/

2. **Cloner en miroir** :
   ```bash
   git clone --mirror file:///chemin/vers/LPPP LPPP-mirror.git
   cd LPPP-mirror.git
   ```

3. **Supprimer le dossier node_modules** :
   ```bash
   java -jar bfg.jar --delete-folders node_modules
   git reflog expire --expire=now --all && git gc --prune=now --aggressive
   ```

4. Puis pousser le miroir vers origin/gitlab (refs remplacés).

---

## Option C — Retirer du suivi sans réécrire l’historique

Si la réécriture d’historique est impossible ou non souhaitée :

```bash
git rm -r --cached node_modules
git add .gitignore
git commit -m "chore: retirer node_modules du suivi"
git push origin main
```

**Attention** : GitLab peut **continuer à refuser** le push si le blob 112 MiB est encore dans l’historique (ex. dans un commit précédent). Dans ce cas, seule l’Option A ou B débloque.

---

## Après la purge

- Tous les collaborateurs : `git fetch origin`, `git reset --hard origin/main` (ou rebase) car l’historique a changé.
- Vérifier : `git ls-tree -r HEAD | grep node_modules` → ne doit rien retourner.
- Mise à jour : `erreurs-et-solutions.md`, `log-projet.md`, `regle-jamais-committer-node-modules.md` (référence à cette procédure).

---

## LPPP-Casapy (repo standalone) — à part

Cette procédure concerne le **dépôt principal** LPPP. Pour **deploy/LPPP-Casapy** (repo `LPPP_casapy` sur GitHub) :

- Si rebase en cours : `git rebase --abort` dans `deploy/LPPP-Casapy`.
- Repartir propre : `git fetch origin`, `git reset --hard origin/main`.
- Régénérer l’export depuis LPPP : `python3 manage.py export_landing_static casapy ...` puis commit + push dans `deploy/LPPP-Casapy`.

Voir `deploy/PUSH-CASAPY.md` § « Push refusé : Updates were rejected ».

---

---

## Exécution (2026-01-30)

- Miroir créé : `c:\home\lucas\tools\LPPP-clean.git`
- `git filter-repo --path node_modules --invert-paths --force` exécuté avec succès.
- Repo principal : origin remplacé par miroir → fetch → reset --hard origin/main → origin/gitlab rétablis → **push origin main --force** (HTTPS) et **push gitlab main --force** (HTTPS) réussis.
- GitLab accepte à nouveau le push (blob 112 MiB supprimé de l’historique).

*Document créé : 2026-01-30. Pilote : DevOps. Coordination : Architecte, Ingénieur système, Pentester (sprint nettoyage).*
