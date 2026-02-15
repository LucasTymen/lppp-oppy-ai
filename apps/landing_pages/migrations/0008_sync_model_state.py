# Synchronisation état du modèle (pas de changement de schéma en base)
# Résout : "Your models in app(s): 'landing_pages' have changes that are not yet reflected in a migration"

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landing_pages", "0007_add_yuwell_portfolio_landing"),
    ]

    operations = [
        migrations.AlterField(
            model_name="landingpage",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("relance-evenement", "Relance événement"),
                    ("proposition", "Proposition / Mission"),
                    ("lead-magnet", "Lead magnet"),
                    ("lowtech", "Low tech / Sans tech"),
                    ("autre", "Autre"),
                ],
                default="autre",
                max_length=40,
            ),
        ),
    ]
