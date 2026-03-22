SEO Semantique

Rapport SEO sémantique complet — **https://www.oppy.ai/\*\*
Type* : audit sémantique (contenu, lexique, structure thématique, intentions, cohérence marque).
URL analysée* : https://www.oppy.ai/ (homepage).
Date d’extraction* : 2026-03-22 (HTML ~297 905 octets, réponse HTTP 200).
Méthode* : analyse du document HTML public (titres, métadonnées, fréquences lexicales approximatives, navigation) — sans accès Search Console ni crawl exhaustif du site.
Documents liés* : BENCHMARK_WWW_OPPY_AI_20260322.md (SEO technique & signaux canonical/OG), sprint docs/sprints/SPRINT_EQUIPE_BENCHMARK_SEO_OPPY_AI_2026.md.
1. Synthèse exécutive

| Axes | Diagnostic | Gravité |

|------|------------|---------|

| Cohérence marque | <title> et og:title = « Home - Oppycx » ; contenu et footer = Opportunity / OPPYAI | Élevée — dilution de l’entité nommée pour Google et les réseaux. |

| Proposition sémantique H1 | « Touchez plus de clients… » : bénéfice générique ; peu d’ancrage produit / catégorie marché dans le H1 | Moyenne — opportunité de renforcer le champ lexical métier (CPaaS, CX, omnicanal B2B). |

| Densité thématique homepage | Répétition forte des mêmes produits (Agent IA vocal, Vidéobot, RCS, SMS, etc.) dans plusieurs blocs | Moyenne — risque de fatigue sémantique sur une seule URL et de manque de profondeur par intention. |

| Champ lexical dominant | Clients, plateforme, automatisation, canaux (RCS, SMS, email), agent / vocal, rétention, paiement | Positive — alignement global avec l’offre CPaaS / engagement client. |

| Signaux confiance | Logos grands comptes, 5 200 entreprises, EcoVadis or | Positive — bon levier E-E-A-T Trust côté marque. |

Conclusion (1 phrase)* : la homepage oppy.ai couvre bien le secteur (omnicanal, IA vocale, recouvrement, RCS) mais fragmente l’identité de marque (Oppycx vs Opportunity / OPPYAI) et concentre trop d’intentions produit sur une seule page sans hiérarchie claire pour le moteur.
2. Périmètre, limites et méthode
2.1 Ce que ce rapport couvre
Sémantique de la homepage : titres visibles, menu, blocs texte, métadonnées title / og:description.
Fréquences : comptage sur le HTML (brut ou texte dé-htmlisé) — indicateurs relatifs, pas un score Google officiel.
Architecture des rubriques telles qu’exposées dans le HTML (Solutions, Produits, Ressources).
2.2 Ce que ce rapport ne couvre pas (sans données supplémentaires)
Crawl de l’ensemble des URLs, maillage interne quantifié, cannibalisation inter-pages.
Search Console : requêtes, impressions, CTR, pages positionnées.
Analyse concurrentielle SERP (who ranks sur « agent vocal B2B », « RCS marketing », etc.).
TF-IDF multi-documents du site (possible via module interne SquidResearch seo-audit si instance disponible).
2.3 Biais techniques
Occurrences du type « eco » peuvent inclure du bruit (classes CSS, « EcoVadis », etc.) : interpréter avec prudence.
« amp » en haut des fréquences : probablement lié au markup AMP ou entités HTML — non interprété comme le mot français « ampère ».
3. Métadonnées & alignement SERP / social

| Élément | Contenu observé | Analyse sémantique |

|---------|-----------------|-------------------|

| <title> | Home - Oppycx | Faible valeur SEO : « Home » est vide ; Oppycx n’est pas aligné avec le discours public Opportunity/OPPYAI. |

| og:title | Idem | Même problème pour les aperçus de partage. |

| og:description | Long paragraphe reprenant promesse omnicanale + IA vocale | Riche en mots-clés mais longue ; à tester en A/B (première phrase = promesse + catégorie). |

| meta name="description" | Non isolée dans l’extrait analysé | Vérifier présence/absence — doublon ou vide = opportunité. |

| canonical / og:url | opportunity-crm.com | Voir rapport technique : l’entité URL diffère du domaine visité — impact sur la consolidation sémantique. |

Recommandation sémantique (P0)* : une ligne de titre du type « Opportunity — Plateforme omnicanale & agents vocaux IA (B2B) »* (à valider marketing) + unicité du nom dans title, H1, OG, footer.
4. Entité de marque (named entity) & E-E-A-T
4.1 Signaux observés dans le HTML (occurrences approximatives, HTML en minuscules)

| Terme | Ordre de grandeur | Interprétation |

|-------|-------------------|----------------|

| oppycx | ~76 | Très présent (URLs, config WP, branding technique) — domine le code. |

| opportunity | ~54 | Présent (logo, textes, ©) — cohérent avec la marque corporate. |

