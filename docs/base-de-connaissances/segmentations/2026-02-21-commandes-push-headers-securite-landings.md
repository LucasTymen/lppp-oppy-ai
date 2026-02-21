# Commandes pour propager les headers sécurité sur les landings

**Contexte** : les `vercel.json` avec headers (X-Content-Type-Options, X-Frame-Options, Referrer-Policy) ont été modifiés dans le repo LPPP. Pour que les headers s’appliquent sur Vercel, chaque landing doit avoir son vercel.json à jour dans son repo de déploiement.

---

## Infopro (déployé depuis repo principal)

**Source** : `deploy/static-infopro-vercel/` (Root Directory sur Vercel)  
**Repo** : landingPageCreatorForProspection (déjà poussé)

Le vercel.json est déjà dans le repo principal. Si les headers n’apparaissent pas :

1. Vercel → projet **lppp-infopro** → Deployments → dernier déploiement → **Redeploy**
2. Ou : Settings → Caching → **Purge Cache** puis Redeploy

---

## Promovacances (repo LPPP_promovacances)

```bash
cd ~/tools/homelucastoolsLandingsPagesPourProspections

# Clone + copie (inclut vercel.json à jour)
rm -rf deploy/repo-promovacances
git clone https://github.com/LucasTymen/LPPP_promovacances.git deploy/repo-promovacances
cp -r deploy/static-promovacances-vercel/* deploy/repo-promovacances/

cd deploy/repo-promovacances
git add .
git commit -m "feat(security): headers X-Content-Type-Options, X-Frame-Options, Referrer-Policy"
git push origin main
git remote add gitlab git@gitlab.com:LucasTymen/lppp_promovacances.git 2>/dev/null || true
git push gitlab main
```

---

## P4S (repo LPPP_P4S-Architecture)

Le vercel.json est dans `deploy/static-p4s-vercel/`. Il faut copier **tout** le dossier (pas seulement index.html) :

```bash
cd ~/tools/homelucastoolsLandingsPagesPourProspections

# Créer clone si besoin
rm -rf deploy/repo-p4s
git clone https://github.com/LucasTymen/LPPP_P4S-Architecture.git deploy/repo-p4s

# Copier tout (index.html, rapport.html, vercel.json)
cp deploy/static-p4s-vercel/index.html deploy/repo-p4s/
cp deploy/static-p4s-vercel/rapport.html deploy/repo-p4s/ 2>/dev/null || true
cp deploy/static-p4s-vercel/vercel.json deploy/repo-p4s/

cd deploy/repo-p4s
git add .
git commit -m "feat(security): headers X-Content-Type-Options, X-Frame-Options, Referrer-Policy"
git push origin main
git remote add gitlab git@gitlab.com:LucasTymen/lppp_p4s-architecture.git 2>/dev/null || true
git push gitlab main
```

---

## Casapy (repo LPPP_casapy)

Le vercel.json est déjà dans `deploy/LPPP-Casapy/` (pas un submodule, dossier normal dans LPPP). À pousser vers le repo Casapy :

```bash
cd ~/tools/homelucastoolsLandingsPagesPourProspections/deploy/LPPP-Casapy

git add vercel.json
git status
git commit -m "feat(security): headers X-Content-Type-Options, X-Frame-Options, Referrer-Policy"
git pull origin main --rebase 2>/dev/null || true
git push origin main
git push gitlab main
```

---

## Ackuracy (repo LPPP_Ackuracy)

Le script copie `deploy/standalone-ackuracy/*` vers le repo. Lancer le script :

```bash
cd ~/tools/homelucastoolsLandingsPagesPourProspections
bash deploy/push-standalone-ackuracy.sh
```

(Pour un message de commit plus précis : modifier le script temporairement ou faire un `git commit --amend` après.)

---

## Yuwell (submodule → LPPP_yuwell_portfolio)

```bash
cd ~/tools/homelucastoolsLandingsPagesPourProspections/deploy/yuwell-portfolio

git add vercel.json
git status
git commit -m "feat(security): headers X-Content-Type-Options, X-Frame-Options, Referrer-Policy"
git push origin main
git push gitlab main

# Revenir au repo LPPP et mettre à jour la référence du submodule
cd ~/tools/homelucastoolsLandingsPagesPourProspections
git add deploy/yuwell-portfolio
git commit -m "chore: mise à jour ref submodule yuwell (headers sécurité)"
git push origin main
git push gitlab main
```

---

## Vérification après déploiement

```bash
curl -I https://lppp-infopro.vercel.app
curl -I https://lppp-promovacances.vercel.app
curl -I https://lppp-p4-s-architecture.vercel.app
curl -I https://lppp-casapy.vercel.app
curl -I https://lppp-ackuracy.vercel.app
curl -I https://lppp-yuwell-portfolio.vercel.app
```

Vérifier la présence de : `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`.
