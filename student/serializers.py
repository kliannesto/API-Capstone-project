from rest_framework import serializers
from .models import Student,Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'