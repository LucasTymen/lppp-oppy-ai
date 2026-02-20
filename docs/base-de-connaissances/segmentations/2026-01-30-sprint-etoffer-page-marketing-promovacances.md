# Sprint : Étoffer la page Positionnement marketing Promovacances

**Date** : 2026-01-30  
**Statut** : 🟡 En cours  
**Pilotes** : **Expert Mathématiques**, **Expert Marketing & Growth**, **Rédacteur en chef**, **Infographiste**

---

## 1. Objectif

Enrichir `docs/contacts/promovacances/positionnement-marketing.html` pour rendre le contenu plus accessible aux esprits mathématiques et moins rébarbatif, en :

- **Conservant** le texte créé par le Rédacteur en chef
- **Récupérant** les chiffres issus des sources (Google Ads, Meta Ad Library, diagnostic)
- **Montrant** les calculs et raisonnements (formules, démonstrations)
- **Illustrant** par des infographies et diagrammes (templates du projet Promovacances / Casapy)

---

## 2. Rôles et responsabilités

| Rôle | Tâche | Livrable |
|------|-------|----------|
| **Expert Mathématiques** | Formules, ordres de grandeur, raisonnements (perte conversion, reach %, AOV, scénarios) | Blocs « Formules » et « Calculs » |
| **Expert Marketing & Growth** | Synthèse données ads, lecture des métriques (impressions, couverture, âge/genre), hypothèses chiffrées | Données structurées, tableaux, légendes |
| **Rédacteur en chef** | Textes existants conservés ; phrases de liaison si besoin (anti-détection IA, humanisation) | Texte finalisé |
| **Infographiste** | Graphiques (barres âge, donut répartition, waterfall, bullet chart), cohérence charte Promovacances | HTML/CSS/SVG inline (promovacances_style_tokens.css) |

---

## 3. Données sources (extraction)

### 3.1 Google Ads (Centre de transparence)
- Annonceur : Karavel SAS (promovacances.com)
- ~3 000 annonces actives, France, thème Voyage
- Sardaigne : 800k–900k impressions, avr. 2023 → nov. 2025
- All inclusive : 100k–125k impressions, nov. 2024 → nov. 2025

### 3.2 Meta (Ad Library — promovacances_metaads_perfs.md)

| Pub | ID | Couverture | Répartition âge (calculée) |
|-----|-----|------------|---------------------------|
| « Des séjours faciles, fiables… » | 1961864931426132 | 129 330 | 18–24 : 1,2 % ; 25–34 : 9,7 % ; 35–44 : 22,5 % ; 45–54 : 26,2 % ; 55–64 : 24,3 % ; 65+ : 17,6 % → **45+ : 68 %** |
| Émirats -30 % (vidéo 15 s) | 1234405061351906 | 14 699 | **65+ : 58 %** ; 45+ cumulé : **86 %** |
| Émirats -30 % (image) | 1436448531319107 | 21 552 | **65+ : 38 %** ; 45+ : ~72 % |
| Club Framissima Grèce | 1253005116786186 | 5 747 | 45+ : **70 %** ; 55–64 : 26 % ; 65+ : 23 % ; ~66 % femmes |

### 3.3 Formules (spec-infographiques)
- **CA** = Visites × CVR × AOV
- **Perte** = Orders × p × AOV (p = % perte conversion)
- Ex. 30k visites, 1,5 % CVR, 1 200 €, perte 18 % → ~28 k€/mois

---

## 4. Templates à réutiliser

- `infographie-promovacances-7-formats.html` : speedometer, timeline, bullet chart, waterfall, recovery ring, heatmap
- `promovacances_style_tokens.css` : variables (--pv-blue, --pv-ink, --pv-gray-*)
- `spec-infographiques-visuel-contextuel-promovacances.md` : blocs priorités, chaîne, scénarios

---

## 5. Livrables attendus

- [ ] Page `positionnement-marketing.html` enrichie : chiffres, formules, infographies
- [ ] Conservation intégrale du texte Rédacteur en chef
- [ ] Blocs visuels : répartition âge (bar chart), volume Google vs Meta (donut ou barres), formules encadrées, scénarios CA/perte
- [ ] Sources citées (Google Ads Transparency, Meta Ad Library)
- [ ] Mise à jour `log-projet.md` si besoin

---

## 6. Références

- `docs/contacts/promovacances/positionnement-marketing.html`
- `docs/contacts/promovacances/promovacances_metaads_perfs.md`
- `docs/contacts/promovacances/promovacances-marketing-study-en.md`
- `docs/contacts/promovacances/spec-infographiques-visuel-contextuel-promovacances.md`
- `docs/contacts/promovacances/PROMOVACANCES_DIAGNOSTIC_20260219.md`
- `docs/contacts/casapy/infographie-funnel-positionnement-casapy.html` (chaîne, matrice)
