# Stratégie qualité contenu — toutes les landings

**Objectif** : Obtenir pour **tous** les templates et **toutes** les landings la même qualité de contenu que la landing P4S (complète, personnalisée, sans squelette), tout en gardant le contenu **100 % dynamique** : on ne s’adresse jamais deux fois au même profil, ni aux mêmes activités, ni aux mêmes personnes.

**Pilotes** : Chef de Projet (validation, coordination), Rédacteur (contenus par contact), Designer (templates), Dev Django (données + export), DevOps (déploiement).  
**Référence qualité** : Landing P4S (Django `/p/p4s-archi/` + export statique Vercel).

---

## 1. Référence « qualité P4S » (barre à atteindre partout)

Toute landing livrée doit atteindre ce niveau, quel que soit le template (Django `proposition`, futur `modern` / `minimal` / `corporate`, Next.js standalone, export statique) :

| Critère | Description |
|--------|-------------|
| **Contenu complet** | Toutes les sections prévues par le template sont remplies depuis les données (hero, enjeux, solution, services, stack, offre, coordonnées, CTA). Pas de blocs vides ni de « Lorem ipsum ». |
| **Pas de squelette** | La page affichée = la page finale. Pas de structure vide, pas de placeholders visibles pour le visiteur. |
| **Contact utilisable** | CTA et coordonnées fonctionnent : popup contact avec texte « Vous pouvez me contacter par Mail à cette adresse : [email] » (fallback quand `mailto:` ne fonctionne pas). Voir `erreurs-et-solutions.md` § CTA/Gmail. |
| **Rapport (si applicable)** | Si un rapport intermédiaire existe pour le contact, lien « Consulter le rapport complet » pointant vers une URL ou une page dédiée (ex. `rapport.html` ou `/p/<slug>/rapport/`), avec ancre `#analyse-seo-complete` si analyse SEO détaillée. Sinon, pas de lien mort. |
| **Résumé SEO (si étude)** | Quand une étude SEO / manque à gagner existe : section « Résumé SEO » sur la landing (`seo_resume`) + lien vers la page rapport (ancre). Renforce la crédibilité sans dupliquer tout le rapport. |
| **Personnalisation visuelle** | Hero avec image de fond (ou thème), style perso ou thème CSS Vampire (ou **thème manuel** si extraction insuffisante) ; pas de page générique non personnalisée. |
| **Source unique par contact** | Tout le contenu affiché provient d’**un seul** jeu de données associé à **ce** contact (voir § 2). |

**Squelette vs inversion complète** : une landing « squelette » a le contenu rempli mais un style générique (pas de thème cible, pas de logo, pas de rapport/démo). L’**inversion complète** = contenu OK + thème (CSS Vampire ou manuel) + optionnel démo Loom + lien rapport + vérif visuelle. Pour les projets à venir, utiliser la checklist de passage squelette → complète sans recréer de doc : voir `docs/contacts/0flow/squelette-vs-inversion-complete.md` (et l’adapter au slug du contact).

Référence technique : `templates/landing_pages/proposition.html`, `docs/contacts/p4s-archi/landing-proposition-joel.json`, `docs/contacts/0flow/squelette-vs-inversion-complete.md`, `reconstitution-landing-p4s-personnalisation.md`, `schema-landing-proposition.md`.

---

## 2. Contenu 100 % dynamique — règle impérative

**On ne s’adresse jamais deux fois au même profil ni aux mêmes activités ni aux mêmes personnes.** Donc :

- **Un contact (prospect) = un jeu de données unique.** Pas de réutilisation du même `content_json` ou du même fichier JSON pour deux contacts différents.
- **Source de vérité par contact** : `docs/contacts/<slug>/landing-proposition-<prénom ou identifiant>.json` (ou équivalent selon le type de landing). Chaque fichier est rédigé/spécifique pour ce contact (société, nom, enjeux, offre, rapport, coordonnées affichées).
- **En base Django** : chaque `LandingPage` a son propre `content_json` ; pas de copier-coller d’une landing à l’autre sans adapter tout le contenu au nouveau contact.
- **Export / déploiement** : l’export statique ou le build Next.js utilisent **le** JSON (ou le `content_json`) du contact cible, jamais un fichier « exemple » ou générique.

Conséquences pour l’équipe :
- **Rédacteur** : produit un contenu distinct par contact (headline, pain points, services, mission flash, etc.).
- **Chef de Projet** : vérifie qu’aucune landing n’est livrée avec un contenu partagé ou un placeholder.
- **Dev Django / Designer** : les templates lisent uniquement les variables issues du contexte (content, landing_page) ; aucun texte en dur spécifique à un prospect.

Voir `organisation-donnees-contacts.md` (un contact = un dossier, données isolées).

---

## 3. Application systématique par type de livrable

