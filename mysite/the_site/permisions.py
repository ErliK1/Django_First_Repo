from rest_framework import permissions
from .models import Employee
from django.contrib.auth.models import User

class EmployeePermision(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

class StudentEmployeePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        #print(request.query_params['employee'])
        if request.method == permissions.SAFE_METHODS:
            return True
        if request.data:
            employee = Employee.objects.get(id=request.data['employee'])
            return employee.user == request.user
        return True

    # def has_object_permission(self, request, view, obj):
    #

class StudentListPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        employee = Employee.objects.get(user=user.id)

        return True
