from django.contrib import admin
from django.urls import path
from . import views
from event_description import views as v1
app_name = "CulturalEvents"
urlpatterns = [
    path('', views.index, name='index'),
]
