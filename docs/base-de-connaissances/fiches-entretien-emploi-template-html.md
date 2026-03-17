# Fiches entretien emploi — Template HTML à appliquer à chaque fois

**Objectif** : Règles de structure HTML à respecter pour toute fiche de préparation à l’entretien. À appliquer systématiquement lors de la création ou de la mise à jour d’une fiche.

**Référence complète** : `fiches-entretien-emploi-modele-et-veille.md` (modèle canonique, contenu, enrichissements). Ce document ne décrit que la **structure et le comportement** à la racine.

---

## 1. Sections à la racine

Les **sections principales** sont des **blocs au même niveau** (racine du contenu). Aucune section ne doit être imbriquée dans une autre.

Structure attendue :

| Niveau racine | Section |
|---------------|---------|
| **0** | Votre présentation |
| **1** | Formalités administratives |
| **2** | Programmation — Questions techniques (contient en son sein : Python, Django, Java, Spring, Angular, concepts, Growth/KPI, Frameworks, **SEO**, **Cybersécurité**) |
| **3** | Questions à poser [à l’entreprise] |
| **4** | [Nom entreprise] — Ce que vous devez savoir |
| **5** | Checklist finale avant entretien |
| **6** | Lexique des abréviations |

**Règle impérative** : Chaque section = un `<button class="accordion">` suivi d’un `<div class="panel">`. Le **panel de la section 2 doit être fermé** par un `</div>` **avant** le commentaire et le bouton de la section 3. Les sections 3, 4, 5 et 6 sont donc bien **au même niveau racine** que 0, 1 et 2 (pas à l’intérieur du panel de la section 2).

---

## 2. Accordéons fermés par défaut

À l’ouverture de la page, **tous les accordéons sont fermés**.

- Ne pas ajouter la classe `active` sur les boutons `.accordion`.
- Ne pas ajouter `style="display: block;"` sur les `.panel`.

L’utilisateur ouvre les sections au clic. Aucune section n’est affichée par défaut.

---

## 3. Récapitulatif à vérifier

- [ ] Les 7 sections (0 à 6) sont au même niveau (pas d’imbrication section 3–6 dans section 2).
- [ ] Un seul `</div>` ferme le panel de la section 2 avant la section 3.
- [ ] Aucun accordéon n’a `active` ni `display: block` au chargement.
- [ ] SEO et Cybersécurité sont **dans** la section 2 (sous-accordéons ou onglets), pas à la racine.

---

*Référence : fiches-entretien-emploi-modele-et-veille.md ; fiche de référence : Opportunity GAM (prepa_entretien_OPPORTUNITY_GAM.html).*
