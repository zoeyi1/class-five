from django.urls import path
from . import views

app_name = 'classfive' # necessary for inquiry form

urlpatterns = [
    path("", views.home),
    path("events", views.events),
    path("contact", views.contact, name='contact'), # name='contact' necessary for inquiry form
    path("philosophy", views.philosophy),
    path("merch", views.merch),
    path("training", views.training),
    path("about", views.about),
    path("team", views.team)
]