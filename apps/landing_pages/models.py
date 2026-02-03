from django.db import models
from django.conf import settings


class LandingPage(models.Model):
    """Landing page personnalisée pour une cible de prospection."""

    SECTOR_CHOICES = [
        ("cybersecurite", "Cybersécurité / OT-IT"),
        ("juridique", "Juridique / Cabinets avocats"),
        ("industrie", "Industrie"),
        ("low-tech", "Low tech / Sans tech"),
        ("autre", "Autre"),
    ]
    CATEGORY_CHOICES = [
        ("relance-evenement", "Relance événement"),
        ("proposition", "Proposition / Mission"),
        ("lead-magnet", "Lead magnet"),
        ("lowtech", "Low tech / Sans tech"),
        ("autre", "Autre"),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100)
    prospect_name = models.CharField(max_length=200, blank=True)
    prospect_company = models.CharField(max_length=200, blank=True)
    sector = models.CharField(
        max_length=40, choices=SECTOR_CHOICES, default="autre", blank=True
    )
    category = models.CharField(
        max_length=40, choices=CATEGORY_CHOICES, default="autre", blank=True
    )
    template_key = models.CharField(max_length=80, default="default")
    content_json = models.JSONField(default=dict, blank=True)
    is_published = models.BooleanField(default=False)
    # URL du déploiement standalone (Vercel) — pour traçage et console
    deploy_url = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="landing_pages",
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Landing page"
        verbose_name_plural = "Landing pages"

    def __str__(self):
        return f"{self.title} ({self.slug})"
