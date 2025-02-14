from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages
from .models import User, Student
# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = "student/student_list.html"
    context_object_name = "students"
    
    def get_queryset(self):
        return super().get_queryset().select_related('user')
    
    
class StudentAddView(View):
    pass
