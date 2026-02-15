# Exploitation du JSON prospection low-tech

**Fichier** : `2026-01-30_prospection-commando-lowtech.json`  
**Usage** : base de données locale pour scripts de prospection, suivi CRM personnel, personnalisation emails/LinkedIn.

---

## Structure

| Section | Rôle |
|--------|------|
| **meta** | Stratégie (MISSION_THEN_CDI), zone_focus (Créteil, rayon 15 km, zones_couvertes), exclusions_strictes, valeurs_autorisees (mode_ciblage_principal). |
| **opportuniteEmbauche** | Objectif (CDI), stratégie d'entrée, délai 1–3 mois, alternance (Rocket School = levier secondaire). |
| **entreprises_ciblees** | Liste : `nom`, `ville`, `segment`, `mode_ciblage_principal`, `besoin`, `priorite`. Champs optionnels (enrichissement) : `decideur_cible`, `contact` (tel, web, email_pattern ou email_contact), `growth_hook`, `angle_relance`. |
| **plan_action_proof_of_value** | Durée standard 15 jours, preuves recommandées (scraping, audit SEO, tracking, automation). |

---

## Exploitation en code

- **mode_ciblage_principal** : adapter les templates (MISSION_THEN_CDI → message mission courte 15 j ; MISSION_THEN_ALTERNANCE → mentionner Rocket School).
- **besoin** : variable de personnalisation pour objets de mail / messages LinkedIn.
- **plan_action_proof_of_value.preuves_recommandees** : arguments techniques à injecter dans les propositions.

Exemple Python (filtrer priorités HAUTE) :

```python
import json
with open('2026-01-30_prospection-commando-lowtech.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
high = [e for e in data['entreprises_ciblees'] if e['priorite'] == 'HAUTE']
```

---

## Sécurité

Si le fichier est enrichi avec des contacts directs (noms, emails) : l’ajouter au `.gitignore` ou garder ces champs dans un fichier local non versionné.

**Stratégie correspondances** : utiliser ce JSON comme base pour enchaîner **audits SEO** → **prospects** → **correspondance besoin ↔ preuve**. Voir `docs/base-de-connaissances/strategie-automatisation-correspondances-prospection.md`.

*Référence : REGISTRE-RESSOURCES.md, segment lowtech / classification-landings-secteur-categorie.md.*
