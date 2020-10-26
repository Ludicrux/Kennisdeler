"""User forms"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', "job", "organization", "profile_picture",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', "job", "organization", "profile_picture",)
