from student.models import User
from django import forms
import secrets
import string

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        print("Inside save of custom user creation form")
        user = super().save(commit=False)
        # Generate a random password
        alphabet = string.ascii_letters + string.digits + string.punctuation
        raw_password = ''.join(secrets.choice(alphabet) for _ in range(12))  # 12-character password
        user.set_password(raw_password)  # Hash and save the password
        user._raw_password = raw_password  # Temporarily store the raw password for email
        user.username = user.email
        user.is_active = True
        user.is_staff = True
        if commit:
            user.save()
        user._raw_password = raw_password  # Temporarily store the raw password for email
        return user