from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Course, Professor, Teacher
from .serializers import StudentSerializer, CourseSerializerGet, CourseSerializerCreate, CourseSerializerRetrieve, ProfessorSerializerGet, ProfessorSerializerCreate, ProfessorCourseSerializerCreate, TeacherSerializer, TeacherStudentSerializer
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
        professor_serializer = ProfessorSerializerGet(data=request.data)
        if professor_serializer.is_valid():
            course_data = professor_serializer.validated_data['course']
            course_serializer = CourseSerializerCreate(data=course_data)
            print(course_data)
            return Response(professor_serializer.data, status=status.HTTP_200_OK)
        return Response(professor_serializer.data, status=status.HTTP_200_OK)

class TeacherShow(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherCreate(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherStudentCreate(generics.CreateAPIView):

    queryset = Teacher.objects.all()
    serializer_class = TeacherStudentSerializer

    # def create(self, request, *args, **kwargs):
    #     teacher_details = request.data
    #     teacher_serializer = TeacherStudentSerializer(data=request.data)
    #     if teacher_serializer.is_valid():
    #         student_serializer = StudentSerializer(data=teacher_serializer.validated_data['student'])
    #         if student_serializer.is_valid():
    #             student_serializer.save()
    #         else:
    #             return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         teacher_model = Teacher(teacher_name=teacher_serializer.validated_data['teacher_name'],teacher_password=teacher_serializer.validated_data['teacher_password'], student=student_serializer)
    #         print(teacher_serializer.validated_data)
    #         teacher_model.save()
    #         return Response(teacher_details.data, status=status.HTTP_200_OK)
    #     return Response(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)








