from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
]
