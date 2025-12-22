from django.urls import path, include
from accounts import views

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
]