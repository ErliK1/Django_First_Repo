from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Course, Professor, Teacher, StudentCourse
from .serializers import StudentSerializer, CourseSerializerGet, CourseSerializerCreate, CourseSerializerRetrieve, ProfessorSerializerGet, ProfessorSerializerCreate, ProfessorCourseSerializerCreate, TeacherSerializer, TeacherStudentSerializer, CourseStudentCreate, StudentCourseInitiallyCreate
from rest_framework import generics

from rest_framework import permissions

# Create your views here.

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class StudentSpecific(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerGet
    # permission_classes = [permissions.IsAdminUser]
    # def list(self, request, *args, **kwargs):
    #     courses = Course.objects.all()
    #     course_serializer = CourseSerializerGet(courses, many=True)
    #     return Response(course_serializer.data)

class CourseCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerCreate
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class CourseDestroyer(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerGet

class CourseRetrieve(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerRetrieve

# class CourseUpdate(generics.UpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class =


class ProfessorList(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializerGet

class ProfessorCreate(generics.CreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializerCreate

class ProfessorCourseCreate(generics.CreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorCourseSerializerCreate

    # def create(self, request, *args, **kwargs):
    #     professor_serializer = ProfessorSerializerGet(data=request.data)
    #     if professor_serializer.is_valid():
    #         course_data = professor_serializer.validated_data['course']
    #         course_serializer = CourseSerializerCreate(data=course_data)
    #         print(course_data)
    #         return Response(professor_serializer.data, status=status.HTTP_200_OK)
    #     return Response(professor_serializer.data, status=status.HTTP_200_OK)

class TeacherShow(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherCreate(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherStudentCreate(generics.CreateAPIView):

    queryset = Teacher.objects.all()
    serializer_class = TeacherStudentSerializer


class CourseStudent(generics.CreateAPIView):

    queryset = StudentCourse.objects.all()
    serializer_class = CourseStudentCreate


class InitialStudentCourse(generics.CreateAPIView):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseInitiallyCreate







