"""Models for users"""
from django.db import models
from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from django_resized import ResizedImageField
from django_extensions.db.models import TimeStampedModel

from users.managers import CustomUserManager


class Profile(TimeStampedModel):
    """Profile for user"""
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    job = models.CharField(_("werkend als"), max_length=30)
    organization = models.CharField(_("organisatie"), max_length=30)
    profile_picture = ResizedImageField(
        quality=100,
        size=[50, 50],
        crop=['middle', 'center'],
        upload_to="images/user-images",
    )

    def __str__(self):
        return f"{self.user}"


class User(AbstractUser):
    """User model"""
    username = None
    email = models.EmailField('email address', unique=True)
    full_name = models.CharField("full name", max_length=50)
    slug = models.SlugField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.full_name}"

    def article_count(self):
        return f"{self.article_set.count()}"

    def get_absolute_url(self):
        """returns url for for the user"""
        return reverse(
            "users:user-article-list",
            kwargs={'slug': str(self.slug)}
        )

    def _generate_unique_slug(self):
        unique_slug = slugify(self.full_name)
        num = 1
        while User.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{unique_slug}-{num}"
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.first_name = (self.first_name).lower()
        self.last_name = (self.last_name).lower()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.slug = self._generate_unique_slug()
        super(User, self).save(*args, **kwargs)

    def profile(self):
        return get_object_or_404(Profile, user=self.id)
