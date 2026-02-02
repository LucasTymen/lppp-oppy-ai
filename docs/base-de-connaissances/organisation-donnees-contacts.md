# Organisation des données par contact

**Rôle** : Règle projet pour éviter de mélanger les données d’un contact avec un autre.  
**Pilote** : Tous les agents qui manipulent des données liées à un contact (prospect) ; le Conseiller et le Chef de Projet veillent au respect de la règle.

---

## Règle : un contact = un dossier

**Chaque contact (prospect) dispose de son propre dossier** pour y ranger toutes les données le concernant quand il y a besoin :

- Contenus de landing (`content_json`, brouillons)
- Notes, compte-rendu d’échange, relances
- Rapport SEO prospect (synthèse, pas les CSV bruts)
- Fichiers annexes (exports, pièces) liés à ce contact

Cela évite de mélanger les données entre contacts et de s’y perdre.

---

## Emplacement et convention

- **Racine** : `docs/contacts/`
- **Un dossier par contact** : `docs/contacts/<slug_contact>/`
- **Slug** : identifiant court, lisible, sans espaces ni caractères spéciaux. Exemples :
  - `societe-dupont_jean` (entreprise_nom)
  - `cabinet-martin_relance-salon-2025`
  - `contact_<id>` si vous utilisez un identifiant métier

Nommage libre tant qu’il est **unique** et **stable** pour ce contact.

---

## Contenu type d’un dossier contact

| Fichier / dossier | Usage (optionnel) |
|-------------------|--------------------|
| `content_json.json` ou `landing-relance.json` | Contenu de landing pour ce contact (hero, CTA, etc.) |
| `notes.md` | Notes, CR d’échanges, relances |
| `rapport-complet-<slug>.md` | **Rapport complet** : fiche société + concurrence + PESTEL/SWOT/Porter + rapport SEO. Utiliser le **template** `docs/base-de-connaissances/template-rapport-complet-prospect.md` (copier dans le dossier contact, renommer, remplir). Uniforme pour toutes les entreprises démarchées. |
| `etude-concurrentielle-pestel-swot-porter.md` | Étude détaillée société, produits, concurrence, PESTEL, SWOT, Porter (peut alimenter le rapport complet). |
| `rapport-seo.md` | Synthèse rapport SEO seul (voir `rapport-seo-prospect.md`) si pas de rapport complet. |
| `pieces/` | Fichiers annexes (exports, docs) pour ce contact uniquement |

Aucun fichier obligatoire : on crée ce dont on a besoin.

---

## Qui fait quoi

- **Création d’un nouveau dossier contact** : dès qu’un nouveau contact est suivi (relance salon, prospection), créer `docs/contacts/<slug_contact>/` et y ranger les données.
- **Conseiller / Chef de Projet** : rappeler la règle et vérifier que les segmentations et le REGISTRE-CONTACTS pointent vers les bons dossiers.
- **Rédacteur** : déposer les `content_json` et textes par contact dans le dossier du contact.
- **Expert SEO** : déposer la synthèse rapport SEO dans le dossier du contact.
- **Growth / Pentester** : données enrichies (fiche data prospect) peuvent être référencées ou déposées dans le dossier contact si besoin.

---

## Registre des dossiers contacts

Un fichier **`docs/contacts/REGISTRE-CONTACTS.md`** liste les contacts ayant un dossier, avec slug et usage éventuel. À mettre à jour à chaque création de dossier contact.

---

## Références

- **Template rapport complet** (fiche + stratégie + SEO, uniforme par entreprise) : `docs/base-de-connaissances/template-rapport-complet-prospect.md`
- **Rapport SEO prospect** : `docs/base-de-connaissances/rapport-seo-prospect.md`
- **Structure content_json** : `docs/base-de-connaissances/structure-content-json-relance-evenement.md`
- **Ressources utilisateur** (CV, segments) : `docs/ressources-utilisateur/REGISTRE-RESSOURCES.md`

---

*Décision projet : 2025-01-30. Un contact = un dossier pour éviter de s’y mêler les pinceaux.*
