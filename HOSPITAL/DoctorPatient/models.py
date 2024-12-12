from django.db import models
from django.contrib.auth.models import AbstractUser 
from pymongo import MongoClient

#Mysql
class User(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialist = models.CharField(max_length=255, null=True)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    age = models.PositiveIntegerField()

class Appointment(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=(('Scheduled', 'Scheduled'), ('Cancelled', 'Cancelled')))

#mongodb
class Prescription:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['hospital_db']
        self.collection = self.db['prescriptions']

    def create_prescription(self, data):
        return self.collection.insert_one(data)

    def get_prescriptions(self, patient_id):
        return list(self.collection.find({"patient_id": patient_id}))
    
    def get_prescriptions_by_appointment(self, appointment_id):
        return self.collection.find({"appointment_id": appointment_id})