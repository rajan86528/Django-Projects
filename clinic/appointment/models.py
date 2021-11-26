from django.db import models
from django.conf import settings
from account.models import User
# Create your models here.

class Appointment(models.Model):
    appointment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    required_speciality = models.CharField(max_length=100, blank=False)
    date_of_Appointment = models.DateField(blank=False)
    start_Time_of_Appointment = models.TimeField(blank=False)

    def __str__(self):
        return str(self.required_speciality)