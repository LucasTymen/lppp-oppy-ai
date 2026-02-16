# Référentiel des landing pages (code et migrations)

**Rôle** : Source de vérité pour **quelles landing pages existent dans le code** (migrations, commandes `create_landing_*`) et leurs **secteur / catégorie**. Utile après une réinitialisation de base : savoir quoi recréer et avec quelles valeurs.

**Modèle** : `LandingPage` — champs `sector`, `category` (voir `apps/landing_pages/models.py` pour les choix).

---

## 1. Secteurs (SECTOR_CHOICES)

| Valeur | Libellé |
|--------|---------|
| `cybersecurite` | Cybersécurité / OT-IT |
| `juridique` | Juridique / Cabinets avocats |
| `industrie` | Industrie |
| `low-tech` | Low tech / Sans tech |
| `mairie` | Mairie / Collectivités territoriales |
| `autre` | Autre |

*(Le modèle n’inclut pas `formation` ; la commande ORSYS utilise `formation` — à ajouter aux choices si besoin.)*

---

## 2. Catégories (CATEGORY_CHOICES)

| Valeur | Libellé |
|--------|---------|
| `relance-evenement` | Relance événement |
| `proposition` | Proposition / Mission |
| `lead-magnet` | Lead magnet |
| `lowtech` | Low tech / Sans tech |
| `autre` | Autre |

---

## 3. Landing pages recréées par les migrations (déjà en base après `migrate`)

| Slug | Titre | Secteur | Catégorie | Template |
|------|-------|---------|-----------|----------|
| `maisons-alfort` | Conciergerie IA Maisons-Alfort (élus) | autre | autre | concierge_maisons_alfort |
| `yuwell-portfolio` | Portfolio Yuwell — étude graphique | autre | proposition | proposition |

---

## 4. Landing pages recréables via commandes (si le JSON existe)

| Slug | Commande | Secteur | Catégorie | Fichier JSON attendu |
|------|----------|---------|-----------|------------------------|
| `p4s-archi` | `create_landing_p4s` | cybersecurite | proposition | `docs/contacts/p4s-archi/landing-proposition-joel.json` |
| `0flow` | `create_landing_0flow` | cybersecurite | proposition | `docs/contacts/0flow/landing-proposition-samson.json` |
| `orsys` | `create_landing_orsys` | formation | proposition | `docs/contacts/orsys/landing-proposition-aboubakar.json` |
| `lazaregue-avocats` | `create_landing_lazaregue` | juridique | proposition | `docs/contacts/lazaregue-avocats/landing-proposition-sarah.json` |
| `fitclem` | `create_landing_fitclem` | autre | proposition | `docs/contacts/fitclem/landing-proposition-fitclem.json` |

**Exemple (WSL, depuis la racine du projet) :**
```bash
docker compose exec web python manage.py create_landing_p4s --publish
docker compose exec web python manage.py create_landing_0flow --publish
docker compose exec web python manage.py create_landing_orsys --publish
docker compose exec web python manage.py create_landing_lazaregue --publish
docker compose exec web python manage.py create_landing_fitclem --publish
```

*(Si le fichier JSON manque, la commande affiche une erreur et ne crée pas la landing.)*

---

## 5. Dossiers contacts (registre)

Les dossiers sous `docs/contacts/<slug>/` et le **registre** `docs/contacts/REGISTRE-CONTACTS.md` listent les **contacts** (p4s-archi, ackuracy, orsys, 0flow, lazaregue-avocats, mairies, fitclem, etc.). Tous n’ont pas une commande `create_landing_*` : seuls ceux listés en § 4 ont une commande dédiée. Les autres landings (ackuracy, green-communications, etc.) devraient être créées à la main dans l’admin ou via une commande générique si elle existe.

---

*Document créé pour retrouver les landings et leurs catégories après réinitialisation de la base. Dernière mise à jour : 2026-01-30.*
