from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_list),
    path("p/<slug:slug>/", views.landing_public, name="landing_public"),
]
