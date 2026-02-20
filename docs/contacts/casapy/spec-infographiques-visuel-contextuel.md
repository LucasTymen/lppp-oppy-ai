# Casapy — Infographiques visuelles + contextuelles (spec exécutable)

**Pour** : Infographiste + Rédacteur en chef.  
**Demande utilisateur** : approche **très visuelle + contextuelle** ; formules réutilisables ; snippets HTML/CSS/JS « drop-in » ; rendu **joli** ; **chaque bloc doit être expliqué par un texte court** (tenants et aboutissants).

---

## Consignes transverses

| Rôle | Consigne |
|------|----------|
| **Infographiste** | S’inspirer des blocs ci-dessous (jauges, tableau criticité, flowchart, cartes scénarios, plan). Rendre **joli** (cohérent avec la charte Casapy, fond sombre, lisibilité). Intégration possible : HTML/SVG/CSS + JS minimal (landing Django/Next) ou composants React si besoin. |
| **Rédacteur en chef** | **Chaque bloc visuel est accompagné d’un texte court** qui explique les **tenants et les aboutissants** (pourquoi ce chiffre, pourquoi cette priorité, quelle conséquence). Compréhensible par un humain, **non marqué IA** — appliquer `docs/bonnes-pratiques.md`. Une phrase sous le visuel ou un encart suffit. |

Références : `docs/bonnes-pratiques.md`, `.cursor/rules/redacteur-en-chef.mdc`, `spec-deck-casapy-7-slides.md`.

---

## A) Comment infographier ces data (avec contexte, pas juste des chiffres)

### 1) “Diagnostic Perf” → 2 jauges + 1 phrase explicative

**Visuel :** 2 *gauges* (ou barres) :

- **TTFB Homepage : 3,77 s** (rouge)
- **TTFB PDP : 3,63 s** (rouge)

Sous-titre (contexte, 1 ligne) :

> “Le serveur répond trop lentement : c’est un problème backend/DB/hosting ; le front (JS/CSS) n’est pas le goulot principal.”

Et un mini repère :

- “Bon < 0,5 s” (vert) ; “Critique > 2 s” (rouge)

### 2) “Priorités techniques” → tableau criticité (chips)

**Visuel :** tableau 2 colonnes (Sujet / Statut) avec des chips :

- TTFB ~3,7 s → **Critique**
- LCP mobile 32 s → **Bloquant**
- Hébergement mutualisé → **Inadapté**
- Perte conversion 25–50 % → **Business**

### 3) “Chaîne de blocage” → flowchart

**Visuel :** 3 boîtes + flèches :

**Serveur (TTFB)** → **DB (sessions/index)** → **Front (LCP/JS)**

Sous-texte : “LCP élevé est une conséquence : tant que TTFB est haut, le rendu est retardé.”

### 4) “Manque à gagner” → 3 cartes scénarios

**Visuel :** 3 cards avec :

- Inputs (visites, conv, panier)
- **Ventes perdues**
- **Impact mensuel** (gros chiffre)

---

## B) Formules (propres, réutilisables)

### 1) CA mensuel

\[
CA = Visits \times ConvRate \times AOV
\]

### 2) Ventes (commandes)

\[
Orders = Visits \times ConvRate
\]

### 3) Perte de ventes (si perte conversion p)

\[
LostOrders = Orders \times p
\]

où \( p = 0{,}30 \) pour -30 %.

### 4) Manque à gagner

\[
LostRevenue = CA \times p
\]

ou

\[
LostRevenue = LostOrders \times AOV
\]

**Ex. scénario 10 k / 2 % / 900 € :**

- Orders = 10 000 × 0,02 = 200  
- LostOrders (30 %) = 60  
- LostRevenue = 60 × 900 = **54 000 €**

---

## C) Code HTML/CSS/JS minimal (intégration landing)

Intégration possible en landing Next.js (composant ou `dangerouslySetInnerHTML`) ou dans un template Django. Idéalement en JSX/React pour maintenabilité ; ci-dessous en HTML/CSS/JS « drop-in ».

---

### 1) Bloc “Jauges TTFB” (SVG — simple, léger)

