from django.shortcuts import render
from datetime import time
from .models import BusRoute
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BusRouteSerializer

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

class BusRouteListView(APIView):
    def get(self, request):
        routes = BusRoute.objects.filter(origin="Ngong", destination="Nairobi")
        serializer = BusRouteSerializer(routes, many=True)
        return Response(serializer.data)
