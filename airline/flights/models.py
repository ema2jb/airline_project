from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length= 64)


    def __str__(self):
        return f"{self.code}({self.city})"


class flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} takes {self.duration}"

class passenger(models.Model):
    first = models.CharField(max_length = 64)
    last = models.CharField(max_length = 64)
    flights = models.ManyToManyField(flight, blank=True, related_name ="passenger")

    def __str__(self):
        return f"{self.first} {self.last}"
