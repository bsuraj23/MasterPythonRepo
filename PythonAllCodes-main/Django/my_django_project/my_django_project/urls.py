import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'my_django_project' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_project.settings')

# Get the WSGI application for the project.
application = get_wsgi_application()

# Install Django package
os.system('pip install django')

# Apply database migrations
os.system('python manage.py migrate')

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]