from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import AppointmentSerializer, AssessmentSerializer, EvaluationReportSerializer
from .models import Appointment, Assessment, EvaluationReport
# Create your views here.
# Appointment views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def appointment_list(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Evaluation Report views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def evaluation_report_list(request):
    if request.method == 'GET':
        reports = EvaluationReport.objects.all()
        serializer = EvaluationReportSerializer(reports, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EvaluationReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def evaluation_report_detail(request, pk):
    try:
        report = EvaluationReport.objects.get(pk=pk)
    except EvaluationReport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EvaluationReportSerializer(report)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EvaluationReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Assessment views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def assessment_list(request):
    if request.method == 'GET':
        assessments = Assessment.objects.all() 
        serializer = AssessmentSerializer(assessments, many=True) 
        return Response(serializer.data) 
    elif request.method == 'POST': 
        serializer = AssessmentSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def assessment_detail(request, pk): 
    try: 
        assessment = Assessment.objects.get(pk=pk) 
    except Assessment.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
       serializer = AssessmentSerializer(assessment)
       return Response(serializer.data)
    elif request.method == 'PUT':
       serializer = AssessmentSerializer(assessment, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
       assessment.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)