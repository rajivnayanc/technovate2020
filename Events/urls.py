from django.contrib import admin
from django.urls import path,include
from . import views
from TechnicalEvents import views as v1
from CulturalEvents import views as v2
from InformalEvents import views as v3

from event_description import views as v4

app_name = "Events"

urlpatterns = [
    path('', views.index, name='index'),

    path('culturalevents/', v2.index, name='cultural'),

    path('culturalevents/<int:id>/', v4.cultural_desc, name='cultural_desc'),

    path('technicalevents/', v1.index, name='technical'),
    path('technicalevents/<int:id>/', v4.technical_desc, name='technical_desc'),

    path('informalevents/', v3.index, name='informal'),
    path('informalevents/<int:id>/', v4.informal_desc, name='informal_desc'),
]


