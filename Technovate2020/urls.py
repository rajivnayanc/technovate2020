"""Technovate2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

from Error404 import views as v1
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('HomePage.urls')),
    path('events/',include('Events.urls')),
    path('aboutus/',include('about_us.urls')),
    path('contactus/',include('contact_us.urls')),
    path('gallery/',include('gallery.urls')),
    path('preevents/',include('pre_events.urls')),
    path('sponsors/',include('sponsors.urls')),
    path('hospitality/',include('Hospitality.urls')),
    path('celebnight/',include('Celeb_Night.urls')),
    path('game/',include('game.urls')),
    path('blogs/',include('blogs.urls')),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

handler404 = v1.error404