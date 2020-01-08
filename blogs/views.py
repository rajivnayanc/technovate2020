from django.shortcuts import render
from .models import Blogs
# Create your views here.
def index(request):
    blogs = Blogs.objects.all().order_by('-post_date')
    context = {
        'blogs':blogs
    }
    return render(request,'blogs/index.html',context=context)

def blogindex(request,id):
    blog = Blogs.objects.get(pk=id)
    context = {
        'blog':blog
    }
    return render(request, 'blogs/posts.html',context=context)
