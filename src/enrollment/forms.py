from django import forms
from django.core.exceptions import ValidationError
from enrollment.models import Enrollment
from student.models import Student
from course.models import Course


class EnrollmentForm(forms.Form):
    """
    Form to create the enrollment.
    """
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    
    def clean(self):
        """
        Function to validate the enrollment date.
        """
        cleaned_data = super().clean()
        student = cleaned_data.get("student")
        course = cleaned_data.get("course")
        
        if Enrollment.objects.filter(student=student, course=course).exists():
            raise ValidationError("This student is already enrolled in this course.")
        
        return cleaned_data