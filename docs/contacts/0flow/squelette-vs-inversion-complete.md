# 0flow — Squelette vs inversion complète

**Objectif** : Savoir où on en est (squelette) et ce qu’il faut pour livrer la **version complète** (inversion complète = page prête à envoyer au prospect).

Référence projet : `docs/base-de-connaissances/reconstitution-landing-p4s-personnalisation.md`, `strategie-qualite-contenu-landings.md`.

---

## 1. Squelette (état actuel typique)

| Élément | État squelette |
|--------|-----------------|
| **Contenu** | JSON rempli (hero, enjeux, services, stack, CTA) → sections visibles. |
| **Thème visuel** | **Aucun** thème 0Flaw → fallback **style perso** (Inter, indigo/violet, dégradé générique). Le prospect ne voit pas l’univers 0Flaw. |
| **Hero** | Pas d’image de fond cible → dégradé générique ou style perso. |
| **Logo** | Pas de logo 0Flaw. |
| **Démo Loom** | `loom_embed_url` vide → section « Démo 60 sec » absente ou masquée. |
| **Rapport** | `rapport_url` vide → pas de lien « Consulter le rapport » / téléchargement. |
| **Impression** | Page « correcte » mais **générique** : on sent que c’est une landing type, pas une page pensée pour 0Flaw. |

---

## 2. Inversion complète (ce que ça donne quand tout est fait)

| Élément | État inversion complète |
|--------|--------------------------|
| **Contenu** | Idem : JSON complet, sections remplies, ton aligné 0Flaw (voir `style-voix-et-design-0flaw.md`). |
| **Thème visuel** | **CSS Vampire** exécuté sur https://0flaw.fr/ → **couleurs, polices, logo 0Flaw** injectés dans la page. Le prospect se retrouve dans son univers. |
| **Hero** | Dégradé ou image issue du thème 0Flaw (selon ce que CSS Vampire extrait). |
| **Logo** | Logo 0Flaw affiché (nav + hero si template le prévoit). |
| **Démo Loom** | `loom_embed_url` renseigné → section « Démo 60 sec » visible avec iframe Loom. |
| **Rapport** | `rapport_url` renseigné → CTA « Télécharger mon rapport » ou « Consulter le rapport » fonctionnel. |
| **Impression** | Page **finale** : personnalisée, crédible, prête à envoyer (lien, QR code, entretien). |

---

## 3. Checklist : passer du squelette à l’inversion complète

À faire **dans cet ordre** (le thème est conservé lors des mises à jour suivantes) :

| # | Action | Commande / Fichier |
|---|--------|---------------------|
| 1 | Mettre le contenu en base (JSON → Django) | `python3 manage.py create_landing_0flow --update` (et `--publish` si besoin). |
| 2 | **Appliquer le thème 0Flaw** (couleurs, polices, logo) | `python3 manage.py css_vampire https://0flaw.fr/ --slug 0flow --apply` |
| 3 | Renseigner la démo Loom (optionnel) | Mettre `loom_embed_url` dans `landing-proposition-samson.json`, puis `create_landing_0flow --update`. |
| 4 | Renseigner le rapport (optionnel) | Mettre `rapport_url` dans le JSON (ou en base), puis `create_landing_0flow --update`. |
| 5 | Vérifier le rendu | Ouvrir `http://localhost:8000/p/0flow/` (sans cache). Vérifier : thème 0Flaw, logo, CTA, lien rapport. |
| 6 | Export statique (si déploiement standalone) | `python3 manage.py export_landing_static 0flow --output <chemin>/index.html` → même rendu qu’en Django. |

Après l’étape 2, **ne pas** refaire CSS Vampire à chaque mise à jour de contenu : `create_landing_0flow --update` préserve `theme` et `theme_css`.

---

## 4. En résumé

- **Squelette** = contenu OK, **style générique** (pas de thème 0Flaw, pas de logo, pas de démo/rapport liés).
- **Inversion complète** = contenu OK + **thème 0Flaw** (CSS Vampire) + **optionnel** démo Loom + lien rapport + vérif visuelle.

Le **levier principal** pour « inverser » est **CSS Vampire** sur https://0flaw.fr/ ; le reste (Loom, rapport) renforce la crédibilité et l’action.

---

*Dernière mise à jour : 2026-01-30.*
