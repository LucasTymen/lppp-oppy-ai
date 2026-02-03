# Classification des landings — secteur et catégorie

**Rôle** : Proposition pour classer les landing pages par **secteur** et **catégorie**, afin d’utiliser le projet naturellement et de voir les rendus par type.  
**Pilotes** : Chef de Projet, Dev Django, Designer.  
**Référence** : `fonction-premiere-et-segments-prospection.md`, modèle `LandingPage`.

---

## 1. Objectif

- **Voir les rendus** des landings facilement (liste, filtres).
- **Classer** les landings par **secteur** (ex. Cybersécurité, Juridique, Industrie) et par **catégorie** (ex. Relance événement, Proposition, Lead magnet).
- Rendre le projet **utilisable au quotidien** : une page « Galerie / Liste des landings » avec filtres secteur + catégorie.

---

## 2. Proposition : secteurs

Secteur = domaine ou type de prospect ciblé.

| Valeur (exemple) | Description |
|------------------|-------------|
| `cybersecurite` | Cybersécurité, OT/IT (ex. P4S-archi) |
| `juridique` | Cabinets avocats, ART, juridique |
| `industrie` | Industrie, manufacturing |
| `low-tech` | Boîtes low tech, sans tech |
| `autre` | Non classé ou autre segment |

**Implémentation** : liste prédéfinie (choices) ou modèle `Sector` (nom, slug). Pour rester simple au début : champ `sector` (CharField avec choices).

---

## 3. Proposition : catégories

Catégorie = type d’offre / d’angle de la landing.

| Valeur (exemple) | Description |
|------------------|-------------|
| `relance-evenement` | Relance après salon / événement |
| `proposition` | Proposition de mission (ex. Growth Engineer pour P4S) |
| `lead-magnet` | Lead magnet, contenu à télécharger |
| `lowtech` | Boîtes low tech / sans tech (prospection commando) |
| `autre` | Autre |

**Implémentation** : champ `category` (CharField avec choices), aligné avec les `template_key` existants (relance-evenement, default, etc.) si besoin.

---

## 4. Modèle (évolution)

Ajout sur `LandingPage` (ou équivalent) :

- `sector` : CharField avec choices (ou FK vers modèle Sector).
- `category` : CharField avec choices (ou FK vers modèle Category).

Migration Django après ajout des champs. Valeurs par défaut `autre` pour les landings existantes.

---

## 5. Rendu : liste avec filtres

- **Backend** : Vue (Django ou API) listant les landings avec filtres optionnels `?sector=cybersecurite&category=relance-evenement`.
- **Frontend** :
  - **Django** : page `/landings/` avec formulaire ou liens de filtre (secteur, catégorie), cartes ou tableau avec lien vers chaque rendu (`/p/<slug>/`).
  - **Next.js** : page « Galerie » ou « Liste des landings » avec filtres (dropdown ou chips) et cartes cliquables vers `/p/<slug>` ou équivalent.

Cela permet de **parcourir les rendus par secteur et par catégorie** sans passer uniquement par l’admin.

---

## 6. Avis synthétique

- **Oui, c’est pertinent** pour un usage naturel : tu ouvres une page « Landings », tu filtres par secteur (ex. Cybersécurité) ou par catégorie (ex. Relance événement), et tu cliques sur une carte pour voir le rendu.
- **Ordre recommandé** :  
  1) Faire **redémarrer le projet** (voir `demarrage-projet-equipe-tech.md`).  
  2) Ajouter **secteur** et **catégorie** au modèle + migration.  
  3) Exposer une **liste avec filtres** (Django puis/ou Next.js) et les liens vers les pages de rendu.

---

## 7. Références

- **Démarrage** : `demarrage-projet-equipe-tech.md`
- **Segments** : `fonction-premiere-et-segments-prospection.md`
- **Modèle** : `apps/landing_pages/models.py`
- **Stack frontend** : `stack-frontend-nextjs-react.md`

---

*Document créé pour l’équipe technique et le Chef de Projet. Dernière mise à jour : 2025-01-30.*
