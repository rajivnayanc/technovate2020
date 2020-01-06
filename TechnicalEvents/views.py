from django.shortcuts import render
from django.http import HttpResponse
from Events.models import Technical
# Create your views here.

def index(request):
    event_list = Technical.objects.all()
    return render(request, 'TechnicalEvents/index.html', {'event_list': event_list})

