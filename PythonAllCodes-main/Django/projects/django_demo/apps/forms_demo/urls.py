from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='forms_example'),
]
