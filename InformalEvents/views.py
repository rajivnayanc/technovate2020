from django.shortcuts import render
from django.http import HttpResponse

from Events.models import Informal
# Create your views here.

def index(request):
    event_list = Informal.objects.all()
    return render(request,'InformalEvents/index.html',{'event_list':event_list})
