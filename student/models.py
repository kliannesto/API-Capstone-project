from django.db import models

# Create your models here.

class Course(models.Model):
    code= models.CharField(max_length=10, default = 'CODE')
    description = models.CharField(max_length=200, default='description')

    def __str__(self):
        return self.code + '-' + self.description

class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=30)
    guardiancontactno = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete = models.CASCADE, null = True, blank=True)

    
