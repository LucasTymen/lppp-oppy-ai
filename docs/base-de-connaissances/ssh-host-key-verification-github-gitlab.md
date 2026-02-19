# SSH — Host key verification failed (GitHub / GitLab)

**Pilote** : DevOps (règle `devops.mdc`).  
**Contexte** : Push/pull vers GitHub ou GitLab échoue avec `Host key verification failed`.  
**Référence** : `git-remotes-github-gitlab.md`, `infra-devops.md`, `erreurs-et-solutions.md`.

---

## 1. Diagnostic

### Erreur typique

```
Host key verification failed.
fatal: Could not read from remote repository.
```

### Cause

SSH ne reconnaît pas les clés d’hôte de GitHub ou GitLab. Cela arrive notamment quand :

1. **`known_hosts` vide ou incomplet** — première connexion ou fichier réinitialisé
2. **Environnement différent** — Cursor/PowerShell vs WSL/Git Bash utilisent des `~/.ssh` différents
3. **Clé chargée mais host non vérifié** — la clé privée est correcte mais le serveur n’est pas dans `known_hosts`

### Stratégie LPPP : réutiliser la clé existante

Le projet utilise **les mêmes clés SSH que SquidResearch** (`~/.ssh`).  
Si une clé fonctionne déjà ailleurs (SquidResearch, autre projet), il suffit de :

- ajouter GitHub et GitLab à `known_hosts`
- charger la clé dans l’agent SSH (`ssh-add`) si besoin

---

## 2. Solution rapide — Ajouter les host keys

### A) Depuis Git Bash ou WSL (recommandé)

Chemins `~/.ssh` :

- **Git Bash (Windows)** : `C:\Users\<ton_user>\.ssh`
- **WSL** : `/home/<ton_user>/.ssh`

```bash
# Créer le dossier .ssh si besoin
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Ajouter GitHub et GitLab à known_hosts (Ed25519 + RSA)
ssh-keyscan -t ed25519 -t rsa github.com >> ~/.ssh/known_hosts
ssh-keyscan -t ed25519 -t rsa gitlab.com >> ~/.ssh/known_hosts

# Tester
ssh -T git@github.com
ssh -T git@gitlab.com
```

### B) Depuis PowerShell (si Git for Windows installé)

Git for Windows fournit `ssh-keyscan` via `C:\Program Files\Git\usr\bin\` :

```powershell
$sshDir = "$env:USERPROFILE\.ssh"
if (-not (Test-Path $sshDir)) { New-Item -ItemType Directory -Path $sshDir }

& "C:\Program Files\Git\usr\bin\ssh-keyscan.exe" -t ed25519 -t rsa github.com | Add-Content -Path "$sshDir\known_hosts"
& "C:\Program Files\Git\usr\bin\ssh-keyscan.exe" -t ed25519 -t rsa gitlab.com | Add-Content -Path "$sshDir\known_hosts"

# Test
& "C:\Program Files\Git\bin\ssh.exe" -T git@github.com
& "C:\Program Files\Git\bin\ssh.exe" -T git@gitlab.com
```

---

## 3. Charger la clé dans l’agent SSH

Si la clé existe mais n’est pas chargée :

```bash
# Démarrer l’agent (si besoin)
eval $(ssh-agent -s)

# Charger la clé (ex. id_ed25519 ou celle utilisée pour SquidResearch)
ssh-add ~/.ssh/id_ed25519
# ou
ssh-add ~/.ssh/id_rsa
```

Sur Windows (PowerShell) :

```powershell
& "C:\Program Files\Git\usr\bin\ssh-agent.exe"
& "C:\Program Files\Git\usr\bin\ssh-add.exe" "$env:USERPROFILE\.ssh\id_ed25519"
```

---

## 4. Vérifier les fingerprints (optionnel)

Avant d’ajouter à `known_hosts`, on peut contrôler les fingerprints officiels :

**GitHub (2024)** : [github.com/.../githubs-ssh-key-fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)

- Ed25519 : `SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU`
- RSA : `SHA256:uNiVztksCsDhcc0u9e8BujQXVUpKZIDTMczCvj3tD2s`

```bash
ssh-keyscan -t ed25519 github.com 2>/dev/null | ssh-keygen -lf -
```

Si le fingerprint affiché correspond à celui ci-dessus, ajouter est sûr.

---

## 5. Si le problème persiste

### Environnement utilisé par Cursor

Le terminal Cursor peut utiliser :

- PowerShell → Git for Windows → `C:\Users\<user>\.ssh`
- WSL → `/home/<user>/.ssh`

S’assurer que les commandes ci-dessus sont exécutées dans **le même environnement** que celui utilisé pour `git push`.

### Fallback HTTPS

Si SSH reste bloquant, basculer temporairement sur HTTPS avec un PAT (Personal Access Token) :

```bash
git remote set-url origin https://github.com/LucasTymen/landingPageCreatorForProspection.git
git remote set-url gitlab https://gitlab.com/LucasTymen/landingpagecreatorforprospection.git
git push origin main
# Mot de passe = PAT GitHub (pas le mot de passe du compte)
# Idem pour GitLab avec un token ou mot de passe de déploiement
```

Puis reconfigurer SSH quand la config est corrigée.

---

## 6. Checklist DevOps

| Étape | Commande / action |
|-------|-------------------|
| 1. `known_hosts` à jour | `ssh-keyscan -t ed25519 -t rsa github.com gitlab.com >> ~/.ssh/known_hosts` |
| 2. Clé chargée | `ssh-add ~/.ssh/id_ed25519` (ou ta clé) |
| 3. Test GitHub | `ssh -T git@github.com` |
| 4. Test GitLab | `ssh -T git@gitlab.com` |
| 5. Push | `git push origin main` puis `git push gitlab main` |

---

*Document créé : 2026-01-30. Référence : erreurs-et-solutions.md (Push — Host key verification), git-remotes-github-gitlab.md.*
