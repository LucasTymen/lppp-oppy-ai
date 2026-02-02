# Stratégie : landings standalone vs hub (une seule app, onglet principal)

**Contexte** : aujourd’hui le frontend Next.js sur Vercel sert une page d’accueil (hub) avec un lien vers « Page P4S-archi ». Un visiteur sur la landing P4S peut remonter à l’onglet principal et découvrir les autres landings.

**Risque perçu** : n’importe qui peut, en remontant au hub, accéder aux landings des autres prospects.

**Préférence utilisateur** : landings **standalone** pour chaque intervenant (pas de hub commun qui expose les autres).

---

## 1. Avis agent (coordination technique)

- **Ton inquiétude est légitime** : un hub avec liens vers toutes les landings casse l’effet « page dédiée à ce prospect ». En B2B, le prospect doit avoir l’impression d’une proposition sur-mesure, pas d’un catalogue.
- **Standalone = meilleure maîtrise** : une URL par prospect, sans navigation vers une page listant les autres, réduit le risque de fuite et renforce le positionnement « one-to-one ».
- **Options cohérentes avec ta préférence** :
  - **Option A** : un projet Vercel par prospect (ex. `p4s-archi.vercel.app` ou sous-domaine dédié) — isolation maximale, un peu plus de config par nouveau prospect.
  - **Option B** : un seul projet Next.js mais **supprimer le hub** : la page d’accueil `/` n’existe pas ou redirige ; chaque landing est à une URL « propre » (ex. `/p4s-archi`) et **aucun lien** vers une liste d’autres landings. Les gens n’arrivent que par le lien direct que tu envoies.
  - **Option C** : sous-domaines ou chemins dédiés + pas de page d’accueil listant les landings (même idée que B, avec des URLs encore plus isolées si besoin).

En résumé : **standalone est aligné avec la confidentialité et le positionnement** ; le Chef de Projet et l’architecte peuvent trancher entre A (un projet par prospect) et B/C (un projet, pas de hub).

---

## 2. Avis Chef de Projet / Product Owner

- **Confidentialité et confiance** : chaque prospect doit recevoir une URL qu’il peut partager en interne sans que ses collègues tombent sur d’autres clients. Landings standalone = pas de découverte accidentelle des autres.
- **Positionnement** : la landing doit être perçue comme « ta page pour eux », pas comme « une page parmi d’autres ». Pas de hub = pas de liste = message plus fort.
- **Validation livrables** : on valide que toute nouvelle landing respecte la règle « pas de lien vers une page listant les autres prospects » ; si on garde un seul projet Vercel, la page d’accueil ne doit pas être un index des landings.
- **Recommandation** : **landings standalone** (un lien = une landing, pas de remontée vers un hub listant les autres). Choix technique (un projet par prospect vs un projet sans hub) à laisser à l’architecte / DevOps selon coût et simplicité.

---

## 3. Avis Architecte (technique, structure)

- **Isolation** : standalone = une URL (ou un sous-domaine / projet) par prospect. Pas de navigation commune qui expose les autres → aligné avec la confidentialité et la demande métier.
- **Deux familles de solutions** :
  1. **Un projet Vercel par prospect**  
     - Chaque prospect a son propre projet (ex. repo ou sous-dossier dédié, ou même repo avec plusieurs projets Vercel pointant vers des `rootDirectory` ou branches différents).  
     - URLs du type : `p4s-archi.vercel.app` ou `landing-p4s.vercel.app`.  
     - **+** : isolation totale, pas de hub possible. **−** : plus de projets à gérer, déploiements et env vars à dupliquer (ou à scriptiser).
  2. **Un seul projet Next.js, sans hub**  
     - Le même projet Vercel sert plusieurs routes (`/p4s-archi`, `/autre-prospect`, etc.) mais **il n’y a pas de page d’accueil listant les landings**.  
     - La route `/` : 404 ou redirection vers une page neutre (ex. « LPPP » sans liens), ou vers une landing par défaut si tu veux.  
     - Les prospects n’arrivent que par le **lien direct** (ex. `...vercel.app/p4s-archi`). Pas de lien « Retour à l’accueil » qui mène à une liste.  
     - **+** : un seul déploiement, un seul projet. **−** : si quelqu’un devine d’autres slugs (`/autre-prospect`), il peut y accéder ; on peut limiter avec des tokens ou de l’auth si besoin plus tard.

- **Recommandation court terme** : **Option 2 (un projet, pas de hub)** : supprimer ou neutraliser la page d’accueil actuelle (pas de lien vers les landings), ne pas mettre de lien « Accueil » sur les landings qui ramène à une liste. Chaque landing reste une entrée standalone pour celui qui reçoit le lien. Si plus tard tu veux une isolation encore plus forte (domaines/sous-domaines par prospect), on passe à l’option 1 avec un projet (ou sous-domaine) par prospect.

---

## 4. Synthèse et décision à enregistrer

| Critère | Hub actuel | Standalone (recommandé) |
|--------|------------|--------------------------|
| Confidentialité | Faible (liste des landings accessible) | Forte (pas de liste, lien direct uniquement) |
| Positionnement | « Une page parmi d’autres » | « Ta page pour ce prospect » |
| Complexité | Un projet, une page d’accueil | Un projet sans hub, ou un projet par prospect |

**Accord de principe** : **landings standalone** — pas de page d’accueil qui liste les landings des autres ; chaque prospect reçoit une URL dédiée, sans remontée possible vers un index.

**Suite technique (fait 2025-01-30)** : page d'accueil neutralisée (`frontend/src/app/page.tsx` — aucun lien) ; landing P4S titre « P4S Architecture — Joël, suite à notre échange », pas de lien Accueil. Réf. `deploiement-vercel-frontend.md` § 6.

**À faire (optionnel)** :
- Supprimer ou neutraliser la page d’accueil Next.js (pas de liens vers les landings).
- Sur chaque landing : pas de lien « Retour à l’accueil » (ou un accueil neutre sans liste).
- Optionnel plus tard : un projet Vercel ou sous-domaine par prospect si besoin d’isolation maximale.

Une fois la variante choisie (un projet sans hub vs un projet par prospect), mettre à jour `decisions.md` et `deploiement-vercel-frontend.md`.

---

*Document créé suite à la demande utilisateur sur le risque d’accès aux landings des autres via l’onglet principal. Avis agent, Chef de Projet et Architecte. Dernière mise à jour : 2025-01-30.*
