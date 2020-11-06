"""Admin for users"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        'email',
        "full_name",
        "slug",
        'is_staff',
        'is_active',
    )
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (
            None,
            {'fields': ("first_name", "last_name", 'email', 'password')}
        ),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    "first_name",
                    "last_name",
                    'email',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active',
                )
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    exclude = ("slug", "full_name",)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
