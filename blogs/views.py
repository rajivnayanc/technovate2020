from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'blogs/index.html')

def blogindex(request,id):
    return render(request, 'blogs/posts.html')
