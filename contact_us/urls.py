from django.contrib import admin
from django.urls import path
from . import views

app_name = "ContactUs"
urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.query, name='query'),
]
