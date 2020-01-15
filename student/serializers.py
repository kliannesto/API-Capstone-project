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

class EventDateWithObjectSerializer(serializers.ModelSerializer):   
    event = EventNameSerializer()
    class Meta:
        model = EventDate
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Attendance
        fields = '__all__'
    def create(self, validated_data):
        event = validated_data.get('eventDate')
        print(event)
        student = validated_data.get('student')
        logType = validated_data.get('logType')
        attendances = Attendance.objects.filter(student= student, eventDate=event)
        if len(attendances) > 0:
            return attendances[0]
        attendance = Attendance.objects.create(**validated_data)
        return attendance

class AttendanceWithEventDateSerializer(serializers.ModelSerializer):
    eventDate =   EventDateWithObjectSerializer() 
    class Meta:
        model = Attendance
        fields = '__all__'


class ReadStudentSerializer(serializers.ModelSerializer):
    course=CourseSerializer()
    class Meta:
        model = Student
        fields = '__all__'