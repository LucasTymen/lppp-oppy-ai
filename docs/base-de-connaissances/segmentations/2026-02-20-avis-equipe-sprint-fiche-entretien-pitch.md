# Avis à l’équipe — Sprint FicheEntretienPitch

**Date** : 2026-02-20  
**Pilote** : Chef de Projet  
**Statut** : 🟡 Étude (pas de code pour l’instant)  
**Objet** : Nouvelle feature « FicheEntretienPitch » — fiches HTML pures pour préparer les entretiens d’embauche à l’avance.

---

## 1. Décision projet

- **Feature** : FicheEntretienPitch = fiches en **HTML pur** pour la préparation des entretiens.
- **Bases inchangées** : la partie **questions techniques** et **culture générale** reste telle quelle (réutilisable quel que soit le domaine) ; éventuellement **mise à jour / actualisation** uniquement.
- **Style** : on garde **toujours le même style**.
- **Interaction** : tout est **accordéon / drop-down** ; tout contenu est **encapsulé** dedans pour usage pratique et flexible.
- **Consigne immédiate** : **ne rien coder pour l’instant** — uniquement **étudier** la fiche de référence (style, technologie, argumentaire, structure, organisation).
- **Template** : **pas besoin d’en créer un nouveau**. Le projet dispose déjà du **modèle canonique** : `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html`. Chaque nouvelle fiche = copie de ce modèle + **contenu adapté selon la boîte et le poste** (présentation, formalités, questions à poser, bloc entreprise, checklist, lexique). La distinction « fixe vs à adapter » est détaillée dans `fiches-entretien-emploi-modele-et-veille.md` § « Fixe vs à adapter (par boîte et poste) ».

---

## 2. Fiche de référence analysée

**Fichier étudié** : `2511_pitch_Clever-Age_prepa_entretien.html` (Downloads — fourni par l’utilisateur).

### 2.1 Style

| Élément | Détail |
|--------|--------|
| **Fond page** | Dégradé linéaire `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`, `min-height: 100vh` |
| **Conteneur** | Fond blanc, `max-width: 1400px`, `padding: 30px`, `border-radius: 15px`, `box-shadow` |
| **Typo** | `font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif` |
| **Titre** | H1 centré, `color: #333`, `font-size: 2.5em` ; sous-titre centré `#666`, `1.2em` |
| **Info-box** | Bandeau rappel (dégradé violet comme l’accordéon), texte blanc, `border-radius: 10px` |
| **Accordéon principal** | `.accordion` : dégradé violet, texte blanc, `padding: 15px`, `border-radius: 8px`, hover = dégradé inversé + `translateX(5px)` |
| **Sous-accordéon** | `.sub-accordion` : fond `#e9ecef`, texte `#495057`, hover `#dee2e6`, `translateX(3px)` |
| **Panels** | `.panel` : fond `#f8f9fa`, bordure gauche `4px solid #667eea` ; `.sub-panel` : fond blanc, bordure gauche `3px solid #6c757d` |
| **Encadrés sémantiques** | `.highlight` (jaune), `.success` (vert), `.warning` (rouge), `.info` (bleu), `.tip` (bleu clair + préfixe 💡) |
| **Code** | Fond `#f4f4f4`, `Courier New`, couleur `#e83e8c` |
| **Liens** | `color: #667eea`, soulignement au hover |

### 2.2 Technologie

| Composant | Choix |
|-----------|--------|
| **HTML** | HTML5, `lang="fr"`, structure sémantique (titres, listes, paragraphes) |
| **CSS** | Un seul bloc `<style>` dans le `<head>` ; pas de fichier externe |
| **JS** | **jQuery 3.6.0** (CDN) ; script en fin de `<body>` |
| **Interactivité** | Clic sur `.accordion` → `toggleClass('active')` + `$(this).next('.panel').slideToggle()` ; idem pour `.sub-accordion` / `.sub-panel` |
| **UX** | `scroll-behavior: smooth` sur `html` |
| **Dépendances** | Aucune autre lib ; pas de `<details>` / `<summary>` natif (tout en boutons + div) |

### 2.3 Argumentaire

- **Info-box** : rappel rapide (disponibilité, prétentions, localisation, télétravail, type de contrat).
- **Section 0** : présentation (pitch 2 min, version courte 1 min), triple profil (Dev / Growth / Design), coordonnées.
- **Section 1** : formalités (disponibilité, prétentions, géo, type de contrat) avec encadrés success / warning / highlight.
- **Section 2** : programmation — questions techniques (Python, Django, Java, Spring, Angular, etc.) avec Q/R en sous-accordéons, réponses dans `.tip`.
- **Section 3** : questions à poser à l’entreprise.
- **Section 4** : entreprise — ce qu’il faut savoir (valeurs, clients, chiffres, stacks).
- **Section 5** : checklist finale avant entretien.
- **Section 6** : lexique des abréviations.

