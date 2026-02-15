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
    path("p/<slug:slug>/", views.landing_public, name="landing_public"),
    path("p/<slug:slug>/rapport/", views.landing_rapport, name="landing_rapport"),
    path("p/<slug:slug>/prospects/", views.landing_prospects, name="landing_prospects"),
    path("p/<slug:slug>/proposition/", views.landing_proposition_value, name="landing_proposition_value"),
]
