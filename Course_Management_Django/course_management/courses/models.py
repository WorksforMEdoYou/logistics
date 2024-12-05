from django.db import models
from subscriber.models import Subscriber
# Create your models here.
# Course model
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in hours
    counselor = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name='courses')