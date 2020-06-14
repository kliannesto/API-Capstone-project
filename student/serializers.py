from rest_framework import serializers
from .models import Student,Course,EventName,SY,Semester,EventDate,Attendance, SMSLogs

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
        try:
            attendance = Attendance.objects.get(student= student, eventDate=event)
            attendance.isPresent = True
            attendance.save()
            return attendance

        except Attendance.DoesNotExist:
            attendance = Attendance.objects.create(**validated_data)
            return attendance       

class ReadStudentSerializer(serializers.ModelSerializer):
    course=CourseSerializer()
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceWithEventDateSerializer(serializers.ModelSerializer):
    eventDate =   EventDateWithObjectSerializer() 
    student = ReadStudentSerializer()
    class Meta:
        model = Attendance
        fields = '__all__'




class SMSLogsSerializer(serializers.ModelSerializer):   
    class Meta:
        model = SMSLogs
        fields = '__all__'

class AttendanceScheduleSerializer(serializers.ModelSerializer):   
    attendances = AttendanceSerializer (many=True)
    class Meta:
        model = EventDate
        fields = ['id','event','eventdate','sy','semester','logType','attendances']
    def create(self, validated_data):
        attendances = validated_data.pop('attendances')
        eventdate = EventDate.objects.create(**validated_data)
        print(eventdate)
        for attendance in attendances:
            Attendance.objects.create(eventDate=eventdate,**attendance)
        return eventdate      

        