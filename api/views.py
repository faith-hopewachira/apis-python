from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from classes.models import ClassPeriod
from .serializers import ClassPeriodSerializer





# Create your views here.
class StudentListView(APIView):
    # FUNCTION FOR THE GET METHOD
    def get(self, request):
        # RETRIEVING ALL STUDENTS DATA
        students = Student.objects.all()
        # SERIALIZING IT TO JSON FORMAT
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)


class ClassListView(APIView):
    def get(self, request):
        classes_school = Class.objects.all()
        serializer = ClassPeriodSerializer(classes, many = True)
        return Response(serializer.data)