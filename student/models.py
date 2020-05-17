from django.db import models

# Create your models here.

class Course(models.Model):
    code= models.CharField(max_length=10)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.code + " "+ '-' +" " + self.description

class Student(models.Model):
    student_id = models.CharField(unique=True, null=True, blank=True,max_length=20)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null= True, blank=True)
    mobileno = models.CharField(max_length=30, null=True, blank=True)
    guardiancontact = models.CharField(max_length=30, null=True, blank=True)
    course = models.ForeignKey(Course,on_delete = models.CASCADE, null = True, blank=True)
    religion = models.CharField(max_length=30, null=True,blank=True)
    isActive = models.BooleanField(default=False, null=True,blank=True)

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
    sy = models.ForeignKey(SY,on_delete = models.CASCADE, null = True, blank=True)
    semester = models.IntegerField( null = True, blank=True)
    eventdate = models.DateField(blank=True, null=True)
    logType = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.event.name + '-' + str(self.eventdate)


class Attendance(models.Model):

    student = models.ForeignKey(Student,on_delete = models.CASCADE, null = True, blank=True)
    eventDate = models.ForeignKey(EventDate,on_delete = models.CASCADE, null = True, blank=True,related_name="attendances")
    logType = models.IntegerField(null=True, blank=True)
    isPresent = models.BooleanField(default = False, blank=True, null=True)

class SMSLogs(models.Model):
    log = models.CharField(max_length = 300)
    recipient = models.CharField(max_length=20, null=True, blank=True)



   
   
    



    

    
    
    




    
