# Rangement projet, landing pages et ressources

**Date** : 2026-01-30  
**Chef de Projet** : pilote (Accountable)  
**Statut** : 🟡 En cours

**Avis équipe** : `docs/base-de-connaissances/avis-equipe-rangement-projet-landings-ressources.md`

---

## Objectif

Ranger le projet, les landing pages et les ressources en appliquant les bonnes pratiques (§ 5 et 6) et les règles d’organisation (contacts, ressources utilisateur). Chaque rôle contribue dans son périmètre.

---

## Tâches par rôle

### Chef de Projet
- [ ] Valider le périmètre et les priorités de rangement avec l’utilisateur si besoin.
- [ ] S’assurer que l’avis est connu (référence dans TODO, registre, logs).
- [ ] Clôturer la tâche quand la checklist globale est satisfaisante (pas de validation formelle obligatoire ; rangement continu).

### Orchestrateur
- [ ] Rappeler la stratégie rangement/organisation si un agent crée des fichiers hors cadre.
- [ ] Vérifier que le registre et les docs de référence sont à jour (contacts, ressources).

### Dev Django
- [ ] Racine : aucun script ou fichier temporaire laissé ; code métier dans `apps/`.
- [ ] Landings : cohérence modèles / vues / templates avec les dossiers `docs/contacts/<slug>/` et `deploy/` (sources de contenu, URLs).

### Designer
- [ ] Templates dans `templates/` ; pas de fichiers orphelins à la racine ou dans docs sans usage.
- [ ] Landings : assets et styles rangés ; références chartes/contacts à jour.

### DevOps
- [ ] Racine et docker/ : uniquement les fichiers prévus ; pas de scripts temporaires ; scripts utiles dans `scripts/` documenté ou Makefile.
- [ ] Deploy : chaque projet dans `deploy/<projet>/` avec structure claire ; pas de doublons ni de dossiers morts sans README.

### Rédacteur / Conseiller
- [ ] Ressources utilisateur : tout contenu reçu dans `docs/ressources-utilisateur/` avec entrée dans `REGISTRE-RESSOURCES.md`.
- [ ] Contacts : un contact = un dossier ; contenu (landing, notes, rapport) dans `docs/contacts/<slug>/` ; `REGISTRE-CONTACTS.md` à jour.

### Growth / Data Analyst / Expert SEO
- [ ] Fichiers générés (rapports, CSV, études) rangés dans le dossier contact concerné ou `docs/contacts/<slug>/` ; pas de fichiers à la racine ni dans docs sans lien clair.

### Automatizer
- [ ] Workflows exportés et déposés dans `docs/n8n-workflows/`, `docs/flowise-workflows/` selon la règle de sauvegarde ; pas de copies temporaires laissées.

### Tous les agents
- [ ] En fin de session : supprimer fichiers de test, debug, one-shot ; ne rien créer « au cas où » ; un fichier = un rôle clair (bonnes pratiques § 5 et 6).

---

## Checklist globale (rappel)

| Zone | Règle |
|------|--------|
| Racine | Seulement README, Makefile, manage.py, docker-compose, requirements, .env.example, .gitignore + dossiers apps/, lppp/, docs/, docker/, templates/, .cursor/. |
| Landings / contacts | Un contact = `docs/contacts/<slug>/` ; REGISTRE-CONTACTS à jour. |
| Ressources | `docs/ressources-utilisateur/` + REGISTRE-RESSOURCES à jour. |
| Deploy | Un projet = `deploy/<projet>/` ; structure lisible, pas de doublons inutiles. |
| Docs | Tout dans `docs/` (base-de-connaissances, logs, segmentations, contacts) ; pas de .md à la racine. |

---

## Références

- **Bonnes pratiques** : `docs/bonnes-pratiques.md` § 5 et 6.
- **Organisation contacts** : `docs/base-de-connaissances/organisation-donnees-contacts.md`.
- **Registre contacts** : `docs/contacts/REGISTRE-CONTACTS.md`.
- **Ressources** : `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md`.
- **Pilotage** : `.cursor/rules/pilotage-agents.mdc` (rangement, nettoyage, organisation).

---

*Document maintenu par le Chef de Projet. Dernière mise à jour : 2026-01-30.*
