import uuid
import os

from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel


SUBJECT_CHOICES = [
    ('ASF', 'Asfalt'),
    ('AST', 'Assistent'),
    ('BES', 'Bestratingen'),
    ('BET', 'Betonboren'),
]

LEVEL_CHOICES = [
    ('1', 'Niveau 1'),
    ('2', 'Niveau 2'),
    ('3', 'Niveau 3'),
    ('4', 'Niveau 4'),
]

FILE_TYPE_CHOICES = [
    ('3DB', '3D-beeld'),
    ('ANI', 'Animaties'),
    ('DID', 'Didactische werkvorm'),
    ('GRO', '(Groeps)opdracht'),
    ('PRE', 'Presentatie'),
    ('TOE', 'Toets'),
    ('NVT', 'N.v.t.'),
]

def article_file_path(instance, filename):
    """Generate file path for uploaded file"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('files/article-files/', filename) 

def article_image_path(instance, filename):
    """Generate file path for uploaded image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('images/article-images/', filename) 


class Tag(TimeStampedModel):
    """tags used for article"""
    name = models.CharField(max_length=50)


class Article(TimeStampedModel):
    """Model for the user uploaded articles"""
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_desc = CharField(max_length=120)
    long_desc = models.TextField(max_length=1500, blank=True)
    image = models.ImageField(upload_to=article_image_path)
    uploaded_file = models.FileField(upload_to=article_file_path)
    user_likes = models.ManyToManyField(User, blank=True)
    subject = models.CharField(
        max_length=3, choices=SUBJECT_CHOICES, default='ASF'
    )
    level = models.CharField(
        max_length=1, choices=LEVEL_CHOICES, default='1'
    )
    tags = models.ManyToManyField(Tag, blank=True)
    file_type = models.CharField(
        max_length=3, choices=FILE_TYPE_CHOICES, default='3DB'
    )
    is_public = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    downloads = models.ManyToManyField(User, blank=True)