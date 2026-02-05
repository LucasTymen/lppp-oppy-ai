from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.scraping.flowise_client import get_flowise_chat_embed_url


class EssaisIndexView(LoginRequiredMixin, TemplateView):
    """Premier écran : présentation relance salon — positionnement freelance/alternant, ciblage activité/pain points."""

    template_name = "landingsgenerator/index.html"
    login_url = "/admin/login/"


class ConciergeChatView(LoginRequiredMixin, TemplateView):
    """Interface de test du chatbot Concierge IA (Flowise). Affiche l'embed du chatflow si FLOWISE_CHATFLOW_ID est configuré."""

    template_name = "landingsgenerator/concierge_chat.html"
    login_url = "/admin/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flowise_embed_url"] = get_flowise_chat_embed_url()
        return context