| oppyai | ~7 | Sous-représenté vs usage marketing (widget « Laissez OPPYAI vous appeler »). |

4.2 E-E-A-T (aperçu homepage)

| Pilier | Constats |

|--------|----------|

| Experience | Mise en avant cas d’usage (relance, RDV, signature vocale) — crédible mais générique. |

| Expertise | Produits nommés (RCS, Vidéobot, Touch & Pay) — bon. |

| Authoritativeness | Logos clients + volume « 5 200 entreprises » — fort. |

| Trust | EcoVadis or, liens mentions légales / confidentialité — correct pour une home B2B. |

Manque pour approfondir* : pages Qui sommes-nous, équipe, certifications, études de cas nommées (hors homepage).
5. Architecture informationnelle & hiérarchie des titres
5.1 Menu principal (rubriques sémantiques)

Les blocs navigation exposent une taxonomie Solutions / Produits / Ressources :

Solutions : Acquisition, Relation clients, Rétention & paiement, Allmysms.
Produits : Agent RCS, Email & SMS, Agent IA vocal, Vidéobot, Touch & Pay, Module RDV, Signature vocale, Quality monitoring, Conformités des ventes, Boutique virtuelle (selon extrait HTML).
Ressources : Blog, RCS cas d’usage, Qui sommes-nous, Plateforme, Contact.
Analyse* : la taxonomie est claire pour un humain ; côté SEO, chaque entrée devrait idéalement correspondre à une URL dédiée avec H1 unique et texte non dupliqué depuis la home.
5.2 H1 / H2 visibles (homepage)

| Niveau | Texte (extrait significatif) | Rôle sémantique |

|--------|------------------------------|-----------------|

| H1 | Touchez plus de clients où qu’ils soient, quand ils veulent ! | Awareness / promesse émotionnelle — peu de mots-clés catégorie (ex. plateforme d’engagement, CPaaS). |

| H2 | Une seule plateforme pour orchestrer… (SMS, RCS, emails, WhatsApp, agents IA vocaux) | Pilier : définition de l’offre — bonne densité canaux. |

| H2 | Les Agents IA vocaux intelligents… | Cluster produit phare. |

| H2 | Engagez vos clients sur tous les canaux | Cluster omnicanal / scénarios. |

| H2 | Une équipe d’experts | Cluster accompagnement / services. |

| H2 | Automatisez l’expérience client… | Cluster pont produit / AllMySMS & co. |

| H2 | 5 200 entreprises… / RSE / EcoVadis / CTA final | Preuve sociale & responsabilité — utile pour la confiance. |

Nombre de balises titres* : ~84 balises h1–h6 dans le document (inclut navigation, modales, cookie) — beaucoup pour une seule page « contenu » ; le moteur peut pondérer différemment les titres dans le body vs header/footer.
5.3 H3 / produits répétés

Les mêmes intitulés produits (Agent IA vocal, Vidéobot, RCS, SMS & email, etc.) reviennent dans plusieurs sections → pour l’utilisateur c’est de la réassurance ; pour le SEO c’est du texte quasi dupliqué sur la même URL.

6. Champs lexicaux & clusters thématiques
6.1 Top termes (texte dé-htmlisé simplifié — top concepts)
Source : tokenisation grossière, stopwords français partiels.*

| Fréquence indicative | Terme |

|----------------------|--------|

| ~19 | clients |

| ~12 | amp (bruit technique possible) |

| ~11 | agent, rcs |

| ~11 | sms |

| ~8 | vocal |

| ~7 | rétention, email |

| ~6 | vidéobot, plateforme, marketing, paiement |

| ~5 | relation, touch, pay, expérience, campagnes |

6.2 Occurrences ciblées (HTML brut, minuscules — ordre de grandeur)

| Expression / terme | Occurrences | Cluster thématique |

|--------------------|-------------|---------------------|

| rcs | ~55 | Canaux riches / SMS 2.0 |

| sms | ~25 | Messaging / campagnes |

| agent ia vocal / ia vocal | ~9 | IA conversationnelle vocale |

| vidéobot | ~7 | Vidéo interactive |

| videobot | ~4 | Incohérence graphique (anglais vs français) |

| email | ~14 | Email marketing / transactional |

| whatsapp | ~3 | Messagerie — sous-exploité en volume vs promesse « omnicanal » |

| callbot | ~2 | Synonymie avec agent vocal — à unifier lexicalement |

| recouvrement | ~4 | Rétention / créance — bon différenciateur |

| omnicanal | ~1 | Concept clé sous-répété explicitement |

| plateforme | ~12 | Ancrage « solution » |

| scénario(s) | ~3 | Automation / parcours client |

6.3 Carte sémantique proposée (à valider marketing)
[Plateforme Opportunity / OPPYAI]

|

+------------+-----------+-----------+------------+

|            |           |           |            |

Acquisition   Relation    Rétention    Canaux      Confiance

|         client      & paiement     riches      (logos, EcoVadis)

|            |           |           |

