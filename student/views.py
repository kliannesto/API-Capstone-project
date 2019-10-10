from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Student,Course,EventName,SY,Semester,EventDate,Attendance
from .serializers import StudentSerializer,CourseSerializer,EventNameSerializer,SYSerializer,EventDateSerializer,SemesterSerializer,AttendanceSerializer,ReadStudentSerializer
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class StudentList(generics.ListAPIView):
#     serializer_class = StudentSerializer
#     def get_queryset(self):
#         return Student.objects.all()

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
    serializer_class = EventDateSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class ReadStudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = ReadStudentSerializer

def index(request):
    return render(request,'index.html')


    


