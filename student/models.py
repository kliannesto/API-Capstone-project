from django.db import models

# Create your models here.

class Course(models.Model):
    name= models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=30)
    guardiancontactno = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete = models.CASCADE, null = True, blank=True)
