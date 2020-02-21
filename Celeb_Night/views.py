from django.shortcuts import render
from .models import Celeb_Images
# Create your views here.

def index(request):
    objects = Celeb_Images.objects.all()
    status = True 
    if len(objects)==0:
        status=False
    context = {
        'data':objects,
        'status':status
    }
    return render(request,'Celeb_Night/hospitality.html',context=context)