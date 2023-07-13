from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_username = models.CharField(max_length=200,default='username')
    student_email = models.EmailField(max_length=200, default='email')
    student_password = models.CharField(max_length=200, default='pass')

    def __str__(self):
        return str(self.student_username)

class Course(models.Model):
    course_id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length=200, default='Course')

    def __str__(self):
        return str(self.course_name)


class StudentTakesCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

