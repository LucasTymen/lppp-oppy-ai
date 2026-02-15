# Sprint — DevOps mène la résolution (Erreur 153, chatbot vide, VariableDoesNotExist)

**Date** : 2026-02-07  
**Statut** : 🟡 En cours  
**Pilote** : **DevOps** (consulte tous les agents, intervient directement, organise les flux pour empêcher les erreurs de se reproduire).

**Objectif** : Solutionner et **empêcher** la réapparition de : (1) **Erreur 153** (vidéo YouTube hero), (2) **Chatbot vide** (écran blanc / iframe), (3) **VariableDoesNotExist** (ex. `hero_subtitle` sur `/p/maisons-alfort/`).

**Règle** : DevOps consulte le registre, les règles (Pentester, Automatizer, Chef de Projet), `erreurs-et-solutions.md` et `integration-video-youtube-landings.md` ; applique les correctifs dans le code et la doc ; met à jour les flux pour que ces erreurs ne se reproduisent pas.

---

## Contexte

- **Erreur rencontrée** : `VariableDoesNotExist at /p/maisons-alfort/` — `Failed lookup for key [hero_subtitle]` dans le template `proposition.html` (hero sub). Le `content` passé à la vue ne contenait pas la clé `hero_subtitle` ; un template (ou une ancienne version en conteneur) utilisait `default:content.hero_subtitle`, ce qui provoque une résolution de variable et l’exception.
- **Objectifs du sprint** : Corriger le code, renforcer la vue et les templates, documenter les flux anti-régression.

---

## Flux anti-régression (organisés par DevOps)

### 1. VariableDoesNotExist (clés `content.*`)

| Qui | Action |
|-----|--------|
| **Vue** | `_content_with_defaults()` dans `apps/landing_pages/views.py` : **toujours** renseigner **les deux** clés `hero_sub_headline` et `hero_subtitle` avec la **même** valeur normalisée (`hero_sub_headline or hero_subtitle or ""`). Ainsi, tout template (y compris ancienne version en conteneur) qui référence l’une ou l’autre ne lève pas d’exception. |
| **Templates** | Utiliser de préférence **une seule** clé normalisée : `content.hero_sub_headline` avec `|default:''`. Ne **jamais** utiliser `default:content.hero_subtitle` (ni toute autre clé potentiellement absente) dans un filtre — privilégier un default littéral ou une clé garantie par la vue. |
| **Prévention** | Toute nouvelle clé `content.*` utilisée dans un template doit être ajoutée aux `defaults` dans `_content_with_defaults()` et, si besoin, normalisée (une valeur, plusieurs clés) pour compatibilité. Voir `erreurs-et-solutions.md` § VariableDoesNotExist. |

### 2. Erreur 153 (YouTube)

| Qui | Action |
|-----|--------|
| **Settings** | `SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"` dans `lppp/settings.py` (SecurityMiddleware envoie l’en-tête sur la réponse). |
| **Vue** | En-tête explicite sur la réponse landing : `response["Referrer-Policy"] = "strict-origin-when-cross-origin"` (déjà en place dans `landing_public`). |
| **Template iframe** | `referrerpolicy="strict-origin-when-cross-origin"` sur l’iframe ; URL via filtre **youtube-nocookie.com** (`youtube_embed_background`) ; lien de secours « Regarder la vidéo sur YouTube » (`youtube_watch_url`). |
| **Prévention** | Avant d’ajouter une vidéo YouTube : consulter `integration-video-youtube-landings.md`. Ne jamais ajouter une iframe YouTube sans referrer policy et sans lien de secours. Voir `erreurs-et-solutions.md` § YouTube Erreur 153. |

### 3. Chatbot vide (Flowise)

| Qui | Action |
|-----|--------|
| **Vue** | Pour le slug `maisons-alfort`, injection de `flowise_embed_url`, `flowise_api_host`, `flowise_chatflow_id` ; en cas d’exception, passage de chaînes vides pour éviter 500. |
| **Template** | Utiliser le web component **flowise-fullchatbot** (comme concierge) lorsque `flowise_api_host` et `flowise_chatflow_id` sont présents ; proposer un lien « Ouvrir le chat dans un nouvel onglet » pour diagnostic. |
| **Infra** | Flowise sur le port prévu (3010 en dev) ; `FLOWISE_URL`, `FLOWISE_CHATFLOW_ID` dans `.env` ; `docker compose exec web python manage.py check_flowise_embed` pour vérifier l’URL d’embed. |
| **Prévention** | Voir `flowise-chatbot-ecran-vide-diagnostic.md`, `erreurs-et-solutions.md` (écran blanc, iframe vide). |

---

## Tâches réalisées (2026-02-07)

- [x] **VariableDoesNotExist hero_subtitle** : (1) Vue — `_content_with_defaults()` renseigne désormais **les deux** clés `hero_sub_headline` et `hero_subtitle` avec la même valeur normalisée pour les templates `proposition`, `proposition_value`, `relance-evenement`. (2) Template `relance-evenement.html` — utilisation de `content.hero_sub_headline` uniquement (plus de référence à `hero_subtitle` dans le bloc hero). (3) Template `proposition.html` — déjà sécurisé (`hero_sub_headline|default:''`) ; la vue garantit que même une ancienne version du template (conteneur non reconstruit) ne plantera pas.
- [ ] **Vérification en environnement** : après déploiement ou `docker compose up --build web`, vérifier que `/p/maisons-alfort/` se charge sans 500 et que le hero (titre, sous-titre, vidéo) et le chatbot s’affichent correctement.
- [ ] **Mise à jour logs** : log-projet, log-ia et ce document mis à jour en fin de sprint.

---

## Références

- **Erreurs** : `erreurs-et-solutions.md` (VariableDoesNotExist, YouTube 153, chatbot écran vide)
- **Vidéo YouTube** : `integration-video-youtube-landings.md`
- **Chatbot** : `flowise-chatbot-ecran-vide-diagnostic.md`
- **Vue** : `apps/landing_pages/views.py` (`_content_with_defaults`, `landing_public`)
- **Templates** : `templates/landing_pages/proposition.html`, `relance-evenement.html`, `proposition_value.html`
- **Sprint précédent** : `2026-02-07-sprint-refonctionnement-landing-optimisation-hierarchisation.md`

---

*Sprint piloté par DevOps ; consultation de tous les agents via registre et base de connaissances. Dernière mise à jour : 2026-02-07.*
