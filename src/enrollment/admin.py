from django.contrib import admin
from enrollment.models import Enrollment

# Register your models here.
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["student", "course"]
    search_fields = ["student__user__first_name", "student__user__last_name", "course__title"]
    list_filter = ["course__title"]
    
admin.site.register(Enrollment, EnrollmentAdmin)