# Expert SEO — Démarche : étude wording + copywriting, croisement avec le rapport SEO

**Rôle** : Démarche de l’Expert SEO / AI-GEO pour produire le rapport lead magnet : étude **wording** (wordpricing / choix des mots, formulation) et **copywriting**, croisement avec le **rapport SEO** fourni par l’utilisateur.  
**Pilote** : Expert SEO / AI-GEO.  
**Référence** : `rapport-seo-prospect.md` (rapport SEO), `expert-seo-ai-geo.mdc` (règle Expert SEO).

---

## 1. Objectif de la démarche

1. **Étude et rapport** sur ce qui peut être amélioré en **wording** (wordpricing — choix des mots, formulation, ton) et en **copywriting** (accroches, CTA, structure du message, conversion).
2. **Croisement** de ces données avec le **rapport SEO** fourni par l’utilisateur (stats, indexation, visibilité, données Screaming Frog ou autre).
3. **Livrable** : rapport structuré pour le lead magnet (onglet landing), avec pistes d’amélioration croisées (SEO + wording + copywriting), en gardant les meilleures pistes en interne.

---

## 2. Périmètre de l’étude

### 2.1 Wording (wordpricing)

- **Choix des mots** : vocabulaire, niveau de langue, cohérence avec la cible et le secteur.
- **Formulation** : clarté, concision, ton (professionnel, accessible, incisif).
- **Cohérence** : alignement avec la charte, le positionnement et les segments (voir `fonction-premiere-et-segments-prospection.md`).

### 2.2 Copywriting

- **Accroches** : titres, sous-titres, premiers paragraphes (hook).
- **CTA (calls-to-action)** : formulation, placement, urgence / bénéfice.
- **Structure du message** : hiérarchie, lisibilité, parcours de conversion.
- **Éditorial anti-détection IA** : appliquer `docs/bonnes-pratiques.md` (humanisation, pas de marqueurs IA).

### 2.3 Croisement avec le rapport SEO

- **Entrées** : rapport SEO fourni par l’utilisateur (CSV Screaming Frog, KPIs, visibilité, indexation, etc.) + contenus / pages analysés (wording, copywriting).
- **Traitement** : croiser les recommandations SEO (technique, sémantique) avec les recommandations wording + copywriting pour proposer des **pistes cohérentes** (ex. : un même bloc de contenu peut être optimisé à la fois pour le SEO et pour la conversion).
- **Sortie** : rapport unifié (synthèse, chiffres clés, pistes SEO + wording + copywriting), partie publique (lead magnet) et partie interne (meilleures pistes réservées).

---

## 3. Stack et outils

- **SEO sémantique** : stack Python open-source (spaCy, Gensim, NLTK, Transformers) pour topic modelling, clustering, similarité — voir `seo-semantique-outils-open-source.md`.
- **Rapport SEO** : données fournies par l’utilisateur (fichiers dans `docs/ressources-utilisateur/` ou transmis via le Conseiller) ; référence méthodologie dans `rapport-seo-prospect.md`.
- **Bonnes pratiques** : `docs/bonnes-pratiques.md` (éditorial, humanisation).

---

## 4. Niveau d’information à transmettre et chiffrage (à discuter)

**À discuter avec l’utilisateur** : niveau d’information que l’on transmet dans le rapport lead magnet (public) et comment **chiffrer** la valeur pour éviter de se faire « piquer » les idées.

- **Niveau d’information** : combien dévoiler dans le rapport public (pistes génériques vs pistes très actionnables) ; ce qui reste en **note interne** (stratégie avancée, leviers différenciants).
- **Chiffrage** : comment quantifier / monétiser la valeur du conseil (rapport gratuit vs payant, paliers de détail, offre de suivi) pour protéger les idées et rémunérer l’expertise.
- **Documentation** : une fois la discussion tenue, mettre à jour ce document (décisions dans `decisions.md`) et la règle Expert SEO si besoin.

---

## 5. Références projet

- **Rapport SEO prospect** : `docs/base-de-connaissances/rapport-seo-prospect.md`
- **Règle Expert SEO** : `.cursor/rules/expert-seo-ai-geo.mdc`
- **Registre** : `docs/base-de-connaissances/registre-agents-ressources.md`
- **Bonnes pratiques** : `docs/bonnes-pratiques.md`
- **Décisions** : `docs/base-de-connaissances/decisions.md` (niveau d’info, chiffrage, après discussion)

---

*Document maintenu par l’Expert SEO / AI-GEO. Dernière mise à jour : 2025-01-30. Section § 4 à compléter après discussion niveau d’information et chiffrage.*
