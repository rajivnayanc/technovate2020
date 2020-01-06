from django.contrib import admin
from django.urls import path
from . import views

app_name = "sponsors"
urlpatterns = [
    path('',views.index,name='index'),
    path('success/',views.query,name='query'),
    path('previoussponsors/',views.previous,name='previous'),
]

