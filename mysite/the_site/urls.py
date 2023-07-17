from django.urls import path, include
from . import views

urlpatterns = [
    path('student/', views.StudentView.as_view(), name='StudentList'),
    path('employee/', views.EmployeeView.as_view(), name='EmployeeList'),
    path('student/c/', views.StudentCreateView.as_view(), name='StudentForm'),
]