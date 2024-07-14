from django.urls import path
from .views import StudentListView
from .views import ClassListView

urlpatterns = [
    path("students/", StudentListView.as_view(),name="student_list_view"),
    path("classes_school/", ClassListView.as_view(),name="class_list_view"),

]