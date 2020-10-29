"""Admins for users"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import User


class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("full_name",'email', 'is_staff', 'is_active', "job", "organization", "profile_picture")
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ( "first_name", "last_name", 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('User Detauls', {'fields': ("job", "organization", "profile_picture")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                "first_name",
                "last_name",
                'email',
                'password1',
                'password2',
                "job",
                "organization",
                "profile_picture",
                'is_staff',
                'is_active',
                )
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
