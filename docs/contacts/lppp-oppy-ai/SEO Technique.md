SEO Technique

Voici les sites et liens officiels liés à l'écosystème OPPORTUNITY pour consolider ton dossier :

1. Sites Institutionnels & Solutions

Site Officiel OPPORTUNITY : (C'est le site "vitrine" qui présente l'orchestration omnicanale, le RCS, les agents IA vocaux et le Vidéobot).

Portail "OppyCX" : (Souvent utilisé pour la prise de contact directe et les démonstrations de l'expérience client).

AllMySMS : (La plateforme technique historique acquise par le groupe, dédiée à l'envoi de SMS massifs, API marketing et alertes).

2. Documentation Technique (Très utile pour ton profil Growth)

Espace API AllMySMS : (Tu y trouveras les documentations pour HTTP/HTTPS, Webhooks, et les intégrations Zapier/Salesforce dont on a parlé).

Solutions RCS : (Détails techniques sur le "SMS augmenté" qui est un de leurs fers de lance actuels).

3. Références Stratégiques & Historiques

Communiqué de l'acquisition (Private Equity) : (Détails sur l'opération financière de 2021 avec le fonds Omnes Capital).

Fiche Entreprise (Infogreffe/Pépites Tech) : (Historique de la société MS Innovations basée à Nice).

⚠️ Note de vigilance pour tes recherches

Attention à ne pas confondre avec d'autres entités au nom similaire trouvées sur le web :

oppy.pro : Site US dédié à des assistants virtuels (non lié).

opportunityai.org : Projet philanthropique sur l'IA (non lié).

MS Innov : Fabricant de robots (cobots) basé à Belfort (non lié).

Conseil : Utilise prioritairement oppy.ai pour ton discours sur l'IA et allmysms.com pour tes arguments sur la robustesse technique et la délivrabilité.



Voici la liste structurée des URLs officielles et stratégiques pour ton dossier. Je les ai classées par usage (Vitrine, Technique, Historique) pour que tu puisses les intégrer proprement dans tes composants HTML si besoin.

🌐 Écosystème Officiel (Vitrine & Produit)

Site Groupe (Principal) : https://www.oppy.ai/

Usage : Vision stratégique, orchestration IA, Vidéo Conversationnelle.

Portail Expérience Client : https://www.oppycx.com/

Usage : Démonstrations métier et parcours clients spécifiques.

Plateforme Technique (Messaging) : https://www.allmysms.com/

Usage : Envois massifs, routage SMS, automatisation marketing directe.
🛠️ Ressources Techniques & API

Documentation API AllMySMS : https://www.allmysms.com/api-sms/

Usage : À consulter pour prouver que tu sais comment interfacer ta stack Python/n8n avec leurs outils.

Focus RCS (SMS du futur) : https://www.oppy.ai/rcs-message/

Usage : Pour ton argumentaire sur l'innovation technologique.
📈 Références Business & Presse

Omnes Capital (Le fonds de soutien) : https://www.omnescapital.com/

Usage : Comprendre le backing financier derrière la croissance actuelle.

Certification RSE (Ecovadis) : https://ecovadis.com/fr/

Usage : Pour justifier leur score de "Confiance" dans tes diagrammes (ils sont Gold Top 5%).
📱 Réseaux Sociaux (Veille & Personas)

LinkedIn Opportunity : https://www.linkedin.com/company/opportunity-saas/

Usage : Analyser leur ligne éditoriale actuelle (que tu devras faire évoluer).

LinkedIn AllMySMS : https://www.linkedin.com/company/allmysms-com/

💡 Conseil de pro : En entretien, mentionner que tu as déjà "jeté un œil à la doc API sur allmysms.com pour voir les possibilités de webhooks" montrera immédiatement que tu es un Growth Engineer qui anticipe la technique, et non un simple utilisateur.





Sprint équipe — Benchmark data-driven + SEO (site : oppy.ai)
Statut* : sprint à exécuter (pas d’interface à développer : livrables = rapports, mesures, décisions).
Site principal audité* : https://www.oppy.ai/
Périmètre élargi obligatoire* : tous les domaines détectés ou liés (canonical, sitemap, OG, liens) — à cartographier par l’équipe.
Dernière mise à jour* : 2026-03-22
1. Objectifs du sprint

| ID | Objectif | Critère de fin de sprint |

|----|-----------|---------------------------|

| O1 | Benchmark data-driven reproductible (chiffres datés, même protocole) | Tableau rempli + exports (JSON/CSV/screenshots) archivés |

| O2 | SEO technique : stack, perf, indexation, redirections, sécurité transport | Rapport DevOps + Pentester + synthèse Architecte |

| O3 | SEO sémantique : thèmes, entités, duplication, cannibalisation | Rapport Marketing (conséquences) + base Rédaction |

| O4 | Rédaction : livrable « viable » (actionnable sans refaire l’audit) | Document 5–15 pages max ou équivalent structuré |

Principe* : chaque rôle relève les détails dans sa grille ; le chef de projet / orchestrateur consolide ; aucune donnée inventée — source obligatoire (outil, URL, capture, log).
2. RACI (synthèse)

| Activité | Marketing | Rédaction | DevOps | Pentester | Architecte |

|----------|-----------|-----------|--------|-----------|------------|

| Définition messages & positionnement vs mesures | A/R | C | I | I | C |

| Rapport lexical / pages pilotes / guidelines éditoriales | C | A/R | I | I | I |

| Mesures infra (DNS, HTTP, TTFB, cache, CI perf) | I | I | A/R | C | C |

| Surface d’attaque, headers, cookies, tiers | I | I | C | A/R | C |

| Cohérence multi-domaines, canonical, dette technique | C | C | C | I | A/R |

A = accountable, R = responsible, C = consulted, I = informed*
3. Périmètre URL & baseline « déjà observé » (à valider / compléter)

Attention : ce bloc est une amorce factuelle (mesures ponctuelles). L’équipe doit reprendre les commandes et dater chaque résultat.

3.1 Domaines à traiter comme un seul système

| URL / domaine | Rôle supposé (à confirmer) |

|---------------|---------------------------|

| https://www.oppy.ai/ | Entrée marketing auditée |

| https://opportunity-crm.com/ | Canonical déclaré dans le HTML de oppy.ai (à vérifier après déploiement) |

| https://oppycx.com/ | Hébergement médias / marque « Oppycx » (ex. og:image) |

| oppyai.fr | Liens sortants depuis le contenu (à inventorier) |

3.2 Indices stack / infra (revalidation obligatoire)

| Indicateur | Valeur observée (amorce) | Source type |

|------------|---------------------------|-------------|

| CMS | WordPress (wp-json, wp-content) | En-têtes HTML + Link |

| Runtime | PHP (PHPSESSID) | Cookies / en-têtes |

| www.oppy.ai — Server | Apache | curl -sI |

| opportunity-crm.com — Server | cloudflare | curl -sI |

| HTML homepage | ~298 Ko (ordre de grandeur) | curl -w '%{size_download}' |

| TTFB (un point géo) | ~0,52 s (non labo) | curl -w time_starttransfer |

| Cache document | no-store, no-cache (homepage) | Cache-Control |

| robots.txt (oppy.ai) | Sitemap pointant vers oppycx.com | GET /robots.txt |

Risque SEO majeur (hypothèse à trancher)* : découplage URL affichée / canonical / og:url / sitemap → risque de dilution des signaux, duplication et confusion utilisateur. L’Architecte rend une décision documentée (une propriété Search Console par langue ? redirects 301 ?).
4. Benchmark data-driven — protocole commun
4.1 Jeux de données (dimensions)

Chaque mesure doit préciser : date, heure UTC, localisation / IP sortante (pays, ou « CI GitHub » / « poste Paris »), device (mobile desktop), réseau (fibre / 4G / VPN).

| Dimension | Valeur à noter |

|-----------|----------------|

| URL exacte | |

| User-Agent | |

| Itérations | min. 5 pour moyenne ; 20+ si stabilité |

| Warmup | oui/non (1 requête discard) |

4.2 Métriques à collecter (tableau à remplir par l’équipe)

| Métrique | Outil / commande | Seuil d’alerte (indicatif) |

|----------|-------------------|----------------------------|

| TTFB | curl (voir §6) | > 800 ms mobile |

| Taille HTML | curl -w | > 200 Ko homepage à justifier |

| Status HTTP | curl -o /dev/null -w '%{http_code}' | ≠ 200 sur URL canonique |

| TLS / chaîne | openssl s_client | cert expiré / chaîne incomplète |

| DNS A/AAAA/CNAME | dig | incohérence multi-région |

| LCP / INP / CLS | PageSpeed Insights / Lighthouse | seuils Google CWV |

| Liens cassés (échantillon) | crawler | % > 1 % sur templates clés |

Fichier de consolidation recommandé* : docs/DATA_DRIVEN/BENCHMARK_SEO_OPPY_AI_YYYYMMDD.csv (une ligne = une mesure).
5. Marketing — SEO sémantique : conséquences & conclusions
Livrable* : docs/DATA_DRIVEN/RAPPORT_MARKETING_SEO_SEMANTIQUE_OPPY_AI.md (ou équivalent).
5.1 Questions à trancher avec données (pas d’avis sans page crawl)

Entité de marque : alignement Opportunity / Oppy / Oppycx / Opportunity AI — quelle forme légale et publicitaire dans title, H1, footer ?

Champ sémantique prioritaire (3–5 piliers) : ex. omnicanal, agent vocal, RCS, recouvrement, relation client.

Cannibalisation : pages qui ciblent les mêmes intentions (plusieurs URLs « agent vocal », « RCS », etc.).

Duplicate : blocs répétés dans le HTML (même série de produits plusieurs fois) — impact sur unicité par URL.

Maillage : proportion liens internes vs sortants vers oppyai.fr, oppycx.com, etc.

5.2 Sorties attendues (data-driven)

| Livrable | Contenu |

|----------|---------|

| Tableau intention de recherche × URL pilote | 10–20 lignes |

| Carte sémantique (mindmap ou tableau) | piliers → sous-thèmes → URLs |

| Risques | top 5 avec gravité (H/M/L) et preuve (capture, extrait H2) |

| Recommandations marketing | max 10, chacune liée à une mesure ou page |

5.3 Outils sémantiques (à lancer)
Crawl export (Screaming Frog, Oncrawl, ou script maison) : H1, H2, title, meta description, word count.
Si stack SquidResearch disponible : API interne documentée GET /documents/seo-audit/?url=... (extraction + probing — voir docs/TODO.md module SEO sémantique).
Google Search Console (si accès client) : requêtes, pages, cannibalisation.
6. Rédaction — rapport « viable »
Livrable* : document prêt à être partagé client / direction (PDF ou Markdown exporté).
6.1 Structure imposée (minimum)

Résumé exécutif (1 page) : 3 constats, 3 risques, 3 actions prioritaires.

Lexique métier validé (terme préféré / termes à éviter) — aligné Marketing.

Fiches par template (Home, Produit phare, Contact, Blog article type) :

Title / meta description proposés (caractères)

H1 unique + plan H2–H3

FAQ 3–5 questions (schema FAQ optionnel — à valider avec Architecte)

Snippet & SERP : exemples de rendu (pas de promesse de position).

Liste de contenus à produire / réécrire (priorisée P0–P2).

6.2 Critères de qualité « viable »
Chaque recommandation rédactionnelle référence une URL ou un extrait issu de l’audit.
Pas de jargon SEO non expliqué pour un lecteur marketing.
7. DevOps — outils & commandes (SEO technique, stack, flux)
Livrable* : log des commandes + sorties (texte) dans benchmarks/reports/seo_external/oppy_ai/ ou docs/DATA_DRIVEN/.
7.1 Identification HTTP / stack
*# Chaîne de redirection + en-têtes (remplacer HOST)*

HOST="<https://www.oppy.ai>"

curl -sSIL --max-time 30 "$HOST/" | sed -n '1,40p'

*# TTFB + taille (une requête)*

curl -sS -o /dev/null -w 'http_code:%{http_code} ttfb:%{time_starttransfer}s total:%{time_total}s size:%{size_download}\\n' --max-time 30 "$HOST/"

*# Comparaison multi-domaines (canonical / cookies / CDN)*

for u in "<https://www.oppy.ai/>" "<https://opportunity-crm.com/>" "<https://oppycx.com/>"; do

echo "=== $u ==="

curl -sI --max-time 20 "$u" | sed -n '1,25p'

done
7.2 DNS & résolution
dig +short www.oppy.ai A

dig +short www.oppy.ai AAAA

dig +short opportunity-crm.com A

dig +short oppycx.com A

*# Optionnel : traceroute / mtr vers IP frontale (attention charge réseau)*
7.3 TLS
echo | openssl s_client -servername www.oppy.ai -connect www.oppy.ai:443 2>/dev/null | openssl x509 -noout -dates -subject -issuer
7.4 Ressources & perf « lab »
PageSpeed Insights — URL mobile + desktop, exporter JSON si possible.
WebPageTest — filmstrip, waterfall, connexion 4G.
En CI / local si installé : npx lighthouse "$URL" --output json --output-path ./lighthouse-oppy.json --chrome-flags="--headless"
7.5 Indexation & fichiers standards
curl -sS "<https://www.oppy.ai/robots.txt>"

curl -sS "<https://oppycx.com/sitemap_index.xml>" | head -c 4000

*# Puis : télécharger les sitemaps listés et vérifier les URL canoniques déclarées dans les pages échantillon*
7.6 Flux applicatifs (observables sans code)
Onglet Réseau (DevTools) : nombre de requêtes, domaines tiers (analytics, tag manager, chat).
HAR export sur homepage + page produit (stockage interne sécurisé, données perso anonymisées).
8. Pentester — surface, headers, cookies, tiers
Livrable* : docs/DATA_DRIVEN/RAPPORT_PENTEST_SEO_TECHNIQUE_OPPY_AI.md (focus non destructif : observation seulement sauf mandat écrit).
8.1 Checklist

| Point | Commande / outil | Note |

|-------|------------------|------|

| CSP actuelle | en-tête Content-Security-Policy | Trop permissive = risque XSS si faille WP/plugin |

| X-Frame-Options / clickjacking | curl -sI | |

| Cookies : Secure, HttpOnly, SameSite | DevTools / curl | |

| Énumération WordPress | wpscan (si autorisé par le client), /wp-json/wp/v2/users | Ne pas brute-forcer sans accord |

| Fichiers sensibles | pas de scan agressif sans périmètre | |

| Tiers | liste domaines appelés au chargement | privacy + perf |

8.2 Outils utiles (selon mandat)
securityheaders.com (scan passif URL)
SSL Labs (note TLS — usage raisonnable)
whatweb, httpx -tech-detect (si installés sur poste équipe)
9. Architecte — cartographie & décisions
Livrable* : schéma domaines + flux (Mermaid ou draw.io) + ADR court (Architecture Decision Record).
9.1 Décisions à documenter

Hostname canonique unique par marché / langue.

Redirections 301 : oppy.ai → ? ; www vs non-www.

Sitemap unique : hébergement et propriété dans GSC.

Assets (images OG) : domaine stable et HTTPS.

Séparation marketing vs app (si opportunity-crm.com est outil SaaS) : risque de mélange d’intentions sur une même URL.

9.2 Exemple Mermaid (à compléter)

HTML canonical?

og:image?

liens contenu?

Utilisateur

Unsupported markdown: link

opportunity-crm.com

oppycx.com

oppyai.fr

10. Définition of Done (sprint)
Fichier CSV (ou équivalent) benchmark avec ≥ 30 lignes de mesures datées.
Rapports Marketing, Rédaction, DevOps, Pentester, Architecte déposés et nommés.
Réunion de restitution 45 min : 5 slides max + Q&R.
Aucune recommandation sans référence source.
11. Références externes (site audité)
Site public : https://www.oppy.ai/
12. Module interne SquidResearch (optionnel)

Si l’instance Django locale / staging est disponible avec le module SEO documenté :

Endpoint type : GET /documents/seo-audit/?url=https://www.oppy.ai/
Réf. connaissance : docs/TODO.md (module SEO sémantique), docs/BASE_CONNAISSANCES/MODULE_ANALYSE_SEO_SEMANTIQUE.md si présent.
Ne pas lancer d’audits massifs contre le site tiers sans cadre légal / accord client.*



Benchmark data-driven — **https://www.oppy.ai/\*\* (focus unique)
Périmètre* : uniquement l’URL **https://www.oppy.ai/\*\* (homepage + signaux HTTP/DNS/TLS + extrait sémantique public).
Mesures* : 2026-03-22T16:48:52Z (UTC) — poste/outil : CLI depuis environnement développeur (réseau non labo).
Site audité* : https://www.oppy.ai
1. Synthèse exécutive

| Signal | Constat | Impact SEO / marque |

|--------|---------|---------------------|

| Canonical | Pointe vers https://opportunity-crm.com/ alors que l’utilisateur est sur www.oppy.ai | Risque de confusion d’URL canonique pour les moteurs ; les signaux peuvent être attribués au mauvais hostname selon interprétation Google. |

| og:url | Idem https://opportunity-crm.com/ | Partages réseaux sociaux affichent une autre URL que celle visitée. |

| og:title / site | « Home - Oppycx » / og:site_name Oppycx | Incohérence avec la marque visible (Opportunity, OPPYAI sur la page — cf. contenu public). |

| Sitemap (robots.txt) | Sitemap: <https://oppycx.com/sitemap_index.xml> | Plan de site hors domaine oppy.ai → audit indexation oppy.ai à corréler avec GSC sur la bonne propriété. |

| Perf brute | HTML ~298 Ko, TTFB ~0,38–0,47 s (5 runs) | Homepage lourde ; pas de cache navigateur sur le document (no-store). |

| Stack | WordPress (wp-json), PHP (PHPSESSID), Apache, HTTP/2 | Surface classique WP (plugins, mises à jour) ; CSP très permissive. |

Conclusion courte* : le domaine www.oppy.ai fonctionne techniquement (200, TLS valide), mais les balises d’agrégation SEO/social renvoient vers d’autres domaines et une autre étiquette de marque (Oppycx). Le sprint équipe doit trancher une stratégie hostname unique ou documenter l’intention (marketing + architecte).
2. Données techniques (reproductibles)
2.1 HTTP — en-têtes réponse GET / (extrait)

| En-tête | Valeur |

|---------|--------|

| HTTP/2 | 200 |

| server | Apache |

| content-type | text/html; charset=UTF-8 |

| cache-control | no-store, no-cache, must-revalidate |

| pragma | no-cache |

| link | <https://www.oppy.ai/wp-json/>; rel="<https://api.w.org/>" |

| x-frame-options | SAMEORIGIN |

| referrer-policy | strict-origin-when-cross-origin |

| content-security-policy | Très large (default-src *, unsafe-inline, unsafe-eval sur scripts) |

Cookies observés* : utmtracking (Secure, HttpOnly, SameSite=Lax) ; PHPSESSID (path=/).
2.2 Benchmark TTFB & taille — 5 requêtes consécutives

| Run | http_code | TTFB (s) | total (s) | size (octets) |

|-----|-----------|----------|-----------|---------------|

| 1 | 200 | 0,435 | 0,490 | 297 905 |

| 2 | 200 | 0,379 | 0,448 | 297 905 |

| 3 | 200 | 0,465 | 0,520 | 297 905 |

| 4 | 200 | 0,417 | 0,466 | 297 905 |

| 5 | 200 | 0,468 | 0,523 | 297 905 |

Agrégats* : TTFB min 0,379 s · max 0,468 s · moyenne 0,433 s · taille constante 297 905 octets (~291 Ko).
Commande* :
curl -sS -o /dev/null -w 'http:%{http_code} ttfb:%{time_starttransfer} total:%{time_total} size:%{size_download}\\n' --max-time 25 '<https://www.oppy.ai/>'
2.3 DNS — www.oppy.ai

| Type | Résultat |

|------|----------|

| A | 35.180.17.239, 13.39.26.74, 13.37.91.81 |

| AAAA | (aucun enregistrement renvoyé au moment du test) |

2.4 TLS — certificat présenté pour www.oppy.ai

| Champ | Valeur |

|-------|--------|

| subject | CN = www.oppy.ai |

| notBefore | 19 mai 2025 GMT |

| notAfter | 16 juin 2026 GMT |

2.5 robots.txt — https://www.oppy.ai/robots.txt
User-agent: *

Allow: /

Sitemap: <https://oppycx.com/sitemap_index.xml>
2.6 Balises SEO / social (extrait HTML homepage)

| Balise | Valeur |

|--------|--------|

| link rel="canonical" | https://opportunity-crm.com/ |

| meta property="og:url" | https://opportunity-crm.com/ |

| meta property="og:title" | Home - Oppycx |

| meta property="og:site_name" | Oppycx |

| meta property="og:image" | https://oppycx.com/wp-content/uploads/2025/02/opportunity_ai.png |

| meta name="robots" | index, follow, max-image-preview:large, … |

3. SEO sémantique (homepage — source contenu public oppy.ai)
Analyse qualitative basée sur le texte visible / structure publique ; crawl multi-URL à faire par l’équipe.*
3.1 Proposition de valeur (H1 / chapô)
H1 (public) : « Touchez plus de clients où qu’ils soient, quand ils veulent ! »* — bénéfice générique ; peu de différenciation produit dans la chaîne H1 seule.
Sous-titre : plateforme omnicanale (SMS, RCS, emails, WhatsApp, agents IA vocaux), marketing, relation client, recouvrement.
3.2 Piliers thématiques déduits

Agents IA vocaux / callbot (répété plusieurs fois dans le corps — risque de redondance sur une même URL).

Canaux : RCS, SMS, email, Vidéobot, Touch & Pay, RDV, signature vocale.

Axes métier : acquisition, relation client, rétention & paiement.

Confiance : logos clients, EcoVadis or (2025), 5 200 entreprises.

3.3 Incohérences rédactionnelles / SEO (à traiter par la rédaction)
Titres dupliqués ou quasi identiques (Agent IA Vocal, Vidéobot, RCS, SMS & EMAIL réapparaissent).
Fautes / variantes : « diffiser », VideoBot vs Vidéobot, Touch&Pay vs Touch & Pay*.
Marque : Opportunity, Oppycx, OPPYAI — à normaliser (title, H1, footer, OG).
3.4 Actions marketing / rédaction (priorisées)

| P | Action |

|---|--------|

| P0 | Décision URL canonique et alignement canonical + og:url + GSC sur www.oppy.ai ou redirection marketing 301 vers le domaine choisi. |

| P0 | Harmoniser nom de marque dans title, og:title, og:site_name, H1. |

| P1 | Réduire répétition des blocs produits sur la home ou les déporter vers des pages dédiées (maillage). |

| P1 | Corriger typos et casse des noms produits. |

| P2 | Alléger HTML / cache page d’accueil (objectif : CWV + coût serveur). |

4. Pentester (aperçu — non exhaustif)
CSP : politique large → en cas de XSS (plugin WP, formulaire), impact aggravé.
Cookies : PHPSESSID sans attributs Secure/HttpOnly visibles sur la ligne brute du test — revérifier dans navigateur (ici utmtracking est bien Secure; HttpOnly).
Surface : WordPress — suivre mises à jour core / plugins / comptes admin.
5. Fichier CSV associé

Voir : BENCHMARK_WWW_OPPY_AI_20260322.csv (même dossier).

6. Suite sprint

Référence cadre équipe : docs/sprints/SPRINT_EQUIPE_BENCHMARK_SEO_OPPY_AI_2026.md (mis à jour — focus www.oppy.ai).





timestamp_utc,url,metric,value,unit,notes

2026-03-22T16:48:52Z,https://www.oppy.ai/,http_status,200,code,GET /

2026-03-22T16:48:53Z,https://www.oppy.ai/,server,Apache,string,response header

2026-03-22T16:48:53Z,https://www.oppy.ai/,html_size_bytes,297905,bytes,5 runs identical

2026-03-22T16:48:53Z,https://www.oppy.ai/,ttfb_s,0.435,seconds,run 1

2026-03-22T16:48:54Z,https://www.oppy.ai/,ttfb_s,0.379,seconds,run 2

2026-03-22T16:48:55Z,https://www.oppy.ai/,ttfb_s,0.465,seconds,run 3

2026-03-22T16:48:56Z,https://www.oppy.ai/,ttfb_s,0.417,seconds,run 4

2026-03-22T16:48:57Z,https://www.oppy.ai/,ttfb_s,0.468,seconds,run 5

2026-03-22T16:48:57Z,https://www.oppy.ai/,ttfb_avg_s,0.433,seconds,calculated from 5 runs

2026-03-22T16:49:00Z,https://www.oppy.ai/,dns_a,"35.180.17.239;13.39.26.74;13.37.91.81",list,dig +short A

2026-03-22T16:49:00Z,https://www.oppy.ai/,dns_aaaa,empty,string,no AAAA returned

2026-03-22T16:49:00Z,https://www.oppy.ai/,tls_cn,www.oppy.ai,string,openssl x509 subject

2026-03-22T16:49:00Z,https://www.oppy.ai/,tls_not_after,2026-06-16,string,GMT

2026-03-22T16:49:00Z,https://www.oppy.ai/,canonical_url,https://opportunity-crm.com/,url,link rel=canonical

2026-03-22T16:49:00Z,https://www.oppy.ai/,og_url,https://opportunity-crm.com/,url,meta og:url

2026-03-22T16:49:00Z,https://www.oppy.ai/,og_title,Home - Oppycx,string,meta og:title

2026-03-22T16:49:00Z,https://www.oppy.ai/,sitemap_in_robots,https://oppycx.com/sitemap_index.xml,url,robots.txt line

2026-03-22T16:49:00Z,https://www.oppy.ai/,cache_control,no-store no-cache must-revalidate,string,header



Voici ce qui a été fait, centré uniquement sur https://www.oppy.ai.

1. Rapport benchmark data-driven (mesures réelles)

docs/DATA_DRIVEN/BENCHMARK_WWW_OPPY_AI_20260322.md

Synthèse exécutive (canonical / og:url / sitemap / marque Oppycx vs contenu Opportunity / OPPYAI).
5 runs TTFB + taille HTML fixe 297 905 octets, en-têtes, DNS A (3 IPv4, pas d’AAAA au test), TLS jusqu’au 16/06/2026, robots.txt, extrait balises SEO/social.
SEO sémantique homepage : piliers (IA vocale, canaux, preuves), répétitions, typos, P0–P2 pour marketing & rédaction.
Aperçu pentest (CSP, surface WP).

docs/DATA_DRIVEN/BENCHMARK_WWW_OPPY_AI_20260322.csv

Une ligne par métrique (horodatage UTC, reproductible).
2. Sprint équipe mis à jour
docs/sprints/SPRINT_EQUIPE_BENCHMARK_SEO_OPPY_AI_2026.md
Focus = www.oppy.ai ; les autres domaines ne sont qu’annexe pour expliquer ce qui est déclaré dans le HTML/robots d’oppy.ai.
Section 3 alignée sur le rapport du 2026-03-22.
§7 DevOps : précision que le HOST par défaut est www.oppy.ai.

Constat principal déjà chiffré : l’utilisateur est sur www.oppy.ai, mais canonical et og:url pointent vers opportunity-crm.com, le sitemap vers oppycx.com, et og:title reste « Home - Oppycx » — à trancher côté produit + technique (cf. rapport §1 et §3).

Prochaine étape côté équipe : PSI / Lighthouse mobile sur la même URL + crawl interne des liens depuis la home uniquement, en complément de ce benchmark.