# Correction et relance du projet (WSL — ModuleNotFoundError environ)

**Date** : 2025-01-30  
**Statut** : 🟢 Terminé  
**Pilotes** : Orchestrateur (architecte), DevOps, Dev Django (techos)

**Note pour l’équipe** : Préférence utilisateur — **WSL par défaut** (environnement de dev et commandes terminal). Privilégier WSL dans les procédures, la doc et les commandes proposées.

---

## Contexte

En WSL, le lancement du projet sans Docker échouait avec **ModuleNotFoundError: No module named 'environ'** (dépendances non installées). L’utilisateur a demandé que l’**architecte**, le **DevOps** et les **techos** interviennent pour corriger et relancer le projet.

---

## Rôles et actions réalisées

| Rôle | Responsable | Actions |
|------|-------------|---------|
| **Orchestrateur (architecte)** | Cohérence Make ↔ doc, registre | Alignement stratégie Make (venv-install, runserver) ; mise à jour strategie-operationnelle-make.md § 3.7 ; cohérence environnement-wsl-linux ↔ pret-a-demarrer. |
| **DevOps** | Infra, Make, env WSL | Ajout cible Make **venv-install** (création .venv + pip install -r requirements.txt) ; **runserver** utilise .venv/bin/python si présent, sinon python3 ; mise à jour environnement-wsl-linux.md (Option B, § 6 ModuleNotFoundError) ; doc pret-a-demarrer.md § 5.1 déjà en place. |
| **Dev Django (techos)** | Déps, check, runserver | Vérification requirements.txt (django-environ présent) ; runserver Make compatible WSL (détection .venv, python3). |

---

## Livrables

- **Makefile** : cibles `venv-install`, `runserver` (détection .venv / python3), `make help` mis à jour.
- **Docs** : `environnement-wsl-linux.md` (Option B avec venv-install, § 6 ModuleNotFoundError) ; `strategie-operationnelle-make.md` § 3.7 (Dev local WSL) ; `pret-a-demarrer.md` § 5.1 (déjà présent).
- **Décision** : `decisions.md` — workflow WSL dev (venv-install, runserver).
- **Log** : `log-ia.md` — intervention architecte / DevOps / techos pour correction et relance.

---

## Procédure de relance (WSL)

À la racine du projet (où se trouvent `manage.py` et `requirements.txt`) :

```bash
make venv-install   # Crée .venv + installe toutes les deps (dont django-environ)
make runserver      # Lance Django (utilise .venv automatiquement)
```

Avec Docker (db + redis seuls, Django en local) :

```bash
make dev
make venv-install
make runserver
```

---

## Références

- **Prêt à démarrer** : `docs/base-de-connaissances/pret-a-demarrer.md` § 5.1
- **Environnement WSL** : `docs/base-de-connaissances/environnement-wsl-linux.md`
- **Stratégie Make** : `docs/base-de-connaissances/strategie-operationnelle-make.md` § 3.7
- **Règle DevOps** : `.cursor/rules/devops.mdc`
- **Registre** : `docs/base-de-connaissances/registre-agents-ressources.md`
