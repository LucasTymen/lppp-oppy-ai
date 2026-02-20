#!/usr/bin/env python3
"""
Génère les visuels slide-ready pour Casapy (audit SEO, e-commerce) en SVG (vectoriel).
Usage : python scripts/generate_visuels_casapy.py [--output docs/contacts/casapy]
Sortie : SVG dans le dossier indiqué (fond transparent, net à toute résolution).
Référence : brief visuels enjeux Casapy, spec-deck-casapy-7-slides.md.
"""
import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.gridspec import GridSpec

# Style : rouge=problème, orange=moyen, vert=objectif
# Contraste fond sombre (spec Casapy) : texte = blanc ; mise en valeur = jaune / orangé / bleu turquoise
COLORS = {
    "danger": "#dc2626",
    "danger_light": "#fef2f2",
    "orange": "#f97316",
    "orange_light": "#fff7ed",
    "success": "#059669",
    "primary": "#2563eb",
    "gray_700": "#334155",
    "gray_900": "#0f172a",
    "text_on_dark": "#ffffff",
    "accent_turquoise": "#22d3ee",
    "accent_yellow": "#fde047",
}


def setup_figure(dpi=120):
    """Figure par défaut, police lisible, fonds transparents. Fond sombre → TOUT le texte en blanc (lisibilité)."""
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "legend.facecolor": "none",
        "legend.frameon": False,
        "text.color": COLORS["text_on_dark"],
        "axes.labelcolor": COLORS["text_on_dark"],
        "axes.titlecolor": COLORS["text_on_dark"],
        "xtick.color": COLORS["text_on_dark"],
        "ytick.color": COLORS["text_on_dark"],
    })


def _so_what(ax, text: str, x=0.92, y=0.08, fontsize=9):
    """Encadré So what en bas à droite (même place sur toutes les slides)."""
    ax.text(x, y, text, ha="right", va="bottom", fontsize=fontsize, color=COLORS["gray_900"],
            bbox=dict(boxstyle="round,pad=0.35", facecolor=COLORS["accent_turquoise"], edgecolor="white", alpha=0.95),
            transform=ax.transAxes)


def _save_svg(fig, path: Path):
    """Sauvegarde en SVG (vectoriel, fond transparent) pour affichage net à toute résolution."""
    fig.patch.set_facecolor("none")
    for ax in fig.axes:
        ax.patch.set_facecolor("none")
        leg = ax.get_legend()
        if leg is not None:
            leg.get_frame().set_facecolor("none")
            leg.get_frame().set_alpha(0)
    fig.savefig(path, format="svg", bbox_inches="tight", transparent=True)


