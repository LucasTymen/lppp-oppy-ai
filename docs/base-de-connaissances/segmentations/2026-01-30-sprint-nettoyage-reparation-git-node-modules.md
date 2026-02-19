# Sprint — Nettoyage et réparation Git (node_modules, LPPP-Casapy)

**Date** : 2026-01-30  
**Statut** : En cours  
**Pilote** : DevOps (exécution) ; coordination : Architecte, Ingénieur système/réseau, Pentester.

**Contexte** : node_modules a été committé dans le dépôt principal LPPP ; GitLab refuse le push (blob 112 MiB > 100 MiB). Le repo LPPP-Casapy a des conflits de rebase. Objectif : nettoyer, réparer, documenter.

---

## 1. Diagnostic (fait)

| Problème | Détail |
|----------|--------|
| **GitLab push refusé** | Blob `57ee9a59...` (112 MiB) = `node_modules/@next/swc-linux-x64-gnu/next-swc.linux-x64-gnu.node` |
| **LPPP-Casapy** | Rebase en conflit (modify/delete, index.html, casapy-wave-progression.png, spec-deck) ; remote a eu un forced update |
| **Règle projet** | Ne jamais générer tous les nodes ; ne jamais committer node_modules. Voir `regle-jamais-generer-tous-les-nodes.md`, `regle-jamais-committer-node-modules.md`. |

---

## 2. Rôles et tâches

### DevOps (Responsible — exécution)

- [ ] **Purge historique LPPP principal** : retirer `node_modules/` de tout l’historique Git (git filter-repo ou BFG). Procédure : `procedure-purge-node-modules-histoire-git.md`.
- [ ] Vérifier `.gitignore` (node_modules, **/node_modules) avant et après purge.
- [ ] Après purge : `git push origin main --force`, `git push gitlab main --force` (coordination avec l’équipe : tous les clones devront refetch/rebase).
- [ ] **LPPP-Casapy** : soit abort rebase + reset --hard origin/main + régénérer l’export depuis LPPP ; soit documenter la résolution manuelle des conflits et push. Réf. `deploy/PUSH-CASAPY.md`.
- [ ] Mettre à jour `erreurs-et-solutions.md` et les logs après réparation.

### Architecte (Consulted — structure)

- [ ] Valider la **séparation des périmètres** : dépôt principal LPPP (Django, apps, docs) vs repo standalone LPPP-Casapy (uniquement export statique : index.html, PNG, rapport.html). Éviter que du code Django ou node_modules ne soit poussé dans LPPP_casapy.
- [ ] Points de défaillance identifiés : `git add -A` à la racine, npm install à la racine, mélange des remotes (origin pointant vers LPPP_casapy depuis la racine LPPP). Documenter dans la procédure ou la stratégie Git.

### Ingénieur système / Réseau (Consulted)

- [ ] **Chemins et environnement** : documenter le chemin WSL correct pour le projet (ex. `/home/lucas/tools/...` ou `/mnt/c/...`) pour les commandes `rm -rf node_modules`, `cd` dans les procédures.
- [ ] Après purge : vérifier que clone frais et push fonctionnent (réseau, SSH/HTTPS, pas de blocage firewall).

### Pentester (Consulted — sécurité)

- [ ] Vérifier qu’**aucun secret** ni artefact sensible n’est exposé dans l’historique Git (avant/après purge). Si des commits ont pu contenir des fichiers sensibles, signaler.
- [ ] Valider que la procédure de purge ne laisse pas de traces réutilisables (refs, reflog) en environnement partagé si pertinent.

### Chef de Projet (Accountable)

- [ ] Valider la checklist avant push prod après réparation.
- [ ] S’assurer que les logs (`log-projet.md`, `log-ia.md`) et le registre erreurs/solutions sont à jour.

---

## 3. Ordre d’exécution

1. **Sauvegarde** : s’assurer que les changements locaux importants sont committés ou sauvegardés ailleurs (le filter-repo réécrit l’historique).
2. **Purge** (DevOps) : exécuter la procédure `procedure-purge-node-modules-histoire-git.md` sur le dépôt principal.
3. **Push forcé** (DevOps) : origin puis gitlab ; prévenir l’équipe.
4. **LPPP-Casapy** (DevOps) : résoudre selon procédure (abort + reset ou résolution manuelle).
5. **Vérifications** (Ingénieur système, Pentester) : clone frais, push, absence de secrets.
6. **Documentation** (DevOps, Chef de Projet) : mise à jour erreurs-et-solutions, logs, procédures.

---

## 4. Références

- `docs/base-de-connaissances/regle-jamais-committer-node-modules.md`
- `docs/base-de-connaissances/regle-jamais-generer-tous-les-nodes.md`
- `docs/base-de-connaissances/erreurs-et-solutions.md` (node_modules committé, OOM Cursor)
- `docs/base-de-connaissances/procedure-purge-node-modules-histoire-git.md` (à créer / ci-dessous)
- `deploy/PUSH-CASAPY.md`
- `git-remotes-github-gitlab.md`

---

*Segmentation créée pour coordination Architecte, Ingénieur système/réseau, DevOps, Pentester. Dernière mise à jour : 2026-01-30.*
