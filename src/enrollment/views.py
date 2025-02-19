from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.contrib import messages

from .models import Enrollment
from student.models import Student
from course.models import Course
from enrollment.forms import EnrollmentForm
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

class EnrollmentView(View):
    template_name = "enrollment/enrollment.html"
    
    def get(self, request, *args, **kwargs):
        enrollments = Enrollment.objects.all()
        context = {
            'enrollments': enrollments
        }
        return render(request, self.template_name, context)
    
    
class EnrollmentAddView(UserPassesTestMixin, View):
    template_name = "enrollment/enrollment_add.html"
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to access this page.")
        return redirect('enrollment-list')
    
    def get(self, request, *args, **kwargs):
        form = EnrollmentForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data.get("student")
            course = form.cleaned_data.get("course")
            enrollment = Enrollment(student=student, course=course)
            enrollment.save()
            messages.success(request, "Enrollment added successfully.")
            return redirect("enrollment-list")
        else:
            messages.error(request, "Error adding enrollment. Please try again.")
        return render(request, self.template_name, {'form': form})