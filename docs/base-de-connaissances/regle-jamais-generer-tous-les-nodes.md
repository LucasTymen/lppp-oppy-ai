# Règle : Ne jamais générer tous les nodes

**Pilote** : Tous les agents.  
**Référence** : `pilotage-agents.mdc`, `erreurs-et-solutions.md`.

---

## Règle impérative (toutes les équipes)

**Ne jamais générer tous les nodes** — utiliser **uniquement** ce qui est nécessaire pour l’infographie ou le projet.

### Ce que « nodes » désigne

- **node_modules** : arbre de dépendances npm (`npm install` génère des milliers de fichiers).
- Tout autre arbre volumineux créé automatiquement (cache, build, etc.) qui n’est pas strictement nécessaire à l’indexation ou au travail en cours.

### Pourquoi

1. **OOM (Out Of Memory)** : Cursor indexe le workspace. Si `node_modules/` est présent à la racine ou dans des dossiers ouverts, l’indexation peut provoquer un crash (« The window terminated unexpectedly (reason: 'oom') »).
2. **Lenteur** : gros arbres = recherche et ouverture lentes.
3. **Bruit** : fichiers inutiles masquent les vrais besoins du projet.

---

## Ce qu’il faut faire

| Contexte | Action |
|----------|--------|
| **Projet LPPP (racine)** | Ne **pas** exécuter `npm install` à la racine. Le projet est Django ; Next.js vit dans `frontend/` ou `deploy/standalone-*`. |
| **Standalone / deploy** | `npm install` **uniquement** dans le dossier du projet concerné (ex. `deploy/standalone-ackuracy`, `deploy/LPPP-Casapy` si besoin). |
| **Infographie / visuels** | N’utiliser que les notes, briefs et assets nécessaires à la tâche. Ne pas tout charger. |
| **Cursor** | S’assurer que `node_modules/` est ignoré (`.gitignore`, `.cursorignore`) et **supprimé** s’il a été créé à la racine par erreur. |

---

## Si node_modules a été créé à la racine

```bash
# À la racine du projet LPPP
rm -rf node_modules
# Vérifier qu'il n'est pas committé (déjà dans .gitignore)
git status
```

---

## Prévention

- **Tous les agents** : ne jamais proposer ni exécuter `npm install` à la racine du projet LPPP sans demande explicite.
- **DevOps** : rappeler cette règle lors des procédures de déploiement.
- **Chef de Projet** : valider que le workspace reste léger et exploitable.

---

*Décision enregistrée : 2026-01-30. Cause : crash Cursor OOM après génération de nodes à la racine.*
