# Stack frontend — Next.js + React (standard projet)

**Rôle** : Règle technique **systématique** pour le frontend des landing pages LPPP.  
**Pilotes** : Designer, Dev Django (frontend), DevOps.  
**Objectifs** : effet « waouh », pages plus sexy grâce à React ; déploiement facile sur Vercel.

---

## 1. Décision

**Le frontend des landing pages utilise systématiquement :**

- **Next.js** : framework pour le code des pages et le routing.
- **React** : composants, interactivité, effets visuels (« waouh »).
- **Déploiement** : Vercel (intégration native Next.js, déploiement automatisé).

---

## 2. Architecture cible

| Couche | Techno | Hébergement |
|--------|--------|-------------|
| **Backend** (API, admin, campaigns, intelligence, Celery, n8n, Flowise) | Django | Contabo (Docker) |
| **Frontend** (landing pages, /essais/, pages publiques) | **Next.js + React** | **Vercel** |

- Le frontend Next.js peut consommer une API Django (ex. `/api/`) pour les données dynamiques.
- Les landing pages statiques ou pré-rendues (content_json) peuvent être servies par Next.js sans appel API si le contenu est injecté au build.

---

## 3. Règle pour l’équipe technique

**Toujours appliquer** :

1. **Nouvelles landing pages** : coder en Next.js + React, pas en templates Django HTML.
2. **Composants React** : utiliser pour les effets visuels (animations, micro-interactions, transitions) qui donnent l’effet « waouh ».
3. **Déploiement** : déployer le frontend Next.js sur Vercel (liaison Git, déploiement auto au push).
4. **Designer** : concevoir en pensant composants React (états, hover, scroll, transitions).
5. **Dev Django / frontend** : développer les pages dans le projet Next.js, réutiliser les composants.

---

## 4. Organisation du code (à mettre en place)

Options possibles :

- **Option A** : dossier `frontend/` ou `landings/` à la racine du dépôt LPPP (monorepo) — Next.js dans un sous-dossier.
- **Option B** : dépôt séparé pour le frontend Next.js (si l’équipe préfère).

La **configuration Vercel** pointe vers le répertoire Next.js (ex. `frontend/` ou racine si tout est Next.js).

---

## 5. Effets « waouh » (exemples React)

- Animations au scroll (fade-in, parallax léger).
- Transitions fluides entre états (hover, focus).
- Micro-interactions sur les CTA (scale, feedback visuel).
- Thème clair/sombre avec transition douce (déjà en place côté concept).
- Composants visuels distinctifs (cards, hero animé, sections décalées).

---

## 6. Références

- **Infra** : `infra-devops.md` (§ 3.2 Vercel, déploiement Next.js).
- **Décision** : `decisions.md`.
- **Vercel** : [vercel.com/lucas-tymens-projects](https://vercel.com/lucas-tymens-projects)

---

*Document créé à la demande utilisateur. Dernière mise à jour : 2025-01-30. L’équipe technique (Designer, Dev, DevOps) applique systématiquement Next.js + React pour le frontend et Vercel pour le déploiement.*
