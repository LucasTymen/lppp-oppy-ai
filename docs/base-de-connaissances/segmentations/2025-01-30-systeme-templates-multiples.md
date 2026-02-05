# Système de templates multiples pour landing pages

**Date** : 2025-01-30  
**Chef de Projet** : Agent Chef de Projet UX/UI  
**Statut** : 🟡 En cours (planification terminée, développement à démarrer)

---

## 📋 User Story

> En tant qu'utilisateur LPPP, je veux pouvoir choisir parmi plusieurs templates de landing page (moderne, minimaliste, corporate) afin d'adapter le design à la cible de prospection et maximiser le taux de conversion.

**Contexte** :
- Actuellement, le projet n'a qu'un seul template (`default.html`) très basique (système-ui, sans design moderne)
- Les tendances web 2026 montrent que les landing pages performantes utilisent des designs différenciés selon la cible (startup tech vs corporate traditionnel)
- Un système de templates multiples permet de personnaliser l'expérience sans développer une landing page custom pour chaque prospect

**Critères d'acceptation** :
- [ ] Au moins 3 templates disponibles : "modern", "minimal", "corporate"
- [ ] Sélection du template dans l'admin Django (champ `template_key`)
- [ ] Chaque template est responsive (mobile-first)
- [ ] Les contenus dynamiques (`content_json`) s'adaptent à chaque template
- [ ] **Qualité contenu** : chaque template atteint la barre « qualité P4S » (contenu complet, pas de squelette, contact utilisable) ; contenu **100 % dynamique** (un contact = un jeu de données unique). Voir `strategie-qualite-contenu-landings.md`.
- [ ] Temps de chargement < 2s (Lighthouse)
- [ ] Score accessibilité > 90 (WCAG 2.1)

---

## 🎯 Objectifs et KPIs

**Objectif principal** : Augmenter le taux de conversion de 20% en adaptant le design à la cible

**KPIs mesurables** :
- Temps de chargement < 2s (Lighthouse Performance)
- Taux de conversion par template (A/B testing futur)
- Score accessibilité > 90 (Lighthouse Accessibility)
- Adoption : 80% des nouvelles landing pages utilisent un template non-default

---

## 🔧 Specs techniques

### Architecture

**Composants impactés** :
- `apps/landing_pages/models.py` : modifier `LandingPage.template_key` (choices)
- `apps/landing_pages/views.py` : logique de sélection de template
- `apps/landing_pages/admin.py` : ajouter le champ dans l'admin
- `templates/landing_pages/` : créer `modern.html`, `minimal.html`, `corporate.html`

**Nouvelles dépendances** :
- Tailwind CSS (via CDN pour démarrage rapide, build optimisé plus tard)
- Alpine.js (optionnel, pour micro-interactions légères)

**Modifications de base de données** :
- Modifier `LandingPage.template_key` : `CharField(max_length=80, default="default", choices=[...])`
- Migration Django à créer

### Données

**Champs `content_json` nécessaires** (communs à tous les templates) :
```json
{
  "hero": {
    "title": "Titre principal",
    "subtitle": "Sous-titre accrocheur",
    "cta_text": "Démarrer maintenant",
    "cta_url": "#contact",
    "background_image_url": "https://..." // optionnel
  },
  "features": [
    {"icon": "⚡", "title": "Rapide", "description": "..."},
    {"icon": "🔒", "title": "Sécurisé", "description": "..."}
  ],
  "testimonials": [
    {"author": "Jean Dupont", "company": "Acme Corp", "text": "..."}
  ],
  "cta_final": {
    "title": "Prêt à démarrer ?",
    "text": "Contactez-nous dès aujourd'hui",
    "button_text": "Prendre rendez-vous"
  }
}
```

**Sources de données** :
- Saisie manuelle dans l'admin Django (phase 1)
- Génération automatique via n8n/Flowise (phase 2, future)

### Design

**Templates concernés** :

1. **modern.html** : Startup tech, SaaS
   - Hero avec vidéo ou gradient animé
   - Typographie moderne (Inter, Poppins)
   - Couleurs vives (bleu électrique, violet)
   - Animations scroll reveal
   - CTA contrastés (orange, vert)

