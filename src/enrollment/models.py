from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Enrollment(models.Model):
    """
    Model to store the enrollment of a student in a course.
    """

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    
    student = models.ForeignKey(
        "student.Student",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.course.title}"
    
    class Meta:
        verbose_name = _("Enrollment")
        verbose_name_plural = _("Enrollments")
        ordering = ["student", "course"]
        unique_together = ["student", "course"]