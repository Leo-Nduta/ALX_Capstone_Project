from django.shortcuts import render
from datetime import time
from .models import BusRoute, Stage, BusFare
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BusRouteSerializer
from .data import stage_names

# Create your views here.
peak_hours = [
    (time(16, 0), time(20, 0)),
    (time(6, 0), time(9,0))
]

def is_peak_time(current_time, base_fare, peak_fare):
    for start, end in peak_hours:
        if start <= current_time <= end:
            return peak_fare
    return base_fare

class BusRouteListView(APIView):
    def get(self, request):
        routes = BusRoute.objects.filter(origin="Ngong", destination="Nairobi")
        serializer = BusRouteSerializer(routes, many=True)
        return Response(serializer.data)

from restframework.permissions import IsAdminUser
class FareUpdateView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        pass

class FareQueryView(APIView):
    def post(self, request):
        boarding_stage_id = request.data.get('boarding_stage_id')
        destination_stage_id = request.data.get('destination_stage_id')
        
        if not boarding_stage_id or not destination_stage_id:
            return Response(
                {
                    "error": "both boarding_stage_id and destination_stage_id are required",
                    "available stages": stage_names
                }, status=400
            )
        try:
            boarding_stage = Stage.objects.get(id=boarding_stage_id)
        except Stage.DoesNotExist:
            return Response(
                {
                    "error": "Invalid boarding_stage_id",
                    "available stages": stage_names
                }, status=400
            )
        
        try:
            destination_stage = Stage.objects.get(id=destination_stage_id)
        except Stage.DoesNotExist:
            return Response(
                {
                    "error": "Invalid destination_stage_id",
                    "available stages": stage_names
                }, status=400
            )
        
        fare = BusFare.objects.get(
            from_zone = boarding_stage.zone,
            to_zone = destination_stage.zone
        )
        amount = fare.peak_fare if request.data.get('is_peak_time') else fare.base_fare
        return Response(
            {
                "boarding_stage": boarding_stage.name,
                "destination_stage": destination_stage.name,
                "from zone": boarding_stage.zone.name,
                "to zone": destination_stage.zone.name,
                "fare_amount": amount
            }
        )