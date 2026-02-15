# Déploiement LPPP sur Contabo (à côté de Squid Research) — Sécurisation

**Objectif** : documenter la faisabilité et les conditions pour déployer le projet LPPP sur Contabo **conjointement** à Squid Research, **sans endommager** ce dernier, avec une **sécurisation totale** impliquant DevOps, architecte, chef de projet et **pentester**.

**Références** : `infra-devops.md`, `regles-securite.md`, `utilisation-flowise-n8n-prod-squidresearch-contabo.md`, `.cursor/rules/pentester.mdc`, `.cursor/rules/devops.mdc`.

---

## 1. Faisabilité : LPPP et Squid Research sur le même Contabo

**Oui, c’est possible**, sous conditions d’**isolation** et de **priorité Squid Research**.

| Principe | Description |
|----------|-------------|
| **Deux stacks distincts** | LPPP a son propre `docker-compose` (conteneurs, volumes, réseaux). Squid Research garde le sien. Aucun partage de conteneurs ni de volumes entre les deux. |
| **Priorité Squid Research** | Pour toute modification de conteneurs, ports ou credentials sur le serveur, **Squid Research a la priorité**. LPPP s’adapte (ports, noms, chemins). En cas de conflit, c’est LPPP qui change. Voir `infra-devops.md` § 1. |
| **Pas de déploiement LPPP « dans » la prod Squid** | Ne pas lancer le stack LPPP dans le même répertoire ni avec les mêmes noms de conteneurs/volumes que Squid Research. Deux répertoires (ex. `~/squidResearch`, `~/homelucastoolsLandingsPagesPourProspections` ou équivalent sur le VPS). |
| **Réseau / reverse proxy** | Sur le même VPS : deux applications = deux sous-chemins ou deux (sous-)domaines (ex. `lppp.ton-domaine.com`, `app.squidresearch.com`). Le reverse proxy (Nginx, Caddy, Traefik) route vers le bon conteneur selon le host/path. |

**Résumé** : déployer LPPP sur Contabo à côté de Squid Research est faisable en gardant deux environnements complètement séparés (fichiers, conteneurs, .env) et en réservant des ports / domaines distincts. Aucune modification des conteneurs ou credentials Squid Research.

---

## 2. Sécurisation totale — Qui fait quoi

La sécurisation doit être **prévue et validée** avant mise en prod, avec les rôles suivants.

| Rôle | Responsabilités (sécurité) |
|------|----------------------------|
| **DevOps** | Isolation des stacks (réseaux Docker, volumes, .env séparés). Secrets (pas de credentials dans le dépôt, variables d’env sur le serveur). Déploiement (CI/CD ou manuel) sans exposition des clés. Vérification des ports et de la coexistence avec Squid Research. Voir `infra-devops.md`, `.cursor/rules/devops.mdc`. |
| **Architecte** | Conception de l’isolation (réseau, reverse proxy, séparation des services). Choix des chemins, domaines et règles de routage pour que LPPP et Squid Research ne se chevauchent pas. |
| **Chef de projet** | Validation du plan de déploiement et de la checklist sécurité. S’assurer que Pentester, DevOps et Architecte sont alignés avant toute mise en prod. Mise à jour des logs et de la base de connaissances (décisions, procédures). |
| **Pentester** | **Réduction des vulnérabilités et des risques** : audit des failles (injection, XSS, CSRF, exposition d’API, credentials). Réduction des risques de **détection** (scans, signatures) et de **hacking** (renforcement des contrôles d’accès, rate limiting, logs). Application de `regles-securite.md` et de la politique credentials. Voir `.cursor/rules/pentester.mdc` et `politique-credentials-securite-flux.md` (si présent). |

**Règle** : aucun déploiement LPPP sur Contabo en production sans :

1. Validation **DevOps** (isolation, secrets, ports).  
2. Validation **Architecte** (schéma d’isolation et de routage).  
3. Validation **Chef de projet** (plan et checklist).  
4. **Audit / revue Pentester** (vulnérabilités, durcissement, recommandations appliquées).

---

## 3. Mesures de sécurité à appliquer (résumé)

- **Checklist prod** : `regles-securite.md` § 9 — `DEBUG=False`, `SECRET_KEY` forte, `ALLOWED_HOSTS` explicite, HTTPS, cookies sécurisés, pas de secrets dans le code.  
- **Django** : configuration production (HTTPS, CSRF, XSS, injection), authentification et sessions (cookies sécurisés).  
- **API et rate limiting** : limiter les appels sur les endpoints sensibles (enrichissement, webhooks).  
- **Flux et credentials** : pas de log de mots de passe ni de tokens ; isolation des flux (Flowise, n8n) et validation des entrées.  
- **Pentester** : identifier et traiter les vulnérabilités, réduire la surface d’attaque et les risques de détection / prise de contrôle.

