from django.shortcuts import render
from rest_framework import generics, response
from .models import Doctor,Appointment
from .serializers import DoctorSerializer,AppointmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def list_doctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def doctor_detail(request, doctor_id):
    try:
        doctor =  Doctor.objects.get(pk=doctor_id)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'},status=400)
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data)
@api_view(['POST'])
def book_appointment(request):
   
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

