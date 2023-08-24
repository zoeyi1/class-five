from django.contrib import admin

# Register your models here.
from .models import event, slide, card

admin.site.register(event)
admin.site.register(slide)
admin.site.register(card)