2. **minimal.html** : Agence, freelance, design studio
   - Beaucoup d'espaces blancs
   - Typographie élégante (serif pour titres)
   - Noir & blanc avec 1 couleur accent
   - Mise en page asymétrique
   - Micro-interactions subtiles

3. **corporate.html** : Entreprise traditionnelle, B2B
   - Layout classique et rassurant
   - Typographie professionnelle (sans-serif)
   - Couleurs sobres (bleu marine, gris)
   - Logos clients en évidence
   - Formulaire de contact prominent

**Composants réutilisables** :
- Hero section (variantes : vidéo, image, gradient)
- Features grid (2, 3 ou 4 colonnes)
- Testimonials carousel
- CTA section (inline ou full-width)
- Footer (liens, mentions légales)

**Responsive** :
- Mobile-first (breakpoints Tailwind : sm, md, lg, xl)
- Menu hamburger sur mobile
- Images optimisées (srcset, lazy loading)

---

## 👥 Segmentation des tâches

### 1. Chef de Projet (3h)

**Responsabilité** : Planification, veille design, validation

- [x] Analyser les tendances web design 2026 (Dribbble, Awwwards, TailwindUI)
- [x] Définir 3 templates prioritaires : "modern", "minimal", "corporate"
- [x] Créer les wireframes (description textuelle, pas besoin de Figma pour MVP)
- [x] Rédiger les specs techniques (ce document)
- [x] Mettre à jour `docs/TODO.md` et `docs/boite-a-idees.md`
- [ ] Valider les livrables des agents (templates, code Django)
- [ ] Tester l'UX sur mobile et desktop
- [ ] Mettre à jour les logs (`docs/logs/log-projet.md`)

**Livrables** :
- ✅ Wireframes (descriptions dans ce document)
- ✅ Specs techniques (ce document)
- ⏳ Validation finale (après développement)

---

### 2. Développeur Django (4h)

**Responsabilité** : Backend et logique métier

- [ ] Modifier le modèle `LandingPage` dans `apps/landing_pages/models.py` :
  ```python
  TEMPLATE_CHOICES = [
      ('default', 'Default (basique)'),
      ('modern', 'Modern (startup tech)'),
      ('minimal', 'Minimal (agence design)'),
      ('corporate', 'Corporate (B2B traditionnel)'),
  ]
  template_key = models.CharField(
      max_length=80,
      default='default',
      choices=TEMPLATE_CHOICES,
      help_text="Template de design à utiliser"
  )
  ```
- [ ] Créer la migration de base de données : `python manage.py makemigrations`
- [ ] Modifier `apps/landing_pages/views.py` pour sélectionner le bon template :
  ```python
  def landing_page_detail(request, slug):
      landing_page = get_object_or_404(LandingPage, slug=slug, is_published=True)
      template_name = f"landing_pages/{landing_page.template_key}.html"
      # Fallback vers default si template n'existe pas
      return render(request, template_name, {...})
  ```
- [ ] Ajouter le champ `template_key` dans `apps/landing_pages/admin.py` (fieldsets)
- [ ] Écrire les tests unitaires dans `apps/landing_pages/tests/` :
  - Test de sélection de template
  - Test de fallback vers default
  - Test de validation des choices
- [ ] Exécuter les tests : `PYTHONPATH=".:apps" python3 -m pytest apps/landing_pages/ -v`

**Livrables** :
- Code Python (models, views, admin)
- Migration de base de données
- Tests unitaires (couverture > 80%)

**Dépendances** :
- ✅ Specs du Chef de Projet (terminées)
- ⏳ Templates HTML du Designer (parallèle)

**Estimation** : 4h (1h modèle + 1h vues + 1h admin + 1h tests)

---

### 3. Designer UI/UX (10h)

**Responsabilité** : Templates HTML/CSS et expérience utilisateur

#### 3.1. Setup Tailwind CSS (1h)
- [ ] Ajouter Tailwind CSS via CDN dans `templates/base.html` (ou créer base commune) :
  ```html
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            primary: '#3b82f6',
            secondary: '#8b5cf6',
          }
        }
      }
    }
  </script>
  ```
- [ ] Documenter le choix (CDN vs build) dans `docs/base-de-connaissances/decisions.md`

#### 3.2. Template "modern.html" (3h)
- [ ] Créer `templates/landing_pages/modern.html`
- [ ] Hero section avec gradient animé (Tailwind gradients)
- [ ] Features grid (3 colonnes, icônes emoji ou SVG)
- [ ] Testimonials section (cards avec ombre)
- [ ] CTA final (bouton large, couleur vive)
- [ ] Footer (liens, copyright)
- [ ] Responsive mobile (menu hamburger, stack vertical)

#### 3.3. Template "minimal.html" (3h)
- [ ] Créer `templates/landing_pages/minimal.html`
- [ ] Hero section minimaliste (typographie grande, espaces blancs)
- [ ] Features en liste verticale (asymétrique)
- [ ] Testimonials en texte simple (pas de cards)
- [ ] CTA discret (lien souligné ou bouton outline)
- [ ] Footer minimaliste
- [ ] Responsive mobile

#### 3.4. Template "corporate.html" (2h)
- [ ] Créer `templates/landing_pages/corporate.html`
- [ ] Hero section classique (image + texte à gauche)
- [ ] Features grid (2 colonnes, icônes sobres)
- [ ] Logos clients (grid 4 colonnes, grayscale)
- [ ] Formulaire de contact (nom, email, message)
- [ ] Footer complet (liens multiples, mentions légales)
- [ ] Responsive mobile

#### 3.5. Composants réutilisables (1h)
- [ ] Documenter les composants dans `docs/base-de-connaissances/composants-ui.md` :
  - Structure HTML de chaque composant
  - Classes Tailwind utilisées
  - Variables `content_json` nécessaires
  - Exemples d'utilisation

**Livrables** :
- 3 templates HTML/CSS (modern, minimal, corporate)
- Documentation des composants
- Tests manuels sur mobile/desktop (screenshots)

**Dépendances** :
- ✅ Wireframes du Chef de Projet (terminés)
- ⏳ Code Django du Développeur (parallèle, pas bloquant)

**Estimation** : 10h (1h setup + 3h modern + 3h minimal + 2h corporate + 1h doc)

---

### 4. Rédacteur (3h)

**Responsabilité** : Contenus et SEO

- [ ] Rédiger les contenus pour chaque template (exemples `content_json`) :
  - `modern_example.json` : startup tech (ton dynamique, innovant)
  - `minimal_example.json` : agence design (ton élégant, créatif)
  - `corporate_example.json` : B2B traditionnel (ton sérieux, rassurant)
- [ ] Appliquer les bonnes pratiques éditoriales (`docs/bonnes-pratiques.md`) :
  - Humanisation (pas de "révolutionnaire", "cutting-edge")
  - Variété syntaxique (phrases courtes et longues)
  - Ton adapté à la cible
- [ ] Créer un guide des variables dynamiques dans `docs/base-de-connaissances/variables-content-json.md` :
  - Liste des champs disponibles
  - Exemples de valeurs
  - Bonnes pratiques (longueur des titres, etc.)
- [ ] Optimiser pour le SEO :
  - Meta descriptions (150-160 caractères)
  - Titres H1 avec mots-clés
  - Alt text pour images
- [ ] Valider l'orthographe et la grammaire (LanguageTool)

**Livrables** :
- 3 fichiers JSON d'exemple (contenus rédigés)
- Documentation des variables `content_json`
- Checklist SEO

**Dépendances** :
- ✅ Specs du Chef de Projet (terminés)
- ⏳ Templates du Designer (pour adapter les contenus)

**Estimation** : 3h (1h par template + 1h doc)

---

### 5. Data Analyst (2h)

**Responsabilité** : Préparation du tracking analytics

- [ ] Définir les événements à tracker :
  - Page view (par template)
  - Clic sur CTA principal
  - Clic sur CTA final
  - Soumission de formulaire (si applicable)
  - Temps passé sur la page
- [ ] Créer un dashboard analytics (Jupyter notebook ou Django admin custom) :
  - Taux de conversion par template
  - Temps de chargement moyen
  - Taux de rebond
