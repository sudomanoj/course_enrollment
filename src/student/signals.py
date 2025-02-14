from django.db.models import signals
from django.dispatch import receiver
from student.models import User, Student
from django.core.mail import send_mail
from django.conf import settings
import random
import string


@receiver(signals.post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    """
    Signal to create a student profile when a user is created.
    """
    if created and hasattr(instance, '_raw_password'):
        raw_password = instance._raw_password
        subject = 'Your account has been created'
        message = f'''
        Hello {instance.first_name},

        Your account has been created successfully.
        Your username is: {instance.username}
        Your temporary password is: {raw_password}
        Please change your password after logging in.
        '''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email,]
        send_mail(subject, message, email_from, recipient_list)
        print(f"Email sent to {instance.email} with password: {raw_password}")
        print(f"Raw password: {raw_password}")
        Student.objects.create(user=instance)