from django.contrib import admin

# Register your models here.
from .models import Event, Slide, Card, TeamMember

admin.site.register(Event)
admin.site.register(Slide)
admin.site.register(Card)
admin.site.register(TeamMember)