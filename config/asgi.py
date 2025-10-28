"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
>>>>>>> 525a4ba (Сделана первая версия МП для ДЗ)

application = get_asgi_application()
