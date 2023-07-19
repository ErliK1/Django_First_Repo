from django.shortcuts import render
from .models import Employee, Student
from . import serializers
from rest_framework import generics
from .permisions import EmployeePermision, StudentEmployeePermission, StudentListPermission
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import Response, status



# Create your views here.

class EmployeeView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializerCheck


class StudentView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = (IsAuthenticated, )

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

    def put(self, request, *args, **kwargs):
        print(*args)
        # if len(args) == 0:
        #     return Response({'message': f'{args}'}, status=status.HTTP_400_BAD_REQUEST)
        # if len(kwargs) > 0:
        #     return Response({'message': f'{kwargs}!!'}, status=status.HTTP_400_BAD_REQUEST)
        if len(kwargs) == 1:
            student = Student.objects.get(pk=kwargs['pk'])
            student_serializer = serializers.StudentSerializer(student, data=request.data)
            if student_serializer.is_valid():
                student_serializer.validated_data['name'] = student_serializer.validated_data['name'] + '/U'
                student_serializer.save()
                return Response(student_serializer.data, status=status.HTTP_200_OK)
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Error!!'}, status=status.HTTP_400_BAD_REQUEST)


class EmployeePermisionBasedView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = (EmployeePermision,)


class StudentPermissionBasedView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeePermissionSerializer
  #  permission_classes = (StudentEmployeePermission,)




class StudentEmployeeCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentEmployeeCreateSerializer

