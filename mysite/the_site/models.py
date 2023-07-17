from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=0)
    position = models.CharField(choices=(('Teacher', 'Teacher'), ('Professor', 'Professor')), max_length=50)

    def __str__(self):
        return self.user.__str__()
class Student(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.__str__()


