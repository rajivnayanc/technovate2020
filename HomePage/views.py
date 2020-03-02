from django.shortcuts import render
from django.http import HttpResponse
from .models import Links
# Create your views here.
def index(request):
    output = Links.objects.all()[:1].get()
    return render(request,'HomePage/index.html',context={'output':output})

