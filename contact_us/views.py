from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Messages
# Create your views here.

def index(request):
    return render(request,'contact_us/index.html')

def query(request):
    if request.method=='POST':
        message = Messages()

        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.phone = request.POST.get('phone')
        message.institute = request.POST.get('institute')
        message.message = request.POST.get('message')
        message.save()

        context = {'message': 'Done'}
        return render(request,'contact_us/index.html',context)
    else:
        context = {'message': 'Invalid Request'}
        return render(request,'contact_us/index.html',context)
