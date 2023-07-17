from django.shortcuts import render
from .models import Employee, Student
from . import serializers
from rest_framework import generics
# Create your views here.

class EmployeeView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializerCheck

class StudentView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
