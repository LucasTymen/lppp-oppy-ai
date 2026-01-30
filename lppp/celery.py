import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
apps = os.path.join(root, "apps")
for p in (apps, root):
    if p not in sys.path:
        sys.path.insert(0, p)

from celery import Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lppp.settings")
app = Celery("lppp")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
