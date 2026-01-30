from django.contrib import admin
from .models import Campaign, Prospect


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active", "created_at")
    list_filter = ("is_active",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    list_display = ("company_name", "contact_name", "campaign", "created_at")
    list_filter = ("campaign",)
    search_fields = ("company_name", "contact_name", "email")
