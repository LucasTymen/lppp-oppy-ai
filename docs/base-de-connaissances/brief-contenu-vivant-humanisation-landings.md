# Brief — Contenu vivant et humanisation (landings)

**Pour** : Rédacteur, Designer (webdesign), Chef de Projet.  
**Objectif** : Rendre le contenu des landings **plus vivant, humain** et **combler les manques** (sections qui semblent vides, transitions absentes, ton trop sec).

**Références** : `bonnes-pratiques.md` (humanisation, image pratique § 2 bis), `strategie-qualite-contenu-landings.md`, `schema-landing-proposition.md`.

---

## 1. Constats (pourquoi ça peut sembler « vide »)

- **Sections sans accroche** : titre + liste ou paragraphe seul, sans phrase d’introduction ou de transition.
- **Hero trop compact** : intro + icebreaker fusionnés en un bloc unique ; pas de phrase de contexte narrative (type « positionnement » P4S).
- **Enjeux** : liste à puces sans lead-in (« Pour vous, j’ai identifié trois points… »).
- **Pas de lien rapport** : quand une étude (PESTEL, SWOT, Porter) ou un rapport complet existe pour le contact, `rapport_url` vide = opportunité manquée de montrer du concret.
- **Rythme visuel** : blocs uniformes (titre + texte) sans respiration ni mise en avant (citation, encadré).

---

## 2. Mission Rédacteur

### 2.1 Champs à renseigner pour « combler les manques »

| Champ | Usage | Exemple |
|-------|--------|--------|
| **positionnement** | Paragraphe narratif (contexte, angle, « pourquoi je vous contacte »). À afficher après le hero ou avant les enjeux. Déjà utilisé sur P4S. | « J’ai une idée précise de ce qu’Ackuracy apporte côté Red Team. Voici où je peux vous être utile : prospection RSSI automatisée, rapport SEO déjà prêt. » |
| **enjeux_lead** | Une phrase d’introduction avant la liste des pain points. Optionnel dans le JSON ; si présent, le template l’affiche au-dessus de la liste. | « Pour Ackuracy, j’ai identifié trois enjeux côté prospection : » |
| **rapport_url** | Dès qu’un rapport ou une étude (PESTEL/SWOT/Porter) existe pour le contact, renseigner l’URL (page exportée, Google Doc, ou `/rapport.html` en standalone). | `rapport.html` ou URL du rapport complet. |
| **coordonnees_intro** | Phrase au-dessus des coordonnées (optionnel). Déjà en dur dans certains templates ; peut être dynamique. | « Pour échanger ou voir le prototype : » |

### 2.2 Ton et humanisation

- **Varier les longueurs** : alterner phrase courte et phrase un peu plus longue ; éviter tous les paragraphes de la même taille.
- **Transitions** : une phrase de liaison entre deux sections quand ça sonne naturel (ex. « Concrètement, voici ce que je propose. » avant les prestations).
- **« Vous » et contexte** : garder le prénom / la société ; reformuler les listes en une phrase narrative quand c’est possible (ex. un pain point = une phrase en « vous »).
- **Mission flash / CTA** : ton direct, invitant, sans jargon (« Je te montre le prototype quand tu veux » plutôt que « N’hésitez pas à solliciter une démonstration »).
- **Pas de remplissage** : chaque ajout doit apporter une info ou une intention claire (voir `bonnes-pratiques.md` § 2).

### 2.3 Où déposer les contenus

- **JSON par contact** : `docs/contacts/<slug>/landing-proposition-<prénom>.json`.
- **Nouveaux champs optionnels** : `positionnement`, `enjeux_lead`, `coordonnees_intro` — les ajouter au JSON quand pertinent ; le Designer / Dev s’assure que les templates (Django et Next.js) les affichent s’ils sont présents.

---

## 3. Mission Designer (webdesign)

### 3.1 Rythme et respiration

- **Section lead** : si le contenu fournit `enjeux_lead` ou un sous-titre de section, l’afficher visuellement (petit texte au-dessus du titre, ou en italique sous le titre) pour casser la monotonie titre → bloc.
- **Bloc « Why Growth Engineer »** : le traiter en **citation / callout** (bordure gauche, fond légèrement différencié, ou guillemets) pour lui donner du poids sans ajouter de texte.
- **Espacement** : vérifier que les sections ne sont pas trop serrées ; une marge ou padding cohérent évite l’impression de « mur de texte ».

### 3.2 Hiérarchie et lisibilité

- **Hero** : si `intro` et `icebreaker` sont longs, envisager deux lignes ou paragraphes distincts (intro courte + icebreaker en dessous) au lieu d’un seul bloc.
- **Listes** : garder un espacement entre les items (space-y) pour que la liste ne ressemble pas à un bloc compact.
- **CTA** : contraste et taille suffisants ; libellé lisible (voir brief copywriting CTA si besoin).

### 3.3 Templates concernés

- **Django** : `templates/landing_pages/proposition.html` (sections 01–07, icebreaker, coordonnées).
- **Next.js standalone** : `deploy/standalone-ackuracy/src/app/page.tsx` (et futurs standalones) — afficher `positionnement`, `enjeux_lead` quand présents dans le JSON.

---

## 4. Coordination

- **Chef de Projet** : valider que chaque landing visée (P4S, Ackuracy, prochaines) a bien un contenu « vivant » (checklist § 5).
- **Rédacteur** : remplir les champs optionnels (positionnement, enjeux_lead, rapport_url) par contact et déposer les JSON à jour.
- **Designer** : adapter les templates pour afficher les nouveaux champs et appliquer les principes visuels (callout, lead-in, respiration).

---

## 5. Checklist « contenu vivant » (avant livraison)

- [ ] **Positionnement** : si la landing cible un décideur après un événement / un échange, un paragraphe `positionnement` (narratif) est présent et affiché.
- [ ] **Enjeux** : liste des pain points avec, si possible, une phrase `enjeux_lead` au-dessus.
- [ ] **Rapport** : si une étude (PESTEL/SWOT/Porter) ou un rapport complet existe pour le contact, `rapport_url` est renseigné et le lien « Consulter le rapport » visible.
- [ ] **Ton** : phrases variées, transitions naturelles, pas de mur de listes sans contexte.
- [ ] **Visuel** : bloc « Why Growth Engineer » mis en avant (callout/citation) ; sections aérées.

---

## 6. Fichiers à aligner

| Fichier | Action |
|---------|--------|
| `schema-landing-proposition.md` | Documenter les champs optionnels `enjeux_lead`, `coordonnees_intro` (si pas déjà présents). |
| `docs/contacts/<slug>/landing-proposition-*.json` | Rédacteur : ajouter positionnement, enjeux_lead, rapport_url selon le contact. |
| `templates/landing_pages/proposition.html` | Designer : afficher enjeux_lead au-dessus de la liste enjeux ; callout pour why_growth_engineer. |
| `deploy/standalone-ackuracy/src/app/page.tsx` | Afficher positionnement (après hero), enjeux_lead (au-dessus de la liste), style callout pour why_growth_engineer. |

---

*Brief créé pour rendre les landings plus vivantes et humaines, en coordination Rédacteur / Designer. Dernière mise à jour : 2025-01-30.*
