from django.urls import path
from . import views

app_name = 'middleware_signals'

urlpatterns = [
    path('ping/', views.ping_view, name='ping'),
    path('headers/', views.header_echo, name='headers'),
]
