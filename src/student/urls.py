from django.urls import path
from student.views import StudentListView, StudentAddView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student-list"),
    path("students/add/", StudentAddView.as_view(), name="student-add"),
]