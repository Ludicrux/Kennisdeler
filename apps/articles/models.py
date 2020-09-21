"""
Models for user uploaded articles
"""

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify

from django_extensions.db.models import TimeStampedModel


SUBJECT_CHOICES = [
    ("ASF", "Asfalt"),
    ("AST", "Assistent"),
    ("BES", "Bestratingen"),
    ("BET", "Betonboren"),
]

LEVEL_CHOICES = [
    (1, "Niveau 1"),
    (2, "Niveau 2"),
    (3, "Niveau 3"),
    (4, "Niveau 4"),
]

FILE_TYPE_CHOICES = [
    ("3DB", "3D-beeld"),
    ("ANI", "Animaties"),
    ("DID", "Didactische werkvorm"),
    ("GRO", "(Groeps)opdracht"),
    ("PRE", "Presentatie"),
    ("TOE", "Toets"),
    ("NVT", "N.v.t."),
]


class Tag(TimeStampedModel):
    """tags used for article"""
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f"{self.name}"


class Article(TimeStampedModel):
    """Model for the user uploaded articles"""
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_desc = models.CharField(max_length=120)
    long_desc = models.TextField(max_length=1500, blank=True)
    image = models.ImageField(upload_to="images/article-images/")
    uploaded_file = models.FileField(upload_to="documents/article-documents/")
    user_likes = models.ManyToManyField(
        User, blank=True, related_name="user_likes"
    )
    subject = models.CharField(
        max_length=3, choices=SUBJECT_CHOICES, default="ASF"
    )
    level = models.IntegerField(
        choices=LEVEL_CHOICES, default=1
    )
    tags = models.ManyToManyField(Tag, blank=True)
    file_type = models.CharField(
        max_length=3, choices=FILE_TYPE_CHOICES, default="3DB"
    )
    is_public = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    downloads = models.ManyToManyField(
        User, blank=True, related_name="user_downloads"
    )

    class Meta:
        verbose_name = "Artikel"
        verbose_name_plural = "Artikelen"

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("articlepage", args=[self.slug])

    def save(self, *args, **kwargs):
        """Slugify the title and save it"""
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
