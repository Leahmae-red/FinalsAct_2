from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_profile, name='student_profile'),
]