from django.urls import path
from . import views

app_name = 'appointment'


urlpatterns = [
    path('create_appontment/', views.BookAppointmentView, name='create_appontment'),
    path('appointment_list/', views.AppointmentListView.as_view(), name='appointment_list'),
]
