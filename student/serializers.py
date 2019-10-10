from rest_framework import serializers
from .models import Student,Course,EventName,SY,Semester,EventDate,Attendance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EventNameSerializer(serializers.ModelSerializer):   
    class Meta:
        model = EventName
        fields = '__all__'

class SYSerializer(serializers.ModelSerializer):   
    class Meta:
        model = SY
        fields = '__all__'

class SemesterSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Semester
        fields = '__all__'

class EventDateSerializer(serializers.ModelSerializer):   
    class Meta:
        model = EventDate
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Attendance
        fields = '__all__'

class ReadStudentSerializer(serializers.ModelSerializer):
    course=CourseSerializer()
    class Meta:
        model = Student
        fields = '__all__'