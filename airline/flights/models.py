from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.city} ({self.code})'


class Flight(models.Model):
    # origin will use the forgien key to get the data from Airport Model (Table)
    # models.CASCADE will delete Flight if Airport Data is deleted
    # related_name will give the access to get the flight
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()


    # String Representation or Dundar method for expressing string format of the object
    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination} '
















