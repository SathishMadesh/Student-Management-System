from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'students/index.html',
                  {'students': Student.objects.all()}
                  )

def view_student(request, id):
    student = Student.objects.get(id=id)
    return HttpResponseRedirect(reverse('index'))