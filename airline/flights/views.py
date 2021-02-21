from django.shortcuts import render
from flights.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {"flights":flight.objects.all()})

def fly(request, flight_id):
    fli = flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {"flig":fli,
    "passengers":fli.passenger.all(),
    "non_passengers":passenger.objects.exclude(flights=fli).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        fly = flight.objects.get(pk = flight_id)
        person = passenger.objects.get(pk = int(request.POST["passenger"]))
        person.flights.add(fly)
        return HttpResponseRedirect(reverse("flights:flight", args = [fly.id]))
