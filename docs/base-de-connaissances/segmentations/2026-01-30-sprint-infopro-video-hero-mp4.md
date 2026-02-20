# Sprint — Infopro : vidéo hero MP4 (remplacement YouTube)

**Date** : 2026-01-30  
**Pilotes** : Infographiste, DevOps  
**Statut** : Terminé

## Contexte

Remplacement de la vidéo YouTube par une vidéo MP4 locale pour le fond hero de la landing Infopro. Éviter les problèmes YouTube (Erreur 153, blocage, dépendance externe).

**Important** : La vidéo `videoplayback.1771604396470.publer.com.mp4` (stockée dans promovacances) est destinée à **Infopro**, pas à Promovacances.

## Objectif

- Fond hero : vidéo MP4 locale
- Sans son (muted)
- Lecture en boucle infinie (loop)
- Pas d'outils de lecture (autoplay, playsinline)
- Tout automatique et infini

## Étapes

- [x] Création segmentation
- [x] Copier vidéo vers `docs/contacts/infopro/hero-infopro.mp4`
- [x] Mettre à jour `landing-proposition-infopro.json` (hero_video_mp4_url, vider hero_video_url)
- [x] Modifier export pour copier `hero-infopro.mp4` pour slug infopro
- [x] Régénérer export statique
- [x] Mise à jour log-projet, log-ia

## Notes

- **Infographiste** : livrables complémentaires (édition vidéo, overlays, etc.) possiblement non terminés avant crash — à vérifier si besoin.
- **Registre d'exécutions** : log-projet, log-ia et cette segmentation doivent rester à jour à chaque étape.

## Références

- Template `proposition.html` : priorité `hero_video_mp4_url` > `hero_video_url` (YouTube)
- Vidéo source : `docs/contacts/promovacances/videoplayback.1771604396470.publer.com.mp4`
