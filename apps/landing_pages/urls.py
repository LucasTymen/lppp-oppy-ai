from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_list),
    path("p/<slug:slug>/", views.landing_public, name="landing_public"),
    path("p/<slug:slug>/rapport/", views.landing_rapport, name="landing_rapport"),
    path("p/<slug:slug>/prospects/", views.landing_prospects, name="landing_prospects"),
    path("p/<slug:slug>/proposition/", views.landing_proposition_value, name="landing_proposition_value"),
]
