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
router.register('eventcounts',views.EventDateViewSet)
router.register('attendance',views.AttendanceViewSet)
router.register('readstudents',views.ReadStudentViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/students/course/<course_id>',views.StudentByCourse.as_view()),
    path('',views.index)
]