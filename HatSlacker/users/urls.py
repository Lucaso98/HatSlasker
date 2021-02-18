from django.urls import path
from . import views

urlpatterns = [
    path('', views.hem, name='hem'),
    path('nyanvandare/', views.nyanvandare, name='nyanvandare'),
    path('felbrodyr/', views.felbrodyr, name='felbrodyr'),
    path('minskalager/', views.minskalager, name='minskalager'),
]