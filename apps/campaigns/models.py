from django.db import models
from django.conf import settings


class Campaign(models.Model):
    """Campagne de prospection (cibles, landing pages, statut)."""
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="campaigns",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Prospect(models.Model):
    """Cible de prospection (entreprise / contact)."""
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="prospects",
    )
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    landing_page = models.OneToOneField(
        "landing_pages.LandingPage",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prospect",
    )
    enriched_data = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["company_name"]

    def __str__(self):
        return f"{self.company_name} ({self.campaign.name})"
