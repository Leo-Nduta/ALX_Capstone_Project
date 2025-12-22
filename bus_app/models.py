from django.db import models

# Create your models here.
class BusFare(models.Model):
    route = models.CharField(max_length = 50)
    base_fare = models.IntegerField()
    peak_fare = models.IntegerField()

class Meta:
    db_table = 'Fare_Chart'

class Bus(models.Model):
    sacco = models.CharField(max_length = 20)
    fare = models.ForeignKey(BusFare, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sacco

class Bus_Route(models.Model):
    sacco = models.ForeignKey(Bus, on_delete=models.CASCADE)
    origin = models.CharField(max_length = 20)
    destination = models.CharField(max_length = 20)
    duration = models.DurationField()
    stage_count = models.IntegerField(default = 0)
    distance_km = models.FloatField()
    
    def __str__(self):
        return f"{self.origin} to {self.destination}: {self.base_fare} (Base), {self.peak_fare} (Peak)"