```html
<section class="card">
  <h3>Diagnostic TTFB</h3>
  <p class="muted">
    Référence : bon &lt; 0,5 s • critique &gt; 2 s. Zone rouge = problème serveur/backend (pas prioritairement JS/CSS).
  </p>

  <div class="grid2">
    <div class="gauge" data-label="Homepage" data-value="3.77" data-max="4.5"></div>
    <div class="gauge" data-label="PDP" data-value="3.63" data-max="4.5"></div>
  </div>
</section>

<style>
  :root{
    --bg:#0b0b10; --card:#12121a; --text:#f2f2f7; --muted:#a7a7b4;
    --red:#ff4d4f; --orange:#ff9f0a; --green:#34c759; --line:#232334;
  }
  body{background:var(--bg); color:var(--text); font-family:system-ui, -apple-system, Segoe UI, Roboto, Arial;}
  .card{background:var(--card); border:1px solid var(--line); border-radius:14px; padding:18px; max-width:980px;}
  .muted{color:var(--muted); margin-top:6px;}
  .grid2{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px; margin-top:14px;}
  .gaugeWrap{background:#0f0f16; border:1px solid var(--line); border-radius:14px; padding:14px;}
  .gTitle{display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;}
  .chip{padding:4px 8px; border-radius:999px; font-size:12px; font-weight:600;}
  .chip.red{background:rgba(255,77,79,.15); color:var(--red); border:1px solid rgba(255,77,79,.35);}
</style>

<script>
  function colorForTTFB(v){
    if(v < 0.5) return '#34c759';
    if(v < 2.0) return '#ff9f0a';
    return '#ff4d4f';
  }

  document.querySelectorAll('.gauge').forEach(el=>{
    const label = el.dataset.label;
    const v = parseFloat(el.dataset.value);
    const max = parseFloat(el.dataset.max || '5');
    const pct = Math.max(0, Math.min(1, v/max));
    const stroke = colorForTTFB(v);

    el.innerHTML = `
      <div class="gaugeWrap">
        <div class="gTitle">
          <strong>${label}</strong>
          <span class="chip red">${v.toFixed(2)}s • Critique</span>
        </div>
        <svg viewBox="0 0 120 70" width="100%" height="120" aria-label="TTFB gauge">
          <path d="M10 60 A50 50 0 0 1 110 60" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="10" stroke-linecap="round"/>
          <path d="M10 60 A50 50 0 0 1 110 60" fill="none" stroke="${stroke}" stroke-width="10" stroke-linecap="round"
                stroke-dasharray="${Math.round(157*pct)} 157"/>
          <text x="60" y="48" text-anchor="middle" font-size="16" fill="#f2f2f7" font-weight="700">${v.toFixed(2)}s</text>
          <text x="60" y="66" text-anchor="middle" font-size="10" fill="#a7a7b4">objectif &lt; 0,8 s</text>
        </svg>
      </div>
    `;
  });
</script>
```

**Texte d’accompagnement (Rédacteur en chef)** : une phrase sous le bloc qui explique pourquoi le TTFB est le goulot et pourquoi ce n’est pas le front en premier (tenants et aboutissants).

---

### 2) Bloc “Priorités techniques” (table + chips)

```html
<section class="card" style="margin-top:14px;">
  <h3>Priorités techniques — Niveau de criticité</h3>

  <table class="tbl">
    <tr><td>TTFB (~3,7 s)</td><td><span class="pill crit">Critique</span></td></tr>
    <tr><td>LCP mobile (32 s)</td><td><span class="pill block">Bloquant</span></td></tr>
    <tr><td>Hébergement mutualisé</td><td><span class="pill bad">Inadapté</span></td></tr>
    <tr><td>Perte conversion (25–50 %)</td><td><span class="pill biz">Business</span></td></tr>
  </table>
</section>

<style>
  .tbl{width:100%; border-collapse:separate; border-spacing:0 10px; margin-top:10px;}
  .tbl td{padding:12px 12px; background:#0f0f16; border:1px solid var(--line);}
  .tbl td:first-child{border-radius:12px 0 0 12px;}
  .tbl td:last-child{border-radius:0 12px 12px 0; text-align:right;}
  .pill{padding:6px 10px; border-radius:999px; font-size:12px; font-weight:700; display:inline-block;}
  .crit{color:var(--red); background:rgba(255,77,79,.15); border:1px solid rgba(255,77,79,.35);}
  .block{color:#ffcc00; background:rgba(255,204,0,.12); border:1px solid rgba(255,204,0,.3);}
  .bad{color:#ff9f0a; background:rgba(255,159,10,.12); border:1px solid rgba(255,159,10,.3);}
  .biz{color:#5ac8fa; background:rgba(90,200,250,.12); border:1px solid rgba(90,200,250,.3);}
</style>
```

