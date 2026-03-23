# Rougier & Ple — LPPP

**Société** : Rougier & Ple (RougierEtPle).  
**Objectif** : nouvelle landing LPPP pour prospecter Rougier & Ple.

## Contexte

- À compléter selon le secteur et l’offre (audit SEO, growth, acquisition, autre).
- Angle et contenu à définir avec les données du contact.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `landing-proposition-rougier-et-ple.json` | Contenu de la page proposition. |
| `rougier-et-ple_style_tokens.css` | Style dashboard (même charte qu'Infopro : fond sombre, accents vifs). |
| `infographie-rougier-et-ple-7-formats.html` | Infographie 7 formats (tachymètre, timeline, bullet, heatmap, waterfall, recovery). |
| `positionnement-marketing.html` | Page positionnement marketing (funnel AAARR, dashboard, PESTEL, etc.). |
| `funnel-aaarrr-rougier-et-ple.html` | Tunnel AAARRR (Pirate Funnel) intégré au style dark R&P ; intégré dans positionnement-marketing. |
| `forces-de-porter-analyse-concurrentielle.html` | Illustration étude concurrentielle + 6 forces de Porter (radar + cartes, marché papeterie & loisirs créatifs). |
| `README.md` | Ce fichier. |

## Accès à la landing

- **Page principale** (fallback depuis le JSON) : **http://localhost:8010/p/rougier-et-ple/**
- **Infographie 7 formats** : **http://localhost:8010/p/rougier-et-ple/assets/infographie-rougier-et-ple-7-formats.html**
- **Positionnement marketing** : **http://localhost:8010/p/rougier-et-ple/assets/positionnement-marketing.html**
- **Forces de Porter (étude concurrentielle)** : **http://localhost:8010/p/rougier-et-ple/assets/forces-de-porter-analyse-concurrentielle.html** — ou ouvrir directement le fichier dans un navigateur.
- **Funnel AAARRR** : intégré dans la page Positionnement marketing ; standalone : **http://localhost:8010/p/rougier-et-ple/assets/funnel-aaarrr-rougier-et-ple.html**

Le template proposition (même structure qu’Infopro) reçoit `infographie_url` et `positionnement_marketing_url` pour les liens nav / CTA.

## Export statique (quand la landing est prête)

```bash
python3 manage.py export_landing_static rougier-et-ple --json docs/contacts/rougier-et-ple/landing-proposition-rougier-et-ple.json --output deploy/static-rougier-et-ple-vercel/index.html
```

## Références

- Template de départ : `docs/base-de-connaissances/template-landing-promovacances-base-depart.md`
- Savoir-faire : `docs/ressources-utilisateur/cv_base_datas_pour_candidatures.json`
