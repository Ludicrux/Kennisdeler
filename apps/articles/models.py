"""
Models for user uploaded articles
"""

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField
from django_resized import ResizedImageField

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

    class Meta:
        """META"""
        verbose_name = "Opleiding"
        verbose_name_plural = "Opleidingen"

    def __str__(self):
        """Returns name stirng"""
        return f"{self.name}"

    def save(self, *args, **kwargs):
        """save function override"""
        # Image resizing
        img = Imaging(self.image)
        img.resize_by_max(new_height=300)
        self.image = img.save_image()

        super().save(*args, **kwargs)


class Tag(TimeStampedModel):
    """Tags used for article"""
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        """META"""
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        """Returns name stirng"""
        return f"{self.name}"


class Article(TimeStampedModel):
    """Model for the user uploaded articles"""
    title = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from=['title'], unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_desc = models.CharField(max_length=120)
    long_desc = models.TextField(max_length=1500, blank=True)
    image = ResizedImageField(
        quality=100,
        size=[1000, 500],
        upload_to="images/article-images",
    )
    thumb = ResizedImageField(
        quality=100,
        size=[40, 40],
        crop=["middle", "center"],
        blank=True,
        upload_to="images/article-thumbnail",
    )
    uploaded_file = models.FileField(
        upload_to="documents/article-documents",
        blank=True
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
    user_favorites = models.ManyToManyField(
        User,
        blank=True,
        through="Favorite",
        related_name="user_favorites"
    )

    class Meta:
        """META"""
        verbose_name = "Artikel"
        verbose_name_plural = "Artikelen"

    def __str__(self):
        """return the string title"""
        return f"{self.title}"

    def get_absolute_url(self):
        """returns url for for the detail view"""
        return reverse(
            "articles:article-detail",
            kwargs={'slug': str(self.slug)}
        )

    def get_absolute_url_edit(self):
        """returns the url for the edit view"""
        return reverse(
            "articles:article-edit",
            kwargs={'slug': str(self.slug)}
        )


class Like(TimeStampedModel):
    """Model to filter the article by popularity"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        """META"""
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        """returns the creation datetime"""
        return f"{self.created}"


class Favorite(TimeStampedModel):
    """Model to allow sorting of favorites by most recent"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        """META"""
        verbose_name = "Favoriet"
        verbose_name_plural = "Favorieten"

    def __str__(self):
        """returns the creation datetime"""
        return f"{self.created}"
