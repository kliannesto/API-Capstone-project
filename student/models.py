from django.db import models

# Create your models here.

class Course(models.Model):
    code= models.CharField(max_length=10)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.code + " "+ '-' +" " + self.description

class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=30)
    guardiancontact = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete = models.CASCADE, null = True, blank=True)
    isActive = models.BooleanField(default=False)

class EventName(models.Model):
    name = models.CharField(max_length=100)
    fines = models.IntegerField()

    def __str__(self):
        return self.name + " "+ '-' +" " + "₱" + str(self.fines) +".00"

class SY(models.Model):
    AY = models.CharField(max_length=20)

    def __str__(self):
        return self.AY

class Semester(models.Model):
    semester = models.CharField(max_length=30)

    def __str__(self):
        return self.semester

class EventDate(models.Model):
    event = models.ForeignKey(EventName,on_delete = models.CASCADE, null = True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.name + '-' + str(self.date)


class Attendance(models.Model):
    student = models.CharField(max_length=100)
    event = models.ForeignKey(EventDate,on_delete = models.CASCADE, null = True, blank=True)
    sy = models.ForeignKey(SY,on_delete = models.CASCADE, null = True, blank=True)
    semester = models.ForeignKey(Semester,on_delete = models.CASCADE, null = True, blank=True)
    isPresent = models.BooleanField(default=False)
    



    

    
    
    




    
