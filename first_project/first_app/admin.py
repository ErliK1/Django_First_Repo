from django.contrib import admin
from .models import Course, Student, Teacher, Professor, StudentCourse
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Professor)
admin.site.register(StudentCourse)

