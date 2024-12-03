from django.test import TestCase
from .models import Customer, Shipper, Consignment

class CustomerModelTest(TestCase):
    def setUp(self):
        Customer.objects.create(name="John Doe", address="123 Main St", phone="1234567890")

    def test_customer_str(self):
        customer = Customer.objects.get(id=1)
        self.assertEqual(str(customer), "John Doe")