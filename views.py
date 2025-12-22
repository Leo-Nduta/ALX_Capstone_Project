from django.shortcuts import render
from datetime import datetime, time
from .models import Fare

# Create your views here.
peak_hours = [
    (time(16, 0), time(20, 0)),
    (time(6, 0), time(10))
]

def is_peak_hour(current_time, base_fare, peak_fare):
    for start, end in peak_hours:
        if start <= current_time <= end:
            return peak_fare
    return base_fare
