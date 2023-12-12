from django.contrib import admin
from django.urls import path
from DjangoCRM.apps.mycrm import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('Register/', views.Register_user, name='Register'),
]
