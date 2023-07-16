from rest_framework import serializers
from first_app.models import Course, Student, Teacher, Professor, StudentCourse

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializerGet(serializers.ModelSerializer):

    #student = StudentSerializer()
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

    # student = StudentSerializer(Student.objects.all(), many=True)
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

    course = CourseSerializerGet()
    class Meta:
        model = Professor
        fields = '__all__'

class ProfessorCourseSerializerCreate(serializers.ModelSerializer):

    course = CourseSerializerCreate()
    class Meta:
        model = Professor
        fields = '__all__'

    def create(self, validated_data):
        course_data = validated_data.pop('course')
        course = Course.objects.create(**course_data)
        professor = Professor.objects.create(course=course, **validated_data)
        return professor


class TeacherSerializer(serializers.ModelSerializer):
    student = StudentSerializer()


    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherStudentSerializer(serializers.ModelSerializer):

    student = StudentSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        student_detail = validated_data.pop('student')
        student = Student.objects.create(**student_detail)
        student.save()
        teacher = Teacher.objects.create(student=student, **validated_data)
        teacher.save()
        return teacher

class CourseStudentCreate(serializers.ModelSerializer):

    class Meta:
        model = StudentCourse
        fields = '__all__'

class StudentCourseInitiallyCreate(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializerCreate()
    class Meta:
        model = StudentCourse
        fields = '__all__'

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        student_model = Student.objects.create(**student_data)
        course_data = validated_data.pop('course')
        course_model = Course.objects.create(**course_data)
        student_takes_course = StudentCourse.objects.create(student=student_model, course=course_model)
        return student_takes_course