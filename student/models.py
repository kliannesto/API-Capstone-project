from django.db import models

# Create your models here.

class Course(models.Model):
    name= models.CharField(max_length=20)

class Student(models.Model):
    student_id = models.IntegerField()
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=30)
    guardiancontactno = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
