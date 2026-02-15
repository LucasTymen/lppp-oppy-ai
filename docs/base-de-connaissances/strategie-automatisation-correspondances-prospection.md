# Stratégie — Automatiser les correspondances (cibles ↔ audits SEO ↔ prospects)

**Objectif** : À partir de la base JSON des sociétés low-tech / sous-digitalisées, enchaîner de façon structurée : **audits SEO** → **identification de prospects** → **correspondance** entre le besoin de l’entreprise et la preuve de valeur proposée (rapport SEO, scraping, tracking, etc.), sans perdre d’informations.

**Pilotes** : Toi (audits SEO, prospection) ; **Expert SEO** (rapports) ; **Growth** (analyse, priorisation) ; **Automatizer** (scripts / liste de suivi si besoin). **Chef de Projet** valide le flux.

**Références** : `docs/ressources-utilisateur/textes/2026-01-30_prospection-commando-lowtech.json`, `organisation-donnees-contacts.md`, `rapport-seo-prospect.md`, `README-prospection-lowtech.md`.

---

## 1. Principe des correspondances

Une **correspondance** = lier pour chaque **entreprise cible** :

| Élément | Source | Usage |
|--------|--------|--------|
| **Cible** | `entreprises_ciblees[]` (nom, besoin, priorite, segment, mode_ciblage_principal) | Qui on cible |
| **Preuve de valeur** | `plan_action_proof_of_value.preuves_recommandees` + besoin | Ce qu’on propose en premier (audit SEO, scraping, tracking, automation) |
| **Prospect(s)** | Décideurs / contacts trouvés (audit, LinkedIn, OSINT) | À qui on s’adresse |
| **Livrable** | Rapport SEO, synthèse, lien landing | Ce qu’on dépose dans le dossier contact |

Règle : **dès qu’une cible est travaillée** (audit SEO fait ou prospect identifié), créer un **dossier contact** `docs/contacts/<slug>/` et y ranger rapport, fiche, notes — comme pour les contacts existants (P4S, Ackuracy, etc.).

---

## 2. Correspondance besoin ↔ preuve recommandée

Pour personnaliser la proposition, mapper le **besoin** (champ `besoin` de l’entreprise) vers la **preuve** la plus parlante (issue de `plan_action_proof_of_value.preuves_recommandees`).

| Type de besoin (exemples) | Preuve à mettre en avant en priorité |
|---------------------------|--------------------------------------|
| SEO (local, niche, technique, concurrentiel) | **Audit SEO concurrentiel local** + synthèse manque à gagner |
| Lead Gen, scraping, extraction, cold mailing | **Scraping prospects qualifiés** |
| Tracking (appels, formulaires, conversions, distributeurs) | **Mise en place tracking appels/formulaires** |
| Automation (devis, suivi leads, reporting) | **Automation (Python/no-code) pour gain de temps commercial** |

Plusieurs besoins possibles par entreprise : choisir la preuve la plus alignée pour le **premier contact**, garder les autres pour la relance ou la proposition détaillée.

---

## 3. Flux opérationnel (toi + équipe)

1. **Prioriser** : Partir des cibles **priorite = HAUTE** (et éventuellement MOYENNE) dans le JSON. Filtrer par segment ou zone si besoin.
2. **Pour chaque cible choisie** :
   - **Audit SEO** : lancer l’audit (Screaming Frog, visibilité, concurrence locale si pertinent). Produire une **synthèse** (nombre de problèmes, impact, échantillon de 5 prospects si trouvés) — voir `rapport-seo-prospect.md` § 2b.
   - **Créer le dossier contact** : `docs/contacts/<slug>/` avec slug dérivé du nom (ex. `socateb`, `lacroix-signalisation`, `clinique-de-bercy`). Règle : minuscules, tirets, pas d’accents. Voir § 4.
   - **Déposer** : `rapport-seo.md` ou `rapport-complet-<slug>.md` (template `template-rapport-complet-prospect.md`), et optionnellement `fiche-contact.json` (décideur, contact trouvé).
   - **Mettre à jour le registre** : `docs/contacts/REGISTRE-CONTACTS.md` (une ligne par nouveau dossier).
