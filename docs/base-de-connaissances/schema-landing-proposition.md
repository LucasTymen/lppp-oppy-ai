# Schéma landing « Proposition » — Full-Stack Conversion

**Template Django** : `templates/landing_pages/proposition.html`  
**Template key** : `proposition` (champ `LandingPage.template_key`).  
**Hero (Aérosection)** : pattern réutilisable pour les autres landings/rapports — voir `template-hero-aerosection.md`.

**Contenu dynamique** : les champs ci-dessous sont **toujours renseignés par contact** (un prospect = un jeu de données unique). Ne pas réutiliser le même `content_json` pour deux contacts. Voir `strategie-qualite-contenu-landings.md` et `organisation-donnees-contacts.md`.

Structure pensée pour convertir un décideur (Directeur, PDG) : **machine à résoudre des problèmes**, pas un CV en ligne. **Alignement design** : référence « landing CV / page perso » (voir `design-brief-landing-reference-cv.md`) — hero **pleine hauteur** (100vh), nav sticky avec ancres (Enjeux, Solution, Services, Stack, Offre), sections aérées (01–05), animations fade-in hero, smooth scroll. **Style société** : thème CSS Vampire (couleurs, logo, polices) appliqué partout. Mobile-first.

---

## Structure des sections (ordre d’affichage)

