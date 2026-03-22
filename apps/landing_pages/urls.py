from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_list),
    path("console/", views.console_landings, name="console_landings"),
    path(
        "maisons-alfort/",
        lambda req: redirect("landing_public", slug="maisons-alfort", permanent=False),
        name="concierge_maisons_alfort_public",
    ),
    path("yuwell/", views.yuwell_portfolio, name="yuwell_portfolio"),
    path("yuwell", views.yuwell_portfolio),
    path("yuwell/presentation/", views.yuwell_presentation, name="yuwell_presentation"),
    path("yuwell/study-case/", views.yuwell_study_case, name="yuwell_study_case"),
    path("yuwell/study-case-2/", views.yuwell_study_case_2, name="yuwell_study_case_2"),
    path("yuwell/charte-graphique/", views.yuwell_charte_graphique, name="yuwell_charte_graphique"),
    path("yuwell/a-propos/", views.yuwell_a_propos, name="yuwell_a_propos"),
    # Casapy assets et dashboard (même URL servie par la vue générique)
    path("p/casapy/assets/<path:filename>", views.serve_casapy_asset, name="casapy_assets"),
    path("p/casapy/audit-dashboard/", views.casapy_audit_dashboard, name="casapy_audit_dashboard"),
    # Promovacances assets (infographie 7 formats, images)
    path("p/promovacances/assets/<path:filename>", views.serve_promovacances_asset, name="promovacances_assets"),
    # Infopro assets (infographie 7 formats, positionnement-marketing, images)
    path("p/infopro/assets/<path:filename>", views.serve_infopro_asset, name="infopro_assets"),
    # LPPP-OppyAI — assets statiques (infographie, positionnement, etc.)
    path("p/lppp-oppy-ai/assets/<path:filename>", views.serve_lppp_oppy_ai_asset, name="lppp_oppy_ai_assets"),
    # Rougier & Ple assets (infographie 7 formats, positionnement-marketing, CSS)
    path("p/rougier-et-ple/assets/<path:filename>", views.serve_rougier_et_ple_asset, name="rougier_et_ple_assets"),
    # Dashboard audit SEO : 1 template + 1 JSON par projet (docs/contacts/<slug>/audit-dashboard.json)
    path("p/<slug:slug>/audit-dashboard/", views.seo_audit_dashboard, name="seo_audit_dashboard"),
    path("p/<slug:slug>/", views.landing_public, name="landing_public"),
    path("p/<slug:slug>/rapport/", views.landing_rapport, name="landing_rapport"),
    path("p/<slug:slug>/prospects/", views.landing_prospects, name="landing_prospects"),
    path("p/<slug:slug>/proposition/", views.landing_proposition_value, name="landing_proposition_value"),
]