3. **Identifier les prospects** : pendant ou après l’audit (LinkedIn, site, OSINT). Renseigner **decideur_cible**, **contact** (email_pattern, tel, web) dans la fiche ou dans des notes — et, si tu veux garder le JSON central à jour, ajouter ces champs dans `2026-01-30_prospection-commando-lowtech.json` pour l’entrée concernée.
4. **Correspondance dans la proposition** : pour l’email / la landing / le message LinkedIn, utiliser **besoin** + **growth_hook** / **angle_relance** (déjà dans le JSON quand renseignés) et la **preuve** correspondante (audit SEO, scraping, etc.) pour personnaliser.

---

## 4. Convention de slug (dossier contact)

Pour les entreprises du JSON low-tech, dériver le slug du **nom** :

- Minuscules, espaces → tirets, pas d’accents, pas de parenthèses (ou les remplacer par un suffixe court).
- Exemples :  
  `SOCATEB` → `socateb`  
  `LACROIX SIGNALISATION` → `lacroix-signalisation`  
  `CLINIQUE DE BERCY` → `clinique-de-bercy`  
  `CUISINES SCHMIDT (réseau IDF)` → `cuisines-schmidt-reseau-idf` ou `schmidt-idf`

Cohérent avec `organisation-donnees-contacts.md` (slug unique, stable, lisible).

---

## 5. Automatisation légère (optionnel)

- **Liste « à traiter »** : script (Python ou Make) qui lit le JSON, liste les entreprises pour lesquelles **il n’existe pas encore** de dossier `docs/contacts/<slug>/`, éventuellement filtrées par **priorite = HAUTE**. Tu peux l’exécuter en début de semaine pour savoir sur quelles cibles concentrer les audits.
- **Export CSV de suivi** : même source JSON → CSV (nom, ville, segment, besoin, priorite, slug, statut « dossier créé » oui/non) pour suivi en tableau (Excel, Google Sheet).
- **Pas d’automatisation complète** (envoi d’emails, création de rapports sans ton passage) : décision projet — données SEO/KPI et contenu par prospect au fur et à mesure. Voir `fonction-premiere-et-segments-prospection.md` § orientations faisabilité.

Si tu veux un tel script, le placer dans `scripts/` avec un README court et le faire exécuter par **Automatizer** ou **Dev Django** (lecture du JSON + liste des slugs manquants ou export CSV).

---

## 6. Récap — qui fait quoi

| Étape | Qui | Livrable / action |
|-------|-----|--------------------|
| Prioriser les cibles | Toi / Growth | Liste (HAUTE, puis MOYENNE) à partir du JSON |
| Audit SEO | Toi | CSV / données → synthèse (nb problèmes, impact, 5 prospects si trouvés) |
| Rapport | Toi / Expert SEO | `rapport-seo.md` ou `rapport-complet-<slug>.md` dans le dossier contact |
| Création dossier contact | Toi / Conseiller / Chef de Projet | `docs/contacts/<slug>/` + entrée REGISTRE-CONTACTS |
| Identification prospects | Toi (LinkedIn, OSINT, site) | Fiche contact, notes, mise à jour JSON si besoin |
| Correspondance besoin ↔ preuve | Toi / Rédacteur | Message / landing / email personnalisé (besoin + growth_hook + preuve) |
| Script liste / CSV | Automatizer / Dev Django (si demandé) | Script dans `scripts/` + doc |

---

## 7. Prochaines étapes immédiates

1. Choisir 3–5 cibles **priorite HAUTE** dans le JSON (ex. LACROIX SIGNALISATION, DESAUTEL, BROSSARD, STILL France, MECALAC, CLINIQUE DE BERCY, CUISINES SCHMIDT, P4S, ECRITEL, KLARITY ASSURANCE).
2. Lancer les **audits SEO** sur ces cibles (site, concurrence locale si pertinent).
3. Pour chaque audit terminé : **créer le dossier contact** (slug), **déposer le rapport**, **mettre à jour REGISTRE-CONTACTS**.
4. Au fur et à mesure : **identifier les prospects** (décideurs, contacts) et les noter dans le dossier ou dans le JSON.
5. (Optionnel) Demander à l’équipe un **script « cibles sans dossier »** ou **export CSV** pour suivre l’avancement.

*Document créé pour structurer l’enchaînement cibles → audits SEO → prospects et la correspondance besoin ↔ preuve. Dernière mise à jour : 2026-01-30.*
