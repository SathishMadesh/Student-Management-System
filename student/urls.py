from django.contrib import admin
from django.urls import path
from .views import index, view_student

urlpatterns = [
    path('', index),
    path('<int:id>', view_student, name='view_student')
]