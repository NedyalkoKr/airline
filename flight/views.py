from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from flight.models import Flight, Passenger

def index(request):
    ''' display all flights '''
    context = {
        'main_header': 'Flights',
        'title': 'Flights',
        'flights': Flight.objects.all()
    }
    return render(request, 'flight/index.html', context)

def flight(request, flight_id):
    ''' return individual flight details and passengers on this flight'''
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404(f'Flight {flight} does not exist.')
    context = {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flight=flight).all(),
        'number_of_passengers': flight.passengers.count()
    }

    return render(request, 'flight/flight.html', context)


def book(request, flight_id):
    try:
        passenger_id = int(request.POST['passenger'])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, 'flight/error.html', {'message': 'No passenger selected'})
    except Flight.DoesNotExist:
        return render(request, 'flight/error.html', {'message': 'No such flight exist'})
    except Passenger.DoesNotExist:
        return render(request, 'flight/error.html', {'message': 'No passenger with that id exist'})

    passenger.flight.add(flight)
    return HttpResponseRedirect(reverse('flight', args=(flight_id,)))