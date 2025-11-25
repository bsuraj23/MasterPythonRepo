from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('templates/', include('apps.templates_demo.urls')),
    path('forms/', include('apps.forms_demo.urls')),
    path('models/', include('apps.models_demo.urls')),
    path('auth_demo/', include('apps.auth_demo.urls')),
    path('views_demo/', include('apps.views_demo.urls')),
    path('ms/', include('apps.middleware_signals.urls')),
    path('state/', include('apps.state_demo.urls')),
    path('advanced/', include('apps.advanced.urls')),
]
