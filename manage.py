#!/usr/bin/env python
"""Django's manage.py — PYTHONPATH inclut apps/ (stratégie SquidResearch)."""
import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lppp.settings")
    # Injecter apps/ dans le PYTHONPATH pour imports métier
    root = os.path.dirname(os.path.abspath(__file__))
    apps_path = os.path.join(root, "apps")
    if apps_path not in sys.path:
        sys.path.insert(0, apps_path)
    if root not in sys.path:
        sys.path.insert(0, root)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
