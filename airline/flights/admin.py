from django.contrib import admin
# Register your models here.
from .models import *

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(flight, FlightAdmin)
admin.site.register(passenger, PassengerAdmin)
