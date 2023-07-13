from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='home'),
    path('<int:pk>/', views.StudentSpecific.as_view()),
    path('course/', views.CourseList.as_view(), name='course'),
    path('course/post', views.CourseCreate.as_view()),
    path('course/<int:pk>/', views.CourseDestroyer.as_view(), name='Destroyer of Courses'),
    path('course/<int:pk>/s/', views.CourseRetrieve.as_view(), name='Retrieve')
]