**Texte d’accompagnement** : court encart qui dit pourquoi ces niveaux (critique / bloquant / business) et ce qu’on en déduit comme ordre d’action.

---

### 3) “Chaîne de blocage” (flowchart CSS)

```html
<section class="card" style="margin-top:14px;">
  <h3>Chaîne de blocage — Serveur → DB → Front</h3>
  <p class="muted">Le TTFB élevé bloque le rendu : LCP devient une conséquence (Elementor/WooCommerce + scripts/images + requêtes SQL).</p>

  <div class="flow">
    <div class="node">
      <strong>Serveur</strong>
      <span class="muted">TTFB ~3,7 s</span>
    </div>
    <div class="arrow">→</div>
    <div class="node">
      <strong>Base de données</strong>
      <span class="muted">sessions • transients • index</span>
    </div>
    <div class="arrow">→</div>
    <div class="node">
      <strong>Front</strong>
      <span class="muted">LCP • JS • images</span>
    </div>
  </div>
</section>

<style>
  .flow{display:flex; gap:10px; align-items:stretch; margin-top:12px; flex-wrap:wrap;}
  .node{flex:1; min-width:220px; background:#0f0f16; border:1px solid var(--line); border-radius:14px; padding:14px;}
  .arrow{display:flex; align-items:center; font-size:22px; color:#8a8aa0;}
</style>
```

**Texte d’accompagnement** : une phrase qui résume pourquoi on attaque dans cet ordre (serveur d’abord, puis DB, puis front).

---

### 4) “Manque à gagner” (cartes + calcul automatique)

```html
<section class="card" style="margin-top:14px;">
  <h3>Manque à gagner (scénarios)</h3>
  <p class="muted">Hypothèse : perte conversion = <strong>30 %</strong>. À recalibrer avec GA4 (trafic, CVR, AOV).</p>

  <div class="cards" id="scenarios"></div>
</section>

<style>
  .cards{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin-top:12px;}
  .c{background:#0f0f16; border:1px solid var(--line); border-radius:14px; padding:14px;}
  .c .big{font-size:26px; font-weight:800; margin-top:8px;}
  .kv{display:flex; justify-content:space-between; color:var(--muted); font-size:13px; margin-top:6px;}
  @media (max-width:900px){ .cards{grid-template-columns:1fr;} }
</style>

<script>
  const lossRate = 0.30;
  const scenarios = [
    { visits: 5000,  cvr: 0.02, aov: 900,  label: "Scénario 1" },
    { visits: 10000, cvr: 0.02, aov: 900,  label: "Scénario 2" },
    { visits: 10000, cvr: 0.05, aov: 1200, label: "Scénario 3" },
  ];

  function euro(n){ return n.toLocaleString('fr-FR') + ' €'; }

  const root = document.getElementById('scenarios');
  root.innerHTML = scenarios.map(s=>{
    const orders = s.visits * s.cvr;
    const lostOrders = orders * lossRate;
    const lostRevenue = lostOrders * s.aov;

    return `
      <div class="c">
        <strong>${s.label}</strong>
        <div class="kv"><span>Visites</span><span>${s.visits.toLocaleString('fr-FR')}</span></div>
        <div class="kv"><span>Conversion</span><span>${(s.cvr*100).toFixed(1)}%</span></div>
        <div class="kv"><span>Panier</span><span>${euro(s.aov)}</span></div>
        <div class="kv"><span>Ventes perdues</span><span>${lostOrders.toFixed(0)}</span></div>
        <div class="big" style="color:#ff4d4f;">${(lostRevenue/1000).toFixed(0)} k€/mois</div>
      </div>
    `;
  }).join('');
</script>
```

**Texte d’accompagnement** : expliquer en une ou deux phrases d’où viennent ces scénarios (hypothèse -30 %, à recalibrer avec GA4) et ce qu’on en tire (ordre de grandeur business, pas une facture exacte).

---

### 5) “Plan d’action priorisé” (timeline)

