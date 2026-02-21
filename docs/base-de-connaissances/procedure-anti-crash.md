# Procédure anti-crash — sauvegarde incrémentale et reprise

> **⚠️ SYSTÉMATIQUE POUR TOUS — 2026-02-21** : En raison d’une instabilité du système, ces mesures sont **obligatoires pour l’ensemble de l’équipe** (tous les agents). Aucune exception. Voir `decisions.md` (2026-02-21).

**Objectif** : éviter de recommencer une tâche multi-étapes du début après un crash (Cursor, IDE, session). Permettre une reprise rapide au dernier point connu.

**Applicable** : toute tâche multi-fichiers ou multi-étapes (création landing, duplication projet, refactor, sprint). **Désormais obligatoire pour tous**, y compris les tâches jugées courtes.

**Références** : `pilotage-agents.mdc` § « Sauvegarde incrémentale obligatoire », `erreurs-et-solutions.md` § « Crash / reprise », `decisions.md` (2026-01-30, 2026-02-21).

---

## 1. Avant de commencer une tâche multi-étapes

- [ ] Créer un fichier `.progress-<slug>.md` à la racine (ex. `.progress-infopro.md`) ou utiliser `docs/TODO.md` comme suivi.
- [ ] Inscrire la date, le titre de la tâche et une liste numérotée des étapes prévues.
- [ ] Optionnel : ajouter un commentaire timestamp dans le fichier principal concerné.

**Exemple `.progress-infopro.md`** :

```markdown
# [2026-01-30 14:32] Landing Infopro — progression

## Étapes prévues
1. Créer dossier docs/contacts/infopro/
2. Adapter landing-proposition-infopro.json
3. Mettre à jour proposition.html (variables infopro)
4. Export statique et vérification

## Fait
- [x] 1. Dossier créé — 14:35
- [x] 2. JSON adapté — 14:42
- [ ] 3. En cours
- [ ] 4. À faire
```

---

## 2. Pendant la tâche — à chaque bloc logique (1–3 fichiers)

- [ ] **Commit git** avec message explicite : `feat(infopro): étape 2 — JSON adapté`
- [ ] Mettre à jour le fichier de progression (cocher l’étape, timestamp).
- [ ] Mettre à jour `docs/logs/log-projet.md` et `docs/logs/log-ia.md` (brève ligne).
- [ ] Optionnel : commentaire dans le code : `<!-- STEP 2026-01-30T14:42 — JSON infopro adapté -->`

---

## 3. En cas de crash ou d’interruption

1. Consulter `docs/logs/log-projet.md` et `docs/logs/log-ia.md` pour le dernier état.
2. Chercher un fichier `.progress-<slug>.md` ou des commentaires `<!-- STEP ... -->` dans les fichiers modifiés.
3. Consulter les commits récents : `git log --oneline -10`.
4. Reprendre **au dernier marqueur connu**, pas du début.
5. Si besoin : documenter l’état dans `erreurs-et-solutions.md` (entrée « Crash / reprise ») pour l’agent en charge des erreurs.

---

## 4. Une fois la tâche terminée et validée

- [ ] Supprimer le fichier `.progress-<slug>.md`.
- [ ] Retirer les commentaires `<!-- STEP ... -->` temporaires (ou les conserver si l’utilisateur le souhaite pour l’historique).
- [ ] Commit final + push sur les deux remotes : `make push-both` ou `make commit-push MSG="feat(infopro): landing terminée"`.
- [ ] Mettre à jour `docs/TODO.md`, segmentations concernées et logs.

---

## 5. Checklist rapide (OBLIGATOIRE pour tout agent)

| Action | Fréquence | Obligatoire |
|--------|-----------|-------------|
| Commit git (message explicite) | Après chaque bloc logique (1–3 fichiers) | Oui |
| Mise à jour log-projet / log-ia | À chaque étape | Oui |
| Fichier `.progress-<slug>.md` | Créer en début de tâche multi-étapes, supprimer à la fin | Oui |
| Commentaires timestamp | Étape clé ou reprise difficile | Recommandé |
| Reprise au dernier marqueur | En cas de crash — jamais recommencer du début | Oui |

---

## 6. Rappel — système instable

En cas d’instabilité globale : **appliquer ces mesures sans dérogation**. Le Chef de Projet, l’Orchestrateur et l’agent en charge des erreurs vérifient que tous les agents les suivent. En début de session, consulter `log-projet.md` et reprendre au dernier marqueur.

---

*Dernière mise à jour : 2026-02-21 — Mesures anticrash rendues systématiques pour toute l’équipe (instabilité). Décision decisions.md 2026-02-21.*
