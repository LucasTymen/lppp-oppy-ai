# Schéma landing « Proposition » — Full-Stack Conversion

**Template Django** : `templates/landing_pages/proposition.html`  
**Template key** : `proposition` (champ `LandingPage.template_key`).

Structure pensée pour convertir un décideur (Directeur, PDG) : **machine à résoudre des problèmes**, pas un CV en ligne. Mobile-first, sans icônes. Google Fonts (Roboto, Open Sans) chargées par défaut.

---

## Structure des sections (ordre d’affichage)

1. **Hero** — Le « Quoi » et le « Pour qui » : headline (promesse chiffrée), sub-headline (combo), CTA.
2. **Icebreaker** (optionnel) — Contexte de prospection.
3. **Intro** (optionnel) — Phrase d’accroche en texte, pas en titre.
4. **Pain Points** — Vos enjeux : empathie, galères spécifiques (liste ou paragraphe).
5. **Solution / Workflow** — Comment le code transforme le chaos en système (gouvernance, scalabilité, sécurité) + image optionnelle.
6. **Ce que j’offre — Mes services pour vous** — Onglets : Rapport SEO, échantillon de prospects, automatisations et workflows, autres (à définir selon besoins).
7. **Expertise Stack** — Stack technique (langages, automation, data) en tags.
8. **Mission Flash** — Offre irrésistible : audit 48h, 3 leviers, etc.
9. **Pourquoi un Growth Engineer et pas une agence ?** — Citation / argument choc.
10. **CTA final** — Bouton d’action.

---

## Champs `content_json`

| Clé | Obligatoire | Description |
|-----|-------------|-------------|
| `page_title` | Recommandé | Titre de la page (onglet navigateur). Ex. « Optimisation Growth pour P4S Architecture ». |
| `hero_headline` | Recommandé | Promesse chiffrée (ex. « Automatisez 80% de votre Lead Gen Cyber sans recruter »). |
| `hero_sub_headline` | Optionnel | Combo (ex. « Infrastructure Python + Stratégie Growth »). |
| `hero_subtitle` | Optionnel | Pour [Société] — [Prénom]. |
| `intro` | Optionnel | Phrase d’accroche (texte d’intro, pas titre). |
| `icebreaker` | Optionnel | Contexte de prospection personnalisé. |
| `cta_text` | Optionnel | Libellé du CTA (ex. « Réserver mon Diagnostic Flash (15 min) »). |
| `cta_url` | Optionnel | URL du CTA (mailto ou calendrier). |
| `pain_points` | Optionnel | Liste de strings (enjeux / galères) ou une seule string (affichée comme paragraphe via filtre `as_list`). Fallback : `activite_pain_points`. |
| `activite_pain_points` | Optionnel | Texte brut (rétrocompat) si `pain_points` absent. |
| `solution_workflow` | Optionnel | Texte : comment le code transforme le chaos en système. Fallback : `positionnement`. |
| `workflow_image_url` | Optionnel | URL d’une image (schéma RACI, pools d’agents, etc.). |
| `positionnement` | Optionnel | Rétrocompat : utilisé comme `solution_workflow` si ce dernier absent. |
| `services` | Optionnel | Liste d’objets `{ "title": "...", "description": "..." }` pour la section **Ce que j’offre** (onglets) : ex. Rapport SEO, Échantillon de prospects, Automatisations et workflows, autres à définir selon besoins. |
| `expertise_stack` | Optionnel | Objet `{ "langages": [], "automation": [], "data": [] }` — noms d’outils affichés en tags. |
| `mission_flash` | Optionnel | Offre irrésistible (ex. « Audit technique de 48h : j’identifie 3 leviers… »). Fallback : `produit_commercial`. |
| `produit_commercial` | Optionnel | Rétrocompat : utilisé comme `mission_flash` si absent. |
| `why_growth_engineer` | Optionnel | Citation / argument choc (agence vs code propriétaire, RACI, 24/7). |
| `theme` | Optionnel | Thème CSS Vampire (polices, couleurs, logo). Voir `css-vampire.md`. |
| `theme_css` | Optionnel | Variables CSS générées (injectées dans la landing). |

---

## Règles éditoriales

- **Hero** : headline = promesse de résultat chiffré ; sub = combo technique + stratégie.
- **Pain points** : formulations orientées « vous » (empathie, galères spécifiques).
- **Mission Flash** : porte d’entrée facile (audit 48h, 3 leviers), pas un CDI d’emblée.
- **Why Growth Engineer** : punch (« agence = vent et PDF », « moi = code propriétaire, infra 24/7, RACI »).

Référence : `docs/bonnes-pratiques.md` (éditorial anti-détection IA, humanisation).

---

## Exemple (P4S)

Voir `docs/contacts/p4s-archi/landing-proposition-joel.json` et la commande `create_landing_p4s`.

*Dernière mise à jour : 2025-01-30.*
