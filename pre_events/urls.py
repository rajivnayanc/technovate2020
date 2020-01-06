from django.contrib import admin
from django.urls import path
from . import views

app_name = "PreEvents"
urlpatterns = [
    path('',views.index,name='index'),
]

