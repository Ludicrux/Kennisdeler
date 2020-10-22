"""
Filters for articles
"""
from django import forms
from articles import models
from articles.models import Article, Subject
import django_filters


class ArticleFilter(django_filters.FilterSet):
    """
    Filter for article list
    """

    subject = django_filters.ModelChoiceFilter(
        queryset=Subject.objects.all(),
        label="Opleiding"
    )
    level = django_filters.ChoiceFilter(
        choices=models.LEVEL_CHOICES,
        label="Niveau"
    )
    file_type = django_filters.MultipleChoiceFilter(
        choices=models.FILE_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Soort document"
    )

    class Meta:
        model = Article
        fields = ["subject", "level", "file_type", ]
