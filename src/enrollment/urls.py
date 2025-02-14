from django.urls import path
from enrollment.views import EnrollmentView, EnrollmentAddView

urlpatterns = [
    path("enrollments/", EnrollmentView.as_view(), name="enrollment-list"),
    path("enrollment/add/", EnrollmentAddView.as_view(), name="enrollment-add"),
]
