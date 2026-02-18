# Casapy — Assets et spécifications mise en forme

**Date** : 2026-01-30  
**Usage** : logo et vidéo hero pour rapport synthétique, landing ou toute mise en forme Casapy.

---

## Logo

- **URL** : https://www.casapy.com/wp-content/uploads/2025/04/logo-casapy-HD-1.pdf-1.png  
- Utilisation : header, rapport, supports de présentation.

---

## Vidéo de fond (hero section)

**Règle** : comme d’habitude — **uniquement sur la hero section**, derrière l’overlay avec scanlines, en **parallaxe**.

- **URL** : https://www.casapy.com/wp-content/uploads/2026/02/video-quali-55.mp4  
- **Comportement** : `autoplay`, `muted`, `playsinline`, `loop`  
- **Placement** : fond de la hero, derrière overlay + scanlines ; effet parallaxe au scroll.  
- **Référence technique** : même principe que FitClem / autres landings (`.hero.has-bg-video`, `.hero-bg-video`, overlay, scanlines).

**Exemple de balise (structure)** :

```html
<video class="elementor-background-video-hosted" role="presentation" autoplay muted playsinline loop
  src="https://www.casapy.com/wp-content/uploads/2026/02/video-quali-55.mp4"></video>
```

À intégrer dans le conteneur hero, derrière l’overlay (et scanlines si prévus), avec CSS parallaxe (position fixed ou transform selon la maquette).

---

## Référence mise en page

- **Deploy FitClem** : `deploy/LPPP-FitClem/index.html` — hero vidéo, `.hero.has-bg-video`, overlay, parallaxe.  
- Adapter pour Casapy (logo + vidéo ci-dessus).

---

*Document maintenu par Designer / Chef de Projet. Dernière mise à jour : 2026-01-30.*
