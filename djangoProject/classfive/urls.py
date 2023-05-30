from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("calendar", views.calendar),
    path("subscribe", views.subscribe),
    path("about", views.about),
    path("shop", views.shop),
]