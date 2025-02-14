from django.contrib import admin
from course.models import (
    Category,
    Course,
    Video,
    Document,
    MCQQuestion,
    MCQOption
)
from .forms import CategoryForm, MCQQuestionForm

# Register your models here.
class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1
    
class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    
class MCQOptionInline(admin.TabularInline):
    model = MCQOption
    extra = 4
    
    
class CourseAdmin(admin.ModelAdmin):
    inlines = [DocumentInline, VideoInline]
  
admin.site.register(Course, CourseAdmin)

  
class MCQQuestionAdmin(admin.ModelAdmin):
    inlines = [MCQOptionInline]
    form = MCQQuestionForm
    
admin.site.register(MCQQuestion, MCQQuestionAdmin)


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm

admin.site.register(Category, CategoryAdmin)