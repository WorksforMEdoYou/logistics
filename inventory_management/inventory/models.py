from django.db import models
from django.contrib.auth.models import AbstractUser , Group, Permission
from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_details = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100, unique=True)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    TRANSACTION_TYPES = (
        ('incoming', 'Incoming'),
        ('outgoing', 'Outgoing'),
    )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=8, choices=TRANSACTION_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.transaction_type}"

class CustomUser (AbstractUser):
    email = models.EmailField(unique=True)
    # Override the groups and user_permissions fields to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change this to avoid clashes
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Change this to avoid clashes
        blank=True,
    )