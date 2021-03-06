from rest_framework import viewsets

from myapp.models import Customer
from rest.serializer import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
