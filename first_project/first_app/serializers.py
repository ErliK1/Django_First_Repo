from rest_framework import serializers
from .models import Student, Course

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializerGet(serializers.ModelSerializer):

    student = StudentSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'


    def to_internal_value(self, data):
        validated = {
            'course_id': self.data.get('course_id'),
            'course_name': self.data.get('course_name'),
            'student': self.data.get('student')['student_username']
        }

        return validated

class CourseSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'