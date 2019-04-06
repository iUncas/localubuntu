
#WSGI config for web project.

#It exposes the WSGI callable as a module-level variable named ``application``.

#For more information on this file, see
#https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/


import os
import os
import time
import traceback
import signal
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/python-cgi/web')
# adjust the Python version in the line below as needed
#sys.path.append('/home/wojtek/python/env/lib/python3.6/site-packages')
sys.path.append('/home/wojtek/python/env/lib/python3.5/site-packages/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

application = get_wsgi_application()
