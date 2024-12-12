import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Doctor, Patient, Appointment, Prescription, User
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, UserSerializer

#                                NO AUTHENTICATION NEEDED
# creating the user
class RegisterUserView(APIView):
    def post(self, request):
        data = request.data
        role = data.get('role')
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            phone=data.get('phone'),
            role=role
        )
        if role == 'doctor':
            Doctor.objects.create(user=user, specialist=data['specialist'])
        elif role == 'patient':
            Patient.objects.create(user=user, age=data['age'])
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        from django.contrib.auth import authenticate
        data = request.data
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
#                                             AUTHENTICATION NEEDED
# =================================================================================================================

# Patient
# patient -> doctor list
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_doctors(request):
    doctor_list = Doctor.objects.all()
    serializer = DoctorSerializer(doctor_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# parient -> edit details
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_details_patient(request):
    id = request.data.get('patient_id')
    if not id:
        return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return Response({"error":"The patient Not Exist"}, status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# patient view particular details
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patient_view(request):
    id = request.data.get('patient_id')
    if not id:
        return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return Response({"error":"The patient Not Exist"}, status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patient, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

# Patient -> Appintment Create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_appointment(request):
    data = request.data
    # Parse the date field if it is in DD-MM-YYYY HH:MM AM/PM format
    try:
        if "date" in data and "-" in data["date"] and ("AM" in data["date"] or "PM" in data["date"]):
            # Convert "12-12-2024 03:58 PM" format
            date_obj = datetime.strptime(data["date"], "%d-%m-%Y %I:%M %p")
            data["date"] = date_obj.strftime("%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return Response({"error": "Invalid date format. Use 'DD-MM-YYYY HH:MM AM/PM'."}, status=status.HTTP_400_BAD_REQUEST)
    serializer = AppointmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# =================================================================================================================

# DOCTOR
# doctor -> patient list
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_patient(request):
    patient_list = Patient.objects.values('id', 'username', 'age')
    serializer = PatientSerializer(patient_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# doctor -> edit details
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_details_doctor(request):
    id = request.data.get('doctor_id')
    if not id:
        return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        doctor = Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
        return Response({"error":"The doctor Not Exist"}, status=status.HTTP_404_NOT_FOUND)
    serializer = DoctorSerializer(doctor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# doctor view particular details
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_view(request):
    id = request.data.get('doctor_id')
    if not id:
        return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        doctor = Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
        return Response({"error":"The doctor Not Exist"}, status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(doctor, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# doctor view appointment
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_appointments(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# paricular doctor view appointment
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def particular_doctor_appointments(request):
    doctor_id = request.data.get('doctor_id')
    if not doctor_id:
        return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        doctor = Appointment.objects.get(doctor=doctor_id)
    except Appointment.DoesNotExist:
        return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = AppointmentSerializer(doctor, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Doctor -> create prescription
@api_view(['POST'])
def create_or_update_prescription(request):
    data = request.data
    
    # Validate the associated appointment
    try:
        appointment = Appointment.objects.get(id=data.get("appointment_id"))
    except Appointment.DoesNotExist:
        return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)

    # Connect to Prescription (MongoDB)
    prescription = Prescription()

    # Check if a prescription already exists for the patient
    existing_prescription = prescription.collection.find_one({"patient_id": data.get("patient_id")})
    
    if existing_prescription:
        # Update the past history and other fields
        updated_data = {
            "appointment_id": data.get("appointment_id"),
            "doctor_id": data.get("doctor_id"),
            "patient_id": data.get("patient_id"),
            "date": data.get("date"),
            "bp": data.get("bp"),
            "pulse": data.get("pulse"),
            "temperature": data.get("temperature"),
            "symptoms": data.get("symptoms"),
            "alergic": data.get("alergic"),
            "medicine": data.get("medicine"),
            "test": data.get("test"),
            "scan": data.get("scan"),
        }
        
        # Append new data to `past_history` field
        if "past_history" in existing_prescription:
            updated_past_history = existing_prescription["past_history"] + [updated_data]
        else:
            updated_past_history = [updated_data]
        
        # Update the document in MongoDB
        prescription.collection.update_one(
            {"_id": existing_prescription["_id"]},
            {"$set": {"past_history": updated_past_history, **updated_data}}
        )
        return Response(
            {"status": "success", "message": "Prescription updated successfully."},
            status=status.HTTP_200_OK,
        )
    else:
        # Create a new prescription document
        prescription_data = {
            "appointment_id": data.get("appointment_id"),
            "doctor_id": data.get("doctor_id"),
            "patient_id": data.get("patient_id"),
            "date": data.get("date"),
            "bp": data.get("bp"),
            "pulse": data.get("pulse"),
            "temperature": data.get("temperature"),
            "symptoms": data.get("symptoms"),
            "alergic": data.get("alergic"),
            "medicine": data.get("medicine"),
            "test": data.get("test"),
            "scan": data.get("scan"),
            "past_history": [],
        }
        result = prescription.create_prescription(prescription_data)
        return Response(
            {"status": "success", "prescription_id": str(result.inserted_id)},
            status=status.HTTP_201_CREATED,
        )
# =================================================================================================================

# DOCTOR PATIENT COMMON (APPOINTMENT CANCEL)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def cancel_appointment(request):
    appointment_id = request.data.get('appointment_id')
    if not appointment_id:
        return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)

    appointment.status = "Cancelled"
    appointment.save()
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data, status=status.HTTP_200_OK)

# DOCTOR PATIENT COMMON (APPOINTMENT CANCEL)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_prescriptions(request):
    patient_id = request.data.get('patient_id')
    if not patient_id:
         return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        prescription = Prescription()
        prescriptions = prescription.get_prescriptions(patient_id)
        return Response(prescriptions, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
        