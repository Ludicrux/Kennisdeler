"""User forms"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form"""
    job = forms.CharField(label="Werkend als", max_length=30)
    organization = forms.CharField(label="Organisatie", max_length=30)
    profile_picture = forms.ImageField(label="Profiel foto")

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email',)


class CustomUserChangeForm(UserChangeForm):
    """Custom user change form"""

    class Meta:
        model = User
        fields = ('email',)
