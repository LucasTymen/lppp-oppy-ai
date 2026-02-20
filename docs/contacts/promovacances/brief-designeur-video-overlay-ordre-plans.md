# Brief Designer — Vidéo arrière-plan et overlay (ordre des plans)

**Pour** : Designer UI/UX (Graphiste)  
**Date** : 2026-01-30  
**Contexte** : Des sections de texte sont encore coupées ou masquées par la vidéo sur les pages Promovacances.

---

## Demande

Mettre la **vidéo en arrière-plan** et l’**overlay juste au-dessus**, de façon à ce qu’aucune section de texte ne soit coupée ou recouverte par la vidéo.

---

## Contraintes techniques

1. **Ordre des plans (z-index)**  
   - Vidéo : plan le plus bas (arrière-plan)  
   - Overlay : juste au-dessus de la vidéo (dégradé semi-transparent pour lisibilité)  
   - Contenu (texte, cartes, infographies) : toujours au-dessus de l’overlay, jamais masqué

2. **Stack attendu**  
   ```
   [vidéo fond] → z-index 0
   [overlay]    → z-index 0 (ou 1), même conteneur ou juste au-dessus
   [contenu]    → z-index 1+ (ou position: relative + z-index) — jamais coupé
   ```

3. **Fichiers concernés**  
   - `docs/contacts/promovacances/promovacances_style_tokens.css` : `.site-bg-fixed`, `.site-bg-video`, `.site-bg-overlay`, `.site-content`  
   - Pages : `positionnement-marketing.html`, `infographie-promovacances-7-formats.html`, `rapport.html`, `index.html`  
   - Templates : `templates/landing_pages/proposition.html` (si export index)

---

## Vérifications

- [ ] La vidéo reste en arrière-plan (100 % écran, `position: fixed`)  
- [ ] L’overlay couvre toute la zone vidéo et est bien au-dessus  
- [ ] Toutes les sections de texte sont lisibles et jamais coupées par la vidéo  
- [ ] Comportement cohérent sur toutes les pages (rapport, infographie, positionnement marketing, accueil)

---

*Référence : `brief-designeur-nav-video-logo.md`, `promovacances_style_tokens.css`.*
