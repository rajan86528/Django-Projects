from django import forms
from . models import Appointment


class BookAppointment(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('required_speciality','date_of_Appointment', 'start_Time_of_Appointment')
        exclude = []