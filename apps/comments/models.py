"""
Models for user written comments
"""

from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel

from articles.models import Article


class Comment(TimeStampedModel):
    """Comments left by users on articles"""
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )
    message = models.TextField(max_length=257)
    seen = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.message}"
