from django.shortcuts import render, redirect
from appointment .models import Appointment
from django.contrib.auth.decorators import login_required
from appointment .forms import BookAppointment
from account.models import User
from django.views.generic import ListView

class AppointmentListView(ListView):
    model = Appointment
    template_name = '../templates/appointment_list.html'
    context_object_name = 'appointment'

def BookAppointmentView(request):
    user = request.user
    form = BookAppointment(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        appointment_user = User.objects.filter(email=user.email).first()
        obj.appointment_user = appointment_user
        obj.save()
        form = BookAppointment()
    
    return render(request, '../templates/create_appointment.html', {'form':form})
