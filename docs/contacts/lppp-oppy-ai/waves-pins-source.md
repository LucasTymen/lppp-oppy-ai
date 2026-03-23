# Waves Pins — source et paramètres

**Source** : waves-pins-three-js (CodePen, Sabo Sugi)  
**Original** : https://codepen.io/sabosugi/pen/emzpagK  
**Licence** : MIT

## Implémentation LPPP-OppyAI

- **CodePen (optionnel)** : si `hero_codepen_url` est renseigné, il est **prioritaire** dans le template. Le thème Oppy applique un **clip bas** (~18 %) + iframe un peu plus haute pour **masquer la barre / console** d’embed CodePen ; la nav reste au-dessus (`z-index: 1000`).
- **Script local (recommandé, sans console)** : `hero_codepen_url: ""` + `hero_waves_pins: true` → `waves-pins-hero.js` (paramètres ci-dessous, animation plus ample / rapide / « random » que la version d’origine).
- **Three.js** : CDN jsDelivr (pour le script local)
- **Templates** : `proposition.html`, `proposition_value.html`

## Paramètres (settings)

| Paramètre    | Valeur    |
|-------------|-----------|
| Amplitude (`waveHeight`) | 6.4       |
| Frequency X | 0.42      |
| Frequency Z | 0.78      |
| Chaos Level (`chaosScale`) | 9.2       |
| Random wobble | 2.85   |
| Random speed mult. | 1.65 |
| Speed (base) | 0.034 (+ léger jitter temporel) |
| Gap         | 1.3224    |
| Dot Size    | 0.45441   |
| Dot Opacity | 0.769     |
| Line Length | 9.804     |
| Line Opacity| 0.449     |
| Line Growth | true      |
| Color Left  | #8612b7   |
| Color Right | #06777c   |
| Fog Color   | #070023   |
| Fog Density | 0.0185    |
| Cam X       | -3.7      |
| Cam Y       | 10.5      |
| Cam Z       | 15.147    |

## Fichiers zip d’origine

Conserver `waves-pins-three-js.zip` en référence (Downloads).
