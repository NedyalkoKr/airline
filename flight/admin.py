from django.contrib import admin
from flight.models import Flight, Airport, Passenger

@admin.register(Flight)
class FligtAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'duration',)
    list_filter = ('origin', 'destination',)
    search_fields = ('origin', 'destinaiton',)

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('city', 'code',)

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name', 'flight')
    search_fields = ('first_name', 'last_name', 'flight')
    filter_horizontal = ('flight',)