from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('traffic/', views.traffic, name='traffic'),
    path('logs/', views.logs, name='logs'),
    path('analytics/', views.analytics, name='analytics'),
    path('blocks/', views.blocks, name='blocks'),
]