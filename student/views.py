from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime;
from .models import Student,Course,EventName,SY,Semester,EventDate,Attendance,SMSLogs
from .serializers import StudentSerializer,CourseSerializer,SMSLogsSerializer,AttendanceScheduleSerializer,AttendanceWithEventDateSerializer,EventNameSerializer,SYSerializer,EventDateWithObjectSerializer,EventDateSerializer,SemesterSerializer,AttendanceSerializer,ReadStudentSerializer
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
)
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentList(generics.ListAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.all()

class DateAttendanceBySemAndAY(generics.ListAPIView):
    serializer_class = EventDateWithObjectSerializer
    def get_queryset(self):
        ay_id = self.kwargs['ay_id']
        sem_id = self.kwargs['sem_id']
        print(ay_id)
        print(sem_id)
        ay = SY.objects.get(id = ay_id)
        return EventDate.objects.filter( sy = ay, semester=sem_id)

@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'POST':  
        user_credentials = request.data
        username=user_credentials['username']
        password=user_credentials['password']
        try:
            user=authenticate(username=username,password=password)
            login(request,user)
            return Response({"usename": username,"is_admin":True, "is_auth":True})
        except:
            return Response({"usename": username,"is_admin": False, "is_auth":False})
    return Response({"message": "Hello, world!"})

	


class DateAttendanceByStudentSemAndAY(generics.ListAPIView):
    serializer_class = AttendanceWithEventDateSerializer
    def get_queryset(self):
        ay_id = self.kwargs['ay_id']
        sem_id = self.kwargs['sem_id']
        student = Student.objects.get(student_id = self.kwargs['st_id'])

        print(ay_id)
        print(sem_id)
        ay = SY.objects.get(id = ay_id)
        return Attendance.objects.filter(eventDate__sy = ay, eventDate__semester=sem_id, student = student)





class DateAttendanceByCourseSemAndAY(generics.ListAPIView):
    serializer_class = AttendanceWithEventDateSerializer
    def get_queryset(self):
        ay_id = self.kwargs['ay_id']
        sem_id = self.kwargs['sem_id']
        course = Course.objects.get(id = self.kwargs['course_id'])
        ay = SY.objects.get(id = ay_id)
        return Attendance.objects.filter(eventDate__sy = ay, eventDate__semester=sem_id, student__course = course)



class AttendanceAll(generics.ListAPIView):
    serializer_class = AttendanceWithEventDateSerializer
    def get_queryset(self):
        return Attendance.objects.all()


class StudentByCourse(generics.ListAPIView):
    serializer_class = ReadStudentSerializer
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        c = Course.objects.get(id = course_id)
        return Student.objects.filter( course = c)

class EventNameViewSet(viewsets.ModelViewSet):
    queryset = EventName.objects.all()
    serializer_class = EventNameSerializer

class SYViewSet(viewsets.ModelViewSet):
    queryset = SY.objects.all()
    serializer_class = SYSerializer

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class EventDateViewSet(viewsets.ModelViewSet):
    queryset = EventDate.objects.all()
    serializer_class = AttendanceScheduleSerializer

class EventDateWithObjectViewSet(viewsets.ModelViewSet):
    queryset = EventDate.objects.all()
    serializer_class = EventDateWithObjectSerializer

class EventDateNow(generics.ListAPIView):
    serializer_class = EventDateSerializer
    def get_queryset(self):
        return EventDate.objects.filter( eventdate = datetime.now())

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class ReadStudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = ReadStudentSerializer

def index(request):
    return render(request,'index.html')

@api_view(['GET'])
def get_studID(request, st_id):
    student = Student.objects.get(student_id = st_id)

    ser = StudentSerializer(student)
    return Response(ser.data)

class SMSLogsViewSet(viewsets.ModelViewSet):
    queryset = SMSLogs.objects.all()
    serializer_class = SMSLogsSerializer



    


