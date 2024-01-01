from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from django.urls import reverse
from .forms import StudentForm

# Create your views here.

def index(request):
    return render(request, 'students/index.html',
                  {'students': Student.objects.all()}
                  )

def view_student(request, id):
    student = Student.objects.get(id=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['std_num']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_branch = form.cleaned_data['branch']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                std_num = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                branch = new_branch,
                gpa = new_gpa
            )
            new_student.save()
            return render(request, 'students/add.html',{
                'form' : StudentForm(),
                'success' : True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html',{
        'form' : StudentForm()
    })

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'student/edit.html',{
                'form':form,
                'success':True
            })
    else:
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
    return render(request, 'student/edit.html',{
        'form':form
    })
