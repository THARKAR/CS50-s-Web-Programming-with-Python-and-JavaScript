from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Flight, Airport, Passenger

# Create your views here.
def index(request):
    return render(request,'flights/index.html', {
        'flights': Flight.objects.all()
    })


def flight(req, flight_id):
    # flight = Flight.objects.get(pk=flight_id)
    flight = Flight.objects.get(id=flight_id)
    return render(req, 'flights/flight.html', {
        'flight': flight,
        'passengers': flight.passenger.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight).all()
    })



def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(id=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
        print(passenger)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight',args=(flight.id,)))

        











