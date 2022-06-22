from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializer import CourseSerializer,  StudentListSerializer

class CourseAPI(viewsets.ModelViewSet):
    def create(self, request):
        if request.user.teacher:
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher= request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "You Dont Have Permission"}, status=status.HTTP_400_BAD_REQUEST)


class Enrollment(APIView):
    def enroll_user(self, request):
        obj = get_object_or_404(Course, id = request.GET.get('getid', 1) )
        obj.students.add(request.user)
        return Response({"Enrolled": "You Are Enrolled"}, status=status.HTTP_202_ACCEPTED )

class StudentList(APIView):
    def get(self, request):
        obj = get_object_or_404(Course, id = request.GET.get('getid', 1) )
        serializer = StudentListSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK )





