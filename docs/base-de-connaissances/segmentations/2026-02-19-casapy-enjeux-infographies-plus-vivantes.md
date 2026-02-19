# Casapy — Enjeux : infographies plus vivantes (fond transparent, panel visuel)

**Date** : 2026-02-19  
**Demandeur** : utilisateur  
**Statut** : 🟡 En attente évaluation Chef de Projet + Architecte

---

## 📋 Contexte

La section **« Voici comment illustrer les enjeux pour une lecture immédiate »** sur la landing Casapy affiche aujourd’hui les 4 points en texte + les infographies PNG (slide1–4, one-pager). L’utilisateur souhaite :

1. **Plus vivant** : infographies de qualité type **Madpot Lib** (référence qualité visuelle)
2. **Fond transparent** : conserver le background de la page, pas de fond opaque
3. **Panel visuel** : évaluer si des bibliothèques **JavaScript ou React** peuvent permettre un panel plus visuel et interactif pour ces infographies

---

## 🎯 Contenu à contextualiser (4 enjeux)

1. **Impact perf → business** : Serveur → TTFB 3,7 s → LCP 32 s → UX dégradée → perte conv. -30 % → ≈ 54 k€/mois (10 k visites × 2 % × 900 € × 30 %).
2. **Diagnostic technique** : Waterfall TTFB vs Front — le goulot est le serveur. Jauges : TTFB 3,7 s / objectif < 0,8 s ; LCP 32 s / objectif < 2,5 s.
3. **Hébergement** : Mutualisé (risque élevé) vs stack adaptée WooCommerce (VPS, Redis, DB optimisée, perf stable).
4. **SEO & Growth** : Matrice Urgence/Impact (quick wins, structurant, à clarifier) + timeline 30/60/90 j.

---

## 👥 Rôles impliqués

| Rôle | Mission |
|------|---------|
| **Graphiste / Infographiste** | Créer ou adapter les infographies (style Madpot Lib), fond transparent |
| **Rédacteur en chef** | Rendre le texte plus vivant, contextualiser, accroche |
| **Chef de Projet** | Prioriser, valider le brief, coordonner livrables |
| **Architecte** | Évaluer la faisabilité d’un panel JS/React pour un affichage plus visuel ; impact stack, intégration landing statique vs Django vs Next |

---

## ❓ Questions pour Chef de Projet + Architecte

1. **Système actuel** : La landing Casapy est exportée en HTML statique (deploy/LPPP-Casapy) pour Vercel. Peut-on intégrer des bibliothèques JS/React (ex. D3.js, Chart.js, Recharts, ou composants React) pour un panel infographies plus visuel ?
2. **Contraintes** : 
   - Page statique (pas de build Node/React côté Vercel si Framework = Other)
   - Option : vanilla JS + librairies CDN (D3, Chart.js, etc.) → pas de build
   - Option : composant React/Next embarqué → nécessite Framework Next.js ou build
3. **Recommandation** : Quelle approche privilégier (vanilla JS + CDN vs intégration Next/React) pour rester cohérent avec la stack et le déploiement Vercel ?

---

## 📁 Fichiers concernés

- `docs/contacts/casapy/landing-proposition-casapy.json` (enjeux_lead, pain_points)
- `templates/landing_pages/proposition.html` (section enjeux, infographics)
- `docs/contacts/casapy/` (slide*.png, infographie*.html — à refaire avec fond transparent si besoin)
- `scripts/generate_visuels_casapy.py` (Matplotlib — option `transparent=True` pour export PNG)
- `deploy/LPPP-Casapy/` (export statique)

---

## 📝 Notes

- Référence qualité : **Madpot Lib** (à documenter ou retrouver pour alignement style)
- Infographies actuelles : PNG opaques générés par Matplotlib ; possibilité d’exporter en PNG/SVG avec fond transparent
- Brief Infographiste : `docs/base-de-connaissances/brief-infographiccraft.md`, règle `infographiste-dataviz.mdc`

---

*Segmentation créée suite à demande utilisateur. À traiter par Chef de Projet et Architecte.*
