from django.shortcuts import render

# Create your views here.

def error404(request,exception):
    data = {}
    return render(request,'Error404/index.html',data)
