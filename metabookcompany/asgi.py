"""
ASGI config for metabookcompany project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
"""
Created by Usukhbayar Otgonbat
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metabookcompany.settings')

application = get_asgi_application()
