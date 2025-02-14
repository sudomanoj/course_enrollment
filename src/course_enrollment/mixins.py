from django.db import models

class TimeStampMixin(models.Model):
    """
    Mixin to add created_at and updated_at fields to a model.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class UserStampMixin(models.Model):
    """
    Mixin to add created_by and updated_by fields to a model.
    """

    created_by = models.ForeignKey(
        "student.User",
        on_delete=models.SET_NULL,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
        editable=False,
    )

    updated_by = models.ForeignKey(
        "student.User",
        on_delete=models.SET_NULL,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )

    class Meta:
        abstract = True