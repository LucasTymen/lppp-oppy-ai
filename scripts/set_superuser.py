#!/usr/bin/env python
"""Crée ou met à jour le superuser Django. Variables requises : DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lppp.settings")
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
if not all([username, email, password]):
    print("Usage: DJANGO_SUPERUSER_USERNAME=... DJANGO_SUPERUSER_EMAIL=... DJANGO_SUPERUSER_PASSWORD=... python3 scripts/set_superuser.py")
    sys.exit(1)
user, created = User.objects.get_or_create(username=username, defaults={"email": email})
user.email = email
user.set_password(password)
user.is_superuser = True
user.is_staff = True
user.is_active = True
user.save()
print("Superuser OK:", username, "(créé)" if created else "(mis à jour)")
