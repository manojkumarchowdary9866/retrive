from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    topics=topic.objects.all()

    d={'ts':topics}
    return render(request,'display_topic.html',d)



def display_webpage(request):
    webpages=webpage.objects.all()
    d={'ws':webpages}
    return render(request,'display_webpage.html',d)


def display_access(request):
    access=AccessRecord.objects.all()
    d={'ac':access}
    return render(request,'display_access.html',d)