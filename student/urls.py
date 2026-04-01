from django.urls import path
from .views import student_list, student_detail, home

urlpatterns = [
    path('', home),  # frontend
    path('students/', student_list),
    path('students/<int:id>/', student_detail),
]