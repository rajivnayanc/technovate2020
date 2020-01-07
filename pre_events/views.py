from django.shortcuts import render
from .models import PreEvent
# Create your views here.
def index(request):
    event_list = PreEvent.objects.all().order_by('-id')
    context = {
        'event_list': event_list
    }
    # print(event_list)
    return render(request,'pre_events/index.html',context = context)
