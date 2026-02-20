# DevOps — Connexion Vercel Infopro au repo général

**Date** : 2026-02-20  
**Pilote** : DevOps  
**Statut** : 🟡 En cours (script push lancé ; config Vercel manuelle)  
**Contexte** : Crash lors de la config ; reprise avec mesures anti-crash.

---

## Objectif

Configurer le projet Vercel **lppp-infopro** pour qu’il déploie depuis le **repo général** (landingPageCreatorForProspection) avec Root Directory, sans passer par le clone du repo LPPP_infopro.

---

## Pré-requis (à faire avant ou en parallèle)

- [ ] **deploy/static-infopro-vercel/** doit exister dans le repo GitHub `landingPageCreatorForProspection`.
- Si absent : `git add deploy/static-infopro-vercel/ && git commit -m "feat(infopro): dossier static-infopro-vercel pour Vercel" && git push origin main`

---

## Étapes DevOps

| # | Action | Détail |
|---|--------|--------|
| 1 | Disconnect | Vercel → lppp-infopro → Settings → Git → **Disconnect** |
| 2 | Connect | Connect Git Repository → **landingPageCreatorForProspection** (LucasTymen) |
| 3 | Root Directory | Settings → General → Root Directory = **deploy/static-infopro-vercel** |
| 4 | Build | Build Command = vide, Framework = **Other** |
| 5 | Save + Redeploy | Save puis Redeploy |
| 6 | Vérifier | Ouvrir https://lppp-infopro.vercel.app/ et cliquer sur « Positionnement marketing » |

---

## Livrables

- [ ] lppp-infopro.vercel.app déploie correctement
- [ ] Page Positionnement marketing affiche le Growth Dashboard (funnel, carte perceptuelle, etc.)
- [ ] Mise à jour de `deploy/PUSH-INFOPRO.md` (nouvelle procédure sans clone)
- [ ] Mise à jour de `docs/logs/log-projet.md`
- [ ] Suppression de `docs/contacts/infopro/.progress-vercel-devops.md`

---

*Réf. : PUSH-INFOPRO.md, erreurs-et-solutions.md (Root Directory), pilotage-agents.mdc (anti-crash).*
