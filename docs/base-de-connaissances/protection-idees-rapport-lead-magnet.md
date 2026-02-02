# Protection des idées et données — rapport lead magnet

**Contexte** : le rapport complet (fiche société, PESTEL/SWOT/Porter, SEO, opportunités, plan d’action) est très riche. S’il est affiché en **accès libre** sur une URL publique (`/p/<slug>/rapport/`), un visiteur (ou un concurrent) peut copier les idées, les données et la méthodologie sans engagement.

**Risque** : se faire « piquer » les idées, les recommandations actionnables et les données (estimations d’impact, priorisation, angles métier).

**Référence** : cette question est déjà identifiée dans le projet — à discuter (niveau d’info, chiffrage). Voir `expert-seo-demarche-rapport-wording-copywriting.md` § 4, `rapport-seo-prospect.md` § 4, `agents-roles-responsabilites.md` (Expert SEO : garder les meilleures pistes en interne).

---

## Pistes de protection (à trancher avec le Chef de Projet)

| Option | Description | Avantage | Inconvénient |
|--------|-------------|----------|--------------|
| **1. Accès restreint au rapport** | La page `/p/<slug>/rapport/` n’est accessible qu’avec un **token** dans l’URL (ex. `/p/p4s-archi/rapport/?token=xxx`) ou après **connexion** (lien envoyé par email après prise de contact). | Seuls les prospects légitimes voient le détail. | Nécessite génération de tokens ou auth ; lien à envoyer manuellement. |
| **2. Version publique allégée** | Sur la landing : **synthèse courte** (2–3 paragraphes, chiffres clés sans le détail). Le **rapport complet** n’est pas en ligne ; tu l’envoies par email ou en visio après un premier échange. | Tu montres la valeur sans tout dévoiler. | Plus de travail manuel (envoi du PDF ou du lien sécurisé). |
| **3. Pas de lien « Rapport » en public** | Retirer le lien « Consulter le rapport » de la nav publique ; garder le rapport en base (Markdown) pour **usage interne** ou envoi ciblé. La landing reste orientée CTA (coordonnées, Diagnostic Flash). | Aucun risque de copie du rapport par un visiteur anonyme. | Le prospect ne voit pas la preuve de la qualité du rapport avant de te contacter. |
| **4. Rapport après engagement** | Le rapport complet n’est débloqué (lien ou PDF) qu’après **prise de rendez-vous** (calendrier) ou **formulaire** (nom, email, société). | Tu filtres les vrais prospects et protèges le contenu. | Mise en place technique (formulaire, envoi automatique du lien, etc.). |

---

## Recommandation courte

- **Court terme** : au minimum, **ne pas partager l’URL du rapport** publiquement (réseaux, signature mail). La donner uniquement au prospect ciblé (ex. Joël P4S) après échange. L’URL existe mais n’est pas indexable ni diffusée.
- **Moyen terme** : trancher la discussion **niveau d’info + chiffrage** (doc § 4) et décider soit **version synthèse publique + détail après contact**, soit **accès rapport par token/lien envoyé à la main**.

---

## Décisions à enregistrer

Une fois la stratégie choisie : mettre à jour `decisions.md` (niveau d’info, accès rapport, chiffrage si pertinent) et ce document (option retenue, mise en œuvre technique si besoin).

---

## Trace et réutilisation : une seule source, un seul généré

- **Source unique** : `docs/contacts/<slug>/rapport-complet-<slug>.md` — le rapport complet est rédigé **une seule fois** et conservé comme trace pour réutilisation (autres prospects, suivi, mise à jour).
- **Teaser public** : `rapport-teaser-<slug>.md` (optionnel) — extrait (synthèse + 1–2 éléments type estimation d’impact) affiché sur la page « Consulter le rapport » pour prouver le sérieux sans tout dévoiler. La vue Django affiche le teaser en priorité s’il existe.
- **PDF** : export optionnel à partir du rapport complet (Markdown) lorsque tu veux envoyer le rapport par email au prospect. Ne pas maintenir deux versions : le Markdown reste la source ; le PDF est généré quand nécessaire (outil externe ou commande à prévoir si besoin).

*Document créé suite à la question utilisateur sur le risque de se faire voler les idées et les données. Référence : expert-seo-demarche-rapport-wording-copywriting.md § 4.*
