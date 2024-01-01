from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['std_num','first_name','last_name','email','branch','gpa']
        labels = {
            'std_num':'Student Name',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-Mail',
            'branch': 'Field of Study',
            'gpa': 'GPA'
        }
        widgets = {
            'std_num': forms.NumberInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'branch': forms.TextInput(attrs={'class':'form-control'}),
            'gpa': forms.NumberInput(attrs={'class':'form-control'})
        }