from django.shortcuts import render
from .models import Employee, Student
from . import serializers
from rest_framework import generics
from .permisions import EmployeePermision, StudentEmployeePermission
from rest_framework import permissions
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

class StudentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

class EmployeePermisionBasedView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = (EmployeePermision,)


class StudentPermissionBasedView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeePermissionSerializer
    permission_classes = (StudentEmployeePermission, )