def slide1_impact_perf_business(out_dir: Path):
    """Slide 1 — Le frein #1 est serveur, pas le front."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis("off")

    steps = [
        ("Serveur\nHosting", COLORS["gray_700"], 1.5),
        ("TTFB\n3,7 s", COLORS["danger"], 3),
        ("LCP\n32 s", COLORS["danger"], 4.5),
        ("UX\ndégradée", COLORS["orange"], 6),
        ("Perte conv.\n-30 %", COLORS["orange"], 7.5),
        ("≈ 54 k€/mois", COLORS["accent_yellow"], 9.2),
    ]
    y = 2.5
    box_h, box_w = 0.9, 1.3
    for i, (label, color, x) in enumerate(steps):
        rect = FancyBboxPatch((x, y - box_h / 2), box_w, box_h, boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor="white", linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + box_w / 2, y, label, ha="center", va="center", fontsize=9, color=COLORS["text_on_dark"], fontweight="bold")
        if i < len(steps) - 1:
            ax.annotate("", xy=(x + box_w + 0.15, y), xytext=(x + box_w, y),
                        arrowprops=dict(arrowstyle="->", color=COLORS["accent_turquoise"], lw=2))

    ax.text(6, 0.8, "Hébergement mutualisé → TTFB ~3,7s → LCP ~32s. Pages perçues « cassées », friction, perte de confiance.",
            ha="center", fontsize=9, style="italic", color=COLORS["text_on_dark"])
    ax.set_title("Le frein #1 est serveur, pas le front", fontsize=14, fontweight="bold", pad=20, color=COLORS["text_on_dark"])
    _so_what(ax, "−30% conv ≈ 54k€/mois\n(hyp. à valider GA4)")
    fig.tight_layout()
    _save_svg(fig, out_dir / "slide1-impact-perf-business.svg")
    plt.close()


def slide2_waterfall_ttfb(out_dir: Path):
    """Slide 2 — Le goulot = temps de réponse serveur."""
    fig, ax = plt.subplots(figsize=(10, 5))
    labels = ["DNS/Connexion", "TTFB (goulot)", "Téléchargement", "Render/LCP"]
    values = [0.2, 3.7, 0.8, 8]  # secondes
    colors = [COLORS["accent_turquoise"], COLORS["danger"], COLORS["orange"], COLORS["orange"]]
    x = np.arange(len(labels))
    bars = ax.bar(x, values, color=colors, edgecolor="white", linewidth=1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10, color=COLORS["text_on_dark"])
    ax.set_ylabel("Temps (s)", color=COLORS["text_on_dark"])
    ax.set_title("Le goulot = temps de réponse serveur", fontsize=14, fontweight="bold", color=COLORS["text_on_dark"])
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.2, f"{v}s", ha="center", fontsize=9, color=COLORS["text_on_dark"])
    ax.axhline(y=0.8, color=COLORS["success"], linestyle="--", alpha=0.8, label="Objectif TTFB < 0,8 s")
    ax.legend(loc="upper right", fontsize=8, labelcolor=COLORS["text_on_dark"])
    ax.set_ylim(0, max(values) * 1.15)
    ax.tick_params(colors=COLORS["text_on_dark"])
    _so_what(ax, "Priorité =\nbackend / DB / hosting")
    fig.tight_layout()
    _save_svg(fig, out_dir / "slide2-waterfall-ttfb.svg")
    plt.close()


def slide3_hebergement_comparatif(out_dir: Path):
    """Slide 3 — Mutualisé = performance instable sur WooCommerce."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle("Mutualisé = performance instable sur WooCommerce", fontsize=12, fontweight="bold", color=COLORS["text_on_dark"], y=1.02)

    left_items = ["Ressources partagées (CPU/PHP-FPM/DB)", "WooCommerce + Elementor", "Latence variable, pics"]
    right_items = ["VPS / stack dédiée", "Redis, OPcache", "Perf stable"]
    for ax, items, title, color in [
        (ax1, left_items, "Mutualisé (aujourd'hui)", COLORS["danger"]),
        (ax2, right_items, "Recommandation (VPS/Cloud)", COLORS["success"]),
    ]:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, len(items) + 1)
        ax.axis("off")
        ax.set_title(title, fontsize=11, color=COLORS["text_on_dark"])
        for i, item in enumerate(items):
            y = len(items) - i
            ax.add_patch(FancyBboxPatch((0.1, y - 0.35), 0.8, 0.6, boxstyle="round,pad=0.02",
                                        facecolor=f"{color}40", edgecolor=color))
            ax.text(0.5, y, item, ha="center", va="center", fontsize=9, color=COLORS["text_on_dark"])
        badge = "Risque élevé" if color == COLORS["danger"] else "Perf stable"
        ax.text(0.5, 0.4, badge, ha="center", va="center", fontsize=10, fontweight="bold", color=COLORS["gray_900"],
                bbox=dict(boxstyle="round", facecolor=COLORS["accent_turquoise"], edgecolor="white"))
    _so_what(ax2, "Stabiliser =\nUX + conversion")
    fig.tight_layout()
    _save_svg(fig, out_dir / "slide3-hebergement-comparatif.svg")
    plt.close()


