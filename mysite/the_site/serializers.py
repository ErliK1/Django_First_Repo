from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username',)
class EmployeeSerializerCheck(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = models.Employee
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    #employee = EmployeeSerializerCheck()
    class Meta:
        model = models.Student
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    student_set = StudentSerializer(many=True)

    class Meta:
        model = models.Employee
        fields = (
            'id',
            'user',
            'phone_number',
            'student_set'
        )

class EmployeePermissionSerializer(serializers.ModelSerializer):

    student_set = StudentSerializer(many=True)
    class Meta:
        model = models.Employee
        fields = (
            'student_set',
        )
class StudentEmployeeCreateSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializerCheck()
    class Meta:
        model = models.Student
        fields = '__all__'

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        user_data = employee_data.pop('user')
        user = models.User.objects.create(**user_data)
        employee = models.Employee.objects.create(user=user, **employee_data)
        student = models.Student.objects.create(employee=employee, **validated_data)
        return student
