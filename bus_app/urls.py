from django.urls import path, include
from accounts import views

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('bus-routes/', views.BusRouteListView.as_view(), name='bus-routes'),
]