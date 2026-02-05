# Pointeur — Log commun LPPP ↔ SquidResearch

**Ce fichier est un pointeur.** Le document de référence (adresses, ports, variables d’env, chemins, coexistence des deux stacks, état des projets Docker) est maintenu dans le dépôt **SquidResearch**.

---

## Où trouver le log commun

| Contexte | Chemin |
|----------|--------|
| **Linux / WSL** | `/home/lucas/tools/squidResearch/docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md` |
| **Windows (accès WSL)** | `\\wsl.localhost\Ubuntu-22.04\home\lucas\tools\squidResearch\docs\infrastructure\LOG_COMMUN_LPPP_SQUIDRESEARCH.md` |
| **Depuis la racine du dépôt SquidResearch** | `docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md` |

---

## Contenu du log commun (résumé)

- **§ 1** — Adresses (LPPP : 8000, 5678, 3000, 5432, 6379 ; SquidResearch : 8000, 3000, 5679, 3001, 5432, 5555, etc.) et conflits de ports si les deux stacks tournent en même temps.
- **§ 2** — Variables d’environnement (.env LPPP à la racine LPPP ; .env SquidResearch dans `/home/lucas/tools/squidResearch` ; ne pas mélanger).
- **§ 3** — Chemins des deux dépôts ; aucun chemin SquidResearch n’est monté dans le docker-compose LPPP.
- **§ 4** — Fichiers / logs à tenir à jour (côté LPPP et SquidResearch).
- **§ 5** — Avis et recommandations (coexistence, hermeticité).
- **§ 6** — Résumé pour relecture rapide.
- **§ 7** — État des projets Docker (snapshot : projets Compose et conteneurs LPPP vs SquidResearch).

---

## Mise à jour

Dès qu’un port, un chemin ou une décision d’infra change côté LPPP ou SquidResearch, mettre à jour le fichier **canonique** dans SquidResearch (`docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md`). Ce pointeur LPPP peut rester inchangé tant que l’emplacement du log commun ne change pas.

---

*Dernière synchro de ce pointeur : 2026-02-04. Source : dépôt SquidResearch.*
