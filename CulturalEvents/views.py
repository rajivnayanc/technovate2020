from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Events.models import Cultural


def index(request):
    event_list = Cultural.objects.all()
    return render(request,'CulturalEvents/index.html',{'event_list':event_list})
