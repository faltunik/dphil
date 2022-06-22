from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentListSerializer(serializers.ModelSerializer):
    students = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['students']
