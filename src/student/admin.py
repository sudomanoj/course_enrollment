from django.contrib import admin
from student.models import User, Student
from student.forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "first_name", "last_name", "is_staff"]
    add_form = CustomUserCreationForm  # This is for creating new users
    form = CustomUserCreationForm  # This is for editing users (can be customized if needed)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )

admin.site.register(User, CustomUserAdmin)