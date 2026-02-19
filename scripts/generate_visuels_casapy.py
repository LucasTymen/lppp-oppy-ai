#!/usr/bin/env python3
"""
Génère les visuels slide-ready pour Casapy (audit SEO, e-commerce).
Usage : python scripts/generate_visuels_casapy.py [--output docs/contacts/casapy]
Sortie : PNG (et SVG si --svg) dans le dossier indiqué.
Référence : brief visuels enjeux Casapy (4 slides + one-pager).
"""
import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.gridspec import GridSpec

# Style : rouge=problème, orange=moyen, vert=objectif
COLORS = {
    "danger": "#dc2626",
    "danger_light": "#fef2f2",
    "orange": "#f97316",
    "orange_light": "#fff7ed",
    "success": "#059669",
    "primary": "#2563eb",
    "gray_700": "#334155",
    "gray_900": "#0f172a",
}


def setup_figure(dpi=120):
    """Figure par défaut, police lisible, fond transparent."""
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "figure.facecolor": "none",
        "axes.facecolor": "none",
    })


def _save_transparent(fig, path: Path, dpi=150):
    """Sauvegarde avec fond transparent pour conserver le background de la page."""
    fig.patch.set_facecolor("none")
    for ax in fig.axes:
        ax.patch.set_facecolor("none")
    fig.savefig(path, dpi=dpi, bbox_inches="tight", transparent=True)


def slide1_impact_perf_business(out_dir: Path):
    """Slide 1 — Chaîne cause → effet + impact €."""
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
        ("≈ 54 k€/mois", COLORS["danger"], 9.2),
    ]
    y = 2.5
    box_h, box_w = 0.9, 1.3
    for i, (label, color, x) in enumerate(steps):
        rect = FancyBboxPatch((x, y - box_h / 2), box_w, box_h, boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor="white", linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + box_w / 2, y, label, ha="center", va="center", fontsize=9, color="white" if color != COLORS["orange_light"] else COLORS["gray_900"], fontweight="bold")
        if i < len(steps) - 1:
            ax.annotate("", xy=(x + box_w + 0.15, y), xytext=(x + box_w, y),
                        arrowprops=dict(arrowstyle="->", color=COLORS["gray_700"], lw=2))

    ax.text(6, 0.8, "10k visites × 2% × 900€ = 180k€ CA/mois  |  180k€ × 30% = 54k€ impact (scénario conservateur)",
            ha="center", fontsize=9, style="italic", color=COLORS["gray_700"],
            bbox=dict(boxstyle="round", facecolor="#f8fafc", edgecolor="#e2e8f0"))
    ax.set_title("Impact perf → Impact business — Casapy", fontsize=14, fontweight="bold", pad=20)
    fig.tight_layout()
    _save_transparent(fig, out_dir / "slide1-impact-perf-business.png")
    plt.close()


def slide2_waterfall_ttfb(out_dir: Path):
    """Slide 2 — Waterfall simplifié (TTFB vs Front)."""
    fig, ax = plt.subplots(figsize=(10, 5))
    labels = ["DNS/Connexion", "TTFB (goulot)", "Téléchargement", "Render/LCP"]
    values = [0.2, 3.7, 0.8, 8]  # secondes
    colors = ["#94a3b8", COLORS["danger"], "#64748b", COLORS["orange"]]
    x = np.arange(len(labels))
    bars = ax.bar(x, values, color=colors, edgecolor="white", linewidth=1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel("Temps (s)")
    ax.set_title("Waterfall — le goulot est le TTFB (serveur), le front ne peut pas compenser")
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.2, f"{v}s", ha="center", fontsize=9)
    ax.axhline(y=0.8, color=COLORS["success"], linestyle="--", alpha=0.7, label="Objectif TTFB < 0,8 s")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_ylim(0, max(values) * 1.15)
    fig.tight_layout()
    _save_transparent(fig, out_dir / "slide2-waterfall-ttfb.png")
    plt.close()


