from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.contrib import messages


from .models import Course, Category
from .forms import CategoryForm


# Create your views here.
class HomeView(TemplateView):
    template_name = "course/home.html"
    


class CategoryListView(ListView):
    model = Category
    template_name = "course/category_list.html"
    context_object_name = "categories"
    queryset = Category.objects.filter(is_shown=True).order_by("priority", "title")


class CategoryAddView(View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, "course/category_add.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully.")
            return redirect("category-list")
        else:
            messages.error(request, "Error adding category. Please try again.")
        return render(request, "course/category_add.html", {"form": form})
        
        
class CourseListView(ListView):
    model = Course
    template_name = "course/course_list.html"
    context_object_name = "courses"
    queryset = Course.objects.filter(published=True)
    
    
class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course_detail.html"
    context_object_name = "course"
    
    def get_queryset(self):
        return super().get_queryset().select_related('category').prefetch_related('videos', 'documents', 'mcq_questions', 'mcq_questions__options')