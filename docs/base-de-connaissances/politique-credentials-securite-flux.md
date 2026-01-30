# Politique credentials et sécurité des flux

**Rôle** : Garantir que les **credentials** (admin Django, Flowise, n8n, DB, etc.) ne sont **jamais divulgués ni committés**, et que les **flux** (appli, robots, workflows Flowise/n8n) sont **sécurisés et isolés** pour éviter injections et fuites de données.

**Pilotes** : **DevOps**, **architecte réseau** (infra, isolation), **agent dédié sécurité (Pentester)** — en charge d’appliquer les règles, d’isoler les flux des robots et d’empêcher que les workflows ne créent des fuites de données.

---

## 1. Credentials : jamais divulgués ni committés

- **Règle** : Les identifiants (compte admin Django, mots de passe Flowise/n8n, DB, tokens, clés API) ne doivent **jamais** être écrits dans le code, dans les issues, dans les messages de commit ni dans un fichier versionné.
- **Stockage** : uniquement dans `.env` (non versionné, déjà dans `.gitignore`), ou dans les secrets de la plateforme (GitHub Secrets, Vercel, variables d’environnement prod). **Jamais** dans un fichier committé.
- **Création du superutilisateur** : exécuter `docker compose exec web python manage.py createsuperuser` (ou `make createsuperuser`) en local et saisir les identifiants **à la main** ; ne pas les mettre dans un script ni dans la doc.
- **DevOps** : s’assurer que `.env` et tout fichier contenant des secrets restent ignorés ; ne jamais pousser de credentials dans le dépôt. Voir `infra-devops.md`, `regles-securite.md`.
- **Architecte réseau / DevOps** : sécuriser l’accès aux services (DB, Redis, Flowise, n8n) par réseau et credentials (variables d’env, pas de valeurs par défaut faibles en prod).

---

## 2. Agent dédié sécurité : Pentester (Paintteur)

L’**agent Pentester** (règle `.cursor/rules/pentester.mdc`) est l’**agent dédié à la sécurité**. Il est en charge de :

- **Appliquer toutes les règles** de sécurité du projet (injection, XSS, CSRF, validation des entrées, rate limiting) — voir `regles-securite.md`.
- **Isoler les flux des robots** : s’assurer que les flux d’enrichissement (OSINT, Celery, API enrich) et les appels depuis Flowise/n8n sont isolés (rate limiting, validation, pas de propagation de données sensibles vers l’extérieur sans contrôle).
- **Empêcher que les workflows (Flowise, n8n) ne créent des fuites de données** : guide-rails sur les API (validation, limites batch, pas d’exécution de code arbitraire), contrôle des entrées/sorties des webhooks, pas de log de credentials ni de données personnelles. Voir `enrichissement-osint-flowise-n8n.md` (guide-rails).
- **Sécuriser les flots** pour l’appli (Django) et pour les robots/workflows Flowise et n8n : authentification des API (secret partagé, token, ou contrôle d’accès), protection contre les injections, isolation des données.

Référence : `docs/base-de-connaissances/regles-securite.md`, `docs/base-de-connaissances/enrichissement-osint-flowise-n8n.md`, `.cursor/rules/pentester.mdc`.

---

## 3. DevOps et architecte réseau

- **DevOps** : infrastructure, secrets (`.env`, GitHub Secrets, Vercel), pas de commit de credentials ; coordination avec l’agent sécurité (Pentester) pour les règles applicatives et les flux.
- **Architecte réseau** (ou rôle assumé par DevOps) : isolation réseau des services (DB, Redis, web, Flowise, n8n), exposition des ports maîtrisée, pas d’exposition d’endpoints sensibles sans contrôle d’accès.

---

## 4. Références

- **Règles de sécurité** : `docs/base-de-connaissances/regles-securite.md`
- **Infra et secrets** : `docs/base-de-connaissances/infra-devops.md`
- **Guide-rails Flowise / n8n** : `docs/base-de-connaissances/enrichissement-osint-flowise-n8n.md`
- **Règle Pentester** : `.cursor/rules/pentester.mdc`
- **.gitignore** : à la racine (`.env`, `secrets/`, `credentials/`, etc.)

---

*Document créé par le Conseiller. Les credentials ne sont jamais stockés dans ce document ni ailleurs dans le dépôt. Dernière mise à jour : 2025-01-30.*
