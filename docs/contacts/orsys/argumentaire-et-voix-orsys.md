# Argumentaire et voix ORSYS — Brief Rédaction & Design

**Pour** : Rédacteur, Designer.  
**Objectif** : Aligner tout contenu ORSYS (landing, rapport, relances) sur des **données terrain**, pas du marketing. **Approche** : reprise de contact après un échange agréable au salon — proposer ce qu’on sait faire sans pression, pas de spam ni d’approche lourde.

**Structure « offensive »** (éviter catalogue froid) : (1) **Promesse choc** en header (ex. « Et si vous connaissiez les besoins formation avant qu'ils vous appellent ? ») ; (2) **Diagnostic « Fuite de cash »** visuel (chiffres : 40 % invisible, manque à gagner estimé) ; (3) **Cas d'usage concrets** (Radar levées, Alerte stack, IA Act) au lieu d'une liste de « services » ; (4) **Offre POC** type « Pack Commando — 5 jours » (zéro risque, livrables clairs). Ton : percutant en 30 s, pas « je fais du SEO » mais « je transforme vos données techniques en CA ».

**Référence complète** : `rapport-complet-orsys.md` (PESTEL, Porter, SWOT, concurrence, script).

---

## Contexte à garder en tête

- **Février 2026** : marché de la formation en consolidation (« la grande purge »). Entreprises ne financent plus que le **Business Critical**.
- **CPF** bridé, subventions OPCO en baisse → bascule B2C → **B2B Pur** (Plans de développement des compétences).
- **Opportunité** : IA Act européen (former DPO/RSSI), restructurations, FNE-Formation = budgets captables.
- **À ne pas dire** : « faire du marketing », « génération de leads » sans préciser *quels* signaux (restructuration, conformité, levées de fonds, changement de stack).

---

## Message central (script contrat)

> *« Mon script ne cherche pas “qui recrute”, il cherche “qui lève des fonds” ou “qui change de stack technique”. On va utiliser l’automatisation pour aller chercher les budgets de **restructuration** et de **conformité IA Act**. Je vous apporte une **machine de guerre** pour détecter les **signaux faibles** là où vos concurrents attendent que le téléphone sonne. »*

À décliner en : hero, mission_flash, solution_workflow, CTA (sans copier-coller brut — adapter au support).

---

## Vocabulaire à privilégier

| À utiliser | À éviter |
|-----------|----------|
| Signaux faibles, données terrain, automatisation (coûts d’acquisition) | Marketing, génération de leads (vague) |
| Restructuration, conformité IA Act, FNE-Formation, Plans de développement des compétences | CPF, recrutement (seul angle) |
| Machine de guerre, prévoir qui va licencier/pivoter, budgets captables | Liste de prospects, cold outreach |
| Business Critical, B2B Pur | B2C, volume pour le volume |

---

## À faire côté rédaction

- **Landing** : hero, intro, mission_flash, solution_workflow et seo_resume doivent refléter **signaux faibles** + **restructuration / conformité IA Act** (voir `landing-proposition-aboubakar.json` mis à jour).
- **Rapport** : garder le ton « analyse réalité 2026 », pas prospectus. C’est **ce qu’on leur propose** — PESTEL, Porter, SWOT, concurrence, script.
- **Lettre d’accompagnement** (mail qui envoie le rapport) : utiliser le modèle `lettre-accompagnement-rapport-orsys.md`. **Ton** : reprise de contact agréable, « au cas où ça pourrait servir », pas de vente forcée ni de relance lourde. Court, humain, sans engagement. Garder le script / l’angle « signaux faibles » pour *si* la conversation va plus loin, pas dans le premier mail.
- **À développer** : les **3 types de signaux faibles** que le script peut détecter pour ORSYS (à sortir et intégrer en bloc réutilisable).

---

## À faire côté design

- **Style** : **charte orsys.fr extraite par CSS Vampire** (pas de thème perso). Source : `python manage.py css_vampire https://www.orsys.fr/` → thème injecté dans `apps/landing_pages/themes.py` (THEME_ORSYS, THEME_CSS_ORSYS). Analyse : fond bleu marine `#1a2d6b`, texte `#ffffff`, primaire magenta `#d81b60`, secondaire teal `#26a69a`, polices Lato (body et heading), logo `LOGO_ORSYS_FRA_2025.png` (Wikimedia). Pour réappliquer en base : `create_landing_orsys --update --publish` ou `css_vampire https://www.orsys.fr/ --slug orsys --apply`.
- Pas de survente visuelle (pas de « Waouh leads illimités »). Ton **pro**, sobre, data.
- Si callouts ou encadrés dans le rapport, utiliser pour : PESTEL impact ORSYS, script contrat, opportunité IA Act.
- **Graphique** (optionnel) : un petit visuel (courbe ou bloc CSS) montrant la perte liée au SEO / manque à gagner renforce l'argument pour un profil comme Aboubakar (chiffrage = argument n°1).

---

*Brief créé pour aligner rédaction et design sur l’analyse ORSYS février 2026. Dernière mise à jour : 2026-02.*
