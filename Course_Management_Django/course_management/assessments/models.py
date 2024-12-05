from django.db import models
# Create your models here.
from subscriber.models import Subscriber
from courses.models import Course

class Appointment(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20)

class EvaluationReport(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    report_details = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

class Assessment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    assessment_details = models.TextField()
    due_date = models.DateTimeField()