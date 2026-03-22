# Plan de mise à jour — Next.js / React (sécurité RSC & advisories)

**Rôle** : Procédure **obligatoire** pour tout projet LPPP utilisant **Next.js avec App Router** (React Server Components).  
**Pilotes** : **DevOps** (exécution upgrade, inventaire), **Chef de Projet** (priorisation), **Dev Django / frontend** (validation build).  
**Références officielles** : billet Next.js *Security Update: December 11, 2025* ; correctifs React en amont (CVE listées ci‑dessous).

---

## 1. Pourquoi ce plan existe

Des **vulnérabilités critiques** ont été identifiées sur le **protocole React Server Components** (contexte React2Shell / correctifs amont). Elles impactent les applications Next.js en **App Router** :

| CVE | Gravité | Risque |
|-----|---------|--------|
| **CVE-2025-55182** (React) / **CVE-2025-66478** (Next.js) | Critique | **React2Shell — exécution de code à distance (RCE)** : requêtes forgées peuvent mener à une exécution de code non autorisée. Disclosure 4 déc. 2025. |
| **CVE-2025-55184** | Élevée | **Déni de service (DoS)** : requête HTTP forgée peut provoquer une boucle infinie et bloquer le process serveur. |
| **CVE-2025-67779** | (complément) | **Correctif complet** du DoS — le premier correctif pour 55184 était incomplet ; **ré-upgrader** si déjà passé sur une version « initiale » recommandée. |
| **CVE-2025-55183** | Moyenne | **Exposition de code source** : requête forgée peut faire renvoyer le code compilé d’autres Server Functions (logique métier, secrets inline dans le code). |

**Pages Router** : non affecté par ces vecteurs RSC, mais **Next.js recommande tout de même** de monter sur une version patchée de la ligne de release.

**Il n’y a pas de contournement** : **upgrade obligatoire** vers une version corrigée.

---

## 2. Versions corrigées (référence — décembre 2025)

À appliquer selon la **ligne majeure** du projet (`package.json` → `next`) :

| Ligne actuelle | Monter vers (exemple advisory) |
|----------------|--------------------------------|
| 14.x (≥ 13.3, 14.0.x, 14.1.x) | **14.2.35** (dernière 14.2.x patchée) |
| 15.0.x | **15.0.7** |
| 15.1.x | **15.1.11** |
| 15.2.x | **15.2.8** |
| 15.3.x | **15.3.8** |
| 15.4.x | **15.4.10** |
| 15.5.x | **15.5.9** |
| 15.x canary | **15.6.0-canary.60** |
| 16.0.x | **16.0.10** |
| 16.x canary | **16.1.0-canary.19** |

**Commandes types** (adapter la ligne) :

```bash
npm install next@14.2.35   # exemple 14.x
# ou : next@15.5.9, next@16.0.10, etc.
```

**Outil interactif** (vérification + bump déterministe) :

```bash
npx fix-react2shell-next
```

Après upgrade : `npm audit`, build local (`npm run build`), tests, puis déploiement (Vercel).

**Packages à vérifier** (Vercel dashboard ou CLI) : `next`, `react-server-dom-webpack`, `react-server-dom-parcel`, `react-server-dom-turbopack`.

---

## 2b. Actions spécifiques Vercel (déploiements hébergés sur Vercel)

