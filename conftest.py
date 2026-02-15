# Pytest root conftest — charge Django (PostgreSQL uniquement, pas de SQLite)
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lppp.settings")
django.setup()
