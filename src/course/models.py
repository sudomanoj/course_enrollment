from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from course_enrollment.mixins import TimeStampMixin, UserStampMixin
from course.validators import validate_video_size, validate_document_size


class Category(TimeStampMixin, UserStampMixin):
    """
    Model to store the course categories.
    """
    uuid = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
    )
    
    title = models.CharField(
        max_length=255,
        unique=True,
    )
    
    priority = models.PositiveIntegerField(
        default=0,
    )
    
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="sub_category",
        null=True,
        blank=True,
    )
    
    slug = models.SlugField(
        max_length=255,
        unique=True,
        editable=False,
    )
    
    is_shown = models.BooleanField(
        default=True,
    )
    
    def parent_name(self):
        return self.parent.name if self.parent else "Root"
    
    def get_root(self):
        if self.parent:
            return self.parent.get_root()
        return self
    
    def get_descendants(self, include_self=False):
        descendants = []
        if include_self:
            descendants.append(self)
        for child in self.sub_category.all():
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants
    
    def get_ansestors(self):
        ansestors = []
        if self.parent:
            ansestors.extend(self.parent.get_ansestors(include_self=True))
        return ansestors
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not self.sub_category.exists()
    
    def save(self, *args, **kwargs):
        self.title = self.title.strip().lower()
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=base_slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["title"]
        
        
        
class Course(TimeStampMixin, UserStampMixin):
    """
    Model to store the course information.
    """
    
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    
    title = models.CharField(
        max_length=255,
    )
    
    description = models.TextField(
        blank=True,
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="courses",
    )
    
    slug = models.SlugField(
        max_length=255,
        unique=True,
        editable=False,
    )
    
    published = models.BooleanField(
        default=True,
    )
    
    def save(self, *args, **kwargs):
        self.title = self.title.strip().lower()
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Course.objects.filter(slug=base_slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        ordering = ["title"]
        
        
class Video(TimeStampMixin, UserStampMixin):
    """
    Model to store the video information.
    """
    
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    
    title = models.CharField(
        max_length=255,
    )
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="videos",
    )
    
    video = models.FileField(
        upload_to="videos/",
        validators=[
            validate_video_size,
            FileExtensionValidator(allowed_extensions=["mp4"]),
            ],
    )
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
        ordering = ["title"]
        
        
class Document(TimeStampMixin, UserStampMixin):
    """
    Model to store the document information.
    """
    
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    
    title = models.CharField(
        max_length=255,
    )
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="documents",
    )
    
    document = models.FileField(
        upload_to="documents/",
        validators=[
            validate_document_size,
            FileExtensionValidator(allowed_extensions=["pdf"]),
            ],
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")
        ordering = ["title"]
        
        
class MCQQuestion(TimeStampMixin, UserStampMixin):
    """
    Model to store the MCQ question information.
    """
    
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    
    question = models.TextField()
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="mcq_questions",
    )
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = _("MCQ Question")
        verbose_name_plural = _("MCQ Questions")
        ordering = ["question"]
        
        
class MCQOption(TimeStampMixin, UserStampMixin):
    """
    Model to store the MCQ option information.
    """
    
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    
    question = models.ForeignKey(
        MCQQuestion,
        on_delete=models.CASCADE,
        related_name="options",
    )
    
    option = models.CharField(
        max_length=255,
    )
    
    is_correct = models.BooleanField(
        default=False,
    )
    
    def __str__(self):
        return self.option
    
    class Meta:
        verbose_name = _("MCQ Option")
        verbose_name_plural = _("MCQ Options")
        ordering = ["option"]