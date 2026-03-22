# Organisation : projets et nouveaux dossiers

**Rôle** : Règle projet pour savoir où créer un nouveau dossier (chaque projet à part) et où stocker les éléments communs aux nouveaux projets (templates, modèles).  
**Pilote** : Chef de Projet, Conseiller ; tous les agents appliquent la règle.

---

## 1. Principle : un projet = un dossier à part

**Chaque nouveau projet (nouvelle cible : entreprise, contact, candidature) dispose de son propre dossier.** On ne mélange pas les données de deux projets dans le même dossier.

- **Nouveau contact / prospection / landing** → nouveau dossier dédié.
- **Nouvelle fiche entretien** (nouvelle boîte, nouveau poste) → nouveau dossier dédié.

Les **éléments communs** (modèles, templates, checklists) ne vont **pas** dans un dossier « par projet » : ils restent dans les emplacements partagés (voir § 3).

---

## 2. Où créer le dossier d’un nouveau projet ?

Deux racines existantes, selon le type de projet :

| Type de projet | Emplacement | Registre / référence |
|----------------|-------------|------------------------|
| **Contact / prospection / landing** (rapport SEO, proposition, relance, données prospect) | `docs/contacts/<slug>/` | `docs/contacts/REGISTRE-CONTACTS.md` |
| **Préparation entretien emploi** (fiche HTML par entreprise et poste) | `docs/ressources-utilisateur/fiches-entretien-emploi/<slug_entreprise>/` | README du dossier fiches-entretien-emploi |

- **Slug** : identifiant court, unique, sans espaces ni caractères spéciaux (ex. `clever-age`, `rougier-et-ple`).
- **Même entreprise, deux usages** : une même boîte peut avoir à la fois un dossier **contact** (landing, rapport) et un dossier **fiche entretien** (prep entretien). Ex. Clever Age → `docs/contacts/clever-age/` si prospection, et `docs/ressources-utilisateur/fiches-entretien-emploi/clever-age/` pour la fiche entretien.

**Règle** : dès qu’on commence à travailler sur une **nouvelle** cible (nouvelle société, nouveau poste pour une fiche entretien), on crée le dossier correspondant et on met à jour le registre (REGISTRE-CONTACTS pour les contacts).

---

## 3. Où stocker les éléments « pour les nouveaux projets » ?

Tout ce qui sert à **créer ou préparer** des projets futurs (templates, modèle canonique, checklists, procédures) reste dans des **emplacements partagés** — pas dans un dossier dédié à une seule cible.

| Élément | Emplacement partagé |
|--------|----------------------|
| Modèle canonique fiche entretien | `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html` |
| Doc modèle et veille fiches entretien (fixe vs à adapter, checklist « nouvelle société ») | `docs/base-de-connaissances/fiches-entretien-emploi-modele-et-veille.md` |
| Template rapport complet prospect | `docs/base-de-connaissances/template-rapport-complet-prospect.md` |
| Structure content_json (landing) | `docs/base-de-connaissances/structure-content-json-relance-evenement.md` |
| Règles d’organisation contacts | `docs/base-de-connaissances/organisation-donnees-contacts.md` |
| Registre des contacts (liste des dossiers existants) | `docs/contacts/REGISTRE-CONTACTS.md` |
| Stratégie déploiement (checklist par projet) | `docs/base-de-connaissances/strategie-deploiement-git-vercel.md` |

**En résumé** : les **données et livrables propres à une cible** vont dans le dossier de ce projet ; les **modèles, templates et listes de référence** restent dans la base de connaissances ou les espaces partagés.

---

## 4. Checklist « Nouveau projet »

- [ ] Choisir le **type** (contact/prospection **ou** fiche entretien).
- [ ] Choisir un **slug** unique et stable.
- [ ] Créer le dossier : `docs/contacts/<slug>/` **ou** `docs/ressources-utilisateur/fiches-entretien-emploi/<slug>/`.
- [ ] Mettre à jour le **registre** (REGISTRE-CONTACTS pour les contacts).
- [ ] Partir du **modèle/template** partagé (modèle canonique pour fiches entretien, template rapport ou structure JSON pour contacts) et adapter le contenu à la cible.

---

## Références

- **Contacts** : `organisation-donnees-contacts.md`, `docs/contacts/REGISTRE-CONTACTS.md`
- **Fiches entretien** : `fiches-entretien-emploi-modele-et-veille.md`, `docs/ressources-utilisateur/fiches-entretien-emploi/README.md`
- **Rangement général** : `docs/bonnes-pratiques.md` § 6 (organisation, rien à la racine, un fichier = un rôle clair)

---

*Décision projet : 2026-02-20. Chaque projet dans un nouveau dossier à part ; éléments pour les nouveaux projets dans les emplacements partagés.*