- [ ] Documenter les KPIs dans `docs/base-de-connaissances/kpis-landing-pages.md`
- [ ] Préparer les requêtes SQL pour extraire les données (PostgreSQL)

**Livrables** :
- Liste des événements à tracker
- Dashboard analytics (mockup ou code)
- Documentation des KPIs

**Dépendances** :
- ⏳ Déploiement en staging (pour collecter les données réelles)

**Estimation** : 2h (1h définition événements + 1h dashboard)

---

### 6. Growth Hacker (1h)

**Responsabilité** : Automation et génération de contenus (future)

- [ ] Documenter le workflow n8n pour générer les `content_json` automatiquement :
  - Input : données prospect (nom, entreprise, secteur)
  - Processing : appel à Flowise (LLM) pour générer les contenus
  - Output : `content_json` prêt à injecter dans Django
- [ ] Créer un workflow n8n de test (sans LLM, juste des templates statiques)
- [ ] Exporter le workflow en JSON : `docs/n8n-workflows/generate-landing-content.json`

**Livrables** :
- Documentation du workflow n8n
- Workflow de test (export JSON)

**Dépendances** :
- ✅ Specs des `content_json` (terminées)
- ⏳ Templates du Designer (pour tester)

**Estimation** : 1h (documentation + workflow simple)

---

### 7. DevOps (2h)

**Responsabilité** : Infrastructure et déploiement

- [ ] Vérifier que les nouveaux templates sont inclus dans le build Docker :
  - `templates/landing_pages/` doit être copié dans l'image
  - Vérifier le `COPY` dans `docker/Dockerfile.web`
- [ ] Tester le build local : `make build && make up`
- [ ] Déployer sur staging (Vercel ou Contabo) :
  - Pousser sur branche `staging`
  - Vérifier le déploiement automatique
  - Tester les 3 templates sur staging
- [ ] Tester les performances (Lighthouse) :
  - Performance > 90
  - Accessibility > 90
  - Best Practices > 90
  - SEO > 90
- [ ] Créer un rapport de performances : `docs/rapports/lighthouse-templates-2025-01-30.md`
- [ ] Déployer en production (après validation du Chef de Projet)