```html
<section class="card" style="margin-top:14px;">
  <h3>Plan d'action priorisé</h3>

  <ol class="steps">
    <li><strong>Serveur</strong> — migration VPS / hosting WooCommerce optimisé + cache (Redis/OPcache)</li>
    <li><strong>Base de données</strong> — nettoyage (sessions/transients), index, requêtes</li>
    <li><strong>Front-end</strong> — LCP image, defer JS, optimisation Elementor</li>
  </ol>
</section>

<style>
  .steps{margin:10px 0 0; padding-left:20px; color:var(--text);}
  .steps li{margin:10px 0; line-height:1.35;}
</style>
```

**Texte d’accompagnement** : pourquoi cet ordre (gains rapides + base saine pour CRO/SEO).

---

## 7 formats « moins évidents » (livré)

Fichier **exécuté** : `docs/contacts/casapy/infographie-casapy-7-formats.html` (un seul HTML autonome, 7 blocs).

| # | Format | Description | Priorité |
|---|--------|-------------|----------|
| 1 | **Speedometer score global 0–100** | Un seul tachymètre type Lighthouse ; le client voit « dans le rouge » sans lire. | — |
| 2 | **User Journey Timeline** | Frise 0 ms → 35 s : requête, TTFB 3,77 s, LCP 32 s, page utilisable. L’espace vide = attente. | **Prioritaire** (impact émotionnel) |
| 3 | **Lost Revenue Meter animé** | Compteur type taxi : +X € toutes les secondes (54 k€/mois → ~0,02 €/s). Urgence business. | **Prioritaire** |
| 4 | **Bullet Chart** | Barre objectif / valeur actuelle / marqueur standard. TTFB et LCP en un coup d’œil. | **Prioritaire** |
| 5 | **Heatmap Impact × Effort** | Matrice 2×2 : Nettoyage DB, Migration VPS, Cache Redis, Optimisation front. « Par quoi commencer ? » | — |
| 6 | **Waterfall (cascade chargement)** | HTML (3,77 s) → CSS → Images → JS → LCP. Montre pourquoi 32 s est une conséquence. | — |
| 7 | **Progress ring Recovery** | Ring « 78 % résolvable côté serveur ». Oriente vers la solution. | — |

**Recommandation** : les 3 prioritaires (Timeline + Lost Revenue Meter + Bullet Chart) racontent une histoire complète sans que le client ait besoin de lire.

**Template Django (récupération Chef de Projet)** : la version « dashboard complet » (polices Space Mono, Bebas Neue, DM Sans, grain, 7 blocs) est implantée en **template** : `templates/landing_pages/casapy_audit_dashboard.html`. URL : `/p/casapy/audit-dashboard/`. Récupérer le fichier pour réinjection (autre projet, iframe, export statique). Voir `docs/contacts/casapy/README.md` § Dashboard audit performance.

**Texte d’accompagnement (Rédacteur en chef)** — un court encart par bloc, tenants et aboutissants, `docs/bonnes-pratiques.md` :
- **Score global** : ce que signifie la note (agrégat TTFB + LCP) et pourquoi c’est « rouge ».
- **Timeline** : ce que vit l’utilisateur (attente avant premier octet, puis avant LCP) ; une phrase.
- **Compteur perte** : 54 k€/mois = hypothèse -30 % conversion ; à recalibrer avec GA4 ; une phrase.
- **Bullet** : objectif (vert), standard (marqueur), actuel (rouge) ; pourquoi agir d’abord sur le serveur.
- **Heatmap** : « En haut à gauche = à faire en premier » (impact élevé, effort faible).
- **Waterfall** : le TTFB bloque tout le reste ; LCP est une conséquence.
- **Ring** : la majeure partie du gain est côté infra, pas front.

---

## Intégration

- **100 % statique** : HTML/SVG/CSS + JS minimal comme ci-dessus ou `infographie-casapy-7-formats.html` (template Django ou iframe).
- **React / Next** : convertir en composants (`<PerfGauges />`, `<PriorityTable />`, `<ScenarioCards />`, `<Speedometer />`, `<JourneyTimeline />`, `<LostRevenueMeter />`, etc.) avec data en JSON ; préciser Tailwind ou CSS modules si besoin.
- **Joli** : charte Casapy (fond sombre, couleurs cohérentes), espacements, typo lisible, responsive.

*Spec rédigée à partir de la demande utilisateur. Infographiste = visuels ; Rédacteur en chef = texte court (tenants et aboutissants) par bloc, `docs/bonnes-pratiques.md`.*
