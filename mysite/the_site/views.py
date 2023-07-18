from django.shortcuts import render
from .models import Employee, Student
from . import serializers
from rest_framework import generics
from .permisions import EmployeePermision, StudentEmployeePermission, StudentListPermission
from rest_framework import permissions
from django.contrib.auth.models import User


# Create your views here.

class EmployeeView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializerCheck


class StudentView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = (StudentListPermission,)

    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        employee = Employee.objects.get(user=user.id)
        print(user)
        return Student.objects.filter(employee=employee.id)


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = (StudentEmployeePermission,)


class EmployeePermisionBasedView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = (EmployeePermision,)


class StudentPermissionBasedView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeePermissionSerializer
    permission_classes = (StudentEmployeePermission,)