1. **Hero** — Le « Quoi » et le « Pour qui » : headline (promesse chiffrée), sub-headline (combo), CTA.
2. **Icebreaker** (optionnel) — Contexte de prospection.
3. **Intro** (optionnel) — Phrase d’accroche en texte, pas en titre.
4. **Pain Points** — Vos enjeux : empathie, galères spécifiques (liste ou paragraphe).
5. **Solution / Workflow** — Comment le code transforme le chaos en système (gouvernance, scalabilité, sécurité) + image optionnelle.
6. **Ce que j’offre — Mes services pour vous** — Onglets : Rapport SEO, Paid Media (prix récupérateur selon besoins), échantillon de prospects, automatisations. Affichage recommandé : grille 2×2 (titre bénéfice `prestations_headline` + CTA « En savoir plus » par bloc). Voir design-brief § 5.
7. **Expertise Stack** — Stack technique (langages, automation, data) en tags.
8. **Mission Flash** — Offre irrésistible : audit 48h, 3 leviers, etc.
9. **Pourquoi un Growth Engineer et pas une agence ?** — Citation / argument choc.
10. **En un coup d'œil** (optionnel) — Diagramme et/ou funnel si `diagram_url` ou `funnel_image_url` renseigné.
11. **CTA final** — Bouton d’action.

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
| `enjeux_lead` | Optionnel | Phrase d’introduction affichée au-dessus de la liste des enjeux (pour humaniser et combler les manques). Ex. « Pour vous, j’ai identifié trois points : » Voir `brief-contenu-vivant-humanisation-landings.md`. |
| `activite_pain_points` | Optionnel | Texte brut (rétrocompat) si `pain_points` absent. |
| `solution_workflow` | Optionnel | Texte : comment le code transforme le chaos en système. Fallback : `positionnement`. |
| `workflow_image_url` | Optionnel | URL d’une image (schéma RACI, pools d’agents, etc.). |
| `positionnement` | Optionnel | Rétrocompat : utilisé comme `solution_workflow` si ce dernier absent. |
| `about_me` | Optionnel | Texte de présentation « Qui je suis » : affiché comme **premier onglet** de la section « Ce que j’offre ». On peut y mettre **toute la liste** (Paid Media, SEO, Data/tracking, Growth & automatisation, création & optimisation + 4 offres) — voir `positionnement-freelance-offres.md`. Ou reprendre le bloc de ta landing CV (`design-brief-landing-reference-cv.md`). Retours à la ligne conservés (`linebreaksbr`). |
| `about_me_title` | Optionnel | Titre de l’onglet (défaut : « Qui je suis »). |
| `services` | Optionnel | Liste d’objets `{ "title": "...", "description": "..." }` pour la section **Ce que j’offre** (onglets) : ex. Rapport SEO, Paid Media, Échantillon de prospects, Automatisations, etc. **Ne pas tout lister** : choisir 2 à 4 services **pertinents pour ce contact** (distiller selon les besoins — voir `positionnement-freelance-offres.md` § Règle ne pas survendre). Si `about_me` est présent, « Qui je suis » est le premier onglet, puis les services. |
| `expertise_stack` | Optionnel | Objet `{ "langages": [], "automation": [], "data": [] }` — noms d’outils affichés en tags. |
| `mission_flash` | Optionnel | Offre irrésistible (ex. « Audit technique de 48h : j’identifie 3 leviers… »). Fallback : `produit_commercial`. |
| `produit_commercial` | Optionnel | Rétrocompat : utilisé comme `mission_flash` si absent. |
| `why_growth_engineer` | Optionnel | Citation / argument choc (agence vs code propriétaire, RACI, 24/7). |
| `hero_background_url` | Optionnel | URL de l'image de fond du hero (prioritaire sur `theme.background_image_url`). |
| `hero_video_url` | Optionnel | URL YouTube (watch ou embed) pour fond du hero : lecture en boucle, muet, plein écran. Ex. `https://www.youtube.com/watch?v=xxx`. Prioritaire sur image si les deux sont renseignés. |
| `theme` | Optionnel | Thème CSS Vampire (polices, couleurs, logo). Voir `css-vampire.md`. |
| `theme.use_fallback` | Optionnel | Si `true`, applique le style perso (fallback). Voir `style-perso-fallback.md`. |
| `theme_css` | Optionnel | Variables CSS générées (injectées dans la landing). |
| `use_perso_style` | Optionnel | Si `true`, force le style perso (fallback). Voir `style-perso-fallback.md`. |
| `diagram_url` | Optionnel | URL d'une image de diagramme personnalisé (section « En un coup d'œil »). |
| `funnel_image_url` | Optionnel | URL d'une image de funnel adapté (section « En un coup d'œil »). |
| `prospects` | Optionnel | Liste d'objets `{ "name": "...", "company": "...", "role": "...", "relevance": "..." }` pour la page **Prospects** (`/p/<slug>/prospects/`). Échantillon de prospects identifiés pour ce contact. |
| `contact_email` | Optionnel | Adresse e-mail affichée en dur (ex. `lucas.tymen@gmail.com`) dans la section Coordonnées. Prioritaire sur `contact_gmail` : évite le mailto si aucun client mail configuré ; le texte est copiable. |
| `contact_gmail` | Optionnel | URL mailto. Utilisé seulement si `contact_email` est absent. Sinon, on affiche `contact_email` en clair. |
| `rapport_url` | Optionnel | URL du rapport (version intermédiaire, Google Doc, PDF, etc.). Si renseigné : lien « Consulter le rapport » dans la nav et bloc « Consulter le rapport complet » dans la section Ce que j'offre. Sinon ces liens sont masqués. |
| `contact_linkedin` | Optionnel | URL du profil LinkedIn. Affiche un lien « LinkedIn » dans la section **Coordonnées**. |
| `contact_github` | Optionnel | URL du profil GitHub. Affiche un lien « GitHub » dans la section **Coordonnées**. |
| `contact_linktree` | Optionnel | URL du Linktree (ou équivalent). Affiche un lien « Linktree » dans la section **Coordonnées**. |
| `coordonnees_intro` | Optionnel | Phrase affichée au-dessus des coordonnées (ex. « Pour échanger ou voir le prototype : »). Si vide, les templates peuvent utiliser un texte par défaut. Voir `brief-contenu-vivant-humanisation-landings.md`. |
| `loom_embed_url` | Optionnel | URL d'embed Loom (ex. `https://www.loom.com/embed/xxx`) pour la section **Démo 60 sec**. Si renseigné, une section avec iframe vidéo est affichée après la section Solution. |
| `alert_banner` | Optionnel | Bandeau teal sous la nav (style 0Flaw). Une ligne de texte centrée, fond `--lp-primary`. Ex. « Rapport d'audit offert — Réserver un échange ». |
| `seo_resume` | Optionnel | Objet pour la section **Résumé SEO** sur la landing : `title`, `manque_annuel`, `intro`, `problemes_cles` (liste de strings), `lien_analyse` (libellé du lien). Affiche un résumé et un lien vers `rapport_url#analyse-seo-complete`. Nécessite `rapport_url` renseigné. |
| `demo_video_caption` | Optionnel | Légende affichée au-dessus de la vidéo (ex. « En 60 secondes : comment j'ai automatisé… »). |

**Comportement contact** : si au moins un des champs `contact_*` est renseigné, la section « Coordonnées » est affichée, le lien nav « Me contacter » pointe vers `#coordonnees`, et les CTA (hero + bas de page) pointent vers `#coordonnees` au lieu de `cta_url`. Sinon, le CTA utilise `cta_url` (ex. mailto) comme avant.

---

## Règles éditoriales

- **Hero** : headline = promesse de résultat chiffré ; sub = combo technique + stratégie.
- **Pain points** : formulations orientées « vous » (empathie, galères spécifiques).
- **Mission Flash** : porte d’entrée facile (audit 48h, 3 leviers), pas un CDI d’emblée.
- **Why Growth Engineer** : punch (« agence = vent et PDF », « moi = code propriétaire, infra 24/7, RACI »).

Référence : `docs/bonnes-pratiques.md` (éditorial anti-détection IA, humanisation).

---

## Projets à venir — à porter comme modification

Pour chaque nouvelle landing, **ne pas recréer de document** : s’appuyer sur les **fiches de mission existantes** et les mettre à jour si besoin. À prévoir :

| Domaine | Fiche à suivre | Ce qu’on apporte |
|---------|----------------|------------------|
| **Rapport** | `brief-contenu-vivant-humanisation-landings.md` | Page rapport (présentation + résumé + ancre `#analyse-seo-complete`), `rapport_url`, lien « Consulter le rapport ». |
| **Style** | `design-brief-landing-reference-cv.md`, `css-vampire.md` | Étude approfondie : couleurs, dégradés, logos, image de fond hero ; thème manuel si CSS Vampire insuffisant ; `hero_background_url` ; bandeau `alert_banner`. |
| **Contenu humanisé** | `brief-contenu-vivant-humanisation-landings.md` | `seo_resume`, `alert_banner`, `enjeux_lead`, `positionnement`, `coordonnees_intro` ; compléter le squelette. |
| **Squelette → complète** | `strategie-qualite-contenu-landings.md`, `docs/contacts/<slug>/squelette-vs-inversion-complete.md` | Réutiliser la checklist 0flow (ou l’adapter au slug) : thème, hero, rapport, démo Loom. |

Exemple de référence : `docs/contacts/0flow/` (rapport, seo_resume, alert_banner, thème manuel, hero image).

---

## Exemple (P4S)

Voir `docs/contacts/p4s-archi/landing-proposition-joel.json` et la commande `create_landing_p4s`.

*Dernière mise à jour : 2025-01-30.*
