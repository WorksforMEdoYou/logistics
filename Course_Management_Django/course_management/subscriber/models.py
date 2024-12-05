from django.db import models
from users.models import User
# Create your models here.
# Subscriber model
class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    subscription_date = models.DateField(auto_now_add=True)