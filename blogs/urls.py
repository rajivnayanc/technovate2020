from django.contrib import admin
from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.blogindex, name='blogindex'),
]