| Action | Détail |
|--------|--------|
| **Vercel Agent** | Détection automatique des projets vulnérables et ouverture de PR pour upgrade. Voir le dashboard Vercel → Security. |
| **Standard Protection** | Activer la **Standard Protection** pour **tous** les déploiements (preview, staging) **sauf** le domaine de production. Réduit l’exposition des previews. |
| **Audit des liens partagés** | Vérifier les liens partagés pointant vers des previews ou déploiements non protégés ; mettre en place des exceptions de protection si nécessaire. |
| **Rotation des secrets** | Si l’application était **en ligne et non patchée au 4 déc. 2025 13:00 PT**, faire **tourner tous les secrets** (env vars) dès que le patch est déployé. Voir [Vercel docs — rotating env vars](https://vercel.com/docs/projects/environment-variables). |
| **WAF Vercel** | Vercel applique des règles WAF contre les variantes connues d’exploit. **Le WAF ne remplace pas l’upgrade** — le correctif applicatif reste obligatoire. |

---

## 3. Plan de mise à jour « partout » (inventaire LPPP)

### 3.1 Périmètre

Tout dépôt qui contient :

- un `package.json` avec **`next`** ;
- et usage de l’**App Router** (`app/`).

Inclut notamment : repos **standalone** de landings (Vercel), sous-dossiers `deploy/static-*-vercel` si Next.js, monorepo `frontend/` si présent, **tout clone** hors workspace LPPP référencé dans `deploy/README-standalone.md` ou fiches contact.

### 3.2 Cadence recommandée

| Fréquence | Action |
|-----------|--------|
| **Immédiat** | Après publication d’un **advisory critique** Next.js / React (RSC) : traiter en **P0** sous 7 jours ouvrés. |
| **Mensuel** | DevOps : contrôle `npm outdated` / release notes Next.js sur les projets Next listés. |
| **Avant chaque prod** | Case **checklist pré-prod** : version `next` ≥ version minimale patchée connue (voir § 2 ou dernier advisory). |

### 3.3 Registre d’inventaire (à tenir à jour)

Documenter dans un tableur ou dans **`docs/logs/log-projet.md`** / fiche contact :

| Projet / repo | Branche prod | `next` (version) | App Router ? | Dernière vérif. advisory | Responsable |
|---------------|--------------|------------------|--------------|---------------------------|-------------|
| *ex. LPPP_P4S-Architecture* | main | *à lire* | oui/non | YYYY-MM-DD | DevOps |

**Orchestrateur / Chef de Projet** : s’assurer que la liste des **URLs Vercel + repos** connus est couverte (cf. `console/` landings, `deploy_url`, README contacts).

---

## 4. RACI (synthèse)

| Rôle | Action |
|------|--------|
| **DevOps** | **R** : inventaire, exécution `npm install next@…`, build, push, redeploy Vercel ; documenter version après coup. |
| **Dev Django / frontend** | **R** : valider régression UI, routes, Server Actions si utilisées. |
| **Chef de Projet** | **A** : prioriser P0, valider checklist pré-prod après upgrade. |
| **Pentester** | **C** : si surface RSC / Server Functions sensible. |

---

## 5. Liens utiles (à consulter à chaque incident)

- **Vercel — React2Shell Security Bulletin** : [vercel.com/knowledge-base/react2shell-security-bulletin](https://vercel.com/knowledge-base/react2shell-security-bulletin) — Vue d’ensemble (RCE, DoS, source disclosure), Vercel Agent, Standard Protection, rotation secrets.
- Blog Next.js — *Security Update: December 11, 2025* (rechercher sur [nextjs.org/blog](https://nextjs.org/blog)).
- Dépôt outil : `fix-react2shell-next` (GitHub, lié dans l’advisory officiel).
- Doc projet : `stack-frontend-nextjs-react.md`, `checklist-pre-prod-integrite.md`, `procedure-fin-landing-repo-deploiement.md`.
- Registre erreurs : `erreurs-et-solutions.md` § Next.js / sécurité RSC.

---

## 6. Django / landings statiques

Les exports **HTML statiques** (sans runtime Next.js sur Vercel en mode « static only ») ne sont **pas** impactés par ces CVE côté **runtime Next sur le serveur**. En revanche, si le **build** qui génère ces fichiers passe par **Next.js App Router**, le **pipeline de build** doit utiliser une version **patchée** de `next` pour éviter vulnérabilités en CI / preview.

---

*Document créé suite aux advisories Next.js décembre 2025 (CVE-2025-55183, CVE-2025-55184, CVE-2025-67779). Dernière mise à jour : 2026-01-30 — **réviser** à chaque nouvel advisory officiel.*
