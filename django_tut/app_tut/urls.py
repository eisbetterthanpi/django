# from django.contrib import admin
from django.urls import path#, include
from . import views

urlpatterns = [
    path('', views.home, name="app_tut-home"),
    path('about/', views.about, name="app_tut-about"),
]
