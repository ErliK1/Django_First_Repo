from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='home'),
    path('<int:pk>/', views.StudentSpecific.as_view()),
]