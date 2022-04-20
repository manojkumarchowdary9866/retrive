from django.shortcuts import render

from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topic(request):
    topics=topic.objects.all()

    d={'ts':topics}
    return render(request,'display_topic.html',d)



def display_webpage(request):
    webpages=webpage.objects.all()
    webpages=webpage.objects.filter(topic_name='football')

    #webpages=webpage.objects.exclude(topic_name='football')
    #webpages=Webpage.objects.all()[0:2:]
    #webpages=Webpage.objects.all()[-3]
    #Wwebpages=webpage.objects.all().order_by('name')
    #webpages=webpage.objects.all().order_by('-name')
    #webpages=webpage.objects.all().order_by(Length('name'))
    #webpages=webpage.objects.all().order_by(Length('name').desc())
    #webpages=webpage.objects.filter(name__startswith='R')
    #webpages=webpage.objects.filter(name__endswith='i')
    #webpages=webpage.objects.filter(name__contains='t')
    #webpages=webpage.objects.filter(name__in=('dhoni','Thomas'))
    #webpages=webpage.objects.filter(name__regex=r'^[a-zA-Z]{2}o')
    #webpages=webpage.objects.filter(Q(topic_name='football') & Q(name='James'))
    #webpages=webpage.objects.filter(Q(topic_name='football') & Q(url__startswith='https') & Q(name__endswith='s'))

    d={'ws':webpages}
    return render(request,'display_webpage.html',d)



def display_access(request):
    #access=AccessRecord.objects.all()
    #access=AccessRecord.objects.filter(date='1991-12-16')
    #access=AccessRecord.objects.filter(date__gte='1991-12-16')
    #access=AccessRecord.objects.filter(date__lt='2010-03-28')
    #access=AccessRecord.objects.filter(date__year='2003')
    #access=AccessRecord.objects.filter(date__year__gt='2003')
    #access=AccessRecord.objects.filter(date__month='12')
    access=AccessRecord.objects.filter(date__day='28')
    d={'ac':access}
    return render(request,'display_access.html',d)
def update_webpage(request):
    #webpage.objects.filter(topic_name='football').update(name='Ronaldo')
    #webpage.objects.filter(name='Thomas').update(url='http://Steven.com/')
    #webpage.objects.update_or_create(name='Rachel',defaults={'url':'http://manoj.com'})
    t=topic.objects.get_or_create(topic_name='Rugbi')[0]
    t.save()
    webpage.objects.update_or_create(topic_name='Rugbi',defaults={'topic_name':t,'name':'Rugbi Star','url':'http://Ronaldo.com/'})

    webapges=webpage.objects.all()
    d={'ws':webapges}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):
    #webpage.objects.filter(name='Ronaldo').delete()
    webpage.objects.all().delete()
    webapges=webpage.objects.all()
    d={'ws':webapges}
    return render(request,'display_webpage.html',d)


