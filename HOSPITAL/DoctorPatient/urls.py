from django.urls import path
from . import views

urlpatterns = [
    path('registeruser/', views.RegisterUserView.as_view(), name='register_user'),
    path('login/', views.LoginView.as_view(), name='login'),
    
    path('appointmentcancel/', views.cancel_appointment, name='patient-doctor-cancel-appointment'), #both cancel (appointment_id)
    path('prescriptonview/', views.list_appointments, name='prescription-view-doctor-patient'),# both view (patient_id)
    
    # PATIENT
    path('doctorlist/', views.get_all_doctors, name='All-doctor-list'), # patient can view doctor full list
    path('patientedit/', views.edit_details_patient, name='edit-particular-patient'),#patient can edit their details (patient_id)
    path('patientdetails/', views.patient_view, name='patient-view-particular'),#patient can view their details (patient_id)
    path('appointmentcreate/', views.create_appointment, name='patient-appointment-create'), # patient can create appointment
    # DOCTOR
    path('patientlist/', views.get_all_patient, name='All-patient-list'), # doctor can view patient full list
    path('allappointment/', views.list_appointments, name='all-appointments'), # list all the appointments
    path('doctorappointment/', views.particular_doctor_appointments, name='particular-doctor-appointment'),#require (doctor_id)
    path('doctoredit/', views.edit_details_doctor, name='edit-particular-doctor'),#doctor can edit their details (doctor_id)
    path('doctordetails/', views.doctor_view, name='doctor-view-particular'),#doctor can view their details (doctor_id)
    path('createprescription/', views.create_or_update_prescription, name='prescription-create') #require a list of documents
]