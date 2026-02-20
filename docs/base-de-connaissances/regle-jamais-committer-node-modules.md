# Règle : Ne jamais committer node_modules

**Pilote** : DevOps (règle `devops.mdc`).  
**Applicable à** : Toutes les équipes (Dev Django, Designer, DevOps, Chef de Projet, Automatizer, Infographiste, etc.).  
**Référence** : `.gitignore`, `infra-devops.md`, `erreurs-et-solutions.md`.

---

## Règle impérative

> **node_modules ne doit JAMAIS être committé, poussé ou inclus dans un dépôt Git.**

- `node_modules` est généré par `npm install` / `pnpm install` / `yarn`.
- Contenu : milliers de fichiers, centaines de Mo (souvent > 100 Mo) → dépasse les limites GitLab/GitHub.
- Risque : push refusé (ex. GitLab 100 Mo), historique lourd, conflits, temps de clone inutiles.

---

## Ce que chaque équipe doit faire

| Rôle | Action |
|------|--------|
| **DevOps** | Vérifier que `node_modules/` et `**/node_modules/` sont dans `.gitignore`. Avant chaque push : `git status` → ne doit pas afficher `node_modules`. |
| **Dev Django / Designer** | Ne jamais faire `git add .` sans filtrer ; privilégier `git add <fichiers explicites>` ou `git add -u`. |
| **Chef de Projet** | Rappeler la règle dans les briefs et checklists. |
| **Tous** | En cas de doute : `git check-ignore -v node_modules` → doit afficher une règle .gitignore. |

---

## Si node_modules a été committé par erreur

1. **Retirer du suivi** (sans supprimer le dossier local) :
   ```bash
   git rm -r --cached node_modules
   git rm -r --cached '**/node_modules'   # si sous-dossiers
   git commit -m "chore: retirer node_modules du suivi Git"
   ```

2. **Si déjà poussé** : l’historique contient les fichiers. Pour GitLab (limite 100 Mo) :
   - **Procédure détaillée** : `procedure-purge-node-modules-histoire-git.md` (git filter-repo ou BFG).
   - Option A : utiliser `git filter-repo` ou BFG pour réécrire l’historique et supprimer node_modules.
   - Option B : créer un nouveau commit sans node_modules et pousser ; les anciens blobs restent dans l’historique (GitLab peut continuer à refuser).

3. **Consulter** : `erreurs-et-solutions.md` (entrée « node_modules committé »). **Sprint équipe** : `segmentations/2026-01-30-sprint-nettoyage-reparation-git-node-modules.md` (DevOps, Architecte, Ingénieur système, Pentester).

---

## Prévention

- `.gitignore` racine : `node_modules/` et `**/node_modules/`.
- Chaque repo standalone (deploy/standalone-*, deploy/LPPP-Casapy) doit avoir son propre `.gitignore` avec `node_modules`.
- CI/CD : ne pas lancer `npm install` dans un contexte qui commit ensuite.

---

*Document créé : 2026-01-30. Règle projet : toutes les équipes.*
