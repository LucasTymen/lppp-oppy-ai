# Règles de sécurité LPPP

Règles de sécurité évidentes à respecter dans le projet. Aligné avec les règles du projet (anti-hallucination, data-driven). Référence : [Django security](https://docs.djangoproject.com/en/stable/topics/security/), bonnes pratiques OWASP.

**Règle unique pour tous les agents en charge** : en fin de session, livraison ou déploiement, **toujours** repasser en debug mode off (`DEBUG=False`) et s’assurer des mesures de protection (checklist § 9). Cette règle s’applique à tous les agents (Dev Django, DevOps, Chef de Projet, Orchestrateur, etc.). Voir aussi `.cursor/rules/pilotage-agents.mdc` § Sécurité.

---

## 1. Secrets et credentials

- **Ne jamais** committer de secrets, mots de passe, clés privées, tokens ou clés API dans le dépôt (code, issues, messages de commit).
- **.gitignore** : `.env`, `.env.*` (sauf `.env.example`), `*.pem`, `*.key`, `secrets/`, `credentials/`, etc. Voir `.gitignore` à la racine et `infra-devops.md` (§ Conventions).
- **Variables d’environnement** : utiliser `.env` (non versionné) en local ; en prod et CI : variables d’environnement ou Secrets du dépôt (GitHub Secrets, Vercel, etc.).
- **SECRET_KEY Django** : en production, utiliser une clé longue et aléatoire (ex. `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`), jamais la valeur par défaut du code.

---

## 2. Django : configuration production

- **DEBUG** : doit être `False` en production. Ne jamais laisser `DEBUG=True` en prod (fuite d’informations, stack traces).
- **ALLOWED_HOSTS** : en production, lister explicitement les domaines autorisés (pas de `*`). Ex. `ALLOWED_HOSTS=app.example.com,api.example.com`.
- **HTTPS** : en production, servir le site en HTTPS. Lorsque `DEBUG=False`, le projet applique déjà dans `lppp/settings.py` : `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF`, `X_FRAME_OPTIONS`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `SECURE_SSL_REDIRECT` (désactivable via `SECURE_SSL_REDIRECT=False` si le proxy gère HTTPS), `SECURE_PROXY_SSL_HEADER`, `SESSION_COOKIE_HTTPONLY`, `SESSION_COOKIE_SAMESITE`. Voir [Django security settings](https://docs.djangoproject.com/en/stable/ref/settings/#security).
- **Base de données** : mots de passe forts ; pas de compte par défaut en prod. Préférer des credentials dédiés par environnement.

---

## 3. Protection des requêtes (CSRF, XSS, injection)

- **CSRF** : ne pas désactiver le middleware CSRF (`django.middleware.csrf.CsrfViewMiddleware`). Pour les API consommées par des clients non-navigateur (N8N, Flowise), utiliser des tokens CSRF ou des mécanismes dédiés (ex. header secret, JWT) et documenter.
- **XSS** : utiliser les templates Django (échappement automatique) ; ne pas marquer de contenu comme `safe` sans validation stricte. Éviter `mark_safe` sur des entrées utilisateur.
- **Injection SQL** : utiliser l’ORM Django ou les requêtes paramétrées ; ne jamais concaténer des entrées utilisateur dans du SQL brut.
- **Validation des entrées** : valider et normaliser toutes les entrées (formulaires, API, query params). Limiter longueurs et formats (guide-rails dans `apps.scraping.enriched.osint_sources`).

---

## 4. Authentification et mots de passe

- **Mots de passe** : Django utilise par défaut PBKDF2 ; ne pas désactiver les `AUTH_PASSWORD_VALIDATORS` en prod. Exiger des mots de passe robustes (longueur, complexité).
- **Sessions** : en prod, `SESSION_COOKIE_SECURE=True`, `SESSION_COOKIE_HTTPONLY=True`, `SESSION_COOKIE_SAMESITE` approprié. Éviter de stocker des données sensibles en session sans besoin.

---

## 5. API et rate limiting

- **API publiques ou webhooks** : limiter les appels (rate limiting) pour éviter abus et scraping. Utiliser `apps.scraping.enriched.security` (EnrichmentRateLimiter) sur les endpoints d’enrichissement.
- **Authentification API** : pour les API internes (N8N, Flowise), utiliser un secret partagé (header, token) ou une authentification par IP / VPN ; ne pas exposer d’endpoints sensibles sans contrôle d’accès.

---

## 6. Fichiers et uploads

- **Upload** : valider types MIME et extensions ; stocker les fichiers hors de la racine web si possible ; limiter la taille. Ne pas exécuter de fichiers uploadés.
- **Static / media** : en prod, servir les fichiers statiques et media via le serveur web ou un CDN, pas via Django en mode DEBUG.

---

## 7. Logs et erreurs

- **Logs** : ne pas logger de mots de passe, tokens ou données personnelles. Les fichiers de log sont dans `.gitignore` ; ne pas les committer.
- **Erreurs en prod** : ne pas afficher de stack traces aux utilisateurs ; utiliser des pages d’erreur génériques et remonter les erreurs vers un système de monitoring (logs serveur, Sentry, etc.).

---

## 8. Dépendances et mise à jour

- **Dépendances** : maintenir `requirements.txt` à jour ; vérifier les CVE sur les paquets utilisés (Django, Celery, etc.) et mettre à jour les versions mineures/patch.
- **Images Docker** : utiliser des images officielles et des tags versionnés ; mettre à jour régulièrement.

---

## 9. Checklist avant mise en production

- [ ] `DEBUG=False`
- [ ] `SECRET_KEY` forte et unique (variable d’environnement)
- [ ] `ALLOWED_HOSTS` explicite (pas de `*`)
- [ ] HTTPS activé ; cookies sécurisés (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`)
- [ ] Mots de passe DB et services robustes ; pas de compte par défaut
- [ ] Aucun secret dans le code ni dans le dépôt
- [ ] Rate limiting sur les API sensibles
- [ ] Logs sans données sensibles ; pas de stack trace exposée aux utilisateurs

---

*Dernière mise à jour : 2025-01-30. Source : projet LPPP, Django security docs, bonnes pratiques OWASP.*
