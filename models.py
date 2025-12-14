from django.db import models

# Create your models here.
class Fare(models.Model):
    route = models.CharField(max_length = 50)
    base_fare = models.IntegerField(max_digits=3)
    peak_fare = models.IntegerField(max_digits=3)

class Meta:
    db_table = Fare_Chart