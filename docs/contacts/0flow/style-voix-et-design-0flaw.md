# Style voix et design 0Flaw — Brief Rédacteur & Designer

**Pour** : Rédacteur, Designer (webdesign), Chef de Projet.  
**Objectif** : Aligner la **voix** (rédaction) et le **design** (visuel) de la landing 0flow sur le style de 0Flaw (https://0flaw.fr/), pour que le prospect se sente dans son univers.

**Références** : `docs/base-de-connaissances/bonnes-pratiques.md`, `brief-contenu-vivant-humanisation-landings.md`, `css-vampire.md`, `design-brief-landing-reference-cv.md`.

---

## 1. Style voix 0Flaw (Rédacteur)

### 1.1 Ton et niveau de langue

- **Professionnel et direct** : pas de formel excessif ; « vous » naturel, phrases courtes et percutantes.
- **Orienté bénéfices** : chaque bloc répond à « quoi pour eux » (former, tester, sécuriser, anticiper).
- **Vocabulaire cybersécurité** : posture cyber, vigilance, menaces, conformité, audits, formations, phishing, simulations, tableaux de bord — sans jargon technique lourd (ils parlent « équipes », « bons réflexes », « situations réalistes »).
- **Accroches type 0Flaw** : « plateforme 360° », « élever sa posture », « sans les saturer », « ancrer les bons réflexes », « anticiper avec une avance stratégique ».

### 1.2 Formulations à s’inspirer (0flaw.fr)

| Contexte | Exemple 0Flaw | À adapter pour la landing 0flow |
|----------|----------------|-----------------------------------|
| Proposition de valeur | « La plateforme 360° qui forme, teste et sécurise votre entreprise » | Angle automation / workflow : « la chaîne qui connecte, automatise et sécurise vos outils » |
| Bénéfice court | « Formez vos équipes en continu, sans les saturer » | « Automatisez en continu, sans saturer vos équipes » |
| Preuve / clarté | « Tableaux de bord clairs », « résultats concrets et précis » | « Rapports et indicateurs clairs », « gains mesurables » |
| CTA | « Demander une démo », « Parler à un expert », « Réserver une démo » | Garder le même niveau : « Réserver un échange », « Voir la démo 60 sec », « Télécharger le rapport d’audit » |

### 1.3 À éviter

- Formules trop commerciales ou « startup » (pas de « disrupt », « game-changer »).
- Listes interminables ; privilégier 3–4 points forts par section.
- Ton infantilisant ou alarmiste ; 0Flaw est rassurant et factuel (« sans jamais les exposer », « prouvez facilement vos efforts »).

### 1.4 Où appliquer

- **Hero** : intro + icebreaker en phase avec ce ton (bénéfice, clarté).
- **Enjeux / pain points** : formulations « vous » + vocabulaire cyber/automation.
- **Services (Insight Cards)** : titres percutants, sous-titres courts, CTA cohérents.
- **Mission flash / CTA** : direct, invitant (« Je te montre le prototype quand tu veux » reste OK, voir `brief-contenu-vivant-humanisation-landings.md`).

---

## 2. Design — CSS Vampire sur 0flaw.fr (Designer)

### 2.1 Principe

Pour que la landing **0flow** reprenne les **couleurs, polices et logo** de 0Flaw, exécuter **CSS Vampire** sur le site cible. Le thème extrait est injecté dans `content_json` (theme, theme_css) et appliqué par le template `proposition.html`.

Référence complète : `docs/base-de-connaissances/css-vampire.md`.

### 2.2 Commande à lancer

**Sur l’hôte (WSL)** — avec le backend Django qui tourne et la landing 0flow déjà créée en base :

```bash
python3 manage.py css_vampire https://0flaw.fr/ --slug 0flow --apply
```

**Dans Docker** :

```bash
docker compose exec web python3 manage.py css_vampire https://0flaw.fr/ --slug 0flow --apply
```

### 2.3 Ce que CSS Vampire extrait de 0flaw.fr

| Élément | Utilisation sur la landing 0flow |
|--------|-----------------------------------|
| **Couleurs** | `--lp-bg`, `--lp-text`, `--lp-primary`, `--lp-secondary` (fond, textes, boutons, liens) |
| **Polices** | `--lp-font-body`, `--lp-font-heading` (si présentes sur le site) |
| **Logo** | Affiché en nav et dans le hero (sauf si `--no-logo`) |
| **Fond** | Si une image de fond est extraite (et non filtrée) : hero 100 %, parallaxe, scanlines. Sinon : dégradé à partir des couleurs du thème. |

### 2.4 Ordre recommandé

1. Créer/mettre à jour la landing en base : `python3 manage.py create_landing_0flow --update [--publish]`.
2. Lancer CSS Vampire sur la page **Formation** (proche de notre approche) : `css_vampire https://0flaw.fr/solution/formation --slug 0flow --apply`.
3. Vérifier le rendu sur `/p/0flow/` (recharger sans cache si besoin).
4. Ajuster le contenu (JSON) si besoin, puis refaire `create_landing_0flow --update` **sans** refaire CSS Vampire (le thème est conservé).

---

## 3. Synthèse pour les agents

| Rôle | Action |
|------|--------|
| **Rédacteur** | Rédiger et mettre à jour les textes de `landing-proposition-samson.json` en respectant le **style voix 0Flaw** (§ 1). |
| **Designer** | S’assurer que le **thème 0Flaw** est appliqué via **CSS Vampire** (§ 2) ; vérifier hiérarchie, espacements et CTA (voir `design-brief-landing-reference-cv.md`, `brief-contenu-vivant-humanisation-landings.md`). |
| **Chef de Projet** | Valider cohérence voix + visuel avant envoi / entretien. |

---

*Document créé pour la landing 0flow (Samson Fedida). Dernière mise à jour : 2026-01-30.*