def slide4_plan_priorise(out_dir: Path):
    """Slide 4 — Plan d'action priorisé (1-2-3 : serveur → DB → front)."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.set_title("Plan d'action priorisé", fontsize=14, fontweight="bold", color=COLORS["text_on_dark"], pad=20)

    blocs = [
        (1, "Serveur\nmigration ou cache\n(Redis / OPcache)", 1.2),
        (2, "DB\nnettoyage transients/sessions\n+ index", 4.2),
        (3, "Front\nLCP image, defer JS\noptimisation Elementor", 7.2),
    ]
    for num, label, x in blocs:
        ax.add_patch(FancyBboxPatch((x, 1.2), 2.4, 1.8, boxstyle="round,pad=0.04",
                                    facecolor=f"{COLORS['primary']}50", edgecolor=COLORS["accent_turquoise"]))
        ax.text(x + 1.2, 2.5, str(num), ha="center", va="center", fontsize=28, fontweight="bold", color=COLORS["accent_yellow"])
        ax.text(x + 1.2, 1.8, label, ha="center", va="center", fontsize=9, color=COLORS["text_on_dark"])
    _so_what(ax, "Gains rapides +\nbase saine CRO/SEO")
    fig.tight_layout()
    _save_svg(fig, out_dir / "slide4-plan-priorise.svg")
    plt.close()


def slide5_scenarios_cout(out_dir: Path):
    """Slide 5 — Manque à gagner : 3 cartes (27k / 54k / 180k)."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.set_title("Manque à gagner (ordre de grandeur)", fontsize=14, fontweight="bold", color=COLORS["text_on_dark"], pad=20)

    cards = [
        ("27 k€/mois", "5k visites × 2% × 900€ × 30%", 0.8),
        ("54 k€/mois", "10k visites × 2% × 900€ × 30%", 3.8),
        ("180 k€/mois", "10k visites × 5% × 1200€ × 30%", 6.8),
    ]
    for val, detail, x in cards:
        ax.add_patch(FancyBboxPatch((x, 1), 2.2, 1.8, boxstyle="round,pad=0.04",
                                    facecolor=f"{COLORS['orange']}40", edgecolor=COLORS["orange"]))
        ax.text(x + 1.1, 2.3, val, ha="center", va="center", fontsize=18, fontweight="bold", color=COLORS["accent_yellow"])
        ax.text(x + 1.1, 1.5, detail, ha="center", va="center", fontsize=7, color=COLORS["text_on_dark"])
    ax.text(5, 0.5, "À recalibrer avec trafic réel + CVR + AOV (GA4)", ha="center", fontsize=9, style="italic", color=COLORS["text_on_dark"])
    _so_what(ax, "La perf est un sujet\nbusiness, pas technique")
    fig.tight_layout()
    _save_svg(fig, out_dir / "slide5-scenarios-cout.svg")
    plt.close()


