#!/usr/bin/env python
"""Affiche les superusers (username, email, is_staff, is_active)."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lppp.settings")
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
users = list(User.objects.filter(is_superuser=True))
if not users:
    print("Aucun superuser en base.")
else:
    for u in users:
        print("username:", repr(u.username))
        print("email:", repr(u.email))
        print("is_staff:", u.is_staff, "is_active:", u.is_active)
        print("---")
