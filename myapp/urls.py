from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
]
