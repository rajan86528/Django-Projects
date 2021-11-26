from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_view, name='home'),
]
