from django.shortcuts import render

from rest_framework import generics
from .serializers import InsuranceSerializer
from .models import Insurance

class InsuranceList(generics.ListCreateAPIView):
    queryset = Insurance.objects.all().order_by('id')
    serializer_class = InsuranceSerializer

class InsuranceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insurance.objects.all().order_by('id')
    serializer_class = InsuranceSerializer
