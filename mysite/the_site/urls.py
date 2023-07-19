from django.urls import path, include
from . import views


urlpatterns = [
    path('student/', views.StudentView.as_view(), name='StudentList'),
    path('employee/', views.EmployeeView.as_view(), name='EmployeeList'),
    path('student/c/', views.StudentCreateView.as_view(), name='StudentForm'),
    path('employeeb/<int:pk>/', views.EmployeePermisionBasedView.as_view(), name='Permission Employee'),
    path('employee/<int:pk>/', views.StudentPermissionBasedView.as_view()),
    path('student/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    path('student/employee', views.StudentEmployeeCreateView.as_view(), name='Create Employee and Student'),

]