Campagnes    Automatisation  Touch & Pay   RCS, SMS,

email/SMS    analyse       recouvrement   WhatsApp

|

Agent IA vocal / Vidéobot / RDV / Signature
7. Intentions de recherche (mapping qualitatif)
Sans données GSC, mapping hypothétique à valider par les requêtes réelles.**

| Intention type | Exemples de requêtes cibles | Adéquation homepage actuelle |

|----------------|----------------------------|------------------------------|

| Catégorie | « plateforme sms professionnel », « solution rcs entreprise » | Moyenne — mots présents mais H1 peu catégoriel. |

| Produit | « agent vocal ia commercial », « vidéobot interactif b2b » | Bonne — blocs dédiés mais répétitifs. |

| Use case | « recouvrement client sms », « prise de rdv automatisée » | Partielle — idées présentes, peu de détails (pas de pages dédiées analysées ici). |

| Marque | « Opportunity », « Oppycx », « Oppy AI » | Faible cohérence — risque de requêtes brand diluées. |

| Comparatif | « alternative à … » | Non couvert sur la home (normal). |

8. Redondance, duplication & cannibalisation
8.1 Intra-page (homepage)
Même promesse produit réécrite plusieurs fois (agent vocal, vidéobot, RCS) → une seule URL absorbe beaucoup de variantes ; intérêt : renforcer la page sur la requête « marque + plateforme » ; risque : manque de pages satellites pour le longue traîne.
8.2 Inter-pages (hypothèse)
Si des landing produit existent avec les mêmes paragraphes que la home → cannibalisation probable. Action : crawl + matrice mot-clé × URL cible*.
8.3 JSON-LD
1 bloc application/ld+json détecté (comptage brut) — à auditer au Rich Results Test pour type (Organization, WebSite, FAQ, etc.) et cohérence avec la marque choisie.
9. Qualité éditoriale & cohérence terminologique

| Problème | Exemple / zone | Impact |

|----------|----------------|--------|

| Casse / graphie | VideoBot vs Vidéobot | Fragmentation des signaux sur une entité produit. |

| Orthographe | diffiser (signalé précédemment sur contenu public) | Crédibilité / qualité perçue. |

| Symboles | Touch & Pay vs Touch & Pay vs espaces | Cohérence brand + snippets. |

| Anglicismes | Quality monitoring, Boutique virtuelle | OK B2B si glossaire aligné avec le reste du site FR. |

10. Plan d’action sémantique (priorisé)

| Priorité | Action | Responsable type |

|----------|--------|------------------|

| P0 | Nom unique : arbitrage Opportunity vs Oppycx vs OPPYAI → appliquer à <title>, og:*, H1, schema.org | Marketing + SEO |

| P0 | Réécrire le title (≤ 60 car. utiles) + meta description dédiée (≤ 155 car.) avec 1 promesse + 1 catégorie | Rédaction |

| P1 | Enrichir le H1 ou ajouter un sous-titre visible immédiat avec termes catégorie (plateforme d’engagement client B2B, etc.) | Rédaction + Marketing |

| P1 | Dédupliquer les blocs produits sur la home : garder un bloc synthétique + liens vers pages piliers | Rédaction + Dev contenu |

| P1 | Page glossaire ou hub « Omnicanal » / « IA vocale » pour capter omnicanal (1 occurrence explicite = faible ancrage) | SEO + Rédaction |

| P2 | Harmoniser callbot / agent vocal / IA vocale (lexique utilisateur) | Rédaction |

| P2 | Augmenter la présence WhatsApp si offre réelle (alignement promesse / contenu) | Marketing |

| P3 | Étude SERP concurrentielle + réécriture H2 en questions (FAQ) + schema FAQ si pertinent | SEO |

11. Indicateurs de succès (à suivre post-actions)

| KPI | Outil |

|-----|--------|

| Impressions / clics sur requêtes brand et catégorie | Google Search Console |

| Part des pages avec 1 seul H1 « métier » | Crawl (Screaming Frog, etc.) |

| Clics depuis organic sur pages piliers produit | GSC + analytics |

| Taux de clics sur résultats enrichis | GSC + Rich results |

12. Annexes
A. Références
URL auditée : https://www.oppy.ai/
Benchmark technique : docs/DATA_DRIVEN/BENCHMARK_WWW_OPPY_AI_20260322.md
B. Reproductibilité (extrait HTML)
curl -sS -o /tmp/oppy_home.html '<https://www.oppy.ai/>'

wc -c /tmp/oppy_home.html
Document généré dans le cadre du benchmark SquidResearch ; à compléter après crawl multi-URL et export Search Console.*
JK



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
Rapport sémantique détaillé* : docs/DATA_DRIVEN/RAPPORT_SEO_SEMANTIQUE_COMPLET_WWW_OPPY_AI.md
Ci-dessous : rappel court ; le document lié contient l’analyse complète (lexique, intentions, E-E-A-T, plan d’action).*
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



