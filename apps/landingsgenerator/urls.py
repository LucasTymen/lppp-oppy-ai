from django.urls import path
from . import views

app_name = "landingsgenerator"

urlpatterns = [
    path("", views.EssaisIndexView.as_view(), name="index"),
]
