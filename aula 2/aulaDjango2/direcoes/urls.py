from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/norte', views.norte),
    path('/sul', views.sul),
    path('/leste', views.leste),
    path('/oeste', views.oeste)
]