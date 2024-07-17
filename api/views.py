from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from classes.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from .serializers import TeacherSerializer
from teacher.models import Teacher
from course.models import Course
from classes.models import Class


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

class TeachersListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many = True)
        return Response(serializer.data)


class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many = True)
        return Response(serializer.data)

        