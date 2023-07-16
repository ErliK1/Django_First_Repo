from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='home'),
    path('<int:pk>/', views.StudentSpecific.as_view()),
    path('course/', views.CourseList.as_view(), name='course'),
    path('course/post/', views.CourseCreate.as_view()),
    path('course/<int:pk>/', views.CourseDestroyer.as_view(), name='Destroyer of Courses'),
    path('course/<int:pk>/s/', views.CourseRetrieve.as_view(), name='Retrieve'),
    path('professor/g/', views.ProfessorList.as_view()),
    path('professor/c/', views.ProfessorCreate.as_view()),
    path('professor/cb/', views.ProfessorCourseCreate.as_view()),
    path('teacher/v/', views.TeacherShow.as_view()),
    path('teacher/c/', views.TeacherCreate.as_view()),
    path('teacher/cc/', views.TeacherStudentCreate.as_view()),
    path('course/cc/', views.CourseStudent.as_view(), name='courseStuent'),
    path('course/bc/', views.InitialStudentCourse.as_view()),
]