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

- **§ 1** — Adresses et conflits de ports ; référence au doc **AVIS_SOLUTIONS_AGENTS_LPPP_ROUTAGE.md** (voir § 4.2).
- **§ 2** — Variables d’environnement (.env LPPP à la racine LPPP ; .env SquidResearch dans `/home/lucas/tools/squidResearch` ; ne pas mélanger).
- **§ 3** — Chemins des deux dépôts ; aucun chemin SquidResearch n’est monté dans le docker-compose LPPP.
- **§ 4** — Fichiers / logs à tenir à jour (côté LPPP et SquidResearch) ; **§ 4.2** référence **AVIS_SOLUTIONS_AGENTS_LPPP_ROUTAGE.md** (avis et solutions par rôle).
- **§ 5** — Avis et recommandations. **§ 5.3 Stack propre LPPP** : LPPP doit utiliser uniquement sa propre stack (lppp_web, lppp_n8n, lppp_flowise, lppp_db, lppp_redis). Aucune URL/host/port dans le .env ou les configs LPPP ne doit pointer vers SquidResearch (8000, 5679, 3001, etc.). Ports LPPP dédiés : 8010, 5433, 6380, 3010, 5678/5681. **§ 5.4 Herméticité** : utiliser exclusivement lppp_web, lppp_n8n, lppp_flowise, lppp_db, lppp_redis ; stack LPPP autonome. **§ 5.5** — Compléments.
- **§ 6** — Résumé pour relecture rapide.
- **§ 7** — État des projets Docker (snapshot : projets Compose et conteneurs LPPP vs SquidResearch).

---

## Mise à jour

Dès qu’un port, un chemin ou une décision d’infra change côté LPPP ou SquidResearch, mettre à jour le fichier **canonique** dans SquidResearch (`docs/infrastructure/LOG_COMMUN_LPPP_SQUIDRESEARCH.md`). Ce pointeur LPPP peut rester inchangé tant que l’emplacement du log commun ne change pas.

---

## Document Avis / Solutions (SquidResearch)

Dans le dépôt SquidResearch : **`docs/infrastructure/AVIS_SOLUTIONS_AGENTS_LPPP_ROUTAGE.md`** — synthèse retours LPPP (sprint urgent, étude d’impact) et avis/solutions par rôle (Chef de Projet, Architecte, DevOps, Pentester). Les agents LPPP s’y réfèrent pour le détail des actions et des risques.

---

*Dernière synchro de ce pointeur : 2026-02-05. Source : dépôt SquidResearch (log commun § 5.3, § 5.4, AVIS_SOLUTIONS).*
