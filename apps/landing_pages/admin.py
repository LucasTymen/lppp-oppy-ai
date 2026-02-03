from django.contrib import admin
from .models import LandingPage


@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "prospect_company", "sector", "category", "is_published", "deploy_url", "created_at")
    list_filter = ("is_published", "template_key", "sector", "category")
    search_fields = ("title", "slug", "prospect_name", "prospect_company")
    prepopulated_fields = {"slug": ("title",)}
