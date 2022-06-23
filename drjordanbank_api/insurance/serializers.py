from rest_framework import serializers
from .models import Insurance

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ('id', 'company', 'accountHolder', 'policyNumber', 'idNumber')
