from django.shortcuts import render
from .models import Gallery
# Create your views here.

def index(request):
    images = Gallery.objects.all()
    context = {
        'images':images
    }
    return render(request,'gallery/index.html',context=context)
