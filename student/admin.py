from django.contrib import admin
from .models import Student,Course,EventName,SY,Semester,EventDate,Attendance

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(EventName)
admin.site.register(SY)
admin.site.register(Semester)
admin.site.register(EventDate)
admin.site.register(Attendance)

# Register your models here.
