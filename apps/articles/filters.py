"""
Filters for articles
"""
from django import forms
from articles import models
from articles.models import Article
import django_filters


class ArticleFilter(django_filters.FilterSet):
    """
    Filter for article list
    """
    file_type = django_filters.MultipleChoiceFilter(
        choices=models.FILE_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Article
        fields = ["subject", "level", "file_type", ]
