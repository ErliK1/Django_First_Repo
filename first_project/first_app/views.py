from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
from rest_framework import generics


# Create your views here.

class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(Student.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_200_OK)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentSpecific(APIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        student_serializer = StudentSerializer(student)
        return Response(student_serializer.data)

    def put(self, request, pk):
        student_serializer = StudentSerializer(self.get_object(pk), data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_200_OK)
        return Response(student_serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        student: Student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        student = self.get_object(pk)
        student_serializer = StudentSerializer(student, data=request.data, partial=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_200_OK)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)









