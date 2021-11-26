from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction, models
from .models import User,Patient, Doctor

class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    profile = models.ImageField(null=False, blank=False) 
    address = models.TextField(max_length=200) 
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=50)  
    pincode = models.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name','profile', 'address', 'city', 'state', 'pincode', 'password1', 'password2')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.profile = self.cleaned_data.get('profile')
        user.address = self.cleaned_data.get('address')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.pincode = self.cleaned_data.get('pincode')
        user.save()
        patient = Patient.objects.create(user=user)
        patient.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    profile = models.ImageField(null=False, blank=False) 
    address = models.TextField(max_length=200) 
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=50)  
    pincode = models.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name','profile', 'address', 'city', 'state', 'pincode', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.profile = self.cleaned_data.get('profile')
        user.address = self.cleaned_data.get('address')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.pincode = self.cleaned_data.get('pincode')
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.save()
        return user
