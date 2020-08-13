import os
import sys

path = '/home/bst/django_app/portfolio_app_v2'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_app.settings')
application = get_wsgi_application()