**Livrables** :
- URL de staging (ex: https://lppp-staging.vercel.app)
- Rapport Lighthouse (screenshots)
- URL de production (après validation)

**Dépendances** :
- ⏳ Code Django du Développeur (terminé)
- ⏳ Templates du Designer (terminés)
- ⏳ Validation du Chef de Projet (bloquant pour prod)

**Estimation** : 2h (1h staging + 1h tests Lighthouse)

---

## 🔄 Dépendances et ordre d'exécution

### Phase 1 : Planification (séquentiel) ✅ TERMINÉ
1. **Chef de Projet** → Wireframes et specs (bloquant pour les autres)

### Phase 2 : Développement (parallèle) 🟡 EN COURS
2. **Designer** → Templates HTML/CSS (10h)
3. **Développeur Django** → Modèles et vues (4h)
4. **Rédacteur** → Contenus (3h)
5. **Data Analyst** → Préparation analytics (2h)
6. **Growth Hacker** → Documentation workflow (1h)

**Durée estimée Phase 2** : 2 jours (avec parallélisation)

### Phase 3 : Intégration (séquentiel)
7. **Développeur Django** → Intégrer les templates et contenus (1h)
8. **Développeur Django** → Exécuter les tests (30min)

### Phase 4 : Validation (séquentiel)
9. **Chef de Projet** → Valider les livrables (1h)
10. **Chef de Projet** → Tester l'UX mobile/desktop (1h)

### Phase 5 : Déploiement (séquentiel)
11. **DevOps** → Déployer sur staging (1h)
12. **Chef de Projet** → Valider sur staging (30min)
13. **DevOps** → Déployer en production (30min)

**Durée totale estimée** : 3-4 jours (avec parallélisation optimale)

---

## ✅ Critères de validation

### Fonctionnel
- [ ] Les 3 templates s'affichent correctement (modern, minimal, corporate)
- [ ] Le champ de sélection fonctionne dans l'admin Django
- [ ] Les contenus dynamiques (`content_json`) sont bien injectés dans chaque template
- [ ] Le responsive fonctionne (mobile, tablette, desktop)
- [ ] Fallback vers `default.html` si template non trouvé

### Performance
- [ ] Temps de chargement < 2s (Lighthouse Performance > 90)
- [ ] Score accessibilité > 90 (WCAG 2.1, Lighthouse Accessibility)
- [ ] Pas d'erreurs console JavaScript
- [ ] Images optimisées (lazy loading, srcset)

### Qualité
- [ ] Tests unitaires passent (couverture > 80%)
- [ ] Pas de linter errors (flake8, black, isort)
- [ ] Documentation à jour (README, base de connaissances)
- [ ] Code review passée (si applicable)

### Éditorial
- [ ] Contenus appliquent les bonnes pratiques (`docs/bonnes-pratiques.md`)
- [ ] Orthographe et grammaire validées (LanguageTool)
- [ ] SEO optimisé (meta descriptions, H1, alt text)
- [ ] Ton adapté à chaque template (modern = dynamique, minimal = élégant, corporate = sérieux)

---

## 📊 Suivi de l'avancement

| Agent | Statut | Avancement | Bloqueurs | ETA |
|-------|--------|------------|-----------|-----|
| Chef de Projet | 🟢 Terminé | 100% | — | — |
| Développeur Django | ⚪ Pas démarré | 0% | — | J+1 |
| Designer | ⚪ Pas démarré | 0% | — | J+2 |
| Rédacteur | ⚪ Pas démarré | 0% | — | J+1 |
| Data Analyst | ⚪ Pas démarré | 0% | — | J+2 |
| Growth Hacker | ⚪ Pas démarré | 0% | — | J+1 |
| DevOps | ⚪ Pas démarré | 0% | Attend validation | J+3 |

**Légende** :
- ⚪ Pas démarré
- 🟡 En cours
- 🟢 Terminé
- 🔴 Bloqué

---

## 📝 Notes et décisions

### Décisions prises
- **2025-01-30** : Utiliser Tailwind CSS via CDN pour démarrage rapide (build optimisé plus tard si besoin)
- **2025-01-30** : Créer 3 templates initialement (modern, minimal, corporate), ajouter d'autres plus tard selon les besoins
- **2025-01-30** : Pas d'Alpine.js pour le MVP (ajouter plus tard si besoin de micro-interactions JS)
- **2025-01-30** : Formulaire de contact uniquement dans template "corporate" (pas dans modern/minimal pour MVP)

### Risques identifiés
- **Risque 1** : Tailwind CSS via CDN peut alourdir le temps de chargement (300KB)
  - **Mitigation** : Passer à un build optimisé (purge CSS) en Phase 2 si nécessaire
- **Risque 2** : Responsive complexe sur certains templates (minimal asymétrique)
  - **Mitigation** : Mobile-first, tester sur vrais devices (pas juste DevTools)
- **Risque 3** : `content_json` peut devenir complexe avec beaucoup de champs
  - **Mitigation** : Documenter clairement les variables, créer des exemples

### Questions en suspens
- ❓ Faut-il permettre la personnalisation des couleurs par landing page (override Tailwind config) ?
  - **Réponse** : Non pour MVP, ajouter en Phase 2 si demandé
- ❓ Doit-on créer un preview mode avant publication ?
  - **Réponse** : Oui, à ajouter dans TODO (priorité moyenne)

---

## 🔗 Références

- **Tendances web design 2026** :
  - [Awwwards](https://www.awwwards.com/) (sites primés)
  - [Dribbble](https://dribbble.com/tags/landing-page) (designs landing pages)
  - [TailwindUI](https://tailwindui.com/components/marketing/sections/heroes) (composants Tailwind)
- **Documentation technique** :
  - `docs/bonnes-pratiques.md` (éditorial anti-détection IA)
  - `docs/base-de-connaissances/agents-roles-responsabilites.md` (matrice RACI)
- **Code de référence** :
  - SquidResearch : `/home/lucas/tools/squidResearch` (templates, composants)

---

*Document maintenu par le Chef de Projet. Dernière mise à jour : 2025-01-30.*