| Type | Règle |
|------|--------|
| **Template Django (proposition, futur modern/minimal/corporate)** | Le template affiche toutes les sections prévues ; les champs vides (optionnels) masquent la section (pas de bloc vide). Contenu 100 % depuis `content` / `content_json`. |
| **Nouvelle landing (nouveau contact)** | Créer `docs/contacts/<slug>/` et un JSON de proposition dédié ; remplir toutes les clés nécessaires pour atteindre la qualité P4S ; ne pas réutiliser le JSON d’un autre contact. |
| **Export statique (Vercel, etc.)** | Utiliser `export_landing_static` avec le slug (et `--json` si besoin) ; inclure `--rapport-md` si un rapport intermédiaire existe. La page exportée doit être identique à la vue Django (contenu + popup contact + lien rapport si présent). |
| **Standalone Next.js** | Contenu depuis `landing.json` copié depuis le dossier contact ; hero + toutes les sections ; pas de squelette. Voir `generation-landing-nextjs-contenu-hero.md`. |

---

## 4. Rôles et responsabilités (équipe)

| Rôle | Responsabilité dans la stratégie |
|------|-----------------------------------|
| **Chef de Projet** | Valider que chaque landing livrée respecte la barre « qualité P4S » et la règle contenu dynamique ; refuser un livrable squelette ou contenu réutilisé à l’identique pour un autre contact. |
| **Rédacteur** | Rédiger un contenu **unique par contact** (headline, enjeux, solution, services, mission flash, etc.) ; déposer le JSON dans `docs/contacts/<slug>/` ; appliquer `bonnes-pratiques.md` (éditorial, humanisation, image pratique § 2 bis). |
| **Designer** | S’assurer que les templates (Django et/ou Next.js) affichent toutes les sections à partir des données ; pas de texte en dur lié à un prospect ; popup contact et liens conditionnels (rapport) intégrés. |
| **Dev Django** | Maintenir le schéma `content_json` et les templates pour que tout soit piloté par les données ; export statique avec même logique que la vue ; pas de contenu codé en dur. |
| **DevOps** | Déploiement des pages statiques ou Next.js avec le bon contenu (repo / build alimenté par le JSON du contact). |
| **Expert SEO / Growth** | Rapports et études (rapport intermédiaire, PESTEL/SWOT, etc.) par contact dans `docs/contacts/<slug>/` ; alimentation du lien « Consulter le rapport » quand applicable. |

---

## 5. Checklist « qualité contenu » (avant livraison landing)

À valider avant de considérer une landing livrée (Chef de Projet ou agent qui assiste) :

- [ ] **Un contact = un jeu de données** : le contenu affiché provient d’un JSON (ou `content_json`) dédié à ce contact, pas partagé avec un autre.
- [ ] **Sections complètes** : hero, enjeux, solution, services, stack, offre, coordonnées, CTA sont renseignés et visibles (ou masqués proprement si optionnels vides).
- [ ] **Pas de squelette** : aucun bloc vide, placeholder ou « à remplir » visible pour le visiteur.
- [ ] **Contact utilisable** : CTA et/ou Gmail ouvrent le popup avec l’email (ou lien fonctionnel) ; pas de lien mort.
- [ ] **Rapport** : si rapport intermédiaire prévu, le lien « Consulter le rapport » pointe vers une URL/page valide ; sinon le lien est absent.
- [ ] **Personnalisation** : hero (image ou thème) et style cohérents avec la cible (société ou style perso).
- [ ] **Éditorial** : ton et formulations conformes à `bonnes-pratiques.md` (humanisation, pas de détection IA, image pratique § 2 bis).

---

## 6. Fichiers et références

| Document | Usage |
|----------|--------|
| `schema-landing-proposition.md` | Structure des champs `content_json` ; rappel : contenu toujours par contact. |
| `organisation-donnees-contacts.md` | Un contact = un dossier ; où ranger les JSON et rapports. |
| `reconstitution-landing-p4s-personnalisation.md` | Degrés de personnalisation (hero, thème, style perso, contenu). |
| `generation-landing-nextjs-contenu-hero.md` | Application qualité + contenu dynamique pour les standalones Next.js. |
| `erreurs-et-solutions.md` | Popup contact (CTA/Gmail), déploiement, auth Git. |
| `deploy/PUSH-POUR-VERSION-COMPLETE.md` | Export + rapport intermédiaire + déploiement P4S. |
| `brief-contenu-vivant-humanisation-landings.md` | Contenu vivant, humanisation, combler les manques (positionnement, enjeux_lead, callout, rapport, seo_resume, alert_banner) ; Rédacteur + Designer. |
| `docs/contacts/0flow/squelette-vs-inversion-complete.md` | Checklist squelette → inversion complète (thème, hero, rapport, démo) ; à réutiliser/adapter pour chaque nouveau contact. |

---

*Stratégie validée par l’utilisateur : qualité P4S pour tous les templates, contenu 100 % dynamique (jamais 2 fois le même profil/activité/personne). Dernière mise à jour : 2025-01-30.*
