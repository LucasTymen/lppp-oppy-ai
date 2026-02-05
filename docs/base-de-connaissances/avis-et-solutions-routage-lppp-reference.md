# Avis et solutions routage LPPP — Référence

**Objectif** : Référencer le document **AVIS_SOLUTIONS_AGENTS_LPPP_ROUTAGE.md** (dépôt SquidResearch) et résumer les règles applicables côté LPPP pour la stack autonome et l’herméticité.

**Document canonique (SquidResearch)** : `docs/infrastructure/AVIS_SOLUTIONS_AGENTS_LPPP_ROUTAGE.md`  
- WSL : `/home/lucas/tools/squidResearch/docs/infrastructure/AVIS_SOLUTIONS_AGENTS_LPPP_ROUTAGE.md`  
- Windows : `\\wsl.localhost\Ubuntu-22.04\home\lucas\tools\squidResearch\docs\infrastructure\AVIS_SOLUTIONS_AGENTS_LPPP_ROUTAGE.md`

**Pointeur log commun** : `docs/base-de-connaissances/log-commun-lppp-squidresearch.md` (§ 4.2, § 5.3, § 5.4).

---

## Règles applicables (résumé)

- **Stack propre LPPP** (log commun § 5.3) : LPPP utilise **uniquement** sa propre stack : lppp_web, lppp_n8n, lppp_flowise, lppp_db, lppp_redis. Aucune URL / host / port dans le .env ou les configs LPPP ne doit pointer vers SquidResearch (8000, 5679, 3001, 5432, 6379, etc.).
- **Ports LPPP dédiés** : Django 8010, PostgreSQL 5433, Redis 6380, Flowise 3010, n8n 5681 (ou 5678). Deux stacks hermétiques, pouvant tourner en parallèle.
- **Herméticité** (§ 5.4) : Utiliser exclusivement les conteneurs LPPP ; stack LPPP autonome.

---

## Actions par rôle (synthèse, détail dans le doc SquidResearch)

| Rôle | Avis / solutions (référence) |
|------|------------------------------|
| **Chef de Projet** | Valider la règle « stack LPPP autonome + ports LPPP décalés » ; ne pas accepter d’exceptions où LPPP utiliserait n8n/Flowise SquidResearch. |
| **Architecte** | S’appuyer sur le log commun ; grille de ports LPPP (8010, 5433, 6380, 3010, 5681) ; URLs d’embed / webhooks / ALLOWED_HOSTS sur les ports LPPP. |
| **DevOps** | Coexistence sans modifier SquidResearch ; LPPP sur 8010, 5433, 6380, 3010, 5681 ; pas de volume ni .env croisés ; documenter « Docker LPPP = 8010 ». |
| **Pentester** | Aucun credential ni URL LPPP pointant vers SquidResearch ; exposition minimale ; rappeler le risque « mauvais Flowise/n8n » si LPPP pointait vers les services SquidResearch. |

Pour le **détail complet** des avis et solutions : consulter le document canonique dans le dépôt SquidResearch (chemin ci-dessus).

---

## Fichiers LPPP impactés (état actuel)

- **docker-compose.yml** : ports 8010:8000, 5433:5432, 6380:6379, 3010:3000, 5681:5678.
- **.env.example** : commentaire stack autonome ; FLOWISE_URL=http://localhost:3010, N8N_WEBHOOK_URL=http://localhost:5681/.
- **Makefile** : services-urls et health-check sur 8010, 5433, 6380, 3010, 5681.
- **infra-devops.md** § 3.4 : tableau des ports LPPP.
- **pret-a-demarrer.md** : Option B avec DB_PORT=5433, REDIS 6380, FLOWISE_URL 3010.

*Dernière mise à jour : 2026-02-05.*
