from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Course, Professor
from .serializers import StudentSerializer, CourseSerializerGet, CourseSerializerCreate, CourseSerializerRetrieve, ProfessorSerializerGet, ProfessorSerializerCreate, ProfessorCourseSerializerCreate
from rest_framework import generics


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

    def list(self, request, *args, **kwargs):
        courses = Course.objects.all()
        course_serializer = CourseSerializerGet(courses, many=True)
        return Response(course_serializer.data)

class CourseCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerCreate




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

    def create(self, request, *args, **kwargs):
        professor_serializer = ProfessorSerializerCreate(data=request.data)
        if professor_serializer.is_valid():
            course_ordered_data = professor_serializer.validated_data['course']
            course_serializer = CourseSerializerCreate(data=course_ordered_data)
            if course_serializer.is_valid():
                course_serializer.save()
            else:
                return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            professor_serializer.validated_data['course'] = course_serializer
            professor_serializer.save()
            return Response(professor_serializer.data, status=status.HTTP_200_OK)
        return Response(professor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #CHECK AGAIN HEREE

