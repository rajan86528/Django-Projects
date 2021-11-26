from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile = models.ImageField(null=True, blank=True, upload_to = "images/" ) 
    address = models.TextField(max_length=200) 
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=50)  
    pincode = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return str(self.user.username)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    
    def __str__(self):
        return str(self.user.username)
