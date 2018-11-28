from django.urls import path
from flight.views import index, flight, book

urlpatterns = [
    path('', index, name='index'),
    path('flight/<int:flight_id>', flight, name='flight'),
    path('book/<int:flight_id>', book, name='book')
]