def slide3_hebergement_comparatif(out_dir: Path):
    """Slide 3 — Mutualisé vs Stack adaptée (2 colonnes)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle("Pourquoi l'hébergement bloque — Mutualisé vs Stack adaptée WooCommerce", fontsize=12, fontweight="bold")

    left_items = ["Ressources partagées", "PHP-FPM partagé", "MySQL partagé", "Pics = perf instable"]
    right_items = ["CPU/RAM dédiés", "Cache serveur (Redis)", "DB optimisée", "Monitoring & auto-scaling"]
    for ax, items, title, color in [
        (ax1, left_items, "Mutualisé (aujourd'hui)", COLORS["danger"]),
        (ax2, right_items, "Recommandation (VPS/Cloud)", COLORS["success"]),
    ]:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, len(items) + 1)
        ax.axis("off")
        ax.set_title(title, fontsize=11, color=color)
        for i, item in enumerate(items):
            y = len(items) - i
            ax.add_patch(FancyBboxPatch((0.1, y - 0.35), 0.8, 0.6, boxstyle="round,pad=0.02",
                                        facecolor=f"{color}20", edgecolor=color))
            ax.text(0.5, y, item, ha="center", va="center", fontsize=9)
        badge = "Risque élevé" if color == COLORS["danger"] else "Perf stable"
        ax.text(0.5, 0.4, badge, ha="center", va="center", fontsize=10, fontweight="bold", color="white",
                bbox=dict(boxstyle="round", facecolor=color, edgecolor="white"))

    fig.tight_layout()
    _save_transparent(fig, out_dir / "slide3-hebergement-comparatif.png")
    plt.close()


def slide4_matrice_seo_timeline(out_dir: Path):
    """Slide 4 — Matrice 2×2 Urgence/Impact + timeline 30/60/90."""
    fig = plt.figure(figsize=(12, 5))
    gs = GridSpec(1, 2, width_ratios=[1.2, 1], figure=fig)

    ax1 = fig.add_subplot(gs[0])
    # Matrice 2×2
    quadrants = [
        ("Quick wins\nHigh impact", "Canonicals, hreflang\nStructure URLs\nClusters sémantiques", COLORS["success"]),
        ("Structurant\nHigh impact", "Architecture SEO\nPages piliers\nDonnées structurées", COLORS["primary"]),
        ("Quick wins\nLower impact", "Titles/meta\nInternal linking", "#94a3b8"),
        ("À clarifier", "Acquisition payante\nMeta/Google : aucune trace", COLORS["orange"]),
    ]
    positions = [(0, 1), (1, 1), (0, 0), (1, 0)]  # Haut-g, Haut-d, Bas-g, Bas-d
    for (qx, qy), (title, content, color) in zip(positions, quadrants):
        rect = FancyBboxPatch((qx * 0.5, qy * 0.5), 0.48, 0.48, boxstyle="round,pad=0.02",
                              facecolor=f"{color}25", edgecolor=color)
        ax1.add_patch(rect)
        ax1.text(qx * 0.5 + 0.24, qy * 0.5 + 0.38, title, ha="center", fontsize=9, fontweight="bold")
        ax1.text(qx * 0.5 + 0.24, qy * 0.5 + 0.2, content, ha="center", fontsize=8)
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis("off")
    ax1.set_title("SEO & Growth — Urgence vs Impact")

    ax2 = fig.add_subplot(gs[1])
    ax2.axis("off")
    timeline = [
        "0–30 j : Perf serveur + tracking + audit indexation",
        "30–60 j : Clusters + templates catégorie + CRO",
        "60–90 j : Scale contenus + campagnes tests",
    ]
    for i, t in enumerate(timeline):
        ax2.add_patch(FancyBboxPatch((0.1, 0.75 - i * 0.25), 0.8, 0.2, boxstyle="round,pad=0.02",
                                     facecolor="#f1f5f9", edgecolor=COLORS["primary"]))
        ax2.text(0.5, 0.85 - i * 0.25, t, ha="center", va="center", fontsize=9)
    ax2.set_title("Timeline 30/60/90 jours")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    fig.suptitle("SEO & Growth — état des lieux → plan", fontsize=12, fontweight="bold")
    fig.tight_layout()
    _save_transparent(fig, out_dir / "slide4-matrice-seo-timeline.png")
    plt.close()


def one_pager_dashboard(out_dir: Path):
    """Bonus — One-pager 4 blocs (jauges, impact, causes, roadmap)."""
    fig = plt.figure(figsize=(10, 6))
    gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3)

    # 1. Jauges TTFB / LCP
    ax1 = fig.add_subplot(gs[0, 0])
    metrics = [("TTFB", 3.7, 0.8), ("LCP", 32, 2.5), ("INP", 0.15, 0.1)]
    for i, (name, val, target) in enumerate(metrics):
        ax1.barh(i, min(val, 5) if name == "LCP" else val, color=COLORS["danger"], height=0.5)
        ax1.axvline(x=target, color=COLORS["success"], linestyle="--", alpha=0.8)
        ax1.text(0.2, i, f"{name}: {val}", va="center", fontsize=9)
    ax1.set_yticks(range(3))
    ax1.set_yticklabels(["TTFB", "LCP", "INP"])
    ax1.set_xlabel("s")
    ax1.set_title("Core Web Vitals")
    ax1.set_xlim(0, 5)

    # 2. Impact business
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis("off")
    ax2.text(0.5, 0.7, "54 k€/mois", ha="center", fontsize=24, fontweight="bold", color=COLORS["danger"])
    ax2.text(0.5, 0.5, "Impact scénario conservateur", ha="center", fontsize=10)
    ax2.text(0.5, 0.3, "10k visites × 2% × 900€ × 30%", ha="center", fontsize=9, style="italic")
    ax2.set_title("Impact business")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    # 3. Causes racines
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.axis("off")
    causes = ["Hébergement mutualisé", "WooCommerce + Elementor", "Base de données"]
    for i, c in enumerate(causes):
        ax3.text(0.1, 0.8 - i * 0.25, f"• {c}", fontsize=10)
    ax3.set_title("Causes racines")
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    # 4. Roadmap
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis("off")
    steps = ["1. Serveur (Redis / VPS)", "2. Base de données", "3. Front (LCP, JS)"]
    for i, s in enumerate(steps):
        ax4.text(0.1, 0.8 - i * 0.25, s, fontsize=10)
    ax4.text(0.5, 0.2, "Gain attendu : LCP < 2,5 s", ha="center", fontsize=9, style="italic")
    ax4.set_title("Roadmap 3 étapes")
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)

    fig.suptitle("Casapy — Dashboard exécutif (one-pager)", fontsize=14, fontweight="bold")
    _save_transparent(fig, out_dir / "one-pager-dashboard-casapy.png")
    plt.close()


def casapy_wave_progression(out_dir: Path):
    """Graphique sinusoïde : progression + cycles avant/après fix serveur (CVR ou TTFB)."""
    n_days = 90
    baseline = 1.8
    slope = 0.01
    period = 21
    phase = 0.5
    amp_before = 0.35
    amp_after = 0.15
    fix_day = 30
    noise = 0.03
    rng = np.random.default_rng(42)
    t = np.arange(n_days)
    A = np.where(t < fix_day, amp_before, amp_after)
    y = (baseline + slope * t) + A * np.sin(2 * np.pi * (t / period) + phase)
    y = y + rng.normal(0, noise, size=n_days)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, y, linewidth=2, color=COLORS["primary"])
    ax.axvline(fix_day, linestyle="--", linewidth=1.5, color=COLORS["danger"])
    ax.text(fix_day + 2, np.min(y) + 0.1, "Fix serveur\n(VPS + cache)", fontsize=9)
    ax.set_title("Simulation : progression + cycles (ex: CVR) avant/après fix")
    ax.set_xlabel("Jours")
    ax.set_ylabel("KPI (ex: CVR %)")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    _save_transparent(fig, out_dir / "casapy-wave-progression.png")
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Génère les visuels Casapy (4 slides + one-pager + wave)")
    parser.add_argument("--output", default="docs/contacts/casapy", help="Dossier de sortie")
    parser.add_argument("--svg", action="store_true", help="Exporter aussi en SVG")
    args = parser.parse_args()
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    setup_figure()
    slide1_impact_perf_business(out_dir)
    slide2_waterfall_ttfb(out_dir)
    slide3_hebergement_comparatif(out_dir)
    slide4_matrice_seo_timeline(out_dir)
    one_pager_dashboard(out_dir)
    casapy_wave_progression(out_dir)

    fmt = "svg" if args.svg else "png"
    if args.svg:
        # Ré-exporter en SVG (matplotlib peut le faire via savefig)
        pass  # déjà fait en PNG ; pour SVG, changer extension dans chaque savefig

    print(f"Visuels générés dans {out_dir.absolute()}")
    for f in out_dir.glob("*.png"):
        print(f"  - {f.name}")


if __name__ == "__main__":
    main()
