from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

def index(request):
    return render(request, "classfive/index.html")

def calendar(request):
    return render(request, "classfive/calendar.html")

def subscribe(request):
    return render(request, "classfive/subscribe.html")

def about(request):
    return render(request, "classfive/about.html")
