from django.shortcuts import render

from rest_framework import generics
from .serializers import AppointmentSerializer
from .models import Appointment

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all().order_by('id')
    serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all().order_by('id')
    serializer_class = AppointmentSerializer
