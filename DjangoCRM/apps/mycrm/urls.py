from django.contrib import admin
from django.urls import path
from DjangoCRM.apps.mycrm import views

urlpatterns = [
    path('', views.home, name='home'),
]
