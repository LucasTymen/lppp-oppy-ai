#!/usr/bin/env python
"""Met à jour uniquement l'email du superuser (sans toucher au mot de passe)."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lppp.settings")
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = "Lucas@dmin"
email = "lucas.tymen@gmail.com"
user = User.objects.filter(username=username).first()
if not user:
    print("Utilisateur", username, "introuvable.")
    sys.exit(1)
user.email = email
user.save()
print("Email mis à jour pour", username, ":", email)
