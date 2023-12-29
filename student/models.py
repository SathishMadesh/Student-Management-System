from django.db import models

# Create your models here.
class Student(models.Model):
    std_num = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    branch = models.CharField(max_length=100)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student:{self.first_name}'