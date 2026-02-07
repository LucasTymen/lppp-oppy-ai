from django.contrib import admin
from django.utils.html import format_html
from .models import LandingPage


@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "prospect_company",
        "sector",
        "category",
        "template_key",
        "is_published",
        "lien_voir_landing",
        "deploy_url",
        "created_at",
    )
    list_display_links = ("title", "slug")
    list_filter = ("is_published", "template_key", "sector", "category")
    search_fields = ("title", "slug", "prospect_name", "prospect_company")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["-updated_at"]
    list_per_page = 25
    date_hierarchy = "created_at"

    @admin.display(description="Voir la landing")
    def lien_voir_landing(self, obj):
        url = obj.get_absolute_url()
        return format_html(
            '<a href="{}" target="_blank" rel="noopener">Ouvrir</a>',
            url,
        )
