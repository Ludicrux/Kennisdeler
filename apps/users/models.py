"""Models for users"""
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField

from users.managers import CustomUserManager


class User(AbstractUser):
    """User model"""
    username = None
    full_name = models.CharField(_("full name"), unique=True, max_length=35)
    email = models.EmailField(_('email address'), unique=True)

    job = models.CharField(_("werkend als"), max_length=30)
    organization = models.CharField(_("organisatie"), max_length=30)
    profile_picture = ResizedImageField(
        quality=100,
        size=[50, 50],
        crop=['middle', 'center'],
        upload_to="images/user-images",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name", "job", "organization", "profile_picture"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def article_count(self):
        return f"{self.article_set.count()}"

    def get_absolute_url(self):
        """returns url for for the user"""
        return reverse(
            "users:user-article-list",
            kwargs={'full_name': str(self.full_name)}
        )

    def save(self, *args, **kwargs):
        self.first_name = (self.first_name).lower()
        self.last_name = (self.last_name).lower()
        self.full_name = f"{self.first_name}_{self.last_name}"
        super().save(*args, **kwargs)
