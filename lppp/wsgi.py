import os
import sys

# PYTHONPATH apps/ (stratégie SquidResearch)
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
apps = os.path.join(root, "apps")
for p in (apps, root):
    if p not in sys.path:
        sys.path.insert(0, p)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lppp.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
