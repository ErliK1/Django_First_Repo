from rest_framework import serializers
from .models import Student, Course, Professor, Teacher

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializerGet(serializers.ModelSerializer):

    student = StudentSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'


    # def to_internal_value(self, data):
    #     validated = {
    #         'course_id': self.data.get('course_id'),
    #         'course_name': self.data.get('course_name'),
    #         'student': self.data.get('student')['student_username']
    #     }
    #
    #     return validated

class CourseSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseSerializerRetrieve(serializers.ModelSerializer):

    student = StudentSerializer(Student.objects.all(), many=True)
    class Meta:
        model = Course
        fields = '__all__'

class CourseSerializerUpdater(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class ProfessorSerializerGet(serializers.ModelSerializer):

    course =  CourseSerializerCreate()
    class Meta:
        model = Professor
        fields = '__all__'

class ProfessorSerializerCreate(serializers.ModelSerializer):

    #course = CourseSerializerCreate
    class Meta:
        model = Professor
        fields = '__all__'

class ProfessorCourseSerializerCreate(serializers.ModelSerializer):

    course = CourseSerializerGet()
    class Meta:
        model = Professor
        fields = '__all__'

    # def create(self):

class TeacherSerializer(serializers.ModelSerializer):
    #student = StudentSerializer()


    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherStudentSerializer(serializers.ModelSerializer):

    student = StudentSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'

    # def create(self, validated_data):
    #     student_detail = validated_data.pop('student')
    #     self.student = StudentSerializer(data=student_detail)
    #     if(self.student.is_valid()):
    #         self.student.save()
    #
    #






