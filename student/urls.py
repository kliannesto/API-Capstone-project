from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('students',views.StudentViewSet)
router.register('courses',views.CourseViewSet)
router.register('eventnames',views.EventNameViewSet)
router.register('sy',views.SYViewSet)
router.register('semesters',views.SemesterViewSet)
router.register('events',views.EventDateViewSet)
router.register('eventLists',views.EventDateWithObjectViewSet)
router.register('attendance',views.AttendanceViewSet)
router.register('readstudents',views.ReadStudentViewSet)
router.register('smslogs',views.SMSLogsViewSet)



urlpatterns = [
    path('api/',include(router.urls)),
    path('api/students/course/<course_id>',views.StudentByCourse.as_view()),
    path('api/eventsnow/',views.EventDateNow.as_view()),
    path('api/attendancelists',views.AttendanceAll.as_view()),
    path('api/login',views.login_view),
    path('',views.index),
    path('api/students/studentbyId/<st_id>',views.get_studID),
    path('api/dateattendance/sem/<sem_id>/ay/<ay_id>',views.DateAttendanceBySemAndAY.as_view()),
    path('api/dateattendance/sem/<sem_id>/ay/<ay_id>/stud/<st_id>',views.DateAttendanceByStudentSemAndAY.as_view()),
    path('api/dateattendance/sem/<sem_id>/ay/<ay_id>/course/<course_id>',views.DateAttendanceByCourseSemAndAY.as_view()),
    path('api/dateattendance/sem/<sem_id>/ay/<ay_id>',views.DateAttendanceBySemAndAY.as_view()),
    

    
]