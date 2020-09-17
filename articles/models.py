#
from django.db import models
from django.contrib.auth.models import User

#
from django_extensions.db.models import TimeStampedModel


class Tag(TimeStampedModel):
    """
    tags for the article
    """
    name = models.CharField(max_length=50)


class Article(TimeStampedModel):
    """
    Model for the user uploaded articles
    """
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_desc = CharField(max_length=120)
    long_desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='', blank=True)
    uploaded_file = models.FileField(upload_to='', blank=True)
    user_likes = models.ManyToManyField(User, related_name='user_likes', help_text)
    subject = models.CharField(max_length=25)
    level = models.CharField(max_length=25)
    tags = models.ManyToManyField(Tag, related_name='tags')
    file_type = models.CharField(max_length=50)
    is_public = models.BooleanField(default=0)
    views = models.IntegerField()
    downloads = models.IntegerField()
