from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser

from course_enrollment.mixins import TimeStampMixin, UserStampMixin


class User(AbstractUser):
    """
    Model to store the student details.
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    
    first_name = models.CharField(
        max_length=255,
    )
    
    last_name = models.CharField(
        max_length=255,
    )
    
    email = models.EmailField(
        unique=True,
    )
    
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["first_name", "last_name"]
        
        
class Student(models.Model):
    """
    Model to store the student details.
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    
    user = models.OneToOneField(
        "student.User",
        on_delete=models.CASCADE,
        related_name="student",
    )
    
    def __str__(self):
        return self.user.get_full_name()