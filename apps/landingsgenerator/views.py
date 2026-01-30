from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class EssaisIndexView(LoginRequiredMixin, TemplateView):
    """Premier écran : présentation relance salon — positionnement freelance/alternant, ciblage activité/pain points."""

    template_name = "landingsgenerator/index.html"
    login_url = "/admin/login/"
