from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Student,Course
from .serializers import StudentSerializer,CourseReadSerializer
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseReadSerializer

class StudentList(generics.ListAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.all()
