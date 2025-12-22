from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length = 50, blank = True)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    birth_date = models.DateField(blank=True, null=True)
    