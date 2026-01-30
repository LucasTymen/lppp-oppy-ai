# Formules et algorithmes de référence — LPPP

**Rôle** : Spec canonique pour l’implémentation du **scoring**, de la **qualité des données** et du **matching**. Les agents **Data Analyst** (logique métier et algorithmes) et **Dev Django** s’en inspirent pour implémenter sans réinventer ; toute évolution de formule passe par ce document puis par `intelligence-metier-algorithmes.md` et le code.

**Objectifs** : Fiabilité et performance du système ; base solide et allègement des agents (une seule source de vérité pour les formules).

**Pilotes** : Data Analyst (rédaction et maintenance des formules), Chef de Projet (validation). Référence croisée : `intelligence-metier-algorithmes.md` (où brancher, stratégie d’implantation).

---

## 1. Conventions

- **Plage score prospect** : \( [0, 100] \) (entier ou float selon usage).
- **Complétude enriched** : \( \text{enriched\_completeness} \in [0, 1] \) (float).
- **Variables booléennes** : utilisées comme 0/1 dans les expressions quand besoin (ex. `has_email`).

---

## 2. Scoring prospect

### 2.1 Sous-scores (entrées du calcul)

| Variable | Définition | Domaine |
|----------|------------|--------|
| \( \text{email\_score} \) | 40 si email valide, 0 sinon | \( \{0, 40\} \) |
| \( \text{company\_score} \) | 30 si company_name non vide (après normalisation), 0 sinon | \( \{0, 30\} \) |
| \( \text{contact\_score} \) | 20 si contact_name non vide (après normalisation), 0 sinon | \( \{0, 20\} \) |
| \( \text{enriched\_score} \) | \( \min(10, \max(0, \text{enriched\_completeness} \times 10)) \) | \( [0, 10] \) |

**Total brut max** : \( 40 + 30 + 20 + 10 = 100 \).

### 2.2 Formule par défaut

\[
\text{score} = \min\bigl(100, \operatorname{round}(\text{email\_score} + \text{company\_score} + \text{contact\_score} + \text{enriched\_score})\bigr)
\]

- **Implémentation** : expression sécurisée `safe_eval` avec contexte `email_score`, `company_score`, `contact_score`, `enriched_score` (et optionnellement `has_email`, `has_company`, `has_contact` en 0/1).
- **Config** : formule surchargeable (ex. via `DEFAULT_SCORE_EXPRESSION` ou config Django) pour rester dans les opérateurs/fonctions autorisés (`+`, `-`, `*`, `/`, `min`, `max`, `round`, `abs`).

### 2.3 Seuils d’usage (recommandations)

| Seuil | Usage typique |
|-------|----------------|
| \( \text{score} \geq 80 \) | Message très personnalisé, priorité haute |
| \( 50 \leq \text{score} < 80 \) | Message adapté, priorité normale |
| \( \text{score} < 50 \) | Message générique ou relance qualité |

---

## 3. Complétude prospect (`prospect_completeness`)

### 3.1 Sortie (dictionnaire)

Fonction qui retourne des **indicateurs** utilisés par le scoring et les rapports qualité :

| Clé | Type | Définition |
|-----|------|------------|
| `has_email` | bool | Email valide (regex § 4.1) |
| `has_company` | bool | Company name non vide après normalisation |
| `has_contact` | bool | Contact name non vide après normalisation |
| `enriched_completeness` | float | \( 0.5 \cdot \mathbb{1}_{\text{"company"} \in \text{enriched}} + 0.5 \cdot \mathbb{1}_{\text{"contact"} \in \text{enriched}} \) ⇒ \( \in \{0, 0.5, 1.0\} \) |
| `company_normalized` | str | Nom d’entreprise normalisé (§ 4.2) |
| `contact_normalized` | str | Nom de contact normalisé (§ 4.3) |

### 3.2 Lien avec le score

Les champs `has_email`, `has_company`, `has_contact`, `enriched_completeness` sont les **entrées** de `score_prospect()` (§ 2).

---

## 4. Qualité et normalisation

### 4.1 Email valide

- **Fonction** : `is_valid_email(value)`.
- **Règle** : chaîne non vide, trim, puis match regex (voir `apps.intelligence.quality.EMAIL_REGEX`) :
  - Pattern : `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

### 4.2 Normalisation nom d’entreprise

- **Fonction** : `normalize_company_name(name)`.
- **Étapes** : trim → NFD (décomposition Unicode) → suppression des caractères de catégorie Mn (accents). Pas de lowercase imposé dans la spec (implémentation actuelle : sans lower pour rester conservative).

### 4.3 Normalisation nom de contact

- **Fonction** : `normalize_contact_name(name)`.
- **Étapes** : trim → collapse des espaces multiples en un seul espace.

---

## 5. Matching prospect ↔ landing

### 5.1 Score d’un prospect (pour affichage / tri)

\[
\text{get\_prospect\_score}(\text{prospect}) = \text{score\_prospect}(\ldots)
\]

avec les arguments dérivés de `prospect_completeness(company_name, contact_name, email, enriched_data)`.

### 5.2 Meilleure landing pour un prospect (`best_landing_for_prospect`)

**Entrées** : `prospect`, `candidates` (liste optionnelle de `LandingPage`).

**Algorithme** :

1. Si le prospect a déjà une landing liée (`prospect.landing_page_id` renseigné) → retourner `prospect.landing_page`.
2. Sinon, si `candidates` est vide ou None → retourner `None`.
3. Sinon : parcourir `candidates` dans l’ordre ; retourner la **première** landing avec `is_published == True` ; si aucune, retourner la première de la liste.

*Extension future* : critères supplémentaires (template_key, score minimal, campagne) pourront être ajoutés dans ce document puis implémentés sans changer la signature tant que possible.

### 5.3 Correspondance prospect ↔ landing (`prospect_matches_landing`)

**Entrées** : `prospect_company`, `prospect_contact`, `landing_prospect_company`, `landing_prospect_name`.

**Règle** : après normalisation (§ 4.2, § 4.3) :

- `company_ok` : True si les deux company sont vides ou si égales après normalisation.
- `contact_ok` : True si les deux contact sont vides ou si égaux après normalisation.

Retour : `company_ok ∧ contact_ok`.

---

## 6. Expressions sécurisées (`safe_eval`)

Pour les formules configurables (ex. score) :

- **Opérateurs autorisés** : `+`, `-`, `*`, `/`, `%`, `**`.
- **Fonctions autorisées** : `abs`, `round`, `min`, `max`.
- **Variables** : fournies dans le contexte (pas d’accès arbitraire au scope).
- **Constantes** : nombres uniquement.

Toute nouvelle variable ou fonction ajoutée au contexte doit être documentée ici et dans `intelligence-metier-algorithmes.md`.

---

## 7. Références et mise à jour

- **Implémentation** : `apps.intelligence` (scoring, quality, matching).
- **Où c’est utilisé** : `intelligence-metier-algorithmes.md` (§ 2, 3).
- **Décisions de conception** : `decisions.md` en cas de changement de formule ou de stratégie.
- **Pilotes** : Data Analyst (logique métier et algorithmes), Chef de Projet (validation). En cas de désaccord ou d’évolution majeure, escalade au Chef de Projet puis à l’Orchestrateur si besoin (voir `coordination-agents.mdc`).

---

*Document créé pour fiabiliser le système et alléger les agents (source unique de vérité pour les formules). Dernière mise à jour : 2025-01-30.*
