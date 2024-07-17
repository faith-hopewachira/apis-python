from django.urls import path
from .views import StudentListView
from .views import ClassListView
from .views import ClassPeriodSerializer
from .views import CourseListView
from  .views import TeachersListView

urlpatterns = [
    path("students/", StudentListView.as_view(),name="student_list_view"),
    path("classes_school/", ClassListView.as_view(),name="class_list_view"),
    path("teacher/", TeachersListView.as_view(), name= "teacher_list_view"),
    path("course/", CourseListView.as_view(), name="course_list_view"),


    

]