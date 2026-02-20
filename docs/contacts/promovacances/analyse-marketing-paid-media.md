# Analyse marketing — Paid media Promovacances

Synthèse des signaux paid (Google Ads, Meta) à partir des données publiques. Source : Centre de transparence Google Ads, Bibliothèque publicitaire Meta. Dernière mise à jour : 2026.

---

## 1. Sources vérifiables

| Source | URL / accès | Données disponibles |
|--------|-------------|---------------------|
| Google Ads Transparency | [adstransparency.google.com](https://adstransparency.google.com) | Annonceur, domaine, volume annonces, formats, fourchettes d’impressions, périodes |
| Meta Ad Library | Bibliothèque publicitaire Meta (France) | Ciblage déclaré, couverture estimée par âge/genre, créas, dates de diffusion |
| API / BigQuery | Si export disponible | Analyse à l’échelle (formats, volumes, périodes, domaines) |

**Limites** : Meta ne révèle pas lookalike, retargeting, ni objectif de campagne (clics vs conversions).

---

## 2. Google Ads — faits observés

- **Annonceur** : Karavel SAS (domaine promovacances.com)
- **Volume** : ~3 000 annonces (région France)
- **Format** : texte, thème « Voyage et tourisme »

### Exemples (Centre de transparence Google)

| Thème | Impressions | Période | Dernière diffusion |
|-------|-------------|---------|--------------------|
| Sardaigne | 800k – 900k | 4 avr. 2023 → 21 nov. 2025 | 19 févr. 2026 |
| All inclusive | 100k – 125k | 25 nov. 2024 → 21 nov. 2025 | 19 févr. 2026 |

**Lecture** : PPC très structuré, thèmes destination/offre en rotation longue durée (2023 → 2026), volume compatible avec une approche template / feed / automatisée.

---

## 3. Meta (Facebook / Instagram) — faits observés

- **Ciblage déclaré** : France, 18–65+, tous genres (large / algo-driven)
- **Sujets** : offres (destinations, clubs, tout inclus, promos), variantes multiples (1/4, 1/6…)

### Exemples de couverture (estimation Meta)

| Pub | ID | Couverture | Note |
|-----|-----|------------|------|
| « Des séjours faciles, fiables… » | 1961864931426132 | ~129 330 | — |
| Émirats -30% (vidéo 0:15) | variante | — | Répartition âge : ~57 % reach en 65+ |
| Nouveau Club Framissima Grèce | 1253005116786186 | ~5 747 | Active 6h au moment de capture |

### Framissima Grèce — répartition diffusion estimée

- **45–54** : ~21 %
- **55–64** : ~26 %
- **65+** : ~23 %
- **45+ total** : ~70 %
- **Genre** : ~66 % femmes

---

## 4. Hypothèses (non vérifiables sans accès compte)

1. **Broad ≠ hasard** : avec un ciblage large, l’algo optimise la diffusion selon objectif (clic, LPV, achat) et réactions.
2. **Sur-représentation 45+ / 65+** : peut venir du message (club 5★, sérénité, bord de plage) plus que d’un ciblage explicite.
3. **65+ et « faux clics »** : risque possible selon placements/device ; à valider via LPV/CVR/CPA par âge et placements, pas par exclusion systématique.
4. **Segmenter par créa plutôt que par audience** : garder broad pour l’apprentissage, différencier messages (ex. Ibiza/Goa vs sérénité vs famille) plutôt que ciblage âge trop serré.
5. **Google Ads** = capture de demande (requêtes, intention, mots-clés) ; **Meta** = génération de demande (offres, créas, test & learn).

---

## 5. Pistes pour approfondir

- **Google** : mots-clés payants, variations d’annonces, positions, concurrence (outils de paid research).
- **Meta** : analyse créas (promo vs brand), rotation, cohérence landing (bit.ly, promesse, conversion), LPV/clic et CVR/CPA par âge si données disponibles.
- **Objectif de campagne Meta** : clics vs conversions — détail qui change le diagnostic, non visible dans la bibliothèque.

---

## 6. Références

- Google Ads Transparency Center : <https://adstransparency.google.com>
- Meta Ad Library : recherche par annonceur « Promovacances » ou domaine promovacances.com
