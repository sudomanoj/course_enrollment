from django.urls import path
from course.views import (CategoryAddView, HomeView, CategoryListView, CourseListView, CourseDetailView, CourseAddView)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("category/add/", CategoryAddView.as_view(), name="category-add"),
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("course/", CourseListView.as_view(), name="course-list"),
    path("course/add/", CourseAddView.as_view(), name="course-add"),
    path("course/<slug:slug>/", CourseDetailView.as_view(), name="course-detail"),
]
