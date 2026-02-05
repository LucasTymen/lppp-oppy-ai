#!/usr/bin/env python
"""Affiche les superusers (username, email). À lancer depuis la racine : python3 scripts/show_superusers.py"""
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
    print("Aucun superuser en base. Créer un compte : python3 manage.py createsuperuser")
else:
    for u in users:
        print("username:", u.username)
        print("email:", u.email)
        print("is_active:", u.is_active)
