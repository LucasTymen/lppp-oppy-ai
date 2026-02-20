# Push Infopro Digital — repo lppp-infopro

**Vercel** : projet **lppp-infopro**, lié au repo `LucasTymen/lppp-infopro`.  
**Workflow** : copier le contenu exporté dans le repo lppp-infopro, push → Vercel déploie.

---

## 1. Régénérer l'export (après modification)

```bash
python manage.py export_landing_static infopro --json docs/contacts/infopro/landing-proposition-infopro.json --output deploy/static-infopro-vercel/index.html --rapport-md docs/contacts/infopro/rapport-complet-infopro.md
```

---

## 2. Copier dans lppp-infopro et push

**WSL / bash** (recommandé) :

```bash
cd ~/tools/homelucastoolsLandingsPagesPourProspections
chmod +x deploy/push-infopro.sh
./deploy/push-infopro.sh
```

**PowerShell** : `.\deploy\push-infopro.ps1` (depuis la racine LPPP ; nécessite git dans le PATH)

Le script : export → clone lppp-infopro → copie → commit → push origin + gitlab.

Vercel déploie automatiquement.

---

## 3. Vercel

- Repo : **lppp-infopro**
- Root Directory : vide (ou `./`)
- Framework : Other, Build : vide

---

## 4. URL

https://lppp-infopro.vercel.app/