Ton : professionnel, structuré, chiffré quand pertinent (ex. Parazar +3000€/mois, +40% SEO).

### 2.4 Structure et organisation

| Niveau | Rôle | Classes / rôles |
|--------|------|------------------|
| **Page** | `div.container` unique | Contient tout le contenu |
| **En-tête** | H1 + subtitle + info-box | Identité + rappel rapide |
| **Niveau 1** | Sections métier | `button.accordion` + `div.panel` |
| **Niveau 2** | Sous-thèmes / Q-R | `button.sub-accordion` + `div.sub-panel` |
| **Niveau 3** | Sous-sous (ex. Q1, Q2…) | Parfois `button.sub-accordion` + `div.sub-panel` imbriqués |
| **Contenu** | Blocs de texte / listes | `div.highlight`, `div.success`, `div.warning`, `div.info`, `div.tip`, `ul`, `code` |

**Numérotation des sections** : 0 à 6 avec emoji (👤, 📑, 💻, ❓, 🏢, ✅, 📖). Sous-sections avec emoji (📝, 💪, 📞, 💼, 💰, etc.).

**Règle** : tout le contenu lisible est **à l’intérieur** d’un panel (accordéon ou sous-accordéon) ; rien d’étalé en plein écran hormis le titre, sous-titre et info-box.

---

## 3. Alignement avec l’existant LPPP

| Élément | Dans le projet |
|--------|----------------|
| **Modèle canonique** | `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html` (même structure que la fiche Clever Age analysée) |
| **Doc modèle et veille** | `docs/base-de-connaissances/fiches-entretien-emploi-modele-et-veille.md` (structure, checklist « nouvelle société », veille par onglet) |
| **Organisation** | Un dossier par entreprise ; fiche HTML + ressources + résumé + versions |
| **Rôle** | **Assistant Entretien Emploi** (règle `assistant-entretien-emploi.mdc`) — crée et met à jour les fiches |

La fiche Clever Age (Downloads) est **conforme** au modèle déjà décrit dans la base de connaissances. Les sections « questions techniques » et « culture générale » correspondent à la **section 2 (Programmation)** et aux rappels réutilisables ; elles sont **à ne pas modifier dans leur principe**, uniquement à **actualiser** si besoin.

---

## 4. Consignes pour l’équipe (sprint FicheEntretienPitch)

1. **Ne pas coder** tant que l’étude n’est pas validée et que le périmètre du sprint n’est pas figé.
2. **S’appuyer sur cette analyse** pour toute évolution future (style, technologie, structure).
3. **Ne pas toucher** au contenu des blocs « questions techniques » et « culture générale » comme base réutilisable — uniquement mise à jour / actualisation.
4. **Conserver** : même style visuel, tout en accordéon/drop-down, tout contenu encapsulé dans les panels.
5. **Assistant Entretien Emploi** : continuer à utiliser le modèle canonique et la checklist « nouvelle société » pour toute nouvelle fiche ; la fiche Clever Age (ou sa copie dans le projet) peut servir de **référence de contenu** pour une fiche « pitch » type Clever Age.

---

## 5. Prochaines étapes (à définir avec le Chef de Projet)

- Valider cette étude avec l’utilisateur.
- Décider du périmètre exact du sprint FicheEntretienPitch (nouvelles fiches ? template ? intégration dans un flux ?).
- Ensuite seulement : tâches par agent (Assistant Entretien Emploi, Rédacteur, Designer si besoin, DevOps si déploiement).

---

## 6. Références

- Fiche analysée : `2511_pitch_Clever-Age_prepa_entretien.html` (Downloads)
- Modèle canonique : `docs/ressources-utilisateur/fiches-entretien-emploi/_modele-canonique_prepa_entretien.html`
- Doc fiches entretien : `docs/base-de-connaissances/fiches-entretien-emploi-modele-et-veille.md`
- README fiches : `docs/ressources-utilisateur/fiches-entretien-emploi/README.md`
- Règle Assistant Entretien Emploi : `.cursor/rules/assistant-entretien-emploi.mdc`

---

*Document rédigé pour avis à toute l’équipe — étude de la fiche de référence, pas de code à ce stade.*
