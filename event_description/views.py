from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from Events import models


def cultural_desc(request,id):
    # return HttpResponse("Hello")
    event = models.Cultural.objects.get(pk=id)
    context = {
        'title':'Cultural Event',
        'event':event
    }
    return render(request,'event_description/index.html',context=context)


def technical_desc(request, id):
    # return HttpResponse("Hello")
    event = models.Technical.objects.get(pk=id)
    context = {
        'title': 'Technical Event',
        'event': event
    }
    return render(request, 'event_description/index.html', context=context)


def informal_desc(request, id):
    # return HttpResponse("Hello")
    event = models.Informal.objects.get(pk=id)
    context = {
        'title': 'Informal Event',
        'event': event
    }
    return render(request, 'event_description/index.html', context=context)

