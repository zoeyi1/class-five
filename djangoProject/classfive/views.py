from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from .models import event, slide, card

def home(request):
    eventInstances = event.objects.all()
    slideInstances = slide.objects.all()
    return render(request, "classfive/home.html", {"eventInstances": eventInstances, "slideInstances": slideInstances})

def calendar(request):
    cardInstances = card.objects.all()
    return render(request, "classfive/calendar.html", {"cardInstances": cardInstances})

def subscribe(request):
    return render(request, "classfive/subscribe.html")

def about(request):
    return render(request, "classfive/about.html")

def shop(request):
    return render(request, "classfive/shop.html")