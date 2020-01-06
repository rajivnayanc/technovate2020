from django.shortcuts import render
from .models import SponsorContact
# Create your views here.
from .models import SponsorType
from .models import Sponsor

def index(request):
    sponsorsType = list(SponsorType.objects.all())

    sponsors = {}
    for s in sponsorsType:
        q = Sponsor.objects.all().filter(types=s)
        if q.exists():
            sponsors[s] = q
        else:
            sponsors[s] = None

    context = {
        'sponsors':sponsors
    }

    return render(request,'sponsors/sponsors.html',context=context)


def previous(request):
    return render(request, 'sponsors/previous.html')


def query(request):
    if request.method == 'POST':
        message = SponsorContact()
        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.save()

        context = {'message': "Thank You! We'll contact you soon!"}
        return render(request, 'sponsors/sponsors.html', context)
    else:
        context = {'message': 'Invalid Request'}
        return render(request, 'sponsors/sponsors.html', context)
