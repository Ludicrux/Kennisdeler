"""
Models for user uploaded articles
"""

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from lib.images import Imaging


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


class Subject(TimeStampedModel):
    """Subjects used for the article"""
    name = models.CharField(max_length=25, unique=True)
    image = models.ImageField(upload_to="images/subject-images/")

    def __str__(self):
        return f"{self.name}"


class Tag(TimeStampedModel):
    """Tags used for article"""
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f"{self.name}"


class Article(TimeStampedModel):
    """Model for the user uploaded articles"""
    title = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from=['title'], unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_desc = models.CharField(max_length=120)
    long_desc = models.TextField(max_length=1500, blank=True)
    image = models.ImageField(
        upload_to="images/article-images",
        verbose_name="articleimg"
    )
    uploaded_file = models.FileField(
        upload_to="documents/article-documents",
        verbose_name="articledoc"
    )
    user_likes = models.ManyToManyField(
        User, blank=True, through="Like", related_name="user_likes"
    )
    subject = models.ForeignKey(
        Subject, null=True, on_delete=models.SET_NULL
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
    downloads = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Artikel"
        verbose_name_plural = "Artikelen"

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse(
            "articles:article-detail",
            kwargs={'slug': str(self.slug)}
        )

    def get_absolute_url_edit(self):
        return reverse(
            "articles:article-edit",
            kwargs={'slug': str(self.slug)}
        )

    def save(self, *args, **kwargs):
        img = Imaging(self.image)
        img.resize_by_max(new_width=700)
        self.image = img.save_image()

        super().save(*args, **kwargs)


class Like(TimeStampedModel):
    """Model to filter the article by popularity"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.created}"
