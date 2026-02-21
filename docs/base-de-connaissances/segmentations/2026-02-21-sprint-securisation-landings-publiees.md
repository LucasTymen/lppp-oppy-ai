# Sprint : Sécurisation de toutes les landing pages publiées

**Date** : 2026-02-21  
**Statut** : En cours  
**Rôles** : DevOps, Architecte réseau, Pentester, Chef de Projet  

---

## 1. Objectif

Sécuriser toutes les landing pages publiées sur Vercel en appliquant :
- Headers de sécurité (X-Content-Type-Options, X-Frame-Options, Referrer-Policy)
- Vérification absence de secrets dans le code déployé
- Alignement avec la checklist `regles-securite.md` § 9

---

## 2. Landings concernées

| Landing | Dossier deploy | Repo / Vercel |
|---------|----------------|---------------|
| Infopro | `static-infopro-vercel/` | landingPageCreatorForProspection (Root Dir) |
| Promovacances | `static-promovacances-vercel/` | repo dédié |
| P4S | `static-p4s-vercel/` | LPPP_P4S-Architecture |
| Casapy | `LPPP-Casapy/` | LPPP_casapy |
| Ackuracy | `standalone-ackuracy/` | LPPP_Ackuracy |
| Yuwell | `yuwell-portfolio/` | LPPP_yuwell_portfolio |
| 0flow | submodule | LPPP_0flow |
| Orsys | submodule | LPPP_Orsys |
| FitClem | submodule | LPPP-FitClem |

---

## 3. Actions

### 3.1 Headers de sécurité (vercel.json)

Ajouter à chaque `vercel.json` :

```json
"headers": [
  {
    "source": "/(.*)",
    "headers": [
      { "key": "X-Content-Type-Options", "value": "nosniff" },
      { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
      { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
    ]
  }
]
```

- **X-Content-Type-Options: nosniff** : empêche le navigateur de deviner le type MIME.
- **X-Frame-Options: SAMEORIGIN** : limite l’embedding en iframe (évite le clickjacking depuis d’autres domaines).
- **Referrer-Policy** : limite les fuites de referrer en cross-origin.

> Vercel fournit déjà HSTS par défaut.

### 3.2 Vérification secrets

- [ ] Aucun `AIza`, `pk_live_`, `sk_live_` dans les fichiers déployés
- [ ] Aucun `FLOWISE_API_KEY` ni token dans le HTML/JS client (seuls `flowise_api_host`, `flowise_chatflow_id` pour l’embed si pertinent)

### 3.3 Checklist pré-prod

Voir `checklist-pre-prod-integrite.md` (secrets, config, page accessible).

---

## 4. Fichiers modifiés

- `deploy/static-infopro-vercel/vercel.json`
- `deploy/static-promovacances-vercel/vercel.json`
- `deploy/static-p4s-vercel/vercel.json`
- `deploy/LPPP-Casapy/vercel.json`
- `deploy/standalone-ackuracy/vercel.json`
- `deploy/standalone-p4s/vercel.json`
- `deploy/yuwell-portfolio/vercel.json`

---

## 5. Clôture

Après modification : commit, push, redéploiement Vercel (automatique si lié au repo). Vérifier que les headers sont bien envoyés (`curl -I https://...` ou DevTools → Network → Headers).
