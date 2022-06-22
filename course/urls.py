from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 


course_router = DefaultRouter()

course_router.register('post', views.CourseAPI, basename = 'course')


urlpatterns = [
    path('', include(course_router.urls)),
    path('enroll/', views.Enrollment.as_view(), name = 'enroll'),
    path('student/', views.StudentList.as_view(), name = 'student'),
]