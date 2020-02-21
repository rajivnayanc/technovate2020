from django.shortcuts import render
from django.http import HttpResponse
from .models import Links
# Create your views here.
def index(request):
    output = Links.objects.get(pk=1)
    return render(request,'HomePage/index.html',context={'output':output})