def slide6_fact_hypothesis(out_dir: Path):
    """Slide 6 — Audit marketing : ce qui est prouvé vs à valider."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle("Audit marketing : ce qui est prouvé vs à valider", fontsize=14, fontweight="bold", color=COLORS["text_on_dark"], y=1.02)

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis("off")
    ax1.set_title("FACT", fontsize=12, color=COLORS["accent_turquoise"])
    ax1.add_patch(FancyBboxPatch((0.1, 0.5), 0.8, 0.35, boxstyle="round,pad=0.02", facecolor=f"{COLORS['accent_turquoise']}30", edgecolor=COLORS["accent_turquoise"]))
    ax1.text(0.5, 0.67, "Pas de traces Meta/Google\n(à date des bibliothèques)", ha="center", va="center", fontsize=10, color=COLORS["text_on_dark"])
    ax1.text(0.5, 0.25, "Next : collecter 5 preuves\nsite + tracking", ha="center", va="center", fontsize=9, style="italic", color=COLORS["text_on_dark"])

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    ax2.set_title("HYPOTHESIS", fontsize=12, color=COLORS["accent_yellow"])
    ax2.add_patch(FancyBboxPatch((0.1, 0.35), 0.8, 0.5, boxstyle="round,pad=0.02", facecolor=f"{COLORS['accent_yellow']}25", edgecolor=COLORS["accent_yellow"]))
    ax2.text(0.5, 0.75, "Persona, USP, funnel, canaux", ha="center", va="center", fontsize=10, color=COLORS["text_on_dark"])
    ax2.text(0.5, 0.5, "À valider avec données", ha="center", va="center", fontsize=9, color=COLORS["text_on_dark"])
    _so_what(ax2, "Décisions basées sur\ndonnées, pas intuitions")
    fig.tight_layout()
    _save_svg(fig, out_dir / "slide6-fact-hypothesis.svg")
    plt.close()


def slide4_matrice_seo_timeline(out_dir: Path):
    """Slide optionnel — Matrice 2×2 Urgence/Impact + timeline 30/60/90 (SEO & Growth)."""
    fig = plt.figure(figsize=(12, 5))
    gs = GridSpec(1, 2, width_ratios=[1.2, 1], figure=fig)

    ax1 = fig.add_subplot(gs[0])
    quadrants = [
        ("Quick wins\nHigh impact", "Canonicals, hreflang\nStructure URLs", COLORS["success"]),
        ("Structurant\nHigh impact", "Architecture SEO\nPages piliers", COLORS["primary"]),
        ("Quick wins\nLower", "Titles/meta\nInternal linking", COLORS["accent_turquoise"]),
        ("À clarifier", "Meta/Google : aucune trace", COLORS["orange"]),
    ]
    positions = [(0, 1), (1, 1), (0, 0), (1, 0)]
    for (qx, qy), (title, content, color) in zip(positions, quadrants):
        rect = FancyBboxPatch((qx * 0.5, qy * 0.5), 0.48, 0.48, boxstyle="round,pad=0.02",
                              facecolor=f"{color}40", edgecolor=color)
        ax1.add_patch(rect)
        ax1.text(qx * 0.5 + 0.24, qy * 0.5 + 0.38, title, ha="center", fontsize=9, fontweight="bold", color=COLORS["text_on_dark"])
        ax1.text(qx * 0.5 + 0.24, qy * 0.5 + 0.2, content, ha="center", fontsize=8, color=COLORS["text_on_dark"])
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis("off")
    ax1.set_title("SEO & Growth — Urgence vs Impact", color=COLORS["text_on_dark"])

    ax2 = fig.add_subplot(gs[1])
    ax2.axis("off")
    timeline = [
        "0–30 j : Perf serveur + tracking",
        "30–60 j : Clusters + CRO",
        "60–90 j : Scale contenus + campagnes",
    ]
    for i, t in enumerate(timeline):
        ax2.add_patch(FancyBboxPatch((0.1, 0.75 - i * 0.25), 0.8, 0.2, boxstyle="round,pad=0.02",
                                     facecolor=f"{COLORS['primary']}30", edgecolor=COLORS["accent_turquoise"]))
        ax2.text(0.5, 0.85 - i * 0.25, t, ha="center", va="center", fontsize=9, color=COLORS["text_on_dark"])
    ax2.set_title("Timeline 30/60/90 jours", color=COLORS["text_on_dark"])
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    fig.suptitle("SEO & Growth — état des lieux → plan", fontsize=12, fontweight="bold", color=COLORS["text_on_dark"])
    fig.tight_layout()
    _save_svg(fig, out_dir / "slide4-matrice-seo-timeline.svg")
    plt.close()


def one_pager_dashboard(out_dir: Path):
    """One-pager — Dashboard exécutif (5 blocs : symptôme, cause, impact, plan, marketing)."""
    fig = plt.figure(figsize=(10, 6))
    gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3)

    # 1. Symptôme (TTFB / LCP — zone rouge)
    ax1 = fig.add_subplot(gs[0, 0])
    metrics = [("TTFB", 3.7, 0.8), ("LCP", 32, 2.5)]
    for i, (name, val, target) in enumerate(metrics):
        ax1.barh(i, min(val, 5) if name == "LCP" else val, color=COLORS["danger"], height=0.5)
        ax1.axvline(x=target, color=COLORS["success"], linestyle="--", alpha=0.8)
        ax1.text(0.2, i, f"{name}: {val}", va="center", fontsize=9, color=COLORS["text_on_dark"])
    ax1.set_yticks(range(2))
    ax1.set_yticklabels(["TTFB", "LCP"], color=COLORS["text_on_dark"])
    ax1.set_xlabel("s", color=COLORS["text_on_dark"])
    ax1.set_title("Symptôme — zone rouge", color=COLORS["text_on_dark"])
    ax1.tick_params(colors=COLORS["text_on_dark"])
    ax1.set_xlim(0, 5)

    # 2. Impact (gros chiffre)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis("off")
    ax2.text(0.5, 0.7, "~54 k€/mois", ha="center", fontsize=24, fontweight="bold", color=COLORS["accent_yellow"])
    ax2.text(0.5, 0.5, "Scénario conservateur (à valider GA4)", ha="center", fontsize=10, color=COLORS["text_on_dark"])
    ax2.text(0.5, 0.3, "10k visites × 2% × 900€ × 30%", ha="center", fontsize=9, style="italic", color=COLORS["text_on_dark"])
    ax2.set_title("Impact", color=COLORS["text_on_dark"])
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    # 3. Causes racines
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.axis("off")
    causes = ["Mutualisé + WooCommerce/Elementor", "Latence / variabilité"]
    for i, c in enumerate(causes):
        ax3.text(0.1, 0.8 - i * 0.35, f"• {c}", fontsize=10, color=COLORS["text_on_dark"])
    ax3.set_title("Cause", color=COLORS["text_on_dark"])
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    # 4. Plan 30 jours + Marketing
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis("off")
    ax4.text(0.1, 0.85, "Plan 30 j : Serveur/cache → DB → Front", fontsize=10, color=COLORS["text_on_dark"])
    ax4.text(0.1, 0.5, "Marketing clean room : FACT/HYPOTHESIS", fontsize=9, color=COLORS["text_on_dark"])
    ax4.text(0.1, 0.35, "5 preuves à fournir + GA4/GTM", fontsize=9, color=COLORS["accent_turquoise"])
    ax4.set_title("Plan + Marketing", color=COLORS["text_on_dark"])
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)

    fig.suptitle("Casapy — Dashboard exécutif (one-pager)", fontsize=14, fontweight="bold", color=COLORS["text_on_dark"])
    _save_svg(fig, out_dir / "one-pager-dashboard-casapy.svg")
    plt.close()


def casapy_wave_progression(out_dir: Path):
    """Slide 7 — Après fix : baseline meilleure + volatilité plus faible (Wave TTFB, plus bas = mieux)."""
    n_days = 90
    baseline = 3.7
    slope = -0.02
    period = 21
    phase = 0.5
    amp_before = 0.5
    amp_after = 0.15
    fix_day = 30
    noise = 0.05
    rng = np.random.default_rng(42)
    t = np.arange(n_days)
    A = np.where(t < fix_day, amp_before, amp_after)
    y = (baseline + slope * t) + A * np.sin(2 * np.pi * (t / period) + phase)
    y = y + rng.normal(0, noise, size=n_days)
    y = np.clip(y, 0.3, 5)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, y, linewidth=2, color=COLORS["accent_turquoise"])
    ax.axvline(fix_day, linestyle="--", linewidth=2, color=COLORS["accent_yellow"])
    ax.axhline(0.8, linestyle=":", color=COLORS["success"], alpha=0.8, label="Objectif < 0,8 s")
    ax.text(fix_day + 2, np.min(y) + 0.15, "Fix (J0)\nVPS + cache", fontsize=9, color=COLORS["accent_yellow"],
            bbox=dict(boxstyle="round,pad=0.2", facecolor=COLORS["gray_900"], edgecolor=COLORS["accent_turquoise"]))
    ax.set_title("Après fix : baseline meilleure + volatilité plus faible", fontsize=14, fontweight="bold", color=COLORS["text_on_dark"])
    ax.set_xlabel("Jours", color=COLORS["text_on_dark"])
    ax.set_ylabel("TTFB (s) — plus bas = mieux", color=COLORS["text_on_dark"])
    ax.legend(loc="upper right", fontsize=8, labelcolor=COLORS["text_on_dark"])
    ax.tick_params(colors=COLORS["text_on_dark"])
    ax.grid(alpha=0.25, color=COLORS["text_on_dark"])
    for spine in ax.spines.values():
        spine.set_color(COLORS["text_on_dark"])
    _so_what(ax, "CVR, SEO (CWV),\nROAS durable")
    fig.tight_layout()
    _save_svg(fig, out_dir / "casapy-wave-progression.svg")
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Génère les visuels Casapy (7 slides + one-pager + wave, fond sombre)")
    parser.add_argument("--output", default="docs/contacts/casapy", help="Dossier de sortie")
    parser.add_argument("--svg", action="store_true", help="Ignoré (export SVG par défaut)")
    args = parser.parse_args()
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    setup_figure()
    slide1_impact_perf_business(out_dir)
    slide2_waterfall_ttfb(out_dir)
    slide3_hebergement_comparatif(out_dir)
    slide4_plan_priorise(out_dir)
    slide5_scenarios_cout(out_dir)
    slide6_fact_hypothesis(out_dir)
    slide4_matrice_seo_timeline(out_dir)  # optionnel SEO & Growth
    one_pager_dashboard(out_dir)
    casapy_wave_progression(out_dir)

    print(f"Visuels générés (SVG) dans {out_dir.absolute()}")
    for f in sorted(out_dir.glob("*.svg")):
        print(f"  - {f.name}")


if __name__ == "__main__":
    main()
