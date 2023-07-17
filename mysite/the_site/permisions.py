from rest_framework import permissions

class EmployeePermision(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

class StudentEmployeePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user