Le détail des règles est dans `regles-securite.md` et dans la règle agent `pentester.mdc`.

---

## 4. Séparation stricte LPPP / SquidResearch (conteneurs étanches)

LPPP et SquidResearch sont **deux projets distincts** qui doivent rester séparés dans des conteneurs étanches et **ne pas entrer en conflit**.

| Élément | SquidResearch | LPPP |
|---------|---------------|------|
| **Répertoire** | `/var/www/squidresearch` | `/var/www/lppp` |
| **Django** | port 8000 | port 8010 |
| **PostgreSQL** | 5432 (hôte) | 5433 (hôte) |
| **Redis** | 6379 (hôte) | 6380 (hôte) |
| **n8n** | 5679 (hôte) | 5681 (hôte) |
| **Flowise** | 3000/3001 | 3010 (hôte) |
| **Conteneurs** | squidresearch_* (ou préfixe SquidResearch) | lppp_* |

**Règle** : aucun partage de conteneurs, volumes ni `.env` entre les deux projets. SquidResearch a la priorité ; LPPP s’adapte.

---

## 5. Comment fonctionne le domaine (SquidResearch sur Contabo)

### 5.1 SquidResearch

1. **DNS** : `squidresearch.com` et `www.squidresearch.com` pointent vers l’IP du VPS : **173.249.4.106**.
2. **Serveur** : Nginx écoute sur les ports 80 et 443, gère le SSL (Let’s Encrypt), et proxy vers Django (port 8000) selon le Host.
3. **Django SquidResearch** : `ALLOWED_HOSTS` contient `squidresearch.com`, `www.squidresearch.com`, `173.249.4.106`. `SITE_URL` = `https://www.squidresearch.com`.

**Flux** : DNS → 173.249.4.106 → Nginx (80/443) → Django SquidResearch (8000).

### 5.2 Accès par IP vs par domaine

- **https://www.squidresearch.com** : trafic via Nginx, Host `www.squidresearch.com`.
- **http://173.249.4.106:8000** : accès direct au port Django SquidResearch (si 173.249.4.106 dans ALLOWED_HOSTS).

### 5.3 LPPP — domaine dédié (sous-domaine ou domaine séparé)

Pour que LPPP soit accessible par un nom de domaine (ex. `lppp.tondomaine.com` ou `lppp.squidresearch.com`) :

1. **DNS** : créer un enregistrement pointant vers 173.249.4.106 (ex. `lppp.tondomaine.com` → 173.249.4.106).
2. **Nginx** : ajouter un bloc `server` qui écoute pour le Host LPPP et fait `proxy_pass` vers `127.0.0.1:8010` (port exposé par le conteneur web LPPP). Nginx route selon le Host (squidresearch.com → 8000 ; lppp.tondomaine.com → 8010).
3. **Django LPPP** : dans `.env` sur le serveur :
   - `ALLOWED_HOSTS=lppp.tondomaine.com,173.249.4.106,localhost,127.0.0.1,web`
   - `SITE_URL=https://lppp.tondomaine.com`
   - `DEBUG=False`

4. **Accès direct par IP** : `http://173.249.4.106:8010` fonctionne si `173.249.4.106` est dans `ALLOWED_HOSTS`.

**Récap** : SquidResearch et LPPP coexistent sur le même serveur ; chacun a ses ports et son (sous-)domaine ; Nginx fait le routage selon le Host.

---

## 6. Prochaines étapes recommandées

1. **Architecte + DevOps** : rédiger un schéma d’isolation (réseau, répertoires, reverse proxy) pour Contabo avec LPPP + Squid Research.  
2. **DevOps** : documenter la procédure de déploiement LPPP sur le VPS (clone, .env, ports, commandes) sans toucher à Squid Research.  
3. **Chef de projet** : ajouter une entrée dans le registre / les décisions et une checklist « Pré-déploiement Contabo LPPP » (validation DevOps, Architecte, Pentester).  
4. **Pentester** : réaliser une revue de sécurité (config Django, API, flux Flowise/n8n, exposition des services) et une liste de recommandations avant ou juste après la première mise en prod.

---

*Document créé pour cadrer le déploiement LPPP sur Contabo et la sécurisation avec l’équipe (DevOps, Architecte, Chef de projet, Pentester). Dernière mise à jour : 2026-02-07. § 4–5 : séparation LPPP/SquidResearch, domaine et Nginx.*
