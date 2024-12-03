from rest_framework import serializers
from .models import Customer, Shipper

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = '__all__'

class ConsignmentSerializer(serializers.Serializer):
    customer = serializers.CharField(max_length=255)
    shipper = serializers.CharField(max_length=255)
    description = serializers.CharField()
    status = serializers.CharField()
    created_at = serializers.DateTimeField()
