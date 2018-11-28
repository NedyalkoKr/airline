from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.city} - {self.code}'


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.PositiveIntegerField()

    def __str__(self):
        return  f'From {self.origin} to {self.destination}' 


class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    flight = models.ManyToManyField(Flight, blank=True, related_name='passengers')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'