from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_username = models.CharField(max_length=200,default='username')
    student_email = models.EmailField(max_length=200, default='email', unique=True)
    student_password = models.CharField(max_length=200, default='pass')

    def __str__(self):
        return str(self.student_username)

class Course(models.Model):
    course_id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length=200, default='Course')
    student = models.ManyToManyField(Student)

    def __str__(self):
        return str(self.course_name)



class Professor(models.Model):
    professor_name = models.CharField(max_length=200)
    professor_email = models.EmailField(max_length=100)
    professor_password = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.professor_name)
