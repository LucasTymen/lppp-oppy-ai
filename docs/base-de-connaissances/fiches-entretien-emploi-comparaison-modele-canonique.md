# Fiches entretien — Comparaison modèle donné vs modèle canonique HTML

**Objectif** : Identifier ce qui **manque** dans le fichier `_modele-canonique_prepa_entretien.html` par rapport au modèle de référence (fiche Clever Age) et aux décisions d’enrichissement (cours et révisions, notions principales).

**Règle projet** : Le modèle que l’utilisateur a donné est la **structure de référence**. Toute fiche doit avoir **la même organisation, la même structure, le même nombre d’onglets**. Le **contenu**, lui, change et s’adapte dynamiquement (par boîte, par poste). Voir `fiches-entretien-emploi-modele-et-veille.md` § 1 « Règle centrale ».

---

## 1. Ce qui est déjà dans le modèle canonique HTML

- **Structure 0 → 6** : Présentation, Formalités, Programmation (tests techniques), Questions à poser, [Entreprise] Ce que vous devez savoir, Checklist finale, Lexique.
- **Section 2 (Programmation — Tests techniques)** avec sous-accordéons au format **cours et révisions** (Q/R avec Définition, Exemple, Cas d’usage dans `.tip`) :
  - **Python** (Q1–Q14)
  - **Django** (Q1–Q7+)
  - **Java** (questions courantes)
  - **Spring** (questions courantes)
  - **Angular** (questions courantes)
  - **Growth & Marketing** (AARRR, Build-Measure-Learn, North Star Metric, Growth Loops, ICE Score, etc.)
- **Lexique** (section 6) : Growth & Marketing, Performance Web, Technologies & Frameworks, Sécurité & Conformité.
- **Info-box**, styles, script accordéons : conformes au modèle donné.

---

## 2. Ce qui manque dans le modèle canonique HTML

Les blocs suivants sont **documentés** dans `fiches-entretien-emploi-modele-et-veille.md` (§ 6) comme à inclure en **cours et révisions** (notions principales), mais ils **ne sont pas encore** dans le fichier HTML. Il faut les **ajouter** en section 2 (Programmation / Tests techniques), au **même format** que Python ou Django (sous-accordéon « MODULE – Questions Courantes » avec Q/R en `.tip`).

| Module | Référence doc | Statut dans le HTML |
|--------|----------------|----------------------|
| **IoT** | § 6.4 | ❌ Manquant |
| **CSS** | § 6.7 | ❌ Manquant |
| **Cybersécurité** | § 6.3 | ❌ Manquant (bloc dédié type cours ; le lexique « Sécurité » existe en section 6 mais pas un module Q/R en section 2) |
| **Maintenance informatique N2** | § 6.1 | ❌ Manquant |
| **DevOps** (Git, GitLab CI/CD, GitHub Actions, Docker, WordPress) | § 6.6 | ❌ Manquant (une Q « Quels outils DevOps » existe en section 4 entreprise, mais pas de module cours/révisions en section 2) |
| **SQL** | § 6.8 | ❌ Manquant |
| **PostgreSQL** | § 6.9 | ❌ Manquant |
| **Ruby / Ruby on Rails** | § 6.5 | ❌ Manquant (optionnel) |

---

## 3. Règle pour compléter le modèle

- **Ne rien supprimer** : tout le contenu existant (Python, Django, Java, Spring, Angular, Growth, etc.) reste.
- **Ajouter** les modules manquants en **section 2** (après les blocs existants), au **même format** :
  - Un `<button class="sub-accordion">[emoji] NOM MODULE - Questions Courantes</button>` (ou « Notions principales »)
  - Un `<div class="sub-panel">` contenant des Q1, Q2, … avec `<div class="tip">` et **Définition**, **Exemple**, **Cas d’usage** (ou équivalent).
- Contenu de chaque module : voir les § 6.1, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9 de `fiches-entretien-emploi-modele-et-veille.md`.

---

## 4. Résumé

**Modèle donné** (fiche de référence Clever Age + décisions projet) = structure 0→6 + tests techniques **repris tels quels** + **enrichissement** (IoT, CSS, Cybersécurité, Maintenance N2, DevOps, SQL, PostgreSQL, éventuellement Ruby/Rails) au format **cours et révisions**.

**Modèle canonique HTML actuel** = structure 0→6 + Python, Django, Java, Spring, Angular, Growth déjà présents. **Il manque** les 7 (ou 8) modules d’enrichissement listés ci-dessus, à ajouter en section 2 au même format que Python/Django.

---

*Référence : fiches-entretien-emploi-modele-et-veille.md, _modele-canonique_prepa_entretien.html*
