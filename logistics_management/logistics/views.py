from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Shipper
from .serializers import CustomerSerializer, ShipperSerializer, ConsignmentSerializer
from .mongo_models import Consignment

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ShipperViewSet(ModelViewSet):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer

class ConsignmentViewSet(ViewSet):
    def list(self, request):
        consignments = Consignment.find({})
        return Response(consignments)

    def create(self, request):
        serializer = ConsignmentSerializer(data=request.data)
        if serializer.is_valid():
            Consignment.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
