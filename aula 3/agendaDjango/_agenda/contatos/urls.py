from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('amigos/', views.amigos, name='amigos'),
    path('familia/', views.familia, name='familia'),
    path('empresa/', views.empresa, name='empresa'),
]