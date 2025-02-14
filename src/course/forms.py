from django import forms 
from django.core.exceptions import ValidationError
from course.models import Video, Document, Category, MCQQuestion, MCQOption, Course


class CourseForm(forms.ModelForm):
    """
    Form to create the course.
    """
    
    class Meta:
        model = Course
        fields = ["title", "category", "description", "published"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

class CategoryForm(forms.ModelForm):
    """
    Form to create the category.
    """
    
    class Meta:
        model = Category
        fields = ["title", "parent", "priority", "is_shown"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["parent"].queryset = Category.objects.filter(parent=None)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
        
    def clean(self):
        """
        Function to validate the category parent.
        """
        cleaned_data = super().clean()
        parent = cleaned_data.get("parent")
        if parent and parent.parent:
            raise ValidationError("Only root categories are allowed as parent.")
        return cleaned_data

class VideoForm(forms.ModelForm):
    """
    Form to create the video.
    """
    
    class Meta:
        model = Video
        fields = ["title", "video"]
        
    def clean_video(self):
        """
        Function to validate the video size upto 50MB.
        """
        video = self.cleaned_data.get("video")
        if video.size > 50 * 1024 * 1024:
            raise ValidationError("The maximum file size that can be uploaded is 50MB.")
        return video
    
    
class DocumentForm(forms.ModelForm):
    """
    Form to create the document.
    """
    
    class Meta:
        model = Document
        fields = ["title", "document"]
        
    def clean_document(self):
        """
        Function to validate the document size upto 10MB.
        """
        document = self.cleaned_data.get("document")
        if document.size > 10 * 1024 * 1024:
            raise ValidationError("The maximum file size that can be uploaded is 10MB.")
        return document
    
class MCQQuestionForm(forms.ModelForm):
    """
    Form to create the MCQ option.
    """
    
    class Meta:
        model = MCQQuestion
        fields = ["question", "course",]
        
    def clean(self):
        """
        Function to validate that exactly 4 options exist and at least one of them is correct.
        """
        cleaned_data = super().clean()
        return cleaned_data